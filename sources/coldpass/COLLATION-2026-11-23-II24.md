---
report: cold pass, pair II.24 (the twenty-fourth 1824 chapter under D199; D302 standing (D426, D457), no page eligible for the sample)
units: [NM-DISC.2.24, FG-CONS.2.24]
passes: [NM A (subagent, full chapter), NM B (subagent, full chapter, D484), FG A (subagent, full), FG B (subagent, full); each with its own image, work and output folders, forbidden every other path (D370)]
comparison_reads: [NM-DISC.2.24-1554 (subagent, Giglio 1554 page images only, own folders); 1933 edition pp. 57-59 (scan pages 63-65) read by the collator at the loci below]
performed: 2026-11-23 (passes, collation, rulings by precedent; no question put to David)
rule: SCOPE §7, as revised by D199, D203 and D302 (standing, D426, D457)
method: difflib.SequenceMatcher over word tokens, after DEC-009 Class A on both sides; the 1554 compared by character after spelling normalisation (u/v, h, j, ſ, doubled consonants, ti/zi, tildes, &/et/ed, accents, elision and word division) and then read through by hand against its transcript to separate forms of one word from word-level differences; D203(b) letter classes tested on the result
disposition: NM read twice in full, the passes identical in every word and mark (D484); the 1554's whole words, its omissions and its order not taken (D485). FG three paragraphs, the passes identical but at one split, read with the 1933 (`le adoperano`); one emendation, `[e]'` (D486). Rubrics and heading; Canestrini's two notes not carried (D487). No new establishment question
---

# Pair II.24 — cold passes and collation

Every image was cut from the rendered page in pixels and checked before any
reader saw it (D437): the 1824 pages at 350 ppi (2178 × 3282 px, native),
the Canestrini pages at 1200 ppi (1367 × 2184 px; native 600), the Giglio
leaves at 500 ppi (1639 × 3244, 1625 × 3209 px). Whole pages and thirds
(Canestrini: halves) with a 4% overlap; each crop's size matched its pixel
range, and the checksums within each reader's folder were distinct (44,
44, 36, 15, 15). Every reader checked its own images against the manifest
and found each what its name says.

**The 1824 extract was one page short.** NM-DISC-II24-pages.pdf (zero-based
pages 29-38 of the volume) ends at p. 35 in the middle of the chapter's last
period. The volume scan was fetched again from its recorded URL; its sha256
matches the one recorded (`db7f7e05...`), and pp. 26-35 rendered from it are
pixel-identical to the extract. p. 36 (zero-based 39), where the chapter
ends at l. 4, was extracted as NM-DISC-II24-p36.pdf and recorded in the
witness file. Both readers had p. 36 (D484).

NM pass A, FG passes A and B and the Giglio read were dispatched together.
NM pass B followed once pass A showed no page eligible for the sample. No
output was overwritten; each body matches its own witness.

`fazione` occurs in neither unit (D317, closed by D341; checked); nor does
`ferro`. `fortezza` occurs throughout both units, in every instance the
stronghold (D312); neither the virtue (FG I.10) nor the strength of a
country (D432) occurs.

## NM-DISC.2.24 — 1824, pp. 26-36

2,449 words (p. 26 114, p. 27 259, p. 28 263, p. 29 255, p. 30 247, p. 31
265, p. 32 256, p. 33 253, p. 34 256, p. 35 254, p. 36 27). Both passes find
CAPITOLO XXIV on p. 26 below the end of II.23 (`come nel suo luogo più
appieno si discorrerà.`), the two-line italic rubric `Le Fortezze
generalmente sono molto / più dannose che utili.`, an enlarged initial P,
one printed block with no indents and no notes, the Latin of Juvenal and
Virgil in italic (p. 28 ll. 1-2), and the end at p. 36 l. 4 `se ne /
assicurarono.`, CAPITOLO XXV following on the same page.

**No sample (D302).** A fifth of 2,449 is 490; the fullest page (p. 31)
holds 265. No page is eligible, so pass B read the whole chapter, as D352,
D391, D437, D476 (**D484**).

**Result.** The passes agree in every word and every mark (2,460 tokens
with the rubric, to 2,460). Pass A has three doubts, pass B seven. One is
between words: pass A's `⟨voglio|voglia⟩ mi basti` (p. 32 l. 15), a round
bowl crossed by a stroke; pass B reads `voglio` without doubt, the 1554
prints `uoglio`, and the same phrase stands at p. 33 l. 5 `e voglio mi
basti`. A doubt of one reader at a damaged sort, settled by sense and the
1554 (D457, D468). The rest are broken letters with no word for an
alternative (`altro` ×2, `eziandio`, `e'`, `prima`, `fendere`), a stray
mark after `poter` (B), and the mark after `riscontro` (both: a comma with
a tick above it), read as a comma by both and printed as a comma in the
1554.

**Against the 1554 (ruled by precedent).** The sense-bearing whole words,
each read by both full 1824 readers without doubt:

