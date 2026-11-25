# Port manifest

Moved from `SCOPE.md` §6 on 2026-11-25: the record of the 2026-09-18 port
from the predecessor repository, not doctrine. References to "SCOPE §6" mean
this file. See also `PORT-NOTES.md`.

Audited against the old repository on 2026-09-18. Counts and sizes below are
measured, not estimated.

**Carry:**

```
sources/witnesses/{FG-CONS,NM-DISC}/    1.6MB — I.12 extracts + witness metadata
sources/normalized/{NM-DISC,FG-CONS}/   2 files
sources/comparisons/{NM-DISC,FG-CONS}/  2 files
sources/provenance/{NM-DISC,FG-CONS}/   10 files
sources/findings/{NM-DISC,FG-CONS}/     2 files
corpus/NM-DISC/NM-DISC.1.12.md
corpus/FG-CONS/FG-CONS.1.12.md
relationships/FG-CONS/*.md           → links/pairing-map.md  one file, not 39
register/machiavelli/NM-DISC.md      → sources/register/, rewritten per §4
register/guicciardini/FG-CONS.md     → sources/register/, rewritten per §4
translation-system/profiles/MACHIAVELLI.md      as draft, not doctrine
translation-system/profiles/GUICCIARDINI.md     as draft, not doctrine
translation-system/TERMINOLOGY-METHOD-v0.9.md   as draft, not doctrine
qc/source-integrity/                    pilot doc + one run's results
decisions/DEC-009, DEC-010              rewritten to one page each
.gitignore
scripts/validate                     → not carried; rewritten per §7
```

**Do not carry, and know why:**

- **`sources/witnesses/` in full.** 21MB exists; 19MB of it is FG-RIC,
  NM-PRIN, FG-SDI, NM-COR-OUT and the two legations — every one out of scope
  under §8. Draft 0.2 of this manifest said "all of it (~22MB)."
- **`scripts/validate`.** 1,155 lines checking route states, self-merge tags,
  HEAD conventions and legacy glyph claims — machinery this file deletes. See
  §7.
- **`TRANSLATION_PROTOCOL.md`.** Never listed in draft 0.2's manifest, and it
  should be left behind deliberately rather than by omission: it is built on
  DEC-013 route states, risk tiers A/B/C and freeze-at-v1.0 language this file
  abolishes. Anything load-bearing in it folds into §3.
- **`translation-system/profiles/GENRES.md`.** Built for the whole-works
  ambition.
- **`sources/handoffs/`.** 18 old work-item records. Check once for
  acquisition detail recorded nowhere else, then archive.

**Archive, do not delete:** everything else — 140 work items, 39 reviews, 17
of 19 decision records, GENESIS, CONSTITUTION, ARCHITECTURE, EDITION-GATE,
SOURCE-ROUTING, ROUTING, GIT-WORKFLOW, AGENTS.md as written, dashboard.html,
`editorial-packets/`. The old repository stays on disk, untouched, as a
sibling.

**Git history.** The old repository carries 488 commits. The new one starts
from `git init` with none. That is a decision, not an oversight: provenance
lives in unit front-matter, and the old history survives in the archived
sibling. Record the old repository's final commit hash in the new one's first
commit message so the two can be tied together later.

**Out of scope, archived with regret:** `NM-PRIN.15` and `FG-SDI.1.1`. Both
established S2, both real work, neither in the pairing. Seed of a second
project, not a reason to widen this one.

**Layout:**

```
conversation-with-machiavelli/
  SCOPE.md          the only doctrine
  AGENTS.md         20 lines
  corpus/           established Italian, by unit
  translations/     English, by unit
  sources/          witnesses, normalized, comparisons, provenance, findings
  links/            the 39 response records
  site/             the build
  scripts/          validate · state · build
```
