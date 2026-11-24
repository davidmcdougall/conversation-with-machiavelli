---
report: cold pass, pair III.17 (the twenty-fifth 1824 chapter under D199; D302 standing (D426, D457), the sample page p. 148 with two line crops)
units: [NM-DISC.3.17, FG-CONS.3.17]
passes: [NM A (subagent, full chapter), NM B (subagent, the sample page p. 148 and two line crops of p. 149), FG A (subagent, full), FG B (subagent, full); each with its own image, work and output folders, forbidden every other path (D370)]
comparison_reads: [NM-DISC.3.17-1554 (subagent, Giglio 1554 page images only, own folders); 1933 edition pp. 61-62 (scan pages 67-68) read by the collator at the loci below]
performed: 2026-11-24 (passes, collation, rulings by precedent; no question put to David)
rule: SCOPE §7, as revised by D199, D203 and D302 (standing, D426, D457)
method: difflib.SequenceMatcher over word tokens, after DEC-009 Class A on both sides (accents, ſ, elision spacing, line-end hyphens); marks compared as a second token stream; the 1554 compared by word after spelling normalisation (u/v, h, j, ſ, doubled consonants, tildes, &/et/ed, ꝑ, accents, elision and word division) and then read through by hand against its transcript to separate forms of one word from word-level differences; D203(b) letter classes tested on the result
disposition: NM pass A full, pass B the sample page with crops, agreeing word for word (D492); the 1554's whole words, its omissions and its order not taken (D493). FG one paragraph, the passes identical once each doubt is resolved to the word it names, the common `⟨suo|sue⟩` read with the 1933, `pensiero.` supplied (D494). Rubrics and heading; Canestrini's note not carried (D495). No new establishment question
---

# Pair III.17 — cold passes and collation

The first Book III chapter. Every image was cut from the rendered page in
pixels and checked before any reader saw it (D437): the 1824 pages at 350
ppi (2052 × 3228 px, native 351), the Canestrini pages at 1200 ppi (1367 ×
2184 px; native 600), the Giglio leaves at 500 ppi (1625 × 3209, 1639 ×
3244 px). Whole pages and thirds (Canestrini: halves) with a 4% overlap;
each crop's size matched its pixel range, and the checksums within each
reader's folder were distinct (12, 6, 6, 8, and 6 for pass B). Every reader
checked its own images against the manifest and found each what its name
says. The two line crops for pass B were checked on a contact strip before
dispatch: each holds its whole line and nothing of its neighbours'
letters.

**The extracts and the chapter's end.** Each extract was checked to reach
the chapter's end before any reader was sent. The Canestrini extract
(pp. 74-75) and the Giglio extract (fol. 178v-179r) each print the next
heading (CONSIDERAZIONE SUL CAPITOLO XIX; Cap. XVIII). The 1824 extract,
NM-DISC-III17-pages.pdf (zero-based pages 151-152, pp. 148-149), ends at
the foot of p. 149 with `la sua rovina.`, with no following heading on the
page, so the end could not be proved from it. The volume scan was fetched
again from its recorded URL; its sha256 matches the one recorded
(`db7f7e05...`), pp. 148-149 rendered from it are pixel-identical to the
extract, and p. 150 (zero-based 153) opens CAPITOLO XVIII at its head. p. 150
was extracted as NM-DISC-III17-p150.pdf (sha256 `36836954...`) and recorded
in the witness file, and pass A had it, as boundary evidence only (D492,
as D484). The chapter opens at the head of p. 148 under its heading; the
end of III.16 is on p. 147, which no reader needed.

All four full readers were dispatched together; pass B followed once pass A
and the Giglio read were in and the sample page had been chosen. No output
was overwritten; each body matches its own witness.

`fazione`, `ferro` and `fortezza` occur in neither unit (D317, closed by
D341; D433; D312, D432; checked).

## NM-DISC.3.17 — 1824, pp. 148-149

347 words (p. 148 187, p. 149 160). Pass A finds CAPITOLO XVII at the head of
p. 148, a three-line italic rubric ending `d' im- / portanza.` with a
printed stop, an enlarged initial D, one printed block with no indents and
no notes, and the end at p. 149 l. 20 `la sua rovina.`; on p. 150 CAPITOLO
XVIII, its rubric `Nessuna cosa è più degna d' un Capitano, che presentire
i partiti del nimico.`, and `Diceva Epaminonda tebano`.

