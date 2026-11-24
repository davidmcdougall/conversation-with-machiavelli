---
unit: FG-CONS.3.17
reader: "cold reader fgA (Pass A, full)"
source: "Francesco Guicciardini, Considerazioni intorno ai Discorsi del Machiavelli, in G. Canestrini (ed.), Opere inedite di Francesco Guicciardini, vol. 1, Firenze 1857, pp. 74-75; page images only"
witness_images:
  - {file: 1857-p074-page.png, size: "1367x2184", rows: "0-2184", sha256_16: 92fb612344635ff6, check: "size and full sha256 match manifest"}
  - {file: 1857-p074-part1of2-y0-1179.png, size: "1367x1179", rows: "0-1179", sha256_16: f70fb485030eb2dc, check: "size and full sha256 match; pixel-identical to page rows 0-1179"}
  - {file: 1857-p074-part2of2-y1005-2184.png, size: "1367x1179", rows: "1005-2184", sha256_16: 7c77ee8f2315b92a, check: "size and full sha256 match; pixel-identical to page rows 1005-2184"}
  - {file: 1857-p075-page.png, size: "1367x2184", rows: "0-2184", sha256_16: 4e4a93ad2ea7a79c, check: "size and full sha256 match manifest"}
  - {file: 1857-p075-part1of2-y0-1179.png, size: "1367x1179", rows: "0-1179", sha256_16: 4c97960bcb0cb16b, check: "size and full sha256 match; pixel-identical to page rows 0-1179"}
  - {file: 1857-p075-part2of2-y1005-2184.png, size: "1367x1179", rows: "1005-2184", sha256_16: 47ae484f521727f9, check: "size and full sha256 match; pixel-identical to page rows 1005-2184"}
manifest_check: "PASS: all 6 files match manifest pixel size and full sha256; all 4 part images are pixel-identical (numpy array_equal) to the stated rows of their page image"
boundaries:
  precedes: "p. 74, lines 1-9 above the heading close the preceding consideration: '... e i Ro- / mani a Taranto, e negli altri luoghi che le trovorono fatte, / non le smurorono.' (last words 'non le smurorono.', p. 74 rows 653-680)"
  heading_page_line: "p. 74: heading on one line (rows 760-790), rubric on two lines below it (rows 856-885, 896-919), centred"
  body_first_words: "Molto più s ha a astenere (p. 74, line 1)"
  body_last_words: "ancora che avessi detto prima volerla sollecitare (p. 75, line 15)"
  follows: "p. 75 rows 1044-1073: heading 'Considerazione sul Capitolo XIX' (small caps, stop faint/doubtful), rubric 'Se a reggere una moltitudine è più necessario lo ossequio / che la pena', body begins 'La severità, nuda di ogni umanità'"
headings_printed:
  heading: "Considerazione sul Capitolo XVII del Libro III. -- one centred line; CONSIDERAZIONE, CAPITOLO, LIBRO in small capitals with full-capital initial C/C/L; SUL and DEL all small capitals; numerals XVII and III in full capitals; final stop printed after III (clear). The B of LIBRO is broken into vertical strokes (see locus H1)."
  rubric: "Che non si offenda uno, e poi quel medesimo si mandi in amministrazione / e governo d' importanza -- two centred lines, roman (not italic), smaller type than body; line 2 centred; no final stop printed after 'importanza' (no ink right of the word). Apostrophe after 'd' is faint, followed by a clear gap."
