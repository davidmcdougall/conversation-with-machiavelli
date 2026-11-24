---
unit: FG-CONS.3.17
reader: "cold reader fgB (Pass B, full)"
source: "Francesco Guicciardini, Considerazioni intorno ai Discorsi del Machiavelli, in G. Canestrini (ed.), Opere inedite di Francesco Guicciardini, vol. 1, Firenze 1857, pp. 74-75; page images only"
witness_images:
  - {file: 1857-p074-page.png, size: "1367x2184", rows: "0-2184", sha256_16: 92fb612344635ff6, check: "size and full sha256 match manifest"}
  - {file: 1857-p074-part1of2-y0-1179.png, size: "1367x1179", rows: "0-1179", sha256_16: f70fb485030eb2dc, check: "size and full sha256 match; pixel-identical to page rows 0-1179"}
  - {file: 1857-p074-part2of2-y1005-2184.png, size: "1367x1179", rows: "1005-2184", sha256_16: 7c77ee8f2315b92a, check: "size and full sha256 match; pixel-identical to page rows 1005-2184"}
  - {file: 1857-p075-page.png, size: "1367x2184", rows: "0-2184", sha256_16: 4e4a93ad2ea7a79c, check: "size and full sha256 match manifest"}
  - {file: 1857-p075-part1of2-y0-1179.png, size: "1367x1179", rows: "0-1179", sha256_16: 4c97960bcb0cb16b, check: "size and full sha256 match; pixel-identical to page rows 0-1179"}
  - {file: 1857-p075-part2of2-y1005-2184.png, size: "1367x1179", rows: "1005-2184", sha256_16: 47ae484f521727f9, check: "size and full sha256 match; pixel-identical to page rows 1005-2184"}
manifest_check: "PASS: all 6 files match manifest pixel size and full sha256; all 4 part images pixel-identical (numpy array_equal, RGB) to the stated row ranges of their -page image"
boundaries:
  precedes: "end of preceding consideration, p. 74 top, last words: '... e negli altri luoghi che le trovorono fatte, / non le smurorono.' (p. 74, 9th text line below running head)"
  heading_page_line: "p. 74: heading on one line (image rows 760-790) after a blank, rubric on two lines (rows 856-885, 896-919), body begins row 993"
  body_first_words: "Molto più s ha a astenere uno principe (p. 74, line 1)"
  body_last_words: "ancora che avessi detto prima volerla sollecitare. (p. 75, line 15)"
  follows: "p. 75 heading 'Considerazione sul Capitolo XIX.' (small capitals), rubric 'Se a reggere una moltitudine è più necessario lo ossequio / che la pena', body begins 'La severità, nuda di ogni umanità o vogliamo dire' (p. 75, image rows 1044-1270)"
headings_printed:
  heading: "CONSIDERAZIONE SUL CAPITOLO XVII DEL LIBRO III. -- one line, centred; small capitals (initials C, C, L as full capitals; 'sul', 'del' all small capitals); roman numerals XVII and III as full capitals; final stop printed after III. 'Libro': the b is broken and could be read u (Li⟨b|u⟩ro) but the word is not in doubt. Rendered in Body as 'Considerazione sul Capitolo XVII del Libro III.'"
  rubric: "Che non si offenda uno, e poi quel medesimo si mandi in amministrazione / e governo d' importanza -- two lines, centred, smaller roman type (NOT italic in print; italic markup in Body follows the output template only); no final stop printed after 'importanza' (no ink in rows 890-925 to the right of the word); visible gap after d'. Several letters broken (dotless i in 'si', 'mandi', 'in', 'amministrazione', 'importanza') without doubt of reading."
