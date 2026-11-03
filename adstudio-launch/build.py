#!/usr/bin/env python3
"""Builds adstudio-launch/index.html: the Ad Studio Meta launch plan (3 Nov 2026).
The ad copy is read from the CPMA repo (tenants/adstudio/launch_plan.json), the same file the agent builds the ads from,
so the page and the campaign never disagree. Run: python3 -I build.py
"""
import html, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
PLAN = os.path.expanduser("~/claude fc/ad-intel/tenants/adstudio/launch_plan.json")
plan = json.load(open(PLAN))
E = html.escape

FILMS = {
    "c01": ("Copy What Already Works", "43.7 s", "v4", "Ready with caveat", "Stat hook: a skincare ad running for two years. Ad Radar finds it, Ad Studio clones it."),
    "c08": ("Same Ad, Your Product", "55.0 s", "v4", "Ready with caveat", "Faceless explainer: Ad Radar sorted by days live, clone for my product. The only film with the $19 price."),
    "c21": ("The Cheat Code", "48.5 s", "v2", "Ready with caveat", "Creator testimonial: nine ads and a creator video in one afternoon. Says 40,000+ brands."),
    "c19": ("Two Seconds", "45.9 s", "v2, approved", "Ready with caveat", "AI presenter: your ad has two seconds to stop the thumb; the agent researches before it makes."),
    "c03": ("I'm Not Real", "46.8 s", "v4", "Ready with caveat", "Twist hook: \"this creator isn't real\". AI creators made in Ad Studio, no creator fee."),
    "c17": ("Spot the AI", "47.0 s", "v2, approved", "Ready with caveat", "Street vox pop: which creator is AI? Both are. Strongest top-of-funnel hook in the set."),
    "c01a": ("Copy What Already Works (alt cut)", "50.6 s", "alt", "Ready with caveat", "Audience call-out hook: \"Running ads for an ecommerce brand? Look at this one.\""),
    "c08a": ("Same Ad, Your Product (alt cut)", "59.3 s", "alt", "Ready with caveat", "Same story as c08 with a better first frame (the blank ad card)."),
}
HELD = [
    ("c04", "The Three Week Wait", "Not ready", "A product picker shows an unrelated catalog item with a rupee price (₹4,000/month) and em dashes at 39 to 41 s; UK-style dates (THU 28 AUG); captions at 93 to 99% of the frame. Re-cut, then add to AS2 or AS4."),
    ("c05", "Nine Ads Before Lunch", "Not ready", "Says nine ads but shows 5 + 3. The alternate cut says four winners (adds up) but may carry a stray voice tag in its last 1.5 s. Fix, then add to AS2."),
    ("c18", "Mirror Hallway", "Your call", "Multilingual presenters (ES, FR, DE, PT, EN) in European settings. Off-brief for the US-only creative rule, on-brief for this campaign's EU markets. One spoken line says \"Ad Studio by Brevo\". Candidate for AS3 in DE, FR, ES."),
]
LANGS = [("en", "English"), ("de", "Deutsch"), ("fr", "Français"), ("it", "Italiano"), ("es", "Español")]

MF = [  # MagicFit sign-up ad sets, Jul 2025 to Jul 2026, Meta insights results (MagicfitSignUp, default attribution)
    ("US", 6349, 978), ("CA", 2276, 339), ("GB", 4162, 612), ("DE", 1864, 327), ("FR", 3704, 658), ("IT", 5231, 904), ("ES", 604, 106),
]


def money(x, d=0):
    return f"${x:,.{d}f}"


def copy_block(ad):
    out = []
    tabs = "".join(f'<button class="tab{" on" if i == 0 else ""}" data-l="{k}">{E(n)}</button>' for i, (k, n) in enumerate(LANGS))
    out.append(f'<div class="tabs">{tabs}</div>')
    for i, (k, n) in enumerate(LANGS):
        c = ad["copy"].get(k)
        if not c:
            continue
        pt = "".join(f"<p>{E(line)}</p>" if line else "" for line in c["primary_text"].split("\n"))
        out.append(f'''<div class="lang" data-l="{k}"{"" if i == 0 else " hidden"}>
  <div class="field"><span>Primary text</span><div class="pt">{pt}</div></div>
  <div class="row2"><div class="field"><span>Headline ({len(c["headline"])}/40)</span><b>{E(c["headline"])}</b></div>
  <div class="field"><span>Description</span>{E(c.get("description", ""))}</div>
  <div class="field"><span>Button</span>Sign up</div></div></div>''')
    return "\n".join(out)


