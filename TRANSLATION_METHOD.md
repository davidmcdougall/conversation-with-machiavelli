# Translation method

How the English translation of *A Conversation with Machiavelli* was
produced. Licensing is in `LICENSE`; source rights are in
`RIGHTS_AND_SOURCES.md`. Statements below are limited to what the repository
records. Where it records nothing, this document says so.

## Translation credit

The canonical credit is:

> AI-assisted translation edited by David McDougall

Use this wording throughout the project. "Edited by David McDougall" refers
to the edition as a whole.

David McDougall is not the sole translator. No AI model is a legal co-author
or copyright holder.

## Translation process

Each pair runs through the six-stage pipeline in SCOPE §3. The steps below
cover its translate, annotate and publish stages as they apply to the
English.

1. **Initial drafts.** Each unit is drafted against the established Italian in
   `corpus/`, Machiavelli first, then Guicciardini against it, with the
   register, glossary, names, Latin and problematic files in `apparatus/` and
   the voice profiles in `translation-drafts/`. The draft date is recorded in
   each unit's `translated:` field. Unit front-matter does not record who or
   what drafted each unit. Git commit trailers name the model of the session
   that committed the translation for pairs I.12, I.14, I.1 and I.3 (Claude
   Opus 5.5); commits from pair I.4 onward carry no such trailer. The
   project's workflow specification, kept outside the repository (see
   Reproducibility), assigns drafting to a Claude session.

2. **AI-proposed alternatives.** Each draft is reviewed by a separate AI
   reviewer that has not seen the drafting work ("subagent with no access to
   the drafting work", `cold_review:` field in `translations/` and
   all 74 units in `translations/`). Reviewers propose corrections and
   alternative renderings. 153 rows of `apparatus/decision-log.md` mention a cold review.

3. **Comparison with the Italian.** Reviewers are given the established
   Italian with the draft (workflow specification). `scripts/build.py` asserts that every Italian
   paragraph has an English paragraph with the same identifier.

4. **Review, correction and selection.** Non-obvious choices are logged in
   `apparatus/decision-log.md` (499 D-numbered rows to date). Judgement calls are routed to
   David McDougall as numbered open items (O-numbers) with a recommendation,
   and his rulings are recorded with their dates. 169 D-rows name him. The
   repository does not distinguish, for every row, whether a ruling was made
   by David McDougall or applied by an AI session under an existing rule.

5. **Quality control.** Automated, deterministic checks (no model):
   `scripts/validate` (witness, reference, pairing, attestation and footnote
   checks; SCOPE §7), `scripts/state --check`, and the alignment and
   cross-link assertions in `scripts/build.py`. AI review: the cold reviews in
   step 2, and cold review of the commentary, recorded in the `cold_review:`
   field of 70 of 74 files in `annotations/` (62 of them backfilled on
   2026-11-24 from `apparatus/decision-log.md` and SCOPE §5). Pairs I.3 and I.4 have no
   recorded commentary review. Human review: the rulings in step 4, and
   a sample read of eight randomly drawn pairs against the Italian before v1.0
   (SCOPE §7, DEC-012), logged in `docs/sample-reads.md`. None is yet
   recorded.

6. **Publication.** `scripts/build.py` generates `site/`; GitHub Pages
   publishes it on push (`.github/workflows/pages.yml`). All 74 published
   English units carry `status: draft_cold_reviewed`. The repository records
   no separate per-unit human approval of the English. It does not establish
   that every passage was individually verified by a human.

**Modern translations.** Grayson (1965) and Atkinson & Sices (2002) are never
translation inputs. SCOPE §1 permits private consultation after a draft is
finished, as a calibration check. No such comparison is recorded in the
repository. See `RIGHTS_AND_SOURCES.md`.

## AI model provenance

