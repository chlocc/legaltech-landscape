#!/usr/bin/env python3
"""Render site/index.html from data/*.json. No dependencies."""
import json, pathlib, html, re

ROOT = pathlib.Path(__file__).parent
D = ROOT / "data"
SITE = ROOT / "docs"
SITE.mkdir(exist_ok=True)

companies = json.loads((D / "companies.json").read_text())
platforms = json.loads((D / "platforms.json").read_text())
frictions = json.loads((D / "frictions.json").read_text())

e = lambda s: html.escape(str(s), quote=True)

CAT_ORDER = ["assistant", "contract", "litigation", "research", "inhouse",
             "ip", "infra", "practice_mgmt", "ai_native_firm", "buyer"]

PLATFORM_KEYS = [("anthropic", "Anthropic"), ("openai", "OpenAI"), ("google", "Google")]

# Short labels for chips and filter buttons; the long text in companies.json
# stays as the tooltip so the taxonomy is still legible on hover.
SHORT = {
    "platform": "Model platform", "assistant": "Assistant / platform",
    "contract": "Contract & CLM", "litigation": "Litigation & e-discovery",
    "research": "Research & data", "inhouse": "In-house tooling",
    "ip": "IP & patents", "infra": "DMS & infrastructure",
    "practice_mgmt": "Practice management", "ai_native_firm": "AI-native firm",
    "buyer": "Firms building",
}

# --- linking -------------------------------------------------------------
NAME_TO_URL = {c["name"]: c["url"] for c in companies["companies"] if c.get("url")}
# Names as the platforms write them, mapped onto the tracked entity.
ALIASES = {
    "Thomson Reuters": "Thomson Reuters — CoCounsel Legal",
    "Thomson Reuters (CoCounsel)": "Thomson Reuters — CoCounsel Legal",
    "Crosby Legal": "Crosby",
    "Accenture": "Accenture Legal",
    "Manifest Law": "Manifest OS / Manifest Law",
}


def link_name(n):
    """Render a partner/customer name as a link when we track it."""
    key = ALIASES.get(n, n)
    url = NAME_TO_URL.get(key)
    if not url:
        stripped = re.sub(r"\s*\(.*?\)", "", n).strip()
        url = NAME_TO_URL.get(ALIASES.get(stripped, stripped))
    return f'<a href="{e(url)}" target="_blank" rel="noopener">{e(n)}</a>' if url else e(n)


def domain(u):
    d = re.sub(r"^https?://(www\.)?", "", u).split("/")[0]
    return d


def sources(items, cls="src"):
    if not items:
        return ""
    links = "".join(
        f'<a href="{e(u)}" target="_blank" rel="noopener">{e(domain(u))}</a>' for u in items
    )
    return f'<div class="{cls}"><span class="src-lbl">Sources</span>{links}</div>'


def platform_cards():
    out = []
    for p in platforms["platforms"]:
        comps = "".join(f"<li>{e(c)}</li>" for c in p["components"])
        partners = ", ".join(link_name(x) for x in p.get("partners", [])) or "&mdash;"
        users = ", ".join(link_name(x) for x in p.get("named_users", [])) or "&mdash;"
        extra = ""
        if p.get("benchmarks"):
            extra += f'<p class="pf-extra"><span class="lbl">Benchmarks</span>{e(p["benchmarks"])}</p>'
        if p.get("people"):
            extra += f'<p class="pf-extra"><span class="lbl">People</span>{e(p["people"])}</p>'
        if p.get("access"):
            extra += f'<p class="pf-extra"><span class="lbl">Access</span>{e(p["access"])}</p>'
        srcs = sources(p.get("sources", []), "pf-src")
        repo = (f'<a class="repo" href="{e(p["repo"])}" target="_blank" rel="noopener">'
                f'{e(domain(p["repo"]))} &#8599;</a>') if p.get("repo") else ""
        out.append(f"""
<article class="pf pf--{e(p['id'])}">
  <header>
    <div class="pf-vendor">{e(p['vendor'])}</div>
    <h3><a href="{e(p['url'])}" target="_blank" rel="noopener">{e(p['product'])} &#8599;</a></h3>
    <div class="pf-date">Launched {e(p['launched'])} {repo}</div>
  </header>
  <p class="pf-shape">{e(p['shape'])}</p>
  <p class="pf-model"><span class="lbl">Model</span>{e(p['model'])}</p>
  <ul class="pf-comps">{comps}</ul>
  {extra}
  <p class="pf-extra"><span class="lbl">Ecosystem</span>{partners}</p>
  <p class="pf-extra"><span class="lbl">Named firms</span>{users}</p>
  {srcs}
</article>""")
    return "\n".join(out)


