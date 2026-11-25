---
unit: NM-DISC.3.24
reader: "cold reader g1554 (Giglio 1554, full)"
source: "Discorsi di Nicolo Machiavelli fiorentino, sopra la prima deca di Tito Livio (Venice, Domenico Giglio, 1554), ff. 188v-189v (leaf1 = 188v, leaf2 = 189r, leaf3 = 189v), 500 ppi"
witness_images:
  - {file: 1554-leaf1-page.png, size: 1625x3209, rows: "0-3209", sha256_16: 98185de66dca37c0, check: "sha256 match; size match"}
  - {file: 1554-leaf1-part1of3-y0-1198.png, size: 1625x1198, rows: "0-1198", sha256_16: 758ae3eb074fb425, check: "sha256 match; size match"}
  - {file: 1554-leaf1-part2of3-y942-2267.png, size: 1625x1325, rows: "942-2267", sha256_16: 1b23074333108368, check: "sha256 match; size match"}
  - {file: 1554-leaf1-part3of3-y2011-3209.png, size: 1625x1198, rows: "2011-3209", sha256_16: 54bb63d4e21878d9, check: "sha256 match; size match"}
  - {file: 1554-leaf2-page.png, size: 1639x3244, rows: "0-3244", sha256_16: 786b8c825e2128b1, check: "sha256 match; size match"}
  - {file: 1554-leaf2-part1of3-y0-1211.png, size: 1639x1211, rows: "0-1211", sha256_16: 9a185f5441aaaf69, check: "sha256 match; size match"}
  - {file: 1554-leaf2-part2of3-y951-2293.png, size: 1639x1342, rows: "951-2293", sha256_16: cf916664b3fc4a0e, check: "sha256 match; size match"}
  - {file: 1554-leaf2-part3of3-y2033-3244.png, size: 1639x1211, rows: "2033-3244", sha256_16: 1bf7979ddc767ed2, check: "sha256 match; size match"}
  - {file: 1554-leaf3-page.png, size: 1625x3209, rows: "0-3209", sha256_16: 979850fa4644c4d3, check: "sha256 match; size match"}
  - {file: 1554-leaf3-part1of3-y0-1198.png, size: 1625x1198, rows: "0-1198", sha256_16: 5505427006ad4cfe, check: "sha256 match; size match"}
  - {file: 1554-leaf3-part2of3-y942-2267.png, size: 1625x1325, rows: "942-2267", sha256_16: 8040f3881eb6ee5f, check: "sha256 match; size match"}
  - {file: 1554-leaf3-part3of3-y2011-3209.png, size: 1625x1198, rows: "2011-3209", sha256_16: fc89c17a451d462a, check: "sha256 match; size match"}
manifest_check: "All 12 images match MANIFEST.txt in pixel size and full sha256. Each part image is pixel-identical (numpy array_equal True) to the stated rows of its -page image (9/9)."
boundaries:
  precedes: "End of III.23 on 188v, lines 15-17 of the text block: '...come da uno ſcoglio,perche tirarſi odio addoſ- / ſo ſenza ſuo profitto,è al tutto partito temerario, / et poco prudente:' (final mark ':' or '.'; the 'ſo' and 'et poco' sorts damaged)"
  heading_page_line: "188v, after a blank line below the end of III.23: two heading lines (y about 1558 and 1670 in 1554-leaf1-page.png)"
  body_first_words: "[S]E ſi conſidera bene il procedere della Repub."
  body_last_words: "ſarebbero anchora uenuti piu tardi nella ſeruitu. (189v, 4th line)"
  follows: "189v: 'DELLA POVERTA DI CINCIN- / nato, et di molti cittadini Romani. C. XXV.', then the body with a large initial: 'NOi habbiamo ragionato altroue, come la ...'"
headings_printed:
  heading: "LA PROLVNGATIONE DE GLI / imperij fece ſerua Roma. Cap. XXIIII. (line 1 in spaced roman capitals, line 2 italic with roman 'R' and 'Cap. XXIIII.'; the 'L' of LA and the 'I' of GLI are damaged sorts; small specks between X.X.IIII are probably not printed points)"
  rubric: "none printed"
