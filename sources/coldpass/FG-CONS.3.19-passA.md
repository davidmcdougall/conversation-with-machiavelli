---
unit: FG-CONS.3.19
reader: "cold reader fgA (Pass A, full)"
source: "Francesco Guicciardini, Considerazioni intorno ai Discorsi del Machiavelli, in G. Canestrini (ed.), Opere inedite di Francesco Guicciardini, vol. 1, Firenze 1857, pp. 75-78; page images only"
witness_images:
  - {file: 1857-p075-page.png, size: "1367x2184", rows: "0-2184", sha256_16: 62deba9fec5cca8f, check: "size ok; sha256 ok"}
  - {file: 1857-p075-part1of2-y0-1179.png, size: "1367x1179", rows: "0-1179", sha256_16: 6f9d732830765878, check: "size ok; sha256 ok; pixel-identical to page rows 0-1179"}
  - {file: 1857-p075-part2of2-y1005-2184.png, size: "1367x1179", rows: "1005-2184", sha256_16: 55ccd47a2b67d9f3, check: "size ok; sha256 ok; pixel-identical to page rows 1005-2184"}
  - {file: 1857-p076-page.png, size: "1367x2200", rows: "0-2200", sha256_16: c5818fc3ea0f4c2f, check: "size ok; sha256 ok"}
  - {file: 1857-p076-part1of2-y0-1188.png, size: "1367x1188", rows: "0-1188", sha256_16: d73fd0358db7984d, check: "size ok; sha256 ok; pixel-identical to page rows 0-1188"}
  - {file: 1857-p076-part2of2-y1012-2200.png, size: "1367x1188", rows: "1012-2200", sha256_16: 1bc710bd0d565806, check: "size ok; sha256 ok; pixel-identical to page rows 1012-2200"}
  - {file: 1857-p077-page.png, size: "1367x2184", rows: "0-2184", sha256_16: e6dc169dc1eac2df, check: "size ok; sha256 ok"}
  - {file: 1857-p077-part1of2-y0-1179.png, size: "1367x1179", rows: "0-1179", sha256_16: c481c7f018e56316, check: "size ok; sha256 ok; pixel-identical to page rows 0-1179"}
  - {file: 1857-p077-part2of2-y1005-2184.png, size: "1367x1179", rows: "1005-2184", sha256_16: 0c5487370841bcf3, check: "size ok; sha256 ok; pixel-identical to page rows 1005-2184"}
  - {file: 1857-p078-page.png, size: "1367x2184", rows: "0-2184", sha256_16: ed1d70392715c6f7, check: "size ok; sha256 ok"}
  - {file: 1857-p078-part1of2-y0-1179.png, size: "1367x1179", rows: "0-1179", sha256_16: b8a662571b5b9048, check: "size ok; sha256 ok; pixel-identical to page rows 0-1179"}
  - {file: 1857-p078-part2of2-y1005-2184.png, size: "1367x1179", rows: "1005-2184", sha256_16: 7f4f658689d95593, check: "size ok; sha256 ok; pixel-identical to page rows 1005-2184"}
manifest_check: "PASS: all 12 files match MANIFEST pixel size and full sha256 (sha256sum); all 8 part images are numpy array_equal to the stated row ranges of their -page image (all RGB)."
boundaries:
  precedes: "end of FG-CONS.3.18 on p. 75, body lines 1-13 above the heading: '... e andò molto renitente a fare la giornata con / Asdrubale, ancora che avessi detto prima volerla sollecitare⟨∅|.⟩' (no inked stop visible, faint ghost only)"
  heading_page_line: "p. 75, below body line 13 of the preceding unit, ink rows 1044-1073 (heading), rubric rows 1116-1145 and 1155-1183; body begins at row 1233"
  body_first_words: "La severità, nuda di ogni umanità o ⟨voghamo|vogliamo⟩ dire (p. 75, l. 1)"
  body_last_words: "s' ha a presupporre, non può fare che non sia temuto. (p. 77, l. 29, end of page text; p. 77 lower half blank)"
  follows: "p. 78: heading 'CONSIDERAZIONE SUL CAPITOLO XXIV⟨.|∅⟩' (small caps), rubric 'La prolungazione degl' ⟨imperii|imperil⟩ ⟨fece|feco⟩ serva Roma.', body opens 'Non è dubio che la prorogazione degli imperii fu occa-'"