running_heads_etc: {p74: "running head 'CONSIDERAZIONI' (capitals/small capitals) centred, page number '74' at left (rows 195-222); no signature or catchword", p75: "running head 'SUI DISCORSI DEL MACHIAVELLI' centred, page number '75' at right (rows 199-228); no signature or catchword", stray_marks: "p74: small speck below running head at right (approx x1140, y230); speck in left margin (approx x55, y1670); vertical scan line/edge in right margin approx x1335 rows ~270-1700; marks at foot approx x740-800, y2150-2165; faint digitiser watermark bottom right (approx x1230-1330, y2040). p75: tiny speck between body lines 12 and 13 at x918-924, rows 830-835; faint digitiser watermark bottom right (approx x1240-1270, y2035). Faint grey blocks (values ~160-215, not below 128) appear where ink has dropped out, e.g. upper dots of semicolons and some stops; these are treated as uncertain loci where they bear on punctuation."}
footnotes: "one note, p. 75 foot, below a rule (rows 1740-1746), smaller type, two lines; call mark (1) set superscript after 'Salinatore,' on p. 75 line 4; transcribed below. No stop printed after 'Nerone'."
paragraphing: "Left ink edge (first column with pixel <128 in the line band). p.74 body: line 1 = 393 px; lines 2-18 = 333-337 px (margin ~335) -> line 1 indented ~58 px (paragraph opening). p.75 body lines 1-15: 113-117 px (margin ~115), none indented (line 1 at 113 px; it continues the paragraph). Following unit's first body line on p.75 = 173 px vs 114-120 margin, indented ~58 px, confirming indent size. The unit has 1 printed paragraph."
line_numbering: "Body lines counted per page from first body line; p.74 lines 1-18 (rows 993-1857), p.75 lines 1-15 (rows 264-980). Heading, rubric, running heads, page numbers and footnote not counted."
body_word_count: 330
words_per_page: {p74: 183, p75: 147}
word_count_method: "work/count.py on work/body.txt: each ⟨a|b⟩ replaced by a (∅ = empty), apostrophe-elided forms split off (a', da'), whitespace-split, only tokens containing a letter counted ('(1)' excluded), a line-end hyphenated word counted once on the line where it begins (com-/mettere, in-/giuria, of-/fendendo, ri-/dicula on p.74; ostina-/tamente, citta-/dini on p.75). Heading and rubric excluded."
uncertain_loci_per_page: {p74: 18, p75: 15}
uncertain_loci_total: 33
conventions: "⟨preferred|alternative⟩ inline; preferred = what the ink most resembles, alternative = the other reading the broken letter/mark admits (sense noted in 'why'). ∅ = no mark printed/visible. Footnote loci (3) are listed separately (F1-F3) and not counted in the body totals. Broken letters whose reading is certain are not marked, notably dotless i throughout and e with lost crossbar inside otherwise certain words (e.g. p.75 'eletto' printed elctto-like, 'possibile', 'Asdrubale', 'vendicarsi', 'renitente'); when the damaged e yields a full o, c or other letter in a position where it changes the word form, it is marked. Spaces before punctuation not recorded. Italics: none in body. Footnote call written (1)."
paths_written: ["/home/claude/p37/readers/fgB/work/check.py", "/home/claude/p37/readers/fgB/work/lines.py", "/home/claude/p37/readers/fgB/work/crop.py", "/home/claude/p37/readers/fgB/work/multi.py", "/home/claude/p37/readers/fgB/work/multic.py", "/home/claude/p37/readers/fgB/work/dots.py", "/home/claude/p37/readers/fgB/work/count.py", "/home/claude/p37/readers/fgB/work/body.txt", "/home/claude/p37/readers/fgB/work/*.png (crops: h74, a0-a6, r1-r3, h2, z1-z5, c1-c5, b0-b4, hb, fn, rh, d1-d6)", "/home/claude/p37/readers/fgB/out/FG-CONS.3.17-passB.md"]
---

# Body

Considerazione sul Capitolo XVII del Libro III.

*Che non si offenda uno, e poi quel medesimo si mandi in amministrazione*
*e governo d' importanza*