running_heads_etc: "188v: running head 'LIBRO' (no folio number on the verso). 189r: 'TERZO.' + folio number '189' (third digit read as 9: closed bowl and descending tail; a remote alternative is 3). 189v: 'LIBRO', catchword 'ricchezze' at the foot. No signatures seen. No catchword seen on 188v or 189r. A dark vertical band at the right edge of 188v and 189v is the page edge/gutter shadow, not a mark."
footnotes: "none"
paragraphing: "One paragraph. The body opens with a woodcut initial S (ink x 127-263, y 1788-2085 on 188v) three lines deep; those three lines start at x 288-292, the next lines at x 106-111. Left ink edges (first column with a pixel darker than 128, measured on the line band): 188v L1-3 292/290/288 (beside the initial), L4-15 111,106,107,110,110,111,106,107,107,110,109,102. 189r L1-35 93,94,100,100,99,99,94,89,92,91,93,95,92,86,86,70,89,85,85,83,82,83,78,80,78,80,72,76,72,69,62,66,60,58,38 (steady leftward drift from page curvature or skew; L16 at 70 is caused by a speck left of 'rouino', and L35 at 38 by the descender of the initial long s of 'ſino'). 189v L1-4 128,128,129,131. No indented line inside the unit."
line_numbering: "none printed; lines counted per page within the unit (188v body L1-15; 189r L1-35; 189v L1-4)"
body_word_count: 466
words_per_page: {188v: 125, 189r: 306, 189v: 35}
word_count_method: "Python script (work/scripts/body.py): preferred reading of each doubt; italic markers removed; whitespace tokens, also split after every apostrophe; only tokens containing a letter are counted, so '&' (188v L12) is not counted; a word split across a line or page counted once on the line where it starts (this includes splits with no visible hyphen: an-/no, pro/longare, laſcia/ta, l'im/perio, fece/ro, per/che, troua/re); heading, running heads and catchword excluded. The initial S is counted as part of 'SE'."
uncertain_loci_per_page: {188v: 8, 189r: 16, 189v: 0}
uncertain_loci_total: 24
conventions: "Diplomatic. ſ kept; u/v as printed; & kept; tildes kept (õ, ũ, ẽ, ã). The ſs ligature (ß-shaped sort) is given as ſs, and double long s (ſſ) as ſſ. ij/ii as printed. The body is italic throughout; each line is wrapped in *...*. Roman capitals in the heading are given plain. [S] = woodcut initial. Line-end hyphens are given where a mark is visible (in this worn impression they often show only as a dot or blob); where none is visible the place is marked ⟨∅|-⟩. Word spacing after commas follows the image approximately and was not measured. Accents only where seen."
paths_written:
  - /root/p39/readers/g1554/out/NM-DISC.3.24-1554.md
  - /root/p39/readers/g1554/work/ (crops *.png, body.json, scripts/crop.py, scripts/enh.py, scripts/lines.py, scripts/lines2.py, scripts/body.py)
---

# Body

[p. 188v]

LA PROLVNGATIONE DE GLI
*imperij fece ſerua* R*oma.* Cap. XXIIII.

[S] *E ſi conſidera bene il procedere della Repub.*
*Romana ſi uedra, due coſe eſſere ſtate cagio-*
*ne de la reſolutione di quella Rep. l'una furo-*
*no le cõtentioni, che nacquero dalla legge ⟨A|Ꝁ⟩graria,*
*l'altra la prolũgatione de gli imperij. Le quali coſe⟨∅|:⟩*
*ſe fuſsino ⟨ſtate|ſtàte⟩ conoſciute bene da principio⟨;|,⟩et fat-*
*⟨tiui|titi⟩ i debiti rimedij, ſarebbe ſtato il uiuer libero piu⟨∅|-⟩*
*lungo et perauentura piu quieto. Et benche quanto*
*alla prolungatione dell'imperio nõ ſi uegga, che in*
*Roma naſceſſe mai alcuno tumulto: nõdimeno ſi ue-*
*de in fatto, quanto nuoce alla città quella auttori-*
*ta, che i cittadini, per tali deliberationi preſono. &*
*ſe gli altri cittadini , a chi era prorogato il magi-*
*ſtrato, fuſsino ſtati ſaui, et buoni, come L. Quintio,*
*⟨non|nõ⟩ ſi ⟨ſarebbe incorſo|ſarebbeincorſo⟩ in queſto inconueniente. la*

