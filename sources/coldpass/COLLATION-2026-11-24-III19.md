---
report: cold pass, pair III.19 (the twenty-sixth 1824 chapter under D199; D302 standing (D426, D457), the sample page p. 154 with four line crops)
units: [NM-DISC.3.19, FG-CONS.3.19]
passes: [NM A (subagent, full chapter, with p. 156 as boundary evidence), NM B (subagent, the sample page p. 154 and four line crops of p. 155), FG A (subagent, full), FG B (subagent, full); each with its own image, work and output folders, forbidden every other path (D370)]
comparison_reads: [NM-DISC.3.19-1554 (subagent, Giglio 1554 page images only, own folders); 1933 edition pp. 62-64 (scan pages 68-70) read by the collator at the loci below]
performed: 2026-11-24 (passes, collation, rulings by precedent; one question put to David, O49)
rule: SCOPE §7, as revised by D199, D203 and D302 (standing, D426, D457)
method: difflib.SequenceMatcher over word tokens, after DEC-009 Class A on both sides (accents, ſ, elision spacing, line-end hyphens); marks compared as a second token stream; the 1554 compared by word after spelling normalisation (u/v, h, j, ſ, doubled consonants, tildes, &/et/ed, accents, elision and word division) and then read through by hand against its transcript to separate forms of one word from word-level differences; D203(b) letter classes tested on the result
disposition: NM pass A full, pass B the sample page with crops, agreeing word for word and mark for mark (D500); the 1554's whole words, its omissions and its added rendering of the Latin not taken (D501). FG two paragraphs, the passes identical once each doubt is resolved to the word it names, but for one split between two forms of one word, `pericolose`/`periculose` (O49, applied provisionally); `sarebbe`, `città` and `genti` kept against the 1933 (D38); pointing by D110, the stop after `ammirabile` supplied (D502). Rubrics and heading; Canestrini's note not carried (D503)
---

# Pair III.19 — cold passes and collation

Every image was cut from the rendered page in pixels and checked before any
reader saw it (D437): the 1824 pages at 350 ppi (2052 × 3228 px, native
351), the Canestrini pages at 1200 ppi (1367 × 2184 and 1367 × 2200 px;
native 600), the Giglio leaves at 500 ppi (1639 × 3244, 1625 × 3209 px).
Whole pages and thirds (Canestrini: halves) with a 4% overlap; each crop's
size matched its pixel range and each part was byte-identical to its rows
of the page, and the checksums within each reader's folder were distinct
(12, 12, 12, 8, and 8 for pass B). Every reader checked its own images
against the manifest and found each what its name says. The four line
crops for pass B were checked on a contact strip before dispatch: each
holds its whole line and nothing of its neighbours' letters.

**The extracts and the chapter's end.** Each extract was checked to reach
the chapter's end before any reader was sent. The Canestrini extract
(pp. 75-78) prints the next heading, CONSIDERAZIONE SUL CAPITOLO XXIV, at
the head of p. 78; the Giglio extract (fol. 181r-181v) prints Cap. XX on
181v. The 1824 extract, NM-DISC-III19-pages.pdf (zero-based pages 157-158,
pp. 154-155), ends at the foot of p. 155 with the chapter's last sentence,
`... potè appresso ai Falisci più che l'armi.`, and no following heading:
its text layer, which names the Falisci, reads as if it had reached CAPITOLO
XX's rubric, but on the image it is Machiavelli's closing sentence, which
announces the next chapter's subject. The end could not be proved from the
extract. The volume scan was fetched again from its recorded URL; its
sha256 matches the one recorded (`db7f7e05...`), pp. 154-155 rendered from
it are pixel-identical to the extract, and p. 156 (zero-based 159) opens
CAPITOLO XX at its head. p. 156 was extracted as NM-DISC-III19-p156.pdf
(sha256 `5716ee9b...`) and recorded in the witness file, and pass A had it,
as boundary evidence only (D500, as D484, D492). The chapter opens at the
head of p. 154 under its heading; the end of III.18 is on p. 153, which no
reader needed.

All four full readers were dispatched together; pass B followed once pass A
and the Giglio read were in and the sample page had been chosen. No output
was overwritten; each body matches its own witness.

`ferro` and `fortezza` occur in neither unit (D433; D312, D432; checked).
`fazione` occurs once, in the Guicciardini, `condurre a fazioni pericolose`
(p. 77 l. 10), of leading an army: the military sense, "actions", decided
by sense as D341 rules (D317, closed by D341).

## NM-DISC.3.19 — 1824, pp. 154-155

