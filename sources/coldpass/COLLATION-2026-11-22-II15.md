---
report: cold pass, pair II.15 (the twenty-second 1824 chapter under D199; sampled under D302, standing (D426, D457))
units: [NM-DISC.2.15, FG-CONS.2.15]
passes: [NM A (subagent, full chapter), NM B-sample (subagent, p. 266 and ten line crops of pp. 264, 265, 267, 268), FG A (subagent, full), FG B (subagent, full); each with its own image, work and output folders, forbidden every other path (D370)]
comparison_reads: [NM-DISC.2.15-1554 (subagent, Giglio 1554 page images only, own folders); 1933 edition pp. 55-56 (scan pages 61-62) read by the collator at the loci below]
performed: 2026-11-22 (passes, collation, rulings by precedent; one question, O48, put to David)
rule: SCOPE §7, as revised by D199, D203 and D302 (standing, D426, D457)
method: difflib.SequenceMatcher over word tokens, after DEC-009 Class A on both sides; 1554 compared by word after spelling normalisation (u/v, h, j, ſ, doubled consonants, ti/zi, tildes, &/et/ed, accents, elision and word division), then read through by hand to separate forms of one word from word-level differences; D203(b) letter classes tested on the 1554 word diff
disposition: NM sample and crops agree with pass A word for word; the 1554's whole words and its Italian rendering of Livy not taken (D468, D469). FG one paragraph, the passes identical in every token; pointing by D110; the printed terminal stop kept; Canestrini's note not carried (D470). Rubrics and heading (D471); the 1824 rubric's `fieno`, doubtful to both 1824 readers against the 1554's `ſieno`, put to David as O48, `fieno` applied provisionally
---

# Pair II.15 — cold passes and collation

Every image was cut from the rendered page in pixels and checked before any
reader saw it (D437): the 1824 pages at 350 ppi (2057 × 3228 px, native),
the Canestrini pages at 1200 ppi (1367 × 2184 px; native 600), the Giglio
leaves at 500 ppi (1639 × 3244, 1625 × 3209 px). Whole pages and thirds
(Canestrini: halves) with a 4% overlap; each crop's size matched its pixel
range, none had its page's dimensions, and the checksums within each
reader's folder were distinct (24, 6, 6, 20; the sample reader 14, its ten
line crops cut at the gaps between printed lines found by a row profile
and checked by eye on a contact strip before dispatch, two of which were
recut one line lower after that check). The 1824 extract's first page is
II.14's last (identical checksum), as is the Giglio fol. 109r. Every reader
checked its own crops against the manifest and found each what its name
says.

NM pass A, FG passes A and B and the Giglio read were dispatched together.
NM pass B followed once pass A and the Giglio read were in and the sample
page was chosen. No output was overwritten; each body matches its own
witness.

`fazione` occurs in neither unit (D317, closed by D341; checked). Nor do
`ferro` or `fortezza`.

## NM-DISC.2.15 — 1824, pp. 264-268

909 words (pass A: p. 264 95, p. 265 228, p. 266 250, p. 267 254, p. 268
82). Pass A finds CAPITOLO XV on p. 264 below the end of II.14 (`fia sempre
partito prudente.`), the two-line italic rubric `Gli Stati deboli sempre
fieno ambigui nel risolversi, / e sempre le deliberazioni lente sono
nocive.`, an enlarged initial I, one printed block with no indents and no
notes, the Latin of Annius' speech in italic (p. 265 ll. 9-13), and the
end at p. 268 l. 11 `stra notata.`, CAPITOLO XVI following on the same
page.

**The sample (D302).** A fifth of 909 is 182: pp. 265, 266 and 267 are
eligible, p. 264 (95) and p. 268 (82) not. Word-level differences from the
1554, after spelling normalisation: p. 264 none; p. 265 three (`di questa
disputa` / `in`, the Italian rendering added after the Latin, `con la
lentezza` / `con lentezza`); p. 266 seven (`procedono` / `procedano`, `o
adempire` / `e`, `foga` / `fuga`, `mai impediranno` / `mai non`, `i
Siracusani` / `in Siracusani`, `ma che era` / `ma era`, `i Lavinj` / `i
Latini`); p. 267 two (`accordarono` / `s'accordarono`, `causa` /
`cagione`); p. 268 three (`molti più segni` / `piu segni`, `alle
Repubbliche` / `alla Republica`, `replicarne` / `replicare`). p. 266 is the
densest per word (7 in 250, against 3 in 228 and 2 in 254) and was chosen
and recorded before it went out, with ten line crops: the eight 1554
differences outside it (p. 265 ll. 8, 13, 30; p. 267 ll. 17-18, 30; p. 268
ll. 3, 6, 9) and pass A's one doubt between words, the rubric's `⟨fieno|
sieno⟩` (p. 264 l. 15), where the 1554 also differs (D203(a)).

