#!/usr/bin/env python3
"""Build ad-studio-statics/index.html: research wall, framework, 20 concepts.
Inputs: concepts.py, framework.html, findings.html, research/*.json (copied from the notes folder)."""
import html, json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from concepts import CONCEPTS, PILLARS, AWARE  # noqa: E402

E = html.escape
GROUPS = [
    ("group-a-ai-ads", "AI ad and video tools"),
    ("group-b-ai-saas", "AI assistants and SaaS"),
    ("group-c-ai-creative", "AI creative tools"),
]
SCORE_KEYS = [("h", "Headline", 25), ("bi", "Big idea", 15), ("st", "Stop", 20), ("cl", "Clarity", 15),
              ("cr", "Credible", 10), ("mi", "Minimal", 10), ("di", "Distinct", 5)]
TOP = [7, 13, 1, 3, 15, 4, 17, 19, 11, 2]


def load_refs():
    out = []
    for key, label in GROUPS:
        p = HERE / "research" / f"{key}.json"
        if not p.exists():
            continue
        for r in json.loads(p.read_text()):
            img = r.get("img") or ""
            if not img or not (HERE / img).exists():
                continue
            r["_group"], r["_label"] = key, label
            out.append(r)
    return out


def ref_card(r):
    days = r.get("days_running")
    days_s = f"{days} days" if isinstance(days, int) else ""
    head = (r.get("headline") or r.get("primary_text_excerpt") or "").strip()
    lib = r.get("library_url") or f"https://www.facebook.com/ads/library/?id={r.get('ad_archive_id','')}"
    mini = r.get("minimalism")
    return (f'<figure class="ref" data-g="{E(r["_group"])}" data-d="{days if isinstance(days, int) else 0}">'
            f'<a href="{E(lib)}" target="_blank" rel="noopener"><img src="{E(r["img"])}" loading="lazy" alt=""></a>'
            f'<figcaption><b>{E(r.get("brand",""))}</b>{" · " + E(days_s) if days_s else ""}'
            f'{" · min " + str(mini) if mini else ""}<br><span>{E(head[:90])}</span>'
            f'<br><a class="lib" href="{E(lib)}" target="_blank" rel="noopener">{E(str(r.get("ad_archive_id","")))}</a></figcaption></figure>')


def ad_file(n):
    f = sorted((HERE / "ads").glob(f"adstudio-static-{n:02d}-*.jpg"))
    return f"ads/{f[0].name}" if f else ""


def concept_card(c):
    img = ad_file(c["n"])
    adimg = f'<a href="{img}" target="_blank"><img class="adimg" src="{img}" loading="lazy" alt="Ad {c["n"]:02d}"></a>' if img else ""
    bars = "".join(
        f'<div class="bar"><span>{lab}</span><i style="--w:{c["s"][k]/mx*100:.0f}%"></i><em>{c["s"][k]}/{mx}</em></div>'
        for k, lab, mx in SCORE_KEYS)
    note = f'<p class="note"><b>Production note:</b> {E(c["note"])}</p>' if c.get("note") else ""
    star = '<span class="pick">Top 10</span>' if c["n"] in TOP else ""
    return f'''<article class="concept" id="c{c["n"]:02d}" data-p="{c["pillar"]}">
<div class="chd"><span class="num">{c["n"]:02d}</span><div class="ttl"><h3>{E(c["title"])}</h3>
<div class="tags"><span class="tag p-{c["pillar"]}">{E(PILLARS[c["pillar"]])}</span><span class="tag">{E(AWARE[c["aware"]])}</span><span class="tag">{E(c["device"])}</span>{star}</div></div>
<span class="score">{c["score"]}</span></div>
<div class="hl">{E(c["headline"])}</div>
<div class="sl">{E(c["subline"])}</div>
<div class="cgrid"><div>
<p><b>Big idea.</b> {E(c["big_idea"])}</p>
<p><b>Visual.</b> {E(c["visual"])}</p>
<p><b>Palette.</b> {E(c["palette"])}</p>
<p><b>Angle.</b> {E(c["angle"])}. <b>Awareness.</b> {E(AWARE[c["aware"]])}.</p>
<p><b>Why it stops the scroll.</b> {E(c["why"])}</p>
<p><b>Legends applied.</b> {E(c["legends"])}</p>
<p class="feed"><b>Feed copy.</b> Primary text: "{E(c["primary"])}" <br>Headline field: "{E(c["meta_headline"])}" · Button: Sign up · On-image CTA: Start for free</p>
{note}</div><div class="bars">{adimg}{bars}</div></div></article>'''


