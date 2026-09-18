---
id: DEC-009
date: 2026-07-16
class: editorial
status: adopted
decided_by: David McDougall
supersedes: null
superseded_by: null
review_horizon: "after Source Integrity Pilot v0"
---

# DEC-009 — Conservative, reversible source normalization

## Issue

WP-004 cannot place text in `corpus/` until the project decides what
normalization means. Orthography, `u/v` and `i/j`, accents, punctuation,
abbreviation expansion, dates, line-end hyphenation, and apparatus separation
can all change what downstream translators and reviewers believe the source
says. The most dangerous failure is a plausible correction or modernization
that becomes invisible because every later stage reads the same altered text.

The repository presently contains no `sources/` or `corpus/` artifacts, so this
decision can govern the first source package without a migration. It implements
ARCHITECTURE-v0.1.md §4: witnesses remain immutable; normalized text is
versioned; transformations are recoverable; anomalies become SOURCE findings;
and rights are assessed before text enters `corpus/`.

## Evidence and constraints

1. Review 0001 identifies OCR corruption that looks like archaic Italian as the
   principal correlated-error channel and requires raw recovery plus explicit
   provenance.
2. ARCHITECTURE §4 requires source QC to flag rather than emend, and requires
   witness independence for S2 claims.
3. TRANSLATION_PROTOCOL names Florentine dating, embedded Latin, qualification
   scope, and OCR corruption as meaning-bearing hazards.
4. The WP-004 pilots deliberately include dense nineteenth-century apparatus,
   a five-state recension complex, and abbreviated and dated diplomatic prose.
   A doctrine that works only for clean modern prose would fail the programme.
5. Modern critical editions may be consulted and credited but their apparatus
   or distinctive emendations may not be reproduced without a work- and
   witness-specific rights determination.

## Options considered

### A. Diplomatic text only

Transcribe every glyph, line, abbreviation, and punctuation mark as witnessed;
make no normalized reading text.

**Advantage:** maximal proximity to the witness.

**Rejected because:** typographic and page-layout noise would enter translation
inputs; OCR and apparatus cleanup would remain ad hoc; comparison across
witnesses would be unnecessarily difficult.

### B. Conservative dual layer — proposed

Retain immutable witnesses and witness-faithful transcriptions; derive a
minimally normalized canonical reading layer. Normalize encoding and structure,
not lexical or syntactic evidence. Put expansions, date conversions, and
uncertain corrections in metadata or annotations rather than silently in body
text.

**Advantage:** supports continuous source use while retaining exact recovery,
machine-auditable intervention, and witness comparison.

**Cost:** translators may encounter historical spelling and punctuation; the
project must maintain compact transformation logs.

### C. Modernized reading text

Regularize spelling, `u/v`, `i/j`, accents, punctuation, abbreviations, and
dates for readability.

**Rejected because:** modernization changes lexical recurrence, clause scope,
dating evidence, authorial/editorial punctuation, and recension differences.
It would make interpretation precede translation and would be difficult to
reverse reliably.

## Proposed decision

Adopt Option B. The project maintains three conceptually distinct layers:

1. **Witness:** the acquired scan, OCR stream, transcription, or consultation
   record. Files under `sources/witnesses/` are immutable and append-only.
2. **Normalized source:** a versioned, witness-derived transcription suitable
   for comparison and canonical establishment. Its changes are limited by the
   rules below and linked to an immutable transformation log.
3. **Canonical corpus passage:** the adjudicated project text with stable
   passage IDs and explicit witness support. Canonical status does not erase
   variants, uncertainty, or SOURCE findings.

Normalization never establishes a disputed reading. Choosing between witnesses,
repairing uncertain OCR, or introducing an unattested reading is textual
adjudication, not normalization.

## Normalization rules

### 1. Encoding and characters

- Encode text as UTF-8 and normalize Unicode to NFC.
- Standardize line endings to LF.
- Preserve letters, lexical spelling, capitalization, diacritics, and accents
  as supported by the governing witness.