- `dipoi non ci è quella sicurtà dentro` (.03) / `dipoi ci è`: the 1554
  drops the negative and reverses the second reason;
- `le sono utili nei tempi di pace` (.03) / `elle ſono inutili`: the 1824's
  irony (useful in peace for doing the subjects ill) against the 1554's
  plain uselessness;
- `ed a quelli che non hanno buoni eserciti` (.13): the 1554 omits it by
  an eye-skip between the two `buoni eserciti`, and so calls fortresses
  useless to those with good armies;
- `essendo maltrattato da un suo Governatore` (.07): the 1554 omits
  `essendo maltrattato`, making the governor the agent of `assassinare`;
- `ed utile il rovinarla` (.08), the chiasmus's last member, omitted by
  the 1554;
- `ripresa e presa` (.12) / `preſa & ripreſa`: the 1824's chiasmus;
- `di quello ch'ella è` (.04), omitted; `cosa` / `coſi`, `come loro` /
  `come queſti`, `e che la seguì` / `& ſegui` (.01); `bene` / `buon` (.02);
  `rispettivo` / `riſpettoſo` (.04); `generazione` / `ſorte` (.05); `tanto
  stimato` / `ſtimato tanto` (.07); `si abbia` / `ſi haueſſe`, `il farla` /
  `di farla`, `Codefa` / `Codeſa` (.08); `ma la non è necessaria` / `ma non
  neceſsaria` (.14).

At the D203(b) letter classes, each read by both without doubt: `alcune` /
`alcuna` (.01), `e se` / `o ſe` (.02), `in su la Fortezza` / `in ſu le
forteZze` (.04), `chi le guarda` / `chi la guarda` (.05), `alle
Repubbliche` / `alla Repub.` (.09), `alla loro Città` / `alle` (.13),
`alla fronte` / `alle`, `Fortezze` / `fortezza` (.14). The 1824 construes
at each. Kept, D38, as D428, D438, D449, D459, D469, D477, with
translator's notes where the sense moves: **D485**. The 1554 prints the two
Latin tags without an Italian rendering.

Recorded as forms, without ruling: `fussero` / `fuſsino` and the like
throughout, `sendo` / `eſſendo`, `massime` / `maſsimamente`, `tenerli` /
`tenergli` and `li` / `gli` throughout, `Principe` / `Prencipe`, `nimico` /
`nemico`, `Donde` / `Onde`, `Dondechè` / `Onde che`, `potette` / `potè` ×4,
`riacquistarla` / `racquiſtarla`, `Federigo` / `Federico`, `Sisto IV` /
`IIII`, `1507` / `MDVII`, `1512` / `MDXII`, `sedici` / `XVI`, `diecimila` /
`X mila`, `dieci` / `X`, `Francesi`, `francese` / `Francioſi`, `Francioſo`,
`rimasto` / `rimaſa`, `dimostrato` / `dimoſtro`, `piccoli` / `piccioli`,
`adunque` / `dunque`, `vissuta` / `uiuuta`, `rifugio` / `rifuggio`,
`lasciano` / `laſcino`, `indietro` / `indrieto`, `de'` / `de i`, `che le
facciano` / `che el faccino`, `giudizio` / `giudicio`, `quelli Popoli` /
`quei popoli`, `di sopra` / `diſopra`, `Governatore` / `gouernadore`. The
1554's reader's doubts between words (`⟨ſarte|ſorte⟩`, `⟨uuci|uuoi⟩`,
`⟨amato|amate⟩`, `⟨ſuoi|ſu i⟩`, `⟨che|chi⟩`, `⟨lo|io⟩`) fall at loci where
the 1824 is read alike by both full passes. The 1554 leaves are sound: weak
impression and blotting at some line ends, a dark gutter band on the
versos, every word legible (D415 not needed).

**Rubric.** The 1554 sets the title as its heading, `LE FORTEZZE
GENERALMENTE SOno molto piu dannoſe, che utili. Ca. XXIIII.`: the same
sentence. The 1824 rubric is read alike by both readers without doubt
(**D487**).

## FG-CONS.2.24 — Canestrini, pp. 70-74

999 words each (p. 70 162, p. 71 327, p. 72 235, p. 73 189, p. 74 86). Both
passes find the heading **CONSIDERAZIONE SUL CAPITOLO XXIV** on p. 70 below
the end of the II.19 reply (`e le ragioni e la esperienza`, no stop), with
no `DEL LIBRO II` and a faint speck after the numeral that both doubt; a
one-line rubric in smaller type, `Le fortezze generalmente sono molto più
dannose che utili`, no stop, the accent on `più` unseen by both; three
indented paragraphs (p. 70 l. 15, p. 71 l. 31, p. 73 l. 4, each indented
about 60 px); the end at p. 74 l. 9 `non le smurorono.`, with a printed stop
both see; and CONSIDERAZIONE SUL CAPITOLO XVII DEL LIBRO III following on p.
74. Canestrini prints no replies to II.25-II.33 or to III.1-III.16.
`paragraph_divisions: witness` (D66). Pass A marks 44 loci, pass B 44 (2 in
the heading and rubric for each).