[p. 74]
Molto più ⟨s ha|s' ha⟩ a astenere uno principe in non si com-
mettere in chi ⟨ha|lia⟩ ingiuriato, che una republica⟨;|,⟩ perchè lo
ingiuriato dal principe ricognosce la ingiuria tutta da lui,
ma uno ingiuriato da una republica ricognosce più la in-
⟨ginria|giuria⟩ da qualche ⟨particulare|particularo⟩ che ⟨l ha|l' ha⟩ perseguitato o si è
trovato in magistrato, che dal nome della città, e però of-
fendendo la città non gli pare vendicarsi⟨.|∅⟩ Di poi chi cerca
la rovina della patria⟨.|,⟩ fa male ⟨a'|a`⟩ parenti, agli amici, ⟨n|a⟩
tutte le cose ⟨aue|sue⟩ medesime, e a sè proprio, e con infamia
di sè medesimo⟨;|,⟩ che non interviene a chi fa contro a uno
principe⟨.|∅⟩ È ancora più facile spegnere uno principe che
una ⟨repablica|republica⟩; e per questo uno ⟨chn|che⟩ sia ingiuriato, può
essere più pronto a entrare in ⟨qnesto|questo⟩ pensiero⟨∅|.⟩ Però io
non sarei facile a fuggire uno cittadino ingiuriato dalla
sua republica, e massime quando la ingiuria non ⟨sin|sia⟩ stata
molto atroce, nel quale caso si potria avergli rispetto, ma
quella di Claudio Nerone allegato nel Discorso, è cosa ri-
dicula a credere, che per essere stato calunniato nel tempo
[p. 75]
⟨cra|era⟩ in Spagna, e anche con qualche ragione, avessi avuto
tanto sdegno che potessi desiderare di ⟨easere|essere⟩ rotto, e le
parole, che lo Scrittore dice che lui usò, non furono parole
sue, ma del Salinatore,(1) il quale doppo il consulato era
stato condannato dal populo, e avendo ricevuta una ⟨talo|tale⟩
⟨ignominta|ignominia⟩, non è meraviglia se ne ⟨risentisai|risentissi⟩ più. Il quale
se bene parlassi così o per ⟨adegno|sdegno⟩ o per certe ⟨natnre|nature⟩ o
fantasie che ⟨banno|hanno⟩ ⟨gh|gli⟩ uomini, è da credere che in fatto la
intendessi altrimenti⟨;|,⟩ e lo mostrano le azioni ⟨suo|sue⟩ prima,
innanzi alla elezione del consulato, ⟨cho|che⟩ lo recusò ostina-
tamente insino non fu quasi sforzato da' principali citta-
dini. Il che ⟨archbe|arebbe⟩ desiderato se avessi avuto cupidità di
vendicarsi, di poi che eletto ⟨consnle|consule⟩ fece il possibile per
vincere, e andò molto renitente a fare la giornata con
Asdrubale, ancora che avessi detto prima volerla sollecitare⟨.|∅⟩

# Footnotes on the page

(1) È lo ⟨slesso|stesso⟩ Marco Livio, di soprannome ⟨Sailnatore|Salinatore⟩, eletto con-
⟨sole|vole⟩ insieme con Claudio Nerone

(p. 75, call after 'Salinatore,' in body line 4; no stop printed after 'Nerone'. Footnote loci F1-F3 are not included in the body counts.)

# Uncertain loci

