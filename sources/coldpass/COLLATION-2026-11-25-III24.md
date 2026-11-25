---
report: cold pass, pair III.24 (the twenty-seventh 1824 chapter under D199; D302 standing (D426, D457), the sample page p. 171 with three line crops)
units: [NM-DISC.3.24, FG-CONS.3.24]
passes: [NM A (subagent, full chapter, with p. 173 as boundary evidence), NM B (subagent, the sample page p. 171 and three line crops of pp. 170 and 172), FG A (subagent, full), FG B (subagent, full); each with its own image, work and output folders, forbidden every other path (D370)]
comparison_reads: [NM-DISC.3.24-1554 (subagent, Giglio 1554 page images only, own folders); 1933 edition pp. 64-65 (scan pages 70-71) read by the collator at the loci below]
performed: 2026-11-25 (passes, collation, rulings by precedent; one question put to David, O50)
rule: SCOPE §7, as revised by D199, D203 and D302 (standing, D426, D457)
method: difflib.SequenceMatcher over word tokens, after DEC-009 Class A on both sides (accents, ſ, elision spacing, line-end hyphens); marks compared as a second token stream; the 1554 compared by word after spelling normalisation (u/v, h, j, ſ, doubled consonants, tildes, &/et/ed, accents, elision and word division) and then read through by hand against its transcript to separate forms of one word from word-level differences; D203(b) letter classes tested on the result
disposition: NM pass A full, pass B the sample page with crops, agreeing word for word and mark for mark; the common doubt `⟨da|dà⟩ principio` read `da` (D508). The 1554's whole words, among them `allongato` and the omitted `fu` and `se`, not taken (D509). FG one paragraph, the passes identical in every word and mark once each doubt is resolved to the word it names; the common doubt `Pompeo ⟨e|o⟩ Crasso` read with the 1933; `o provincie`, `di Gallia` and the want of `che` kept against the 1933 (D38); `imperio decemvirale` against the 1933 `decennale`, kept provisionally (O50); pointing by D110 (D510). Rubrics and heading; Canestrini's note not carried (D511)
---

# Pair III.24 — cold passes and collation

Every image was cut from the rendered page in pixels and checked before any
reader saw it (D437): the 1824 pages at 350 ppi (2052 × 3228 px, native
351), the Canestrini pages at 1200 ppi (1367 × 2184 and 1367 × 2200 px;
native 601), the Giglio leaves at 500 ppi (1625 × 3209, 1639 × 3244 px).
Whole pages and thirds (Canestrini: halves) with a 4% overlap; each crop's
size matched its pixel range and each part was pixel-identical to its rows
of the page, checked before dispatch and again by every reader against its
manifest (16, 9, 9, 12 files, and 7 for pass B). The three line crops for
pass B were checked on a contact strip before dispatch: each holds its
whole line and nothing of its neighbours' letters.

**The extracts and the chapter's end.** The Canestrini extract (seven
pages from p. 78) holds the reply on pp. 78-79, a short rule below its
last line, and the half-title RICORDI POLITICI E CIVILI on the next page:
III.24 is the last reply, and nothing follows it in the *Considerazioni*.
Both readers had the half-title as boundary evidence. The Giglio extract
prints Cap. XXV on its third leaf. The 1824 extract, NM-DISC-III24-pages.pdf
(zero-based 173-175, pp. 170-172), ends with the chapter's last words,
`... nella servitù.`, at p. 172 l. 20, the rest of the page blank and no
following heading: the end could not be proved from it. The volume scan was
fetched again from its recorded URL; its sha256 matches the one recorded
(`db7f7e05...`), pp. 170-172 rendered from it are pixel-identical to the
extract, and p. 173 (zero-based 176) opens CAPITOLO XXV at its head. p. 173
was extracted as NM-DISC-III24-p173.pdf (sha256 `a860a558...`) and recorded
in the witness file, and pass A had it, as boundary evidence only (D508, as
D484, D492, D500). The chapter opens at p. 170 l. 15 under its heading,
below the end of III.23 (`... temerario e poco / prudente.`).

All four full readers were dispatched together; pass B followed once pass A
and the Giglio read were in and the sample page had been chosen. No output
was overwritten; each body matches its own witness.

`ferro` and `fortezza` occur in neither unit (D433; D312, D432; checked).
`fazione` occurs in neither unit (D317, D341; checked).

## NM-DISC.3.24 — 1824, pp. 170-172

