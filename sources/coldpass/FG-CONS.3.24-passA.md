---
unit: FG-CONS.3.24 (Considerazione sul Capitolo XXIV)
reader: "cold reader fgA (Pass A, full)"
source: "Guicciardini, Considerazioni intorno ai Discorsi del Machiavelli, in Opere inedite di Francesco Guicciardini, vol. 1, ed. Giuseppe Canestrini (Florence, Barbera, Bianchi e Comp., 1857), pp. 78-79 (p. 80 boundary evidence)"
witness_images:
  - {file: 1857-p78-page.png, size: 1367x2184, rows: 0-2184, sha256_16: ed1d70392715c6f7, check: "size+sha256 match manifest"}
  - {file: 1857-p78-part1of2-y0-1179.png, size: 1367x1179, rows: 0-1179, sha256_16: b8a662571b5b9048, check: "size+sha256 match; array_equal page rows 0-1179 True"}
  - {file: 1857-p78-part2of2-y1005-2184.png, size: 1367x1179, rows: 1005-2184, sha256_16: 7f4f658689d9559c, check: "size+sha256 match; array_equal page rows 1005-2184 True"}
  - {file: 1857-p79-page.png, size: 1367x2200, rows: 0-2200, sha256_16: 8ecd3562c44f8971, check: "size+sha256 match manifest"}
  - {file: 1857-p79-part1of2-y0-1188.png, size: 1367x1188, rows: 0-1188, sha256_16: c249453c43a50b67, check: "size+sha256 match; array_equal page rows 0-1188 True"}
  - {file: 1857-p79-part2of2-y1012-2200.png, size: 1367x1188, rows: 1012-2200, sha256_16: 2ef49a5af8839db4, check: "size+sha256 match; array_equal page rows 1012-2200 True"}
  - {file: 1857-p80-page.png, size: 1367x2184, rows: 0-2184, sha256_16: 46645f1ae0107e9c, check: "size+sha256 match manifest"}
  - {file: 1857-p80-part1of2-y0-1179.png, size: 1367x1179, rows: 0-1179, sha256_16: bd292dbdc465eebf, check: "size+sha256 match; array_equal page rows 0-1179 True"}
  - {file: 1857-p80-part2of2-y1005-2184.png, size: 1367x1179, rows: 1005-2184, sha256_16: 4202059b5e0be905, check: "size+sha256 match; array_equal page rows 1005-2184 True"}
manifest_check: "PASS - all 9 images match MANIFEST.txt pixel size and full sha256; all 6 part images pixel-identical (numpy array_equal) to the stated rows of their -page image. Note: images are RGB mode."
boundaries:
  precedes: "Not visible in the supplied images: p. 78 opens with running head '78 CONSIDERAZIONI' and then directly the heading of this unit; the preceding unit (presumably the Considerazione on cap. XXIII) ends on p. 77, which is not supplied."
  heading_page_line: "p. 78, first line below running head (ink rows 321-350); rubric at rows 417-447"
  body_first_words: "Non è dubio che la prorogazione"
  body_last_words: "nè facultà di travagliarla per altra via."
  follows: "p. 79: body ends at line 12 (rows 789-826); blank space, a short centred rule at ca. y 1055, rest of page blank (stray specks). p. 80: half-title 'RICORDI POLITICI E CIVILI.' alone on the page - the Considerazioni end with this unit in this volume's sequence."
headings_printed:
  heading: "CONSIDERAZIONE SUL CAPITOLO XXIV⟨.|∅⟩ (caps and small caps: Considerazione sul Capitolo XXIV)"
  rubric: "La prolungazione degl' ⟨imperii|imperil⟩ ⟨fece|feco⟩ serva Roma."