407 words (p. 154 195, p. 155 212). Pass A finds CAPITOLO XIX at the head of
p. 154, a two-line italic rubric ending `l' ossequio che la pena.` with a
printed stop, a raised initial E, one printed block with no indents and no
notes, the Latin of Tacitus in italic, and the end at p. 155 l. 26 `più che
l' armi.`; on p. 156 CAPITOLO XX, its rubric `Uno esempio d' umanità appresso
ai Falisci potette più d' ogni forza romana.`, and `Essendo Camillo con
l'esercito`.

**The sample (D302).** A fifth of 407 is 82; both pages are eligible.
Word-level 1554 differences after spelling normalisation: p. 154 five
(`Donde` / `Onde`, `acconsentono` / `conſentono`, `quando dice` / `Quando
ait`, the 1554's added Italian rendering of the Latin, `che ne diventava` /
`che diuentaua`), 2.6 per hundred words; p. 155 three (`facilità` /
`felicità`, `se non necessitato` / `non neceſsitato`, `spargerlo` /
`ſpargerla`), 1.4. Chosen and recorded before dispatch: **p. 154**, with
line crops of p. 155 l. 8 (rows 942-1019), l. 15 (rows 1473-1549), l. 19
(rows 1779-1853), the three differences outside it, and l. 20 (rows
1853-1930), where the 1554's `adunque` against `dunque` is a form of one
word, cropped all the same. Pass A has no doubt between words, so no
further crop (D203(a)). Pass B was not told which word.

**Result.** The sample page agrees with pass A in every word and every
mark, heading and rubric included (195 words to 195, 238 tokens to 238),
and all four crops agree word for word. Pass B's two doubts: `⟨e|c⟩d` (l. 4),
a worn e with a faint bar, the shape preferred as `e`, which pass A reads
without doubt and the 1554 prints `&`; and a speck after `E` (l. 24), which
both readers describe and both read as no mark. Pass A's doubts are the
same speck, the space after two apostrophes (`de' quali`, `l'odio`), a
reversed-c sort in `dentro` (p. 155 l. 22), which only `o` construes, and a
tail under the last `i` of `armi`. No reading turns on any of them. D302
stands (**D500**).

**Against the 1554 (ruled by precedent).** The sense-bearing whole words,
each read by pass A and, on the sample or a crop, by pass B, without doubt:

- `Donde e' pare` (.02) / `Onde e pare`: two adverbs of one sense;
- `al quale molti altri Scrittori acconsentono` (.02) / `conſentono`: two
  verbs of one sense;
- `quando dice:` (.02) / `Quando ait,`: the 1554 keeps Tacitus' Latin verb;
- the 1554 follows the Latin with an Italian rendering, `Cioe, Per regger
  molti ual piu la ſeuerita, che l'eſſer benigno.`; the 1824 has none: not
  carried, as at II.15;
- `non poteva uno che ne diventava Principe a tempo` (.03) / `uno, che
  diuentaua`: the 1554 omits `ne`, of it (the plebs);
- `per troppa tua facilità` (.04) / `felicità`: easiness against happiness;
- `nessun Principe ne è desideroso se non necessitato` (.04) / `non
  neceſsitato`: the 1824's "unless necessitated" against the 1554's "not
  being necessitated";
- `il desiderio di spargerlo` (.04) / `ſpargerla`: the 1824's pronoun takes
  `sangue`; the 1554's feminine has no noun it can take but `rapina`.

No difference falls at the D203(b) letter classes. The 1824 construes at
each; kept, D38, as D428, D438, D449, D459, D469, D477, D485, D493, with a
translator's note where the sense moves (`facilità`, `se non`, `spargerlo`):
**D501**.

Recorded as forms, without ruling: `de' Nobili` / `de nobili`, `Quinzio` /
`Quintio`, `ubbidito`, `ubbidienti` / `obbidito`, `obbidienti`, `dai suoi`
/ `da ſuoi`, `umano` / `humano`, `opinioni` / `oppenioni`, `eguale` /
`equale`, `Nobiltà` / `nobilita`, `Principe` / `Prencipe`, `fecero` /
`feciono`, `li maneggiavano` / `gli maneggiauano`, `virtù` / `uertu`,
`piuttosto` / `piu toſto`, `alcun` / `alcuno`, `nessun` / `neſſuno`,
`desideroso`, `desiderio` / `diſideroſo`, `diſiderio`, `rare volte` /
`rade uolte`, `sendovi` / `eſſendoui`, `dunque` / `adunque`, `dentro ai` /
`dentro a i`, `un esempio` / `uno eſſempio`, `poena` / `pœna`. The Giglio
reader's doubts (hyphens and stops at line ends, accent-like specks over
`fuggì`, `fugga`, `volte`, `mescolata`, `debbe`, a broken `t` before
`inſolenti`, the smudged `diuentino`, the damaged `F` of `Faliſci`) fall at
loci the 1824 readers read alike without doubt. The leaves are sound: show-
through and worn sorts, no tear or loss, every word of the chapter legible
(D415 not needed).

