#!/usr/bin/env python3
"""Build the reading page for one pair of A Conversation with Machiavelli.

Usage:
  scripts/build.py <pair>     build one pair, e.g. "1.12" or "2.proem", reporting
                              on it, then quietly refresh every other published
                              pair (footers and pair navigation change on every
                              page when a pair is added; CI rejects a stale site/)
  scripts/build.py --all      rebuild every published pair, then the index
  scripts/build.py --index    rebuild only the index (site/index.html)

A pair is "published" when both translations/NM-DISC.<pair>.md and
translations/FG-CONS.<pair>.md exist. Building a pair emits:
  site/pairs/<pair>-content.html   page content only — Artifact input
  site/pairs/<pair>.html           the same content wrapped as a full document
and always refreshes, across every published pair:
  site/index-content.html          contents page, content only
  site/index.html                  contents page, full document — GitHub Pages home
  site/about.html                  what the edition is, title, method, licence (once,
                                   not repeated in every page's footer)
Fonts are self-hosted from site/fonts/ (fonts.css plus woff2 files, SIL OFL).

Nothing here is hand-typed from the texts or about a specific pair:
  - paragraph text comes from corpus/ (Italian) and translations/ (English)
  - a pair's editor's summary (standfirst) and translator's notes come from that pair's
    translation front-matter and its "## Notes" section
  - source and variant apparatus come from sources/provenance/ and
    sources/comparisons/ (AGENTS.md rule 4: witness decisions become source
    notes, collation notes become variant notes)
  - commentary under each paragraph comes from annotations/<unit>.md (stage 5)
  - a pair's position ("Pair N of 39") comes from links/pairing-map.md
  - the edition version comes from SCOPE.md
The only per-work constants kept in this script are bibliographic facts true
of every pair that work answers for (which four witnesses govern the whole
corpus) and the authors' fixed biographical line — see WORKS below, sourced
from SCOPE §4.
"""
import re
import sys
import html
import pathlib
import argparse
import datetime
import os
import subprocess

try:
    import yaml
except ImportError:
    sys.exit("This script needs PyYAML: pip install pyyaml --break-system-packages")

ROOT = pathlib.Path(__file__).resolve().parent.parent

# ---------------------------------------------------------------------------
# Fixed, work-level bibliographic facts (SCOPE §4). These are true of every
# pair a work answers for, so they belong here rather than in any one pair's
# front-matter.
# ---------------------------------------------------------------------------
WORKS = {
    "NM-DISC": dict(
        author="Niccolò Machiavelli",
        work_title="Discorsi sopra la prima Deca di Tito Livio",
        work_dates="written c. 1513–19, printed 1531",
        source_citation=(
            'Established from the 1824 edition (<span class="sig">WIT-NM-DISC-1824-IA</span>), '
            "page-image-backed, which governs. Collated against the 1554 Giglio printing, Venice "
            '(<span class="sig">WIT-NM-DISC-1554-IA</span>), which is comparison evidence only.'
        ),
        edition_year="1824",
    ),
    "FG-CONS": dict(
        author="Francesco Guicciardini",
        work_title="Considerazioni intorno ai Discorsi del Machiavelli",
        work_dates="written 1529–30, printed 1857",
        source_citation=(
            "Established from Canestrini 1857, <i>Opere inedite</i> vol. 1, pp. 1–65 "
            '(<span class="sig">WIT-FG-CONS-1857-CANESTRINI</span>) — the <i>editio princeps</i>, '
            "which governs. Collated against Palmarocchi 1933 "
            '(<span class="sig">WIT-FG-CONS-1933-PALMAROCCHI</span>): page images and the '
            "Wikisource transcription consulted as collation evidence, not reproduced "
            "(RIGHTS_AND_SOURCES.md)."
        ),
        edition_year="1857",
    ),
}

# ---------------------------------------------------------------------------
# Parsing: unit files, front-matter, notes, YAML apparatus sources
# ---------------------------------------------------------------------------

FM_LINE = re.compile(r'^([a-z_]+):\s*(.*)$')
PARA_RE = re.compile(r'^## (\S+)\s*\n+(.+?)(?=\n## |\Z)', re.S | re.M)


def parse_frontmatter(fm_text):
    meta = {}
    for line in fm_text.splitlines():
        m = FM_LINE.match(line)
        if m:
            v = m.group(2).strip()
            v = re.sub(r'\s+#.*$', '', v).strip().strip('"')
            meta[m.group(1)] = v
    return meta


def extract_paragraphs(body):
    paras = {}
    for m in PARA_RE.finditer(body):
        paras[m.group(1)] = " ".join(m.group(2).split())
    return paras


def para_order(ids):
    def key(i):
        tail = i.rsplit(".", 1)[1]
        return (0, int(tail)) if tail.isdigit() else (1, tail)
    return sorted(ids, key=key)


def parse_corpus(unit_id, work_id):
    path = ROOT / f"corpus/{work_id}/{unit_id}.md"
    t = path.read_text(encoding="utf-8")
    _, fm_text, body = t.split("---", 2)
    meta = parse_frontmatter(fm_text)
    body = body.split("\n---\n")[0]
    return meta, extract_paragraphs(body)


def parse_translation(unit_id, work_id):
    path = ROOT / f"translations/{unit_id}.md"
    t = path.read_text(encoding="utf-8")
    _, fm_text, rest = t.split("---", 2)
    meta = parse_frontmatter(fm_text)
    parts = rest.split("\n---\n")
    body = parts[0]
    notes_raw = parts[1] if len(parts) > 1 else ""
    notes_raw = re.sub(r'^\s*## Notes\s*\n', '', notes_raw.strip())
    return meta, extract_paragraphs(body), notes_raw


def load_yaml(rel_path):
    p = ROOT / rel_path
    if not p.exists():
        return None
    return yaml.safe_load(p.read_text(encoding="utf-8"))


def pairing_map():
    """The 39 pairs, in canonical order, from links/pairing-map.md."""
    text = (ROOT / "links/pairing-map.md").read_text(encoding="utf-8")
    rows = []
    for m in re.finditer(
        r'^\|\s*(\d+)\s*\|\s*(NM-DISC\.\S+?)\s*\|\s*(FG-CONS\.\S+?)\s*\|', text, re.M
    ):
        rows.append({"n": int(m.group(1)), "nm": m.group(2), "fg": m.group(3)})
    return rows


def edition_version():
    text = (ROOT / "SCOPE.md").read_text(encoding="utf-8")
    m = re.search(r'\*\*Version\.\*\*\s*Draft\s*(\S+)', text)
    return m.group(1) if m else "?"


# ---------------------------------------------------------------------------
# Page dates (SCOPE §7: "date every page"), derived from git, never typed
# ---------------------------------------------------------------------------

def _git(*args):
    """Read-only git query; GIT_OPTIONAL_LOCKS=0 keeps `status` from taking index.lock."""
    try:
        out = subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True, text=True,
                             env=dict(os.environ, GIT_OPTIONAL_LOCKS="0"), check=True)
        return out.stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return None


def pair_sources(pair):
    nm, fg = f"NM-DISC.{pair}", f"FG-CONS.{pair}"
    return [f"corpus/NM-DISC/{nm}.md", f"corpus/FG-CONS/{fg}.md",
            f"translations/{nm}.md", f"translations/{fg}.md",
            f"annotations/{nm}.md", f"annotations/{fg}.md",
            f"sources/provenance/NM-DISC/{nm}-establishment.yml",
            f"sources/provenance/FG-CONS/{fg}-establishment.yml",
            f"sources/comparisons/NM-DISC/{nm}-witness-disagreements.yml",
            f"sources/comparisons/FG-CONS/{fg}-witness-disagreements.yml"]


