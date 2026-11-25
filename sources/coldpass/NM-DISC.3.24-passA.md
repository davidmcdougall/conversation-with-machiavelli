---
unit: "Discorsi III.24 (CAPITOLO XXIV) — La prolungazione degli Imperj fece serva Roma"
reader: "cold reader nmA (Pass A, full)"
source: "Machiavelli, Discorsi sopra la prima deca di Tito Livio, 1824 Italian edition, vol. 2 (Libro terzo), printed pp. 170-173 (page images 350 ppi)"
witness_images:
  - {file: 1824-p170-page.png, size: 2052x3228, rows: "0-3228", sha256_16: 301baf7473f5b407, check: "sha256+size match manifest"}
  - {file: 1824-p170-part1of3-y0-1205.png, size: 2052x1205, rows: "0-1205", sha256_16: 215bea7f798e1f6d, check: "match; array_equal page rows 0-1205 True"}
  - {file: 1824-p170-part2of3-y947-2281.png, size: 2052x1334, rows: "947-2281", sha256_16: a7b5952d94a254ea, check: "match; array_equal True"}
  - {file: 1824-p170-part3of3-y2023-3228.png, size: 2052x1205, rows: "2023-3228", sha256_16: 82b5a673956879aa, check: "match; array_equal True"}
  - {file: 1824-p171-page.png, size: 2052x3228, rows: "0-3228", sha256_16: a1e3de55bb34ca2c, check: "sha256+size match manifest"}
  - {file: 1824-p171-part1of3-y0-1205.png, size: 2052x1205, rows: "0-1205", sha256_16: 0820dbb88e171d8a, check: "match; array_equal True"}
  - {file: 1824-p171-part2of3-y947-2281.png, size: 2052x1334, rows: "947-2281", sha256_16: f634019139501934, check: "match; array_equal True"}
  - {file: 1824-p171-part3of3-y2023-3228.png, size: 2052x1205, rows: "2023-3228", sha256_16: f6436141715f1ea8, check: "match; array_equal True"}
  - {file: 1824-p172-page.png, size: 2052x3228, rows: "0-3228", sha256_16: c84dcdb850383023, check: "sha256+size match manifest"}
  - {file: 1824-p172-part1of3-y0-1205.png, size: 2052x1205, rows: "0-1205", sha256_16: 0fbf85492366b109, check: "match; array_equal True"}
  - {file: 1824-p172-part2of3-y947-2281.png, size: 2052x1334, rows: "947-2281", sha256_16: b2ad2b2f7988ab72, check: "match; array_equal True"}
  - {file: 1824-p172-part3of3-y2023-3228.png, size: 2052x1205, rows: "2023-3228", sha256_16: a9c372ac6c9d40c0, check: "match; array_equal True"}
  - {file: 1824-p173-page.png, size: 2052x3228, rows: "0-3228", sha256_16: 17b9d33b6117b419, check: "sha256+size match manifest"}
  - {file: 1824-p173-part1of3-y0-1205.png, size: 2052x1205, rows: "0-1205", sha256_16: f0f513c7a259edbf, check: "match; array_equal True"}
  - {file: 1824-p173-part2of3-y947-2281.png, size: 2052x1334, rows: "947-2281", sha256_16: bba344e719e54e85, check: "match; array_equal True"}
  - {file: 1824-p173-part3of3-y2023-3228.png, size: 2052x1205, rows: "2023-3228", sha256_16: b788df5fc9b25d58, check: "match; array_equal True"}
manifest_check: "PASS: all 16 images match MANIFEST.txt in pixel size and full sha256; all 12 part images are pixel-identical (numpy array_equal) to the stated rows of their -page image."
boundaries:
  precedes: "p. 170 ll. 1-14 (end of the preceding chapter, XXIII): '... perchè tirarsi odio addosso senza / suo profitto è al tutto partito temerario e poco / prudente.'"
  heading_page_line: "p. 170, heading 'CAPITOLO XXIV' centred at y≈1767-1815, after prose line 14 ('prudente.') and a blank; rubric at y≈1920-1985; body begins y≈2037"
  body_first_words: "Se si considera bene il procedere della Repub-"
  body_last_words: "acquisti loro, sarebbero ancora venuti più tardi / nella servitù. (p. 172 l. 20; rest of p. 172 blank)"
  follows: "p. 173: running head 'LIBRO TERZO 173'; heading 'CAPITOLO XXV'; rubric (italic, 2 lines) '*Della povertà di Cincinnato, e di molti / cittadini romani.*'; first body line 'Noi abbiamo ragionato altrove, come la più' (large initial N)"