- Preserve historical `u/v` and `i/j`; do not regularize by phonetic value.
- Preserve embedded Latin as Latin and mark its language span.
- Typographic glyph mappings that do not choose a lexical reading—such as
  long `ſ` to `s` or a presentation-form ligature to its constituent
  letters—are permitted only as declared `glyph_normalization` rules. The
  witness locator and rule remain sufficient to reconstruct the witnessed
  form.
- Unicode normalization must not collapse materially distinct characters. Any
  mapping beyond NFC requires an explicit logged rule.

### 2. Whitespace, lineation, and hyphenation

- Page and folio boundaries remain addressable milestones even when line wraps
  are removed from the reading layer.
- Running heads, page numbers, catchwords, signatures, marginalia, and
  apparatus are not body text. Their exclusion is logged with a witness
  locator and structural class.
- Collapse typographic whitespace and ordinary line wraps without changing
  word order.
- Remove a line-end hyphen only when evidence supports a single word. Log
  `dehyphenation` with the witnessed and resulting forms.
- Preserve lexical, compound, or uncertain hyphens. Uncertainty produces a
  SOURCE finding; it is not resolved by a general cleanup rule.

### 3. Orthography, accents, and capitalization

- Do not modernize spelling, word division, capitalization, apostrophes, or
  accents.
- Do not silently supply missing accents or replace historical accent practice
  with modern Italian.
- Search/display aliases may be generated outside the canonical body, provided
  they are visibly derived and cannot be mistaken for source text.

### 4. Punctuation and sentence boundaries

- Preserve witness-supported punctuation and paragraph boundaries.
- Do not repunctuate long periods, split sentences, add quotation marks, or
  regularize semicolons/colons for modern readability.
- Where an edition's punctuation is demonstrably editorial, record that fact
  in provenance; it remains evidence unless a textual-establishment item
  adjudicates another reading.
- Suspected missing, duplicated, or OCR-corrupted punctuation becomes a SOURCE
  finding. Any accepted repair is logged as `witness_correction`, with evidence
  and reviewer status.

### 5. Abbreviations

- Preserve the witnessed abbreviation in the canonical body unless the
  governing source is itself an explicitly expanded diplomatic edition.
- Record expansions in structured annotations with the literal form, proposed
  expansion, evidence, certainty, and responsible agent.
- Never replace an uncertain abbreviation with an expansion in body text.
- Supplied letters, deleted text, interlinear additions, and scribal marks must
  remain distinguishable using the source schema adopted after this doctrine.

### 6. Dates, numbers, money, and measures

- Preserve literal dates, numerals, money, and measures in body text.
- Record a normalized date separately with calendar, date style, conversion
  rule, certainty, and original literal form.
- Florentine dates carry an explicit `ab_incarnatione` or other applicable
  style flag; dates from 1 January through 24 March are never year-shifted
  silently.
- Preserve ambiguous numerals and quantities as witnessed and create a SOURCE
  finding when the reading is uncertain.

### 7. Apparatus, notes, and editorial matter

- Segregate footnotes, marginal notes, variant apparatus, running material, and
  editorial commentary from authorial body text.
- Every excluded block receives a structural class and witness locator.
- Authorial notes and additions are not apparatus merely because they appear
  in a margin or note zone; uncertain agency is a SOURCE finding.
- Modern critical apparatus may be consulted and cited in provenance but is
  not copied into reusable source text unless the rights assessment explicitly
  permits it.

### 8. OCR repair and emendation

- OCR output is a witness derivative, never self-authenticating source text.
- A character or word correction requires the page image or an independent
  witness and is logged as `witness_correction`.
- An unattested conjecture is an `emendation`, must be visibly marked, and
  requires textual adjudication. It cannot be introduced by a normalization
  pipeline.
- No anomaly is corrected solely because the resulting Italian is more
  grammatical or familiar.
- Unresolved anomalies produce SOURCE findings and remain visible to canonical
  establishment and review.

## Machine-checkable transformation record

Every normalized artifact must carry or point to frontmatter containing:

```yaml
work_id:
source_unit_id:
normalized_version:
normalization_decision: DEC-009
derives_from_witnesses: []
governing_witnesses: []
input_sha256: []
output_sha256:
rights_assessment:
normalizer:
normalized_at:
transformation_log:
integrity_class:
unresolved_source_findings: []
```