def main():
    refs = load_refs()
    refs.sort(key=lambda r: -(r.get("days_running") or 0) if isinstance(r.get("days_running"), int) else 0)
    counts = {k: sum(1 for r in refs if r["_group"] == k) for k, _ in GROUPS}
    ref_html = "".join(ref_card(r) for r in refs)
    framework = (HERE / "framework.html").read_text()
    findings = (HERE / "findings.html").read_text() if (HERE / "findings.html").exists() else ""
    by_id = {str(r.get("ad_archive_id")): r for r in refs}

    def ev(m):
        figs = []
        for i in m.group(1).split(","):
            r = by_id.get(i.strip())
            if not r:
                print("evidence id not found:", i)
                continue
            lib = r.get("library_url") or f"https://www.facebook.com/ads/library/?id={i}"
            figs.append(f'<a href="{E(lib)}" target="_blank" rel="noopener" title="{E(r.get("brand",""))}: {E((r.get("headline") or "")[:80])}"><img src="{E(r["img"])}" loading="lazy" alt=""><span>{E(r.get("brand",""))}</span></a>')
        return '<span class="ev">' + "".join(figs) + "</span>"

    findings = re.sub(r"\[\[ev:([0-9, ]+)\]\]", ev, findings)
    concepts_html = "".join(concept_card(c) for c in CONCEPTS)
    ranked = sorted(CONCEPTS, key=lambda c: -c["score"])
    rows = "".join(
        f'<tr><td><a href="#c{c["n"]:02d}">{c["n"]:02d}</a></td><td>{E(c["title"])}</td><td>{E(c["headline"][:60])}</td>'
        f'<td>{E(PILLARS[c["pillar"]].split(" (")[0])}</td><td>{E(AWARE[c["aware"]])}</td><td><b>{c["score"]}</b></td></tr>'
        for c in ranked)
    pill_btns = "".join(f'<button data-f="{k}">{E(v.split(" (")[0])}</button>' for k, v in PILLARS.items())
    grp_btns = "".join(f'<button data-f="{k}">{E(v)} ({counts.get(k,0)})</button>' for k, v in GROUPS)

    gallery = "".join(
        f'<a class="gi" href="#c{c["n"]:02d}"><img src="{ad_file(c["n"])}" loading="lazy" alt=""><span>{c["n"]:02d} {E(c["title"])}</span></a>'
        for c in CONCEPTS if ad_file(c["n"]))
    page = TEMPLATE.format(gallery=gallery, 
        n_refs=len(refs), ref_html=ref_html, grp_btns=grp_btns, framework=framework, findings=findings,
        concepts_html=concepts_html, rows=rows, pill_btns=pill_btns)
    (HERE / "index.html").write_text(page)
    print("wrote index.html", len(page), "bytes,", len(refs), "refs")