headings_printed:
  heading: "CONSIDERAZIONE SUL CAPITOLO XIX⟨.|∅⟩ -- one line, centred, caps and small caps (C of Considerazione and C of Capitolo full capitals, rest small caps; XIX full capitals). 'del Libro ...' is NOT printed. Final stop: doubtful -- only a pale grey dot (darkest value 164, above the 128 ink threshold) in stop position after XIX; preferred reading: a weak stop, alternative nothing."
  rubric: "'Se a reggere una ⟨mollitudine|moltitudine⟩ è più necessario lo ossequio / che la pena⟨∅|.⟩' -- two centred lines in smaller roman (not italic); no inked final stop, only a faint ghost after 'pena'."
running_heads_etc: {p75: "running head 'SUI DISCORSI DEL MACHIAVELLI' (small caps, centred), page number '75' at right; no signature or catchword; foot: footnote rule + 1 footnote; stray grey band with small marks at bottom right (scan artefact)", p76: "page number '76' at left, running head 'CONSIDERAZIONI' (small caps, centred); no signature or catchword; a long thin vertical line in the right margin c. x 1355, rows c. 470-1520 (scan artefact); small black dot at foot centre c. (680,2125); faint 'Digitized by Google'-type watermark fragment bottom right", p77: "running head 'SUI DISCORSI DEL MACHIAVELLI', page number '77' at right; no footnotes, signature or catchword; stray low mark between 'sia' and 'da' in l. 1 (looks like an underscore) and a faint dot below 'legittimi' l. 22; grey band with marks bottom right (scan artefact); lower part of page blank after l. 29", p78: "page number '78' at left, running head 'CONSIDERAZIONI'; heading of next unit; 1 footnote; small mark in left margin beside body l. 8 ('principale'); Google watermark fragment bottom right"}
footnotes: "Three footnotes on pp. 75-78, each numbered (1) and set below a rule. p. 75 fn (1): call after 'Salinatore,' in body line 4 of the preceding unit -- keyed to FG-CONS.3.18, not this unit. p. 76 fn (1): call '(1)' after 'il timore.' in body l. 6 of p. 76 -- keyed to THIS unit (FG-CONS.3.19); transcribed in full below. p. 77: no footnote. p. 78 fn (1): call after 'tirannidi.' in the body of the following unit -- keyed to FG-CONS.3.24, not this unit. All three transcribed below."
paragraphing: "Left ink edge (first column with pixel <128, columns 0-1299) per body line. p. 75 (rows 1233-1708): l.1 173; ll.2-10 116,116,115,116,117,116,114,120,116 -> l.1 indented ~57 px. Heading left edge 305 (centred), rubric lines 201 and 501 (centred). p. 76 (27 lines): 323,323,323,321,319,319,319,321,319,319,319,319,319,321,319,319,318,317,317,317,315,317,317,315,319,315,317 -> no indented line (gradual 323->315 drift is page skew); l.27 'insolenti' ends at x 445 (short line: paragraph end). p. 77 (29 lines): l.1 194; ll.2-29 133,133,133,134,135,134,135,133,133,133,133,132,136,134,134,135,135,135,136,133,134,135,135,135,136,136,136,136 -> l.1 indented ~60 px (new paragraph 'L' altra distinzione'); l.29 ends x 1004 (unit end). So the unit has two paragraphs: p.75 l.1 - p.76 l.27; p.77 l.1 - p.77 l.29."
line_numbering: "no printed line numbers; lines counted per page from the first body line of the unit on that page (p.75: 10 lines, p.76: 27, p.77: 29 = 66 lines)"
body_word_count: 641
words_per_page: {p75: 93, p76: 251, p77: 297}
word_count_method: "Python script over the transcription below: preferred reading of every doubt (∅ dropped), footnote call removed; split after every apostrophe; whitespace tokens; only tokens containing a letter; a hyphenated word counted once, on the line/page where it begins (first token of the line after a line-end hyphen dropped). Heading, rubric, running heads, footnotes excluded."
uncertain_loci_per_page: {p75: 21, p76: 44, p77: 16, p78: 12, breakdown: "unit body 58 (p75 14, p76 28, p77 16); unit heading+rubric 3 (p75); unit footnote p.76 16; neighbours' text and footnotes 16 (p75: 3 in fn to 3.18 + 1 in 'precedes'; p78: 3 in heading/rubric of 3.24 + 9 in fn to 3.24)"}
uncertain_loci_total: 93
conventions: "Diplomatic, line for line. ⟨preferred|alternative⟩ marks every doubt; preferred = what the shape of the printed sort shows, alternative = other reading considered (∅ = nothing printed); where sense favours the alternative the 'why' column says so. Many sorts in this scan are broken in recurrent ways (h with closed bowl reading b; u reading n; final e reading c or o; t without crossbar reading l); each such instance is marked. i-dots lost in the scan (dotless-looking i) are NOT recorded as doubts where no other letter is plausible. Spaces before ; and : and after apostrophes recorded only where a clear gap is visible. Accents as printed (grave throughout). Footnote call rendered ⁽¹⁾. Italic marked *...* (only in the footnotes). Line-end hyphens kept. Neighbours' footnotes transcribed for completeness with doubts marked."
paths_written: ["/root/p38/readers/fgA/out/FG-CONS.3.19-passA.md", "/root/p38/readers/fgA/work/ (crop.py, lines.py, count.py, body.txt, loci.md, crop PNGs)"]
---

