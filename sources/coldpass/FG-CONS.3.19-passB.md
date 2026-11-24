---
unit: FG-CONS.3.19
reader: "cold reader fgB (Pass B, full)"
source: "Francesco Guicciardini, Considerazioni intorno ai Discorsi del Machiavelli, in G. Canestrini (ed.), Opere inedite di Francesco Guicciardini, vol. 1, Firenze 1857, pp. 75-78; page images only"
witness_images:
  - {file: 1857-p075-page.png, size: "1367x2184", rows: "0-2184", sha256_16: 62deba9fec5cca8f, check: "size ok; sha256 ok"}
  - {file: 1857-p075-part1of2-y0-1179.png, size: "1367x1179", rows: "0-1179", sha256_16: 6f9d732830765878, check: "size ok; sha256 ok; pixel-identical to page rows 0-1179"}
  - {file: 1857-p075-part2of2-y1005-2184.png, size: "1367x1179", rows: "1005-2184", sha256_16: 55ccd47a2b67d9f3, check: "size ok; sha256 ok; pixel-identical to page rows 1005-2184"}
  - {file: 1857-p076-page.png, size: "1367x2200", rows: "0-2200", sha256_16: c5818fc3ea0f4c2f, check: "size ok; sha256 ok"}
  - {file: 1857-p076-part1of2-y0-1188.png, size: "1367x1188", rows: "0-1188", sha256_16: d73fd0358db7984d, check: "size ok; sha256 ok; pixel-identical to page rows 0-1188"}
  - {file: 1857-p076-part2of2-y1012-2200.png, size: "1367x1188", rows: "1012-2200", sha256_16: 1bc710bd0d566805, check: "size ok; sha256 ok; pixel-identical to page rows 1012-2200"}
  - {file: 1857-p077-page.png, size: "1367x2184", rows: "0-2184", sha256_16: e6dc169dc1eac2df, check: "size ok; sha256 ok"}
  - {file: 1857-p077-part1of2-y0-1179.png, size: "1367x1179", rows: "0-1179", sha256_16: c481c7f018e56316, check: "size ok; sha256 ok; pixel-identical to page rows 0-1179"}
  - {file: 1857-p077-part2of2-y1005-2184.png, size: "1367x1179", rows: "1005-2184", sha256_16: 0c5487370841bcf3, check: "size ok; sha256 ok; pixel-identical to page rows 1005-2184"}
  - {file: 1857-p078-page.png, size: "1367x2184", rows: "0-2184", sha256_16: ed1d70392715c6f7, check: "size ok; sha256 ok"}
  - {file: 1857-p078-part1of2-y0-1179.png, size: "1367x1179", rows: "0-1179", sha256_16: b8a662571b5b9048, check: "size ok; sha256 ok; pixel-identical to page rows 0-1179"}
  - {file: 1857-p078-part2of2-y1005-2184.png, size: "1367x1179", rows: "1005-2184", sha256_16: 7f4f658689d95593, check: "size ok; sha256 ok; pixel-identical to page rows 1005-2184"}
manifest_check: "PASS. All 12 files match MANIFEST pixel size and full sha256 (hashlib over file bytes); all 8 part images are array-identical (numpy array_equal, RGB) to the stated rows of their -page image. All files RGB."
boundaries:
  precedes: "End of the preceding Considerazione (on Discorsi III.17 or 18; its heading is not on these pages), p. 75 body lines 1-15: '... vincere, e andò molto renitente a fare la giornata con / Asdrubale, ancora che avessi detto prima volerla sollecitare⟨.|∅⟩' (faint grey block where a stop would be). Its footnote (1) is at the foot of p. 75."
  heading_page_line: "p. 75, after a blank space below the preceding unit's last line (page-image y 1044-1073); rubric two lines y 1116-1145 and 1155-1183; body begins y 1233."
  body_first_words: "La severità, nuda di ogni umanità o ⟨voghamo|vogliamo⟩ dire (p. 75, body line 1, indented)"
  body_last_words: "s' ha a presupporre, non può fare che non sia temuto. (p. 77, body line 29, last line of text on the page; lower page blank)"
  follows: "p. 78, top: heading 'CONSIDERAZIONE SUL CAPITOLO XXIV⟨.|∅⟩' (small caps as on p. 75), rubric 'La prolungazione degl' imperii fece serva Roma.' and body 'Non è dubio che la prorogazione degli imperii fu occa- / sione grande a chi volle occupare la republica⟨;|,⟩ perchè era ...'. Nothing intervenes between the end of 3.19 on p. 77 and this heading on p. 78 (no Considerazioni on chapters XX-XXIII)."
