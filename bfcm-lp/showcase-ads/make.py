"""Six VitalVogue BFCM showcase ads for the BFCM 2026 landing page ("Your Black Friday ads, ready in one click").
Each ad = one ranked library template (read only, via bake12 rich baking with the styles.py contract first),
VitalVogue's own Black Friday / Cyber Monday copy written to that template's observed copy sequence, and the
real VitalVogue packshot passed as a reference image. GPT Image 2 via MagicFit.

python3 make.py --prompts          write prompts/ only
python3 make.py [ids...]           render (next attempt number) into renders/<id>-<n>.png, log to ledger.json
"""
import csv, json, os, sys, time, threading, urllib.request
from concurrent.futures import ThreadPoolExecutor

D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, "/Users/farooq.chisty/claude fc/bfcm-2026-deck/creative")
import libbake                                   # read-only bridge to bake12 + styles.py
from libbake import bake, bake12, STYLES
ALL = {r["Template ID"]: r for r in csv.DictReader(open(bake.RANK))}   # all rows (libbake.ROWS drops testimonials)

sys.path.insert(0, "/Users/farooq.chisty/claude fc/caas-daily")
import magicfit_provider as mf
mf.EMAIL = "sheik.farooq@pushowl.com"
EST_USD = 0.211                                   # gpt-image-2 high list price per image (estimate; MagicFit reports none)

BRAND = ("VitalVogue (vitalvogue.in), a real Indian direct-to-consumer shapewear brand whose tagline is HER SECRETS. "
         "Prices are in Indian rupees with the rupee sign. Its Black Friday sale this year is 40 percent off every shaper "
         "from Black Friday through Cyber Monday")

LOGO = ("LOGO PLACEHOLDER: {where}, a perfectly flat, front-facing rectangle of pure chroma-key green #00FF00, about "
        "{w} by {h} pixels, evenly lit, nothing inside it, no border, no shadow across it, nothing overlapping it. "
        "It is the only pure green thing in the image. Do not write the brand name anywhere else as a logo.")

CANVAS = """CANVAS AND TYPE
- Square, 2048 by 2048. This is a finished paid social ad that will be seen at about 400 pixels wide on a phone, so type is big: the hook's letters are tall enough to read at thumbnail size, subheads are clearly smaller than the hook, and every other line of text is still large and comfortably legible on a phone. No fine print.
- Keep every word and the logo placeholder at least 6 percent of the width away from all four edges. Backgrounds and photos may bleed to the edges, text never does.
- Tile the frame: every zone of the square carries something (product, copy, a card, a band). No large empty areas."""

RULES = """RULES FOR THE WHOLE IMAGE
- Every word in the image is one of the exact copy lines above, spelled exactly as written, in correct English. No other words, letters or numbers anywhere: nothing on clothing, walls, props or packaging unless listed.
- The product matches the attached reference photo exactly: same garment, same colour, same cut, same proportions. Show it sharp and clearly visible. The reference photo's own background and any text in it are not part of the ad.
- No faces anywhere. When the product is shown worn, crop the body at the neck or below so no face is ever visible.
- No real third-party brand names, logos, publications or studies. Never render a long dash. Never print a pixel size, a colour code, a percentage of the canvas or an instruction as text.
- Text is crisp, correctly kerned and evenly baselined, with strong contrast against what sits behind it."""

T = {
    "offer": "original_winning_ads-DbBXGWAt9Qh-103-birthday-discount-offer-first-pet-food",
    "usvsthem": "original_winning_ads-DatilwrMxh3-58-hair-serum-us-vs-other-comparison",
    "review": "original_winning_ads-DaQEYVBoo5b-4-testimonial-capsule-daily-dose-social-proof",
    "imessage": "original_winning_ads-DbSNmTbIrQb-11-proposal-text-message-story",
    "callouts": "original_winning_ads-DbHUw-Vq82v-7-melatonin-patch-benefits-handheld-pack",
    "countdown": "original_winning_ads-DbXdEgqoduW-8-handwritten-debloat-countdown-offer",
}