running_heads_etc: "p. 78: '78' at left, 'CONSIDERAZIONI' centred. p. 79: 'SUI DISCORSI DEL MACHIAVELLI.' centred, '79' at right. p. 80: no running head or folio (half-title). Scan artifacts: vertical rule-like mark in right margin of p. 78 (x~1330-1342, y~550-1320); a speck at left margin of p. 78 body line 7 (x 269-273, rows 792-797); grey 'Google'-type watermark traces lower right on all pages; short rule on p. 79 at ca. y 1055 and specks on p. 79-80."
footnotes: "One footnote on p. 78, call ⁽1⁾ after 'tirannidi.' in body p. 78 line 11 (call shape reads like '[11'/'111'), keyed to this unit; 7 lines below a full-measure rule (rows 1545-1550). No footnotes on p. 79 or p. 80."
paragraphing: "Left ink edge (first column with >=3 pixels darker than 128 in the line band; raw first-dark column also reported). p. 78 body line 1: 357 (raw 355) - INDENTED ~62 px; lines 2-21: 295-299 (line 7 raw 269 is a separate margin speck at x 269-273, rows 792-797; text edge 295). p. 79 lines 1-12: 134-140, none indented (line 12 is the short last line, right edge 755). Result: one paragraph, indented first line only; no paragraph break on p. 79."
line_numbering: "Body lines numbered per page from 1: p. 78 lines 1-21, p. 79 lines 1-12. Heading and rubric counted separately (H, R). Footnote lines numbered fn1-fn7."
body_word_count: 318
words_per_page: {"78": 202, "79": 116}
word_count_method: "Python script work/scripts/count.py on work/body.txt: preferred reading of each doubt; footnote call removed; whitespace tokens split after every apostrophe; only tokens containing a letter; hyphenated line-end word counted once on the line/page where it begins; heading, rubric, running heads, notes excluded."
uncertain_loci_per_page: {"78 (heading+rubric)": 3, "78 body": 16, "78 footnote": 16, "79 body": 6}
uncertain_loci_total: 41
conventions: "Diplomatic, line for line; line-end hyphens kept; accents, capitals, punctuation as printed; apostrophe as ' (no space recorded after apostrophes in the body: gaps are narrow; rubric degl' shows a clear gap and is recorded with space); italic none found; ⟨preferred|alternative⟩ for every doubt, ∅ = nothing printed; [p. N] page change. Dotless i (lost dot of i, very frequent: dubıo, deglı, costumı, ...) is transcribed i silently where no other letter is in question; it is marked only where the broken shape reads as another letter (e.g. ii as u in 'imperu'). Footnote call rendered ⁽1⁾."
paths_written:
  - /root/p39/readers/fgA/out/FG-CONS.3.24-passA.md
  - /root/p39/readers/fgA/work/body.txt
  - /root/p39/readers/fgA/work/scripts/snip.py
  - /root/p39/readers/fgA/work/scripts/edges.py
  - /root/p39/readers/fgA/work/scripts/count.py
  - /root/p39/readers/fgA/work/*.png (crops)
---

# Body

CONSIDERAZIONE SUL CAPITOLO XXIV⟨.|∅⟩

La prolungazione degl' ⟨imperii|imperil⟩ ⟨fece|feco⟩ serva Roma.

[p. 78]
Non è dubio che la prorogazione degli imperii fu occa-
sione grande a chi volle occupare la republica; perchè era
instrumento da farsi amici i soldati e ⟨séguito|seguito⟩ co' re, e nelle
nazioni o provincie forestiere, ⟨e|s⟩ a' capitani accresceva ric-
chezza con la quale potevano corrompere gli ⟨uomini|nomini⟩, come
fece a Cesare il lungo imperio di Gallia⟨.|∅⟩ Ma il fondamento
principale de' mali fu la corruzione della città, la quale da-
tasi alla avarizia, alle delizie, era in modo degenerata da-
gli antichi costumi, che ne nacquono le divisioni sangui-
nose della città, dalle quali sempre ne' populi liberi si viene
alle ⟨tirannidi|tirauuidi⟩.⁽⟨1|11⟩⁾ Di quivi nacque la facilità di corrompere
e cittadini e' soldati, di qui potette sperare uno ⟨Catilina|Catihna⟩
sanza imperio e sanza eserciti occupare la republica, di
qui conjurazione di più potenti di dividersi fra loro gli
⟨imperii|imperu⟩ ⟨e|c⟩ gli eserciti, e con queste forze tenere bassi gli
altri⟨;|,⟩ di qui le prorogazioni estraordinarie degli ⟨imperii|imperu⟩,
come fu quella di ⟨Cesare|Ceaare⟩, al quale non la ⟨utilità|utihtà⟩ della re-
publica, non la necessità della guerra, non la ammirazione
della ⟨sua|aua⟩ virtù, ma la conjurazione con Pompeo ⟨e|o⟩ Crasso
di occupare la republica, fece imperio decemvirale. Non
era ⟨stato|atato⟩ prorogato lo imperio a Silla, quando la prima
[p. 79]
volta venne alle mani con Mario, ma ne fu causa la divi-
sione tra la ⟨nobilità|nobihtà⟩ e la plebe, e avendo la plebe per capo
Mario, fu forzata la nobilità cercarsi uno capo⟨.|∅⟩ Però con-
chiuggo che quando Roma non fu corrotta, le prorogazioni
degli imperii e la continuazione del consulato, la quale
ne' tempi difficili usorono molte volte, furono cosa utile ⟨e|c⟩
santa; ma corrotta la città, sursono le battaglie civili, e
i semi delle tirannidi, etiam sanza la prorogazione degli
⟨imperii|imperu⟩. E però ⟨si|st⟩ può conchiudere, che se non fussino
state anche le prorogazioni, non sarebbe mancato ⟨nè|nc̀⟩ a Ce-
sare nè agli altri che occuporono la republica, nè pensiero
nè facultà di travagliarla per altra via.

# Footnotes on the page

[p. 78] keyed to call ⁽1⁾ in body p. 78 line 11 (after "tirannidi."), this unit:

⁽1⁾ Due sono le ⟨cagioni|cajioni⟩ che secondo il Machiavelli prepararono la
caduta della repubblica⟨:|.⟩ le contenzioni che ⟨nacquero|uacquero⟩ dalla legge agra-
ria e la prolungazione del comando degli eserciti⟨.|∅⟩ Quest'ultima produce
sempre due inconvenienti⟨:|∅⟩ l'uno che minor numero di ⟨uomini|ucmini⟩ si eser-
citano negli ⟨imperii|imperu⟩, e si viene per questo a ristringere la ⟨riputazione|ripulazione⟩ ⟨in|m⟩
⟨pochi|poclu⟩⟨,|;⟩ l'altro ⟨che|clie⟩ ⟨chi|clu⟩ rimane ⟨lungo|liingo⟩ tempo a comandare l'esercito, lo
⟨guadagna|guadagıı⟩, e lo rende suo partigiano⟨.|∅⟩

(No footnotes on p. 79 or p. 80.)

# Uncertain loci

n | page | line | printed context | ⟨preferred\|alternative⟩ | why
---|---|---|---|---|---
1 | 78 | H | CAPITOLO XXIV_ | ⟨.\|∅⟩ | only a faint grey trace at baseline after V (min pixel 112, 6 px <128); may be a broken full stop or nothing
2 | 78 | R | degl' imperil | ⟨imperii\|imperil⟩ | final sort is tall like l; sense (plural imperii, cf. body) prefers ii; shape reads il (non-word)
3 | 78 | R | imperil feco serva | ⟨fece\|feco⟩ | last letter closed like o; sense fece; feco a non-word
4 | 78 | 3 | soldati e séguito co' re | ⟨séguito\|seguito⟩ | an acute mark is visible over the e; transcribed as printed, odd accentuation flagged
5 | 78 | 4 | forestiere, s a' capitani | ⟨e\|s⟩ | broken e reads like s; sense e (conjunction); "s" non-word
6 | 78 | 5 | gli nomini, come | ⟨uomini\|nomini⟩ | u reads n; sense uomini; "nomini" non-word
7 | 78 | 6 | di Gallia_ Ma il | ⟨.\|∅⟩ | faint grey blob after Gallia; capital Ma follows, so a full stop by sense
8 | 78 | 11 | alle tirauuidi. | ⟨tirannidi\|tirauuidi⟩ | nn printed as open shapes reading uu/oo; sense tirannidi (cf. p. 79 l. 9)
9 | 78 | 11 | tirannidi.[11 Di | ⟨⁽1⁾\|11⟩ | footnote call: broken parentheses read as 1/[; footnote below is numbered (1)
10 | 78 | 12-13 | uno Catihna | ⟨Catilina\|Catihna⟩ | li fused reads h; sense Catilina; shape non-word
11 | 78 | 15 | imperu e gli | ⟨imperii\|imperu⟩ | ii without dots joined reads u; sense imperii
12 | 78 | 15 | imperii c gli eserciti | ⟨e\|c⟩ | e partly open; conjunction e by sense
13 | 78 | 16 | altri; di qui | ⟨;\|,⟩ | upper dot weak; shape favours semicolon
14 | 78 | 16 | degli imperu, | ⟨imperii\|imperu⟩ | as 11
15 | 78 | 17 | di Ceaare, al quale | ⟨Cesare\|Ceaare⟩ | s reads a (and e near o: "Cosare"); sense Cesare
16 | 78 | 17 | la utihtà della | ⟨utilità\|utihtà⟩ | li reads h; sense utilità
17 | 78 | 19 | della aua virtù | ⟨sua\|aua⟩ | s reads a; sense sua
18 | 78 | 19 | Pompeo o Crasso | ⟨e\|o⟩ | e reads o (closed eye); different Italian words: e "and" vs o "or"; e preferred by sense (the triumvirate: Pompey and Crassus jointly)
19 | 78 | 21 | era atato prorogato | ⟨stato\|atato⟩ | s reads a; sense stato
20 | 79 | 2 | la nobihtà e la plebe | ⟨nobilità\|nobihtà⟩ | li reads h; sense nobilità (cf. l. 3)
21 | 79 | 3 | uno capo_ Però | ⟨.\|∅⟩ | faint grey trace after capo; capital Però follows
22 | 79 | 6 | cosa utile c | ⟨e\|c⟩ | e reads c (bar lost); sense e
23 | 79 | 9 | imperu. E però | ⟨imperii\|imperu⟩ | as 11
24 | 79 | 9 | E però st può | ⟨si\|st⟩ | broken i with spur reads t; sense si
25 | 79 | 10 | mancato nc̀ a Ce- | ⟨nè\|nc̀⟩ | e of nè reads c; sense nè
26 | 78 | fn1 | le cajioni che | ⟨cagioni\|cajioni⟩ | g blurred/broken; sense cagioni
27 | 78 | fn2 | repubblica_ le contenzioni | ⟨:\|.⟩ | grey blot, no solid ink; colon by sense (enumeration follows, lower-case le)
28 | 78 | fn2 | che uacquero | ⟨nacquero\|uacquero⟩ | n reads as two strokes ıı/u; sense nacquero
29 | 78 | fn3 | eserciti_ Quest'ultima | ⟨.\|∅⟩ | faint mark; capital follows
30 | 78 | fn4 | inconvenienti_ l'uno | ⟨:\|∅⟩ | grey blot only; colon by sense (l'uno ... l'altro enumeration); could be ; or .
31 | 78 | fn4 | di ucmini | ⟨uomini\|ucmini⟩ | o reads c; sense uomini
32 | 78 | fn5 | negli imperu, | ⟨imperii\|imperu⟩ | as 11
33 | 78 | fn5 | la ripulazione | ⟨riputazione\|ripulazione⟩ | t reads l; sense riputazione
34 | 78 | fn5 | riputazione m | ⟨in\|m⟩ | dotless i + n read as m; sense in
35 | 78 | fn6 | poclu , | ⟨pochi\|poclu⟩ | h reads lu (shoulder broken); sense pochi
36 | 78 | fn6 | pochi , l'altro | ⟨,\|;⟩ | spaced comma-like mark; could be a semicolon with lost dot (parallel to "l'uno" clause); shape preferred
37 | 78 | fn6 | clie clu rimane | ⟨che\|clie⟩ | h reads li; sense che
38 | 78 | fn6 | che clu rimane | ⟨chi\|clu⟩ | h reads l + i reads u; sense chi (che vs chi are different words; chi preferred: "chi rimane ... lo guadagna")
39 | 78 | fn6 | rimane liingo tempo | ⟨lungo\|liingo⟩ | u reads ii; sense lungo
40 | 78 | fn7 | suo partigiano   . | ⟨.\|∅⟩ | a dot stands detached far right of the word (x~860, faint, min 66); taken as the displaced full stop
41 | 78 | fn7 | lo guadagıı, e lo | ⟨guadagna\|guadagıı⟩ | final n+a broken into vertical strokes; sense guadagna