471 words (p. 170 64, p. 171 249, p. 172 158). Pass A finds CAPITOLO XXIV on
p. 170 below the end of III.23, a one-line italic rubric ending `fece serva
Roma.` with a printed stop, a raised initial S, one printed block with no
indents and no notes, and the end at p. 172 l. 20 `nella servitù.`; on
p. 173 CAPITOLO XXV, its rubric `Della povertà di Cincinnato, e di molti
cittadini romani.`, and `Noi abbiamo ragionato altrove`.

**The sample (D302).** A fifth of 471 is 95; p. 171 and p. 172 are
eligible, p. 170 (64) is not. Word-level 1554 differences after spelling
normalisation: p. 170 one (`fattivi debiti` / `fattiui i debiti`); p. 171
two (`come fu L. Quinzio` / `come L. Quintio`, `prorogato` / `allongato`),
0.80 per hundred words; p. 172 one (`, se non venivano` / `, non
ueniuano`), 0.63. Chosen and recorded before dispatch: **p. 171**, with line
crops of p. 170 l. 7 (rows 2521-2598) and p. 172 l. 17 (rows 1619-1697),
the two differences outside it, and of p. 170 l. 6 (rows 2444-2521), where
pass A doubts `⟨da|dà⟩`, two words (D203(a)). Pass B was not told which
word.

**Result.** The sample page agrees with pass A in every word and every mark
(284 tokens to 284, words and marks), and all three crops agree word for
word. Pass B's doubts are specks (after `ai`, over `prudenza`, `venuto`,
under `si`), the weight of the comma after `deliberazione`, which pass A
reads without doubt, and the raised point after the last `Proconsolo`, which
both read as a stop. Both read `nuocè` and `arebbe` as printed without doubt.
D302 stands.

**The common doubt.** `conosciute bene ⟨da|dà⟩ principio` (p. 170 l. 6):
both readers see a round dot over the `a`, not an accent, and prefer `da`;
only `da` construes, `da principio`, from the beginning, and the 1554
prints `da principio`. Read `da`, as D398 (a common doubt where only one
word construes), and by D203(a), the doubt having had its second reader on
the crop (**D508**).

**Against the 1554 (ruled by precedent).** The sense-bearing whole words,
each read by pass A and, on the sample or a crop, by pass B, without doubt:

- `e fattivi debiti rimedj` (.01) / `et fattiui i debiti rimedij`: the 1554
  has the article;
- `come fu L. Quinzio` (.02) / `come L. Quintio`: the 1554 omits the verb;
- `Il primo a chi fu prorogato l'Imperio` (.04) / `a chi fu allongato
  l'imperio`: two verbs, prorogued against lengthened; the 1824's
  `prorogato` is the chapter's other verb beside `prolungare`;
- `Che se mai i Romani non avessero prolungati li Magistrati e gl'Imperj,
  se non venivano sì tosto a tanta potenza` (.06) / `... et gli imperii,
  non ueniuano ſi toſto`: the 1554 has no second `se`, so that `non
  venivano` is the apodosis (they would not have come so soon to such
  power); in the 1824 the `se` makes it a second protasis and the period
  runs on to `sarebbero`. Both construe.

No difference falls at the D203(b) letter classes. The 1824 construes at
each; kept, D38, as D428, D438, D449, D459, D469, D477, D485, D493, D501,
with a translator's note at the last (**D509**).