[p. 189r]
*bonta delquale è d'uno eſſempio notabile perche eſ-*
*ſendoſi fatto tra la plebe, et il Senato conuentione*
*d'accordo,et hauendo la plebe prolungato in ⟨un' an|un'an⟩⟨∅|-⟩*
*no l'imperio a i tribuni, giudicandogli atti a poter*
*reſiſtere a l'ambitione de nobili, uolle il Senato per*
*gara della plebe⟨∅|.⟩ et per nõ parere da meno di lei, pro⟨∅|-⟩*
*longare il Conſolato a L. Quintio. Ilquale al tutto*
*negò queſta deliberatione dicẽdo che i cattiui eſſem-*
*pi ſi uoleuan cercare de ſpengerli, non d'accreſcerli*
*con un'altro piu cattiuo eſſempio, et uolle ſi faceſsi-*
*no nuoui Cõſoli. Laqual bonta, et ⟨prudenza|prudẽza⟩ ſe ⟨fuſſe|fuſſi⟩*
*ſtata in tutti i cittadini Romani, nõ harebbe laſcia⟨∅|-⟩*
*ta introdurre quella conſuetudine di prolungare i*
*magiſtrati: et da quella non ſi ſarebbe uenuto alla*
*prolungatione de gli imperij, laqual coſa col tempo*
*rouino quella Rep. Il primo, a chi fu allongato l'im⟨∅|-⟩*
*perio, fu P. Philone, ilquale eſſendo a campo alla cit-*
*tà di ⟨Palepoli|Pàlepoli⟩, et uenendo la fine del ſuo Conſolato,*
*et parẽdo al Senato, ch'egli haueſſe in mano quella*
*uittoria, non gli mandarono il ſucceſſore, ma lo fece⟨∅|-⟩*
*ro Procõſolo, tal che fu il primo Proconſolo. Laqual*
*coſa(anchora che moſsa ⟨da il|dal⟩ Senato per utilita pub-*
*blica)fu quella, che con il tẽpo fece ſerua Roma; per⟨∅|-⟩*
*che quanto piu i Romani ſi diſcoſtaron con l'armi,*
*tãto piu pareua loro tale prorogatione neceſſaria, et*
*piu l'uſarono. Laqual coſa fece due inconuenienti,*
*l'uno, che meno numero di huomini ſi eſſercitarono*
*ne gli imperij. et ſi ⟨uẽne|uenne⟩ per queſto a riſtringere la*
*riputatione in pochi: l'altro, che ⟨ſtãdo|ſtando⟩ un cittadino*
*aſſai tempo comãdatore d'uno eſſercito, ſe lo guada-*
*gnaua, et faceuaſelo partigiano: perche quello eſſerci-*
*to col tempo dimenticaua il Senato, et riconoſceua*
*quel capo. Per queſto Silla, et Mario poterono troua⟨∅|-⟩*
*re ſoldati, che contra al bene publico gli ſeguitaſ-*
*ſino. Per queſto ⟨Ceſare|Çeſare⟩ potè occupare la patria, che*

[p. 189v]
*ſe mai i Romani non haueſsino prolungati i magi-*
*ſtrati, et gli imperii, non ueniuano ſi toſto a tanta*
*potẽza, et ſe fuſsino ſtati piu tardi gli acquiſti loro,*
*ſarebbero anchora uenuti piu tardi nella ſeruitu.*

# Footnotes on the page

None printed on 188v, 189r or 189v.

Other damage and show-through (not counted as doubts because the reading is not in question): 189r is worn and lightly inked throughout, most of all in the right half of lines 5-14 and 24-35. Broken or faint sorts at 188v L3 reſolutione, L4 Agraria, L11 fatto, L12 cittadini, L15 non; 189r L5 nobili, per; L6 parere, meno, lei; L7 Quintio. Ilquale; L8 deliberatione, cattiui; L9 ſpengerli, d'accreſcerli; L11 nuoui, prudenza, fuſſe; L12 harebbe; L13 introdurre, conſuetudine; L16 allongato; L17 campo (m broken: 'ca npo'), cit-; L18 uenendo, ſuo; L22 Senato; L24 diſcoſtaron; L25 prorogatione neceſſaria; L27 numero di huomini; L28 riſtringere; L29 un cittadino; L30 guada-; L35 patria. Show-through is visible on all three pages, mostly in the white space around the headings and the lower part of 188v. It nowhere hides a letter of the body. No tears or losses. No marginal quotation marks (,,) or other marginal marks, apart from a speck in the left margin of 189r L16.

# Uncertain loci