| n | page | line | printed context | ⟨preferred\|alternative⟩ | why |
|---|---|---|---|---|---|
| 1 | 74 | 1 | Molto più s ha a astenere | ⟨s ha\|s' ha⟩ | wide gap after s, no apostrophe ink visible; sense expects s' |
| 2 | 74 | 2 | mettere in chi ha ingiuriato | ⟨ha\|lia⟩ | h broken at shoulder, can look like li |
| 3 | 74 | 2 | republica, perchè | ⟨;\|,⟩ | solid comma tail with a faint grey block at x-height (dropped upper dot of semicolon?) |
| 4 | 74 | 5 | giuria da qualche | ⟨ginria\|giuria⟩ | second letter shows n-shape (arch at top); sense giuria |
| 5 | 74 | 5 | particulare che | ⟨particulare\|particularo⟩ | final e with weak crossbar, near o |
| 6 | 74 | 5 | che l ha perseguitato | ⟨l ha\|l' ha⟩ | gap after l, no apostrophe ink; sense expects l' |
| 7 | 74 | 7 | vendicarsi Di poi | ⟨.\|∅⟩ | only a faint grey block at baseline after the i |
| 8 | 74 | 8 | della patria fa male | ⟨.\|,⟩ | faint grey blocks at baseline, no visible tail; sense favours comma |
| 9 | 74 | 8 | a' parenti | ⟨a'\|a`⟩ | raised mark slants like a grave/turned comma; read as apostrophe |
| 10 | 74 | 8 | agli amici, n | ⟨n\|a⟩ | line-final letter shows n-shape; sense (a tutte) favours a |
| 11 | 74 | 9 | le cose sue medesime | ⟨aue\|sue⟩ | first letter shows a-bowl; s/a confusion; sense sue |
| 12 | 74 | 10 | medesimo; che | ⟨;\|,⟩ | comma tail solid, upper dot only a faint grey block |
| 13 | 74 | 11 | principe È ancora | ⟨.\|∅⟩ | faint grey block at baseline only |
| 14 | 74 | 12 | una repablica; | ⟨repablica\|republica⟩ | third-from-u letter shows a-shape; sense republica |
| 15 | 74 | 12 | uno chn sia | ⟨chn\|che⟩ | final letter has two stems with top arch (n); sense che |
| 16 | 74 | 13 | in qnesto pensiero | ⟨qnesto\|questo⟩ | u shows as n |
| 17 | 74 | 13 | pensiero Però | ⟨∅\|.⟩ | no mark visible even in contrast stretch; sense expects stop |
| 18 | 74 | 15 | non sia stata | ⟨sin\|sia⟩ | final letter shows n-shape; a/n; sense sia |
| 19 | 75 | 1 | era in Spagna | ⟨cra\|era⟩ | initial e has lost crossbar, reads c |
| 20 | 75 | 2 | di essere rotto | ⟨easere\|essere⟩ | second letter shows a-bowl; s/a |
| 21 | 75 | 5 | una tale | ⟨talo\|tale⟩ | final letter closed like o |
| 22 | 75 | 6 | ignominia, non | ⟨ignominta\|ignominia⟩ | penultimate letter has t-like ascender (grey block above); sense ignominia |
| 23 | 75 | 6 | se ne risentissi più | ⟨risentisai\|risentissi⟩ | penultimate letter shows a-shape; s/a |
| 24 | 75 | 7 | o per sdegno | ⟨adegno\|sdegno⟩ | initial shows a-shape; s/a; cf. sdegno p.75 l.2 |
| 25 | 75 | 7 | certe nature o | ⟨natnre\|nature⟩ | u shows as n |
| 26 | 75 | 8 | che hanno gli uomini | ⟨banno\|hanno⟩ | h/b: initial looks closed like b |
| 27 | 75 | 8 | gli uomini | ⟨gh\|gli⟩ | l and i merged/broken, looks h |
| 28 | 75 | 9 | altrimenti; e lo | ⟨;\|,⟩ | comma tail solid, upper dot only faint grey blocks |
| 29 | 75 | 9 | le azioni sue prima | ⟨suo\|sue⟩ | final letter closed like o |
| 30 | 75 | 10 | consulato, che lo recusò | ⟨cho\|che⟩ | final letter closed like o |
| 31 | 75 | 12 | Il che arebbe desiderato | ⟨archbe\|arebbe⟩ | third letter e lacks crossbar (c), fourth shows ascender with arch (h/b); sense arebbe |
| 32 | 75 | 13 | eletto consule fece | ⟨consnle\|consule⟩ | u shows as n |
| 33 | 75 | 15 | volerla sollecitare | ⟨.\|∅⟩ | only a faint grey block at baseline |
| F1 | 75 | fn 1 | È lo stesso Marco Livio | ⟨slesso\|stesso⟩ | t lacks crossbar, reads l |
| F2 | 75 | fn 1 | di soprannome Salinatore | ⟨Sailnatore\|Salinatore⟩ | letters after S appear as a-i-l-n; i/l and a/i order broken; sense Salinatore (cf. text p.75 l.4) |
| F3 | 75 | fn 2 | sole insieme | ⟨sole\|vole⟩ | first letter of line partly lost; sense sole (con-/sole) |