headings_printed:
  heading: "CAPITOLO XXIV"
  rubric: "*La prolungazione degli Imperj fece serva Roma.*"
running_heads_etc: "p.170 '170' + 'DISCORSI'; p.171 'LIBRO TERZO' + '171'; p.172 '172' + 'DISCORSI'; p.173 'LIBRO TERZO' + '173'. No signatures, catchwords or marginalia. Stray specks: p.170 left margin (x≈215,y≈2990 in part 3 coords), p.171 right of l.24, p.172 left margin; lower half of p.172 shows only show-through."
footnotes: "none on pp. 170-172 (or in the boundary portion of p. 173)"
paragraphing: "Single paragraph. Left ink edges (first column <128, x px): p.170 body l.1 = 498 (indented, large initial S; other lines 436-439); p.171 ll.1-30 = 220-233 (slow drift down the page, no indent; l.25 'Il primo' = 226); p.172 ll.1-20 = 502-511 (no indent; l.1 'La qual' = 507). Only the first body line is indented."
line_numbering: "Lines numbered from 1 on each page counting body lines only (p.170 body ll.1-8 = page text lines 19-26 after 14 lines of ch. XXIII + heading + rubric); none printed."
body_word_count: 471
words_per_page: {"170": 64, "171": 249, "172": 158}
word_count_method: "Python script on the transcription with preferred readings (∅ = nothing); whitespace tokens, each split after every apostrophe; only tokens containing a letter counted; a word hyphenated at line end counted once on the line/page where it begins; heading, rubric, running heads excluded (no notes)."
uncertain_loci_per_page: {"170": 3, "171": 4, "172": 2}
uncertain_loci_total: 9
conventions: "Diplomatic, line for line; line-end hyphens kept; accents/capitals/punctuation as printed; italic *...*; apostrophe ' with a following space only where a clear gap is visible; the typographic thin space before ':' and ';' and ',' is not reproduced. Worn sorts read silently where only one word is possible: e printed like c (e.g. 'quicto' = quieto, 'vivcre' = vivere, 'talc' = tale, 'Repubblica'), broken b in 'benchè' (p.171 l.1), worn M in 'Magistrati' (p.172 l.17). Specks not transcribed: dot under final e of 'risoluzione' (p.170 l.3), marks over/beside 'ai Tribuni' (p.171 l.12), below 'si sarebbe' and over v of 'venuto' (p.171 l.23), over r of 'tardi' (p.172 l.18). Comma after 'deliberazione' (p.171 l.16) is set low but is a comma. Large initial S on p.170 l.1 transcribed as ordinary S."
paths_written:
  - /root/p39/readers/nmA/out/NM-DISC.3.24-passA.md
  - /root/p39/readers/nmA/work/ (check.py, crop.py, lines.py, strips.py, count.py, body.txt, zoom crops z_*.png, s*.png)
---

# Body

CAPITOLO XXIV

*La prolungazione degli Imperj fece serva Roma.*