headings_printed:
  heading: "CONSIDERAZIONE SUL CAPITOLO XIX⟨.|∅⟩ - one centred line; 'C' of Considerazione and 'C' of Capitolo full capitals, the rest of those words and 'SUL' in small capitals, 'XIX' full-size roman capitals. 'del Libro ...' is NOT printed. Final stop: only a faint grey block (darkest value 164, vs ~20 for ink) at the baseline right after XIX; read as a possible stop, doubtful. Final letter of CONSIDERAZIONE lighter/broken ⟨E|F⟩."
  rubric: "Se a reggere ⟨uua|una⟩ ⟨mollitudine|moltitudine⟩ è più necessario lo ossequio / che la pena⟨.|∅⟩ - two centred lines in smaller roman type (not italic), second line short. Final stop: faint grey block only (darkest 201), doubtful."
running_heads_etc: {p75: "running head 'SUI DISCORSI DEL MACHIAVELLI' (small caps, centred) with page number '75' at right outer margin, same line", p76: "page number '76' at left, running head 'CONSIDERAZIONI' (small caps) centred", p77: "running head 'SUI DISCORSI DEL MACHIAVELLI' with '77' at right", p78: "page number '78' at left, 'CONSIDERAZIONI' centred", signatures: "none visible on any page", catchwords: "none", stray_marks: "p75: faint ghost marks at foot right (about x 1230, y 2050; digitisation watermark residue). p76: a vertical rule/streak in the right margin beside body lines 6-25 (x ~1340, y 451-1421), not text; a small dot at foot centre (x 676-681, y 2125-2130), not a signature; faint 'Google'-like watermark ghost at foot right. p77: an underline-like mark between 'sia' and 'da' in body line 1; a small dot (x 924-928, y 1323-1328) between body lines 22 and 23 under 'legittimi'; faint ghost at foot right. p78: vertical streak in right margin and an apostrophe-like speck in the left margin beside body line 7; an isolated dot well to the right of 'partigiano' at the end of the footnote; ghost watermark at foot right. Grey blocky specks (pixel blocks ~6 px, values 160-235) occur throughout all pages; they make stops doubtful."}
footnotes: "Three footnotes on these pages. (a) p. 75, call (1) after 'Salinatore,' in the preceding unit's body line 4 - keyed to the PRECEDING unit; transcribed below. (b) p. 76, call (1) after 'il timore.' in body line 6 of p. 76 - keyed to THIS unit (FG-CONS.3.19); transcribed in full below, editor's note citing Tacitus. (c) p. 78, call (1) after 'tirannidi.' in the following unit's body - keyed to the FOLLOWING unit (Considerazione sul Capitolo XXIV); transcribed below. Footnotes are in smaller type below a rule; calls are superscript parenthesised numerals."
paragraphing: "Left ink edge (first column with pixel <128, grayscale) per body line. p. 75 (column of the full lines 114-120): unit line 1 = 173 (INDENTED ~57 px, paragraph start); lines 2-10 = 116, 116, 115, 116, 117, 116, 114, 120, 116. p. 76 (right-margin streak excluded, x<1300): lines 1-27 = 323, 323, 323, 321, 319, 319, 319, 319, 321, 319, 319, 319, 319, 319, 321, 319, 319, 318, 317, 317, 317, 315, 317, 317, 315, 319, 315 - NO indented line (variation 315-323 is skew); line 27 'insolenti' is a short last line (right edge 445), paragraph end. p. 77 (column 132-136): line 1 = 194 (INDENTED ~60 px, new paragraph 'L' altra distinzione'); lines 2-29 = 133, 133, 133, 134, 135, 134, 135, 133, 133, 133, 133, 132, 136, 134, 134, 135, 135, 135, 136, 133, 134, 135, 135, 135, 136, 136, 136, 136; line 29 short (right edge 1004), unit end. So: two paragraphs - (1) p. 75 l.1 to p. 76 l.27 'insolenti'; (2) p. 77 l.1 'L' altra distinzione' to p. 77 l.29 'temuto.'"
line_numbering: "Body lines counted per page from the first body line of the unit on that page: p. 75 lines 1-10 (the preceding unit's 15 lines, the heading and the 2-line rubric not counted), p. 76 lines 1-27, p. 77 lines 1-29; running heads, page numbers, heading, rubric and footnotes not counted. Footnote lines are cited as fn1, fn2 ... in the table."
body_word_count: 641
words_per_page: {p75: 93, p76: 251, p77: 297}
word_count_method: "Python script over the transcription below: preferred reading of each ⟨|⟩ taken; ∅ and the footnote call removed; whitespace tokens, further split after every apostrophe (' or ’) so elided forms count separately (e.g. l' una = 2, de'governi = 2); only tokens containing a letter counted (lone ; : , dropped); a word hyphenated across a line end counted once, on the line where it begins, including piace-/vole across pp. 75-76; heading, rubric, running heads and footnotes excluded."
uncertain_loci_per_page: {p75_heading_rubric: 5, p75_body: 14, p76_body: 25, p77_body: 19, footnote_p76_this_unit: 11, footnote_p75_preceding_unit: 3, footnote_p78_following_unit: 7}
uncertain_loci_total: 63
conventions: "uncertain_loci_total = 63 counts heading, rubric and body of this unit; the 11 loci in this unit's footnote (p. 76) and the 10 in the neighbours' footnotes are listed in the table too (84 rows) but kept out of that total. ⟨preferred|alternative⟩: preferred = the letter/mark the printed shape on the image shows; alternative = the other reading considered (usually what sense requires); ∅ = nothing printed. Many sorts print as other letters (h for b, c for e, n for u, b for h, a for s); these are recorded with the shape preferred and the sense reading as alternative, not corrected. An i whose dot is lost (ı) is transcribed i without a doubt marker (no other reading is possible); accents and apostrophes, being substantive, are marked when doubtful. Spacing: a space after an apostrophe is recorded only where a clear gap is visible (l' una, dell' uno, gl' Italiani, s' abbino, de' populi; but l'amore, de'governi closed); spaces before ; : , recorded where printed (altri ;, nità ,). Line-end hyphens kept. Footnote call rendered ⁽¹⁾. No italic in the body; italic in the p. 76 footnote marked *...*. Pixel coordinates refer to the -page images."
paths_written: ["/root/p38/readers/fgB/out/FG-CONS.3.19-passB.md", "/root/p38/readers/fgB/work/ (scratch: crop.py, z.py, comp.py, lines.py, count.py, body.txt, crop PNGs)"]
---

