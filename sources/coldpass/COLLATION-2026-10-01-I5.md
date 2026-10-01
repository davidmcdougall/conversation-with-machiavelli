---
report: dual cold pass, pair I.5
units: [NM-DISC.1.5, FG-CONS.1.5]
passes: [A (drafting session), B (subagent, page images only, separate directory per unit)]
comparison_reads: [NM-DISC.1.5-1554 (subagent, Giglio 1554 page images only, separate directory)]
performed: 2026-10-01
rule: SCOPE §7
method: difflib.SequenceMatcher over word and punctuation tokens, case-sensitive, after DEC-009 Class A on both sides
disposition: NM clean; FG clean at word, clause and sense; pointing resolved by D40, D67 and D110
---

# Pair I.5 — pass A against pass B

Both B passes were dispatched before pass A was made, in separate
directories, and returned only locations, counts and paths. The Canestrini
pages went to the reader at native 600 ppi, upscaled 2x, with half-page crops
(the I.4 fault not repeated); the 1824 pages at native 350 ppi with
top/middle/bottom crops.

## NM-DISC.1.5 — 1824, pp. 29–32

827 words. **One token difference after Class A**, and it is not a reading:
p. 30 `dominati⟨,|;⟩ e per conseguente`, a faint low mark that pass A read
as a comma and pass B marked uncertain, leaning comma. Comma stands (D65's
lighter reading). Both passes find the same boundaries (CAPITOLO V at the top
of p. 29; `dagli altri.` at p. 32 l. 19; CAPITOLO VI opens p. 33), the same
four-line rubric, one printed block with a drop capital, no notes. Both read
`Da questa e' vollono` (feminine) and both pass over a stray accent on
`sottilmente`.

## FG-CONS.1.5 — Canestrini, pp. 14–16

490 words. **No word, clause or sense disagreement.** Both passes find the
heading after `con le arti della pace.` on p. 14, two printed paragraphs
(indents at `Io non intendo`, `Ma quando fussi`), one editor's note on p. 15
(not part of the unit), and the same letter damage — barless e (`dovo`,
`difendero`, `plabei`, `chiamara`, `a in uno`, `volesai`, `quallo`), u broken
into n (`particnlare`, `gnardia`, `qnanto`, `nna`), dots of ii lost
(`patrizu`) — every one read the same way. Both read `plebeio` as printed;
the 1933 edition prints it too.

**Pointing.** Five places where the impression shows no stop or a mark
neither reader can weigh:

| Locus | Pass A | Pass B | 1933 | Disposition |
|---|---|---|---|---|
| .01 `fu ne' plebei(1) Benché` | none | none | `plebei.` | C001, D40: the note reference stands where the stop was |
| .01 `ufficio loro Ma` | none | none | `loro.` | C002, D67 |
| .01 `dell'altro` (paragraph end) | none | none | `l'altro.` | C003, D67 |
| .02 `distinzione⟨.\|:⟩ o tu vuoi` | ⟨.\|:⟩ | ⟨.\|:⟩ | `distinzione:` | C004, D110: both see a mark; the 1933 edition breaks the tie |
| .02 `non plebeo E` | none | none | `plebeo.` | C005, D67 |

`promiscua così`: pass B notes a wide gap and no mark; pass A none; the 1933
edition none. Nothing supplied.

Class A (accents; the plural article `e'` at `e e' nobili`, `e e' consuli e
e' dittatori`, `come e' tribuni`, `e' tribuni`, `e' cittadini`; the
apostrophe dropped at `ne' grandi` and `da' dittatori`, D39; elision spacing)
applied by rule and not enumerated.

## Comparison witnesses

Witness independence (SCOPE §7): the passes do not disagree at any word, so
there is no set of loci to test against the comparison witness. At the five
pointing loci both passes see the same thing and neither sides with the 1933
edition. No pattern.

**FG, 1933 edition.** Readings that differ in word from Canestrini, for the
variant notes: `autorità o cura particulare` (.01; Canestrini without `o
cura`); `v'avevano cura` (.01; Canestrini `n'avevano`); `si vedde` (.01;
`si vede`); `contro a chi volessi opprimere tutta la republica` (.01;
Canestrini `volesse`). Everything else is Palmarocchi's orthographic profile
(`el`, `titolo`, `popolo`, `patrizi`, `prudenzia`, `ignoranzia`, `ed` before
consonants, `uficio`, `coniurazione`, `amazzato`, `crederrò`) and his heavier
pointing (`grandi;`, `opprimere;`, `plebei;`, `nobili;`, `conservi;`), and is
not enumerated.

**NM, 1554 Giglio.** First comparison collation of a *Discorsi* unit since
the 1554 extracts were re-cut (2026-10-01). A third reader transcribed the
Giglio leaves cold (fol. 9v–11r; `NM-DISC.1.5-1554.md`), and the transcript
was collated by word against the established 1824 text, with spelling
normalised (u/v, j, h, -ti-/-zi-, accents, `&`). Every reading cited in a
variant note below was checked on the page image by the collator.

Giglio's chapter is the same argument in a different wording: beyond
spelling, some dozens of words differ, and most are synonyms or reorderings
(`dato forma a`/`costituita`, `commessa`/`collocata`, `posta`/`messa`,
`discordie`/`dissensioni`, `dannosi`/`nocivi`, `noceuole`/`nociva`,
`trattata`/`agitata`). The ones that bear on the English:

- .02 `hanno meno desiderio di usurparla` (1824 `appetito`) and `in quelli
  cupidigia grande di dominare` (1824 `desiderio`) — the chapter's appetite
  vocabulary is distributed differently.
- .03 `sodisfano piu all'ambitione loro, che hauendo piu parte nelle
  Republiche` (1824 `all'ambizione di coloro ch'avendo più parte nella
  Repubblica`).
- .03 `da questo è uollono` (1824 `Da questa e' vollono`).
- .04 `stare in dubbio`, `fusse eletta`, `a cui basti mantenersi`.
- .05 `Marco Follio` (1824 `Marco Fulvio`; Livy's Marcus Folius).
- .05 `dove si disputò, quale` (no `assai`) and `perche l'uno, & l'altro
  appetito` (no `facilmente`).
- .05 `con maggiore potentia, et con maggiore mouimento`; `potere anchora
  essi entrare`.
