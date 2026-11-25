---
unit: "Discorsi III.24 (CAPITOLO XXIV), sample: printed p. 171 whole, plus two line crops from p. 170 and one from p. 172"
reader: "cold reader nmB (Pass B, sample page p. 171 and three line crops)"
source: "Machiavelli, Discorsi sopra la prima deca di Tito Livio, 1824 Italian edition, vol. 2 (Libro terzo)"
witness_images:
  - {file: 1824-p171-page.png, size: 2052x3228, rows: "0-3228", sha256_16: a1e3de55bb34ca2c, check: "size and full sha256 match MANIFEST"}
  - {file: 1824-p171-part1of3-y0-1205.png, size: 2052x1205, rows: "0-1205", sha256_16: 0820dbb88e171d8a, check: "match MANIFEST; numpy array_equal to page rows 0-1205: True"}
  - {file: 1824-p171-part2of3-y947-2281.png, size: 2052x1334, rows: "947-2281", sha256_16: f634019139501934, check: "match MANIFEST; array_equal to page rows 947-2281: True"}
  - {file: 1824-p171-part3of3-y2023-3228.png, size: 2052x1205, rows: "2023-3228", sha256_16: f6436141715f1ea8, check: "match MANIFEST; array_equal to page rows 2023-3228: True"}
  - {file: 1824-p170-line-crop-01-y2444-2521.png, size: 2052x77, rows: "2444-2521 of p170", sha256_16: b4313d0aa2aa42bf, check: "size and full sha256 match MANIFEST (no page image to compare)"}
  - {file: 1824-p170-line-crop-02-y2521-2598.png, size: 2052x77, rows: "2521-2598 of p170", sha256_16: e5f7ccfda7aba49a, check: "size and full sha256 match MANIFEST (no page image to compare)"}
  - {file: 1824-p172-line-crop-03-y1619-1697.png, size: 2052x78, rows: "1619-1697 of p172", sha256_16: 9d4b0a715560d088, check: "size and full sha256 match MANIFEST (no page image to compare)"}
manifest_check: "all 7 images match MANIFEST.txt in pixel size and full sha256; all 3 parts pixel-identical to the stated rows of the p171 page image"
boundaries:
  precedes: "not on these images (chapter opening is before p. 171; p. 170 only as two line crops)"
  heading_page_line: "not on these images; heading CAPITOLO XXIV not seen (stated by caller only)"
  body_first_words: "p. 171 begins mid-sentence: 'benchè quanto alla prolungazione dell' Imperio,' (no capital, no indent)"
  body_last_words: "p. 171 ends: 'fecero Proconsolo; talchè fu il primo Proconsolo' followed by a raised/medial point (doubtful: high-set full stop or speck); no catchword, no hyphen"
  follows: "not on these images (chapter end not seen; p. 172 only as one line crop)"
headings_printed: {heading: "none on p. 171", rubric: "none on p. 171"}
running_heads_etc: "p. 171 running head 'LIBRO TERZO' (spaced small caps; the O of LIBRO looks like Q, broken/odd sort) centred, page number '171' at right; no signature, no catchword, no footnotes; nothing at foot of page"
footnotes: "none on p. 171 or on the crops"
paragraphing: "p. 171: 30 body lines; left ink edge (first column <128, x-height cores) by line 1-30: 222,223,224,221,220,221,220,222,222,223,222,222,226,227,227,225,225,224,225,224,225,228,223,226,226,228,229,231,231,233 px (smooth drift of ~11 px from skew); no line indented, so no paragraph break on the page (line 25 'Il primo', a new sentence, is at 226, not indented). Crops: p170 crop1 438-439 px, crop2 438 px (flush, same measure); p172 crop3 508 px, i.e. ~70 px right of the p170 crops, but p172 is a different (verso) page with its own margin and no page image is supplied, so indent cannot be judged"
line_numbering: "none printed; lines numbered here 1-30 for p. 171"
body_word_count: 250
words_per_page: {p171: 250, p170_crop1: 9, p170_crop2: "9 standalone (8 if 'prin-/cipio' is counted once, on crop1 where it begins)", p172_crop3: 9}
word_count_method: "Python script work/count.py: preferred reading of each doubt (∅ = nothing); whitespace tokens split after every apostrophe; only tokens containing a letter; hyphenated word counted once on its first line; running head excluded. Per-line p. 171: 6,9,8,9,8,8,10,7,9,9,9,8,8,10,9,8,7,8,9,10,6,8,7,8,11,9,8,9,8,7"
uncertain_loci_per_page: {p171: 6, p170_crops: 1, p172_crop: 0}
uncertain_loci_total: 7
conventions: "line for line; hyphens kept; accents/capitals/punctuation as printed; apostrophe as ' with a following space only where a clear gap is seen; no italic on these images; double spaces in justified lines (e.g. 'che  i', 'Magistrati  e') not recorded; the e's crossbar is faint throughout this impression so e often looks like c (che, Plebe, viverc): read as e, not marked; ⟨preferred|alternative⟩, ∅ = nothing printed"
paths_written: ["/root/p39/readers/nmB/out/NM-DISC.3.24-passB.md", "/root/p39/readers/nmB/work/ (crops *.png, p171.txt, c1-c3.txt, count.py)"]
---

