---
unit: FG-CONS.3.24
reader: "cold reader fgB (Pass B, full)"
source: "Guicciardini, Considerazioni intorno ai Discorsi del Machiavelli, in Opere inedite di Francesco Guicciardini, vol. 1, ed. G. Canestrini (Florence, Barbera, Bianchi e Comp., 1857), pp. 78-79 (p. 80 boundary evidence)"
witness_images:
  - {file: 1857-p78-page.png, size: 1367x2184, rows: "0-2184", sha256_16: ed1d70392715c6f7, check: "size+sha256 match"}
  - {file: 1857-p78-part1of2-y0-1179.png, size: 1367x1179, rows: "0-1179", sha256_16: b8a662571b5b9048, check: "size+sha256 match; array_equal page rows 0-1179 True"}
  - {file: 1857-p78-part2of2-y1005-2184.png, size: 1367x1179, rows: "1005-2184", sha256_16: 7f4f658689d9559c, check: "size+sha256 match; array_equal True"}
  - {file: 1857-p79-page.png, size: 1367x2200, rows: "0-2200", sha256_16: 8ecd3562c44f8971, check: "size+sha256 match"}
  - {file: 1857-p79-part1of2-y0-1188.png, size: 1367x1188, rows: "0-1188", sha256_16: c249453c43a50b67, check: "size+sha256 match; array_equal True"}
  - {file: 1857-p79-part2of2-y1012-2200.png, size: 1367x1188, rows: "1012-2200", sha256_16: 2ef49a5af8839db4, check: "size+sha256 match; array_equal True"}
  - {file: 1857-p80-page.png, size: 1367x2184, rows: "0-2184", sha256_16: 46645f1ae0107e9c, check: "size+sha256 match"}
  - {file: 1857-p80-part1of2-y0-1179.png, size: 1367x1179, rows: "0-1179", sha256_16: bd292dbdc465eebf, check: "size+sha256 match; array_equal True"}
  - {file: 1857-p80-part2of2-y1005-2184.png, size: 1367x1179, rows: "1005-2184", sha256_16: 4202059b5e0be905, check: "size+sha256 match; array_equal True"}
manifest_check: "All 9 images match MANIFEST.txt in pixel size and full sha256; all 6 part images are pixel-identical (numpy array_equal) to the stated rows of their page image."
boundaries:
  precedes: "Nothing of a preceding unit is on the supplied pages: p. 78 opens with the running head and then this heading (the preceding reply, presumably on Cap. XXIII, ends on p. 77, not supplied)."
  heading_page_line: "p. 78, first line below the running head (heading y~320-350 px), rubric next line (y~417-447)"
  body_first_words: "Non è dubio che la prorogazione"
  body_last_words: "nè facultà di travagliarla per altra via."
  follows: "On p. 79 the body ends at line 12; below it a short centred rule (y~1158) and blank page. p. 80 is a half-title 'RICORDI POLITICI E CIVILI.' with no folio: XXIV is the last Considerazione in this sequence."
headings_printed:
  heading: "CONSIDERAZIONE SUL CAPITOLO XXIV⟨.|∅⟩ (large-and-small capitals: Considerazione sul Capitolo XXIV; D of CONSIDERAZIONE broken; a faint grey mark after XXIV, not certainly a period)"
  rubric: "La prolungazione degl' ⟨imperii|imperil⟩ ⟨fece|feco⟩ serva Roma."
running_heads_etc: "p. 78: folio '78' left, running head 'CONSIDERAZIONI' centred. p. 79: running head 'SUI DISCORSI DEL MACHIAVELLI.' centred, folio '79' right. p. 80: no running head or folio; half-title 'RICORDI POLITICI E CIVILI.'. Stray marks: tick in left margin of p. 78 at body line 7 (x~269); vertical bar in right margin p. 78 (x~1342, y~551-1125); scanner watermark fragments at bottom right of each page; small specks on p. 79-80. None is text."
footnotes: "One footnote, p. 78, keyed by call ⟨(1)|11⟩ after 'tirannidi.' (p. 78 body line 11) to this unit; 7 lines below a full rule (y~1545). Its final line ends 'partigiano', then a blank gap, then an isolated period far right (possible unprinted/abraded matter). No footnotes on p. 79 or p. 80."
paragraphing: "Single paragraph. Left ink edge (first column <128, margin marks excluded by restricting to x 285-1250 on p. 78): p. 78 line 1 = 355 px, lines 2-21 = 295-299 px -> line 1 indented ~60 px (paragraph start). p. 79 lines 1-12 = 134-140 px (line 1 = 134) -> no indent, so p. 79 continues the same paragraph. Footnote: first line 350 px, others 297-299 px (indented first line)."
line_numbering: "Lines counted per page from the first body line: p. 78 lines 1-21, p. 79 lines 1-12. Heading and rubric not numbered."
body_word_count: 318
words_per_page: {"78": 202, "79": 116}
word_count_method: "Python script (WORK/count.py) on WORK/body.txt: preferred reading of each doubt (∅ removed); whitespace tokens split after every apostrophe; only tokens containing a letter; hyphenated word counted once on the line/page where it begins; heading, rubric, running heads, footnote excluded. Footnote call attached to 'tirannidi.' does not add a token."
uncertain_loci_per_page: {"78 heading+rubric": 3, "78 body": 12, "78 footnote": 17, "79 body": 3}
uncertain_loci_total: 35
conventions: "Diplomatic, line for line; line-end hyphens kept; accents/punctuation as printed; ' for apostrophe, space after it recorded only where a clear gap is visible (rubric degl' imperii); ⟨preferred|alternative⟩, ∅ = nothing printed; [p. N] page change; no italic present in the unit."
paths_written: ["/root/p39/readers/fgB/out/FG-CONS.3.24-passB.md", "/root/p39/readers/fgB/work/body.txt", "/root/p39/readers/fgB/work/count.py", "/root/p39/readers/fgB/work/*.png (crops)"]
---

