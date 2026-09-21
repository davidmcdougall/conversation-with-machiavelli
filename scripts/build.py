#!/usr/bin/env python3
"""Build the reading page for one pair from the established sources.

Emits two files:
  site/content.html   page content only (no doctype/html/head/body) — Artifact input
  site/index.html     the same content wrapped as a full document — GitHub Pages
Nothing here is hand-typed from the texts; everything is read from corpus/ and
translations/ so the published text cannot drift from the established text.
"""
import re, pathlib, html, datetime

ROOT = pathlib.Path(__file__).resolve().parent.parent

def parse(path):
    t = (ROOT / path).read_text(encoding="utf-8")
    _, fm, body = t.split("---", 2)
    meta = {}
    for line in fm.splitlines():
        m = re.match(r'^([a-z_]+):\s*(.*)$', line)
        if m:
            v = m.group(2).strip()
            v = re.sub(r'\s+#.*$', '', v).strip().strip('"')
            meta[m.group(1)] = v
    body = body.split("\n---\n")[0]          # drop any Notes block
    paras = {}
    for m in re.finditer(r'^## (\S+)\s*\n+(.+?)(?=\n## |\Z)', body, re.S | re.M):
        paras[m.group(1)] = " ".join(m.group(2).split())
    return meta, paras

nm_it_m, nm_it = parse("corpus/NM-DISC/NM-DISC.1.12.md")
nm_en_m, nm_en = parse("translations/NM-DISC.1.12.md")
fg_it_m, fg_it = parse("corpus/FG-CONS/FG-CONS.1.12.md")
fg_en_m, fg_en = parse("translations/FG-CONS.1.12.md")

def esc(s):
    s = html.escape(s)
    # Canestrini's supplied letters, and the Latin tag, get marked up
    s = s.replace("[ar]", '<span class="supplied">[ar]</span>')
    s = s.replace("vis venire Romam?", '<i lang="la">vis venire Romam?</i>')
    s = s.replace("*virtù*", '<i lang="it">virtù</i>')
    return s

def rows(it, en, ids):
    out = []
    for i in ids:
        out.append(
f'''      <div class="pair" id="{i}">
        <div class="gutter"><a class="uid" href="#{i}">{i.split(".",1)[1]}</a></div>
        <div class="col it" lang="it">{esc(it[i])}</div>
        <div class="col en" lang="en">{esc(en[i])}</div>
      </div>''')
    return "\n".join(out)

nm_ids = [f"NM-DISC.1.12.{n:02d}" for n in range(1, 8)]
fg_ids = [f"FG-CONS.1.12.{n:02d}" for n in range(1, 4)]