PRODUCTS = {
    "stack": ("the attached photo shows three VitalVogue products side by side: a black saree shapewear skirt (tapered, floor length, "
              "drawstring waist), black high-waisted tummy tucker shaper shorts, and grey high-waist tummy control underwear with a "
              "honeycomb knit panel. Show all three exactly as photographed, each cropped below the waist or on a body cropped at the "
              "waist, never with a face", ["stack3.jpg"]),
    "saree": ("the attached photo shows the VitalVogue Saree Shapewear: a black, floor-length, tapered stretch skirt with a drawstring "
              "waist and a fishtail flare at the hem, worn on a body cropped at the waist", ["saree.jpg"]),
    "shorts": ("the attached photo shows the VitalVogue Tummy Tucker Shaper Shorts: black, high-waisted, mid-thigh length, seamless "
               "compression shorts", ["shorts.jpg"]),
    "underwear": ("the attached photo shows the VitalVogue Tummy Control and Hip Lifting Underwear: grey, very high-waisted seamless "
                  "briefs with a wide waistband and a honeycomb knit tummy panel", ["underwear.jpg"]),
    "belt": ("the attached photo shows the VitalVogue Tummy Tucker Belt: a nude beige waist shaper wrap with long vertical rows of "
             "hook-and-eye closures down the front and soft stretch fabric", ["belt.jpg"]),
}