# Body

CONSIDERAZIONE SUL CAPITOLO XXIV⟨.|∅⟩

La prolungazione degl' ⟨imperii|imperil⟩ ⟨fece|feco⟩ serva Roma.

[p. 78]
Non è dubio che la prorogazione degli ⟨imperii|imperu⟩ fu occa-
sione grande a chi volle occupare la republica; perchè era
instrumento da farsi amici i soldati e séguito co' re, e nelle
nazioni o provincie forestiere, ⟨e|o⟩ a' capitani accresceva ric-
chezza con la quale potevano corrompere gli ⟨uomini|nomini⟩, come
fece a Cesare il lungo imperio di Gallia⟨.|∅⟩ Ma il fondamento
principale de' mali fu la corruzione della città, la quale da-
tasi alla avarizia, alle delizie, era in modo degenerata da-
gli antichi costumi, che ne nacquono le divisioni sangui-
nose della città, dalle quali sempre ne' populi liberi si viene
alle ⟨tirannidi|tiraanidi⟩.⟨(1)|11⟩ Di quivi nacque la facilità di corrompere
e cittadini e' soldati, di qui potette sperare uno ⟨Catilina|Catihna⟩
sanza imperio e sanza eserciti occupare la republica, di
qui conjurazione di più potenti di dividersi fra loro gli
⟨imperii|imperu⟩ e gli eserciti, e con queste forze tenere bassi gli
altri; di qui le prorogazioni estraordinarie degli ⟨imperii|imperu⟩,
come fu quella di ⟨Cesare|Cosare⟩, al quale non la utilità della re-
publica, non la necessità della guerra, non la ammirazione
della ⟨sua|aua⟩ virtù, ma la conjurazione con Pompeo ⟨e|o⟩ Crasso
di occupare la republica, fece imperio decemvirale. Non
era stato prorogato lo imperio a Silla, quando la prima
[p. 79]
volta venne alle mani con Mario, ma ne fu causa la divi-
sione tra la nobilità e la plebe, e avendo la plebe per capo
Mario, fu forzata la nobilità cercarsi uno capo⟨.|∅⟩ Però con-
chiuggo che quando Roma non fu corrotta, le prorogazioni
degli imperii e la continuazione del consulato, la quale
ne' tempi difficili usorono molte volte, furono cosa utile e
santa; ma corrotta la città, sursono le battaglie civili, e
i semi delle tirannidi, etiam sanza la prorogazione degli
⟨imperii|imperu⟩. E però si può conchiudere, che se non fussino
state anche le prorogazioni, non sarebbe mancato nè a ⟨Ce|Co⟩-
sare nè agli altri che occuporono la republica, nè pensiero
nè facultà di travagliarla per altra via.

# Footnotes on the page

p. 78, keyed to this unit by call ⟨(1)|11⟩ at body line 11 ("alle tirannidi."):

⟨(1)|11⟩ Due sono le cagioni che secondo il Machiavelli prepararono la
caduta della repubblica⟨:|∅⟩ le contenzioni che ⟨nacquero|uacquero⟩ dalla legge agra-
ria e la prolungazione del comando degli ⟨eserciti|esercili⟩⟨.|∅⟩ Quest'ultima produce
sempre due ⟨inconvenienti|inconvenienli⟩⟨:|∅⟩ l' uno che minor numero di ⟨uomini|ucmini⟩ si eser-
citano negli ⟨imperii|imperu⟩, e si viene per questo a ristringere la riputazione ⟨in|ıı⟩
⟨pochi|poclu⟩ , l⟨'|∅⟩altro ⟨che|clie⟩ ⟨chi|clu⟩ rimane ⟨lungo|liingo⟩ tempo a comandare l' esercito, lo
⟨guadagna|guadagıı a⟩, e lo rende suo ⟨partigiano|partigiallo⟩⟨∅|illegible matter in the blank gap⟩ .