| Model | Provider | Version or identifier | Role | Evidence |
|---|---|---|---|---|
| Claude Opus 5.5 | Anthropic | Product name only; no API identifier recorded | Session that committed establishment, translation, commentary and site build for pairs I.12, I.14, I.1, I.3, and related I.12 and D68 work (2026-09-26 to 2026-09-29) | `Co-Authored-By` trailers on 15 commits, e.g. `06ae5ac`, `4f23a1b`, `201eb14`, `f31aee7` |
| Claude Opus 5 | Anthropic | Product name only; no API identifier recorded | Session that committed the port, the re-establishment of FG-CONS.1.12, D38, and `LICENSE` v0.3 (2026-09-18 to 2026-09-21); normaliser of FG-CONS.1.12 | `Co-Authored-By` trailers on 7 commits, e.g. `9f91fed`, `66215a3`, `267036b`; `sources/normalized/FG-CONS/FG-CONS.1.12.md` |
| Claude Sonnet 5 | Anthropic | Product name only; no API identifier recorded | Session that committed witness acquisition for all 39 pairs and the build-script generalisation (2026-09-21) | `Co-Authored-By` trailers on `ad3a759`, `b6a241f` |
| Claude, version unstated | Anthropic | Not recorded | Witness acquisition and page extraction; one comparison-read transcription | `acquired_by` / `relocated_by` fields in 153 files under `sources/provenance/`; `sources/coldpass/NM-DISC.2.14-1554.md` |
| Unidentified | Not recorded | Not recorded | Initial translation, translation revision and annotation for pairs I.2 and I.4 onward | Units in `translations/` and `annotations/` record no drafter; their commits carry no model trailer |
| Unidentified ("subagent") | Not recorded | Not recorded | Cold review of translation and commentary (alternative readings, linguistic verification); cold-pass transcription readers | `cold_review:` fields in `translations/`; `sources/coldpass/COLLATION-*.md` `passes:` fields |
| Codex | Not recorded | Not recorded | Acquisition and normalisation of NM-DISC.1.12 and the witness-level records, in the predecessor repository | `sources/normalized/NM-DISC/NM-DISC.1.12.md`; `sources/provenance/*/*-transformation-log.yml`; `sources/provenance/*/WIT-*.yml` |
| None | — | — | Automated quality control | `scripts/validate`, `scripts/state`, `scripts/build.py` |
| None (human) | — | — | Editorial review and rulings | `apparatus/decision-log.md` |

A commit trailer names the model of the session that made the commit. It
does not establish which model performed each step inside that session, or
which model ran its subagents. Transcription pass A for pairs I.1–I.9 and I.14
was performed by the drafting session (`sources/coldpass/COLLATION-*.md`
`passes:` fields); from I.10 on, by subagents
(`sources/coldpass/COLLATION-2026-10-07-I10.md`).

Each file in `translations/` and `annotations/` now carries a `model:` field
(`drafting`, `cold_review`). The backfill records Claude Opus 5.5 as drafting
model for twelve files (pairs I.1, I.3, I.14), where the file was first
committed by an Opus 5.5 session on the day it was drafted, and `unknown`
everywhere else. Exact API model identifiers are not recorded for any role.
`claude-opus-5-5` prepared this document and the licensing changes of DEC-011;
it did no translation work.

The `Co-Authored-By` trailers are git commit metadata. They do not make any
model a co-author or copyright holder of the edition.

## Reproducibility

- Workflow specification: the project's per-pair translation skill
  (`translate-machiavelli-guicciardini`), held in David McDougall's Claude
  account. It is not in the repository and is not versioned with it.
- Apparatus supplied to drafters and reviewers: `apparatus/`,
  `translation-drafts/`, `SCOPE.md`, `apparatus/decision-log.md`.
- Prompts: not recorded.
- Model identifiers and versions: product names in git trailers for 24
  commits up to 2026-09-29; not recorded after that; no API identifiers.
- Inference settings: not recorded.

The translation cannot be reproduced exactly. Each published unit can be
checked against the established Italian and the logged rulings.

DEC-011 requires future units to record the model identifier for drafting and
review in the `model:` field.

## Editorial responsibility

David McDougall directed the editorial process and is responsible for the
published edition. Generative AI contributed substantially to the production
of the English translation. The translation credit reflects this division of
work.

## Copyright

The translation is licensed under CC BY 4.0 to the extent that protectable
rights subsist and are held or controlled by the licensor. No copyright is
asserted over material solely on the basis of its generation by AI.