def matrix_rows():
    rows = []
    for c in companies["companies"]:
        pi = c.get("platform_integrations") or {}
        if not any(pi.get(k) for k, _ in PLATFORM_KEYS):
            continue
        cells = ""
        for k, _ in PLATFORM_KEYS:
            v = pi.get(k)
            if v:
                cells += f'<td class="yes {k}" title="{e(v)}"><span class="dot"></span><span class="mx-note">{e(v)}</span></td>'
            else:
                cells += '<td class="no"></td>'
        rows.append(
            f'<tr><th scope="row"><a href="{e(c["url"])}" target="_blank" rel="noopener">{e(c["name"])}</a>'
            f'<span class="mx-cat" title="{e(companies["categories"][c["category"]])}">'
            f'{e(SHORT[c["category"]])}</span></th>{cells}</tr>'
        )
    return "\n".join(rows)


def company_cards():
    out = []
    order = {k: i for i, k in enumerate(CAT_ORDER)}
    for c in sorted(companies["companies"], key=lambda x: (order.get(x["category"], 99), x["name"])):
        pi = c.get("platform_integrations") or {}
        chips = "".join(
            f'<span class="chip chip--{k}" title="{e(pi[k])}">{lbl}</span>'
            for k, lbl in PLATFORM_KEYS if pi.get(k)
        )
        models = "".join(f'<span class="m">{e(m)}</span>' for m in (c.get("models") or []))
        meta = []
        if c.get("hq"): meta.append(e(c["hq"]))
        if c.get("founded"): meta.append(f'est. {e(c["founded"])}')
        if c.get("valuation"): meta.append(e(c["valuation"]))
        lines = ""
        for label, key in (("Last round", "last_round"), ("History", "funding_history"), ("Model use", "model_note"),
                           ("Traction", "traction"), ("Why it matters", "notable"),
                           ("Caveat", "confidence")):
            if c.get(key):
                cls = " line--caveat" if key == "confidence" else ""
                lines += f'<p class="line{cls}"><span class="lbl">{label}</span>{e(c[key])}</p>'
        srcs = sources(c.get("sources", []), "co-src")
        name = (f'<a href="{e(c["url"])}" target="_blank" rel="noopener">{e(c["name"])}</a>'
                if c.get("url") else e(c["name"]))
        search_blob = e(" ".join(filter(None, [
            c["name"], c.get("what_it_does", ""), c.get("hq") or "",
            " ".join(c.get("models") or []), c.get("notable") or "", c.get("model_note") or ""
        ])).lower())
        out.append(f"""
<article class="co" data-cat="{e(c['category'])}" data-search="{search_blob}"
         data-anthropic="{'1' if pi.get('anthropic') else '0'}"
         data-openai="{'1' if pi.get('openai') else '0'}"
         data-google="{'1' if pi.get('google') else '0'}">
  <div class="co-head">
    <h4>{name}</h4>
    <div class="co-chips">{chips}</div>
  </div>
  <div class="co-meta">{' · '.join(meta) if meta else ''}</div>
  <p class="co-desc">{e(c.get('what_it_does',''))}</p>
  {f'<div class="co-models">{models}</div>' if models else ''}
  {lines}
  {partnerships_block(c)}
  {srcs}
</article>""")
    return "\n".join(out)



def ainative_block():
    firms = [c for c in companies["companies"] if c["category"] == "ai_native_firm"]
    refs = ""
    for r in companies.get("references", []):
        refs += (f'<div class="read"><a href="{e(r["url"])}" target="_blank" rel="noopener">'
                 f'{e(r["name"])} &#8599;</a><p>{e(r["note"])}</p>{sources(r.get("sources", []), "co-src")}</div>')
    names = " &middot; ".join(link_name(c["name"]) for c in sorted(firms, key=lambda x: x["name"]))
    return firms, refs, names