CONTENT = f'''<title>A Conversation with Machiavelli</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;1,400&family=IBM+Plex+Mono:wght@400&family=IBM+Plex+Sans:wght@400;500;600&display=swap">
<style>
:root {{
  --paper:      #EDEEEC;
  --paper-sunk: #E4E6E3;
  --ink:        #1B1E1C;
  --ink-muted:  #5C625E;
  --ink-faint:  #868C87;
  --rule:       #C9CDC8;
  --rule-faint: #DCDFDB;
  --nm:         #3A5A6B;
  --fg:         #6E5A3C;
  --serif: "EB Garamond", "Iowan Old Style", Palatino, "Palatino Linotype", Georgia, serif;
  --sans:  "IBM Plex Sans", -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif;
  --mono:  "IBM Plex Mono", ui-monospace, "SF Mono", Menlo, Consolas, monospace;
}}
@media (prefers-color-scheme: dark) {{
  :root:not([data-theme="light"]) {{
    --paper:      #161917;
    --paper-sunk: #1D211E;
    --ink:        #E3E6E1;
    --ink-muted:  #A0A6A0;
    --ink-faint:  #767C77;
    --rule:       #343934;
    --rule-faint: #262B27;
    --nm:         #8FB4C6;
    --fg:         #C4A97C;
  }}
}}
:root[data-theme="dark"] {{
  --paper:      #161917;
  --paper-sunk: #1D211E;
  --ink:        #E3E6E1;
  --ink-muted:  #A0A6A0;
  --ink-faint:  #767C77;
  --rule:       #343934;
  --rule-faint: #262B27;
  --nm:         #8FB4C6;
  --fg:         #C4A97C;
}}

body {{
  background: var(--paper);
  color: var(--ink);
  font-family: var(--serif);
  font-size: 17px;
  line-height: 1.62;
  -webkit-font-smoothing: antialiased;
}}
.wrap {{ max-width: 1160px; margin: 0 auto; padding-inline: 20px; padding-block: 0 0; }}

/* ---- masthead ---- */
.masthead {{ padding-block: 56px 32px; border-bottom: 1px solid var(--rule); }}
.eyebrow {{
  font-family: var(--sans); font-size: 11px; font-weight: 600;
  letter-spacing: .14em; text-transform: uppercase; color: var(--ink-faint);
  margin: 0 0 18px;
}}
h1 {{
  font-family: var(--serif); font-weight: 400; font-size: clamp(30px, 5vw, 44px);
  line-height: 1.12; margin: 0 0 14px; text-wrap: balance; letter-spacing: -0.01em;
}}
h1 .sub {{ display: block; font-style: italic; color: var(--ink-muted); font-size: .52em; margin-top: 12px; letter-spacing: 0; }}
.standfirst {{
  font-family: var(--sans); font-size: 14.5px; line-height: 1.6;
  color: var(--ink-muted); max-width: 62ch; margin: 0;
}}

/* ---- the pairing device ---- */
.pairing {{
  display: flex; align-items: stretch; gap: 0; margin: 30px 0 0;
  border: 1px solid var(--rule); border-radius: 2px; overflow: hidden;
  font-family: var(--sans); background: var(--paper-sunk);
}}
.pairing > div {{ flex: 1 1 0; padding: 13px 16px; min-width: 0; }}
.pairing .who {{ font-size: 11px; font-weight: 600; letter-spacing: .1em; text-transform: uppercase; margin-bottom: 4px; }}
.pairing .nm-side .who {{ color: var(--nm); }}
.pairing .fg-side .who {{ color: var(--fg); }}
.pairing .what {{ font-size: 13.5px; color: var(--ink-muted); }}
.pairing .arrow {{
  flex: 0 0 auto; display: flex; align-items: center; justify-content: center;
  padding-inline: 14px; color: var(--ink-faint); font-size: 15px;
  border-inline: 1px solid var(--rule);
}}

/* ---- work sections ---- */
.work {{ padding-block: 52px 0; }}
.work-head {{ display: flex; align-items: baseline; gap: 14px; flex-wrap: wrap; margin-bottom: 6px; }}
.work-head .tag {{
  font-family: var(--mono); font-size: 11px; letter-spacing: .04em;
  padding: 3px 7px; border-radius: 2px; color: var(--paper);
}}
.work.nm .tag {{ background: var(--nm); }}
.work.fg .tag {{ background: var(--fg); }}
h2 {{ font-family: var(--serif); font-weight: 500; font-size: 25px; margin: 0; letter-spacing: -0.005em; }}
.rubric {{
  font-style: italic; color: var(--ink-muted); max-width: 70ch;
  margin: 10px 0 0; font-size: 16.5px; line-height: 1.5;
}}
.rubric-note {{
  font-family: var(--sans); font-style: normal; font-size: 12px;
  color: var(--ink-faint); margin-top: 7px;
}}
.colheads {{
  display: grid; grid-template-columns: 54px 1fr 1fr; gap: 0 30px;
  margin-top: 30px; padding-bottom: 7px; border-bottom: 1px solid var(--rule);
  font-family: var(--sans); font-size: 10.5px; font-weight: 600;
  letter-spacing: .13em; text-transform: uppercase; color: var(--ink-faint);
}}

/* ---- the facing pair ---- */
.pair {{
  display: grid; grid-template-columns: 54px 1fr 1fr; gap: 0 30px;
  padding-block: 22px; border-bottom: 1px solid var(--rule-faint);
  scroll-margin-top: 20px;
}}
.pair:target {{ background: var(--paper-sunk); }}
.gutter {{ padding-top: 4px; }}
.uid {{
  font-family: var(--mono); font-size: 10.5px; color: var(--ink-faint);
  text-decoration: none; letter-spacing: -0.02em;
}}
.uid:hover, .uid:focus {{ color: var(--ink); text-decoration: underline; }}
.col {{ min-width: 0; }}
.col.it {{ hyphens: auto; }}
.col.en {{ }}
.supplied {{ color: var(--ink-muted); }}

/* ---- apparatus ---- */
.apparatus {{
  margin-top: 34px; padding-top: 22px; border-top: 2px solid var(--rule);
  font-family: var(--sans); font-size: 13.5px; line-height: 1.58;
  color: var(--ink-muted);
  display: grid; grid-template-columns: repeat(auto-fit, minmax(270px, 1fr)); gap: 26px 34px;
}}
.apparatus h3 {{
  font-family: var(--sans); font-size: 10.5px; font-weight: 600; letter-spacing: .13em;
  text-transform: uppercase; color: var(--ink-faint); margin: 0 0 9px;
}}
.apparatus p {{ margin: 0 0 9px; }}
.apparatus p:last-child {{ margin-bottom: 0; }}
.apparatus .lem {{ font-family: var(--serif); font-size: 15px; color: var(--ink); font-style: italic; }}
.sig {{ font-family: var(--mono); font-size: 12px; color: var(--ink); }}

/* ---- colophon ---- */
.colophon {{
  margin-top: 60px; padding-block: 28px 60px; border-top: 1px solid var(--rule);
  font-family: var(--sans); font-size: 13px; line-height: 1.6; color: var(--ink-muted);
}}
.colophon .row {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 24px 34px; }}
.colophon h3 {{
  font-size: 10.5px; font-weight: 600; letter-spacing: .13em; text-transform: uppercase;
  color: var(--ink-faint); margin: 0 0 8px;
}}
.colophon p {{ margin: 0 0 8px; }}
.colophon ul {{ margin: 0; padding-left: 16px; }}
.colophon li {{ margin-bottom: 5px; }}
.state {{
  margin-top: 26px; padding: 14px 16px; background: var(--paper-sunk);
  border-left: 2px solid var(--ink-faint); border-radius: 0 2px 2px 0;
  font-size: 12.5px;
}}
.state strong {{ color: var(--ink); font-weight: 600; }}
a {{ color: inherit; }}
:focus-visible {{ outline: 2px solid var(--nm); outline-offset: 2px; }}

@media (max-width: 760px) {{
  body {{ font-size: 16.5px; }}
  .colheads {{ display: none; }}
  .pair {{ grid-template-columns: 1fr; gap: 0; padding-block: 20px; }}
  .gutter {{ padding-top: 0; margin-bottom: 8px; }}
  .col.it {{ margin-bottom: 14px; padding-bottom: 14px; border-bottom: 1px dotted var(--rule); }}
  .col.it::before, .col.en::before {{
    display: block; font-family: var(--sans); font-size: 10px; font-weight: 600;
    letter-spacing: .13em; text-transform: uppercase; color: var(--ink-faint); margin-bottom: 6px;
  }}
  .col.it::before {{ content: "Italian"; }}
  .col.en::before {{ content: "English"; }}
  .pairing {{ flex-direction: column; }}
  .pairing .arrow {{ border-inline: 0; border-block: 1px solid var(--rule); padding-block: 6px; }}
}}
</style>

<div class="wrap">

  <header class="masthead">
    <p class="eyebrow">A Conversation with Machiavelli · Pair 12 of 39</p>
    <h1>Religion, and the ruin of Italy
      <span class="sub">Discourses I.12, and Guicciardini's reply</span></h1>
    <p class="standfirst">Machiavelli argues that a state must keep its religion uncorrupted, and that the
      Roman Church has ruined Italy twice over — by its example, and by keeping the peninsula divided.
      Guicciardini, reading him some fifteen years later, goes further than Machiavelli on the first charge,
      grants the premise of the second, and then declines to draw his conclusion.</p>

    <div class="pairing">
      <div class="nm-side">
        <div class="who">Niccolò Machiavelli</div>
        <div class="what">Discorsi sopra la prima Deca di Tito Livio, I.12 · written c. 1513–19, printed 1531</div>
      </div>
      <div class="arrow" aria-hidden="true">answered by</div>
      <div class="fg-side">
        <div class="who">Francesco Guicciardini</div>
        <div class="what">Considerazioni intorno ai Discorsi del Machiavelli · written 1529–30, printed 1857</div>
      </div>
    </div>
  </header>

  <section class="work nm">
    <div class="work-head">
      <span class="tag">NM-DISC.1.12</span>
      <h2>Capitolo XII</h2>
    </div>
    <p class="rubric">{html.escape(nm_it_m["rubric"])}</p>
    <p class="rubric">{html.escape(nm_en_m["rubric_en"])}</p>

    <div class="colheads"><div></div><div>Italian · 1824</div><div>English</div></div>
{rows(nm_it, nm_en, nm_ids)}

    <div class="apparatus">
      <div>
        <h3>Source</h3>
        <p>Established from the 1824 edition (<span class="sig">WIT-NM-DISC-1824-IA</span>), page-image-backed,
          which governs. Collated against the 1554 Giglio printing, Venice
          (<span class="sig">WIT-NM-DISC-1554-IA</span>), which is comparison evidence only.</p>
        <p>Paragraph divisions are editorial. The witness prints the chapter as one unbroken block.</p>
      </div>
      <div>
        <h3>Variants</h3>
        <p><span class="lem">l'oracolo di Delo</span> — 1824. The 1554 witness reads <i>Delfo</i>, Delphi.</p>
        <p><span class="lem">gli augumentano</span> — 1824. 1554: <i>gli aumentano</i>.</p>
        <p><span class="lem">declinazione</span> — 1824. 1554: <i>declinatione</i>.</p>
        <p>The two editions transmit different argument structures at <a href="#NM-DISC.1.12.05">.05</a>:
          where 1824 has Machiavelli's two charges against Rome, 1554 has a different passage entirely.
          The 1824 structure is canonical here; the divergence is recorded, not resolved.</p>
      </div>
      <div>
        <h3>Notes</h3>
        <p><span class="lem">hanno meno religione</span> (.04) — the witness capitalises <i>Religione</i>
          throughout this chapter, four times on the same page, and drops the capital at exactly this phrase.
          English cannot carry the distinction.</p>
        <p><span class="lem">virtù</span> (.06) — left untranslated. Machiavelli sets it beside <i>potente</i>
          in the same clause, so it is not simply power; and it is plainly not moral virtue.</p>
        <p><span class="lem">vis venire Romam?</span> (.03) — “Do you wish to come to Rome?”</p>
      </div>
    </div>
  </section>

  <section class="work fg">
    <div class="work-head">
      <span class="tag">FG-CONS.1.12</span>
      <h2>Considerazione sul capitolo XII</h2>
    </div>
    <p class="rubric">{html.escape(fg_it_m["rubric"])}</p>
    <p class="rubric">{html.escape(fg_en_m["rubric_en"])}
      <span class="rubric-note">Canestrini's own setting of the chapter title over the reply — note the
        lower-case <i>religione</i> and <i>romana</i> — not a reprint of the 1824 heading.</span></p>

    <div class="colheads"><div></div><div>Italian · 1857</div><div>English</div></div>
{rows(fg_it, fg_en, fg_ids)}

    <div class="apparatus">
      <div>
        <h3>Source</h3>
        <p>Established from Canestrini 1857, <i>Opere inedite</i> vol. 1, pp. 1–65
          (<span class="sig">WIT-FG-CONS-1857-CANESTRINI</span>) — the <i>editio princeps</i>, which governs.
          Collated against Palmarocchi 1933 (<span class="sig">WIT-FG-CONS-1933-PALMAROCCHI</span>),
          page images only, consultation evidence under the project's licensing rule.</p>
        <p>Paragraph divisions are editorial. The witness prints the reply as one unbroken block.</p>
      </div>
      <div>
        <h3>Variants</h3>
        <p><span class="lem">non [ar]ebbe patito</span> (.03) — Canestrini supplies the bracketed letters;
          the brackets are his and are kept. Palmarocchi prints <i>arebbe</i> unbracketed.</p>
        <p><span class="lem">in varii tempi</span> (.03) — Canestrini's spelling retained;
          Palmarocchi has <i>vari</i>.</p>
        <p>Capitalisation, punctuation and word division follow Canestrini throughout.
          No reading is hybridised between the two witnesses.</p>
      </div>
      <div>
        <h3>Notes</h3>
        <p><span class="lem">io non concorro facilmente</span> — “I do not readily concur”. Machiavelli
          writes that he will <i>discorrere</i> the reasons that <i>occorrono</i> to him; Guicciardini answers
          that he does not <i>concorrere</i>. Three compounds of <i>currere</i> survive intact into English,
          and the translation holds all three so the answer stays audible.</p>
        <p><span class="lem">però</span> (twice, .03) — consecutive, <i>per ciò</i>: therefore, not however.</p>
        <p><span class="lem">milita</span> (.03) — the Latinate argumentative sense: the reason has no force.
          Modern English “militate” survives mostly in “militate against”, which pulls the other way.</p>
      </div>
    </div>
  </section>

  <footer class="colophon">
    <div class="row">
      <div>
        <h3>What this is</h3>
        <p>A free, openly licensed, bilingual edition of Guicciardini's 39 <i>Considerazioni</i> and the
          <i>Discorsi</i> chapters they answer — 78 text units, Italian and English facing, every reading
          traceable to a named public-domain witness.</p>
        <p>It is a reading edition with a transparent apparatus, not a text of record. It does not adjudicate
          the critical text against Bausi 2001 or the manuscript tradition, and does not claim to.</p>
      </div>
      <div>
        <h3>On the title</h3>
        <p>Machiavelli had been dead two years when Guicciardini wrote; the <i>Discorsi</i> were unpublished,
          and the <i>Considerazioni</i> stayed unprinted until 1857. Machiavelli never answers.</p>
        <p>“Conversation” is a quotation, not a description. It invokes Machiavelli's letter to Vettori of
          10 December 1513, where he changes into court dress at evening, enters the antique courts of ancient
          men, and reports that <i>they, in their humanity, answer me</i>. Guicciardini does to Machiavelli
          what Machiavelli did to Livy — and is denied the reply Machiavelli claimed.</p>
      </div>
      <div>
        <h3>Method</h3>
        <p>No image-derived reading enters the text on a single reading. Each unit is transcribed twice,
          independently, by readers who have not seen each other's work; disagreements are adjudicated against
          the page images and recorded.</p>
        <p>Existing English translations of the <i>Considerazioni</i> — Grayson (1965), Atkinson &amp; Sices
          (2002) — are never used as translation inputs.</p>
      </div>
    </div>

    <div class="state">
      <p><strong>Version 0.3 · {datetime.date.today().isoformat()} · 1 pair of 39.</strong>
        This edition is versioned, not frozen. Two questions are open on this pair and are recorded rather
        than hidden: whether <i>consuetudine</i> and <i>costume</i> should share one English word, and whether
        the full stop closing Guicciardini's reply is his or his editor's — the witness prints none.</p>
    </div>
  </footer>

</div>'''

site = ROOT / "site"
(site / "content.html").write_text(CONTENT, encoding="utf-8")
(site / "index.html").write_text(
  '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
  '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
  '<meta name="description" content="Machiavelli, Discourses I.12, and Guicciardini\'s reply: '
  'Italian and English facing, with a transparent apparatus.">\n'
  '<style>*{box-sizing:border-box}body{margin:0;font:14px system-ui}img{max-width:100%}'
  '[hidden]{display:none!important}</style>\n'
  + CONTENT + '\n</body>\n</html>\n', encoding="utf-8")
print("site/content.html", (site/"content.html").stat().st_size, "bytes")
print("site/index.html  ", (site/"index.html").stat().st_size, "bytes")
print("paragraphs:", len(nm_it), "NM /", len(fg_it), "FG")
assert set(nm_it) == set(nm_en) == set(nm_ids), "NM paragraph ids do not align"
assert set(fg_it) == set(fg_en) == set(fg_ids), "FG paragraph ids do not align"
print("alignment check: Italian and English paragraph ids match in both works")