[p. 170]
Se si considera bene il procedere della Repub-
blica romana, si vedrà due cose essere state ca-
gione della risoluzione di quella Repubblica; l'una
furono le contenzioni che nacquero dalla legge
Agraria; l' ⟨∅|.⟩altra la prolungazione ⟨degl'Imperj|degl' Imperj⟩: le
quali cose se fussero state conosciute bene ⟨da|dà⟩ prin-
cipio, e fattivi debiti rimedj, sarebbe stato il vivere
libero più lungo, e per avventura più quieto. E
[p. 171]
benchè quanto alla prolungazione dell' Imperio,
non si vegga che in Roma nascesse mai alcuno
tumulto, nondimeno si vede in fatto, quanto ⟨nuocè|nuoce⟩
alla Città quella autorità che i cittadini per tali
deliberazioni presero. E se gli altri cittadini, a
chi era prorogato il Magistrato, fussero stati savj
e buoni, come fu L. Quinzio, non si sarebbe in-
corso in questo inconveniente. La bontà del quale
è ⟨d' uno|d'uno⟩ esempio notabile, perchè sendosi fatto tra
la Plebe ed il Senato convenzione d' accordo, ed
avendo la Plebe prolungato in un anno l' Imperio
ai Tribuni, giudicandogli atti a poter resistere al-
l'ambizione dei Nobili, volle il Senato per gara
della Plebe, e per non parere da meno di lei,
prolungare il Consolato a L. Quinzio; il quale al
tutto negò questa deliberazione, dicendo che i cat-
tivi esempj si volevano cercare di spegnerli, non
di accrescerli con un altro più cattivo esempio;
e volle si facessero nuovi Consoli. La qual bontà
e prudenza se fusse stata in tutt'i cittadini roma-
ni, non ⟨arebbe|avrebbe⟩ lasciata introdurre quella consue-
tudine di prolungare i Magistrati, e da quella non
si sarebbe venuto alla prolungazione degl'Imperj:
la qual cosa col tempo rovinò quella Repubblica.
Il primo a chi fu prorogato l' Imperio fu P. Fi-
lone, il quale essendo a campo alla Città di Pa-
lepoli, e venendo la fine del suo Consolato, e
parendo al Senato ch' egli avesse in mano quella
vittoria, non gli mandarono il successore, ma lo
fecero Proconsolo; talchè fu il primo ⟨Proconsolo.|Proconsolo·⟩
[p. 172]
La qual cosa, ancora che mossa dal Senato per
utilità pubblica, fu quella che con il tempo fece
serva Roma. Perchè quanto più i Romani si disco-
starono con le armi, tanto più pareva loro tale
prorogazione necessaria, e più l'usarono. La qual
cosa fece due inconvenienti. L'uno, che meno nu-
mero di uomini si esercitarono negl'Imperj, e si
venne per questo a ristringere la riputazione in
pochi; l'altro, che stando un cittadino assai tem-
po Comandatore d'uno esercito, se lo guadagnava,
e facevaselo partigiano; perchè quello esercito col
tempo dimenticava il Senato, e riconosceva quello
Capo. Per questo Silla e Mario poterono trovare
soldati che contro al bene pubblico li ⟨seguitas-|seguitas=⟩
sero; per questo Cesare potette occupare la patria.
Che se mai i Romani non avessero prolungati li
Magistrati e ⟨gl' Imperj|gl'Imperj⟩, se non venivano sì tosto
a tanta potenza, e se fussero stati più tardi gli
acquisti loro, sarebbero ancora venuti più tardi
nella servitù.

# Footnotes on the page

None.

# Uncertain loci

| n | page | line | printed context | reading | why |
|---|---|---|---|---|---|
| 1 | 170 | 5 | Agraria; l'. altra | ⟨∅\|.⟩ | a small dot sits low between the apostrophe and 'altra'; taken as a speck/damage (no sense for a point), but could be a stray full stop. |
| 2 | 170 | 5 | degl'Imperj: le | ⟨degl'Imperj\|degl' Imperj⟩ | small gap after apostrophe, less than in 'l' altra'; judged not a clear space. |
| 3 | 170 | 6 | bene da prin-cipio | ⟨da\|dà⟩ | a round dot (not a wedge accent) stands above the a; read as speck → 'da'; 'dà' would be a different word (verb). |
| 4 | 171 | 3 | quanto nuocè | ⟨nuocè\|nuoce⟩ | grave accent clearly printed on final e; odd form transcribed as printed; alternative is the normal 'nuoce'. |
| 5 | 171 | 9 | è d' uno esempio | ⟨d' uno\|d'uno⟩ | gap after apostrophe moderate; judged visible. |
| 6 | 171 | 21 | non arebbe lasciata | ⟨arebbe\|avrebbe⟩ | clearly printed 'arebbe' (no v); kept as printed; flagged because 'avrebbe' is the expected form. Different spelling of same word. |
| 7 | 171 | 30 | il primo Proconsolo· | ⟨Proconsolo.\|Proconsolo·⟩ | final point raised to mid-height (same as 'utile·' at p.170 l.4 of ch. XXIII); taken as a full stop set high. |
| 8 | 172 | 14 | li seguitas- | ⟨seguitas-\|seguitas=⟩ | hyphen appears broken/doubled; read as ordinary hyphen. |
| 9 | 172 | 17 | e gl' Imperj | ⟨gl' Imperj\|gl'Imperj⟩ | gap after apostrophe judged visible but slight. |