AI_FIRMS, AI_REFS, AI_NAMES = ainative_block()


def friction_cards(key, kind):
    out = []
    for i, f in enumerate(frictions[key], 1):
        stats = ""
        if f.get("stats"):
            stats = '<div class="stats">' + "".join(
                f'<div class="stat"><b>{e(v)}</b><span>{e(lab)}</span></div>' for v, lab in f["stats"]
            ) + "</div>"
        out.append(f"""
<article class="fr fr--{kind}">
  <div class="fr-n">{i:02d}</div>
  <h4>{e(f['title'])}</h4>
  {stats}
  <p>{e(f['body'])}</p>
  {sources(f.get('sources', []), 'co-src')}
</article>""")
    return "\n".join(out)



PARTNER_GROUPS = [
    ("acquisitions", "Acquired"),
    ("tech_integrations", "Integrations"),
    ("content", "Content partners"),
    ("firm_customers", "Law firm customers"),
    ("inhouse_customers", "In-house customers"),
    ("other", "Other"),
]


def partnerships_block(c):
    """Render a company's collaboration map when we have one."""
    pt = c.get("partnerships")
    if not pt:
        return ""
    groups = ""
    for key, label in PARTNER_GROUPS:
        items = pt.get(key) or []
        if not items:
            continue
        rows = ""
        for it in items:
            nm = (f'<a href="{e(it["url"])}" target="_blank" rel="noopener">{e(it["what"])}</a>'
                  if it.get("url") else e(it["what"]))
            when = f'<span class="pn-when">{e(it["when"])}</span>' if it.get("when") else ""
            note = f'<span class="pn-note">{e(it["note"])}</span>' if it.get("note") else ""
            rows += f'<li><span class="pn-name">{nm}</span>{when}{note}</li>'
        groups += f'<div class="pn-group"><span class="lbl">{label}</span><ul>{rows}</ul></div>'
    n = sum(len(pt.get(k) or []) for k, _ in PARTNER_GROUPS)
    return (f'<details class="pn"><summary>Collaboration map '
            f'<em>{n} tracked</em></summary>{groups}</details>')


def filter_buttons():
    counts = {}
    for c in companies["companies"]:
        counts[c["category"]] = counts.get(c["category"], 0) + 1
    btns = [f'<button class="fb is-on" data-cat="all">All <em>{len(companies["companies"])}</em></button>']
    for k in CAT_ORDER:
        if k in counts:
            btns.append(f'<button class="fb" data-cat="{e(k)}" title="{e(companies["categories"][k])}">'
                        f'{e(SHORT[k])} <em>{counts[k]}</em></button>')
    return "\n".join(btns)


HTML = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Legal AI Landscape &mdash; the model layer and everyone building on it</title>
<meta name="description" content="Who is building what in legal AI, and which foundation-model platform they plug into. Updated {e(companies['as_of'])}.">
<style>
:root {{
  --bg:#0e1013; --panel:#16191e; --panel2:#1c2027; --line:#262b33;
  --ink:#e8eaed; --ink2:#a2a9b4; --ink3:#6f7681;
  --accent:#d97757; --anthropic:#d97757; --openai:#10a37f; --google:#5b8def;
  --mono:ui-monospace,SFMono-Regular,Menlo,monospace;
}}
* {{ box-sizing:border-box; }}
body {{ margin:0; background:var(--bg); color:var(--ink);
  font:15px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif;
  -webkit-font-smoothing:antialiased; }}
a {{ color:inherit; }}
.wrap {{ max-width:1180px; margin:0 auto; padding:0 24px; }}

header.top {{ border-bottom:1px solid var(--line); padding:56px 0 40px; }}
header.top h1 {{ font-size:34px; line-height:1.15; margin:0 0 14px; letter-spacing:-.02em; }}
header.top h1 span {{ color:var(--accent); }}
header.top p {{ color:var(--ink2); max-width:70ch; margin:0 0 10px; font-size:16px; }}
.asof {{ font:12px var(--mono); color:var(--ink3); text-transform:uppercase; letter-spacing:.08em; margin-top:18px; }}
nav.jump {{ display:flex; gap:20px; flex-wrap:wrap; margin-top:22px; font-size:13px; }}
nav.jump a {{ color:var(--ink2); text-decoration:none; border-bottom:1px solid var(--line); padding-bottom:2px; }}
nav.jump a:hover {{ color:var(--accent); border-color:var(--accent); }}