# Body

[p. 75]

CONSIDERAZIONE SUL CAPITOLO XIX⟨.|∅⟩

Se a reggere ⟨uua|una⟩ ⟨mollitudine|moltitudine⟩ è più necessario lo ossequio
che la pena⟨.|∅⟩

La severità, nuda di ogni umanità o ⟨voghamo|vogliamo⟩ dire
piacevolezza, è inutile in chi regge altri ; la umanità o
vero piacevolezza non accompagnata da ⟨qualchc|qualche⟩ severità
è il medesimo ; l' una condita ⟨equalmentc|egualmente⟩ con l' altra sa-
⟨rehbe|rebbe⟩ preziosissima, e ⟨aarebbe|sarebbe⟩ quella armonia ⟨temporata|temperata⟩
⟨chc|che⟩ è ⟨snaviasima|soavissima⟩ e ammirabile⟨∅|.⟩ Ma ⟨perchò|perchè⟩ questo condi-
mento o rare volte o non mai si truova in ⟨nomo|uomo⟩ alcuno;
essendo così lo ordine della natura che ⟨tntte|tutte⟩ le cose no-
stre abbino qualche imperfezione, anzi pare ⟨cbc|che⟩ ciascuno
o ⟨ahbia|abbia⟩ più del severo che del piacevole, o più del piace-