**Canestrini's notes.** Two, both keyed to this reply: (1) on p. 72, called
after `Brescia`, on Julius II's Holy League and Gaston de Foix's recovery of
Brescia in February 1512; (1) on p. 73, called after `Ottaviano`, on
Guidobaldo of Urbino's razing of his fortresses and Ottaviano Fregoso's
taking and razing of the Genoa fortress. Both are his historical glosses;
not carried (D463). The persons are identified in the edition's own
commentary (**D487**).

**Body: one split.** The token streams are identical (999 to 999) after
preferred readings but at `e' tempi nostri ⟨le|la⟩ adoperano` (p. 74 l. 7):
A `le` without doubt, B `la` doubting `le`, a broken a-shaped letter. Only
`le`, the fortresses, construes; the 1933 edition reads `le`. A reading,
with the 1933, as D215, D234, D406 (**D486**).

**Common doubt where only the other word construes.** `in sul tenere ⟨a|e⟩
populi suoi in qualche terrore` (p. 71 l. 14): both read `a`, both naming
`e`, the plural article that Canestrini prints `e` throughout the reply.
`tenere a populi` has no object; the 1933 edition reads `e' popoli`.
Emended `[e]'` under D68, as D442, D450 (E001, **D486**).

**Common doubt where both construe.** `in molti casi ⟨e|o⟩ in molti tempi`
(p. 74 l. 1): both prefer `e`; the 1933 edition reads `ed`. A reading, as
D303 settles a common doubt by the comparison witness (**D486**).

**Doubts where the readers prefer the word.** Common to both or one
reader's: `bene`, `imperio`, `se`, `spesso`, `per`, `qualche`, `s'`,
`stare`, `fussi`, `hassi`, `imperii`, `de'`, `edificato`, `principii`,
`usorono`, `trovandosi`, `e in molti luoghi`, `giudicorono`, B's `debbe`,
`vola`, `arebbe`. Each is the scan's e/o, e/a, s/a, u/a, h/b or l/i break;
every preferred form is a word that construes, and the 1933 edition prints
the same word at each. Readings, as printed, as D398. `servitù`, `sicurtà`,
`così` accented by DEC-009.

**Witness independence (SCOPE §7).** Neither pass carries a 1933
word-reading where Canestrini differs: both have `o a ogni principe`,
`imperii`, `inutili` ×2, `utili`, `armi`, `cagioni`, `nè il populo`, `e i
soccorsi`, `genti nuove`, `rebellione`, `remedii`, `nondimeno`, `adunque`,
`verbi gratia`, against the 1933 `ed a ogni principe`, `imperi`, `inutile`
×2, `utile`, `arme`, `cagione`, `né el popolo`, `ed e' soccorsi`, `gente
nuove`, `ribellione`, `remedi`, `nondimanco`, `adunche`, `verbigrazia`. The
passes read Canestrini.

**Against the 1933 edition.** `di una città, o a ogni principe` (p. 71 l.
32), read by both without doubt against the 1933 `ed a ogni principe`: a
word-level difference at e/o under D203(b); it construes (the tyrant of a
city, or any prince). Kept, D38, as D231, D308 (**D486**). Otherwise forms
(above). The plural article printed `e` (`e' fondamenti`, `e' Romani` ×2,
`e' quali`, `e' sudditi`, `e' populi` ×2, `e' cittadini`, `e' tempi`) set
`e'` by DEC-009 clause 2 (D35).

Pointing (D110): with the 1933 where both see a mark and weigh it
differently or split, `nuove,`, `progenie;`, `allega,`, `Stati,`,
`recuperarne,`, `fortezze; l'altra`, `inimicissime;`, `edificate,`,
`fortezze; ma`; at `dico ⟨:|;⟩ che` (A) / `dico ⟨;|,⟩ che` (B), where the
1933 prints no mark, the lighter of the two read, `;`; marks read alike
kept against the 1933 (`edifica;`, `fortezze;` at p. 71, `terrore;`,
`cattivo:`, `potente,`, `adoperano;`). The stops after `altre`, `no`,
`fortezza`, `provincia`, `Brescia`, `te`, `perdute`, faint to both, each
before a capital, read with the 1933 (D67). The printed stop at the end
kept (D460) (**D486**).

**Heading and rubric.** The heading as printed, without `del libro II`, in
the unit's `heading` front-matter (D443). The rubric agrees with the 1824
rubric word for word; `più` read with it; no stop, as Canestrini's rubrics
are carried (**D487**, as D463, D479).

## Normalisation classes

Accents; elision and apocope spacing; the Florentine plural article
apostrophe; spaces before punctuation; line-end hyphens; note calls.
