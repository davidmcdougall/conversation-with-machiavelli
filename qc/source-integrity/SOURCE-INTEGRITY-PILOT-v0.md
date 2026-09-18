# Source Integrity Pilot v0

**Work item:** WI-000065
**Date:** 2026-07-19
**Status:** review draft; recommendations are non-binding

## Executive judgment

Source work is the demonstrated critical path for the pilot, not translation. Three of seven pilot units have review-approved or accepted S2 source packages (`NM-PRIN.15`, `NM-DISC.1.12`, `FG-CONS.1.12`). Four do not: the Ricordi object has 0/10 independently mapped clean units; the Borgia dispatch remains S1 for lack of an independent textual witness; the Vettori letter has an eligible independent manuscript-line input but has not completed routed transcription and adjudication; and the *Storia d'Italia* passage exists only as an unmerged S1 review draft.

All three deliberately difficult stress samples produced plausible output that was unsafe for direct establishment. Across the heterogeneous operational samples, 18/18 pages or units were false-clean under their test-specific definitions. This is not a pooled statistical estimate of the corpus: the denominators and failure tests differ. It is a consistent directional result that clean-looking extraction, recension labels, and OCR must never be treated as source integrity evidence.

## Pilot-package state

| Pilot unit | Current evidence state | Passage-ready? | Principal remaining gate |
|---|---|---:|---|
| `NM-PRIN.15` | S2 package approved after targeted evidence-record repair | yes | none within this pilot |
| `NM-DISC.1.12` | S2 accepted; decisive 1824/1554 disagreement adjudicated | yes | none within this pilot |
| `FG-CONS.1.12` | S2 accepted; direct-response relation preserved | yes | none within this pilot |
| `FG-RIC` ten-unit object | 0/10 independently mapped clean units | no | manuscript images, rights, critical crosswalk, two independent clean streams |
| `NM-LEG-BORG.1502-10-07` | S1 only; 1875 setting is textually dependent on preceding editions | no | genuinely independent manuscript-based witness |
| `NM-COR-OUT.1513-03-13` | eligible Apografo-Ricci input acquired | no | dual-cold coverage of both poles, third-family/David checks, variant adjudication |
| `FG-SDI.1.1` | five-passage S1 proposal on an unmerged branch | not accepted | Class T visual review and witness-independence resolution |

Evidence: the seven WI-000049/051/053/055/057/059/061 handoffs and item records. WI-000061 is read from branch `source_acquisition/WI-000061-establish-FG-SDI-passage` at `c5b708a`; it is not treated as merged state.

## Stress-test results

| Test | Fixed sample | False-clean result | Other measured failure | Independent coverage | Intervention |
|---|---:|---:|---|---:|---:|
| WI-000062 dense apparatus | 4 pages | 4/4 pages | 70.32% structural contamination; 99/483 body-token edit distance (20.50%) | not the test denominator | 0 human; 3.92 agent min (0.98/page) |
| WI-000063 recension complex | 10 units | 10/10 units | 5/5 linked transitions diverged; normalized divergence 14.58%–94.12% | 0/10 units | 0 human; 1.05 agent min (0.105/unit) |
| WI-000064 diplomatic OCR | 4 pages | 4/4 pages | 17/19 high-risk feature failures (89.47%); 6 structural contaminants | 0 independent witnesses | 46 human min (11.5/page) |

The operational total is 18/18 false-clean pages or units, reported only as an audit alarm. It must not be converted into a corpus-wide error rate because WI-000062 tests page contamination and OCR, WI-000063 tests independently unsupported recension labels, and WI-000064 tests diplomatic-feature preservation.

### Error and disagreement taxonomy

| Failure family | Evidence |
|---|---|
| Structural contamination | apparatus, running furniture, adjacent chapters/documents, preceding commissions, following dispatches |
| OCR character loss | 34 substitutions, 23 diacritic-only differences, 35 insertions, and 7 deletions in WI-000062's isolated body; 15 glyph substitutions plus 2 diacritic/punctuation failures in WI-000064 |
| Boundary and voice leakage | chapter XVI entering chapter XV extraction; commission, footnotes, and dispatch II entering the diplomatic sample |
| Date/hour/signature corruption | `Die 7 octobris`, `Die 8 octobris`, `ore 16`, `dì 9`, and the Latin signature corrupted by OCR |
| Recension non-equivalence | two combination contexts, one split context, and rewriting in all five measured transitions |
| False independence | same-setting reissues and dependent later editions cannot support S2; an unmapped independent witness supplies zero selected-unit coverage |