[p. 76]
vole ⟨cbe|che⟩ del severo ; non sanza cagione ⟨sl|si⟩ dubita quale
sia più a proposito, o ⟨cbi|chi⟩ participando dell' uno e ⟨dell|dell'⟩ al-
tro ha più del severo, o vero chi ha più dello umano, in-
tendendo però di coloro che hanno tanto dell' uno e del-
l' altro, che dove abbonda il timore non ⟨mancbi|manchi⟩ ⟨l|l'⟩ amore,
e dove abbonda l'amore non ⟨mancbi|manchi⟩ il timore.⁽¹⁾ Circa a che
la prima ⟨diatinzione|distinzione⟩ che mi occorre è considerare la na-
tura di chi tu reggi ⟨;|,⟩ perchè alcuni sono di ingegno sì no-
bile e generoso che ⟨piu|più⟩ volentieri vanno con la piacevo-
lezza ⟨cbe|che⟩ col timore ⟨;|,⟩ altri pel contrario pieni di una
certa durezza, che non si possono piegare con la dolcezza,
ma ⟨bisogns|bisogna⟩ domargli e rompergli con la asperità. Non è
dubio ⟨cbe|che⟩ con questi tali bisogna accommodarsi secondo
le loro condizioni ; e a ⟨qnesto|questo⟩ proposito diceva Federico
Barbarossa, principe molto eccellente, e che nato in Ger-
mania aveva lungamente conversato in Italia, che le due
prime nazioni del mondo, e secondo l' altre, piene di molte
⟨vìrtù|virtù⟩, erano e Germani e gl' Italiani ; ma che bisognava
diversa arte di reggergli, perchè e Tedeschi erano arro-
ganti, insolenti, e di qualità ⟨cbe|che⟩ la dolcezza che tu usavi
con loro, la attribuivano ⟨piu|più⟩ presto a timore che a uma-
nità , pel contrario ⟨gl|gl'⟩ Italiani, più trattabili, ⟨piu|più⟩ gentili, e
di natura ⟨cbe|che⟩ la asperità più presto gli sdegnava ⟨cbe|che⟩ spa-
ventava. Però a questi essere necessario perdonare tal-
volta e delitti, e procedere con benignità ⟨;|,⟩ quelli altri pu-
nirli severamente, perchè altrimenti diventerebbono ⟨piu|più⟩
insolenti⟨.|∅⟩

[p. 77]
L' altra ⟨distinzione|disunzione⟩ che mi occorre è che sia da fare
differenza da uno ⟨cbe|che⟩ regga come ⟨principo|principe⟩ e con ⟨antorità|autorità⟩
propria, da chi regge come ministro e in nome di altri ;
perchè io credo che uno principe ⟨abhia|abbia⟩ a avere rispetto
assai di cercare la benevolenza de' populi, potendo occor-
rere molti casi ⟨cbo|che⟩ a conservare lo Stato gli ⟨aia|sia⟩ bisogno
amore estraordinario ⟨de'|dè⟩ populi. Ma in chi comanda in
nome di altri ⟨distingnerei|distinguerei⟩ : o in uno esercito, e allora fussi
più necessario abbondare nello amore ⟨cbe|che⟩ nel timore,
perchè avendoli a condurre a fazioni periculose per la
città loro, vi si conducono assai con lo amore ; ma in chi
governa città o provincie in nome di altri, non gli toc-
cando altro ⟨cbe|che⟩ la cura temporale, e non essendo lui il
signore supremo per il quale e populi s' abbino a muovere
a più di ⟨qnello|quello⟩ che ordinariamente sono ⟨tennti|tenuti⟩, credo con-
duca meglio le cose sue con qualche più terrore che e
principi ordinarii: perchè sapendo e populi che le genti
dependono da altri, e che di qui a qualche tempo lui non
ha a ⟨restaro|restare⟩ in ufficio, non può la benevolenza, che loro
gli portassino, fare fondamento notabile a quelli effetti per
e ⟨qnali|quali⟩ si desidera tanto lo amore verso il ⟨principo|principe⟩. Dico
però che parlando noi de'governi buoni e legittimi, si può
male presupporre che dove è timore non sia anche amore⟨;|,⟩
perchè la severità della ⟨giuatizia|giustizia⟩, che è quella che reca il
timore, non può essere che non sia amata da chi vuole
bene vivere ⟨;|,⟩ ed e converso lo amore che nasce da uma-
nità, da facilità di natura, e da inclinazione a fare grazie,
accompagnato dalla giustizia, come in uno governo buono
s' ha a presupporre, non può fare che non sia temuto.


# Footnotes on the page

**p. 76 - keyed to THIS unit (FG-CONS.3.19); call (1) after "il timore." in p. 76 body line 6 ("non ⟨mancbi|manchi⟩ il timore.⁽¹⁾ Circa a che")**

