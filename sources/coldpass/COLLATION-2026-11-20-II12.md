---
report: cold pass, pair II.12 (the nineteenth 1824 chapter under D199; the first after the unit-thirty review made D302 standing (D426); no eligible sample page, so a full pass B, as D352 and D391)
units: [NM-DISC.2.12, FG-CONS.2.12]
passes: [NM A (subagent, full chapter), NM B (subagent, full chapter), FG A (subagent, full), FG B (subagent, full); each with its own image, work and output folders, forbidden every other path (D370)]
comparison_reads: [NM-DISC.2.12-1554 (subagent, Giglio 1554 page images only, own folders); 1933 edition pp. 51-53 (scan pages 57-59) read by the collator at the loci below]
performed: 2026-11-20 (passes, collation, rulings by precedent; O43-O45 ruled by David the same day)
rule: SCOPE §7, as revised by D199, D203 and D302 (standing, D426)
method: difflib.SequenceMatcher over word tokens, after DEC-009 Class A on both sides; 1554 compared by word after spelling normalisation (u/v, h, j, ſ, doubled consonants, ti/zi, tildes, &/et/ed, accents, elision and word division), then read through by hand to separate forms of one word (`nimico`/`nemico`, `contro`/`contra`, `li`/`gli`, `danaro`/`danaio`, `puoi`/`poi`, numerals) from word-level differences; D203(b) letter classes e/o/a, u/n, s/a tested on the 1554 word diff and on the 1933 pages
disposition: NM two full passes identical; seven D203(b) differences and the sense-bearing whole words kept against the 1554, `aspetta[s]se` emended (D437, D438); FG one split, `lont[a]no` emended, six letters doubtful to both read with the 1933 edition, pointing by D110, no terminal stop (D439); rubrics and headings (D440); three new questions to David, ruled on the recommendations: `[temi]` (D441), `[o]` (D442), the heading as printed without `del libro II` (D443)
---

# Pair II.12 — cold passes and collation

Rendering came first, after II.10's fault (D427). Every image was cut from
the rendered page in pixels, not percentages, and checked before any reader
saw it: the 1824 pages at 350 ppi (2057 × 3228 px, native), the Canestrini
pages at 1200 ppi (1367 × 2184-2200 px; native 600), the Giglio leaves at
500 ppi. Thirds (Canestrini: halves) with a 4% overlap; each crop's size
matched its pixel range, each was byte-for-byte the same region of its
page, none had the whole page's dimensions, and all 81 checksums were
distinct. A contact sheet confirmed the pages: 1824 pp. 254-260,
Canestrini pp. 62-66, Giglio fol. 105r-107v. Every reader checked its own
crops and found each what its name says.

NM pass A, FG passes A and B and the Giglio read were dispatched together,
each confined to its own image, work and output folders and forbidden every
other path (D370). A first dispatch of NM pass A went out without its rules
and was stopped before it read or wrote anything; its folders were emptied
and it was dispatched again. NM pass B followed once pass A's page counts
showed no eligible sample page, in folders of its own. No output was
overwritten; each body matches its own witness.

`fazione` occurs in neither unit (D317, closed by D341; checked). Nor do
`ferro` (D433) or `fortezza` (D432): Canestrini's `ferro` on p. 62 is in
his note to the II.10 reply.

## NM-DISC.2.12 — 1824, pp. 254-260

1,371 words (both passes: p. 254 62, p. 255 258, p. 256 259, p. 257 260,
p. 258 271, p. 259 237, p. 260 24). Both passes find CAPITOLO XII on p.
254 below the end of II.11 (`... di quelli che si pigliano per la difesa
propria.`), the two-line italic rubric `S' egli è meglio, temendo di
essere assaltato, / inferire, o aspettare la guerra.`, a large initial I,
one printed block with no indents, no notes and no Latin, and the end at p.
260 l. 3 `si difenderà meglio.`, CAPITOLO XIII following on the same page.