section {{ padding:56px 0; border-bottom:1px solid var(--line); }}
h2 {{ font-size:13px; font-family:var(--mono); text-transform:uppercase; letter-spacing:.14em;
  color:var(--ink3); margin:0 0 8px; }}
.lede {{ font-size:19px; line-height:1.55; max-width:72ch; margin:0 0 32px; color:var(--ink); letter-spacing:-.01em; }}
.lede strong {{ color:var(--accent); font-weight:600; }}

.pf-grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(320px,1fr)); gap:18px; }}
.pf {{ background:var(--panel); border:1px solid var(--line); border-radius:10px; padding:22px; border-top:3px solid var(--line); }}
.pf--anthropic {{ border-top-color:var(--anthropic); }}
.pf--openai {{ border-top-color:var(--openai); }}
.pf--google {{ border-top-color:var(--google); }}
.pf-vendor {{ font:11px var(--mono); text-transform:uppercase; letter-spacing:.12em; color:var(--ink3); }}
.pf h3 {{ margin:6px 0 4px; font-size:21px; letter-spacing:-.01em; }}
.pf-date {{ font:12px var(--mono); color:var(--ink3); margin-bottom:16px; }}
.pf-shape {{ font-size:15px; color:var(--ink); margin:0 0 16px; padding-left:12px; border-left:2px solid var(--accent); }}
.pf-comps {{ margin:0 0 16px; padding-left:18px; color:var(--ink2); font-size:13.5px; }}
.pf-comps li {{ margin-bottom:6px; }}
.pf-model, .pf-extra, .line {{ font-size:13px; color:var(--ink2); margin:0 0 10px; }}
.lbl {{ display:block; font:10.5px var(--mono); text-transform:uppercase; letter-spacing:.1em;
  color:var(--ink3); margin-bottom:3px; }}
.pf-src, .co-src {{ margin:16px 0 0; padding-top:12px; border-top:1px solid var(--line); }}
.src-lbl {{ display:block; font:10.5px var(--mono); text-transform:uppercase; letter-spacing:.1em;
  color:var(--ink3); margin-bottom:6px; }}
.pf-src a, .co-src a {{ display:inline-block; font:11px var(--mono); color:var(--ink2);
  text-decoration:none; background:var(--panel2); border:1px solid var(--line);
  border-radius:4px; padding:3px 7px; margin:0 4px 4px 0; }}
.pf-src a:hover, .co-src a:hover {{ color:var(--accent); border-color:var(--accent); }}
a.repo {{ color:var(--ink3); text-decoration:none; margin-left:8px; }}
a.repo:hover {{ color:var(--accent); }}
.pf h3 a {{ text-decoration:none; }}
.pf h3 a:hover {{ color:var(--accent); }}
table.mx th[scope=row] a {{ text-decoration:none; }}
table.mx th[scope=row] a:hover {{ color:var(--accent); }}
.callout {{ background:var(--panel); border:1px solid var(--line); border-left:3px solid var(--accent);
  border-radius:8px; padding:20px 22px; margin-bottom:26px; }}
.callout h4 {{ margin:0 0 8px; font-size:15px; }}
.callout p {{ margin:0 0 10px; font-size:14px; color:var(--ink2); }}
.callout p:last-child {{ margin-bottom:0; }}
.callout a {{ color:var(--accent); }}
.pn {{ margin:12px 0 0; border-top:1px solid var(--line); padding-top:12px; }}
.pn > summary {{ cursor:pointer; font:11px var(--mono); text-transform:uppercase; letter-spacing:.1em;
  color:var(--ink2); list-style:none; }}