⁽¹⁾ ⟨Jl|Il⟩ Machiavelli opina essere miglior consiglio per governare una
⟨moltiludine|moltitudine⟩ mostrarsi ⟨umauo|umano⟩ piuttosto che superbo, pietoso piuttosto
che crudele, contro la nota sentenza di Tacito⟨:|∅⟩ *in multitudine regenda*
*plus ⟨pæna|poena⟩ quam obsequium valet*⟨.|∅⟩ ⟨Peró|Però⟩ avverte nello stesso tempo che
dovendo comandare a' sudditi, ⟨afliuchè|affinchè⟩ ⟨nou|non⟩ diventino insolenti, si deb-
ba ricorrere piuttosto alla ⟨pella|pena⟩ che all' ossequio⟨∅|.⟩

**p. 75 - keyed to the PRECEDING unit; call (1) after "Salinatore," in that unit's body line 4 on p. 75 ("ma del Salinatore,⁽¹⁾ il quale doppo il consulato")**

⁽¹⁾ È lo stesso ⟨Merco|Marco⟩ Livio, di soprannome ⟨Sailnatore|Salinatore⟩, eletto con-
sole insieme con Claudio Nerone⟨∅|.⟩

**p. 78 - keyed to the FOLLOWING unit (Considerazione sul Capitolo XXIV); call (1) after "tirannidi." ("alle tirannidi.⁽¹⁾ Di quivi nacque")**

⁽¹⁾ Due sono le cagioni che secondo il Machiavelli prepararono la
caduta della repubblica⟨:|∅⟩ le contenzioni che nacquero dalla legge agra-
ria e la prolungazione del comando degli eserciti⟨.|∅⟩ Quest'ultima produce
sempre due inconvenienti⟨:|∅⟩ l' uno che minor numero di ⟨uemini|uomini⟩ si eser-
citano negli imperii, e si viene per questo a ristringere la riputazione in
pochi ⟨,|;⟩ ⟨l|l'⟩ altro che chi rimane lungo tempo a comandare l' esercito, lo
guadagna, e lo rende suo partigiano⟨∅|.⟩

(No other footnotes on pp. 75-78.)

# Uncertain loci