# id: (template key, product key, format label, BFCM moment, job, why this template, palette,
#      exact copy as (surface, words) pairs, art direction, logo slot (where, w, h) or None, logo variant, alt text)
ADS = {
"vv-01": ("offer", "stack", "Offer poster", "Black Friday launch",
    "Announce the sale like an occasion, with the price floor and the reasons to believe in one card",
    "Offer-first promotion card (Offer and Promotional, score 89.5): an occasion headline, a price burst, benefit bullets and a product stack, built for exactly this kind of dated sale",
    "warm grey #D3CCC3 ground, sunflower yellow #FFC629 headline and burst, ink black #1E1B1A body type, one plum #9B046F accent on the button",
    [("huge headline across the top third, heavy rounded sans in sunflower yellow with a thick ink-black outline and a hard ink drop shadow, on two lines", "IT'S BLACK FRIDAY!"),
     ("bold ink-black subhead directly under the headline", "40% off every shaper this week"),
     ("a big round sunflower-yellow starburst price badge, slightly rotated, overlapping the product stack's top right, ink-black type, two lines: a small word then a big price", "from ₹389"),
     ("benefit bullet one, ink black with a round yellow check icon, left column", "Seamless, no visible lines"),
     ("benefit bullet two, same style", "Stays up, no roll-down"),
     ("benefit bullet three, same style", "Sizes S to 3XL"),
     ("benefit bullet four, same style", "Delivered across India in 3-5 days"),
     ("a plum rounded button at the bottom left with white bold text", "Shop the sale")],
    "Layout: headline band across the top; below it, the left 45 percent holds the four benefit bullets stacked with even spacing and the button; the right 55 percent holds the product stack, the three products standing side by side and slightly overlapping like a lineup, large, filling that area from the subhead down to the bottom margin, on a soft warm-grey studio floor with gentle shadows. Flat promotional graphic design over a photographic product stack.",
    ("in the top left corner above the headline, small", 420, 256), "dark",
    "VitalVogue Black Friday offer ad: 'It's Black Friday! 40% off every shaper this week, from ₹389' beside three shapewear products"),

"vv-02": ("usvsthem", "saree", "Us vs them comparison", "Black Friday week, consideration",
    "Answer 'why not just wear my petticoat' with a side-by-side the shopper reads in one second",
    "Us-vs-them split (Comparison and Proof, score 91.2): the real product on a coloured side against an empty outline of the alternative, positives against negatives",
    "left half soft blush #F6EDEA with plum #9B046F type and plum check icons; right half cool grey #D7D7DA with charcoal #3A3A3F type and grey cross icons; a plum #9B046F bottom band with white type",
    [("left column header, bold plum, two lines, top of the left half", "VitalVogue Saree Shapewear"),
     ("right column header, bold charcoal, two lines, top of the right half", "Regular cotton petticoat"),
     ("left claim one, with a plum check icon", "Tapered, zero bulk"),
     ("left claim two, with a plum check icon, set as a small plum badge", "#1 selling in India"),
     ("right claim one, with a grey cross icon", "Adds bulk at the hips"),
     ("right claim two, with a grey cross icon", "Puffs out under silk"),
     ("right claim three, with a grey cross icon", "Bunches when you walk"),
     ("right claim four, with a grey cross icon", "Waist keeps slipping"),
     ("full-width plum bottom band, white bold type, one line", "Black Friday: now ₹599, 40% off")],
    "A vertical split straight down the middle. Left half: the saree shapewear exactly as in the reference, worn on a body cropped at the waist, standing tall and large in the centre of the half, photoreal, the two left claims beside it. Right half: an empty white outline drawing of a plain gathered cotton petticoat at the same scale, flat line art with no fill, the four right claims stacked beside it. Column headers align on one baseline; claims sit in tidy rows. The bottom band runs across both halves.",
    ("on the blush half in the top left corner above the left header, small", 380, 232), "plum",
    "VitalVogue comparison ad: saree shapewear (tapered, zero bulk, #1 selling in India) against a regular cotton petticoat, Black Friday ₹599"),

"vv-03": ("review", "shorts", "Review card", "Black Friday weekend, social proof",
    "Let a real customer's words carry the sale, with the offer in one chip",
    "Testimonial collage (Social Proof and Testimonials, score 91.2): the product held up close on a pale card with review snippets around it; the quote does the selling",
    "pale sage #DCE4D3 ground, white review cards with soft shadows, ink #2E2A39 type, sunflower #F5B700 stars, a plum #9B046F offer chip",
    [("bold ink caps headline across the top, one or two lines", "THE VIRAL TUMMY TUCKER SHORTS"),
     ("the largest text on the canvas: a big white review card in the middle right, the quote in a large ink serif with curly quote marks", "“Now I can eat at every party without worrying over my belly.”"),
     ("under the quote on the same card: a row of five gold stars, then a small ink line beside a green verified tick and a plain plum round avatar holding a simple white generic person icon", "Verified buyer, Mumbai"),
     ("a smaller white proof card, lower left, ink bold", "#1 selling women's shaper in India"),
     ("a plum rounded chip, lower right, white bold type", "Black Friday: ₹479, 40% off"),
     ("a small ink rounded button at the bottom centre with white caps", "SHOP NOW")],
    "On the left 45 percent, a photoreal hand with natural nails holds the black tummy tucker shorts up by the waistband against the sage ground, the shorts hanging open and flat to the camera, large and sharp, identical to the reference. The review card overlaps the right side of the shorts slightly, the proof card and chip sit below. Clean, airy collage layout but every zone is used.",
    ("in the top right corner above the review card, small", 360, 220), "dark",
    "VitalVogue review ad: 'Now I can eat at every party without worrying over my belly' with the black tummy tucker shorts, Black Friday ₹479"),

"vv-04": ("imessage", "saree", "Native iMessage", "Black Friday weekend, word of mouth",
    "Feel like a friend's tip, not an ad, with the product inside a real chat",
    "Native iMessage story (Native Interface Mockups, score 82.1): a meme caption over an iMessage screenshot with a typed reply in the composer",
    "iOS light mode: pure white #FFFFFF background, iMessage blue #0A84FF sent bubbles with white text, light grey #E9E9EB link preview card, black #000000 system text, grey #8E8E93 secondary text",
    [("meme caption at the very top on white, bold black sans, left aligned, two or three lines", "My cousins: How does your saree always drape so perfectly at every wedding?"),
     ("one short bold black line under the caption, left aligned", "Me:"),
     ("the iMessage conversation header, centred: the default iOS grey round contact avatar with a plain white person silhouette and below it the contact name in small black text", "Bestie"),
     ("inside the sent link preview card in the conversation, title line in bold black", "VitalVogue Saree Shapewear"),
     ("inside the same link preview card, the domain line in grey under the title", "vitalvogue.in"),
     ("a blue sent iMessage bubble under the link preview, white text", "Ordering two more before Black Friday ends."),
     ("the text typed into the iMessage composer field at the bottom, black, not yet sent", "40% off, want one?")],
    "The top 22 percent is plain white holding the caption and the Me: line in large type, like a meme post. Below it, the rest of the square is an exact iPhone Messages screenshot in light mode, edge to edge, no phone frame: a thin status bar with only the time 9:41 (the one extra text allowed in this ad), signal bars, wifi and battery (no carrier name); the conversation header with the avatar and name; then on the right side a sent link preview card whose large image is the saree shapewear photo exactly as in the reference, with the title and domain in a grey strip beneath; then the blue sent bubble; at the bottom the real iMessage composer bar with the plus button, the rounded text field containing the typed text, and the blue send arrow. Reproduce Apple's real Messages chrome, SF Pro font, bubble shapes and spacing as a genuine screenshot would look, zoomed so the message text is large. No keyboard.",
    None, None,
    "VitalVogue iMessage-style ad: a caption asking how the saree drapes so perfectly, answered with a VitalVogue Saree Shapewear link and 'Ordering two more before Black Friday ends'"),

"vv-05": ("callouts", "belt", "Product + callouts", "Cyber Monday push",
    "Show the product up close and make three concrete reasons plus the deadline offer impossible to miss",
    "Benefit-led product hero (Photographic Product and Lifestyle, score 94.5): dark photographic card, hands presenting the product, three icon claims and a CTA pill",
    "deep aubergine #231A2A ground with a soft spotlight, warm white #FAF5EE type, nude product, three plum #9B046F round icon badges, a hot magenta #B40581 CTA pill with white type",
    [("heavy condensed warm-white caps headline across the top, two lines", "THE WAIST SHAPER NOBODY SEES"),
     ("claim one on the right, warm white, beside a round plum badge with a simple line icon of a hook", "Adjustable hooks, your own fit"),
     ("claim two on the right, warm white, beside a round plum badge with a simple line icon of a leaf", "Breathable, skin-friendly fabric"),
     ("claim three on the right, warm white, beside a round plum badge with a simple line icon of a price tag", "Only ₹479 this Black Friday"),
     ("hot magenta pill button at the bottom right, white bold caps", "40% OFF TILL CYBER MONDAY")],
    "Dark photographic product-benefit card. The left 55 percent: two photoreal hands with natural nails hold the tummy tucker belt open toward the camera, showing the rows of hook-and-eye closures, large and sharp, lit by a soft spotlight against the aubergine ground, identical in colour and construction to the reference. The right 45 percent: the three claims stacked with even spacing, each with its round icon badge on the left, then the pill button. Premium, high-contrast, photographic.",
    ("in the top left corner above the headline, small", 380, 232), "light",
    "VitalVogue product ad: hands holding the nude tummy tucker belt with callouts (adjustable hooks, breathable fabric, ₹479) and '40% off till Cyber Monday'"),

"vv-06": ("countdown", "underwear", "Handwritten countdown", "Cyber Monday, final hours",
    "Create last-day urgency with a lo-fi note that feels like the founder wrote it at midnight",
    "Lo-fi handwritten offer (Handwritten Artifacts, score 93.7): a countdown hook, a struck-through price, handwritten benefits and a self-aware joke line",
    "bright white paper with faint grain, crimson red #C8102E marker for the hook and the new price, black marker for everything else, sunflower #F5B700 marker stars",
    [("big handwritten crimson marker headline across the top, one line", "Cyber Monday ends tonight."),
     ("handwritten black marker line under it, underlined twice", "Don't wait."),
     ("handwritten black marker old price, crossed out with a single red marker strike", "₹649"),
     ("big handwritten crimson marker new price next to the crossed-out price, circled", "₹389"),
     ("handwritten black marker benefit line one, left side", "Smooths your tummy,"),
     ("handwritten black marker benefit line two", "Lifts your hips,"),
     ("handwritten black marker benefit line three", "Never rolls down."),
     ("handwritten black marker proof line on the right under the photo, with five hand-drawn sunflower stars below it", "50,000+ customers"),
     ("small handwritten black marker aside at the bottom centre, in brackets", "(our designer is off for Cyber Monday)")],
    "A photographed sheet of bright white paper filling the entire frame edge to edge, shot flat from directly above in soft daylight with a faint paper grain and a very gentle shadow at one corner. All copy is real marker handwriting with natural uneven baselines, no typeset text anywhere. Upper right: the underwear product photo from the reference, printed as a glossy photo print about 30 percent of the frame wide, held by two strips of clear tape, slightly rotated. The prices sit at the left under the headline, large. The benefits run down the left, the proof and stars sit under the photo on the right, the bracketed aside at the bottom.",
    ("a small flat printed sticker stuck on the paper at the bottom right corner", 340, 208), "dark",
    "VitalVogue handwritten Cyber Monday ad: 'Cyber Monday ends tonight', ₹649 crossed out to ₹389, grey tummy control underwear photo taped to the page"),
}