**Result.** The sample agrees with pass A word for word (248 tokens to
248), with no doubt on the page. Each crop reads its line as pass A does.
Two crops carry doubts: crop a, the rubric, `⟨fieno|sieno⟩`, the same doubt
and the same preference as pass A (O48 below); crop g, `dere ⟨lo|le⟩
Stato`, where pass A records the same damaged o (an internal stroke) and
reads `lo` without doubt, the 1554 prints `lo ſtato`, and only `lo`
construes: a doubt of one reader at a damaged sort, settled by sense and
the 1554 as D457 rules, not a disagreement. Clean (**D468**). D302 stands.

What remains is the space in `ch' egli`, `ch' erano`, `all' arme`, `l'
animo`, `l' amicizia` (elision, Class A) and the comma after `il Re` (p.
268 l. 5), which pass A doubts against a stop before the capital `E`: the
1554 prints `Re.Et`; read as a stop, as D67 supplies the stops the
impression lacks.

**Against the 1554 (ruled by precedent).** At the D203(b) letter classes:
`procedono` / `procedano` (o/a), `o adempire` / `e adempire` (o/e), `foga` /
`fuga` (o/u), all on the sample page and read by both 1824 readers without
doubt; the 1824 construes at each (`foga`, a popular rush, against `fuga`,
a flight), as D428, D438. The sense-bearing whole words, each read by both
1824 readers (sample page or crop) without doubt: `nel consiglio di questa
disputa` / `in questa` (.01); `con la lentezza loro` / `con lentezza` (.03);
`mai impediranno` / `mai non impediranno` (.03, the same sense); `vennero i
Siracusani` / `uennono in Siracuſani` (.04); `ma che era ben da detestare` /
`ma era bene` (.04); `sendo i Lavinj` / `eſſendo i Latini` (.05: the 1554
has the Latins sought for aid by themselves; Livy's people are the
Lanuvini, and Guicciardini names them `Lavinii`); `accordarono` /
`s'accordarono` (.06); `per simile causa` / `per ſimile cagione` (.06);
`mostri molti più segni` / `moſtri piu ſegni` (.06); `alle Repubbliche` /
`alla Republica` (.07); `replicarne` / `replicare` (.07). After the Latin the
1554 again adds an Italian rendering (`Cioè,la ſomma de le coſe noſtre ...
accommodar le parole alle coſe.`), which the 1824 does not print. The 1824
construes at each. Kept, D38, as D428, D438, D449, D459, with translator's
notes on `foga`, `Lavinj`, `o adempire` and `alle Repubbliche`: **D469**.

Recorded as forms, without ruling: `fecero` / `feciono` ×2, `allo
individuo` / `a l'individuo`, `quelli` / `quei`, `coscienza` /
`conſcienza`, `contro` / `contra` ×5, `de' Romani` / `di Romani`, `ch'egli`
/ `che egli`, `Principe` / `Prencipe`, `Repubblica` / `Rep.`, `abbiano` /
`habbino`, `massime` / `maſsimamente` ×3, `ajuta` / `aiuta`, `passione` /
`paſsion`, `lasciano` / `laſciono`, `veggano` / `uegghino`, `ardor` /
`ardore`, `alcun` / `alcuno`, `dei` / `de`, `opinione` / `oppenione`, `ai` /
`a i` ×2, `fuori` / `fuora`, `Donde` / `Onde`, `romano` / `Ro.`, `di
ajutare` / `d'aiutare`, `ajutandoli` / `aiutandogli`, `l'ajuto` / `lo
aiuto`, `l'aggiunta` / `la aggiunta`, `avessero` / `haueſsino`, `con i` /
`co i`, `Francesi` / `Francioſi`, `ebbero` / `hebbono`, `Lodovico` /
`Ludouico` ×2, `ch'egli stessero` / `che gli ſteſsino`, `intantochè` /
`intanto, che`, `sendo` / `eſſendo` ×2, `in su` / `inſu`, `nella amicizia`
/ `nell'amicitia`, `di sopra` / `diſopra`, `uno altro` / `un'altro`, `uno
nuovo` / `un nuouo`, `essere` / `eſſer`; in the Latin `accomodare` /
`accommodare`. The 1554's own misprints (`cofe`, `ſarli`, `molte molte`)
and its reader's doubts between words are in the 1554 only. The 1554
leaves are undamaged but for three small stains, each word legible (D415
not needed).

