---
report: dual cold pass, pair I.7
units: [NM-DISC.1.7, FG-CONS.1.7]
passes: [A (drafting session), B (subagent, page images only, separate directory per unit)]
comparison_reads: [NM-DISC.1.7-1554 (subagent, Giglio 1554 page images only, separate directory)]
performed: 2026-10-02
rule: SCOPE §7
method: difflib.SequenceMatcher over word and punctuation tokens, case-sensitive, after DEC-009 Class A on both sides
disposition: NM clean; FG one doubtful letter escalated and ruled (D145), one split kept as printed (D146), two verbless openings emended as D114 (D144); pointing by D67 and D40
---

# Pair I.7 — pass A against pass B

All three cold readers were dispatched before pass A was made, each with a
directory holding only its page images, and returned only boundaries, counts
and paths. The 1824 pages went at native 350 ppi with top/middle/bottom
crops; the Canestrini pages at native 600 ppi, a 2x upscale, and half-page
crops at 3x; the Giglio leaves at 500 ppi with thirds.

## NM-DISC.1.7 — 1824, pp. 40–44

1,056 words (1,075 by pass B's count, which splits elisions). **No word,
clause or sense disagreement.** Pass B marks three loci uncertain on damaged
type (`diano`, with a stray mark over the n; `ne` and `fare` at line ends on
p. 42); pass A reads all three alike. Both passes find the same boundaries
(CAPITOLO VII at the top of p. 40 under the running head; `discorreremo.` at
p. 44 l. 15; CAPITOLO VIII follows on p. 44), the same two-line rubric with a
full stop, one printed block with a drop capital, no notes, and the page
split `sola-|mente` (pp. 42–43).

Both read `per non essere dentro a quello cerchio ordine` (p. 43). It is a
hard phrase; the 1554 edition prints `quel cerchio ordine` too, so it is the
witnesses' reading and stands.

## FG-CONS.1.7 — Canestrini, pp. 18–20

470 words. Three printed paragraphs (indents at `E verissimo`, `E adunque`,
`Bisogna adunque`), as both passes find. One editor's note, (1) on
`Quarantía`, is Canestrini's and is not carried.

| Locus | Pass A | Pass B | 1933 | Disposition |
|---|---|---|---|---|
| .02 `procedono troppo respettivi, ___ in fatto e' giudici` | ⟨e\|o⟩ | ⟨e\|o⟩ | `ed in fatto` | **D145**, David 2026-10-02: `e`, a reading. Common doubt; the letter prints o-shaped as e does throughout the page (`essero`, `parto`, `opiniono`); `o` hardly construes. |
| .02 `la superficie ___ i titoli` | `o` | ⟨e\|o⟩ | `ed e' titoli` | **D146**: `o`, as printed (as D73). Construes; the 1933 reading in the variant note. |
| .02 `muoversi ___ rumori` | ⟨a'\|n'⟩ | `a'` | `a' romori` | `a'`: the letter is broken; `n'` is not a word here. Not a split. |

**Two verbless openings.** Both passes read paragraph-initial `E verissimo`
(.01) and `E adunque necessario` (.02) without an accent, and both note it.
As printed neither period has a finite verb. Emended `[È]` under D68, as
Canestrini's own `E posto` in I.3 was (D114): **D144**. The 1933 edition
prints `È` at both.

**Pointing.**

| Locus | Pass A | Pass B | 1933 | Disposition |
|---|---|---|---|---|
| .01 `vessati o puniti Perché` | none | none | `puniti.` | C001, D67 |
| .01 `in Coriolano` (end of ¶1) | none | none | `Coriolano.` | C002, D67: a paragraph end, not the unit end |
| .02 `più di cinquanta E certo` | none | none | `cinquanta.` | C003, D67 |
| .02 `male disposte E che` | none | none | `disposte.` | C004, D67 |
| .02 `per via del populo in esemplo` | none | none | `popolo:` | C005, D67: lower-case `in` follows, so the 1933 colon, not a stop |
| .03 `degli estremi` (unit end) | none | none | `estremi.` | Not supplied (D40) |

Class A (accents, including Canestrini's `Quarantía` and the pass B
circumflex on `tôrre`, both normalised; the plural article at `e' cattivi`,
`e' cittadini`, `e' giudici`, `e' Gracchi`, `e' quali`, D35; elision and
apocope spacing at `s'ha`, `a' giudicii`) applied by rule and not
enumerated.

## Comparison witnesses

Witness independence (SCOPE §7): at the one split pass A reads `o` with
neither witness reading against it, and pass B leaves it open; at `a'` pass B
agrees with the 1933 edition and pass A leaves it open. No pattern.

**FG, 1933 edition.** Readings that differ in word from Canestrini, for the
variant notes: `ed in fatto` (D145); `ed e' titoli` (D146); `ed [è] facile`,
where Canestrini prints `è facile` without the conjunction; `si vedde di
Alcibiade` (Canestrini `si vede`); and Palmarocchi's bracketed title
`[Quanto siano in una republica necessarie le accuse a mantenerla in
libertade.]`, which is his, not Canestrini's. Everything else is
Palmarocchi's orthographic profile (`el`, `adunche`, `legge`, `accusazione`,
`ragione`, `omori`, `voluntà`, `importanzia`, `ed` before vowels) and his
heavier pointing (semicolons at `stato`, `republica`, `altri`, `Atene`,
`respettivi`, `moltitudine`, `menata`, `populo`), and is not enumerated.

**NM, 1554 Giglio.** A third reader transcribed fol. 14r–15v cold
(`NM-DISC.1.7-1554.md`); the transcript was collated by word against the
established 1824 text, spelling normalised (u/v, h, -ti-/-zi-, doubled
consonants, `&`). The readings cited below were checked on the page image by
the collator. Giglio is again the same argument in other words; the
differences that bear on the English:

- .01 `si da uia a sfogare quelli humori` for `si dà via onde sfogare a quelli
  umori`; `rouinare tutta una Republica` for `rovinare in tutto`; `che la
  commouono` for `che l'agitano`.
- .02 `adirata` for `irritata`; `che ella si haueua in pregiudicio della
  nobilità presa`, without `acquistata, e`; `esso prese tanto disdegno ... lo
  harebbe` (singular) for `venne in tanta indegnazione ... lo arebbero`.
- .03 `ne passano a cosa` for `né trascendono a cosa`.
- .04 `confermare questa oppenione` for `corroborare`; `saria proceduto` for
  `resultato`; no `dai partigiani` (`si procacciano i partigiani, nascon le
  parti`).
- .05 `fare de fautori`; `auanzare il uiuere ciuile` for `trascendere`.
- .06 `a fermezza della soprascritta conchiusione` for `a fortificazione`; `a
  modo di pochissimi` for `de' pochi`; `quell'ingordigia` for `quello
  appetito`; `quel cerchio ordine`, agreeing; `a i molti giudici` for `agli
  assai giudici`.
- .07 `raconta` for `riferisce`; `Franciosi` for `Francesi`.