TEMPLATE = """<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Ad Studio Statics Plan</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">
<style>
:root{{--bg:#f1f1f1;--card:#fff;--fg:#1e1e1e;--mut:#616161;--line:#e2e2e2;--forest:#004c3f;--green:#006a43;--soft:#e6f2ec;--hl:#0b2e25}}
@media (prefers-color-scheme:dark){{:root{{--bg:#0f1412;--card:#171e1b;--fg:#eef2ef;--mut:#9fb0a6;--line:#26322c;--forest:#7fd1ad;--green:#5cc796;--soft:#1d2b25;--hl:#eaf6ef}}}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--fg);font:15px/1.55 Inter,system-ui,sans-serif}}
main{{max-width:1120px;margin:auto;padding:28px 16px 80px}}a{{color:var(--green)}}
h1{{font:800 clamp(26px,4vw,40px)/1.1 Inter,sans-serif;letter-spacing:-.02em;margin:0 0 8px}}
h2{{font:italic 400 clamp(28px,4vw,40px)/1.1 'Instrument Serif',serif;margin:56px 0 12px;color:var(--forest)}}
h3{{margin:0;font-size:18px}}h4{{margin:22px 0 6px;font-size:16px}}
.lead{{color:var(--mut);max-width:780px;margin:0 0 10px}}.status{{display:inline-block;background:var(--soft);color:var(--forest);font-weight:600;border-radius:999px;padding:4px 12px;font-size:13px}}
nav{{display:flex;gap:8px;flex-wrap:wrap;margin:16px 0}}nav a{{text-decoration:none;border:1px solid var(--line);background:var(--card);border-radius:999px;padding:5px 12px;font-size:13px;color:var(--fg)}}
.box{{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:16px 18px;margin:12px 0}}
.box ul,.box ol{{margin:6px 0;padding-left:20px}}.box li{{margin:4px 0}}
table{{width:100%;border-collapse:collapse;font-size:14px}}th,td{{text-align:left;vertical-align:top;padding:8px 10px;border-bottom:1px solid var(--line)}}th{{font-size:12px;text-transform:uppercase;letter-spacing:.04em;color:var(--mut)}}
.tw{{overflow-x:auto;background:var(--card);border:1px solid var(--line);border-radius:14px;margin:12px 0}}
.filters{{display:flex;gap:6px;flex-wrap:wrap;margin:8px 0}}.filters button{{font:600 13px Inter,sans-serif;border:1px solid var(--line);background:var(--card);color:var(--fg);border-radius:999px;padding:5px 12px;cursor:pointer}}.filters button.on{{background:var(--forest);color:#fff;border-color:var(--forest)}}
.refs{{display:grid;grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:10px}}
.ref{{margin:0;background:var(--card);border:1px solid var(--line);border-radius:10px;overflow:hidden}}.ref img{{width:100%;display:block;aspect-ratio:4/5;object-fit:cover;background:#ddd}}
.ref figcaption{{padding:6px 8px 8px;font-size:12px;color:var(--mut);line-height:1.35}}.ref figcaption b{{color:var(--fg)}}.ref figcaption span{{color:var(--fg)}}.lib{{font:11px ui-monospace,monospace}}
.concept{{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:18px;margin:14px 0}}
.chd{{display:flex;gap:14px;align-items:flex-start}}.num{{font:800 28px/1 Inter;color:var(--mut);min-width:40px}}.ttl{{flex:1}}
.tags{{display:flex;gap:6px;flex-wrap:wrap;margin-top:6px}}.tag{{font-size:12px;border:1px solid var(--line);border-radius:999px;padding:2px 9px;color:var(--mut)}}
.p-clone{{border-color:#6aa88d;color:var(--forest)}}.p-link{{border-color:#7f9bd6;color:#3156a3}}.p-free{{border-color:#d6a85c;color:#94661c}}.p-ugc{{border-color:#c98aa9;color:#9a3f6c}}
@media (prefers-color-scheme:dark){{.p-link{{color:#a9c0f0}}.p-free{{color:#efc684}}.p-ugc{{color:#f0b2cf}}}}
.pick{{font-size:12px;font-weight:700;background:var(--forest);color:#fff;border-radius:999px;padding:2px 9px}}
.score{{font:800 26px/1 Inter;color:#fff;background:var(--forest);border-radius:12px;padding:10px 12px;min-width:58px;text-align:center}}
.hl{{font:800 clamp(22px,3.2vw,30px)/1.15 Inter;letter-spacing:-.015em;margin:16px 0 4px;color:var(--hl)}}.sl{{color:var(--mut);font-size:16px;margin-bottom:10px}}
.cgrid{{display:grid;grid-template-columns:1fr 300px;gap:18px}}.adimg{{width:100%;display:block;border-radius:10px;border:1px solid var(--line);margin-bottom:10px}}.gal{{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:12px}}.gi{{display:block;text-decoration:none;color:var(--fg);font-size:13px;font-weight:600}}.gi img{{width:100%;display:block;border-radius:10px;border:1px solid var(--line);margin-bottom:6px}}.cgrid p{{margin:6px 0}}.feed{{background:var(--soft);border-radius:10px;padding:8px 10px;font-size:14px}}.note{{font-size:14px;color:var(--mut)}}
.bars{{font-size:12px;color:var(--mut)}}.bar{{display:grid;grid-template-columns:62px 1fr 40px;gap:6px;align-items:center;margin:5px 0}}.bar i{{display:block;height:8px;border-radius:9px;background:linear-gradient(90deg,var(--green) var(--w),var(--line) var(--w))}}.bar em{{font-style:normal;text-align:right}}
.ev{{display:flex;gap:8px;flex-wrap:wrap;margin:8px 0 4px}}.ev a{{display:block;width:96px;text-decoration:none;font-size:11px;color:var(--mut)}}.ev img{{width:96px;height:120px;object-fit:cover;border-radius:6px;border:1px solid var(--line);display:block}}
.legend td:first-child{{font-weight:700;white-space:nowrap}}.kpi{{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:10px}}.kpi div{{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px}}.kpi b{{display:block;font:800 26px Inter;color:var(--forest)}}
.anat{{display:grid;grid-template-columns:220px 1fr;gap:18px;align-items:start}}.frame{{aspect-ratio:4/5;border:2px solid var(--fg);border-radius:6px;position:relative;font-size:11px;font-weight:700;color:var(--mut)}}.frame div{{position:absolute;left:6%;right:6%;border:1px dashed var(--mut);border-radius:4px;display:flex;align-items:center;justify-content:center;text-align:center}}
@media (max-width:760px){{.cgrid,.anat{{grid-template-columns:1fr}}.frame{{max-width:220px}}}}
</style></head><body><main>
<span class="status">All 20 ads made, 12 Nov 2026. Nothing uploaded to Meta.</span>
<h1>Brevo Ad Studio: 20 static Meta ads</h1>
<p class="lead">The 20 finished ads first, then the research on what AI products run as statics, the rulebook built on Ogilvy and the other legends, and the scored concept behind each ad.</p>
<nav><a href="#ads">The 20 ads</a><a href="#research">1. Research</a><a href="#framework">2. Framework</a><a href="#concepts">3. The 20 concepts</a><a href="#ranked">4. Ranked</a><a href="#next">5. Next</a></nav>

<h2 id="ads">The 20 ads</h2>
<p class="lead">4:5, 1080 x 1350, ready for the Meta feed. Click an ad for its concept, score and feed copy. <a href="ads/brevo-ad-studio-statics-20.zip">Download all 20 (zip, 5.5 MB)</a>.</p>
<div class="gal">{gallery}</div>

<h2 id="research">1. What AI products run as statics</h2>
{findings}
<h4>Reference wall ({n_refs} statics, sorted by days running; click for the Meta Ad Library entry)</h4>
<div class="filters" id="gf"><button data-f="all" class="on">All</button>{grp_btns}</div>
<div class="refs" id="refs">{ref_html}</div>

<h2 id="framework">2. The framework</h2>
{framework}

<h2 id="concepts">3. The 20 concepts</h2>
<p class="lead">Each one: the big idea, the words on the image, the visual, who it talks to, why it should stop the scroll, the feed copy and its score against the rubric. "Top 10" marks my suggested first flight.</p>
<div class="filters" id="pf"><button data-f="all" class="on">All 20</button>{pill_btns}</div>
<div id="concept-list">{concepts_html}</div>

<h2 id="ranked">4. Ranked</h2>
<div class="tw"><table><thead><tr><th>#</th><th>Concept</th><th>Headline</th><th>Pillar</th><th>Awareness</th><th>Score</th></tr></thead><tbody>{rows}</tbody></table></div>

<h2 id="next">5. How they were made, and what's next</h2>
<div class="box"><ul>
<li><b>Rendered whole</b> on GPT Image 2 (the engine Ad Studio itself uses) from one prompt per concept written against the rulebook: zones, exact copy, sizes and palette. Only the Brevo Ad Studio logo is composited. Every word was checked at full size.</li>
<li><b>Real Ad Studio output inside the ads.</b> The example ads in 03, 06, 12 and 15 and the presenter Simone in 10, 15, 17 and 20 come from real Ad Studio generations for the Glowday and drift demo stores. Ad 12's hero is the ad Ad Studio made from the Glowday product link.</li>
<li><b>Real numbers.</b> Day counts (691, 336, 314, 286, 274) are from the public Ad Radar library on 12 Nov 2026.</li>
<li><b>QA.</b> 27 renders for 20 ads. Rebuilt: 13 (a doubled word, then a doubled line), 06 (French words on a demo label), 10 (an invented star rating), 04 (brand-like words on tiny cards, then a button too close to the edge).</li>
<li><b>Next, on your go:</b> square 1:1 and vertical 9:16 versions of the ones you want to run, then upload to the Ad Studio campaign. Nothing goes to Meta without your OK.</li>
</ul></div>
<p class="lead" style="margin-top:28px">Built 12 Nov 2026. Claims verified on ads.brevo.com and ads.brevo.com/pricing the same day.</p>
</main>
<script>
function wire(id,sel,attr){{const bs=document.querySelectorAll('#'+id+' button');bs.forEach(b=>b.onclick=()=>{{bs.forEach(x=>x.classList.remove('on'));b.classList.add('on');const f=b.dataset.f;document.querySelectorAll(sel).forEach(el=>{{el.style.display=(f==='all'||el.dataset[attr]===f)?'':'none'}})}})}}
wire('gf','.ref','g');wire('pf','.concept','p');
</script></body></html>"""

if __name__ == "__main__":
    main()