**The sample (D302): none eligible.** A fifth of 1,371 is 274; the fullest
page, p. 258, holds 271. As at I.40 and I.58, pass B read the whole chapter
(D437, as D352, D391). Every word-level 1554 difference therefore has a
second 1824 reader by page.

**Result: identical.** The passes agree word for word, 1,371 to 1,371.
What remains is apostrophe spacing (`d' Italia` / `d'Italia`, `ne'
suoi`), two spaces before a comma and a semicolon that pass B normalised,
and specks (a raised dot between `possono` and `ad`, marks before `e`, after
`Re`, above `cose` and `forze`), all Class A. Pass A marks 5 loci and pass
B 10; none has a different word for alternative. Both read `ogni` over a
blotted n and `suo` over a broken u.

**`aspettase`** (p. 256 l. 25, .03): both readers see one s and say so,
pass A at enlargement. Not a form the 1824 uses (`aspettasse` four lines
above); the 1554 prints `aſpettaſſe`. Emended `aspetta[s]se` under D68, as
D381: **D438**.

**Against the 1554 (ruled by precedent).**

- D203(b), at e/o/a, each read by both 1824 readers without doubt:
  `ei non le torrebbe il Regno` / `non gli terrebbe` (.02); `ei mostrò`
  / `moſtra` (.02); `come i Romani, e come l'hanno` / `o come hanno` and
  `come l'avevano i Cartaginesi, e come` / `o come` (.05); `tu sei
  spacciato` / `ſpacciata` (.05); `quanto la guerra di casa` / `quanta`
  (.05); `uno esercito romano` / `Romana` (.06). The 1824 construes at
  each. Kept, D38, as D304, D393, D428: **D438**.
- Sense-bearing whole words, each read by both readers without doubt:
  `quella fonte, che mai le manca vita` (1554 `quella forza`; the 1824's
  `seccare quella fonte, come dice Annibale` in .04 answers its own
  reading); `e discostandoti arrischi tutta la fortuna` (the 1554 omits
  `discostandoti`, so the second member loses its condition); `combattere
  più facilmente` (the 1554 omits `più facilmente`); `i Re di Francia` (1554
  `il Re`); `longinque` / `lontane` and `propinque` / `vicine`; `sì
  discosto` / `di diſcoſto`; `se ne salverà` / `ſalueranno`; `inusitato
  alla guerra` / `della`; `Allegano gli Ateniesi` / `Allegane`; `e prima la
  Italia` / `prima l'Italia`; `restarono superiori; come` / `& come`; `ei
  non le torrebbe` / `non` (no subject); `in su i confini` / `in ſu
  confini`; `come l'hanno i Svizzeri` / `come hanno`; `ti appressi a loro`
  / `appreſsi loro`; `in la Magna` / `ne la`; `ch'egli` / `che eſsi`
  (twice); `Non si trova che per assaltare ... mandassero` / `Non ſi troua
  per aſſaltare ... che eſsi mandaſsino`. The 1824 construes at each.
  Kept, D38, as D394, D409, D420, D428, with translator's notes on `fonte`,
  `discostandoti` and `longinque`: **D438**.