**The sample (D302).** A fifth of 347 is 70; both pages are eligible.
Word-level 1554 differences after spelling normalisation: p. 148 four
(`fu da Asdrubale` / `fu Asdrubale`, `bisognava` / `biſogna`, `che lui
aveva` / `che haueua`, `inonestamente` / `dishoneſtamente`), 2.1 per
hundred words; p. 149 two (`tali offese` / `tale offeſe`, `era ancora` /
`anchora era`), 1.25. Chosen and recorded before dispatch: **p. 148**, with
line crops of p. 149 l. 11 (rows 1160-1246) and l. 13 (rows 1312-1394), the
two differences outside it. Pass A has no doubt between words, so no
further crop (D203(a)). Pass B was not told which word.

**Result.** The sample page agrees with pass A in every word and every
mark, heading and rubric included (187 words to 187), and both crops agree
word for word. Pass B's three doubts are worn sorts on p. 148: `⟨cd|ed⟩`
twice (ll. 10, 17) and `⟨nuovc|nuove⟩` (l. 23), a bowl with no bar; pass B
prefers the shape and names the word, pass A reads `ed`, `ed`, `nuove`
without doubt, the 1554 prints `et`, `et`, `nuoue`, and only the word is
Italian. A doubt of one reader at a damaged sort that the other reads and
the 1554 confirms is not a disagreement (D457, D468). Pass A's three doubts
are the space after two apostrophes (`l' aveva`, `s' aveva`) and a dark
point in the word space before `offese` (p. 149 l. 11), which pass B, on
the crop, describes alike and also prefers as a stray mark: no reading
turns on it, and it is not carried. D302 stands (**D492**).

**Against the 1554 (ruled by precedent).** The sense-bearing whole words,
each read by pass A and, on the sample or a crop, by pass B, without doubt:

- `fu da Asdrubale astutamente tanto intrattenuto` (.02) / `fu Aſdrubale
  aſtutamente`: the 1554 omits `da`, so that Hasdrubal, not Nero, is the
  one held in talk;
- `con lo esercito che bisognava` (.02) / `che biſogna`: the 1824's past
  against the 1554's present;
- `che lui aveva a fronte ad Annibale` (.02) / `che haueua`: the 1554 omits
  the pronoun;
- `inonestamente` (.02) / `dishoneſtamente`: two adverbs of one sense, the
  1824's with the negative `in-`;
- `era ancora incorrotta` (.03) / `anchora era`: order;
- `di tali offese` (.03) / `di tale offeſe`: the 1554's singular does not
  agree with `offeſe`.

No difference falls at the D203(b) letter classes. The 1824 construes at
each; kept, D38, as D428, D438, D449, D459, D469, D477, D485, with a
translator's note where the sense moves (`da`): **D493**.

Recorded as forms, without ruling: `dallo esercito` / `dall'eſſercito`,
`d'accordo` / `di accordo`, `per l'addietro` / `ꝑ lo adietro`,
`congiungesse` / `congiugeſſe`, `egli uscì` / `gli uſci`, `gli dette` /
`li dette`, `disonore` / `dishonore`, `sendo` / `eſſendo`, `vennero` /
`uennono`, `qual cagione` / `quale`, `giuocata` / `giocata`,
`riacquistava` / `racquiſtaua`, `contro a` / `contra a`, `lo avevano` /
`l'haueuano`, `romano` / `Ro.`, `quelli tempi` / `quei tempi`, `possano` /
`poſsino`, `com'era` / `come era`, `gli è` / `egliè`, `Repubblica` /
`Rep.`. The Giglio reader's doubts (the mark after `amminiſtratione` in the
heading, faint hyphens at `s'e|ra` and `d'Aſdru|bale`, `⟨li|lì⟩`,
`⟨et|e:⟩`, a point after `ſi`) fall at loci the 1824 readers read alike
without doubt. The leaves are sound: fol. 178v has lost its folio number,
with gutter shadow, show-through and worn type, every word of the chapter
legible (D415 not needed).

**Rubric.** The 1554 sets the title as its heading, `CHE NON SI OFFENDA
VNO ET poi quel medeſimo ſi mãdi in amminiſtratione, et gouerno
d'importanza. Cap. XVII.`: the same sentence but for spelling and a comma.
The 1824 rubric is read alike by both 1824 readers without doubt, with its
stop (**D495**).

## FG-CONS.3.17 — Canestrini, pp. 74-75

330 words each (p. 74 183, p. 75 147). Both passes find the heading
**CONSIDERAZIONE SUL CAPITOLO XVII DEL LIBRO III.** on p. 74 below the end
of the II.24 reply (`non le smurorono.`), set in capitals and small
capitals with `del libro III` and a printed stop that both see clearly; a
two-line rubric in smaller roman type, `Che non si offenda uno, e poi quel
medesimo si mandi in amministrazione / e governo d' importanza`, with no
stop; one paragraph, indented at p. 74 l. 1 (about 58 px), with no other
indent; the end at p. 75 l. 15 `volerla sollecitare.`; and CONSIDERAZIONE
SUL CAPITOLO XIX following on p. 75 (`La severità, nuda di ogni`).
Canestrini prints no reply to III.18. `paragraph_divisions: witness`
(D66). Pass A marks 41 loci (37 in the body), pass B 36 (33 in the body).