# Body

CONSIDERAZIONE SUL CAPITOLO XIX⟨.|∅⟩
(heading in caps and small caps: Considerazione sul Capitolo XIX)

Se a reggere una ⟨mollitudine|moltitudine⟩ è più necessario lo ossequio
che la pena⟨∅|.⟩

[p. 75]
La severità, nuda di ogni umanità o ⟨voghamo|vogliamo⟩ dire
⟨piacevolczza|piacevolezza⟩, è inutile in chi regge altri ; la umanità o
vero piacevolezza non accompagnata da ⟨qualchc|qualche⟩ severità
è il medesimo ; l' una condita ⟨equalmentc|equalmente⟩ con l' altra sa-
⟨rehbe|rebbe⟩ preziosissima, e sarebbe quella armonia ⟨temporata|temperata⟩
⟨chc|che⟩ è ⟨anaviasima|suavissima⟩ e ammirabile⟨∅|.⟩ Ma perchè questo condi-
mento o rare volte o non mai si truova in ⟨nomo|uomo⟩ alcuno;
essendo così lo ordine della natura che ⟨tntte|tutte⟩ le cose no-
stre ⟨ahhino|abbino⟩ qualche imperfezione, anzi pare ⟨chc|che⟩ ciascuno
o ⟨ahbia|abbia⟩ più del severo che del piacevole, o più del piace-
[p. 76]
vole ⟨cbe|che⟩ del severo ; non sanza cagione ⟨sl|si⟩ dubita ⟨qualc|quale⟩
sia più a proposito, o ⟨cbi|chi⟩ participando dell' uno e dell⟨'|∅⟩ al-
tro ha più del severo, o vero chi ha più dello umano, in-
tendendo però di coloro che hanno tanto dell' uno e del-
l' altro, che dove abbonda il timore non ⟨mancbi|manchi⟩ ⟨l|l'⟩ amore,
e dove abbonda l'amore non ⟨mancbi|manchi⟩ il timore.⁽¹⁾ Circa a che
la prima ⟨disfinzione|distinzione⟩ che mi occorre è considerare la na-
tura di chi tu reggi ⟨;|,⟩ perchè alcuni sono di ingegno sì no-
bile e generoso che ⟨piu|più⟩ volentieri vanno con la piacevo-
lezza ⟨cbe|che⟩ col timore ⟨;|,⟩ altri pel contrario ⟨piem|pieni⟩ di una
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
nità , ⟨pei|pel⟩ contrario ⟨gl|gl'⟩ Italiani, più trattabili, ⟨più|piu⟩ gentili, e
di natura ⟨cbe|che⟩ la asperità più presto gli sdegnava ⟨cbe|che⟩ spa-
ventava. Però a questi essere necessario perdonare tal-
volta e delitti, e procedere con benignità ⟨;|,⟩ quelli altri pu-
nirli severamente, perchè altrimenti diventerebbono ⟨più|piu⟩
insolenti⟨∅|.⟩
[p. 77]
L' altra distinzione che mi occorre è che sia da fare
differenza da uno che regga come ⟨principo|principe⟩ e con ⟨antorità|autorità⟩
propria, da chi regge come ministro e in nome di altri ;
perchè io credo che uno principe ⟨abhia|abbia⟩ a avere rispetto
assai di cercare la benevolenza de' populi, potendo occor-
rere molti casi ⟨cbe|che⟩ a conservare lo Stato gli sia bisogno
amore estraordinario ⟨de'|de⟩ populi. Ma in chi comanda in
nome di altri ⟨distingnerei|distinguerei⟩ : o in uno esercito, e allora fussi
più necessario abbondare nello amore che nel timore,
perchè avendoli a condurre a fazioni pericolose per la
città loro, vi si conducono assai con lo amore ; ma in chi
governa città o provincie in nome di altri, non gli toc-
cando altro che la cura temporale, e non essendo lui il
signore supremo per il quale e populi s' ⟨abhino|abbino⟩ a muovere
a più di ⟨qnello|quello⟩ che ordinariamente sono ⟨tennti|tenuti⟩, credo con-
duca meglio le cose sue con qualche più terrore ⟨cbe|che⟩ e
principi ordinarii : perchè sapendo e populi che le genti
dependono da altri, e che di qui a qualche tempo lui non
ha a ⟨restaro|restare⟩ in ufficio, non può la benevolenza, che loro
gli portassino, ⟨faro|fare⟩ fondamento notabile a quelli effetti per
e ⟨qnali|quali⟩ si desidera tanto lo amore verso il ⟨principo|principe⟩. Dico
però che parlando noi de'governi buoni e legittimi, si può
male presupporre che dove è timore non sia anche amore ⟨;|,⟩
perchè la severità della giustizia, che è quella che reca il
timore, non può essere che non sia amata da chi vuole
bene vivere ⟨;|,⟩ ed e converso lo amore che nasce da uma-
nità, da facilità di natura, e da inclinazione a fare grazie,
accompagnato dalla giustizia, come in uno governo buono
s' ha a presupporre, non può fare che non sia temuto.