## Cost and intervention

Human and agent time are kept separate. The tests record **46 human minutes** (WI-000064 only) and **4.97 agent-assisted minutes** (WI-000062/063). Adding them into a single labour rate would be misleading. The only observed human rate is 11.5 minutes/page for the four-page diplomatic sample; it excludes download wait and is not a forecast. The apparatus and recension rates are agent elapsed-intervention measures, not human correction rates.

The pilot did not record translation time, so it cannot estimate a source-to-translation cost ratio. It can still identify the present constraint: translation cannot safely begin for four of seven units because source integrity or review gates remain unmet.

## False-clean analysis

1. Plausibility is not cleanliness. Embedded PDF text can be fluent while 70% of extracted tokens belong to apparatus or adjacent matter.
2. Zoning is necessary but insufficient. After body isolation, WI-000062 still has a 20.50% word-token error rate against the fixed reference.
3. Labels are not mappings. All ten Ricordi files name recensions plausibly, but none is independently mapped to the fixed IDs.
4. Agreement is not independence. Two scans/issues of one setting, or a later edition explicitly derived from earlier editions, cannot supply S2.
5. Diplomatic evidence is unusually fragile. Dates, hours, abbreviations, signatures, and document boundaries fail in ways that can change chronology, agency, and authorship classification.

## Limitations

- Samples were deliberately adversarial and small; prevalence cannot be generalized to the corpus.
- Definitions differ by test, so only stratified figures are inferentially safe.
- WI-000064's pinned Archive.org DjVu XML is not vendored. Its script is deterministic and hash-gated, and Opus verified arithmetic and reference readings, but the reviewer could not rerun against the live XML. Do not cite its OCR fixture strings externally until one independent rerun uses the pinned input.
- WI-000063's manifest contains an inaccurate manually entered freeze time; the immutable baseline commit precedes processing and is the authoritative timestamp.
- WI-000062 and WI-000063 report agent-assisted time, whereas WI-000064 reports human time.
- No translation-time observations exist, so the critical-path judgment is a readiness/bottleneck finding rather than a comparative productivity estimate.
- Four pilot units remain incomplete or unaccepted; failed and blocked cases remain in the seven-unit denominator.

## Non-binding recommendations

1. Treat structural zoning, append-only transformations, and full-resolution image verification as corpus-entry gates, not optional QC.
2. Land WI-000079 only after its targeted Class T schema review; its controlled independence ranks and image-verification fields encode the recurrent failure pattern.
3. Complete WI-000061's Class T visual review before using its S1 draft downstream.
4. Batch the remaining WI-000059 third-family/David readings and editorial variants; do not create canonical text from partial dual-pass coverage.
5. Continue the WI-000055 archive request and crosswalk work; do not relax the ten-unit Risk-A S2 contract.
6. Obtain a genuinely independent manuscript-based witness for WI-000057 or retain the dispatch at S1.
7. Once this report is accepted, unblock WI-000066–074 in their existing order. Their planning should budget source acquisition and boundary work as the near-term constraint.
8. Add comparable time logging to the later translation pilot before making a monetary or throughput claim about source work versus translation.

## Traceability

- WI-000062: `qc/source-integrity/WI-000062/metrics.json`, `intervention-log.yml`, `results.md`, `supersession.yml`.
- WI-000063: `qc/source-integrity/WI-000063/metrics.json`, `intervention-log.yml`, `results.md`.
- WI-000064: `qc/source-integrity/WI-000064/metrics.json`, `intervention-log.yml`, `results.md`; review at `reviews/0005-OPUS-WP004-source-branch-review-2026-07-19/01-WI-000064-review.md`.
- Pilot state: WI-000049/051/053/055/057/059 handoffs on main; WI-000061 handoff at branch commit `c5b708a`.