(No footnotes on p. 79; p. 80 is a half-title.)

# Uncertain loci

n | page | line | printed context | ⟨preferred\|alternative⟩ | why
---|---|---|---|---|---
1 | 78 | heading | CAPITOLO XXIV | ⟨.\|∅⟩ | faint grey mark after V; not a clear period
2 | 78 | rubric | degl' imperii fece | ⟨imperii\|imperil⟩ | final i broken, shape like l; sense imperii
3 | 78 | rubric | imperii fece serva | ⟨fece\|feco⟩ | final e reads as o (e/o shape); sense fece
4 | 78 | 1 | degli imperii fu | ⟨imperii\|imperu⟩ | ii with broken dots reads as u; imperu not a word
5 | 78 | 4 | forestiere, e a' capitani | ⟨e\|o⟩ | blotched round letter; e (and) vs o (or) are different Italian words; prefer e by sense (list of further effects) and shape of eye
6 | 78 | 5 | corrompere gli uomini | ⟨uomini\|nomini⟩ | u reading n; nomini not a word
7 | 78 | 6 | di Gallia. Ma | ⟨.\|∅⟩ | period very faint, but a sentence begins with Ma
8 | 78 | 11 | alle tirannidi. | ⟨tirannidi\|tiraanidi⟩ | nn broken, reads aa; sense tirannidi
9 | 78 | 11 | tirannidi.(1) | ⟨(1)\|11⟩ | footnote call broken; parenthesis shapes read as 1s
10 | 78 | 12 | uno Catilina | ⟨Catilina\|Catihna⟩ | il broken into an h-shape; name Catilina
11 | 78 | 15 | imperii e gli | ⟨imperii\|imperu⟩ | ii reads u
12 | 78 | 16 | degli imperii, | ⟨imperii\|imperu⟩ | ii reads u
13 | 78 | 17 | quella di Cesare | ⟨Cesare\|Cosare⟩ | e reading o; name Cesare
14 | 78 | 19 | della sua virtù | ⟨sua\|aua⟩ | s reading a; aua not a word
15 | 78 | 19 | Pompeo e Crasso | ⟨e\|o⟩ | small filled round letter; e vs o are different Italian words; prefer e by sense (the triumvirate's joint conspiracy)
16 | 79 | 3 | uno capo. Però | ⟨.\|∅⟩ | only a faint grey smudge where a period should be; capital Però follows
17 | 79 | 9 | imperii. E però | ⟨imperii\|imperu⟩ | ii reads u
18 | 79 | 10 | nè a Ce-sare | ⟨Ce\|Co⟩ | e reading o; Cesare by sense
19 | 78 | fn call | (1) Due | ⟨(1)\|11⟩ | call broken, matches body call
20 | 78 | fn 2 | repubblica: le | ⟨:\|∅⟩ | only a grey smudge in the gap
21 | 78 | fn 2 | che nacquero | ⟨nacquero\|uacquero⟩ | n reads as broken ıı/u; sense nacquero
22 | 78 | fn 3 | degli eserciti | ⟨eserciti\|esercili⟩ | t broken to l
23 | 78 | fn 3 | eserciti. Quest'ultima | ⟨.\|∅⟩ | grey smudge; capital follows
24 | 78 | fn 4 | inconvenienti | ⟨inconvenienti\|inconvenienli⟩ | t broken
25 | 78 | fn 4 | inconvenienti: l' uno | ⟨:\|∅⟩ | grey smudge in gap before l'
26 | 78 | fn 4 | numero di uomini | ⟨uomini\|ucmini⟩ | o reads c, letters broken; sense uomini
27 | 78 | fn 5 | riputazione in | ⟨in\|ıı⟩ | two stems only, n broken
28 | 78 | fn 6 | in pochi , | ⟨pochi\|poclu⟩ | h broken into l+u-like strokes
29 | 78 | fn 6 | l'altro | ⟨'\|∅⟩ | apostrophe barely visible
30 | 78 | fn 6 | l'altro che chi | ⟨che\|clie⟩ | h broken
31 | 78 | fn 6 | che chi rimane | ⟨chi\|clu⟩ | h broken
32 | 78 | fn 6 | rimane lungo tempo | ⟨lungo\|liingo⟩ | u broken into two stems
33 | 78 | fn 7 | lo guadagna, | ⟨guadagna\|guadagıı a⟩ | n broken, final a smudged
34 | 78 | fn 7 | suo partigiano | ⟨partigiano\|partigiallo⟩ | n reads as ll
35 | 78 | fn 7 | partigiano ___ . | ⟨∅\|illegible matter⟩ | wide blank gap before an isolated final period; possibly a dropped/abraded reference