# Footnotes on the page

p. 76, call (1) after "il timore." (body p. 76 l. 6) -- keyed to THIS unit (FG-CONS.3.19):

(1) Il ⟨Machiavelh|Machiavelli⟩ opina essere miglior ⟨consigho|consiglio⟩ per governare una
⟨mollitudine|moltitudine⟩ mostrarsi ⟨umauo|umano⟩ ⟨piultosto|piuttosto⟩ che superbo, pietoso ⟨piultosto|piuttosto⟩
⟨cha|che⟩ crudele, contro la nota sentenza di Tacito⟨:|∅⟩ *in multitudine regenda*
*plus ⟨pœna|pæna⟩ quam obsequium valet.* Però avverte nello ⟨slesso|stesso⟩ tempo che
dovendo comandare a' sudditi, ⟨affinchè|affinche⟩ ⟨nou|non⟩ ⟨doventino|diventino⟩ insolenti, si deb-
ba ricorrere ⟨puittosto|piuttosto⟩ alla ⟨peua|pena⟩ che all' ossequio⟨∅|.⟩

p. 75, call (1) after "Salinatore," (body of preceding unit, 4th line of p. 75) -- keyed to FG-CONS.3.18, not this unit:

(1) È lo ⟨slesso|stesso⟩ Marco Livio, di soprannome ⟨Sailnatore|Salinatore⟩, eletto con-
sole insieme con Claudio Nerone⟨∅|.⟩

p. 78, call (1) after "tirannidi." (body of following unit) -- keyed to FG-CONS.3.24, not this unit:

(1) Due sono le cagioni che secondo il Machiavelli prepararono la
caduta della repubblica⟨:|∅⟩ le contenzioni che ⟨nacquero|uacquero⟩ dalla legge agra-
ria e la prolungazione del comando degli eserciti⟨.|∅⟩ Quest'ultima produce
sempre due inconvenienti⟨:|∅⟩ l' uno che minor numero di ⟨uomini|uemini⟩ si eser-
citano negli imperii, e si viene per questo a ristringere la riputazione in
pochi ⟨,|;⟩ ⟨l|l'⟩altro che chi rimane lungo tempo a comandare l' esercito, lo
⟨guadagna|guadagııa⟩, e lo rende suo partigiano ⟨∅|.⟩  (an isolated stop stands c. 70 px to the right of 'partigiano')

# Uncertain loci