# Source-ad objects that would otherwise render literally on shapewear (memory: templates naming an object render it).
SCRUB = [("a large yellow birthday headline", "a large yellow occasion headline"), ("three-product product stack", "three-product stack"),
         ("a real product product", "the real product"), ("hands opening a patch sheet", "hands presenting the product"),
         ("with a food photo and a proposal typed in the composer field", "with an attached photo and a short reply typed in the composer field"),
         ("a photorealistic translucent olive-oil capsule held between fingers", "the photorealistic product held up in a hand"),
         (" The missing numeral before 'Weeks until Summer.' appears intentional in the source creative.", ""),
         ("Source format recorded as lo-fi_handwritten_offer. ", "")]


def block(tid):
    r = ALL[tid]
    b = bake12.template_block(r)
    for a, z in SCRUB:
        b = b.replace(a, z)
    return r, STYLES[r["Style"]], b


def prompt(k):
    t, prod, fmt, moment, job, why, pal, copy, art, logo, variant, alt = ADS[k]
    r, contract, blk = block(T[t])
    pdesc, _ = PRODUCTS[prod]
    lines = "\n".join(f'{i+1}. {surf[0].upper() + surf[1:]}: "{w}"' for i, (surf, w) in enumerate(copy))
    lg = LOGO.format(where=logo[0], w=logo[1], h=logo[2]) if logo else "NO LOGO: this is a native screenshot; the brand appears only inside the link preview text."
    return f"""Finished square social media advertisement for {BRAND}. This is VitalVogue's own {moment} ad. Its job: {job}.
STYLE CONTRACT, must be visibly true: {contract}
LIBRARY TEMPLATE TO REBUILD (ranked winning-ads library, overall rank {r['Overall Rank']}, score {r['Score /100']}): {blk}
Any object, scene or category the template names belongs to its source ad; swap it for this product and its own world. The exact copy below was written to the template's copy sequence for this brand and this sale (where it adds a line for the offer, keep it); use it verbatim and nothing else.
EXACT COPY:
{lines}
ART DIRECTION: {art}
PALETTE: {pal}.
PRODUCT: {pdesc}. Keep it exactly as photographed.
{lg}
{CANVAS}
{RULES}"""