def adset_html(i, s):
    ads = []
    for a in s["ads"]:
        f = FILMS[a["film"]]
        ads.append(f'''<article class="ad">
  <img src="img/{a['film']}.jpg" alt="{E(f[0])} first frame" loading="lazy" width="150" height="267">
  <div class="adbody">
    <div class="adhead"><b>{E(a['film'])} · {E(f[0])}</b><span class="chip">{E(f[1])} · 9:16</span><span class="chip ok">{E(f[3])}</span></div>
    <p class="muted">{E(f[4])}</p>
    {copy_block(a)}
  </div>
</article>''')
    return f'''<section class="adset" id="{s['key']}">
  <h3>{E(s['name'])}</h3>
  {"".join(ads)}
</section>'''


tot_spend = sum(s for _, s, _ in MF)
tot_su = sum(n for _, _, n in MF)
mf_rows = "".join(f"<tr><td>{c}</td><td>{money(s)}</td><td>{n:,}</td><td><b>{money(s / n, 2)}</b></td></tr>" for c, s, n in MF)
mf_rows += f'<tr class="tot"><td>All 7</td><td>{money(tot_spend)}</td><td>{tot_su:,}</td><td><b>{money(tot_spend / tot_su, 2)}</b></td></tr>'
held_rows = "".join(f'<tr><td><img src="img/{k}.jpg" alt="" width="54" height="96" loading="lazy"></td><td><b>{k}</b> {E(t)}</td><td><span class="chip warn">{E(v)}</span></td><td>{E(w)}</td></tr>' for k, t, v, w in HELD)
adsets = "\n".join(adset_html(i, s) for i, s in enumerate(plan["adsets"]))

