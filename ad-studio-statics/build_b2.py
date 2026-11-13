#!/usr/bin/env python3
"""Build ad-studio-statics/batch2.html from concepts_b2.py, framework_b2.html, research/b2-provocative.json and ads-b2/."""
import html, json, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from concepts_b2 import ADS, BANK, EVIDENCE, CLONES  # noqa: E402
from concepts_b2_opts import WIN, CLO, HL, OPTS, RADAR, CDN  # noqa: E402

E = html.escape
TOP5 = [28, 31, 32, 21, 30]
KEYS = [("st", "Stops"), ("one", "One idea"), ("off", "Offer in 3s"), ("tru", "True"), ("wait", "Waiting costs"), ("shot", "Screenshot")]


def img(n, fmt):
    p = HERE / "ads-b2" / f"adstudio-b2-{n}-{fmt}.jpg"
    return f"ads-b2/{p.name}" if p.exists() else ""


def oimg(key, fmt):
    p = HERE / "ads-b2" / "opt" / f"adstudio-b2-{key}-{fmt}.jpg"
    return f"ads-b2/opt/{p.name}" if p.exists() else ""


def opt_col(n, key, wins, ck):
    i45, i11 = oimg(key, "4x5"), oimg(key, "1x1")
    hl = HL[n].format(d=WIN[wins[0]]["days"])
    befores = "".join(f'<a href="{RADAR}{WIN[w]["uuid"]}" target="_blank" rel="noopener"><img src="ads-b2/pairs/{w}.jpg" loading="lazy" alt="{E(WIN[w]["brand"])} winner"></a>' for w in wins)
    after = (f'<span class="arr">&rarr;</span><a href="{CDN}{CLO[ck]["file"]}" target="_blank" rel="noopener"><img src="ads-b2/pairs/c{ck}.jpg" loading="lazy" alt="Clone"></a>' if ck else "")
    prov = "".join(f'<li>Before: <b>{E(WIN[w]["brand"])}</b>, "{E(WIN[w]["text"])}", live {WIN[w]["days"]} days. '
                   f'<a href="{RADAR}{WIN[w]["uuid"]}" target="_blank" rel="noopener">Ad Radar</a> · '
                   f'<a href="https://www.facebook.com/ads/library/?id={WIN[w]["meta"]}" target="_blank" rel="noopener">Meta ad {WIN[w]["meta"]}</a></li>' for w in wins)
    if ck:
        prov += f'<li>After: Ad Studio Clone for {E(CLO[ck]["prod"])}, "{E(CLO[ck]["text"])}". <a href="{CDN}{CLO[ck]["file"]}" target="_blank" rel="noopener">Ad Studio output</a></li>'
    fmts = " · ".join(f'<a href="{s}" target="_blank">{lab}</a>' for s, lab in ((i45, "4:5"), (i11, "1:1")) if s)
    return (f'<div class="opt"><div class="olab">Option {key[-1]}</div>'
            f'<a href="{i45}" target="_blank"><img class="ofinal" src="{i45}" loading="lazy" alt="Ad {key}"></a>'
            f'<div class="ofmt">{fmts}</div><div class="ohl">{E(hl)}</div>'
            f'<div class="pairs">{befores}{after}</div><ul class="prov">{prov}</ul></div>')


def opt_card(a):
    n = a["n"]
    bars = "".join(f'<div class="bar"><span>{lab}</span><i style="--w:{a["b"][k]*10}%"></i><em>{a["b"][k]}</em></div>' for k, lab in KEYS)
    pick = '<span class="pick">Top 5</span>' if n in TOP5 else ""
    cols = "".join(opt_col(n, *o) for o in OPTS[n])
    return f'''<article class="concept wide" id="b{n}"><div class="body">
<div class="chd"><span class="num">{n}</span><div class="ttl"><h3>{E(a["title"])}</h3><div class="tags"><span class="tag">{E(a["mech"])}</span><span class="tag">{E(a["angle"])}</span>{pick}<span class="tag new">3 options, real befores and afters</span></div></div><span class="score">{a["score"]}</span></div>
<div class="opts">{cols}</div>
<div class="sl">{E(a["subline"])}</div>
<p><b>The line it walks.</b> {E(a["line"])}</p>
<div class="bars">{bars}</div></div></article>'''