LEDGER = f"{D}/ledger.json"
_lock = threading.Lock()


def ledger():
    return json.load(open(LEDGER)) if os.path.exists(LEDGER) else {"renders": []}


def run(k, aspect="1:1"):
    p = prompt(k)
    if "—" in p or "–" in p:
        return k, "FAIL long dash in prompt"
    with _lock:
        L = ledger()
        n = 1 + sum(1 for x in L["renders"] if x["id"] == k and x.get("aspect", "1:1") == aspect)
    tag = f"{k}-{n}" if aspect == "1:1" else f"{k}-45-{n}"
    open(f"{D}/prompts/{tag}.txt", "w").write(p)
    refs = [f"{D}/refs/{f}" for f in PRODUCTS[ADS[k][1]][1]]
    t0 = time.time()
    url, err = mf.generate(p, refs=refs, aspect=aspect, resolution="2K", fmt="png")
    rec = dict(id=k, tag=tag, aspect=aspect, template=T[ADS[k][0]], refs=[os.path.basename(x) for x in refs],
               seconds=round(time.time() - t0), est_usd=EST_USD, at=time.strftime("%Y-%m-%d %H:%M:%S"))
    if url:
        dest = f"{D}/renders/{tag}.png"
        urllib.request.urlretrieve(url, dest)
        rec.update(url=url, path=dest)
    else:
        rec.update(error=str(err)[:300])
    with _lock:
        L = ledger(); L["renders"].append(rec); json.dump(L, open(LEDGER, "w"), indent=1)
    return k, rec.get("path") or rec.get("error")


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--prompts" in args:
        for k in ADS:
            open(f"{D}/prompts/{k}-preview.txt", "w").write(prompt(k))
        print("prompts written"); sys.exit()
    aspect = "1:1"
    if "--45" in args:
        aspect = "4:5"; args.remove("--45")
    want = args or list(ADS)
    with ThreadPoolExecutor(6) as ex:
        for res in ex.map(lambda k: run(k, aspect), want):
            print(res, flush=True)
