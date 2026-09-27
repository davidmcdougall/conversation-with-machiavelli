---
id: DEC-009
date: 2026-09-21
class: editorial
status: adopted
decided_by: David McDougall
supersedes: DEC-009 v1 (2026-07-16, adopted 2026-07-17 with amendments A1, A2)
review_horizon: "unit ten"
---

# DEC-009 — Normalisation

## The principle

This is a reading edition, not a text of record (SCOPE §1). The Italian layer's
job is to be readable and to be a true guide to the facing English. A witness
tells us what a nineteenth-century compositor did; it cannot tell us what a
modern reading edition should do. So orthography is ruled here, once, and
applied mechanically without opening the page; and anything that could change
what the text *says* is taken from the governing witness and never normalised.

Governing witnesses: *Discorsi* — 1824. *Considerazioni* — Canestrini 1857.

## Class A — settled here, applied silently, never reported

Fix by rule. Do not consult the page. Do not log instances.

1. **Accents.** Modern usage. Acute on closed final *e* — `perché`, `benché`,
   `né`, `sé`, `ché`, `poiché`. Grave where modern Italian sets grave — `è`,
   `cioè`, `piè`. Supply a missing accent where the unaccented form is not a
   word: `piu` → `più`. Both witnesses print grave throughout; that is house
   style and carries nothing a reader of this edition can use.
2. **Apostrophes.** Apocope takes a space — `de' Romani`, `a' suoi`,
   `e' quali`. Elision takes none — `l'ha`, `d'Italia`, `all'altre`. Supply the
   apostrophe on the Florentine plural article even where the witness omits it:
   `e' quali`, not `e quali`. It is what tells a modern reader the word is the
   article and not the conjunction.
3. **Euphonic *d*.** Modern usage — `ed`, `ad`, `od` before the same vowel
   only. Not read off the page in either direction.
4. **Encoding.** UTF-8, NFC, LF. Long `ſ` → `s`; presentation ligatures to
   their letters.
5. **Lineation.** Join line wraps. Remove a line-end hyphen where the evidence
   is a single word. Running heads, page numbers, catchwords and signatures are
   not body text.
6. **Paragraphing.** Editorial, per SCOPE §3, declared in front matter. The
   witnesses print each unit as one block.

## Class B — taken from the witness as printed

Transcribe what is there. Do not regularise, lighten or strengthen.

7. **Spelling and word forms**, including what look like compositor's errors —
   `soggiogorono`, `violenza`, `eziamdio`. The edition does not correct its
   witness.
   **Amended 2026-09-27 (D68):** except where the form is an error — not a
   word, a broken agreement, a clause left without sense. Those are emended
   from the comparison witness, bracketed in the Italian, and the printed
   form is given in the variant note. A weaker reading that construes is
   still transcribed as printed (D38).
8. **Capitalisation**, including exceptions to the page's own habit. The
   exception is often the reading (D20).
9. **Punctuation.** As printed. Canestrini points more lightly than a modern
   editor would; that is his text, not an error to repair.
10. **Terminal stops.** Never supplied. A unit that ends without one ends
    without one.

## Class C — readings, which normalisation never touches

Escalate to David. Never rerun, never resolve inside a pass.

11. Word division that changes the parse — `però` / `per ò`, `se bene` /
    `sebbene`, `sì che` / `sicché`.
12. A doubtful mark — a gap with no ink, a dropped point — where its presence
    or absence would change which clause a connective governs.
13. Bracketed supplies, illegible characters, and anything touching the
    *currere* chain or Guicciardini's four acts.
14. Any choice between witnesses. Normalisation never establishes a reading.

## What the cold pass reports

Words, clauses and sense — dropped, added, or changed in meaning. Nothing else.

A Class A divergence is not a finding: name the class in one line and move on.
A Class B divergence is a finding. A Class C divergence escalates.

## The test, in one line

Could this change what the sentence says? **No** → Class A: fix by rule, say
nothing. **Yes, and the page settles it** → Class B: take the page. **Yes, and
the page cannot settle it** → Class C: escalate.