.pn > summary::-webkit-details-marker {{ display:none; }}
.pn > summary::before {{ content:"+ "; color:var(--accent); }}
.pn[open] > summary::before {{ content:"\2212 "; }}
.pn > summary:hover {{ color:var(--accent); }}
.pn > summary em {{ font-style:normal; color:var(--ink3); text-transform:none; letter-spacing:0; margin-left:4px; }}
.pn-group {{ margin-top:14px; }}
.pn-group ul {{ list-style:none; margin:0; padding:0; }}
.pn-group li {{ margin-bottom:9px; font-size:13px; }}
.pn-name a {{ color:var(--ink); text-decoration:none; border-bottom:1px solid var(--line); }}
.pn-name a:hover {{ color:var(--accent); border-color:var(--accent); }}
.pn-name {{ font-weight:500; color:var(--ink); }}
.pn-when {{ font:10.5px var(--mono); color:var(--ink3); margin-left:7px; }}
.pn-note {{ display:block; color:var(--ink2); font-size:12.5px; margin-top:2px; }}
.fr-grid {{ display:grid; grid-template-columns:repeat(auto-fill,minmax(340px,1fr)); gap:16px; margin-bottom:12px; }}
.fr {{ background:var(--panel); border:1px solid var(--line); border-radius:10px; padding:20px 22px; position:relative; }}
.fr--block {{ border-left:3px solid #b4564a; }}
.fr--opp {{ border-left:3px solid #4f9d7a; }}
.fr-n {{ font:10.5px var(--mono); color:var(--ink3); letter-spacing:.12em; }}
.fr h4 {{ margin:4px 0 12px; font-size:16.5px; letter-spacing:-.01em; }}
.fr p {{ margin:0; font-size:14px; color:var(--ink2); }}
.stats {{ display:flex; flex-wrap:wrap; gap:18px; margin:0 0 14px; padding:12px 0; border-top:1px solid var(--line); border-bottom:1px solid var(--line); }}
.stat b {{ display:block; font-size:19px; font-weight:600; color:var(--ink); letter-spacing:-.02em; }}
.fr--block .stat b {{ color:#e08a7d; }}
.stat span {{ font:10.5px var(--mono); color:var(--ink3); text-transform:uppercase; letter-spacing:.06em; display:block; max-width:24ch; line-height:1.5; margin-top:2px; }}
.split-h {{ display:flex; align-items:baseline; gap:12px; margin:36px 0 18px; }}
.split-h h3 {{ margin:0; font-size:17px; letter-spacing:-.01em; }}
.split-h span {{ font:11px var(--mono); color:var(--ink3); text-transform:uppercase; letter-spacing:.1em; }}
.pf-extra a, .firmlist a {{ color:var(--ink); text-decoration:none;
  border-bottom:1px solid var(--line); }}
.pf-extra a:hover, .firmlist a:hover {{ color:var(--accent); border-color:var(--accent); }}
.firmlist {{ font-size:15px; line-height:2.1; color:var(--ink3); margin:0 0 26px; }}
.pf-extra a, .firmlist a {{ color:var(--ink); text-decoration:none;
  border-bottom:1px solid var(--line); }}
.pf-extra a:hover, .firmlist a:hover {{ color:var(--accent); border-color:var(--accent); }}
.firmlist {{ font-size:15px; line-height:2.1; color:var(--ink3); margin:0 0 26px; max-width:none; }}

table.mx {{ width:100%; border-collapse:collapse; font-size:13.5px; }}
table.mx th, table.mx td {{ border-bottom:1px solid var(--line); padding:11px 10px; text-align:left; vertical-align:top; }}
table.mx thead th {{ font:11px var(--mono); text-transform:uppercase; letter-spacing:.1em; color:var(--ink3); border-bottom:1px solid var(--line); }}
table.mx th[scope=row] {{ font-weight:500; width:30%; }}
.mx-cat {{ display:block; font:10.5px var(--mono); color:var(--ink3); text-transform:uppercase; letter-spacing:.06em; margin-top:2px; }}
td.yes {{ color:var(--ink2); }}
td.yes .dot {{ display:inline-block; width:7px; height:7px; border-radius:50%; margin-right:7px; vertical-align:middle; }}
td.anthropic .dot {{ background:var(--anthropic); }}
td.openai .dot {{ background:var(--openai); }}
td.google .dot {{ background:var(--google); }}
.mx-note {{ font-size:12.5px; }}
td.no {{ color:var(--ink3); }}
td.no::after {{ content:"·"; color:var(--line); }}
.mx-scroll {{ overflow-x:auto; }}

.controls {{ display:flex; flex-wrap:wrap; gap:8px; align-items:center; margin-bottom:26px; }}
.fb {{ background:var(--panel); border:1px solid var(--line); color:var(--ink2); border-radius:999px;
  padding:6px 13px; font-size:12.5px; cursor:pointer; font-family:inherit; }}
.fb em {{ font-style:normal; color:var(--ink3); margin-left:4px; font-size:11px; }}
.fb:hover {{ border-color:var(--ink3); color:var(--ink); }}
.fb.is-on {{ background:var(--accent); border-color:var(--accent); color:#16100d; font-weight:600; }}
.fb.is-on em {{ color:#16100d; opacity:.65; }}
#q {{ background:var(--panel); border:1px solid var(--line); color:var(--ink); border-radius:8px;
  padding:8px 12px; font-size:13px; font-family:inherit; min-width:220px; flex:1; }}
#q::placeholder {{ color:var(--ink3); }}
.pfilter {{ display:flex; gap:6px; }}
.pf-toggle {{ background:transparent; border:1px solid var(--line); color:var(--ink2); border-radius:999px;
  padding:6px 12px; font-size:12px; cursor:pointer; font-family:inherit; }}
.pf-toggle[data-p=anthropic].is-on {{ background:var(--anthropic); border-color:var(--anthropic); color:#16100d; }}
.pf-toggle[data-p=openai].is-on {{ background:var(--openai); border-color:var(--openai); color:#06201a; }}
.pf-toggle[data-p=google].is-on {{ background:var(--google); border-color:var(--google); color:#0a1524; }}

.co-grid {{ display:grid; grid-template-columns:repeat(auto-fill,minmax(330px,1fr)); gap:16px; }}
.co {{ background:var(--panel); border:1px solid var(--line); border-radius:10px; padding:20px; }}
.co-head {{ display:flex; justify-content:space-between; align-items:flex-start; gap:10px; }}
.co h4 {{ margin:0; font-size:17px; letter-spacing:-.01em; }}
.co h4 a {{ text-decoration:none; }}
.co h4 a:hover {{ color:var(--accent); }}
.co-chips {{ display:flex; gap:4px; flex-shrink:0; }}
.chip {{ font:9.5px var(--mono); text-transform:uppercase; letter-spacing:.06em; padding:3px 6px; border-radius:4px; }}
.chip--anthropic {{ background:rgba(217,119,87,.16); color:var(--anthropic); }}
.chip--openai {{ background:rgba(16,163,127,.16); color:var(--openai); }}
.chip--google {{ background:rgba(91,141,239,.16); color:var(--google); }}
.co-meta {{ font:11.5px var(--mono); color:var(--ink3); margin:5px 0 12px; }}
.co-desc {{ font-size:14px; color:var(--ink); margin:0 0 14px; }}
.co-models {{ display:flex; gap:5px; flex-wrap:wrap; margin-bottom:14px; }}
.co-models .m {{ font:10.5px var(--mono); border:1px solid var(--line); color:var(--ink2);
  padding:2px 7px; border-radius:4px; }}
.line--caveat {{ color:var(--ink3); font-style:italic; }}
.co.hide {{ display:none; }}
#count {{ font:12px var(--mono); color:var(--ink3); margin-bottom:16px; }}

.reads {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(280px,1fr)); gap:14px; }}
.read {{ background:var(--panel); border:1px solid var(--line); border-radius:8px; padding:16px; }}
.read a {{ text-decoration:none; font-size:14.5px; }}
.read a:hover {{ color:var(--accent); }}
.read p {{ font-size:12.5px; color:var(--ink2); margin:6px 0 0; }}
footer {{ padding:40px 0 70px; color:var(--ink3); font-size:12.5px; }}
footer p {{ max-width:75ch; }}
@media (max-width:640px) {{
  header.top h1 {{ font-size:26px; }} .lede {{ font-size:17px; }}
  .wrap {{ padding:0 16px; }} table.mx th[scope=row] {{ width:auto; }}
}}
</style>
</head>
<body>

<header class="top"><div class="wrap">
  <h1>Legal AI: the <span>model layer</span><br>and everyone building on it</h1>
  <p>Three foundation-model vendors shipped legal products in four months. Every incumbent had to decide whether to become a connector. This tracks who sells what, and which platform they plugged into.</p>
  <div class="asof">As of {e(companies['as_of'])} &middot; {len(companies['companies'])} entities tracked</div>
  <nav class="jump">
    <a href="#platforms">The platform layer</a>
    <a href="#matrix">Integration matrix</a>
    <a href="#ainative">AI-native firms</a>
    <a href="#companies">Who does what</a>
    <a href="#frictions">Bottlenecks &amp; openings</a>
    <a href="#reading">Reading</a>
  </nav>
</div></header>

<section id="platforms"><div class="wrap">
  <h2>01 &mdash; The platform layer</h2>
  <p class="lede">Anthropic went first in May and chose <strong>distribution</strong>: put the workflow inside Claude and make every vendor a connector. Google went in August and chose <strong>integration</strong>: don't own the workflow, be the substrate, sell through the SIs. OpenAI went in September and chose <strong>content</strong>: own primary-law retrieval, then sell direct to the Am Law 200. Same market, three different bets about where the value sits.</p>
  <div class="pf-grid">
{platform_cards()}
  </div>
</div></section>

<section id="matrix"><div class="wrap">
  <h2>02 &mdash; Integration matrix</h2>
  <p class="lede">Who has plugged into which platform. The pattern worth noticing: almost nobody picked one. Harvey, Legora, Thomson Reuters and iManage all sit in multiple ecosystems &mdash; and so do the firms. <strong>Being a connector everywhere is the hedge against being disintermediated anywhere.</strong></p>
  <div class="mx-scroll"><table class="mx">
    <thead><tr><th>Company</th><th>Anthropic</th><th>OpenAI</th><th>Google</th></tr></thead>
    <tbody>
{matrix_rows()}
    </tbody>
  </table></div>
</div></section>

<section id="ainative"><div class="wrap">
  <h2>03 &mdash; AI-native law firms</h2>
  <p class="lede">The smallest segment and the only one not retrofitting. These are <strong>regulated law firms</strong>, not software: the first pass is a model, the lawyer is the last checkpoint, and the price is per artefact or per outcome rather than per hour. {len(AI_FIRMS)} tracked here &mdash; the category directory counts just over 50 globally, 31 of them US.</p>
  <div class="callout">
    <h4>The unlock is regulatory, not technical</h4>
    <p>You cannot build this firm in most US states. Non-lawyer ownership is the blocker, and
    <strong>Arizona's Alternative Business Structure programme</strong> is the workaround &mdash; 100+ ABSs approved
    since 2021, including KPMG Law. Justpoint Law took the first ABS licence for an AI-native PI and mass tort
    firm in July 2025; Manifest is incubating its first firm the same way. In the UK the equivalent precedent is
    <strong>Garfield AI</strong>, the first fully AI-driven firm authorised by the SRA.</p>
    <p>So the question underneath this whole segment isn't whether the models are good enough. It's whether a
    second US state follows Arizona &mdash; and what happens to UPL and fee-sharing rules when one does.</p>
  </div>
  <p class="firmlist">{AI_NAMES}</p>
  <div class="reads">{AI_REFS}</div>
</div></section>

<section id="companies"><div class="wrap">
  <h2>04 &mdash; Who does what</h2>
  <p class="lede">The app layer, sorted by what it actually sells. Filter by segment, or by which model platform a company has publicly connected to.</p>
  <div class="controls">
{filter_buttons()}
  </div>
  <div class="controls">
    <input id="q" type="search" placeholder="Search name, product, geography, model&hellip;" autocomplete="off">
    <div class="pfilter">
      <button class="pf-toggle" data-p="anthropic">Anthropic</button>
      <button class="pf-toggle" data-p="openai">OpenAI</button>
      <button class="pf-toggle" data-p="google">Google</button>
    </div>
  </div>
  <div id="count"></div>
  <div class="co-grid" id="grid">
{company_cards()}
  </div>
</div></section>

<section id="frictions"><div class="wrap">
  <h2>05 &mdash; Where it's stuck, and what's open</h2>
  <p class="lede">The capability argument is mostly over. What's left is a set of problems that are commercial, organisational and regulatory &mdash; and the gaps those leave are the actual opportunity. <strong>Almost none of the stated blockers are about whether the models are good enough.</strong></p>

  <div class="split-h"><h3>Bottlenecks</h3><span>What is actually holding it up</span></div>
  <div class="fr-grid">
{friction_cards("bottlenecks", "block")}
  </div>

  <div class="split-h"><h3>Openings</h3><span>What nobody has built yet</span></div>
  <div class="fr-grid">
{friction_cards("opportunities", "opp")}
  </div>
</div></section>

<section id="reading"><div class="wrap">
  <h2>06 &mdash; Reading</h2>
  <div class="reads">
    <div class="read"><a href="https://helenfan1.substack.com/" target="_blank" rel="noopener">Helen's Legal AI Lab &mdash; Helen Fan</a>
      <p>The Legal AI Value Stack (V2): five levels from raw model, to workflow redesigned around agents, to a self-learning data layer within client and ethical-wall boundaries, to AI as system of record, to the AI-native firm. The most useful framework for judging whether a vendor has anything defensible.</p></div>
    <div class="read"><a href="https://www.lawnext.com/" target="_blank" rel="noopener">LawSites &mdash; Bob Ambrogi</a>
      <p>Still the fastest, most sceptical reporting on launches. His framing of the Anthropic launch &mdash; how much appetite does a model vendor have to compete in legal, and how do vendors built on it respond &mdash; is the open question of the year.</p></div>
    <div class="read"><a href="https://www.artificiallawyer.com/" target="_blank" rel="noopener">Artificial Lawyer</a>
      <p>Europe-weighted, opinionated, early on the AI-native firm and regulatory-authorisation stories.</p></div>
    <div class="read"><a href="https://www.legaltechnologyhub.com/" target="_blank" rel="noopener">Legaltech Hub</a>
      <p>The closest thing to a maintained vendor directory; useful for checking whether a product is real or a landing page.</p></div>
  </div>
</div></section>

<footer><div class="wrap">
  <p>Compiled from public reporting and vendor announcements. Valuations and funding are as last publicly reported and go stale fast. &ldquo;Models&rdquo; reflects publicly disclosed foundation-model use only &mdash; most vendors are multi-model and do not disclose routing, so an empty field means undisclosed, not none. Entries carrying a caveat line are lower-confidence. Bracketed numbers link to sources.</p>
</div></footer>

<script>
(function(){{
  var grid=document.getElementById('grid'), cards=[].slice.call(grid.querySelectorAll('.co'));
  var q=document.getElementById('q'), count=document.getElementById('count');
  var cat='all', plats=[];
  function apply(){{
    var t=q.value.trim().toLowerCase(), n=0;
    cards.forEach(function(c){{
      var ok=(cat==='all'||c.dataset.cat===cat)
        && (!t||c.dataset.search.indexOf(t)>-1)
        && plats.every(function(p){{return c.dataset[p]==='1';}});
      c.classList.toggle('hide',!ok); if(ok) n++;
    }});
    count.textContent=n+(n===1?' entity':' entities');
  }}
  document.querySelectorAll('.fb').forEach(function(b){{
    b.addEventListener('click',function(){{
      document.querySelectorAll('.fb').forEach(function(x){{x.classList.remove('is-on');}});
      b.classList.add('is-on'); cat=b.dataset.cat; apply();
    }});
  }});
  document.querySelectorAll('.pf-toggle').forEach(function(b){{
    b.addEventListener('click',function(){{
      var p=b.dataset.p, i=plats.indexOf(p);
      if(i>-1){{plats.splice(i,1);b.classList.remove('is-on');}}
      else{{plats.push(p);b.classList.add('is-on');}}
      apply();
    }});
  }});
  q.addEventListener('input',apply);
  apply();
}})();
</script>
</body>
</html>
"""

(SITE / "index.html").write_text(HTML)
(SITE / "data.json").write_text(json.dumps({"platforms": platforms, "companies": companies}, indent=2))
(SITE / ".nojekyll").write_text("")
print(f"built docs/index.html  ({len(HTML):,} bytes, {len(companies['companies'])} companies, {len(platforms['platforms'])} platforms)")