running_heads_etc: {p74: "running head 'CONSIDERAZIONI' (small caps, centred) with page number '74' at left, rows 195-222; no signature, no catchword", p75: "running head 'SUI DISCORSI DEL MACHIAVELLI' (small caps, centred) with page number '75' at right, rows 199-228; no signature, no catchword; footnote rule rows 1740-1746 (x 142-1048)", stray_marks: "p74: small speck right of running head (~x1140, y235); speck in left margin (~x55, y1640); dark vertical bar at right edge x~1339 from y~480 to y~1880 (scan edge/gutter shadow, not type); faint marks at foot (~x740-800, y2160); faint scanner/library watermark text bottom right (~x1240-1330, y2120). p75: small isolated tick to the left of 'lo' in body line 10 (between 'cho' and 'lo'); a dot (rows 830-835, x 918-924) is the i-dot of 'possibile' (line 13); faint watermark bottom right (~x1240-1300, y2120). No spurious sorts identified in the unit's text."}
footnotes: "one: call '(1)' superscript after 'Salinatore,' on p. 75 line 4; note printed at foot of p. 75 below a rule, two lines, smaller type, transcribed below"
paragraphing: "left ink edge of every body line (ink < 128): p. 74 L1 393, L2 335, L3 333, L4 335, L5 337, L6 337, L7 337, L8 335, L9 335, L10 333, L11 333, L12 335, L13 335, L14 335, L15 335, L16 337, L17 337, L18 335 (margin 333-337; only L1 indented, by ~58 px). p. 75 L1 113, L2 115, L3 114, L4 114, L5 114, L6 115, L7 114, L8 116, L9 117, L10 117, L11 117, L12 116, L13 116, L14 117, L15 116 (margin 113-117; no indent). The unit has 1 printed paragraph."
line_numbering: "body lines counted per page from the first body line on that page; p. 74 lines 1-18 (heading and rubric not counted, preceding consideration's 9 lines not counted), p. 75 lines 1-15; running heads, page numbers, headings, rubrics and footnote not counted"
body_word_count: 330
words_per_page: {p74: 183, p75: 147}
word_count_method: "work/wc.py on work/body.txt: uncertain loci replaced by preferred reading (∅ = nothing), footnote call removed; whitespace tokens; each token split after every apostrophe (' or `) so elided forms count separately; only parts containing a letter counted; a line-end hyphenated word counted once on the page where it begins (first token of the following line skipped). Heading and rubric excluded. Bare 's' and 'l' (printed without apostrophe) count as words."
uncertain_loci_per_page: {p74: 22, p75: 19}
uncertain_loci_total: 41
conventions: "Diplomatic, line for line. ⟨preferred|alternative⟩ inline; ∅ = no mark printed (alternative: mark expected/possibly lost). Preferred reading = what the shape of the printed sort shows; where sense favours the alternative, 'why' says so. An e whose hairline bar has failed so that it looks like c (e.g. fcndcndo, ncl, dcsiderato, elctto, possibilc, parolc, Neronc, Asdruhalc) is treated as a damaged but certain e and not marked, except where it stands as a whole word (p75 l14). Footnote call rendered ⁽¹⁾. Spaces before , ; not recorded. Apostrophe spacing recorded where a clear gap is visible. Rubric set in roman, shown in italic here only per output template."
paths_written: [/home/claude/p37/readers/fgA/work/check.py, /home/claude/p37/readers/fgA/work/lines.py, /home/claude/p37/readers/fgA/work/crops.py, /home/claude/p37/readers/fgA/work/z.py, /home/claude/p37/readers/fgA/work/wc.py, /home/claude/p37/readers/fgA/work/body.txt, "/home/claude/p37/readers/fgA/work/*.png (crops: p074_c0-7, p075_c0-10, z1-z17, z20-z22, l75_10-15, l74a, l74b, fn, fn2)", /home/claude/p37/readers/fgA/out/FG-CONS.3.17-passA.md]
---

# Body

Considerazione sul Capitolo XVII del ⟨Libro|Liuro⟩ III.

*Che non si offenda uno, e poi quel medesimo si mandi ⟨in|m⟩ ⟨amministrazione|amminislrazione⟩*
*e governo d' importanza*

