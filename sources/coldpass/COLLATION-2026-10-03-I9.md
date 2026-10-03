---
report: dual cold pass, pair I.9
units: [NM-DISC.1.9, FG-CONS.1.9]
passes: [A (drafting session), B (subagent, page images only, separate directory per unit)]
comparison_reads: [NM-DISC.1.9-1554 (subagent, Giglio 1554 page images only, separate directory)]
performed: 2026-10-03
rule: SCOPE §7
method: difflib.SequenceMatcher over word and punctuation tokens, case-sensitive, after DEC-009 Class A on both sides
disposition: NM clean; FG clean in word, one verbless period emended as D114 (D167); pointing by D67, D110 and D40
---

# Pair I.9 — pass A against pass B

All three cold readers were dispatched before pass A was made, each with a
directory holding only its page images, and returned only boundaries, counts
and paths. The 1824 pages went at native 350 ppi with top/middle/bottom
crops; the Canestrini pages at native 600 ppi, a 2x upscale, and half-page
crops at 3x; the Giglio leaves at 500 ppi with thirds.

## NM-DISC.1.9 — 1824, pp. 49–52

882 words (both passes, elisions split). **No word, clause or sense
disagreement**: after Class A the two token streams are identical. Both
passes find the same boundaries (CAPITOLO IX under the running head on
p. 49; `e non biasimo.` on p. 52, rest of the page blank; CAPITOLO X opens
p. 53), the same three-line italic rubric with a full stop, one printed block
with a drop capital `E'`, no notes, and the page split `occu-|pare`
(pp. 51–52). Both passes independently mark the one doubtful mark in the
unit: the point after `ordinato bene` (p. 49), which prints low and
tailless before a lower-case `o`. Read as a comma; Class B pointing, not a
reading.

## FG-CONS.1.9 — Canestrini, pp. 22–23

334 words. One printed paragraph (indent at `Non è dubio`), as both passes
find. Two editor's notes, (1) on p. 22 quoting Machiavelli's general rule and
(1) on p. 23 on the life of Romulus, are Canestrini's and are not carried.
After Class A the passes differ in no word. Pass B marks twelve body loci
uncertain on damaged letters (`che`, `uno`, `laude`, `cattiva`,
`constituite`, `autorità`, `annichilate`, `continui`, `mutare`, the `E` of
`E adunque`, a speck between `da` and `pregare`, and the mark after
`fraude`); pass A reads the same words at every one. No letter is doubtful
to both readers, so nothing is escalated under D156.

**One verbless period.** Both passes read `E adunque questo uno modo di
medicina` without an accent, and both note it. As printed the period has no
finite verb. Emended `[È]` under D68, as D114, D144 (the same phrase, `E
adunque`, in FG I.7) and D157: **D167**. The 1933 edition prints `È`. Unlike
the I.3, I.7 .01 and I.8 cases this is mid-paragraph, after a dropped stop,
not the opening of the unit; the ground (no finite verb) is the same.

**Pointing.**

| Locus | Pass A | Pass B | 1933 | Disposition |
|---|---|---|---|---|
| .01 `con la fraude ___ e modi` | ⟨,\|.⟩ | ⟨.\|,⟩ | none | Both see a mark, neither can weigh it, the 1933 edition prints none: the lighter reading, a comma, stands (D110) |
| .01 `estraordinarii Ma` | none | none | `estraordinari.` | C001, D67 |
| .01 `fussi stata buona E adunque` | none | none | `buona. È` | C002, D67 |
| .01 `in esemplo Ma chi` | none | none | `esemplo.` | C003, D67 |
| .01 `reprensione A quello` | none | none | `repren-|sione.` | C004, D67 |
| .01 `troppa autorità bisogna` | gap, no mark | gap, no mark | `autoritá:` | C005, D67; lower case follows, so the 1933 colon, not a point |
| .01 `considerarla bene` (unit end) | none | none | `bene.` | Not supplied (D40) |

Class A (accents; spaces before commas at `autorità ,`, `annichilate ,`,
`stabilisca ,`, `esemplo ,`, `propria ,`) applied by rule and not enumerated.

## Comparison witnesses

Witness independence (SCOPE §7): the passes disagree at one locus, the mark
after `fraude`, where pass A reads a comma, pass B a point, and the 1933
edition nothing. No pattern. Neither pass carries any Palmarocchi reading
listed below.

**FG, 1933 edition.** Readings that differ in word from Canestrini, for the
variant notes: `la violenzia o con la fraude` for `la violenza e con la
fraude`; `le legge` for `le leggi`; `Romolo` (twice) for `Romulo`; `adunche`
for `adunque`; and Palmarocchi's bracketed title, with `fuor degli` for
`fuori delli`. Everything else is Palmarocchi's orthographic profile (`el`,
`ed` before vowels, `-nzia`, `pericolo`, `volontá`, `commune`, `amazzato`)
and his heavier pointing (semicolons at `cattiva`, `stabilisca`, `esemplo`,
`propria`; no comma at `Licurgo`, `fatto`, `detestabile`, `senato`), and is
not enumerated.

**NM, 1554 Giglio.** A third reader transcribed fol. 18r–19v cold
(`NM-DISC.1.9-1554.md`); the transcript was collated by word against the
established 1824 text, spelling normalised (u/v, h, -ti-/-zi-, doubled
consonants, `&`). The readings cited below were checked on the page image by
the collator. Giglio is again the same argument in other words; the
differences that bear on the English:

- rubric: `riformata` for `riformarla`, and no `o` before `al tutto`.
- .01 `questa parte` for `queste parti`; `uno formatore` for `un fondatore`;
  `habbia prima leuato di uita` for `abbia prima morto`; `T. Tatio`.
- .02 `l'auttorita solamente` for `l'autorità solo`; `piu chini al male` for
  `più pronti al male`; `quando ella rimanga ..., quando rimane`.
- .03 `di ragionare il Senato` for `di ragunare` (a misprint or a different
  verb); `non fu introdotto alcun nuouo ordine` for `non fu innovato alcun
  ordine dello antico`; `approua` for `testifica`.
- .04 `confermatione` for `corroborazione`; `Ligurgo` throughout; `Che
  considerando Agide` for `che desiderando Agide`; `usciti fuori` for
  `deviati`; **`fece uenire tutti gli Ephori`** for `fece ammazzare tutti gli
  Efori` (summoned rather than killed); `per se medesimo` for `per sè
  stesso`.
- .05 `Considerate adunque` (the participle agreeing) for `Considerato`;
  `iscusa`.
