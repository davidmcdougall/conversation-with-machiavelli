---
report: dual cold pass, second run — FG-CONS.1.12 re-established
unit: FG-CONS.1.12
passes: [B (2026-09-18), C (2026-09-21)]
performed: 2026-09-21
rule: SCOPE §7 — no image-derived reading enters the text on a single model pass
supersedes: COLLATION-2026-09-18.md for this unit
disposition: one disagreement open — escalated to David, not resolved
---

# FG-CONS.1.12 — pass B against pass C

Pass A is withdrawn: FG-CONS-I12-F001 shows it transcribes Palmarocchi 1933.
Pass B (2026-09-18) and pass C (2026-09-21) are independent cold Canestrini
transcriptions by readers who saw only the page images and not each other.

Collated mechanically — `difflib.SequenceMatcher` over whitespace tokens, not
by eye. 421 tokens against 434 (pass C separates spaced apostrophe groups).

## The §7 2a check, first

**Pass C agrees with Palmarocchi nowhere.** Across every locus where F001 found
pass A siding with the comparison witness — `[ar]ebbe`, the four bare `e`
articles, `ed imperio`, `ed inclinazione`, `de barbari`, `soggiogorono`,
`violenza`, `eziamdio`, grave accents, the seven points of pointing — pass C
reads with Canestrini and against Palmarocchi, independently of pass B. Where
Palmarocchi reads `vitupèri`, pass C reads neither Palmarocchi's form nor pass
B's. Both surviving passes are reading the governing witness.

## Result

**17 divergences in 421 words. One is a reading.**

### Class C — escalates. One locus.

**`vituperii` (B) against `viluperii` (C).** Pass C magnified to 2400× and
compared the third letter against both `t` of `tutti`, four words earlier on
the same line: in this fount `t` carries a short ascender, a crossbar and a
curled foot, and the letter in question has a plain full-height vertical with
none of them. It transcribed `viluperii` as a compositor's error, printed.
Pass B read `vituperii` and did not flag it.

`viluperii` is not a word; `vituperii` is, and is the reading the sense wants —
the Roman court as an exemplar of all the world's disgraces (D26). So this is
either a genuine foul sort faithfully transcribed, or a misread `t`. **Not
resolved here.** It sits in the unit's most quotable line and it is the kind of
thing D26 already turns on. Raised as FG-CONS-I12-F002.

### Class B — findings, ruled by DEC-009, recorded so they can be reversed.

**Two sentence-final stops, at `del mondo` and at `cittadini proprii`.** Pass C
reports at 2000× that no stop is printed at either: Canestrini sets the
superscript note reference in the slot where the stop belongs. Pass B recorded
a stop at both. See O12 — this edition does not carry Canestrini's note
references in the body, so stripping them without restoring the stop would
create an artefact of our own making rather than reproduce one of the witness's.
Both are supplied, **declared**, and logged as `editorial_supply`.

**The terminal stop is not supplied.** Both passes agree none is printed after
`inclinazione sua`, and the asymmetry with the two above is principled: those
restore a break the note reference displaced; this one would close a period the
author left open. problematic.md requires the unit to end mid-thought. O07 is
settled here in that sense.

**`de' Barbari` (B) against `de Barbari` (C).** Pass C checked at every contrast
level and reports clean white at ascender height. Apostrophe supplied by rule
under D35 — the reading is unaffected either way.

**`d'Italia` (B) against `d Italia` (C)** at `al nome d Italia`. Pass C reports
the apostrophe absent here while present at `d' Italia` and `d'Italia` later in
the same unit. Supplied under D39.

### Class A — collapsed, not findings. Thirteen loci.

Spacing before a comma or semicolon (eight), and spacing after an elided
apostrophe (five). Canestrini sets both habits inconsistently on a single page,
so neither is the witness's practice. DEC-009 Class A rules 2 and 5.

**Both passes agree on every mark's identity** — comma at `monarchia`,
`Italia`, `altrimenti`, `republica`, `sudditi`, `Chiesa`; semicolon only at
`de' Romani` and `violenza`. That independent agreement is what finally settles
D37 and the F001 pointing table.

## Restored from the comparison witness

One mark, at `sotto uno re ␣␣ pure`. Both passes independently found a gap of
about two word-spaces with no ink; pass C measured it against the word spaces
either side. Palmarocchi p. 23 prints `sotto uno re; pure`. The semicolon is
restored as a `witness_correction` with Palmarocchi cited — a dropped sort
recovered, not a variant adopted, which is the distinction D38 turns on.

## What this run cost

One reader, about thirteen minutes. It found one word in 421 and confirmed the
other 420 against an independent reading of the same page. That is what the
rule is for, and it is the first time on this unit that the rule has run with
both passes reading the governing witness.