PAGE = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<meta name="referrer" content="no-referrer">
<title>Ad Studio Meta Launch</title>
<style>
:root{{color-scheme:light;--bg:#f6f5f2;--surface:#fcfcfb;--surface-2:#f0efec;--line:#e2e0da;--text:#121211;--text-2:#52514e;--muted:#6b6964;
--accent:#006a43;--accent-soft:#e3f1ea;--crit:#d03b3b;--crit-soft:#fbecec;--warn:#8a5a00;--warn-soft:#fdf3dc;--ok:#006300;--ok-soft:#eaf3ea;--shadow:0 1px 2px rgba(0,0,0,.04),0 2px 10px rgba(0,0,0,.04)}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{color-scheme:dark;--bg:#121211;--surface:#1a1a19;--surface-2:#232321;--line:#2f2f2c;--text:#fff;--text-2:#c3c2b7;--muted:#8f8e86;
--accent:#5fd49b;--accent-soft:#16301f;--crit:#ff8a8a;--crit-soft:#3a1c1c;--warn:#ffc95c;--warn-soft:#33270f;--ok:#5fd45f;--ok-soft:#17301a;--shadow:none}}}}
:root[data-theme="dark"]{{color-scheme:dark;--bg:#121211;--surface:#1a1a19;--surface-2:#232321;--line:#2f2f2c;--text:#fff;--text-2:#c3c2b7;--muted:#8f8e86;
--accent:#5fd49b;--accent-soft:#16301f;--crit:#ff8a8a;--crit-soft:#3a1c1c;--warn:#ffc95c;--warn-soft:#33270f;--ok:#5fd45f;--ok-soft:#17301a;--shadow:none}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--text);font:15px/1.55 Inter,system-ui,-apple-system,Segoe UI,Roboto,sans-serif}}
main{{max-width:1040px;margin:0 auto;padding:28px 16px 80px}}h1{{font-size:28px;line-height:1.2;margin:0 0 6px;letter-spacing:-.01em}}
h2{{font-size:20px;margin:40px 0 12px;padding-top:12px;border-top:1px solid var(--line)}}h3{{font-size:16px;margin:22px 0 10px}}
p{{margin:.4em 0}}.muted{{color:var(--muted)}}.lede{{color:var(--text-2);font-size:16px;max-width:780px}}
nav.toc{{display:flex;flex-wrap:wrap;gap:6px;margin:18px 0}}nav.toc a{{font-size:13px;padding:5px 10px;border:1px solid var(--line);border-radius:999px;color:var(--text-2);text-decoration:none;background:var(--surface)}}
.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:10px}}.kpi{{background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:12px 14px;box-shadow:var(--shadow)}}
.kpi span{{display:block;font-size:12px;color:var(--muted);text-transform:uppercase;letter-spacing:.04em}}.kpi b{{font-size:20px}}
.card{{background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:14px 16px;margin:10px 0;box-shadow:var(--shadow)}}
.blk{{border-left:4px solid var(--crit);background:var(--crit-soft)}}.wrn{{border-left:4px solid var(--warn);background:var(--warn-soft)}}.okc{{border-left:4px solid var(--ok);background:var(--ok-soft)}}
.card h4{{margin:0 0 4px;font-size:15px}}.card ol,.card ul{{margin:.3em 0 .3em 1.2em;padding:0}}.owner{{font-size:12px;color:var(--muted)}}
table{{width:100%;border-collapse:collapse;background:var(--surface);border:1px solid var(--line);border-radius:10px;overflow:hidden;font-size:14px}}
th,td{{text-align:left;padding:8px 10px;border-bottom:1px solid var(--line);vertical-align:top}}th{{background:var(--surface-2);font-size:12px;text-transform:uppercase;letter-spacing:.03em;color:var(--muted)}}
tr.tot td{{background:var(--accent-soft)}}.tw{{overflow-x:auto}}
.chip{{display:inline-block;font-size:12px;padding:2px 8px;border-radius:999px;background:var(--surface-2);color:var(--text-2);margin-left:6px;white-space:nowrap}}
.chip.ok{{background:var(--ok-soft);color:var(--ok)}}.chip.warn{{background:var(--warn-soft);color:var(--warn)}}.chip.crit{{background:var(--crit-soft);color:var(--crit)}}
.adset{{background:var(--surface-2);border-radius:12px;padding:4px 14px 10px;margin:14px 0}}
.ad{{display:flex;gap:14px;background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:12px;margin:10px 0}}
.ad img{{width:150px;height:auto;border-radius:8px;flex:none;align-self:flex-start;background:#000}}.adbody{{flex:1;min-width:0}}
.adhead{{display:flex;flex-wrap:wrap;align-items:center;gap:4px;margin-bottom:4px}}
.tabs{{display:flex;flex-wrap:wrap;gap:4px;margin:8px 0}}.tab{{font:inherit;font-size:12px;padding:3px 9px;border-radius:6px;border:1px solid var(--line);background:var(--surface-2);color:var(--text-2);cursor:pointer}}
.tab.on{{background:var(--accent);border-color:var(--accent);color:#fff}}.field{{margin:6px 0}}.field>span{{display:block;font-size:11px;text-transform:uppercase;letter-spacing:.04em;color:var(--muted)}}
.pt p{{margin:0 0 .5em}}.row2{{display:grid;grid-template-columns:2fr 1.4fr .8fr;gap:10px}}
code{{font:12.5px ui-monospace,SFMono-Regular,Menlo,monospace;background:var(--surface-2);padding:1px 5px;border-radius:4px}}
a{{color:var(--accent)}}
@media (max-width:640px){{.ad{{flex-direction:column}}.ad img{{width:120px}}.row2{{grid-template-columns:1fr}}h1{{font-size:23px}}}}
</style>
</head>
<body>
<main>
<p class="muted">Brevo Ad Studio (ads.brevo.com, formerly MagicFit) · Meta · prepared 3 Nov 2026 · built on CPMA</p>
<h1>Ad Studio Meta launch: plan, blockers and copy</h1>
<p class="lede">One campaign at $100 a day across the US, Canada, the UK, Germany, France, Italy and Spain, on the PushOwl ad account. Four ad sets, one per core promise, eight approved films, optimised to the Ad Studio sign-up. Everything is built in CPMA's new Ad Studio silo and is created paused. Two things block the launch today; both are listed first.</p>
<nav class="toc"><a href="#status">Status</a><a href="#blockers">Blockers</a><a href="#history">MagicFit history</a><a href="#tracking">Tracking audit</a><a href="#setup">Campaign settings</a><a href="#copy">Ad sets and copy</a><a href="#films">Film review</a><a href="#languages">Languages and dubbing</a><a href="#cpma">CPMA and dashboard</a><a href="#optimise">Optimisation</a><a href="#decisions">Your decisions</a></nav>

<h2 id="status">Status</h2>
<div class="grid">
<div class="kpi"><span>Daily budget</span><b>$100</b><p class="muted">one campaign budget</p></div>
<div class="kpi"><span>Ad sets / ads</span><b>4 / 8</b><p class="muted">2 films per promise</p></div>
<div class="kpi"><span>Target cost per sign-up</span><b>$6.50</b><p class="muted">ceiling $10 (MagicFit history $6.16)</p></div>
<div class="kpi"><span>Expected sign-ups</span><b>about 15 a day</b><p class="muted">at the target, before BFCM CPM inflation</p></div>
</div>
<div class="card okc"><h4>Done today</h4><ul>
<li>Audited the pixel, the site's events, PostHog and 16 months of MagicFit campaigns (one-off Meta read, 10 read-only calls, no writes).</li>
<li>Watched all 9 films and 5 alternates frame by frame (OCR, transcripts, loudness, safe zones): 8 cleared for launch, 3 held.</li>
<li>Wrote the copy for 4 ad sets and 8 ads in English, German, French, Italian and Spanish.</li>
<li>Added ads.brevo.com to the pixel's traffic permissions allow list; Meta now receives browser events from the site.</li>
<li>Built the campaign on Meta, paused: 1 campaign, 4 ad sets, 8 ads, the sign-up exclusion audience. Live since 10:45 pm IST on your Go live.</li>
<li>Built and deployed the Ad Studio silo on CPMA: its own database, storage and queues on the shared PushOwl account, with the 8 films in its Library, the plan saved and a dry-run check that names exactly what still blocks it.</li>
</ul></div>

<h2 id="blockers">Blockers</h2>
<div class="card okc"><h4>1. Fixed 3 Nov: ads.brevo.com is on the pixel's allow list</h4>
<p>The site loads the same pixel MagicFit used (<code>569439912209998</code>, "PushOwl Pixel"), but its traffic permissions left out ads.brevo.com, so Meta dropped every browser event there. With your OK I added <code>ads.brevo.com and subdomains</code> to the allow list (Events Manager, PushOwl Pixel, Settings, Traffic permissions). Meta now serves the domain the full pixel config (446 KB, the same as pushowl.com, instead of the 46 KB blocked one), and a test visit fired <code>MagicfitPageView</code> to Meta. PageViews, the click ID cookie and the retargeting pool now build from today.</p>
<p class="owner">CPMA re-checks this before every build and refuses if it ever regresses.</p></div>
<div class="card okc"><h4>2. Live since 3 Nov, 17:15 UTC (10:45 pm IST)</h4>
<p>You released the hold and asked for the build at once, so it ran outside the call windows under a one-off, logged exception (47 Meta calls, 30 writes, all succeeded). On Meta: campaign <code>120251179707980614</code> (PAUSED, $100/day campaign budget, lowest cost), 4 ad sets optimising to <code>MagicfitSignUp</code> with the 7 countries, open audience, Facebook and Instagram, existing sign-ups excluded (audience <code>120251179656850614</code>), and 8 ads with every Advantage+ creative enhancement off and UTMs on. Meta is reviewing the ads now.</p>
<p class="owner">You approved Go live in chat; the card switched on 13 objects (8 ads, 4 ad sets, the campaign). The ads deliver as Meta approves each one. CPMA's Ad Studio loop judges them in the 09:00 and 17:00 IST windows from day 3.</p></div>
<div class="card wrn"><h4>3. The live site contradicts the free allowance</h4>
<p>ads.brevo.com says "3 Free generations, one-time" and, elsewhere on the same page, "You get 2 free generations to try out Ad Studio". Every film and every ad promises 3. Fix the "2" line before traffic arrives.</p><p class="owner">Owner: Ad Studio web team.</p></div>
<div class="card wrn"><h4>4. Confirm a UGC video counts as one of the 3 free ads</h4>
<p>Ad set 3 promises "your first UGC creator free". PostHog shows Free-plan users whose first generation was a <code>VIDEO_AD</code> (65 to 75 credits), which supports it, but the plan's exact rule (3 generations or a credit amount) should be confirmed.</p><p class="owner">Owner: Ad Studio product.</p></div>
<div class="card wrn"><h4>5. Server-side sign-up event: confirm it carries click IDs</h4>
<p><code>MagicfitSignUp</code> reaches the pixel server-side (1:1 with PostHog <code>SignUp</code>: 15 and 15 since 20 Oct). For Meta to credit the right ad it needs <code>fbc</code>/<code>fbp</code>, hashed email, IP, user agent, <code>event_id</code> and <code>event_source_url</code>. The browser click ID cookie (<code>_fbc</code>) is set on ads.brevo.com since the 3 Nov fix, so the server event can pass it on.</p><p class="owner">Owner: Ad Studio engineering.</p></div>
<div class="card wrn"><h4>6. Page name</h4>
<p>MagicFit ads ran from Page <code>1211654965361602</code> and Instagram <code>17841480099076355</code>. The plan uses them; the Page name shows on every ad, so it should read Brevo Ad Studio (or Ad Studio by Brevo).</p><p class="owner">Owner: Farooq.</p></div>
<div class="card wrn"><h4>7. Safe zones (not a launch blocker)</h4>
<p>Most films put captions or stickers in the bottom 20% or top 14% of the frame, which the Reels interface covers and a 4:5 feed crop cuts. All films are 9:16 only. They launch as approved; the fix (captions raised to about 70%) folds into the dubbing re-renders, so each film is re-rendered once.</p></div>

<h2 id="history">MagicFit history (Jul 2025 to Jul 2026)</h2>
<p>MagicFit spent about $36.5k on this account across 45 campaigns. The sign-up ad sets ran open (Advantage+ audience, no interests) in the same countries, optimised to the custom pixel event <code>MagicfitSignUp</code>, with 7-day click, 1-day view and 1-day engaged-view attribution. Cost per sign-up in the seven launch countries:</p>
<div class="tw"><table><thead><tr><th>Country</th><th>Spend</th><th>Sign-ups</th><th>Cost per sign-up</th></tr></thead><tbody>{mf_rows}</tbody></table></div>
<p class="muted">English ads in Germany, France, Italy and Spain were the cheapest (about $5.70), so English-first in Europe is a sound start. The paid conversions those campaigns reported were near zero (<code>MagicfitPayment</code> about 11); the business problem was paid conversion, not sign-up cost, so CPMA reports activation and payment next to sign-ups.</p>

<h2 id="tracking">Tracking audit</h2>
<div class="tw"><table><thead><tr><th>Event</th><th>Where it comes from</th><th>Last 2 weeks</th><th>Use</th></tr></thead><tbody>
<tr><td><code>MagicfitSignUp</code></td><td>Server-side, one per new self-serve account (matches PostHog <code>SignUp</code> 1:1)</td><td>15</td><td><b>Optimise to this</b></td></tr>
<tr><td><code>MagicfitEnhancedSignUp</code></td><td>Server-side after onboarding plus a first generation; includes accounts created through the Brevo and PushOwl integrations</td><td>98</td><td>Report as activation</td></tr>
<tr><td><code>MagicfitPayment</code></td><td>Server-side, paid plan</td><td>3</td><td>Report as paid</td></tr>
<tr><td><code>MagicfitPageView</code></td><td>Browser, every route change (sent with <code>track</code> instead of <code>trackCustom</code>; Meta warns but records it)</td><td>9,309 (none from ads.brevo.com before the 3 Nov fix)</td><td>Retargeting pool, building since 3 Nov</td></tr>
<tr><td>PageView</td><td>Not fired by the site's own code</td><td>n/a</td><td>Optional: add it to the base snippet</td></tr>
</tbody></table></div>
<p class="muted">Also on the site: GA4 <code>G-4YSSQVK9D4</code>, PostHog, Axon (sign_up and purchase), Tolt. The server stores the first-touch UTMs in a <code>__utm</code> cookie and on the PostHog <code>SignUp</code>, so every ad carries UTMs. The home page already runs the three-way landing test (winners, agent, current) by cookie, and the old test pages on pages.dev have no pixel at all, so the ads go to ads.brevo.com.</p>

<h2 id="setup">Campaign settings</h2>
<div class="tw"><table><tbody>
<tr><th>Ad account</th><td>Brevo PushOwl <code>act_1068538947813085</code> (USD). Runs next to the BFCM campaign; BFCM's dashboard and guards only count campaigns named BFCM, and PushOwl's CPMA silo excludes anything named MF or Ad Studio.</td></tr>
<tr><th>Campaign</th><td><code>{E(plan["campaign"]["name"])}</code> · Sales objective · auction · no special ad category</td></tr>
<tr><th>Budget and bid</th><td>Campaign budget (Advantage+) $100 a day · highest volume (lowest cost, no cap) · Meta shifts budget between the four ad sets</td></tr>
<tr><th>Conversion</th><td>Website · PushOwl Pixel <code>569439912209998</code> · custom event <code>MagicfitSignUp</code> · maximise conversions</td></tr>
<tr><th>Attribution</th><td>7-day click, 1-day view, 1-day engaged view (the same as MagicFit, so results compare)</td></tr>
<tr><th>Audience</th><td>Open: Advantage+ audience, no interests · US, CA, GB, DE, FR, IT, ES · people living in or recently in · 18 to 65+ · all genders · all languages</td></tr>
<tr><th>Exclusion</th><td>New audience "AGENT · Ad Studio sign-ups · MagicfitSignUp · 180d", created at build and confirmed in CPMA before Go live</td></tr>
<tr><th>Placements</th><td>Facebook and Instagram only (feeds, Stories, Reels, Explore); no Audience Network, Messenger or Threads</td></tr>
<tr><th>Identity</th><td>Page <code>1211654965361602</code> · Instagram <code>17841480099076355</code> (the MagicFit accounts; see blocker 6)</td></tr>
<tr><th>Ads</th><td>Single video, 1080x1920, our own poster frame as thumbnail (covers c03's black first frame) · button: Sign up · link <code>{E(plan["link"])}</code></td></tr>
<tr><th>URL parameters</th><td><code>{E(plan["url_tags"])}</code></td></tr>
<tr><th>Before Go live</th><td>In Ads Manager, open each ad's preview: switch off Advantage+ creative enhancements that alter a finished film (music, visual touch-ups, text overlays, auto-cropping); keep relevant comments. Turn off multi-advertiser ads.</td></tr>
</tbody></table></div>

<h2 id="copy">Ad sets and copy</h2>
<p>Each ad set carries one promise, and its copy leads with it. The films all close on "Start for free. Your first 3 ads are free", so the copy adds the angle the film doesn't say out loud. Every claim is on the live site: 40,000+ brands, plans from $19 a month, no credit card required, 3 free generations, Ad Radar, cloning around your product, brand and offer, AI presenters with captions. No em dashes, no "Shopify". The language tabs hold the translations for the dubbed versions; until those are approved, English runs everywhere.</p>
{adsets}

<h2 id="films">Film review</h2>
<p>All 9 films and the 5 alternate cuts were checked at full resolution: OCR on every frame at 2 fps, word-timed transcripts, an isolated listen to every "Brevo", loudness (-16 LUFS throughout), black and frozen frames, and safe zones measured from the text positions. No film says Shopify or Klaviyo, shows the admin-only Workflow, or uses a non-USD price apart from c04. Voice pace is 3.4 to 3.9 words a second. Held from the launch:</p>
<div class="tw"><table><thead><tr><th></th><th>Film</th><th>Status</th><th>Why</th></tr></thead><tbody>{held_rows}</tbody></table></div>
<p class="muted">Claims in the films worth a product check (not blocking): "launch it in seconds" and the 3-second LIVE timer (c01, c08); "anything live past 60 days is a proven seller" (c01, c05, c08); "any voice, in any language" (the UI lists about 12 languages); "no creator fee" while generation costs credits (c03); c21 says "TikTok" on a Meta ad.</p>

<h2 id="languages">Languages and dubbing</h2>
<p>You asked for translated text and dubbed audio in Germany, France, Italy and Spain. The copy is translated (tabs above). For the audio:</p>
<ol>
<li><b>Launch English everywhere first.</b> MagicFit's English ads got its cheapest sign-ups in exactly those four countries, so nothing waits on the dubs.</li>
<li><b>Dub one hero film per ad set</b> (c01, c21, c17, c08a), one film and one language at a time for your approval: translated script, the same presenter's voice cloned in the target language, lip-sync on the on-camera takes, captions re-rendered in the language and raised out of the Reels zone. Pilot: c17 in German.</li>
<li><b>Add them as language versions of the same ads</b> (Meta's language customisation: English by default, German, French, Italian and Spanish served by the viewer's language), so the ads keep their history and the campaign stays one campaign.</li>
</ol>

<h2 id="cpma">CPMA and the dashboard</h2>
<ul>
<li><b>A third silo:</b> Ad Studio runs as its own CPMA deployment (<code>cpma-adstudio</code>) with its own database, storage and queues, the same way Vital Vogue does. Pick <b>Ad Studio</b> in the brand switcher at <a href="https://cpma-agent.pages.dev/brand/adstudio">cpma-agent.pages.dev</a>.</li>
<li><b>Shared account, split cleanly:</b> the PushOwl silo drops every MagicFit or Ad Studio campaign (by name, or because its ad sets optimise to a Magicfit event); the Ad Studio silo keeps only those. Each silo can write only to objects it tracks, so neither can touch the other's campaigns.</li>
<li><b>Conversions:</b> sign-ups are read from Meta's <code>conversions</code> field (custom events are only named there); headline metric is cost per sign-up (CPS), with a $6.50 target and a $10 ceiling, provisional until two weeks of data.</li>
<li><b>History:</b> MagicFit's campaigns since Jul 2025 load into the Ad Studio dashboard in tomorrow's 09:00 IST window (queued), so the Command Center opens with the baseline above.</li>
<li><b>Launch flow:</b> the plan check at <code>GET /api/adstudio/plan</code> lists what blocks; the build (<code>POST /api/adstudio/build</code>) runs in the next Meta window, uploads the films, creates the exclusion audience, campaign, ad sets, creatives and ads, all paused, and posts a Go live card with thumbnails. Approving that card is the only switch that spends.</li>
<li><b>Its own loop:</b> after each sync window, the Ad Studio program loop judges the launch ads (the evergreen engine skips program campaigns, as it does for BFCM), pauses clear losers and raises cards. See Optimisation.</li>
<li><b>Off in this silo:</b> PushOwl's BFCM jobs and the evergreen weekly test batch (logged as skipped); production is on hold, so the agent renders nothing for Ad Studio unless you ask.</li>
</ul>

<h2 id="optimise">Optimisation</h2>
<div class="tw"><table><thead><tr><th>When</th><th>What CPMA does</th></tr></thead><tbody>
<tr><td>Days 1 to 3</td><td>Learning: no changes. Syncs at 09:00 and 17:00 IST; flags delivery, CPM by country and early hook rates.</td></tr>
<tr><td>Day 3 on</td><td>The Ad Studio loop judges every ad in each window with CPMA's usual maths. It pauses an ad after about $16 with no sign-up (2.5x the target), or once it has 3+ sign-ups and under a 10% chance of beating $6.50. Pauses are automatic within the guardrails (10 a day, kill switch), never the last live ad in an ad set; those become cards.</td></tr>
<tr><td>Day 7</td><td>Review by promise: keep the best two or three ad sets, move the winning films into them, add c04 and c05 once re-cut and the first dubbed versions.</td></tr>
<tr><td>Scaling</td><td>An ad with 10+ sign-ups and an 80% chance of beating $6.50 raises a card to lift the campaign budget 20% (72 hours apart). Only you approve raises.</td></tr>
<tr><td>Also tracked</td><td>Activation rate (MagicfitEnhancedSignUp per sign-up), paid plans (MagicfitPayment), hook rate, CTR, and CPM per country. BFCM week (20 Nov to 1 Dec) will lift CPMs; the $10 ceiling covers it.</td></tr>
</tbody></table></div>

<h2 id="decisions">Your decisions</h2>
<ol>
<li>c18 Mirror Hallway: allowed for the European countries (it breaks the US-only creative rule on purpose)?</li>
<li>Start the dubbing pilot (c17 in German) in its own session.</li>
</ol>
<p class="muted">Sources: Meta Graph API (act_1068538947813085, pixel 569439912209998), PostHog project 195917, the live ads.brevo.com pages and Meta's pixel config, the film audit in ads-brevo-meta-launch/creatives/REVIEW.md, and the CPMA repo (branch cpma-adstudio-silo).</p>
</main>
<script>
document.querySelectorAll('.ad').forEach(function(ad){{
  ad.querySelectorAll('.tab').forEach(function(t){{
    t.addEventListener('click',function(){{
      ad.querySelectorAll('.tab').forEach(function(x){{x.classList.toggle('on',x===t)}});
      ad.querySelectorAll('.lang').forEach(function(l){{l.hidden=l.dataset.l!==t.dataset.l}});
    }});
  }});
}});
</script>
</body>
</html>
'''

for ch in ("—", "–"):
    assert ch not in PAGE, f"dash {ch!r} in page"
open(os.path.join(HERE, "index.html"), "w").write(PAGE)
print("wrote", os.path.join(HERE, "index.html"), len(PAGE), "bytes")