| n | page | line | printed context | ⟨preferred\|alternative⟩ | why |
|---|---|---|---|---|---|
| 1 | 75 | heading | CAPITOLO XIX⟨.\|∅⟩ | ⟨.\|∅⟩ | a pale grey dot in stop position after XIX (min. value 164, i.e. lighter than ink threshold 128); may be a weakly inked stop or a smudge |
| 2 | 75 | rubric l. 1 | Se a reggere una ⟨mollitudine\|moltitudine⟩ | ⟨mollitudine\|moltitudine⟩ | fourth letter has no crossbar, reads l; sense favours moltitudine |
| 3 | 75 | rubric l. 2 | che la pena⟨∅\|.⟩ | ⟨∅\|.⟩ | only a faint grey ghost (values 154-201) after pena; no inked stop |
| 4 | 75 | 1 | di ogni umanità o ⟨voghamo\|vogliamo⟩ dire | ⟨voghamo\|vogliamo⟩ | l+i fused/broken, look like h; sense vogliamo |
| 5 | 75 | 2 | ⟨piacevolczza\|piacevolezza⟩, è inutile | ⟨piacevolczza\|piacevolezza⟩ | e after l lacks bar, reads c; sense piacevolezza |
| 6 | 75 | 3 | n accompagnata da ⟨qualchc\|qualche⟩ severità | ⟨qualchc\|qualche⟩ | final e reads c; sense qualche |
| 7 | 75 | 4 | ; l' una condita ⟨equalmentc\|equalmente⟩ con l' altr | ⟨equalmentc\|equalmente⟩ | final e reads c; also q/g not fully clear (q preferred, g would give egualmente) |
| 8 | 75 | 5 | ⟨rehbe\|rebbe⟩ preziosissi | ⟨rehbe\|rebbe⟩ | first b open, reads h; sense (sa-)rebbe |
| 9 | 75 | 5 | be quella armonia ⟨temporata\|temperata⟩ | ⟨temporata\|temperata⟩ | second vowel looks o; sense (armonia) temperata |
| 10 | 75 | 6 | ⟨chc\|che⟩ è ⟨anaviasi | ⟨chc\|che⟩ | final e lacks its bar, reads c; sense che |
| 11 | 75 | 6 | ⟨chc\|che⟩ è ⟨anaviasima\|suavissima⟩ e ammirabil | ⟨anaviasima\|suavissima⟩ | s broken to a-shape, u to n-shape, second s to a-shape; letter count fits suavissima, which sense favours |
| 12 | 75 | 6 | sima⟩ e ammirabile⟨∅\|.⟩ Ma perchè q | ⟨∅\|.⟩ | no full-strength mark; at most a faint grey ghost in stop position; sense expects a full stop |
| 13 | 75 | 7 | mai si truova in ⟨nomo\|uomo⟩ alcuno; | ⟨nomo\|uomo⟩ | u reads n (open bottom broken); sense uomo |
| 14 | 75 | 8 | della natura che ⟨tntte\|tutte⟩ le cose no- | ⟨tntte\|tutte⟩ | u reads n; sense tutte |
| 15 | 75 | 9 | stre ⟨ahhino\|abbino⟩ qualche imp | ⟨ahhino\|abbino⟩ | both b's read h; sense abbino |
| 16 | 75 | 9 | ezione, anzi pare ⟨chc\|che⟩ ciascuno | ⟨chc\|che⟩ | final e lacks its bar, reads c; sense che |
| 17 | 75 | 10 | o ⟨ahbia\|abbia⟩ più del sev | ⟨ahbia\|abbia⟩ | first b reads h; sense abbia |
| 18 | 76 | 1 | vole ⟨cbe\|che⟩ del severo | ⟨cbe\|che⟩ | bowl of h closed so the sort reads as b (recurring breakage); sense requires che |
| 19 | 76 | 1 | non sanza cagione ⟨sl\|si⟩ dubita ⟨qua | ⟨sl\|si⟩ | i dot missing and stem tall, reads l; sense si |
| 20 | 76 | 1 | ne ⟨sl\|si⟩ dubita ⟨qualc\|quale⟩ | ⟨qualc\|quale⟩ | final e reads c; sense quale |
| 21 | 76 | 2 | iù a proposito, o ⟨cbi\|chi⟩ participand | ⟨cbi\|chi⟩ | h reads as b (closed bowl); sense chi |
| 22 | 76 | 2 | o dell' uno e dell⟨'\|∅⟩ al- | ⟨'\|∅⟩ | apostrophe after dell damaged, only a faint fragment; sense requires it |
| 23 | 76 | 5 | nda il timore non ⟨mancbi\|manchi⟩ ⟨l\|l'⟩ amor | ⟨mancbi\|manchi⟩ | h reads as b; sense manchi |
| 24 | 76 | 5 | n ⟨mancbi\|manchi⟩ ⟨l\|l'⟩ amore, | ⟨l\|l'⟩ | no apostrophe visible after l; sense l'amore |
| 25 | 76 | 6 | bonda l'amore non ⟨mancbi\|manchi⟩ il timore.⁽ | ⟨mancbi\|manchi⟩ | h reads as b; sense manchi |
| 26 | 76 | 7 | la prima ⟨disfinzione\|distinzione⟩ che mi occo | ⟨disfinzione\|distinzione⟩ | t broken to f-like shape; sense distinzione |
| 27 | 76 | 8 | a di chi tu reggi ⟨;\|,⟩ perchè alcu | ⟨;\|,⟩ | upper dot of semicolon faint/broken; lower part visible as comma |
| 28 | 76 | 9 | le e generoso che ⟨piu\|più⟩ volentieri | ⟨piu\|più⟩ | no accent visible over u; sense/usage più |
| 29 | 76 | 10 | lezza ⟨cbe\|che⟩ col timore | ⟨cbe\|che⟩ | bowl of h closed so the sort reads as b (recurring breakage); sense requires che |
| 30 | 76 | 10 | e\|che⟩ col timore ⟨;\|,⟩ altri pel c | ⟨;\|,⟩ | upper dot of semicolon faint/broken; lower part visible as comma |
| 31 | 76 | 10 | tri pel contrario ⟨piem\|pieni⟩ di una | ⟨piem\|pieni⟩ | n+i run together read m; sense pieni |
| 32 | 76 | 12 | ma ⟨bisogns\|bisogna⟩ domargli e | ⟨bisogns\|bisogna⟩ | final a reads s; sense bisogna |
| 33 | 76 | 13 | dubio ⟨cbe\|che⟩ con questi | ⟨cbe\|che⟩ | bowl of h closed so the sort reads as b (recurring breakage); sense requires che |
| 34 | 76 | 14 | condizioni ; e a ⟨qnesto\|questo⟩ proposito d | ⟨qnesto\|questo⟩ | u reads n; sense questo |
| 35 | 76 | 18 | ⟨vìrtù\|virtù⟩, erano e Ge | ⟨vìrtù\|virtù⟩ | mark over i looks like an accent rather than a round dot; normal form virtù |
| 36 | 76 | 20 | nti, e di qualità ⟨cbe\|che⟩ la dolcezza | ⟨cbe\|che⟩ | bowl of h closed so the sort reads as b (recurring breakage); sense requires che |
| 37 | 76 | 21 | , la attribuivano ⟨piu\|più⟩ presto a ti | ⟨piu\|più⟩ | no accent visible over u; sense/usage più |
| 38 | 76 | 22 | nità , ⟨pei\|pel⟩ contrario ⟨ | ⟨pei\|pel⟩ | letter after e shows a dot like i; sense pel (cf. 'pel contrario' p. 76 l. 10) |
| 39 | 76 | 22 | ei\|pel⟩ contrario ⟨gl\|gl'⟩ Italiani, p | ⟨gl\|gl'⟩ | no clear apostrophe after gl (gap only, faint trace); cf. gl' Italiani l. 18 |
| 40 | 76 | 22 | , più trattabili, ⟨più\|piu⟩ gentili, e | ⟨più\|piu⟩ | accent faint but a trace visible |
| 41 | 76 | 23 | di natura ⟨cbe\|che⟩ la asperità | ⟨cbe\|che⟩ | bowl of h closed so the sort reads as b (recurring breakage); sense requires che |
| 42 | 76 | 23 | esto gli sdegnava ⟨cbe\|che⟩ spa- | ⟨cbe\|che⟩ | bowl of h closed so the sort reads as b (recurring breakage); sense requires che |
| 43 | 76 | 25 | ere con benignità ⟨;\|,⟩ quelli altr | ⟨;\|,⟩ | upper dot of semicolon faint/broken; lower part visible as comma |
| 44 | 76 | 26 | ti diventerebbono ⟨più\|piu⟩ | ⟨più\|piu⟩ | accent faint but a trace visible |
| 45 | 76 | 27 | insolenti⟨∅\|.⟩ | ⟨∅\|.⟩ | no full-strength mark; at most a faint grey ghost in stop position; sense expects a full stop |
| 46 | 77 | 2 | no che regga come ⟨principo\|principe⟩ e con ⟨anto | ⟨principo\|principe⟩ | final e reads o; sense principe |
| 47 | 77 | 2 | o\|principe⟩ e con ⟨antorità\|autorità⟩ | ⟨antorità\|autorità⟩ | u reads n; sense autorità |
| 48 | 77 | 4 | che uno principe ⟨abhia\|abbia⟩ a avere ris | ⟨abhia\|abbia⟩ | second b reads h; sense abbia |
| 49 | 77 | 6 | rere molti casi ⟨cbe\|che⟩ a conservar | ⟨cbe\|che⟩ | bowl of h closed so the sort reads as b (recurring breakage); sense requires che |
| 50 | 77 | 7 | re estraordinario ⟨de'\|de⟩ populi. Ma | ⟨de'\|de⟩ | apostrophe very faint, slightly displaced; sense de' |
| 51 | 77 | 8 | nome di altri ⟨distingnerei\|distinguerei⟩ : o in uno | ⟨distingnerei\|distinguerei⟩ | u reads n; sense distinguerei |
| 52 | 77 | 14 | quale e populi s' ⟨abhino\|abbino⟩ a muovere | ⟨abhino\|abbino⟩ | second b reads h; sense abbino |
| 53 | 77 | 15 | a più di ⟨qnello\|quello⟩ che ordinar | ⟨qnello\|quello⟩ | u reads n; sense quello |
| 54 | 77 | 15 | dinariamente sono ⟨tennti\|tenuti⟩, credo con- | ⟨tennti\|tenuti⟩ | u reads n; sense tenuti |
| 55 | 77 | 16 | alche più terrore ⟨cbe\|che⟩ e | ⟨cbe\|che⟩ | bowl of h closed so the sort reads as b (recurring breakage); sense requires che |
| 56 | 77 | 19 | ha a ⟨restaro\|restare⟩ in ufficio, | ⟨restaro\|restare⟩ | final e reads o; sense restare |
| 57 | 77 | 20 | gli portassino, ⟨faro\|fare⟩ fondamento | ⟨faro\|fare⟩ | final e reads o; sense fare |
| 58 | 77 | 21 | e ⟨qnali\|quali⟩ si desidera | ⟨qnali\|quali⟩ | u reads n; sense quali |
| 59 | 77 | 21 | lo amore verso il ⟨principo\|principe⟩. Dico | ⟨principo\|principe⟩ | final e reads o; sense principe |
| 60 | 77 | 23 | n sia anche amore ⟨;\|,⟩ | ⟨;\|,⟩ | upper dot of semicolon faint/broken; lower part visible as comma |
| 61 | 77 | 26 | bene vivere ⟨;\|,⟩ ed e conver | ⟨;\|,⟩ | upper dot of semicolon faint/broken; lower part visible as comma |
| 62 | 76 | fn(1) l. 1 | Il ⟨Machiavelh\|Machiavelli⟩ opina | ⟨Machiavelh\|Machiavelli⟩ | final li broken to h-shape; sense Machiavelli |
| 63 | 76 | fn(1) l. 1 | miglior ⟨consigho\|consiglio⟩ | ⟨consigho\|consiglio⟩ | li reads h; sense consiglio |
| 64 | 76 | fn(1) l. 2 | ⟨mollitudine\|moltitudine⟩ mostrarsi | ⟨mollitudine\|moltitudine⟩ | t without crossbar reads l; sense moltitudine |
| 65 | 76 | fn(1) l. 2 | mostrarsi ⟨umauo\|umano⟩ | ⟨umauo\|umano⟩ | n reads u; sense umano |
| 66 | 76 | fn(1) l. 2 | ⟨piultosto\|piuttosto⟩ che superbo | ⟨piultosto\|piuttosto⟩ | first t reads l; sense piuttosto |
| 67 | 76 | fn(1) l. 2 | pietoso ⟨piultosto\|piuttosto⟩ | ⟨piultosto\|piuttosto⟩ | first t reads l; sense piuttosto |
| 68 | 76 | fn(1) l. 3 | ⟨cha\|che⟩ crudele | ⟨cha\|che⟩ | e reads a; sense che |
| 69 | 76 | fn(1) l. 3 | di Tacito⟨:\|∅⟩ in | ⟨:\|∅⟩ | faint broken mark after Tacito, colon preferred |
| 70 | 76 | fn(1) l. 4 | plus ⟨pœna\|pæna⟩ quam | ⟨pœna\|pæna⟩ | italic ligature, œ vs æ not distinguishable with certainty |
| 71 | 76 | fn(1) l. 4 | nello ⟨slesso\|stesso⟩ tempo | ⟨slesso\|stesso⟩ | t reads l; sense stesso |
| 72 | 76 | fn(1) l. 5 | ⟨affinchè\|affinche⟩ ⟨nou\|non⟩ | ⟨affinchè\|affinche⟩ | accent over final e not clearly visible |
| 73 | 76 | fn(1) l. 5 | affinchè ⟨nou\|non⟩ ⟨doventino\|diventino⟩ | ⟨nou\|non⟩ | n reads u; sense non |
| 74 | 76 | fn(1) l. 5 | ⟨doventino\|diventino⟩ insolenti | ⟨doventino\|diventino⟩ | second letter looks o; sense/usage diventino |
| 75 | 76 | fn(1) l. 6 | ricorrere ⟨puittosto\|piuttosto⟩ | ⟨puittosto\|piuttosto⟩ | i/u order unclear from broken sorts; sense piuttosto |
| 76 | 76 | fn(1) l. 6 | alla ⟨peua\|pena⟩ che | ⟨peua\|pena⟩ | n reads u; sense pena |
| 77 | 76 | fn(1) l. 6 | all' ossequio⟨∅\|.⟩ | ⟨∅\|.⟩ | no stop visible |
| 78 | 75 | fn(1) [3.18] l. 1 | lo ⟨slesso\|stesso⟩ Marco | ⟨slesso\|stesso⟩ | t reads l; sense stesso |
| 79 | 75 | fn(1) [3.18] l. 1 | soprannome ⟨Sailnatore\|Salinatore⟩ | ⟨Sailnatore\|Salinatore⟩ | l and i transposed in appearance; sense Salinatore (body has Salinatore) |
| 80 | 75 | fn(1) [3.18] l. 2 | Claudio Nerone⟨∅\|.⟩ | ⟨∅\|.⟩ | no stop visible |
| 81 | 75 | precedes, last line | volerla sollecitare⟨∅\|.⟩ | ⟨∅\|.⟩ | only faint grey after sollecitare; sense expects stop (end of unit 3.18) |
| 82 | 78 | heading [3.24] | CAPITOLO XXIV⟨.\|∅⟩ | ⟨.\|∅⟩ | pale mark in stop position |
| 83 | 78 | rubric [3.24] | degl' ⟨imperii\|imperil⟩ | ⟨imperii\|imperil⟩ | last i looks like l; sense imperii |
| 84 | 78 | rubric [3.24] | ⟨fece\|feco⟩ serva Roma. | ⟨fece\|feco⟩ | final e looks o; sense fece |
| 85 | 78 | fn(1) [3.24] l. 2 | della repubblica⟨:\|∅⟩ le | ⟨:\|∅⟩ | faint grey mark after repubblica |
| 86 | 78 | fn(1) [3.24] l. 2 | che ⟨nacquero\|uacquero⟩ | ⟨nacquero\|uacquero⟩ | n reads u |
| 87 | 78 | fn(1) [3.24] l. 3 | degli eserciti⟨.\|∅⟩ Quest'ultima | ⟨.\|∅⟩ | faint grey mark after eserciti; capital follows |
| 88 | 78 | fn(1) [3.24] l. 4 | inconvenienti⟨:\|∅⟩ l' uno | ⟨:\|∅⟩ | faint grey block after inconvenienti |
| 89 | 78 | fn(1) [3.24] l. 4 | di ⟨uomini\|uemini⟩ | ⟨uomini\|uemini⟩ | second letter looks e |
| 90 | 78 | fn(1) [3.24] l. 6 | pochi ⟨,\|;⟩ | ⟨,\|;⟩ | only lower comma part visible |
| 91 | 78 | fn(1) [3.24] l. 6 | ⟨l\|l'⟩altro | ⟨l\|l'⟩ | no clear apostrophe |
| 92 | 78 | fn(1) [3.24] l. 7 | lo ⟨guadagna\|guadagııa⟩ | ⟨guadagna\|guadagııa⟩ | n broken into two strokes |
| 93 | 78 | fn(1) [3.24] l. 7 | partigiano ⟨∅\|.⟩ | ⟨∅\|.⟩ | a stop stands isolated ~70 px to the right of partigiano (displaced sort or stray dot) |