**Rubric.** The 1554 sets the title as its heading, `GLI STATI DEBBOLI
SEMPRE ſieno ambigui nel riſoluerſi,et ſempre le deliberationi lente ſono
nociue. Ca. XV.` At the one word that differs, both 1824 readers doubt the
first letter of `⟨fieno|sieno⟩`, an italic ligature whose crossbar neither
can see, and both prefer `fieno`. The alternatives are different words,
both of which construe: `fieno`, will be, a future like the 1824 rubric of
II.14 (`fia`, D459), and `sieno`, be. Canestrini's rubric over the reply,
read by both FG readers without doubt, has `fieno`; the 1933 edition's
bracketed title has `fiano`, the same future. No precedent rules a doubt
common to both readers where both alternatives construe and the 1554
takes the other; it is put to David as **O48**, with `fieno` recommended
and applied provisionally (**D471**).

## FG-CONS.2.15 — Canestrini, pp. 68-69

296 words each (p. 68 204, p. 69 92). Both passes find the heading
**CONSIDERAZIONE SUL CAPITOLO XV** on p. 68,
below the end of the II.14 reply (`... di poco momento.`), with no `DEL
LIBRO II`; a two-line rubric in smaller type, `Gli Stati deboli sempre
fieno ambigui nel risolversi / e sempre le deliberazioni lente sono
nocive`; one indented paragraph; the end at p. 69 l. 10 `può essere
laudabile.`, with a printed stop and Canestrini's note call; and
CONSIDERAZIONE SUL CAPITOLO XIX following on p. 69 (the reply after II.15
is to II.19). Canestrini's note (1), at the foot of p. 69, `Danna il
Machiavelli le deliberazioni ambigue, lente e tarde, perchè ...`, is his
summary of the chapter and is not carried (D463). `paragraph_divisions:
witness` (D66). Pass A marks 33 loci, pass B 26 (2 and 1 in the rubric, 8
and 4 in the note).

**Body: no split.** The token streams are identical (296 to 296) after
preferred readings.

**Doubts where the readers prefer the word.** Common to both: `uno`,
`questi`, `abbino`, `giudicii`, `Lavinii`, and `è` twice (`che è propria`,
`questa è una`) against an accented `ò` that is no word here; A alone
`hanno` ×2, `etiam`, `sospensioni`, `utili`, `altrimenti`, `sommamente`,
`utile`; B alone `s'`. Each is the scan's h/b, u/n, ii/u, t/i, e/o or c/e
break; every preferred form is a word that construes, and the 1933 edition
prints the same word at each (`giudici`, `lavini`, `utile` in its own
spelling). Readings, as printed, as D398. `così`, `utilità`, accented by
DEC-009 (**D470**).

**Witness independence (SCOPE §7).** Neither pass carries a 1933
word-reading where Canestrini differs: both have `cagioni`,
`deliberazioni`, `prudenza` ×2, `potenza`, `il Discorso`, `periculi`,
`opinioni`, `giudicii`, `E è vero`, `sospensioni`, `utili`, `Lavinii`,
`resolversi`, `Il medesimo`, `chè`, `e utile`, against the 1933
`cagione`, `deliberazione`, `prudenzia`, `potenzia`, `el Discorso`,
`pericoli`, `opinione`, `giudici`, `Ed è vero`, `sospensione`, `utile`,
`lavini`, `risolversi`, `El medesimo`, `che`, `ed utile`. The passes read
Canestrini.

**Against the 1933 edition.** Otherwise forms (above). The plural article
printed `e` (`e partiti`, `e giudicii`, `e quali`) set `e'` by DEC-009
clause 2 (D35). `all altro`, both seeing no apostrophe, closed as elision
(Class A). Pointing: `deliberazioni⟨:|;⟩` (both) with the 1933 `:`;
`altro⟨:|;⟩` (both) with the 1933 `;`; `suspensione ⟨,|;⟩` (both), where
the 1933 prints a colon, a full stop between the two cases, set `;`, the
heavier of the two marks the readers see; `altrimenti.`, `nostra.` (a
faint point both see, each doubting a different alternative) with the
1933 `.`; `republica;`, `irresoluzione;`, `esecuzione;` (A without doubt,
B preferring `;`) kept; `ingegno ,`, `viaggio ,`, `laudare ,`, read alike
by both without doubt, kept against the 1933 `;` (D110). The stop after
`laudabile`, printed and seen by both, kept (D460) (**D470**).

**Heading and rubric.** The heading as printed, without `del libro II`, in
the unit's `heading` front-matter (D443). The rubric agrees with the 1824
rubric word for word, `fieno` included; its broken first letter of line 2
(`⟨e|o⟩`, both readers) and A's `⟨lente|iente⟩`, both preferring the
words, read with the 1824 rubric; the 1933 prints `fiano` and
`diliberazioni`; no stop, as Canestrini's rubrics are carried (**D471**,
as D463).

## Normalisation classes

Accents; elision and apocope spacing; the Florentine plural article
apostrophe; thin spaces before punctuation; line-end hyphens; note calls.