**Rubric.** The 1554 sets the title as its heading, `SE A REGGERE VNA
MOLTITVDINE e piu neceſſario l'oſſequio, che la pena. Ca. XIX.`: the same
sentence but for spelling and a comma. The 1824 rubric is read alike by
both 1824 readers without doubt, with its stop (**D503**).

**The Latin.** `In multitudine regenda plus poena, quam obsequium valet.`
Read alike by both 1824 readers, in italic, with the comma; the 1554
prints `in multitudine regenda plus pœna , quam obſequium ualet.`, the
same words, marked off with `,,` in the margin. No such
sentence is in Tacitus. The nearest is *Annals* 3.55, where Tacitus says
that `obsequium inde in principem et aemulandi amor validior quam poena ex
legibus et metus`: compliance towards the prince and the love of emulating
him were stronger than the penalty of the laws and fear, the reverse of
the sentence Machiavelli gives him (checked against the Latin text at
sacred-texts.com; the editor's reference). Carried as the 1824 prints it,
in latin.md.

## FG-CONS.3.19 — Canestrini, pp. 75-77

641 words each (p. 75 93, p. 76 251, p. 77 297). Both passes find the heading
**CONSIDERAZIONE SUL CAPITOLO XIX** on p. 75 below the end of the III.17
reply (`volerla sollecitare.`), set in capitals and small capitals,
**without** `del libro III`, with a pale grey dot in the stop's place that
both readers doubt (both preferring a stop, darkest value 164 against an
ink threshold of 128); a two-line rubric in smaller roman type, `Se a
reggere una moltitudine è più necessario lo ossequio / che la pena`, with
no inked stop; **two** paragraphs, indented at p. 75 l. 1 (about 57 px) and
at p. 77 l. 1, `L' altra distinzione` (about 60 px), with no other indent;
the end at p. 77 l. 29 `non può fare che non sia temuto.`; and CONSIDERAZIONE
SUL CAPITOLO XXIV at the head of p. 78. Canestrini prints no reply to
III.18 and none to III.20-23. `paragraph_divisions: witness` (D66). Pass A
marks 61 loci in the heading, rubric and body, pass B 63. (Both readers
took the reply above for III.18's, there being no heading over it on these
pages; it is III.17's.)

**Canestrini's note.** One, keyed to this reply: (1) on p. 76, called after
`il timore.`, summarising Machiavelli's chapter and quoting Tacitus'
sentence as Machiavelli gives it; read alike by both, but for broken
letters. His gloss; not carried (D463, D487, D495). The other two notes on
these pages belong to the III.17 reply (p. 75, Salinator) and the III.24
reply (p. 78) (**D503**).

**The readers' preferences.** Both readers, at a letter the scan has
broken, gave the shape as the preferred reading and the word as the
alternative, as at III.17: `voghamo`, `piacevolczza`, `qualchc`,
`rehbe`, `temporata`, `chc`, `nomo`, `tntte`, `ahhino`, `ahbia`, `cbe`,
`sl`, `qualc`, `cbi`, `mancbi`, `disfinzione`|`diatinzione`, `piem`,
`bisogns`, `qnesto`, `pei`, `principo`, `antorità`, `abhia`, `cbo`, `aia`,
`distingnerei`, `abhino`, `qnello`, `tennti`, `restaro`, `faro`, `qnali`,
`giuatizia`, `aarebbe`, `uua`, `mollitudine`. Where one reader prefers the
shape, the other reads the word, mostly without doubt. At every such locus
only the word is Italian and the 1933 edition prints it: readings, the
word, as D398, D406, D494 (**D502**). At `⟨anaviasima|suavissima⟩` (A) /
`⟨snaviasima|soavissima⟩` (B) both see the same broken letters and name two
forms of one word; the shape, `s-n-a-v`, is `suav-` with the scan's u/n
break, and the 1933 prints `suavissima`: read `suavissima`, with A, the
shape and the 1933 (D406, D494). B's `⟨equalmentc|egualmente⟩` names a form
the shape does not show; A reads `equalmente`, which the 1933 prints. The
token streams are then identical, 641 to 641, but at one locus.

**The split.** `condurre a fazioni ⟨pericolose|periculose⟩ per la città loro`
(p. 77 l. 10): A reads `pericolose`, B `periculose`, **both without doubt**.
Two forms of one word; the English is "dangerous" either way. The 1933
prints `pericolose`, but it normalises Canestrini's `periculo-` spellings
throughout (D462), so its form is no evidence, and this reply spells the
root nowhere else. D406 (a split of forms read with the 1933) is narrowed
by D462 exactly where the 1933 normalises, and D462 settled its case by the
reply's own spelling, which is not available here. Not covered by a
precedent: **O49**, with the recommendation `periculose`, the spelling
Canestrini prints for the root in most of the replies so far (22
occurrences to 14 in the established *Considerazioni*), applied
provisionally. An image check would settle it, and is not done unasked.

**Against the 1933 (ruled by precedent).** Three whole words, each read
alike by both readers without doubt, none at the D203(b) letter classes:

- `e sarebbe quella armonia temperata` (.01) / 1933 `e farebbe`: "would
  be" against "would make"; both construe;
- `avendoli a condurre a fazioni pericolose per la città loro` (.02) / 1933
  `per la vita loro`: actions dangerous for their city, against for their
  life; Canestrini's construes, and the city recurs in the next clause
  (`in chi governa città o provincie`);
- `sapendo e' populi che le genti dependono da altri` (.02) / 1933 `le
  grazie`: that the men (the governed) depend on others, against that the
  favours do; Canestrini's construes, weaker, and the 1933's matches
  `inclinazione a fare grazie` at the close.

Kept, D38 (as D400, D408, D450, D486); variant notes and translator's notes
(**D502**). The 1933's readings are the better at `vita` and `grazie`; D38
keeps the governing witness wherever it construes.

**Witness independence (SCOPE §7).** Neither pass carries a 1933
word-reading where Canestrini differs: both have `il medesimo`, `il
timore` ×2, `il signore`, `il quale`, `il principe`, `populi` ×4,
`benevolenza` ×2, `e a questo`, `e allora`, `e in nome`, `condizioni`,
`nazioni`, `gl' Italiani` ×2, `ufficio`, `ordinarii`, `o vero` ×2,
`abbondare`, `sarebbe`, `città`, `genti`, against the 1933 `el medesimo`,
`el timore`, `el signore`, `el quale`, `el principe`, `popoli`,
`benevolenzia`, `ed a questo`, `ed allora`, `ed in nome`, `condizione`,
`nazione`, `gli italiani`, `uficio`, `ordinari`, `overo`, `abondare`,
`farebbe`, `vita`, `grazie`. Pass A's `pericolose` agrees with the 1933 at
the one split; a single form, not a pattern. The passes read Canestrini.

**Pointing (D110).** With the 1933 where both see a mark and doubt its
weight: `col timore,` (p. 76 l. 10; both `⟨;|,⟩`, preferring `;`; 1933
`,`), `anche amore,` (p. 77 l. 23; the same; 1933 `,`); `reggi;`,
`benignità;`, `vivere;`, doubted alike, kept where the 1933 also prints
`;`. `insolenti⟨∅|.⟩` at the end of the first paragraph (A no mark, B a
faint block): a split, the 1933 `insolenti.`, so the stop. The stop after
`ammirabile` (p. 75 l. 6), seen by neither reader before the capital of
`Ma`, supplied from the 1933 (C001, D67). The heading's pale dot: both see
a mark and prefer a stop; the 1933 prints none after CAPITOLO XIX, so the
lighter reading, none (D110). Marks read alike by both are kept against the
1933 (`severità,` l. 1, `altri;`, `alcuno;`, `natura che`, `umano,`,
`condizioni;`, `arroganti, insolenti, e`, `umanità, pel`). Canestrini's
printed stop at the end, seen by both, kept (D460) (**D502**).

**The plural article.** Canestrini prints the Florentine plural article
bare at `e Germani`, `e Tedeschi`, `e delitti`, `e populi` ×2, `e principi
ordinarii`, `per e quali`; set `e'` by D35 (DEC-009 Class A). At `erano e
Germani e gl' Italiani` the first `e` is the article, answered by `gl'`,
not "both ... and"; the 1933 prints `e' germani e gli italiani`.

**Heading and rubric.** The heading as printed, without `del libro III` and
without the stop (D443, D110), in the unit's `heading` front-matter. The
rubric agrees with the 1824 rubric but for `lo ossequio` against `l'
ossequio`, two forms of the article; Canestrini's form carried; the readers'
doubts in it (`⟨uua|una⟩`, `⟨mollitudine|moltitudine⟩`) are broken letters,
read with the 1824 rubric; no stop, as Canestrini's rubrics are carried
(**D503**, as D463, D479, D487, D495). The 1933 sets the 1824's sentence, with
`l'ossequio`, as a bracketed title.

## Normalisation classes

Accents; elision and apocope spacing, and elisions printed with no
apostrophe (`dell al-tro`, `l amore`, `gl Italiani`) set with one (D39);
the Florentine plural article apostrophe (D35); spaces before punctuation;
line-end hyphens; the note call.