def card(a):
    if a["n"] in OPTS:
        return opt_card(a)
    i45, i11 = img(a["n"], "4x5"), img(a["n"], "1x1")
    bars = "".join(f'<div class="bar"><span>{lab}</span><i style="--w:{a["b"][k]*10}%"></i><em>{a["b"][k]}</em></div>' for k, lab in KEYS)
    ev = "".join(
        f'<li>Before: {E(EVIDENCE[k]["label"])}, live {EVIDENCE[k]["days"]} days. '
        f'<a href="{EVIDENCE[k]["radar"]}" target="_blank" rel="noopener">Ad Radar</a> · '
        f'<a href="https://www.facebook.com/ads/library/?id={EVIDENCE[k]["meta"]}" target="_blank" rel="noopener">Meta ad {EVIDENCE[k]["meta"]}</a></li>'
        for k in a["ev"])
    ev += "".join(f'<li>After: {E(CLONES[k]["label"])}. <a href="{CLONES[k]["url"]}" target="_blank" rel="noopener">Ad Studio output</a></li>' for k in a["clone"])
    prov = f'<ul class="prov">{ev}</ul>' if ev else '<p class="note">Copy-only ad: no third-party artifact.</p>'
    pick = '<span class="pick">Top 5</span>' if a["n"] in TOP5 else ""
    imgs = "".join(f'<a href="{s}" target="_blank"><img src="{s}" loading="lazy" alt="Ad {a["n"]} {lab}"></a>' for s, lab in ((i45, "4:5"), (i11, "1:1")) if s)
    return f'''<article class="concept" id="b{a["n"]}"><div class="imgs">{imgs}</div><div class="body">
<div class="chd"><span class="num">{a["n"]}</span><div class="ttl"><h3>{E(a["title"])}</h3><div class="tags"><span class="tag">{E(a["mech"])}</span><span class="tag">{E(a["angle"])}</span>{pick}</div></div><span class="score">{a["score"]}</span></div>
<div class="hl">{E(a["headline"])}</div><div class="sl">{E(a["subline"])}</div>
<p><b>Visual.</b> {E(a["visual"])}</p><p><b>The line it walks.</b> {E(a["line"])}</p>
<p><b>Provenance.</b></p>{prov}
<div class="bars">{bars}</div></div></article>'''


def main():
    research = json.loads((HERE / "research" / "b2-provocative.json").read_text())
    refs = "".join(
        f'<figure class="ref"><a href="{E(r.get("library_url",""))}" target="_blank" rel="noopener"><img src="{E(r["img"])}" loading="lazy" alt=""></a>'
        f'<figcaption><b>{E(r["brand"])}</b> · {E(str(r.get("days_running","")))} days<br><span>{E((r.get("headline") or "")[:90])}</span><br><i>{E((r.get("mechanism") or "")[:70])}</i></figcaption></figure>'
        for r in research if (HERE / r["img"]).exists())
    def gsrc(a):
        return oimg(OPTS[a["n"]][0][0], "4x5") if a["n"] in OPTS else img(a["n"], "4x5")

    def ghl(a):
        return HL[a["n"]].format(d=WIN[OPTS[a["n"]][0][1][0]]["days"]) if a["n"] in OPTS else a["headline"]
    gallery = "".join(f'<a class="gi" href="#b{a["n"]}"><img src="{gsrc(a)}" loading="lazy" alt=""><span>{a["n"]} · {E(ghl(a))}{" (3 options)" if a["n"] in OPTS else ""}</span></a>' for a in ADS if gsrc(a))
    top = "".join(f'<li><a href="#b{a["n"]}">{a["n"]}. {E(ghl(a))}</a> ({a["score"]}): {E(a["mech"])}</li>' for n in TOP5 for a in ADS if a["n"] == n)
    bank = "".join(f'<tr><td>{E(h)}</td><td><b>{s}</b></td><td>{E(st)}</td></tr>' for h, s, st in BANK)
    page = TEMPLATE.format(gallery=gallery, top=top, cards="".join(card(a) for a in ADS), bank=bank,
                           framework=(HERE / "framework_b2.html").read_text(), refs=refs, nrefs=len(research))
    (HERE / "batch2.html").write_text(page)
    print("wrote batch2.html", len(page))