**Canestrini's note.** One, keyed to this reply: (1) on p. 75, called
after `Salinatore,`, identifying him as Marcus Livius Salinator, consul
with Claudius Nero; read alike by both, but for broken letters. His
historical gloss; not carried (D463, D487). The person is identified in the
edition's own commentary and a translator's note (**D495**).

**The readers' preferences.** Both readers, at a letter the scan has
broken, gave the shape as the preferred reading and the word as the
alternative, so that the doubt marks a damaged sort, not two words: pass A
`lia`, `particularo`, `u`, `tntte`, `repnblica`, `meravigha`, `ostina-
tamento`, `c`, `Asdruhale`; pass B `n`, `repablica`, `sin`, `cra`; both
`inginria`, `aue`, `chn`, `qnesto`, `easere`, `talo`, `ignominta`,
`risentisai`, `adegno`, `natnre`, `banno`, `gh`, `cho`, `archbe`,
`consnle`. Where one reader prefers the shape, the other reads the word,
mostly without doubt. At every such locus only the word is Italian and the
1933 edition prints it (`ha`, `particulare`, `a tutte`, `republica`, `sia`,
`era`, `ostinatamente`, `ed andò`, `Asdrubale`, `ingiuria`, `sue`, `che`,
`questo`, `essere`, `tale ignominia`, `risentissi`, `sdegno`, `nature`,
`hanno gli`, `arebbe`, `consule`): readings, the word, as D398, D406
(**D494**). The token streams are then identical, 330 to 330.

**Common doubt between words.** `e lo mostrano le azioni ⟨suo|sue⟩ prima`
(p. 75 l. 9): both prefer `suo`, both naming `sue`, the scan's o/e. Only
`sue` agrees with `azioni`; the 1933 edition reads `le azione sue`. A
reading, with the 1933, as D303 and D398 settle a common doubt by the
comparison witness (**D494**).

**Witness independence (SCOPE §7).** Neither pass carries a 1933
word-reading where Canestrini differs: both have `populo`, `il quale` ×2,
`Il quale`, `e anche`, `e a sè proprio`, `e andò`, `meraviglia`, `azioni`,
`fece il possibile`, `doppo il consulato`, `Il che`, `vendicarsi, di poi`,
against the 1933 `popolo`, `el quale`, `El quale`, `ed anche`, `ed a sé
proprio`, `ed andò`, `maraviglia`, `azione`, `fece el`, `doppo el`, `il
che`, `vendicarsi; di poi`. The passes read Canestrini. No word-level
difference from the 1933 falls at the D203(b) letter classes; `azioni` /
`azione`, `meraviglia` / `maraviglia`, `populo` / `popolo` are forms of one
word.

**Pointing (D110).** With the 1933 where both see a mark and weigh it
differently or split: `republica,` (p. 74 l. 2; A `,`, B `⟨;|,⟩`; 1933
`,`), `vendicarsi.`, `medesimo;`, `principe.`, `altrimenti;`. At `patria⟨.|,⟩
fa male` (both preferring the stop), where the 1933 prints no mark, the
lighter of the two read, `,`. The stop after `pensiero` (p. 74 l. 13),
doubted by both with no mark preferred, before the capital of `Però`,
supplied from the 1933 (C001, D67). Marks read alike by both are kept
against the 1933 (`republica;` at l. 12, `ingiuriato,`, `rispetto,`,
`Discorso,`, `rotto,`, `parole,`, `cittadini.`, `vendicarsi,`). Canestrini's
printed stop at the end, seen by both, kept (D460) (**D494**).

**Heading and rubric.** The heading as printed, with `del libro III` and
its stop, in the unit's `heading` front-matter (D443). The rubric agrees
with the 1824 rubric word for word; pass A's doubts in it (`⟨in|m⟩`,
`⟨amministrazione|amminislrazione⟩`) are broken letters, read with the
1824 rubric and pass B; no stop, as Canestrini's rubrics are carried
(**D495**, as D463, D479, D487). The 1933 sets the same sentence as a
bracketed title.

## Normalisation classes

Accents; elision and apocope spacing, and two elisions with no apostrophe
printed (`s ha`, `l ha`, both readers), set `s'ha`, `l'ha`; the
Florentine plural article apostrophe; spaces before punctuation; line-end
hyphens; the note call.