The immutable transformation log contains one record per intervention or one
declared bulk record for a deterministic encoding-only rule:

```yaml
event_id:
source_unit_id:
output_passage_id:
witness_id:
witness_locator:
operation:
before:
after:
rule_id:
rationale:
evidence: []
certainty:
responsible_agent:
performed_at:
reversible: true
source_finding_id:
review_status:
```

`operation` is a controlled value:

```text
unicode_nfc
line_ending
whitespace
linewrap_join
glyph_normalization
dehyphenation
structural_exclusion
language_annotation
abbreviation_annotation
date_annotation
witness_correction
emendation
```

Additional rules:

- `before` and `after` are required for every text-changing operation.
- `witness_id` and `witness_locator` are required except for file-level
  encoding operations.
- `evidence` is required for `dehyphenation`, `witness_correction`, and
  `emendation`.
- `source_finding_id` is required for uncertain corrections and emendations.
- `review_status` is required for `witness_correction` and `emendation`.
- `reversible` must be `true`; otherwise the artifact fails validation.
- Deterministic bulk rules must name a versioned `rule_id`, input/output hashes,
  and affected span or file. A bulk rule may not perform lexical changes.
- Log entries are append-only. Superseded entries remain and point to their
  replacement; normalized artifacts receive a new version and hash.

The schema and validator implementing these fields are separate later items.
They may encode this decision only after adoption and must not enlarge it.

## Non-silent-emendation invariant

At every passage, a reviewer must be able to answer:

1. What did each witness show?
2. What changed between witness and normalized text?
3. Which changes were deterministic normalization, which were corrections,
   and which were editorial adjudications?
4. Who or what made each change, when, and on what evidence?
5. Can the exact prior state be reconstructed?

If any answer is unavailable, the passage cannot enter `corpus/`. Sampling,
fluency, agreement between two OCR streams from one scan, or downstream
translation review cannot cure the missing provenance.

## Rights and corpus gate

This decision does not determine rights for any work or witness. Every witness
package still requires its own layer-specific rights assessment. No text may
enter `corpus/` unless:

- this decision is adopted;
- the supporting witness rights assessments exist;
- the transformation record validates;
- required SOURCE findings are resolved or explicitly carried;
- the unit meets its required S-class and review gate.

## Migration and compatibility

There are no current `sources/` or `corpus/` artifacts to migrate. Existing
register entries and relationship records are unaffected. If pre-adoption
source files appear before adjudication, they remain witnesses or experimental
artifacts and must not be relabelled canonical without a compliant derivation.

At the Source Integrity Pilot v0 review horizon, evaluate whether the controlled
operations are sufficient, whether logging cost is proportionate, and whether
any rule produced false-clean text. Revision requires a superseding decision;
pilot workers do not drift the doctrine locally.

## Adjudication requested

David is asked to adopt, amend, or reject Option B after Claude's independent
Class T review. In particular, adjudication should confirm:

1. preserving historical `u/v`, `i/j`, accents, and punctuation in canonical
   body text;
2. keeping abbreviation expansions and date conversions in annotations;
3. the boundary between deterministic normalization and textual adjudication;
4. the required transformation fields and controlled operation list;
5. the prohibition on corpus entry before rights, provenance, S-class, and
   SOURCE gates are satisfied.

Until adoption, this record is a proposal only and authorizes no corpus text.


## Adoption

Adopted by David McDougall, 2026-07-17, with amendments A1 and A2 from the Class T review (qc/reports/DEC-009-class-T-review.md; branch merged as PR #2). The doctrine above stands as proposed except as amended here.

**A1 — Grouped structural-exclusion records.** For deterministic layout classes (running heads, page numbers, catchwords, signatures), one grouped transformation-log record per layout class per witness is permitted, citing a versioned rule_id and the affected page range. Footnotes, marginalia, variant apparatus, and any block with uncertain agency remain individually itemised.

**A2 — Home of normalized artifacts.** Normalized sources live under sources/normalized/ (ARCHITECTURE-v0.1 §2); the source schema item encodes this after adoption.