TEMPLATE = """<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Ad Studio Statics Batch 2</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">
<style>
:root{{--bg:#f1f1f1;--card:#fff;--fg:#1e1e1e;--mut:#616161;--line:#e2e2e2;--forest:#004c3f;--green:#006a43;--soft:#e6f2ec;--hl:#0b2e25}}
@media (prefers-color-scheme:dark){{:root{{--bg:#0f1412;--card:#171e1b;--fg:#eef2ef;--mut:#9fb0a6;--line:#26322c;--forest:#7fd1ad;--green:#5cc796;--soft:#1d2b25;--hl:#eaf6ef}}}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--fg);font:15px/1.55 Inter,system-ui,sans-serif}}
main{{max-width:1160px;margin:auto;padding:28px 16px 80px}}a{{color:var(--green)}}
h1{{font:800 clamp(26px,4vw,40px)/1.1 Inter,sans-serif;letter-spacing:-.02em;margin:0 0 8px}}
h2{{font:italic 400 clamp(28px,4vw,40px)/1.1 'Instrument Serif',serif;margin:56px 0 12px;color:var(--forest)}}h3{{margin:0;font-size:18px}}h4{{margin:22px 0 6px;font-size:16px}}
.lead{{color:var(--mut);max-width:820px;margin:0 0 10px}}.status{{display:inline-block;background:var(--soft);color:var(--forest);font-weight:600;border-radius:999px;padding:4px 12px;font-size:13px}}
nav{{display:flex;gap:8px;flex-wrap:wrap;margin:16px 0}}nav a{{text-decoration:none;border:1px solid var(--line);background:var(--card);border-radius:999px;padding:5px 12px;font-size:13px;color:var(--fg)}}
.box{{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:16px 18px;margin:12px 0}}.box li{{margin:4px 0}}
table{{width:100%;border-collapse:collapse;font-size:14px}}th,td{{text-align:left;vertical-align:top;padding:8px 10px;border-bottom:1px solid var(--line)}}th{{font-size:12px;text-transform:uppercase;letter-spacing:.04em;color:var(--mut)}}
.tw{{overflow-x:auto;background:var(--card);border:1px solid var(--line);border-radius:14px;margin:12px 0}}
.gal{{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:12px}}.gi{{display:block;text-decoration:none;color:var(--fg);font-size:12px;font-weight:600}}.gi img{{width:100%;display:block;border-radius:10px;border:1px solid var(--line);margin-bottom:6px}}
.concept{{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:18px;margin:14px 0;display:grid;grid-template-columns:400px 1fr;gap:20px}}
.imgs{{display:grid;grid-template-columns:1fr 1fr;gap:8px;align-content:start}}.imgs img{{width:100%;display:block;border-radius:8px;border:1px solid var(--line)}}
.chd{{display:flex;gap:12px;align-items:flex-start}}.num{{font:800 26px/1 Inter;color:var(--mut)}}.ttl{{flex:1}}.tags{{display:flex;gap:6px;flex-wrap:wrap;margin-top:6px}}
.tag{{font-size:12px;border:1px solid var(--line);border-radius:999px;padding:2px 9px;color:var(--mut)}}.pick{{font-size:12px;font-weight:700;background:var(--forest);color:#fff;border-radius:999px;padding:2px 9px}}
.score{{font:800 24px/1 Inter;color:#fff;background:var(--forest);border-radius:12px;padding:10px 12px;min-width:56px;text-align:center}}
.hl{{font:800 clamp(20px,2.6vw,26px)/1.2 Inter;margin:14px 0 4px;color:var(--hl)}}.sl{{color:var(--mut);margin-bottom:8px}}.body p{{margin:6px 0}}
.prov{{margin:4px 0 8px;padding-left:18px;font-size:13px}}.note{{font-size:13px;color:var(--mut)}}
.bars{{font-size:12px;color:var(--mut);max-width:420px;margin-top:8px}}.bar{{display:grid;grid-template-columns:96px 1fr 26px;gap:6px;align-items:center;margin:4px 0}}.bar i{{display:block;height:7px;border-radius:9px;background:linear-gradient(90deg,var(--green) var(--w),var(--line) var(--w))}}.bar em{{font-style:normal;text-align:right}}
.refs{{display:grid;grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:10px}}.ref{{margin:0;background:var(--card);border:1px solid var(--line);border-radius:10px;overflow:hidden}}.ref img{{width:100%;display:block;aspect-ratio:4/5;object-fit:cover}}.ref figcaption{{padding:6px 8px 8px;font-size:12px;color:var(--mut);line-height:1.35}}.ref figcaption b,.ref figcaption span{{color:var(--fg)}}
.concept.wide{{grid-template-columns:1fr}}.opts{{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin:14px 0}}.opt{{border:1px solid var(--line);border-radius:12px;padding:10px;background:var(--bg)}}.olab{{font-weight:700;font-size:13px;margin-bottom:6px;color:var(--forest)}}.ofinal{{width:100%;display:block;border-radius:8px;border:1px solid var(--line)}}.ofmt{{font-size:12px;margin:4px 0}}.ohl{{font-weight:800;margin:6px 0}}.pairs{{display:flex;gap:6px;align-items:center;margin:8px 0}}.pairs a{{flex:1;min-width:0}}.pairs img{{width:100%;height:150px;object-fit:contain;background:#fff;border-radius:6px;border:1px solid var(--line);display:block}}.arr{{font-weight:800;font-size:20px;color:var(--forest)}}.tag.new{{background:var(--soft);color:var(--forest);border-color:transparent;font-weight:600}}
@media (max-width:820px){{.concept{{grid-template-columns:1fr}}.opts{{grid-template-columns:1fr}}}}
</style></head><body><main>
<span class="status">Batch 2: 20 ads, 13 Nov 2026. Updated: 3 options for every ad that shows a winner or a clone. Nothing uploaded to Meta.</span>
<h1>Brevo Ad Studio statics, batch 2: clone 3 winning ads, free</h1>
<p class="lead">Ads 21 to 40. Edgier and copy-led: quiet layouts, provocative headlines, one offer. Every "before" is a real long-running ad from Ad Radar, shown exactly as it ran, and every "after" is a real Clone run in Ad Studio (GPT Image 2.5) for our redesigned demo brands, <a href="https://glowday.pages.dev/products/tinted-mineral-spf-50">glowday</a> and <a href="https://driftsleep.pages.dev/products/magnesium-sleep-gummies">drift</a>. Each ad comes in 4:5 and 1:1. The nine ads that show winners or clones (21, 23, 24, 31, 32, 33, 35, 36, 39) now come in 3 options each, built on edgier winners, with clones that mirror the original layout.</p>
<nav><a href="#ads">The 20 ads</a><a href="#top5">Top 5</a><a href="#detail">Each ad</a><a href="#bank">Headline bank</a><a href="#framework">Framework appendix</a><a href="#research">Research</a><a href="./">Batch 1</a><a href="ads-b2/brevo-ad-studio-statics-b2.zip">Download all (zip)</a></nav>
<h2 id="ads">The 20 ads</h2><div class="gal">{gallery}</div>
<h2 id="top5">Top 5</h2><div class="box"><ol>{top}</ol></div>
<h2 id="detail">Each ad: copy, mechanism, provenance, banger score</h2>{cards}
<h2 id="bank">Headline bank: 44 written, 20 kept</h2>
<div class="tw"><table><thead><tr><th>Headline</th><th>Banger score</th><th>Status</th></tr></thead><tbody>{bank}</tbody></table></div>
<h2 id="framework">Framework appendix</h2>{framework}
<h2 id="research">Research: {nrefs} provocative statics</h2>
<p class="lead">Live from the Meta Ad Library on 13 Nov 2026, plus the most provocative from the batch 1 wall. Click for the Library entry.</p>
<div class="refs">{refs}</div>
<p class="lead" style="margin-top:28px">Built 13 Nov 2026. Clones run in Ad Studio the same day; run lengths from the public Ad Radar library (12 Nov 2026).</p>
</main></body></html>"""

if __name__ == "__main__":
    main()