| n | page | line | printed context | ⟨preferred\|alternative⟩ | why |
|---|---|---|---|---|---|
| 1 | 75 | heading | CONSIDERAZIONE | ⟨E\|F⟩ | last letter of CONSIDERAZIONE pale, lower arm faint; E is surely meant |
| 2 | 75 | heading | CAPITOLO XIX | ⟨.\|∅⟩ | only a faint grey block (min 164) at baseline after XIX; may be a damaged stop or scan noise |
| 3 | 75 | rubric l.1 | reggere ... ossequio | ⟨uua\|una⟩ | second letter has a hairline closure looking like u; sense: una |
| 4 | 75 | rubric l.1 | una ... è | ⟨mollitudine\|moltitudine⟩ | 4th glyph tall like l (t crossbar not visible); sense: moltitudine |
| 5 | 75 | rubric l.2 | che la pena | ⟨.\|∅⟩ | faint grey block (min 201) after pena; damaged stop or noise |
| 6 | 75 | 1 | o ... dire | ⟨voghamo\|vogliamo⟩ | li joined into an h shape; sense: vogliamo |
| 7 | 75 | 3 | da ... severità | ⟨qualchc\|qualche⟩ | final e lacks its bar |
| 8 | 75 | 4 | condita ... con | ⟨equalmentc\|egualmente⟩ | q-shaped descender and barless final e; sense (and usual form): egualmente |
| 9 | 75 | 5 | sa- / ... preziosissima | ⟨rehbe\|rebbe⟩ | first b open, h-shaped; sense: (sa)rebbe |
| 10 | 75 | 5 | e ... quella | ⟨aarebbe\|sarebbe⟩ | initial s prints like a |
| 11 | 75 | 5 | armonia ... | ⟨temporata\|temperata⟩ | second vowel shows a closed o; sense: temperata |
| 12 | 75 | 6 | ... è | ⟨chc\|che⟩ | final e lacks bar |
| 13 | 75 | 6 | è ... e ammirabile | ⟨snaviasima\|soavissima⟩ | shape reads s-n-a-v-i-a-s-i-m-a (o as n, s as a); sense: soavissima |
| 14 | 75 | 6 | ammirabile ... Ma | ⟨∅\|.⟩ | no stop visible though a capital follows; sense requires a stop |
| 15 | 75 | 6 | Ma ... questo | ⟨perchò\|perchè⟩ | final vowel round like ò; sense: perchè |
| 16 | 75 | 7 | in ... alcuno | ⟨nomo\|uomo⟩ | first letter n-shaped (turned or broken u); sense: uomo |
| 17 | 75 | 8 | che ... le cose | ⟨tntte\|tutte⟩ | second letter n-shaped; sense: tutte |
| 18 | 75 | 9 | pare ... ciascuno | ⟨cbc\|che⟩ | h prints as b, e lacks bar |
| 19 | 75 | 10 | o ... più | ⟨ahbia\|abbia⟩ | first b open, h-shaped |
| 20 | 76 | 1 | vole ... del | ⟨cbe\|che⟩ | h prints as b |
| 21 | 76 | 1 | cagione ... dubita | ⟨sl\|si⟩ | i shows as l |
| 22 | 76 | 2 | o ... participando | ⟨cbi\|chi⟩ | h prints as b |
| 23 | 76 | 2 | e ... al- | ⟨dell\|dell'⟩ | no apostrophe visible after dell (only a faint mark); dell' expected as earlier in line |
| 24 | 76 | 5 | non ... amore | ⟨mancbi\|manchi⟩ | h prints as b |
| 25 | 76 | 5 | manchi ... amore | ⟨l\|l'⟩ | gap after l with no visible apostrophe |
| 26 | 76 | 6 | non ... il timore | ⟨mancbi\|manchi⟩ | h prints as b |
| 27 | 76 | 7 | la prima ... che | ⟨diatinzione\|distinzione⟩ | s looks like a; sense distinzione |
| 28 | 76 | 8 | reggi ... perchè | ⟨;\|,⟩ | upper dot of semicolon faint |
| 29 | 76 | 9 | che ... volentieri | ⟨piu\|più⟩ | no accent visible |
| 30 | 76 | 10 | lezza ... col | ⟨cbe\|che⟩ | h prints as b |
| 31 | 76 | 10 | timore ... altri | ⟨;\|,⟩ | upper dot faint |
| 32 | 76 | 12 | ma ... domargli | ⟨bisogns\|bisogna⟩ | final a looks like s |
| 33 | 76 | 13 | dubio ... con | ⟨cbe\|che⟩ | h prints as b |
| 34 | 76 | 14 | e a ... proposito | ⟨qnesto\|questo⟩ | u n-shaped |
| 35 | 76 | 18 | ... , erano | ⟨vìrtù\|virtù⟩ | mark over the first i slants like a grave; probably a damaged dot |
| 36 | 76 | 20 | qualità ... la | ⟨cbe\|che⟩ | h prints as b |
| 37 | 76 | 21 | attribuivano ... presto | ⟨piu\|più⟩ | no accent visible |
| 38 | 76 | 22 | contrario ... Italiani | ⟨gl\|gl'⟩ | gap with no clear apostrophe |
| 39 | 76 | 22 | trattabili, ... gentili | ⟨piu\|più⟩ | accent not visible (faint speck only) |
| 40 | 76 | 23 | natura ... la | ⟨cbe\|che⟩ | h prints as b |
| 41 | 76 | 23 | sdegnava ... spa- | ⟨cbe\|che⟩ | h prints as b |
| 42 | 76 | 25 | benignità ... quelli | ⟨;\|,⟩ | mark is a broken vertical; semicolon or comma |
| 43 | 76 | 26 | diventerebbono ... | ⟨piu\|più⟩ | no accent visible |
| 44 | 76 | 27 | insolenti | ⟨.\|∅⟩ | faint grey block (min 198) at baseline; paragraph end requires a stop |
| 45 | 77 | 1 | L' altra ... che | ⟨distinzione\|disunzione⟩ | t+i run together into a u-like shape; t ascender visible |
| 46 | 77 | 2 | uno ... regga | ⟨cbe\|che⟩ | h prints as b |
| 47 | 77 | 2 | come ... e con | ⟨principo\|principe⟩ | final vowel shows as o; sense: principe |
| 48 | 77 | 2 | con ... | ⟨antorità\|autorità⟩ | u n-shaped |
| 49 | 77 | 4 | principe ... a avere | ⟨abhia\|abbia⟩ | second b h-shaped |
| 50 | 77 | 6 | casi ... a conservare | ⟨cbo\|che⟩ | h as b, e as o |
| 51 | 77 | 6 | gli ... bisogno | ⟨aia\|sia⟩ | s prints like a |
| 52 | 77 | 7 | estraordinario ... populi | ⟨de'\|dè⟩ | mark sits high over/after e; apostrophe or grave accent |
| 53 | 77 | 8 | altri ... : o | ⟨distingnerei\|distinguerei⟩ | u n-shaped |
| 54 | 77 | 9 | amore ... nel | ⟨cbe\|che⟩ | h prints as b |
| 55 | 77 | 13 | altro ... la cura | ⟨cbe\|che⟩ | h prints as b |
| 56 | 77 | 15 | di ... che | ⟨qnello\|quello⟩ | u n-shaped |
| 57 | 77 | 15 | sono ... , credo | ⟨tennti\|tenuti⟩ | u n-shaped |
| 58 | 77 | 19 | ha a ... in ufficio | ⟨restaro\|restare⟩ | final e shows as o |
| 59 | 77 | 21 | e ... si desidera | ⟨qnali\|quali⟩ | u n-shaped |
| 60 | 77 | 21 | verso il ... . Dico | ⟨principo\|principe⟩ | final vowel shows as o; sense principe |
| 61 | 77 | 23 | anche ... | ⟨amore;\|amore,⟩ | semicolon's upper dot faint |
| 62 | 77 | 24 | della ... , che | ⟨giuatizia\|giustizia⟩ | s prints like a |
| 63 | 77 | 26 | bene vivere ... ed | ⟨;\|,⟩ | upper dot faint |
| 64 | 76 | fn1 | ... Machiavelli | ⟨Jl\|Il⟩ | capital I prints with a hook, like J |
| 65 | 76 | fn2 | una / ... | ⟨moltiludine\|moltitudine⟩ | second t without crossbar |
| 66 | 76 | fn2 | mostrarsi ... | ⟨umauo\|umano⟩ | n shaped like u |
| 67 | 76 | fn3 | Tacito ... in | ⟨:\|∅⟩ | faint marks after Tacito; colon probable |
| 68 | 76 | fn4 | plus ... quam | ⟨pæna\|poena⟩ | italic diphthong looks like æ; poena/pœna |
| 69 | 76 | fn4 | valet ... Però | ⟨.\|∅⟩ | faint grey block only |
| 70 | 76 | fn4 | ... avverte | ⟨Peró\|Però⟩ | accent direction unclear |
| 71 | 76 | fn5 | sudditi, ... | ⟨afliuchè\|affinchè⟩ | ff/n broken; shape a-f-l-i-u-c-h-e; sense affinchè |
| 72 | 76 | fn5 | ... diventino | ⟨nou\|non⟩ | final n u-shaped |
| 73 | 76 | fn6 | alla ... che | ⟨pella\|pena⟩ | n prints like ll |
| 74 | 76 | fn6 | all' ossequio | ⟨∅\|.⟩ | no stop visible at footnote end |
| 75 | 75 | fn1 | stesso ... Livio | ⟨Merco\|Marco⟩ | a looks like e |
| 76 | 75 | fn1 | soprannome ... | ⟨Sailnatore\|Salinatore⟩ | l and i transposed in shape; sense Salinatore |
| 77 | 75 | fn2 | Claudio Nerone | ⟨∅\|.⟩ | no stop visible |
| 78 | 78 | fn2 | repubblica ... le | ⟨:\|∅⟩ | faint mark only |
| 79 | 78 | fn3 | eserciti ... Quest' | ⟨.\|∅⟩ | faint mark only |
| 80 | 78 | fn4 | inconvenienti ... l' | ⟨:\|∅⟩ | faint mark only |
| 81 | 78 | fn4 | di ... si eser- | ⟨uemini\|uomini⟩ | o looks like e |
| 82 | 78 | fn6 | pochi ... altro | ⟨,\|;⟩ | mark after pochi is comma-like |
| 83 | 78 | fn6 | ... altro | ⟨l\|l'⟩ | apostrophe not visible |
| 84 | 78 | fn7 | suo partigiano | ⟨∅\|.⟩ | no stop directly after the word; an isolated dot lies far to the right (displaced stop or stray mark) |
