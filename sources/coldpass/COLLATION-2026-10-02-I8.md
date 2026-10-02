---
report: dual cold pass, pair I.8
units: [NM-DISC.1.8, FG-CONS.1.8]
passes: [A (drafting session), B (subagent, page images only, separate directory per unit)]
comparison_reads: [NM-DISC.1.8-1554 (subagent, Giglio 1554 page images only, separate directory)]
performed: 2026-10-02
rule: SCOPE §7
method: difflib.SequenceMatcher over word and punctuation tokens, case-sensitive, after DEC-009 Class A on both sides
disposition: NM clean; FG one doubtful letter escalated and ruled (D156), one verbless opening emended as D114 (D157); pointing by D67 and D40
---

# Pair I.8 — pass A against pass B

All three cold readers were dispatched before pass A was made, each with a
directory holding only its page images, and returned only boundaries, counts
and paths. The 1824 pages went at native 350 ppi with top/middle/bottom
crops; the Canestrini pages at native 600 ppi, a 2x upscale, and half-page
crops at 3x; the Giglio leaves at 500 ppi with thirds.

## NM-DISC.1.8 — 1824, pp. 44–48

965 words (995 tokens with elisions split, both passes; 997 by pass B's own
count). **No word, clause or sense disagreement**: after Class A the two token
streams are identical. Pass B marks thirteen loci uncertain, all on damaged
type or stray marks (`seminare`, `ordine`, `ordinatore`, `senz'`,
`irritati`, `tempo`, `arebbono`, `stati`, `Fiorentino`, `di`, `benche`, and
the weight of the commas after `odio` and `potendo`); pass A reads every one
alike. Both passes find the same boundaries (CAPITOLO VIII after `seguente
discorreremo.` on p. 44; `punito Manlio.` at p. 48 l. 26; CAPITOLO IX opens
p. 49), the same two-line rubric with a full stop, one printed block with a
drop capital, no notes, and the page splits `ono-|re` (pp. 44–45) and
`con-|tento` (pp. 47–48).

Both read `E benche` without an accent on p. 48 (`benchè` elsewhere): Class A.

## FG-CONS.1.8 — Canestrini, pp. 20–21

443 words. One printed paragraph (indent at `E vera conclusione`), as both
passes find. Two editor's notes, (1) on Cosimo de' Medici and (2) on Giovanni
Guicciardini, are Canestrini's and are not carried. After Class A the passes
differ only at `malignità` (pass B leaves the accent open) and in the note
references, which pass A omits from the text.

| Locus | Pass A | Pass B | 1933 | Disposition |
|---|---|---|---|---|
| .01 `fomentorono ___ feciono` | ⟨e\|a⟩ | ⟨e\|a⟩ | `e feciono` | **D156**, David 2026-10-02: `e`, a reading. Common doubt; the letter prints a-shaped; e loses its crossbar throughout the scan (`falsamento` for `falsamente`, p. 21); `a` does not construe. |

**One verbless opening.** Both passes read paragraph-initial `E vera
conclusione` without an accent, and both note it. As printed the period has
no finite verb in its main clause. Emended `[È]` under D68, as D114 and D144:
**D157**. The 1933 edition prints `È`.

**Pointing.**

| Locus | Pass A | Pass B | 1933 | Disposition |
|---|---|---|---|---|
| .01 `per sé stesse Né` | none | none | `stesse.` | C001, D67 |
| .01 `accusato falsamente Ma` | none | none | `falsamente.` | C002, D67 |
| .01 `da sé medesime caggiono E lo` | none | none | `caggiono.` | C003, D67 |
| .01 `calunniatori, basta, che` | comma | comma | `calunniatori; basta che` | Canestrini's commas, read alike by both; kept (D65) |
| .01 `non sarebbe stato` (unit end) | none | none | `stato.` | Not supplied (D40) |

Class A (accents, including pass B's open `malignità`; the plural article at
`e' carichi`, `e' disordini`, `e' cittadini`, `e' giudicii`, D35; elision at
`l'ha`; spaces before punctuation) applied by rule and not enumerated.

## Comparison witnesses

Witness independence (SCOPE §7): at the one doubtful letter both passes
leave the reading open; at `malignità` pass A agrees with the 1933 accent and
pass B leaves it open. No pattern. Neither pass carries any Palmarocchi
reading listed below.

**FG, 1933 edition.** Readings that differ in word from Canestrini, for the
variant notes: `tanto naturale` (singular) for `naturali`; `traporterá` for
`trasporterà`; `come neanche fanno` for `come né anche fanno`; `è uno sogno`
for `è un sogno`; `nacque le divisione` for `la divisione`; `e' giudici` for
`e' giudicii`; and Palmarocchi's bracketed title. Everything else is
Palmarocchi's orthographic profile (`el`, `ed` before vowels, `abondanzia`,
`prudenzia`, `innocenzia`, `de'`, `popolo`) and his heavier pointing
(semicolons at `romori`, `calunniatori`, `regolata`, `opprimono`, `sogno`,
`Guicciardini`, `carcere`), and is not enumerated.

**NM, 1554 Giglio.** A third reader transcribed fol. 16r–17v cold
(`NM-DISC.1.8-1554.md`); the transcript was collated by word against the
established 1824 text, spelling normalised (u/v, h, -ti-/-zi-, doubled
consonants, `&`). The readings cited below were checked on the page image by
the collator. Giglio is again the same argument in other words; the
differences that bear on the English:

- .01 `libera Roma dallo assedio, & dalla oppressione de Franciosi` (the siege
  as well as the oppression); `laudi, della guerra` for `belliche laudi`; no
  `e` before `quando si rihauesse`; `prigione` for `carcere`.
- .02 `dannose & pessime le calunnie` for `detestabili`; `ciascuno puo essere
  calunniato`, without `da ciascuno`; `Vsasi questa calunnia`, without `più`;
  `aspramente` for `acremente`; `commouono ... gli commossi` for `irritano ...
  gl'irritati`; `contro a loro` for `contro di loro`.
- .03 `all'appetito suo si opponeuano, et faceuano assai`, without `che`;
  `la parte del gran popolo` for `del Popolo`.
- .04 `contento d'un solo`; `Firentino`, `Luca`; `Guicciardoni buō
  commissario` (a misprint of the name, and "good commissary" for
  `Commissario`); `nemici` for `nimici`.