# Front-matter fields that record provenance, not text. A commit whose changes to a
# pair's files only add, remove or alter lines starting with these keys is not a
# revision of anything a reader sees, and does not move the pair's "last revised" date.
METADATA_KEYS = ("model:", "cold_review:")


def last_text_revision(paths):
    """Date of the last commit touching paths that changed more than metadata lines."""
    log = _git("log", "--format=%H %cs", "--", *paths) or ""
    for line in log.splitlines():
        sha, date = line.split()
        diff = _git("show", "--format=", "--unified=0", sha, "--", *paths) or ""
        changed = [l[1:] for l in diff.splitlines()
                   if l[:1] in "+-" and not l.startswith(("+++ ", "--- "))]
        if any(not c.startswith(METADATA_KEYS) for c in changed):
            return date
    return None


def pair_dates(pair):
    """(published, revised) as ISO dates.

    published: the commit that first added site/pairs/<pair>.html; today if not yet committed.
    revised: today if any of the pair's text or apparatus files has uncommitted changes;
    otherwise the date of the last commit touching them. Rebuilding an unchanged pair
    therefore leaves its dates unchanged.
    """
    today = datetime.date.today().isoformat()
    paths = [s for s in pair_sources(pair) if (ROOT / s).exists()]
    added = _git("log", "--diff-filter=A", "--format=%cs", "--", f"site/pairs/{pair}.html")
    published = added.splitlines()[-1] if added else today
    dirty = _git("status", "--porcelain", "--", *paths)
    if dirty is None or dirty:
        revised = today
    else:
        revised = last_text_revision(paths) or today
    return published, max(published, revised)


def long_date(iso):
    d = datetime.date.fromisoformat(iso)
    return f"{d.day} {d.strftime('%B')} {d.year}"


def dates_line(pair):
    published, revised = pair_dates(pair)
    line = f"Published {long_date(published)}"
    if revised != published:
        line += f"; last revised {long_date(revised)}"
    return line + "."


def discover_published():
    """Rows from the pairing map that have both translations on disk."""
    out = []
    for row in pairing_map():
        pair = row["nm"].split(".", 1)[1]
        if (ROOT / f"translations/{row['nm']}.md").exists() and \
           (ROOT / f"translations/{row['fg']}.md").exists():
            out.append(dict(row, pair=pair))
    return out


# ---------------------------------------------------------------------------
# Text formatting
# ---------------------------------------------------------------------------