Recorded as forms, without ruling: `nimico` / `nemico` throughout, `puoi`
/ `poi` (four times in .04, the 1554's spelling of the verb), `danaro` /
`danaio`, `contro` / `contra`, `li` / `gli`, `abbia` / `habbi`,
`sendo` / `eſſendo`, `ragioni da ogni` / `d'ogni`, `cinquantamila` /
`L milia`, `diciotto` / `XVIII`, `trenta o quarantamila` / `XXX o XL
mila`, `centomila` / `C mila`, `Massageti` / `Meſſageti`, `Tamiri` /
`Thamiri`, `Egizio` / `Egittio`. The rest is spelling (the comparison
record, D007).

**Rubric.** The 1824 rubric and the 1554 heading agree but for `inferire`,
where the 1554 reads `muouere`, "move [war]", and for spelling (`SE EGLIE
MEGLIO, TEMENdo di eſſer aſſaltato, muouere, o aſpettare la guerra. Cap.
XII.`). Canestrini's rubric over the reply agrees with the 1824 word for
word (D440).

## FG-CONS.2.12 — Canestrini, pp. 62-65

919 words (A 919, B 919: p. 62 41, p. 63 291, p. 64 276, p. 65 311). Both
passes find the heading **CONSIDERAZIONE SUL CAPITOLO XII** on p. 62 after
the end of the II.10 reply (`... nè la dannerà / in modo alcuno`), with no
`DEL LIBRO II` (the stop after XII doubtful to both); a two-line rubric in
smaller type, `S' egli è meglio, temendo di essere assaltato, inferire, / o
aspettare la guerra`, its stop doubtful to both; two indented paragraphs,
the second at p. 64 l. 5 `Resta la resoluzione`; the end at p. 65 l. 31
`rotti da lui in Spagna o in Africa`, no stop visible to either; and
CONSIDERAZIONE SUL CAPITOLO XIII, again without `del libro II`, opening p.
66. Canestrini's two notes, keyed after `Ferrando).` (p. 63) and `Paolo
Orsino` (p. 64), identify Ferdinand of Naples and Paolo Orsini; they are
his commentary and are not carried. `paragraph_divisions: witness` (D66).
Pass A marks 53 loci in the body, pass B 51; each 2 in the heading and
rubric.

**Body: one split.** p. 65 l. 21 `in luogo lont⟨o|a⟩no`: A prefers the
printed `lontono` and names `lontano`; B prefers `lontano` and says the
second a is printed like o. Both see the o. Not a form of the word; the
1933 edition reads `lontano`. Emended `lont[a]no` under D68, as D429:
**D439**.

**Doubtful to both, the alternatives words.**

| Locus | Pass A | Pass B | 1933 | Reading |
|---|---|---|---|---|
| p. 63 l. 9 `che ___` | ⟨entrate\|entrato⟩ | ⟨entrate\|entrato⟩ | `entrate` | `entrate`, as D398 |
| p. 64 l. 3 `sempre ___ diversione` | ⟨la\|lo⟩ | ⟨la\|lo⟩ | `la` | `la`, as D398 |
| p. 64 l. 6 `quando ___ inimico` | ⟨lo\|la⟩ | ⟨lo\|la⟩ | `lo` | `lo`, as D398 |
| p. 65 l. 5 `di tempo ___ di nuovi ordini` | ⟨e\|a⟩ | ⟨e\|a⟩ | `e` | `e`, as D398 |
| p. 64 l. 27 `Annibale a ___` | ⟨Canne\|Canno⟩ | ⟨Canne\|Canno⟩ | `Canne` | `Canne`, as D398 |
| p. 63 l. 16 `___ differenza` | ⟨È\|E⟩ | ⟨È\|E⟩ | `È` | `È`, as D398 (D114) |
| p. 64 l. 1 `con tutto ___ con parte` | ⟨a\|n⟩ | ⟨a\|o⟩ | `o` | **O44**: emended `[o]` (D442) |

At each of the first six both readers prefer the form that construes, and
the 1933 edition reads it: by precedent (**D439**). At the seventh both
readers take the broken sort, the first letter of p. 64, for an a, which
does not construe (`con tutto a con parte`); only `o` does, "with all or
with part", and the 1933 edition reads it. A letter doubtful to both whose
alternatives are words: put to David (O44), who ruled the recommendation,
`[o]` under D68, the printed form in the variant note (**D442**).

**Against the 1933 edition.**

- `quando lo inimico da chi tu tenti la guerra` (p. 64 l. 7): both readers
  read `tenti` without doubt; the 1933 edition reads `temi`. As printed the
  clause has no sense (war is not attempted *from* an enemy); the case is
  the one in which war is feared, as the rubric's `temendo` and the reply's
  own `quando io aspetto guerra da altri` have it. Put to David (O43), who
  ruled the recommendation: the whole word emended `[temi]` under D126, as
  `[comunicare]`, `tenti` in the variant note (**D441**). Not checked on
  the page image.
- `con tutto [o] con parte` (p. 63 l. 28): both read `tutto`; the 1933
  edition reads `tutte`. Canestrini construes ("with all or with part of
  his forces"). Kept, D38, as D400, D408 (**D439**).
- `sarebbono forse più facilmente stati` (p. 65 l. 29): the 1933 edition
  reads `forse molto più`. Both readers read no `molto`. Kept, D38
  (**D439**).

Every other difference is form, spelling or pointing both readers read
alike (`truovano` / `trovano`, `ragioni` / `ragione`, `considerazioni` /
`considerazione`, `il` / `el`, `potenza` / `potenzia`, `pari` / `pare`,
`degli` / `delli`, `fe` / `fe'`, `ribellioni` / `ribellione`, `dopo` /
`doppo`; the comparison record, D004).