Recorded as forms, without ruling: `Repubblica`, `Rep.` / `Rep.`
(abbreviated twice), `risoluzione` / `reſolutione`, `contenzioni` /
`cõtentioni`, `degl'Imperj` / `de gli imperij`, `fussero`, `fusse` /
`fuſsino`, `fuſſe`, `vivere` / `uiuer`, `per avventura` / `perauentura`,
`nuocè` / `nuoce`, `autorità` / `auttorita`, `presero` / `preſono`,
`Quinzio` / `Quintio`, `del quale` / `delquale`, `esempio` / `eſſempio`,
`ed` / `et`, `dei Nobili` / `de nobili`, `di spegnerli` / `de ſpengerli`,
`volevano` / `uoleuan`, `di accrescerli` / `d'accreſcerli`, `tutt'i` /
`tutti i`, `arebbe` / `harebbe`, `Filone` / `Philone`, `dal Senato` / `da
il Senato` (the Giglio reader's doubt `⟨da il|dal⟩`), `discostarono` /
`diſcoſtaron`, `le armi` / `l'armi`, `quello Capo` / `quel capo`, `contro` /
`contra`, `li seguitassero` / `gli ſeguitaſſino`, `potette` / `potè`, `li
Magistrati` / `i magiſtrati`, `uomini` / `huomini`. The Giglio reader's
doubts (line-end hyphens, `fuſſe`/`fuſſi`, tildes, the worn sorts of
189r) fall at loci the 1824 readers read alike without doubt or at forms.
The leaves are sound: show-through and worn sorts, no tear or loss, every
word of the chapter legible (D415 not needed).

**Foliation.** The Giglio reader reads the recto's folio number as 189
(3 the alternative) and so foliates the chapter 188v-189v; the acquisition
record, from the full scan's sequence, gives fol. 187v-188v; to the
collator the printed figure reads 183 or 188, a worn third digit. The
acquisition record's foliation is kept; nothing textual turns on it.

**Rubric.** The 1554 sets the title as its heading, `LA PROLVNGATIONE DE GLI
imperij fece ſerua Roma. Cap. XXIIII.`: the same sentence but for spelling.
The 1824 rubric is read by pass A without doubt, with its stop (**D511**).

**`nuocè`.** Both readers read the grave accent clearly printed on
`nuocè` (p. 171 l. 3). The accented form is a past, `nocé`, `nocque`, as
the sequence `presero` requires; the accent is set acute by DEC-009 clause 1
(`nuocé`), and the English takes the past, with a translator's note.

## FG-CONS.3.24 — Canestrini, pp. 78-79

318 words each (p. 78 202, p. 79 116). Both passes find the heading
**CONSIDERAZIONE SUL CAPITOLO XXIV** at the head of p. 78 below the running
head, set in capitals and small capitals, **without** `del libro III`, with
a faint trace after XXIV that both readers doubt as a stop; a one-line
rubric in smaller roman type, `La prolungazione degl' imperii fece serva
Roma.`, with a printed stop seen by both; **one** paragraph, indented at
p. 78 l. 1 (about 60 px), with no other indent; the end at p. 79 l. 12 `nè
facultà di travagliarla per altra via.`; a short rule; and the half-title
RICORDI POLITICI E CIVILI on the next page. `paragraph_divisions: witness`
(D66). Pass A marks 41 loci in the heading, rubric, body and note, pass B 35.

**Canestrini's note.** One, keyed to this reply: (1) on p. 78, called after
`tirannidi.`, summarising Machiavelli's two causes and the two
inconveniences; read alike by both, but for broken letters and the faint
pointing of a note. His gloss; not carried (D463, D487, D495, D503). Pages
79 and 80 carry no note (**D511**).

**The readers' doubts.** Both readers, at a letter the scan has broken,
gave the word as the preferred reading and the shape as the alternative:
`imperii`|`imperu`, `uomini`|`nomini`, `tirannidi`|`tirauuidi`,
`Catilina`|`Catihna`, `Cesare`|`Ceaare`|`Cosare`, `utilità`|`utihtà`,
`sua`|`aua`, `stato`|`atato`, `nobilità`|`nobihtà`, `e`|`c` ×2,
`si`|`st`, `nè`|`nc̀`, and the rubric's `imperii`|`imperil`, `fece`|`feco`.
At every such locus only the word is Italian and the 1933 edition prints it:
readings, the word, as D398, D406, D494, D502 (**D510**).

**The common doubts.** Two are between words:

- `e nelle nazioni o provincie forestiere, ⟨e|s⟩ (A) / ⟨e|o⟩ (B) a'
  capitani accresceva` (p. 78 l. 4): both prefer `e`; A's alternative is
  not a word; the 1933 prints `ed a' capitani`. Read `e`, the reading
  of both (D398).
- `con Pompeo ⟨e|o⟩ Crasso` (p. 78 l. 19): both prefer `e`, both naming
  `o`; pass A sees the shape as `o`. Only `e` gives the conspiracy of the
  three; `o` construes only weakly. The 1933 prints `e`. Read `e`, with the
  1933, as D486 (`casi e in molti tempi`, a common doubt with the 1933),
  D215, D234, D406 (**D510**).

**Against the 1933 (ruled by precedent).** Each read alike by both readers
without doubt:

- `e nelle nazioni o provincie forestiere` (.01) / 1933 `e nelle nazione e
  provincie forestiere`: `o` against `e`, at the D203(b) e/o class,
  escalated by that rule and ruled as D486 (`o a ogni principe`, both
  without doubt, kept against the 1933 `ed`): kept, D38; "or" and "and"
  differ little where nations and provinces are one class;
- `il lungo imperio di Gallia` (.01) / 1933 `in Gallia`: the command of
  Gaul against the command in Gaul; both construe; kept, D38;
- `Però conchiuggo che quando Roma non fu corrotta, le prorogazioni` (.01)
  / 1933 `che quando Roma non fu corrotta, che le prorogazione`: the 1933
  repeats `che` after the clause; Canestrini's construes without it; kept,
  D38.

Kept, D38 (as D400, D408, D450, D486, D502); variant notes (**D510**).

**Not covered by a precedent: `decemvirale`.** `ma la conjurazione con
Pompeo e Crasso di occupare la republica, fece imperio decemvirale` (p. 78
l. 20): both readers read `decemvirale` without doubt; the 1933 prints
`decennale`. Caesar's command in Gaul was given for five years and extended
for five more (the editor's reference): ten years, `decennale`.
`decemvirale`, of the decemvirs, is a real word and construes in the
syntax, but makes Caesar's command "decemviral", which no source supports,
and it differs from `decennale` by a few letters a compositor or an editor
reading a manuscript could exchange. D38 keeps a weaker reading that
construes; D126 brackets a real word that cannot be construed in its
place. Which governs here, a word that construes in grammar and fails in
fact, is not settled by any precedent: **O50**, with the recommendation
`decemvirale` kept under D38, the 1933 `decennale` in the variant note and
a translator's note giving the ten-year sense; applied provisionally. An
image check would add nothing, both readers having read the word without
doubt.

**Witness independence (SCOPE §7).** Neither pass carries a 1933
word-reading where Canestrini differs: both have `imperii` ×7, `nazioni o
provincie`, `e a'`, `il lungo`, `di Gallia`, `il fondamento`, `divisioni`,
`tirannidi` ×2, `populi`, `conjurazione` ×2, `decemvirale`, `e avendo`,
`le prorogazioni` (no `che`), `usorono`, `e i semi`, `prorogazioni`,
against the 1933 `imperi`, `nazione e provincie`, `ed a'`, `el lungo`, `in
Gallia`, `el fondamento`, `divisione`, `tirannide`, `popoli`,
`coniurazione`, `decennale`, `ed avendo`, `che le prorogazione`,
`usarono`, `ed e' semi`, `prorogazione`. The passes read Canestrini.

**Pointing (D110).** The stops after `Gallia` (p. 78 l. 6) and `capo`
(p. 79 l. 3), each before a capital, both readers seeing a faint mark and
preferring a stop: read with the 1933, which prints both. `altri;` (p. 78
l. 16), doubted by A (`⟨;|,⟩`) and read by B without doubt, kept, against
the 1933 `altri,`. The heading's faint trace after XXIV, doubted by both:
the 1933 heading prints none, so the lighter reading, none (D110, as D503).
Marks read alike by both kept against the 1933 (`la quale datasi`,
`imperii, come`, `plebe, e avendo`, `civili, e i semi`). Canestrini's
printed stop at the end, seen by both, kept (D460) (**D510**).

**The plural article.** Canestrini prints `e cittadini e' soldati` (p. 78
l. 12): the bare `e` is the article, answered by the printed `e'`, the
two nouns in asyndeton, as the 1933 sets them (`e' cittadini, e'
soldati`); set `e' cittadini` by D35 (DEC-009 Class A), as `e' Germani`
(D502). `séguito`, the noun (a following), with the accent both readers
see, as `ség[u]ito` at FG I.29.

**Heading and rubric.** The heading as printed, without `del libro III`
and without the stop (D443, D110), in the unit's `heading` front-matter.
The rubric agrees with the 1824 rubric but for `degl'imperii` against
`degli Imperj`, two forms of one word; Canestrini's form carried, with the
stop both readers see in it, as his rubrics are carried where a stop is
printed; the readers' doubts in it (`imperii`|`imperil`, `fece`|`feco`)
are broken letters, read with the 1824 rubric (**D511**, as D463, D479,
D487, D495, D503). The 1933 sets the 1824's sentence, with `degl'imperi`,
as a bracketed title.

## Normalisation classes

Accents (`perchè`, `benchè`, `talchè`, `nè` set acute; `nuocè` set
`nuocé`); elision and apocope spacing; the Florentine plural article
apostrophe (D35); spaces before punctuation; line-end hyphens; the note
call.