[p. 74]
Molto più s⟨∅|'⟩ ha a astenere uno principe in non si com-
mettere in chi ⟨lia|ha⟩ ingiuriato, che una republica, perchè lo
ingiuriato dal principe ricognosce la ingiuria tutta da lui,
ma uno ingiuriato da una republica ricognosce più la in-
⟨ginria|giuria⟩ da qualche ⟨particularo|particulare⟩ che l⟨∅|'⟩ ha perseguitato o si è
trovato in magistrato, che dal nome della città, e però of-
fendendo la città non gli pare vendicarsi⟨.|,⟩ Di poi chi cerca
la rovina della patria⟨.|,⟩ fa male a⟨`|'⟩ parenti, agli amici, ⟨u|a⟩
⟨tntte|tutte⟩ le cose ⟨aue|sue⟩ medesime, e a sè proprio, e con infamia
di sè medesimo⟨;|,⟩ che non interviene a chi fa contro a uno
principe⟨.|,⟩ ⟨È|E⟩ ancora più facile spegnere uno principe che
una ⟨repnblica|republica⟩; e per questo ⟨uno|nno⟩ ⟨chn|che⟩ sia ingiuriato, può
essere più pronto a entrare in ⟨qnesto|questo⟩ pensiero⟨∅|.⟩ Però io
non sarei facile a fuggire uno cittadino ingiuriato dalla
sua republica, e massime quando la ingiuria non sia stata
molto atroce, nel quale caso si potria avergli rispetto, ma
quella di Claudio Nerone allegato nel Discorso, è cosa ri-
dicula a credere, che per essere stato calunniato nel tempo
[p. 75]
era in Spagna, e anche con qualche ragione, avessi avuto
tanto sdegno che potessi desiderare di ⟨easere|essere⟩ rotto, e le
parole, che lo Scrittore dice che lui usò, non furono parole
sue, ma del Salinatore,⁽¹⁾ il quale doppo il consulato era
stato condannato dal populo, e avendo ricevuta una ⟨talo|tale⟩
⟨ignominta|ignominia⟩, non è ⟨meravigha|meraviglia⟩ se ne ⟨risentisai|risentissi⟩ più. Il quale
se bene parlassi così o per ⟨adegno|sdegno⟩ o per certe ⟨natnre|nature⟩ o
fantasie che ⟨banno|hanno⟩ ⟨gh|gli⟩ uomini, è da credere che in fatto la
intendessi altrimenti⟨;|,⟩ e lo mostrano le azioni ⟨suo|sue⟩ prima,
innanzi alla elezione del consulato, ⟨cho|che⟩ lo recusò ostina-
⟨tamento|tamente⟩ insino non fu quasi sforzato da' principali citta-
dini. Il che ⟨archbe|arebbe⟩ desiderato se avessi avuto cupidità di
vendicarsi, di poi che eletto ⟨consnle|consule⟩ fece il possibile per
vincere, ⟨c|e⟩ andò molto renitente a fare la giornata con
⟨Asdruhale|Asdrubale⟩, ancora che avessi detto prima volerla sollecitare⟨.|∅⟩

# Footnotes on the page

p. 75, call ⁽¹⁾ after "Salinatore," (body line 4):

⁽¹⁾ È lo stesso Marco Livio, di soprannome ⟨Sailnatore|Salinatore⟩, eletto con-
sole insieme con Claudio Nerone

(no final stop printed)

# Uncertain loci

| n | page | line | printed context | ⟨preferred\|alternative⟩ | why |
|---|---|---|---|---|---|
| H1 | 74 | heading | del Libro III. | ⟨Libro\|Liuro⟩ | small-cap B broken into two vertical stems with no bowls; reads like U; sense favours Libro |
| R1 | 74 | rubric 1 | si mandi in amministrazione | ⟨in\|m⟩ | three broken minims, i-dot not distinct; could be read as m |
| R2 | 74 | rubric 1 | amministrazione | ⟨amministrazione\|amminislrazione⟩ | t with crossbar lost looks like l; letters badly broken throughout word |
| 1 | 74 | 1 | Molto più s ha | ⟨∅\|'⟩ | clear gap after s, no apostrophe ink at any threshold; an apostrophe may have failed to print; sense expects s' |
| 2 | 74 | 2 | in chi ha ingiuriato | ⟨lia\|ha⟩ | h's shoulder broken so it shows as l + i; sense favours ha |
| 3 | 74 | 5 | ginria da qualche | ⟨ginria\|giuria⟩ | second letter after gi shows n (u/n); sense favours giuria (continuing in-) |
| 4 | 74 | 5 | qualche particulare | ⟨particularo\|particulare⟩ | final letter round, bar trace weak: o vs e |
| 5 | 74 | 5 | che l ha | ⟨∅\|'⟩ | no apostrophe ink between l and ha; sense expects l' |
| 6 | 74 | 7 | vendicarsi. Di poi | ⟨.\|,⟩ | small faint (grey) mark at baseline, no visible tail; capital D follows |
| 7 | 74 | 8 | della patria. fa male | ⟨.\|,⟩ | small faint dot at baseline, no tail; lower-case fa follows, so sense favours comma |
| 8 | 74 | 8 | a` parenti | ⟨`\|'⟩ | the elision mark is printed slanting like a grave/backtick, placed low beside the a; probably a broken apostrophe |
| 9 | 74 | 8 | agli amici, a | ⟨u\|a⟩ | last word shows two minims open at top, like u; sense favours a |
| 10 | 74 | 9 | tntte le cose | ⟨tntte\|tutte⟩ | first u shows as n |
| 11 | 74 | 9 | le cose sue medesime | ⟨aue\|sue⟩ | first letter has a bowl like a (s/a) |
| 12 | 74 | 10 | medesimo; che | ⟨;\|,⟩ | lower comma clear, upper dot only faint grey |
| 13 | 74 | 11 | principe. È ancora | ⟨.\|,⟩ | faint small mark at baseline |
| 14 | 74 | 11 | È ancora | ⟨È\|E⟩ | a small dot-like mark above the E, could be a broken grave or a speck |
| 15 | 74 | 12 | una repnblica; | ⟨repnblica\|republica⟩ | u shows as n; sense favours republica |
| 16 | 74 | 12 | per questo uno che | ⟨uno\|nno⟩ | first letter between u and n at enlargement |
| 17 | 74 | 12 | uno chn sia | ⟨chn\|che⟩ | last letter has no eye/bar, looks like n; sense favours che |
| 18 | 74 | 13 | in qnesto pensiero | ⟨qnesto\|questo⟩ | u shows as n |
| 19 | 74 | 13 | pensiero Però io | ⟨∅\|.⟩ | no ink after pensiero at any threshold; capital P follows, so a stop may have failed to print |
| 20 | 75 | 2 | di easere rotto | ⟨easere\|essere⟩ | first s has a bowl like a (s/a) |
| 21 | 75 | 5 | una talo | ⟨talo\|tale⟩ | final letter closed, no bar: o vs e |
| 22 | 75 | 6 | ignominta, | ⟨ignominta\|ignominia⟩ | penultimate letter shows a cross-stroke like t (i/t) |
| 23 | 75 | 6 | meravigha | ⟨meravigha\|meraviglia⟩ | li joined into an h-shape (l/i/h) |
| 24 | 75 | 6 | risentisai più | ⟨risentisai\|risentissi⟩ | second s of -ssi has a bowl like a |
| 25 | 75 | 7 | per adegno | ⟨adegno\|sdegno⟩ | first letter shows as a (s/a); sense favours sdegno (cf. l. 2) |
| 26 | 75 | 7 | certe natnre | ⟨natnre\|nature⟩ | u shows as n |
| 27 | 75 | 8 | che banno | ⟨banno\|hanno⟩ | first letter with closed bowl like b (h/b) |
| 28 | 75 | 8 | gh uomini | ⟨gh\|gli⟩ | li fused into h-shape |
| 29 | 75 | 9 | altrimenti; e lo | ⟨;\|,⟩ | comma clear, upper dot faint |
| 30 | 75 | 9 | le azioni suo prima | ⟨suo\|sue⟩ | final letter closed like o (e/o) |
| 31 | 75 | 10 | consulato, cho lo | ⟨cho\|che⟩ | final letter like o (e/o); sense favours che |
| 32 | 75 | 11 | tamento insino | ⟨tamento\|tamente⟩ | final letter closed like o (e/o); sense (ostina-tamente) favours tamente |
| 33 | 75 | 12 | Il che arebbe | ⟨archbe\|arebbe⟩ | e shows as c and first b as h (h/b) |
| 34 | 75 | 13 | eletto consnle | ⟨consnle\|consule⟩ | u shows as n |
| 35 | 75 | 14 | vincere, e andò | ⟨c\|e⟩ | the one-letter word lacks its bar, looks like c |
| 36 | 75 | 15 | Asdruhale, | ⟨Asdruhale\|Asdrubale⟩ | b open at foot like h (h/b) |
| 37 | 75 | 15 | volerla sollecitare. | ⟨.\|∅⟩ | a faint grey mark at the stop position, weak |
| F1 | 75 | fn 1 | di soprannome Sailnatore | ⟨Sailnatore\|Salinatore⟩ | letters read S-a-i-l in that order at enlargement; sense (cf. body l. 4 Salinatore) favours Salinatore |
