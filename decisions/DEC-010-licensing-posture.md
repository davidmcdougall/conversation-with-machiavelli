---
id: DEC-010
date: 2026-07-17
class: editorial
status: adopted
decided_by: David McDougall
supersedes: null
superseded_by: null
review_horizon: "first public release — outbound commitment ratified or revised then, with counsel review of the concrete rights table (ARCHITECTURE §4)"
---

# DEC-010 — Licensing posture: clean inbound, CC BY intent outbound

## Issue

The project has per-witness *inbound* rights assessment (ARCHITECTURE §4) but no doctrine for what license its own outputs will carry, and no rule for whether copyleft-licensed source layers may enter the corpus. The question stopped being abstract with WI-000048: the 1814 witness's scan layer is public domain, but its Wikisource transcription layer is CC BY-SA 3.0/GFDL (audit: qc/reports/AUDIT-WI-000048-post-merge.md, advisory note 1). WI-000049 establishment needs the inbound rule now; the outbound posture determines it.

## Background asymmetry

Outbound licensing is reversible-by-addition: nothing is published yet, and a rights holder can always add a more permissive grant later, but cannot retract one. Inbound share-alike is the only irreversible move available today: once SA-licensed expression is incorporated into established text, every derivative — including all translations — inherits the share-alike obligation, and sole-ownership flexibility (dual licensing, publisher agreements) is permanently lost for the affected units.

## Decision (on adoption)

**1. Inbound rule — the corpus stays clean of license-encumbered expression.**
Reproduced text in `sources/normalized/` and `corpus/` derives only from public-domain layers (page images, PD editions' body text). License-encumbered layers — CC BY-SA transcriptions, modern critical apparatus, and similar — may be *consulted* as collation and adjudication aids: readings, variants, and page correspondences are facts and may inform establishment, with the consulted layer credited in provenance. Their expression is not copied. Any exception is a superseding decision, never an item-level choice.

**2. Outbound intent — CC BY 4.0.**
The project's stated intent is to release translations, established text, and editorial apparatus under CC BY 4.0, and tooling under an OSI-approved permissive license (MIT). Rationale: the project's founding thesis is repairing an access failure; attribution-only maximizes reach (Wikimedia projects, aggregators, coursepacks, downstream editions) while preserving David's own unrestricted rights as author, including later print or commercial editions. CC BY-NC was considered and rejected for its second-order effects: Wikimedia exclusion, institutional avoidance of NC ambiguity, and reach costs that contradict the thesis. CC BY-SA was rejected inbound-and-outbound together: its practical effect here would be to bind the project's most valuable layer (translations) to the terms of its cheapest input (a transcription that S2 collation substantially reproduces anyway).

**3. Commitment point.**
The CC BY intent governs planning but is formally ratified at first public release (the review horizon), after counsel reviews the concrete per-witness rights table required by ARCHITECTURE §4. Until ratification, nothing is published and no grant is made. This is posture, not legal advice.

**4. Bookkeeping.**
Witness records gain no new fields; the existing `rights_assessment.corpus_reuse` values must henceforth distinguish `reproducible_in_corpus` (PD layers) from `consultable_only` (encumbered layers). WI-000049 and all establishment items apply rule 1 from their first commit.

## Consequences for open work

WI-000049 (Principe XV establishment): transcribe from the 1814 page images and the PD Burd body text; use the Wikisource proofread transcription as a collation aid with provenance credit; do not copy it. SOURCE-NM-PRIN-15-001 (the «fedífrago» glyph) is resolved against the page image per DEC-009 §8 regardless. The same pattern governs the remaining sixteen acquisition/establishment items.

## Adoption

Adopted by David McDougall, 2026-07-17, as proposed. Point 1 (clean inbound) is effective immediately and governs WI-000049 and all establishment items; points 2–3 record CC BY 4.0 intent with ratification gated on counsel review at first public release.
