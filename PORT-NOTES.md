# Port notes — 2026-09-18

Ported from `Machiavelli : Guicciardini Corpus` per SCOPE §6. The old
repository is untouched on disk as a sibling and remains the archive.

## Changed in transit, not merely copied

**`links/pairing-map.md`** replaces `relationships/FG-CONS/*.md`. The 39
predecessor files were one template rendered 39 times — verified: normalising
away the chapter numbers leaves exactly two distinct bodies across all 39, and
the second is only the Book II proem naming. All 39 subject/object pairs were
checked against the SCOPE §2 table and agree. The predecessor record IDs are
retained as a column so the old files remain findable.

**`sources/register/{FG-CONS,NM-DISC}.md`** are rewritten, not copied. Both
asserted a governing critical edition, a source-integrity class and a
pre-translation manuscript gate, all contradicting SCOPE §1, §4 and §8.
Those fields are removed and the witness posture restated to match §4. The
bibliography is retained unchanged and is the reason the files are kept. Each
carries a banner saying it states no project decision.

**`translation-drafts/`** holds three of the six predecessor
`translation-system/` files — the two author profiles and the terminology
method — as drafts, not doctrine. `GENRES.md` and the evaluation blocker were
left behind, as was root-level `TRANSLATION_PROTOCOL.md`.

## Deliberately not ported

- 19MB of out-of-scope witnesses (FG-RIC, NM-PRIN, FG-SDI, NM-COR-OUT, the two
  legations). Only FG-CONS and NM-DISC came across: 1.6MB.
- `scripts/validate`, 1,155 lines. To be rewritten; see `scripts/README.md`.
- `TRANSLATION_PROTOCOL.md`, `translation-system/profiles/GENRES.md`,
  `sources/handoffs/`, 140 work items, 39 reviews, 17 of 19 decision records,
  GENESIS, CONSTITUTION, ARCHITECTURE, EDITION-GATE, SOURCE-ROUTING, ROUTING,
  GIT-WORKFLOW, the old AGENTS.md, dashboard.html, editorial-packets/.

## Outstanding

1. ~~**`DEC-009` and `DEC-010` are carried unedited.**~~ **DEC-009 done
   2026-09-21** — rewritten to one page (14,070 → 3,892 bytes) as three
   normalisation classes; the deferred questions N01–N03 are ruled in
   `decisions.md` as D33, D34 and D36. **DEC-010 still carried unedited.**
2. **`sources/handoffs/` unchecked.** SCOPE §6 asks for one pass over its 18
   records for acquisition detail recorded nowhere else, before archiving.
3. ~~FG-CONS.1.12 is still `review_pending`.~~ **Done 2026-09-18.** Both I.12
   units went through the dual cold pass and are now established at S2; see
   `sources/coldpass/`.

## Git

Initialised 2026-09-18 with the port as its first commit. History was
rewritten twice on 2026-09-26, before the first push, to remove the Palmarocchi
1933 scan images and the pre-F001 Palmarocchi text of FG-CONS.1.12. Commit
hashes cited anywhere before that date no longer resolve.

Git creates lock files and then deletes them. A Cowork session can only delete
in this folder once it has been granted delete permission; without it, every
git write leaves a stale `.git/*.lock` that blocks the next. Grant the
permission at the start of the session, or run git from Terminal.

Published from `master` to GitHub Pages by `.github/workflows/pages.yml`,
which serves `site/`.

## Provenance of the port

Predecessor repository `Machiavelli : Guicciardini Corpus`, at commit `51a8e67e12d229d3894bada8b095377c3891c665`
(488 commits). That repository is unmodified by this port and remains the
archive.

All files carried verbatim were verified byte-identical by md5 after transfer,
including the four witness scans.
