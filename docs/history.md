# How the first pairs got here — September 2026

Moved verbatim from `SCOPE.md` §4 on 2026-11-25. Dated history, not current
state: by 2026-11-25 acquisition was complete for all 39 pairs, 38 pairs were
published, the register files had been rewritten on port, and the Palmarocchi
rights question was closed (`RIGHTS_AND_SOURCES.md` §6). Section references
(§6 etc.) are to `SCOPE.md` as it then stood.

**Read the top row first.** The relationship layer — all 39 pairs, mapped
against the chapter headings — is complete, and it is a real asset. Be precise
about what kind of one. The 39 files in `relationships/FG-CONS/` are a single
template rendered 39 times: 1,040–1,060 bytes each, byte-identical apart from
the chapter number, carrying the same evidence sentence, the same citation and
the same closing paragraph. The information is a 39-row, two-column table plus
one provenance note that applies to every row at once. It ports as one file
(§6), not as thirty-nine.

The map's evidence also cites the Palmarocchi/Wikisource headings — the witness
this project demotes to collation-only. Restate it against Canestrini's
headings on porting, or record plainly that the pairing is attested in both.

**Read the bottom three second.** The I.12 pair went end to end on 2026-09-26:
cold-reviewed English, cold-reviewed commentary (`annotations/`), and published
at https://davidmcdougall.github.io/conversation-with-machiavelli/ from
`site/` by `.github/workflows/pages.yml`. Every estimate below stage 3 is still
one data point.

**The middle was signed off on 2026-09-18.** Both I.12 units sat at
`review_pending` on a Class T review that §7 abolishes, and neither had ever had
the dual cold pass §7 keeps. The pass was run (`sources/coldpass/`), the two
readers agreed on every word, clause and sense across 1,419 words, and both
units were marked `status: established`, `integrity_class: S2`, version 0.2.0.
That was wrong for FG-CONS.1.12, which turned out to be Palmarocchi under
Canestrini's label (FG-CONS-I12-F001). It was re-established from Canestrini on
2026-09-21 and closed at v0.3.1 / S2 on 2026-09-25 (D42). One pair is through
stage 6.

### Acquisition is smaller than it looks

Every unit comes from **four scans, already identified**:

| Text | Governing witness | Comparison witness |
|---|---|---|
| *Discorsi* | 1824 edition (Wikisource, page-image-backed; Commons djvu) | 1554 Giglio, Venice (IA `discorsidinicolo00mach`, 478 leaves) |
| *Considerazioni* | **Canestrini 1857**, *Opere inedite* vol. 1 (IA `bub_gb_F_YZsP2XjO8C`, PD Mark 1.0) | Palmarocchi 1933 (Commons/BEIC djvu) — page images only |

**Identified, not held.** The repository does not contain these four scans. It
contains the I.12 page extracts and the IA/Commons metadata that locates each
witness — `FG-CONS-I12-pages.pdf` (79K), two Palmarocchi page JPGs, and an
`NM-DISC-I12-pages.pdf` from each of the 1824 and 1554 witnesses; 1.6MB in
total. That is a *where to get it*, not a *have it*.

Acquisition is therefore step 0 of execution: download four scans once, map
chapter to page range for 78 units, extract. A day or two, not 38 separate
hunts. Both extraction pipelines are proven on the I.12 pair.

### Sources rights — settled, not open

Recorded in `sources/provenance/FG-CONS/` on 2026-07-17; the Palmarocchi
scan position, provenance naming and licensing pointer amended 2026-09-26:

- **Canestrini 1857 governs the *Considerazioni*.** Public domain by age,
  scan layer under Public Domain Mark 1.0, `corpus_reuse:
  reproducible_in_corpus`. The *editio princeps*, independently typeset
  seventy-six years before Palmarocchi.
- **Palmarocchi 1933 is collation evidence only.** Scan images are consulted,
  not republished: the Commons PD tag keys on Guicciardini, not the 1933
  editorial layer, assessed as in copyright in Italy to 31 Dec 2026 and in the
  US (URAA) to 31 Dec 2028, pending legal review. The Wikisource transcription is CC BY-SA/GFDL and
  Palmarocchi's editorial expression is consultation-only (`RIGHTS_AND_SOURCES.md` §1).
  Readings may inform collation; the expression is never copied.
- The witness inventory records that this route requires **no
  relationship-map change**.
- Per-unit provenance files are named `WIT-<witness-id>.<unit-id>.yml`. The
  legacy flat 1.12 files stay as they are.
- Licensing: LICENSE at repo root is the grant; DEC-011 revises DEC-010 points
  2–3. Source rights are in `RIGHTS_AND_SOURCES.md`; the translation credit and
  model provenance are in `TRANSLATION_METHOD.md`.

The census layer contradicts all of it. `register/guicciardini/FG-CONS.md`
still says Palmarocchi "supplies the openly inspectable page-image-backed
witness used for the present pairing map" and that Canestrini is "not adopted
as a governing critical text" — the exact inverse of what was settled here. It
rates the work S1 and asserts that a work package "must identify the manuscript
basis and select or construct the governing text before translation."
`register/machiavelli/NM-DISC.md` names Bausi 2001 the "primary
governing-edition candidate." Both contradict §1 and §8 outright.

These are not stale summaries. They are the old doctrine intact, and porting
them unchanged installs the second disagreeing state layer on day one — the
specific failure §7 exists to prevent. They port only after every field
asserting a governing edition, a source-integrity class, or a pre-translation
manuscript gate is rewritten to the posture above.