**Pointing (D110, D40).** Where both readers doubt a mark, or split on its
weight, the 1933 edition breaks the tie; a mark both read alike stands.

| Locus | Pass A | Pass B | 1933 | Reading |
|---|---|---|---|---|
| `Autore ___ Perché` | ⟨.\|∅⟩ | ⟨.\|∅⟩ | `.` | `.` |
| `distinzione ___ o io` | ⟨:\|∅⟩ | ⟨:\|∅⟩ | `:` | `:` |
| `più oltre ___ o` | ⟨:\|.⟩ | ⟨.\|:⟩ | `:` | `:` |
| `fuora di casa ___ perché` | ⟨;\|,⟩ | `;` | `;` | `;` |
| `dello inimico ___ È ancora` | ⟨.\|∅⟩ | ⟨.\|∅⟩ | `.` | `.` |
| `il dire ___ io la porto` | ⟨:\|∅⟩ | ⟨:\|∅⟩ | `:` | `:` |
| `a casa sua ___ il dire` | ⟨;\|.⟩ | ⟨;\|.⟩ | `;` | `;` |
| `il dire ___ io esco` | ⟨:\|;⟩ | ⟨:\|;⟩ | `:` | `:` |
| `re Ferrando ___ .` | ⟨)\|∅⟩ | ⟨)\|'⟩ | `)` | `)` |
| `il dire ___ io comincio` | ⟨:\|∅⟩ | ⟨:\|∅⟩ | `:` | `:` |
| `a me ___ a dire` | ⟨;\|,⟩ | ⟨;\|,⟩ | `;` | `;` |
| `a dire ___ io ho già` | ⟨:\|∅⟩ | ⟨:\|∅⟩ | `:` | `:` |
| `in casa ___ ma per` | ⟨;\|,⟩ | `;` | `,` | `;`, read alike |
| `in sul suo ___ come fe` | ⟨,\|∅⟩ | ⟨∅\|,⟩ | `;` | `,` |
| `Visconti ___ E quanto` | ⟨.\|∅⟩ | ⟨.\|∅⟩ | `.` | `.` |
| `temporeggiando ___ E in questo` | ⟨.\|∅⟩ | ⟨.\|∅⟩ | `;` | `.`, the capital following |
| `degli inimici ___ Ma` | ⟨.\|∅⟩ | ⟨.\|∅⟩ | `.` | `.` |
| `di altri ___ dove` | ⟨;\|,⟩ | ⟨;\|,⟩ | `;` | `;` |
| `tuo Stato ___ perdendo` | ⟨,\|;⟩ | `,` | `;` | `,`, read alike |
| `a rifarti ___ dove` | ⟨;\|,⟩ | ⟨,\|;⟩ | `;` | `;` |
| `a Canne ___ come` | ⟨,\|∅⟩ | ⟨,\|∅⟩ | `,` | `,` |
| `lo Stato ___ Portando` | ⟨.\|∅⟩ | ⟨.\|∅⟩ | `.` | `.` |
| `in casa ___ il che` | ⟨;\|,⟩ | `;` | `,` | `;`, read alike |
| `e rifarti ___ E tanto` | ⟨.\|∅⟩ | ⟨.\|∅⟩ | `.` | `.` |
| `spazio di tempo ___ Veggo` | ⟨.\|∅⟩ | ⟨.\|∅⟩ | `.` | `.` |
| `a' Cartaginesi ___ e quando` | ⟨,\|;⟩ | ⟨,\|;⟩ | `;` | `;` |
| `l'avere fatto ___ Né` | ⟨.\|∅⟩ | ⟨.\|∅⟩ | `.` | `.` |
| `stati spacciati ___ perché` | ⟨;\|,⟩ | ⟨;\|,⟩ | `;` | `;` |
| `essere rotto ___ altrimenti` | ⟨;\|,⟩ | ⟨;\|,⟩ | `;` | `;` |
| `da Annibale ___ e' quali` | ⟨;\|,⟩ | ⟨;\|,⟩ | `;` | `;` |
| `in Africa ___` (unit end) | ⟨.\|∅⟩ | ⟨.\|∅⟩ | `.` | none, D40 |