# Body

Heading and rubric: not on these images.

[p. 170, line crops only]

crop 01 (rows 2444-2521):
quali cose se fussero state conosciute bene ⟨da|dà⟩ prin-

crop 02 (rows 2521-2598):
cipio, e fattivi debiti rimedj, sarebbe stato il vivere

[p. 171]

benchè quanto alla prolungazione dell' Imperio,
non si vegga che in Roma nascesse mai alcuno
tumulto, nondimeno si vede in fatto, quanto nuocè
alla Città quella autorità che i cittadini per tali
deliberazioni presero. E se gli altri cittadini, a
chi era prorogato il Magistrato, fussero stati savj
e buoni, come fu L. Quinzio, non si sarebbe in-
corso in questo inconveniente. La bontà del quale
è d' uno esempio notabile, perchè sendosi fatto tra
la Plebe ed il Senato convenzione d' accordo, ed
avendo la Plebe prolungato in un anno l'Imperio
ai⟨∅|¨⟩ Tribuni, giudicandogli atti a poter resistere al-
l' ambizione dei Nobili, volle il Senato per gara
della Plebe, e per non parere da meno di lei,
prolungare il Consolato a L. Quinzio; il quale al
tutto negò questa deliberazione⟨,|;⟩ dicendo che i cat-
tivi esempj si volevano cercare di spegnerli, non
di accrescerli con un altro più cattivo esempio;
e volle si facessero nuovi Consoli. La qual bontà
e ⟨∅|˙⟩prudenza se fusse stata in tutt'i cittadini roma-
ni, non arebbe lasciata introdurre quella consue-
tudine di prolungare i Magistrati, e da quella non
si⟨∅|,⟩ sarebbe ⟨∅|˙⟩venuto alla prolungazione degl'Imperj:
la qual cosa col tempo rovinò quella Repubblica.
Il primo a chi fu prorogato l' Imperio fu P. Fi-
lone, il quale essendo a campo alla Città di Pa-
lepoli, e venendo la fine del suo Consolato, e
parendo al Senato ch' egli avesse in mano quella
vittoria, non gli mandarono il successore, ma lo
fecero Proconsolo; talchè fu il primo Proconsolo⟨.|∅⟩

[p. 172, line crop only]

crop 03 (rows 1619-1697):
Magistrati e gl' Imperj, se non venivano sì tosto

# Footnotes on the page

None.

# Uncertain loci

| n | page | line | printed context | ⟨preferred\|alternative⟩ | why |
|---|---|---|---|---|---|
| 1 | 170 | crop 01 | bene da prin- | ⟨da\|dà⟩ | small round dot over the a, not a slanted grave stroke; sense ('da principio') wants da. Different Italian words (da / dà) |
| 2 | 171 | 12 | ai¨ Tribuni | ⟨∅\|¨⟩ | two small dots after 'ai' at x-height top; read as stray marks/specks, not a diaeresis |
| 3 | 171 | 16 | deliberazione, dicendo | ⟨,\|;⟩ | the mark sits low and oblique with nothing visible above it; shape is a comma, slightly displaced |
| 4 | 171 | 20 | e ˙prudenza | ⟨∅\|˙⟩ | dot above the p of 'prudenza'; stray speck |
| 5 | 171 | 23 | si, sarebbe | ⟨∅\|,⟩ | small hooked mark below the baseline between 'si' and 'sarebbe'; probably a risen space/quad or speck, no comma wanted by sense |
| 6 | 171 | 23 | ˙venuto | ⟨∅\|˙⟩ | dot above the v of 'venuto'; stray speck |
| 7 | 171 | 30 | primo Proconsolo· | ⟨.\|∅⟩ | last mark on the page is a point at mid x-height, after a normal space-less gap; read as a high-set full stop; it could be a speck, with the sentence running on to p. 172 (not supplied) |

Notes (not doubts): line 21 'arebbe' is clearly printed (archaic form of avrebbe; no s or v lost, normal spacing); line 3 'nuocè' with grave as printed; line 23 'degl'Imperj' printed tight, 'Imperj :' with a gap before the colon (not recorded). p170 crop 02 'viverc': final letter is the same faint-barred e as elsewhere, read as 'vivere'.