| n | page | line | printed context | ⟨preferred\|alternative⟩ | why |
|---|---|---|---|---|---|
| 1 | 188v | 4 | dalla legge _graria, | ⟨A\|Ꝁ⟩ | Damaged capital A. Its crossbar and apex are broken, so it looks like a k-shaped sort. The word is Agraria. |
| 2 | 188v | 5 | Le quali coſe_ | ⟨∅\|:⟩ | Two small dots after coſe at the line end. They could be a colon, but the syntax runs on ('coſe ſe fuſſino'), so a speck or show-through is preferred. |
| 3 | 188v | 6 | ſe fuſsino ſt_te | ⟨ſtate\|ſtàte⟩ | A mark over the a, probably damage or show-through rather than an accent. |
| 4 | 188v | 6 | da principio_et fat- | ⟨;\|,⟩ | A dot above the comma under magnification. It reads as a semicolon, but the dot may be a speck. |
| 5 | 188v | 7 | fat-/ t?i i debiti | ⟨tiui\|titi⟩ | The third sort is broken. Its shape is nearer u than t, which gives fat-tiui ('fattivi', 'made there'). The alternative, fat-titi, is a non-word. Preferred on shape and sense. Different readings. |
| 6 | 188v | 7 | libero piu_ / lungo | ⟨∅\|-⟩ | A dot or short dash after piu at the line end. No word is split (piu / lungo), so it is not a hyphen. A stray mark is preferred. |
| 7 | 188v | 15 | n__ ſi ſarebbe | ⟨non\|nõ⟩ | A worn word. The second half reads as 'n' with specks and no clear tilde. Same word either way. |
| 8 | 188v | 15 | ſarebbe_incorſo | ⟨ſarebbe incorſo\|ſarebbeincorſo⟩ | The gap is very narrow, with a speck in it. Word division is uncertain. |
| 9 | 189r | 3 | in un'_an | ⟨un' an\|un'an⟩ | A clear gap after the apostrophe, slightly narrower than a word space. |
| 10 | 189r | 3 | un' an_ / no | ⟨∅\|-⟩ | No hyphen visible at the line end (an-/no). |
| 11 | 189r | 6 | della plebe_ et per | ⟨∅\|.⟩ | A faint mark at the foot after plebe: a broken point or a speck. |
| 12 | 189r | 6 | di lei, pro_ / longare | ⟨∅\|-⟩ | No separate hyphen visible. The o is blotted. |
| 13 | 189r | 11 | et prud_nza | ⟨prudenza\|prudẽza⟩ | Badly worn. A mark above the e may be a tilde or damage. |
| 14 | 189r | 11 | ſe fuſſ_ | ⟨fuſſe\|fuſſi⟩ | The last letter is worn to a blob. Its shape is nearer e. Different verb forms. |
| 15 | 189r | 12 | laſcia_ / ta | ⟨∅\|-⟩ | No hyphen visible at the line end. |
| 16 | 189r | 16 | l'im_ / perio | ⟨∅\|-⟩ | No hyphen visible at the line end. |
| 17 | 189r | 18 | tà di P_lepoli | ⟨Palepoli\|Pàlepoli⟩ | A short stroke above the a, probably a damaged sort or speck. The l after it is also broken. |
| 18 | 189r | 20 | ma lo fece_ / ro | ⟨∅\|-⟩ | No hyphen visible at the line end. |
| 19 | 189r | 22 | moſsa d__l Senato | ⟨da il\|dal⟩ | A dotless i-shaped stroke stands apart between 'da' and 'l'. It is read as 'da il', but it could be a spaced and damaged 'dal'. Same sense. |
| 20 | 189r | 23 | Roma; per_ / che | ⟨∅\|-⟩ | No hyphen visible. per/che is a split word. |
| 21 | 189r | 28 | et ſi u_ne | ⟨uẽne\|uenne⟩ | A clear tilde above the e. The letter after it is broken. 'uẽne' is preferred, as printed. |
| 22 | 189r | 29 | che ſt__do | ⟨ſtãdo\|ſtando⟩ | A bar above the a looks like a tilde. The following letter is faint. |
| 23 | 189r | 33 | poterono troua_ / re | ⟨∅\|-⟩ | No hyphen visible at the line end. |
| 24 | 189r | 35 | Per queſto _eſare | ⟨Ceſare\|Çeſare⟩ | The C has a stroke below it, probably damage or a speck rather than a cedilla. |