`in sul suo ___ come fe`: pass A sees a comma, pass B a gap, the 1933
edition a semicolon; the lighter mark the scan shows is set. `alle
ribellioni ,` is read alike as a comma and kept against the 1933 `;`.

Class A (accents, the apostrophe of the apocopated article and pronoun,
Canestrini's thin space after the apostrophe, line-end hyphens) applied by
rule and not enumerated. Single-reader doubts are non-words or marks
(`aasai`, `cho`, `guorra`, `forzo`, `sonn`, `Stoto`, `sempra`, `sporaro`,
`c'`, `opportonità`, `qnando`): not findings.

## Headings and rubrics

**The 1824.** CAPITOLO XII and the italic rubric, as above.

**Canestrini's heading (O45).** Both readers read CONSIDERAZIONE SUL
CAPITOLO XII, without `del libro II`, and so for XIII on p. 66. D421 had
`build.py` add `del libro II` to every Book II reply, as Canestrini prints
it over II.10 and the proem's reply; this page does not. Put to David, who
ruled the recommendation: the column is headed as printed, through the
unit's `heading` front-matter, `Considerazione sul capitolo XII`; D421 is
narrowed so that each later Book II and III reply takes its heading from
its passes; II.10 and the proem stand (**D443**). `build.py` prints a
`heading` in front-matter in place of its default (`fg_heading()`), so no
code change is needed.

**Canestrini's rubric.** `S' egli è meglio, temendo di essere assaltato,
inferire, o aspettare la guerra`, word for word the 1824 rubric; the stop
doubtful to both and not set, as at II.10 (**D440**, as D430).

## Comparison witnesses

**Witness independence (SCOPE §7).** Neither FG pass carries a Palmarocchi
word-reading where Canestrini differs (list in the establishment record):
both have `tenti`, `tutto`, no `molto`, `truovano`, `ragioni`, `il`,
`potenza`. At the one split, pass B preferred the 1933 letter and recorded
the printed glyph: a preference for sense, not a reading of the other book.
The passes read Canestrini.

**NM, 1554 Giglio.** A third reader transcribed fol. 105r-107r cold
(`NM-DISC.2.12-1554.md`): 1,339 words, 23 doubtful loci, no damage and no
text lost, so D415 does not arise. No marginal inverted commas. The
transcript was collated by word against both passes.

**FG, 1933 edition.** The reply is on scan pages 57-59 (printed pp.
51-53), under CAPITOLO XII with the editor's bracketed rubric, after the
end of the II.10 reply; CAPITOLO XIII follows.

## To David

Three new establishment questions, put in one batch and ruled on the
recommendations: O43 `[temi]` (D441), O44 `[o]` (D442), O45 the heading
as printed (D443). Every other locus falls under an existing ruling and is
ruled by precedent: D437 (procedure), D438 (NM against the 1554, and
`aspetta[s]se`), D439 (FG body), D440 (rubrics).