ROMAN_VALS = [
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"),
    (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"),
]


def roman(n):
    out = []
    for v, s in ROMAN_VALS:
        while n >= v:
            out.append(s)
            n -= v
    return "".join(out)


def nm_heading(pair, meta=None):
    """The Machiavelli column's heading, as the 1824 witness heads the unit:
    CAPITOLO N, or for a unit with no chapter number the witness's own
    heading from the corpus front-matter (`heading`), e.g. the Book II
    half-title LIBRO SECONDO over the proem (D421)."""
    _, ch = pair.split(".", 1)
    if ch.isdigit():
        return f"Capitolo {roman(int(ch))}"
    h = (meta or {}).get("heading", "")
    return h.capitalize() if h else ch.capitalize()


def fg_heading(pair, meta=None):
    """The Guicciardini column's heading, as Canestrini prints it: he adds
    `del libro II` (III) to every reply after Book I, and heads the proem's
    reply `Considerazione sul proemio del libro II` (D421)."""
    book, ch = pair.split(".", 1)
    if (meta or {}).get("heading"):
        return meta["heading"]
    of_book = f" del libro {roman(int(book))}" if book != "1" else ""
    if ch.isdigit():
        return f"Considerazione sul capitolo {roman(int(ch))}{of_book}"
    return f"Considerazione sul proemio{of_book}" if ch == "proem" else f"Considerazione sul {ch}{of_book}"


def rubric_lines(it_m, en_m, note_html=""):
    """The rubric, Italian and English; nothing where the witness prints
    none (D421), so that no empty heading line is emitted."""
    it, en = it_m.get("rubric", ""), en_m.get("rubric_en", "")
    if not it and not en:
        return ""
    return (f'    <p class="rubric">{html.escape(it)}</p>\n'
            f'    <p class="rubric">{html.escape(en)}\n      {note_html}</p>')


def page_title(nm_en_m, fg_en_m):
    """The page heading: never an editorial title (D264). Machiavelli's
    rubric as the witness gives it; where the witness prints no rubric, its
    own heading in English (`heading_en`, D421)."""
    return (fg_en_m.get("title") or nm_en_m.get("rubric_en", "").rstrip(".")
            or nm_en_m.get("heading_en", ""))


def reader_ref(unit_id):
    """A unit as a reader cites it: Discorsi II.14, Considerazioni I.1."""
    work, book, ch = unit_id.split(".", 2)
    name = "Discorsi" if work == "NM-DISC" else "Considerazioni"
    return f"<i>{name}</i> {roman(int(book))}" + (f".{ch}" if ch.isdigit() else f", {ch}")


def sub_label(pair):
    book, ch = pair.split(".", 1)
    sep = ", " if not ch.isdigit() else "."
    return f"Discourses {roman(int(book))}{sep}{ch}, and Guicciardini's reply"


def notes_esc(s):
    """Escape and lightly render markdown used in notes/apparatus prose:
    `code` for an Italian/Latin term, *emphasis* for a loan-word."""
    s = html.escape(s)
    s = re.sub(r'`([^`]+)`', lambda m: f'<i lang="{term_lang(m.group(1))}">{m.group(1)}</i>', s)
    s = re.sub(r'\*([^*]+)\*', lambda m: f'<i lang="{term_lang(m.group(1))}">{m.group(1)}</i>', s)
    return s


_LATIN = None


def latin_terms():
    """apparatus/latin.md: the Latin words and phrases the edition italicises."""
    global _LATIN
    if _LATIN is None:
        p = ROOT / "apparatus/latin.md"
        text = p.read_text(encoding="utf-8") if p.exists() else ""
        _LATIN = {html.unescape(m.group(1)).strip().lower()
                  for m in re.finditer(r'^\|\s*`([^`]+)`\s*\|', text, re.M)}
    return _LATIN


def term_lang(phrase):
    """'la' for a term listed in apparatus/latin.md, otherwise 'it'."""
    return "la" if html.unescape(phrase).strip().lower() in latin_terms() else "it"


def parse_notes(notes_raw):
    """Split a translation's '## Notes' block into (lemma_html, text_html)
    entries. A note titled exactly "The rubric." is pulled out separately —
    it annotates the rubric line, not a numbered paragraph."""
    entries = []
    rubric_note = None
    for block in re.split(r'\n\s*\n', notes_raw.strip()):
        block = " ".join(block.split())
        if not block:
            continue
        m = re.match(r'^\*\*(.+?)\*\*\s*(.*)$', block)
        lemma, text = (m.group(1), m.group(2)) if m else (None, block)
        if lemma and lemma.strip().rstrip(".").lower() == "the rubric":
            rubric_note = notes_esc(text)
            continue
        entries.append((notes_esc(lemma.rstrip(".")) if lemma else None, notes_esc(text), lemma or ""))
    return entries, rubric_note


def _norm(s):
    """Lower-case letters only, for matching a lemma against paragraph text."""
    s = html.unescape(re.sub(r'[*`]', '', s)).lower()
    return re.sub(r'[^a-zàèéìíòóùúç]+', '', s)


def locate_lemma(lemma_raw, it_paras):
    """The paragraph a note's lemma quotes. An explicit "(.02)" wins; otherwise
    the longest "..."-separated stretch of the lemma is looked for in the
    Italian. None when the lemma quotes no paragraph (the heading, say)."""
    m = re.search(r'\(\.(\d+)\)', lemma_raw)
    if m:
        for pid in it_paras:
            if pid.rsplit(".", 1)[1] == m.group(1):
                return pid
    segs = [_norm(x) for x in re.split(r'\.\.\.|…|\(\.\d+\)', lemma_raw)]
    segs = sorted((x for x in segs if len(x) >= 8), key=len, reverse=True)
    for seg in segs:
        hits = [pid for pid, t in it_paras.items() if seg in _norm(t)]
        if len(hits) == 1:
            return hits[0]
    # A word-list lemma ("sfogare, sfogarsi"): located only if every word it
    # names falls in the same single paragraph; a chapter-wide word stays unlocated.
    words = [w.strip().lower() for w in re.split(r',|/|\band\b|\.\.\.|…', re.sub(r'[*`]', '', html.unescape(lemma_raw)))]
    words = [w for w in words if len(w) >= 4 and " " not in w]
    hits = set()
    for w in words:
        pat = re.compile(r'(?<![\w])' + re.escape(w) + r'(?![\w])', re.I)
        hits |= {pid for pid, t in it_paras.items() if pat.search(html.unescape(re.sub(r'[*`]', '', t)))}
    return next(iter(hits)) if len(hits) == 1 else None


def emphasized(text, notes_raw):
    """Escape paragraph text and render markdown *emphasis* as italic,
    marking a span as Latin (rather than the Italian/loan-word default)
    when it is listed in apparatus/latin.md. Also marks up any
    [bracketed] supplied-letter notation."""
    def repl(m):
        phrase = m.group(1)
        return f'<i lang="{term_lang(phrase)}">{phrase}</i>'  # already escaped above

    out = re.sub(r'\*([^*]+)\*', lambda m: "\x00" + m.group(1) + "\x00", text)
    out = html.escape(out).replace("\x00", "\x01")
    out = re.sub(r'\x01([^\x01]+)\x01', repl, out)
    out = re.sub(r'\[([^\]\[]+)\]', r'<span class="supplied">[\1]</span>', out)
    return out


def summary_html(text):
    """The editor's summary: escaped, with markdown *emphasis* as italic
    (Latin where apparatus/latin.md lists it, otherwise Italian)."""
    out = html.escape(text)
    return re.sub(r'\*([^*]+)\*', lambda m: f'<i lang="{term_lang(m.group(1))}">{m.group(1)}</i>', out)


def summary_plain(text):
    """The editor's summary as plain text, for the meta description."""
    return re.sub(r'\*([^*]+)\*', r'\1', text)


XREF = re.compile(r'\[\[((?:NM-DISC|FG-CONS)\.[0-9a-z]+\.[0-9a-z]+\.\d+)\]\]')


def xref_label(target):
    who = "Machiavelli" if target.startswith("NM-DISC") else "Guicciardini"
    return f"{who} .{target.rsplit('.', 1)[1]}"


def parse_annotations(unit_id):
    """Stage 5. annotations/<unit>.md holds one '## <paragraph id>' section per
    paragraph; each note is a '**Label.** text' block. [[UNIT.ID]] is a
    cross-reference to a paragraph on the same pair page. Returns
    {paragraph_id: [(label_html, text_html), ...]} and every target cited."""
    path = ROOT / f"annotations/{unit_id}.md"
    if not path.exists():
        return {}, set()
    text = path.read_text(encoding="utf-8")
    text = re.sub(r'^---\n.*?\n---\n', '', text, count=1, flags=re.S)
    out, targets = {}, set()
    for sec in re.split(r'^## ', text, flags=re.M)[1:]:
        pid, _, body = sec.partition("\n")
        pid = pid.strip()
        notes = []
        for block in re.split(r'\n\s*\n', body.strip()):
            block = " ".join(block.split())
            if not block:
                continue
            targets.update(XREF.findall(block))
            m = re.match(r'^\*\*(.+?)\*\*\s*(.*)$', block)
            label, t = (m.group(1).rstrip("."), m.group(2)) if m else ("Note", block)
            t = notes_esc(t)
            t = XREF.sub(lambda x: f'<a class="xref" href="#{x.group(1)}">{xref_label(x.group(1))}</a>', t)
            notes.append((notes_esc(label), t))
        out[pid] = notes
    return out, targets


def annot_html(notes):
    if not notes:
        return ""
    body = "\n".join(f'<p><span class="lem">{l}.</span> {t}</p>' for l, t in notes)
    return (f'\n        <details class="annot"><summary>Commentary · {len(notes)}</summary>\n'
            f'          {body}\n        </details>')


def marks_html(m):
    """Margin links from a paragraph to its notes and variants in the apparatus."""
    if not m:
        return ""
    out = []
    for key, one, many in (("notes", "note", "notes"), ("variants", "variant", "variants")):
        ids = m.get(key) or []
        if ids:
            out.append(f'<a href="#{ids[0]}">{len(ids)} {one if len(ids) == 1 else many}</a>')
    return f'<span class="marks">{"".join(out)}</span>' if out else ""


def rows_html(it_paras, en_paras, notes_raw, annots=None, marks=None):
    annots = annots or {}
    marks = marks or {}
    out = []
    for i in para_order(it_paras):
        out.append(
            f'''      <div class="pair" id="{i}">
        <div class="gutter"><a class="uid" href="#{i}">{i.split(".", 1)[1]}</a>{marks_html(marks.get(i))}</div>
        <div class="col it" lang="it">{emphasized(it_paras[i], notes_raw)}</div>
        <div class="col en" lang="en">{emphasized(en_paras[i], notes_raw)}</div>{annot_html(annots.get(i))}
      </div>''')
    return "\n".join(out)


def backlink(pid):
    return (f'<a class="loc" href="#{pid}" title="Back to the paragraph">'
            f'¶\u202f{pid.rsplit(".", 1)[1]}</a> ') if pid else ""


def notes_html(entries, unit_id, it_paras, marks):
    """Translator's notes, each anchored, linked back to the paragraph its lemma
    quotes, and counted in that paragraph's margin."""
    if not entries:
        return "<p>No translator's notes recorded for this pair.</p>"
    out = []
    for k, (lemma, text, raw) in enumerate(entries, 1):
        nid = f"n-{unit_id}-{k}"
        pid = locate_lemma(raw, it_paras) if raw else None
        if pid:
            marks.setdefault(pid, {}).setdefault("notes", []).append(nid)
        lem = f'<span class="lem">{lemma}.</span> ' if lemma else ""
        out.append(f'<p id="{nid}">{backlink(pid)}{lem}{text}</p>')
    return "\n".join(out)


def source_html(work_id, unit_id, corpus_meta):
    lines = [f"<p>{WORKS[work_id]['source_citation']}</p>"]
    if corpus_meta.get("paragraph_divisions") == "editorial":
        lines.append(
            "<p>Paragraph divisions are editorial. The witness prints the chapter "
            "as one unbroken block.</p>"
        )
    prov = load_yaml(f"sources/provenance/{work_id}/{unit_id}-establishment.yml")
    for c in (prov or {}).get("corrections", []) or []:
        lines.append(
            f'<p><span class="lem">{notes_esc(str(c.get("was", "")))}</span> → '
            f'<span class="lem">{notes_esc(str(c.get("now", "")))}</span> '
            f'({notes_esc(str(c.get("locator", "")))}). '
            f'{notes_esc(str(c.get("evidence", "")).strip())}</p>'
        )
    return "\n".join(lines)


def variants_html(work_id, unit_id, it_paras, marks):
    data = load_yaml(f"sources/comparisons/{work_id}/{unit_id}-witness-disagreements.yml")
    if not data:
        return "<p>No collation record for this pair yet.</p>"
    out, saw_systematic = [], False
    for r in data.get("records", []) or []:
        if str(r.get("class", "")).startswith("systematic"):
            saw_systematic = True
            continue
        est = r.get("established")
        if est in r:
            # `established` names the witness whose reading stands
            parts = [f'<span class="lem">{notes_esc(str(r[est]))}</span> — '
                     f'{notes_esc(str(est).replace("witness_", ""))}.']
        else:
            # `established` is the edition's own text (an emendation or a ruled reading)
            parts = [f'<span class="lem">{notes_esc(str(est or ""))}</span>.']
        for k in r:
            if k.startswith("witness_") and k != est:
                parts.append(
                    f'The {notes_esc(k.replace("witness_", ""))} witness reads '
                    f'<i lang="it">{notes_esc(str(r[k]))}</i>.'
                )
        if r.get("rationale"):
            parts.append(notes_esc(str(r["rationale"]).strip()))
        # A heading record is located at the unit, not at its first paragraph.
        pid = r.get("locator") if r.get("locator") in it_paras and r.get("class") != "heading" else None
        vid = "v-" + str(r.get("id") or f"{unit_id}-{len(out) + 1}")
        if pid:
            marks.setdefault(pid, {}).setdefault("variants", []).append(vid)
        out.append(f'<p id="{vid}">{backlink(pid)}' + " ".join(parts) + "</p>")
    if saw_systematic:
        out.append(
            "<p>Orthography, capitalization, word division and punctuation follow "
            "the governing witness throughout; no reading is hybridized between "
            "witnesses.</p>"
        )
    return "\n".join(out) if out else "<p>No variants recorded for this pair.</p>"


def open_items_note(nm_meta, fg_meta):
    items = []
    for label, meta in (("Machiavelli side", nm_meta), ("Guicciardini side", fg_meta)):
        v = meta.get("open_for_david", "none")
        if not v.lower().startswith("none"):
            items.append(f"{label} — {v}")
    # Internal detail (who, item codes) stays in the front-matter; the page says only whether any remain.
    if not items:
        return "No open questions on this pair."
    return "Some translation questions on this pair are still open."


# ---------------------------------------------------------------------------
# Shared look
# ---------------------------------------------------------------------------

# Fonts are self-hosted from site/fonts/ (SIL OFL; licences alongside), so no
# reader's request goes to a third party and a blocked font host cannot drop the
# page to Times. {root} is the path from the page to the site root.
STYLE = '''<link rel="stylesheet" href="{root}fonts/fonts.css">
<style>
*, *::before, *::after { box-sizing: border-box; }
html { -webkit-text-size-adjust: 100%; }
body { margin: 0; }
img { max-width: 100%; }
[hidden] { display: none !important; }
:root {
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
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --paper:      #161917;
    --paper-sunk: #1D211E;
    --ink:        #E3E6E1;
    --ink-muted:  #A0A6A0;
    --ink-faint:  #767C77;
    --rule:       #343934;
    --rule-faint: #262B27;
    --nm:         #8FB4C6;
    --fg:         #C4A97C;
  }
}
:root[data-theme="dark"] {
  --paper:      #161917;
  --paper-sunk: #1D211E;
  --ink:        #E3E6E1;
  --ink-muted:  #A0A6A0;
  --ink-faint:  #767C77;
  --rule:       #343934;
  --rule-faint: #262B27;
  --nm:         #8FB4C6;
  --fg:         #C4A97C;
}

body {
  background: var(--paper);
  color: var(--ink);
  font-family: var(--serif);
  font-size: 17px;
  line-height: 1.62;
  -webkit-font-smoothing: antialiased;
}
.wrap { max-width: 1160px; margin: 0 auto; padding-inline: 20px; padding-block: 0 0; }

/* ---- masthead ---- */
.masthead { padding-block: 56px 32px; border-bottom: 1px solid var(--rule); }
.eyebrow {
  font-family: var(--sans); font-size: 11px; font-weight: 600;
  letter-spacing: .14em; text-transform: uppercase; color: var(--ink-faint);
  margin: 0 0 18px; text-wrap: balance;
}
.eyebrow a { color: inherit; text-decoration: none; }
.eyebrow a:hover, .eyebrow a:focus { color: var(--ink); }
h1 {
  font-family: var(--serif); font-weight: 400; font-size: clamp(30px, 5vw, 44px);
  line-height: 1.12; margin: 0 0 14px; text-wrap: balance; letter-spacing: -0.01em;
}
h1 .sub { display: block; font-style: italic; color: var(--ink-muted); font-size: .52em; margin-top: 12px; letter-spacing: 0; }
.standfirst {
  font-family: var(--serif); font-size: 18px; line-height: 1.55;
  color: var(--ink); max-width: 60ch; margin: 22px 0 0;
}
.sf-label {
  display: block; font-family: var(--sans); font-weight: 600; font-size: 10.5px;
  letter-spacing: .13em; text-transform: uppercase; color: var(--ink-faint); margin-bottom: 6px;
}
.index .standfirst { font-size: 17px; color: var(--ink-muted); }

/* ---- the pairing device ---- */
.pairing {
  display: flex; align-items: stretch; gap: 0; margin: 30px 0 0;
  border: 1px solid var(--rule); border-radius: 2px; overflow: hidden;
  font-family: var(--sans); background: var(--paper-sunk);
}
.pairing > div { flex: 1 1 0; padding: 13px 16px; min-width: 0; }
.pairing .who { font-size: 11px; font-weight: 600; letter-spacing: .1em; text-transform: uppercase; margin-bottom: 4px; }
.pairing .nm-side .who { color: var(--nm); }
.pairing .fg-side .who { color: var(--fg); }
.pairing .what { font-size: 13.5px; color: var(--ink-muted); }
.pairing .arrow {
  flex: 0 0 auto; display: flex; align-items: center; justify-content: center;
  padding-inline: 14px; color: var(--ink-faint); font-size: 15px;
  border-inline: 1px solid var(--rule);
}

/* ---- pair-to-pair navigation ---- */
.pairnav {
  display: flex; justify-content: space-between; gap: 14px; flex-wrap: wrap;
  margin-top: 18px; font-family: var(--sans); font-size: 12.5px;
  color: var(--ink-muted);
}
.pairnav a { text-decoration: none; color: var(--ink-muted); }
.pairnav a:hover, .pairnav a:focus { color: var(--ink); text-decoration: underline; }

/* ---- work sections ---- */
.work { padding-block: 52px 0; }
.work-head { display: flex; align-items: baseline; gap: 14px; flex-wrap: wrap; margin-bottom: 6px; }
.work-head .tag {
  font-family: var(--sans); font-size: 10.5px; font-weight: 600; letter-spacing: .12em;
  text-transform: uppercase; padding: 4px 8px 3px; border-radius: 2px; color: var(--paper);
  align-self: center;
}
.work-head .cite { font-family: var(--sans); font-size: 13px; color: var(--ink-faint); }
.work.nm .tag { background: var(--nm); }
.work.fg .tag { background: var(--fg); }
h2 { font-family: var(--serif); font-weight: 500; font-size: 25px; margin: 0; letter-spacing: -0.005em; }
.rubric {
  font-style: italic; color: var(--ink-muted); max-width: 70ch;
  margin: 10px 0 0; font-size: 16.5px; line-height: 1.5;
}
.rubric-note {
  font-family: var(--sans); font-style: normal; font-size: 12px;
  color: var(--ink-faint); margin-top: 7px;
}
.colheads {
  display: grid; grid-template-columns: 66px 1fr 1fr; gap: 0 28px;
  margin-top: 30px; padding-bottom: 7px; border-bottom: 1px solid var(--rule);
  font-family: var(--sans); font-size: 10.5px; font-weight: 600;
  letter-spacing: .13em; text-transform: uppercase; color: var(--ink-faint);
}

/* ---- the facing pair ---- */
.pair {
  display: grid; grid-template-columns: 66px 1fr 1fr; gap: 0 28px;
  padding-block: 22px; border-bottom: 1px solid var(--rule-faint);
  scroll-margin-top: 20px;
}
.pair:target { background: var(--paper-sunk); }
.annot { grid-column: 2 / -1; margin-top: 14px; font-family: var(--sans); font-size: 13.5px;
  line-height: 1.55; color: var(--ink-muted); }
.annot summary { cursor: pointer; font-size: 10.5px; font-weight: 600; letter-spacing: .13em;
  text-transform: uppercase; color: var(--ink-faint); list-style: none; }
.annot summary::-webkit-details-marker { display: none; }
.annot summary::before { content: "+ "; }
.annot[open] summary::before { content: "− "; }
.annot p { margin: 8px 0 0; max-width: 72ch; }
.annot .lem { font-weight: 600; color: var(--ink); }
.annot .xref { color: inherit; text-decoration: underline; text-decoration-color: var(--rule);
  text-underline-offset: 2px; white-space: nowrap; }
.gutter { padding-top: 4px; }
.marks { display: block; margin-top: 10px; font-family: var(--sans); font-size: 11px; line-height: 1.45; }
.marks a { display: block; color: var(--ink-faint); text-decoration: none; white-space: nowrap; }
.marks a:hover, .marks a:focus { color: var(--ink); text-decoration: underline; }
.uid {
  font-family: var(--mono); font-size: 10.5px; color: var(--ink-faint);
  text-decoration: none; letter-spacing: -0.02em;
}
.uid:hover, .uid:focus { color: var(--ink); text-decoration: underline; }
.col { min-width: 0; }
.col.it { hyphens: auto; }
.col.en { hyphens: auto; }
.supplied { color: var(--ink-muted); }

/* ---- apparatus ---- */
.apparatus {
  margin-top: 34px; padding-top: 22px; border-top: 2px solid var(--rule);
  font-family: var(--sans); font-size: 13.5px; line-height: 1.58;
  color: var(--ink-muted);
}
/* Source is a short paragraph; variants and notes run long, so they flow in
   two balanced columns across the full width rather than in one narrow strip. */
.apparatus > div + div { margin-top: 30px; }
.app-source p { max-width: 78ch; }
.app-variants, .app-notes { columns: 2 340px; column-gap: 40px; }
.app-variants h3, .app-notes h3 { column-span: all; }
.apparatus p { break-inside: avoid; scroll-margin-top: 20px; }
.apparatus p:target { background: var(--paper-sunk); box-shadow: 0 0 0 6px var(--paper-sunk); }
.apparatus .loc {
  font-family: var(--mono); font-size: 11px; color: var(--ink-faint); text-decoration: none;
  white-space: nowrap; margin-right: .2em;
}
.apparatus .loc:hover, .apparatus .loc:focus { color: var(--ink); text-decoration: underline; }
.apparatus h3 {
  font-family: var(--sans); font-size: 10.5px; font-weight: 600; letter-spacing: .13em;
  text-transform: uppercase; color: var(--ink-faint); margin: 0 0 9px;
}
.apparatus p { margin: 0 0 9px; }
.apparatus p:last-child { margin-bottom: 0; }
.apparatus .lem { font-family: var(--serif); font-size: 15px; color: var(--ink); font-style: italic; }
.sig { font-family: var(--mono); font-size: 12px; color: var(--ink); }

/* ---- colophon ---- */
.pairnav-foot { margin-top: 56px; padding-top: 18px; border-top: 1px solid var(--rule); }
.colophon {
  margin-top: 40px; padding-block: 0 60px;
  font-family: var(--sans); font-size: 13px; line-height: 1.6; color: var(--ink-muted);
}
.colophon .row { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 24px 34px; }
.colophon h3 {
  font-size: 10.5px; font-weight: 600; letter-spacing: .13em; text-transform: uppercase;
  color: var(--ink-faint); margin: 0 0 8px;
}
.colophon p { margin: 0 0 8px; }
.colophon ul { margin: 0; padding-left: 16px; }
.colophon li { margin-bottom: 5px; }
.colophon .links { margin: 18px 0 0; display: flex; gap: 6px 22px; flex-wrap: wrap; }
.colophon .links a { color: var(--ink-muted); }
.about { max-width: 68ch; padding-block: 44px 0; font-family: var(--serif); font-size: 17px; }
.about h2 { margin: 38px 0 10px; }
.about h2:first-child { margin-top: 0; }
.about p { margin: 0 0 12px; }
.state {
  margin-top: 0; padding: 14px 16px; background: var(--paper-sunk);
  border-left: 2px solid var(--ink-faint); border-radius: 0 2px 2px 0;
  font-size: 12.5px;
}
.state strong { color: var(--ink); font-weight: 600; }
a { color: inherit; }
:focus-visible { outline: 2px solid var(--nm); outline-offset: 2px; }

/* ---- contents / index page ---- */
.toc { margin-top: -22px; }
.toc .book {
  font-family: var(--serif); font-weight: 500; font-size: 22px; margin: 0;
  padding: 34px 0 10px; border-bottom: 1px solid var(--rule);
  display: flex; align-items: baseline; justify-content: space-between; gap: 14px; flex-wrap: wrap;
}
.toc .book:first-child { padding-top: 0; }
.toc .book span { font-family: var(--sans); font-size: 12px; font-weight: 400; color: var(--ink-faint); }
.toc-row {
  display: grid; grid-template-columns: 40px minmax(0, 70ch) 1fr; gap: 0 20px;
  padding-block: 14px; border-bottom: 1px solid var(--rule-faint);
  font-family: var(--sans); align-items: baseline;
}
.toc-row .n { font-family: var(--mono); font-size: 12px; color: var(--ink-faint); }
.toc-row > div:nth-child(2) { line-height: 1.32; }
.toc-row a { text-decoration: none; color: var(--ink); font-family: var(--serif); font-size: 17px; }
.toc-row a:hover, .toc-row a:focus { text-decoration: underline; }
.toc-row .unpublished { color: var(--ink-faint); font-style: italic; font-size: 14px; }
.toc-row .ids { color: var(--ink-faint); font-size: 12px; font-family: var(--sans); margin-top: 3px; }
.toc-row .dated { color: var(--ink-faint); font-size: 12px; text-align: right; }

/* ---- language toggle: on phones the facing columns stack, so the reader picks
   one language (English by default), or both; desktop always shows both ---- */
.langbar { display: none; }
@media (max-width: 760px) {
  .langbar {
    display: flex; align-items: center; gap: 6px; position: sticky; top: 0; z-index: 5;
    margin: 0 -20px; padding: 10px 20px; background: var(--paper);
    border-bottom: 1px solid var(--rule); font-family: var(--sans); font-size: 12.5px;
  }
  .langbar .lb-label { color: var(--ink-faint); margin-right: 4px; font-size: 11px;
    font-weight: 600; letter-spacing: .12em; text-transform: uppercase; }
  .langbar button {
    font: inherit; color: var(--ink-muted); background: transparent; cursor: pointer;
    border: 1px solid var(--rule); border-radius: 2px; padding: 5px 11px;
  }
  .langbar button[aria-pressed="true"] { background: var(--ink); color: var(--paper); border-color: var(--ink); }
  html[data-lang="en"] .col.it, html[data-lang="it"] .col.en { display: none; }
  html[data-lang="en"] .col.en::before, html[data-lang="it"] .col.it::before { display: none; }
  html[data-lang="it"] .col.it { margin-bottom: 0; padding-bottom: 0; border-bottom: 0; }
  .pair { scroll-margin-top: 56px; }
  .apparatus p { scroll-margin-top: 56px; }
}
@media (max-width: 760px) {
  body { font-size: 16.5px; }
  .colheads { display: none; }
  .pair { grid-template-columns: 1fr; gap: 0; padding-block: 20px; }
  .gutter { padding-top: 0; margin-bottom: 8px; display: flex; gap: 14px; align-items: baseline; }
  .marks { display: inline-flex; gap: 12px; margin-top: 0; }
  .annot { grid-column: 1; }
  .col.it { margin-bottom: 14px; padding-bottom: 14px; border-bottom: 1px dotted var(--rule); }
  .col.it::before, .col.en::before {
    display: block; font-family: var(--sans); font-size: 10px; font-weight: 600;
    letter-spacing: .13em; text-transform: uppercase; color: var(--ink-faint); margin-bottom: 6px;
  }
  .col.it::before { content: "Italian"; }
  .col.en::before { content: "English"; }
  .pairing { flex-direction: column; }
  .pairing .arrow { border-inline: 0; border-block: 1px solid var(--rule); padding-block: 6px; }
  .toc-row { grid-template-columns: 1fr; gap: 4px; }
  .toc-row .dated { text-align: left; }
  .app-variants, .app-notes { columns: 1; }
}
</style>'''

# The edition's standing statement (what it is, the title, method, licence) is
# written once, on site/about.html; every page carries a short footer pointing there.
ABOUT = '''    <h2>What this is</h2>
        <p>A free, openly licensed, bilingual edition of Guicciardini's 39 <i>Considerazioni</i> and the
          <i>Discorsi</i> chapters they answer — 78 text units, Italian and English facing, every reading
          traceable to a named public-domain witness.</p>
        <p>It is a reading edition with a transparent apparatus, not a text of record. It does not adjudicate
          the critical text against Bausi 2001 or the manuscript tradition, and does not claim to.</p>
        <p>Edited by David McDougall. AI-assisted English translation edited by David McDougall.</p>
    <h2>On the title</h2>
        <p>Machiavelli had been dead two years when Guicciardini wrote; the <i>Discorsi</i> were unpublished,
          and the <i>Considerazioni</i> stayed unprinted until 1857. Machiavelli never answers.</p>
        <p>“Conversation” is a quotation, not a description. It invokes Machiavelli's letter to Francesco Vettori of
          10 December 1513: at evening he puts on royal and curial garments (<i>panni reali e curiali</i>),
          enters the ancient courts of ancient men (<i>le antiche corti degli antichi uomini</i>), asks them the
          reason for their actions, and <i>quelli per loro umanità mi rispondono</i>, “they, for their humanity,
          answer me”. Guicciardini does to Machiavelli what Machiavelli did to Livy — and is denied the reply
          Machiavelli claimed. The letter is quoted from the 1813 <i>Opere</i>, vol. 8, p. 96, read twice from
          the page image.</p>
    <h2 id="method">Method</h2>
        <p>No image-derived reading enters the text on a single reading. Each unit is transcribed twice,
          independently, by readers who have not seen each other's work; disagreements are adjudicated against
          the page images and recorded.</p>
        <p>The English translation was produced with substantial assistance from generative AI and edited by
          David McDougall. Each draft is reviewed against the Italian by a separate AI reviewer that has not seen
          the drafting work; judgement calls are ruled by the editor and logged. The workflow, and what is and is
          not recorded about the models used, is in <span class="sig">TRANSLATION_METHOD.md</span> in the
          repository.</p>
        <p>Existing English translations of the <i>Considerazioni</i> — Grayson (1965), Atkinson &amp; Sices
          (2002) — are never used as translation inputs.</p>
    <h2 id="licence">Licence</h2>
        <p>The established Italian text and the research and provenance data are dedicated to the public domain under
          <a href="https://creativecommons.org/publicdomain/zero/1.0/">CC0 1.0</a>. They are Machiavelli's and
          Guicciardini's sentences, and this edition adds no condition to them.</p>
        <p>The English translation, the notes and the editorial apparatus are licensed
          <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a> to the extent that rights subsist in
          them and are held by the licensor; no copyright is asserted over material solely because it was generated
          by AI. Reuse them anywhere, including commercially, with
          attribution, for example: <i>A Conversation with Machiavelli</i>, AI-assisted English translation edited
          by David McDougall, CC BY 4.0. The build tooling is MIT.</p>
        <p>The witness scans are other people's digitisations, included as evidence under their own terms; no
          grant is made over them, and no page image of Palmarocchi 1933 is reproduced here. Full terms
          are in the <span class="sig">LICENSE</span> file in the repository, and file by file in
          <span class="sig">REUSE.toml</span>; source
          rights are in <span class="sig">RIGHTS_AND_SOURCES.md</span>.</p>'''

COLOPHON = '''  <footer class="colophon">
{state}
    <p class="links"><a href="{about}">About this edition</a><a href="{about}#licence">Licence</a><a href="{about}#method">Method</a><a href="https://github.com/davidmcdougall/conversation-with-machiavelli">Source and data on GitHub</a></p>
  </footer>'''


# Applies the reader's language choice before first paint (no flash) and wires the
# toggle. Only phones show the toggle; the attribute has no effect on wider screens.
LANG_SCRIPT = """<script>
(function () {
  var KEY = "cwm-lang", d = document.documentElement, v = "en";
  try { v = localStorage.getItem(KEY) || "en"; } catch (e) {}
  d.setAttribute("data-lang", v);
  document.addEventListener("DOMContentLoaded", function () {
    var bs = document.querySelectorAll("[data-set-lang]");
    function sync() { bs.forEach(function (b) { b.setAttribute("aria-pressed", String(b.dataset.setLang === d.getAttribute("data-lang"))); }); }
    bs.forEach(function (b) { b.addEventListener("click", function () {
      d.setAttribute("data-lang", b.dataset.setLang);
      try { localStorage.setItem(KEY, b.dataset.setLang); } catch (e) {}
      sync();
    }); });
    sync();
  });
})();
</script>
"""


def style(root):
    return STYLE.replace("{root}", root)


SITE_URL = "https://davidmcdougall.github.io/conversation-with-machiavelli/"
SITE_NAME = "A Conversation with Machiavelli"

# Two facing leaves in the two authors' colours: the pairing device, as a tab icon.
FAVICON = ("data:image/svg+xml," + "%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E"
           "%3Crect x='3' y='5' width='12' height='22' rx='1.5' fill='%233A5A6B'/%3E"
           "%3Crect x='17' y='5' width='12' height='22' rx='1.5' fill='%236E5A3C'/%3E%3C/svg%3E")


def wrap(content, description, path, title):
    """A full document: the content's <title> and style go in <head>, the rest in
    <body>. `path` is the page's path under the site root, for its canonical URL."""
    head, sep, body = content.partition('\n<div class="wrap">')
    assert sep, "page content must open its body with <div class=\"wrap\">"
    url = SITE_URL + path
    esc = html.escape
    meta = (
        f'<meta name="description" content="{esc(description)}">\n'
        f'<link rel="canonical" href="{url}">\n'
        f'<link rel="icon" href="{FAVICON}">\n'
        f'<meta property="og:type" content="article">\n'
        f'<meta property="og:site_name" content="{SITE_NAME}">\n'
        f'<meta property="og:title" content="{esc(title)}">\n'
        f'<meta property="og:description" content="{esc(description)}">\n'
        f'<meta property="og:url" content="{url}">\n'
        f'<meta name="twitter:card" content="summary">\n'
    )
    return (
        '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        + LANG_SCRIPT +
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
        + meta + head.strip() + "\n</head>\n<body>" + sep + body + "\n</body>\n</html>\n"
    )


def pairnav_html(published, current_pair, index_href="../index.html"):
    ordered = [p["pair"] for p in published]
    i = ordered.index(current_pair) if current_pair in ordered else -1
    prev_p = ordered[i - 1] if i > 0 else None
    next_p = ordered[i + 1] if 0 <= i < len(ordered) - 1 else None
    left = f'<a href="{prev_p}.html">← Pair {prev_p}</a>' if prev_p else "<span></span>"
    right = f'<a href="{next_p}.html">Pair {next_p} →</a>' if next_p else "<span></span>"
    return (
        f'    <nav class="pairnav">{left}'
        f'<a href="{index_href}">All {len(pairing_map())} pairs</a>{right}</nav>'
    )


# ---------------------------------------------------------------------------
# Build one pair
# ---------------------------------------------------------------------------

def build_pair(pair, published):
    nm_id, fg_id = f"NM-DISC.{pair}", f"FG-CONS.{pair}"
    nm_it_m, nm_it = parse_corpus(nm_id, "NM-DISC")
    fg_it_m, fg_it = parse_corpus(fg_id, "FG-CONS")
    nm_en_m, nm_en, nm_notes_raw = parse_translation(nm_id, "NM-DISC")
    fg_en_m, fg_en, fg_notes_raw = parse_translation(fg_id, "FG-CONS")

    assert set(nm_it) == set(nm_en), f"{nm_id}: Italian and English paragraph ids do not align"
    assert set(fg_it) == set(fg_en), f"{fg_id}: Italian and English paragraph ids do not align"

    nm_ann, nm_targets = parse_annotations(nm_id)
    fg_ann, fg_targets = parse_annotations(fg_id)
    on_page = set(nm_it) | set(fg_it)
    for uid, ann in ((nm_id, nm_ann), (fg_id, fg_ann)):
        stray = set(ann) - on_page
        assert not stray, f"annotations/{uid}.md: sections for paragraphs not in the unit: {sorted(stray)}"
    dead = (nm_targets | fg_targets) - on_page
    assert not dead, f"annotation cross-references to paragraphs not on this page: {sorted(dead)}"

    nm_entries, _ = parse_notes(nm_notes_raw)
    fg_entries, fg_rubric_note = parse_notes(fg_notes_raw)

    # Apparatus first: it decides which notes and variants each paragraph's margin points to.
    nm_marks, fg_marks = {}, {}
    nm_variants = variants_html("NM-DISC", nm_id, nm_it, nm_marks)
    nm_notes = notes_html(nm_entries, nm_id, nm_it, nm_marks)
    fg_variants = variants_html("FG-CONS", fg_id, fg_it, fg_marks)
    fg_notes = notes_html(fg_entries, fg_id, fg_it, fg_marks)

    rows = pairing_map()
    row = next((r for r in rows if r["nm"] == nm_id), None)
    eyebrow = f"Pair {row['n']} of {len(rows)}" if row else pair

    title = page_title(nm_en_m, fg_en_m)
    standfirst = fg_en_m.get("standfirst", "")

    fg_rubric_note_html = (
        f'<span class="rubric-note">{fg_rubric_note}</span>' if fg_rubric_note else ""
    )

    CONTENT = f'''<title>A Conversation with Machiavelli — {html.escape(title)}</title>
{style("../")}

<div class="wrap">

  <header class="masthead">
    <p class="eyebrow"><a href="../index.html">A Conversation with Machiavelli</a> · {eyebrow}</p>
    <h1>{html.escape(title)}
      <span class="sub">{html.escape(sub_label(pair))}</span></h1>
    <p class="standfirst"><span class="sf-label">Editor's summary</span> {summary_html(standfirst)}</p>

    <div class="pairing">
      <div class="nm-side">
        <div class="who">{WORKS['NM-DISC']['author']}</div>
        <div class="what">{WORKS['NM-DISC']['work_title']} · {WORKS['NM-DISC']['work_dates']}</div>
      </div>
      <div class="arrow" aria-hidden="true">answered by</div>
      <div class="fg-side">
        <div class="who">{WORKS['FG-CONS']['author']}</div>
        <div class="what">{WORKS['FG-CONS']['work_title']} · {WORKS['FG-CONS']['work_dates']}</div>
      </div>
    </div>
{pairnav_html(published, pair)}
  </header>

  <div class="langbar" role="group" aria-label="Show which language">
    <span class="lb-label">Show</span>
    <button type="button" data-set-lang="en">English</button>
    <button type="button" data-set-lang="it">Italian</button>
    <button type="button" data-set-lang="both">Both</button>
  </div>

  <section class="work nm">
    <div class="work-head">
      <span class="tag" title="{nm_id}">Machiavelli</span>
      <h2>{nm_heading(pair, nm_it_m)}</h2>
      <span class="cite">{reader_ref(nm_id)}</span>
    </div>
{rubric_lines(nm_it_m, nm_en_m)}

    <div class="colheads"><div></div><div>Italian · {WORKS['NM-DISC']['edition_year']}</div><div>English</div></div>
{rows_html(nm_it, nm_en, nm_notes_raw, nm_ann, nm_marks)}

    <div class="apparatus">
      <div class="app-source">
        <h3>Source</h3>
        {source_html("NM-DISC", nm_id, nm_it_m)}
      </div>
      <div class="app-variants">
        <h3>Variants</h3>
        {nm_variants}
      </div>
      <div class="app-notes">
        <h3>Notes</h3>
        {nm_notes}
      </div>
    </div>
  </section>

  <section class="work fg">
    <div class="work-head">
      <span class="tag" title="{fg_id}">Guicciardini</span>
      <h2>{fg_heading(pair, fg_it_m)}</h2>
      <span class="cite">{reader_ref(fg_id)}</span>
    </div>
{rubric_lines(fg_it_m, fg_en_m, fg_rubric_note_html)}

    <div class="colheads"><div></div><div>Italian · {WORKS['FG-CONS']['edition_year']}</div><div>English</div></div>
{rows_html(fg_it, fg_en, fg_notes_raw, fg_ann, fg_marks)}

    <div class="apparatus">
      <div class="app-source">
        <h3>Source</h3>
        {source_html("FG-CONS", fg_id, fg_it_m)}
      </div>
      <div class="app-variants">
        <h3>Variants</h3>
        {fg_variants}
      </div>
      <div class="app-notes">
        <h3>Notes</h3>
        {fg_notes}
      </div>
    </div>
  </section>

{pairnav_html(published, pair).replace('class="pairnav"', 'class="pairnav pairnav-foot"')}

{COLOPHON.format(about="../about.html", state=f"""
    <div class="state">
      <p><strong>Version {edition_version()} · {len(published)} of {len(rows)} pairs published.</strong>
        {dates_line(pair)} This edition is versioned, not frozen. {open_items_note(nm_en_m, fg_en_m)}</p>
    </div>""")}

</div>'''

    pairs_dir = ROOT / "site/pairs"
    pairs_dir.mkdir(parents=True, exist_ok=True)
    (pairs_dir / f"{pair}-content.html").write_text(CONTENT, encoding="utf-8")
    (pairs_dir / f"{pair}.html").write_text(
        wrap(CONTENT, summary_plain(standfirst) or title, f"pairs/{pair}.html", title), encoding="utf-8")
    print(f"site/pairs/{pair}.html", (pairs_dir / f"{pair}.html").stat().st_size, "bytes")
    print("paragraphs:", len(nm_it), "NM /", len(fg_it), "FG — alignment check passed")


# ---------------------------------------------------------------------------
# Build the index
# ---------------------------------------------------------------------------

def build_index(published):
    published_by_nm = {p["nm"]: p for p in published}
    rows = pairing_map()

    toc = []
    revised_dates = []
    book = None
    for r in rows:
        b = r["nm"].split(".")[1]
        if b != book:
            book = b
            label = "Book I" if b == "1" else f"Book {roman(int(b))}"
            n_book = sum(1 for x in rows if x["nm"].split(".")[1] == b)
            n_pub = sum(1 for x in rows if x["nm"].split(".")[1] == b and x["nm"] in published_by_nm)
            toc.append(f'''      <h2 class="book" id="book-{b}">{label} <span>{n_pub} of {n_book} pairs published</span></h2>''')
        pub = published_by_nm.get(r["nm"])
        if pub:
            nm_en_m, _, _ = parse_translation(r["nm"], "NM-DISC")
            fg_en_m, _, _ = parse_translation(r["fg"], "FG-CONS")
            title = page_title(nm_en_m, fg_en_m)
            pub_d, rev_d = pair_dates(pub["pair"])
            revised_dates.append(rev_d)
            toc.append(
                f'''      <div class="toc-row">
        <div class="n">{r['n']:02d}</div>
        <div><a href="pairs/{pub['pair']}.html">{html.escape(title)}</a>
          <div class="ids">{reader_ref(r['nm'])} · {reader_ref(r['fg'])}</div></div>
        <div class="dated">{long_date(rev_d)}</div>
      </div>''')
        else:
            toc.append(
                f'''      <div class="toc-row">
        <div class="n">{r['n']:02d}</div>
        <div><span class="unpublished">Not yet published</span>
          <div class="ids">{reader_ref(r['nm'])} · {reader_ref(r['fg'])}</div></div>
        <div></div>
      </div>''')

    CONTENT = f'''<title>A Conversation with Machiavelli</title>
{style("")}

<div class="wrap">

  <header class="masthead index">
    <p class="eyebrow">A Conversation with Machiavelli · {len(published)} of {len(rows)} pairs published</p>
    <h1>Guicciardini's <i>Considerazioni</i> on the <i>Discorsi</i>
      <span class="sub">A free, bilingual, hyperlinked edition</span></h1>
    <p class="standfirst">Guicciardini answered 39 of Machiavelli's chapters and passed over the rest. Each pair below
      puts the chapter and the reply on one screen, Italian and English facing, with a transparent apparatus.</p>
  </header>

  <section class="work">
    <div class="toc">
{chr(10).join(toc)}
    </div>
  </section>

{COLOPHON.format(about="about.html", state=f"""
    <div class="state">
      <p><strong>Version {edition_version()} · {len(published)} of {len(rows)} pairs published.</strong>
        Last updated {long_date(max(revised_dates)) if revised_dates else "—"}. Each pair is dated on its page and above, by its last revision.
        This edition is versioned, not frozen. Publish, be wrong, fix it, publish again, and date every page.
        Edited by David McDougall. AI-assisted English translation edited by David McDougall.</p>
    </div>""")}

</div>'''

    site = ROOT / "site"
    (site / "index-content.html").write_text(CONTENT, encoding="utf-8")
    (site / "index.html").write_text(
        wrap(CONTENT, "A free, bilingual, hyperlinked edition of Guicciardini's Considerazioni "
                      "and the Discorsi chapters they answer.", "", SITE_NAME),
        encoding="utf-8",
    )
    print("site/index.html", (site / "index.html").stat().st_size, "bytes —",
          len(published), "of", len(rows), "pairs listed")
    build_about(published)


def build_about(published):
    rows = pairing_map()
    CONTENT = f'''<title>About — A Conversation with Machiavelli</title>
{style("")}

<div class="wrap">

  <header class="masthead">
    <p class="eyebrow"><a href="index.html">A Conversation with Machiavelli</a> · About this edition</p>
    <h1>About this edition</h1>
  </header>

  <section class="about">
{ABOUT}
  </section>

  <nav class="pairnav pairnav-foot"><a href="index.html">← All {len(rows)} pairs</a></nav>

{COLOPHON.format(about="about.html", state=f"""
    <div class="state">
      <p><strong>Version {edition_version()} · {len(published)} of {len(rows)} pairs published.</strong>
        This edition is versioned, not frozen.</p>
    </div>""")}

</div>'''
    site = ROOT / "site"
    (site / "about.html").write_text(
        wrap(CONTENT, "What this edition is, its title, its method and its licence.",
             "about.html", "About — " + SITE_NAME), encoding="utf-8")
    print("site/about.html", (site / "about.html").stat().st_size, "bytes")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                  formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pair", nargs="?", help='pair id, e.g. "1.12"')
    ap.add_argument("--all", action="store_true", help="rebuild every published pair")
    ap.add_argument("--index", action="store_true", help="rebuild only the index")
    args = ap.parse_args()

    published = discover_published()

    if args.index:
        pass
    elif args.all:
        for row in published:
            build_pair(row["pair"], published)
    elif args.pair:
        if args.pair not in [p["pair"] for p in published]:
            available = ", ".join(p["pair"] for p in published) or "none"
            sys.exit(
                f'Pair "{args.pair}" is not published yet (needs both '
                f"translations/NM-DISC.{args.pair}.md and translations/FG-CONS.{args.pair}.md). "
                f"Published pairs: {available}"
            )
        build_pair(args.pair, published)
        import contextlib, io
        with contextlib.redirect_stdout(io.StringIO()):
            for row in published:
                if row["pair"] != args.pair:
                    build_pair(row["pair"], published)
        print(f"refreshed the other {len(published) - 1} published pairs")
    else:
        ap.error('give a pair id (e.g. "1.12"), or --all')

    build_index(published)
    # SCOPE §2 and §4 tables follow the files; refresh them with every build.
    import subprocess
    subprocess.run([sys.executable, str(ROOT / "scripts/state"), "--write"], check=True)


if __name__ == "__main__":
    main()
