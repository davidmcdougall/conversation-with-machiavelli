---
unit: NM-DISC.3.19
reader: "cold reader (comparison read), images only"
source: "Machiavelli, Discorsi, Libro terzo, Venice: Domenico Giglio, 1554; fols. 181r-181v; page images only"
witness_images:
  - {file: 1554-fol181r-page.png, size: "1639x3244", rows: "0-3244", sha256_16: 4ea0610189fb50f4, check: "size and full sha256 match manifest"}
  - {file: 1554-fol181r-part1of3-y0-1211.png, size: "1639x1211", rows: "0-1211", sha256_16: 31804ed61d038947, check: "size and sha256 match; pixel-identical to page rows 0-1211"}
  - {file: 1554-fol181r-part2of3-y951-2293.png, size: "1639x1342", rows: "951-2293", sha256_16: f7aed92171a65d1d, check: "size and sha256 match; pixel-identical to page rows 951-2293"}
  - {file: 1554-fol181r-part3of3-y2033-3244.png, size: "1639x1211", rows: "2033-3244", sha256_16: 36e92697ea8281a5, check: "size and sha256 match; pixel-identical to page rows 2033-3244"}
  - {file: 1554-fol181v-page.png, size: "1625x3209", rows: "0-3209", sha256_16: ee85357cc3a45e7c, check: "size and full sha256 match manifest"}
  - {file: 1554-fol181v-part1of3-y0-1198.png, size: "1625x1198", rows: "0-1198", sha256_16: 2fd640634da3f23d, check: "size and sha256 match; pixel-identical to page rows 0-1198"}
  - {file: 1554-fol181v-part2of3-y942-2267.png, size: "1625x1325", rows: "942-2267", sha256_16: 35ac3cddbf2a98e7, check: "size and sha256 match; pixel-identical to page rows 942-2267"}
  - {file: 1554-fol181v-part3of3-y2011-3209.png, size: "1625x1198", rows: "2011-3209", sha256_16: 35c85483e7c522d7, check: "size and sha256 match; pixel-identical to page rows 2011-3209"}
manifest_check: "PASS: all 8 files match manifest pixel size and full sha256; all 6 part images are byte-identical (numpy array_equal) to the stated row ranges of their page image"
boundaries: {precedes: "nothing of the preceding chapter on these pages: fol. 181r opens with running head and folio number, then this chapter's heading (end of III.18 would be on fol. 180v, not supplied)", heading_page_line: "fol. 181r, top, directly under the running head 'T E R Z O.' / '181'; two heading lines", body_first_words: "ERa la Rep. Romana ſolleuata per le nimici-", body_last_words: "...potè appreſſo a i Faliſci piu,che l'armi. (fol. 181v, line 19)", follows: "fol. 181v, after a blank space: heading 'VNO ESSEMPIO D'HVMANITA / appreſſo a i Faliſci potè piu d'ogni forza / Romana. Cap. XX.' then body 'E Sſendo Camillo con l'eſſercito intorno alla ...' (drop initial E)"}
headings_printed: {heading: "SE A REGGERE VNA MOLTITVDINE / e piu neceſſario l'oſſequio,che la pena. Ca.XIX.", type: "line 1 roman capitals (widely spaced); line 2 italic lower case, with 'Ca.' and small-capital roman numerals 'XIX'", lines: 2, final_stop: "yes, a full stop after XIX"}
running_heads_etc: {fol_181r_running_head: "T E R Z O. (spaced roman capitals, with stop)", fol_181r_folio_number: "181 (top right)", fol_181v_running_head: "L I B R O (spaced roman capitals, no stop)", fol_181v_folio_number: "none clearly printed; a very faint ghost at top left (show-through or blind impression), not read", signature: "fol. 181r foot, right of centre: a single swash 'Q'-like letter, read as signature mark (no numeral visible)", catchwords: "none on either page", stray_marks: "r8: comma-like speck between 'ſuoi' and 'ſoldati'; r9: small tick below baseline after 'uittoria'; r11: small speck after 'Ta' at line end; r16: dot after 'ſi' at line end; r20: small mark above before 'non'; v1-v2: scattered specks above 'inſolenti' and 'peſtino,' (incl. an apostrophe-like speck over the n of 'inſolenti'); v4: double-dot mark above end of 'perche'; v5: dot after 'mai'; v8: dot over first n of 'non'; v14: faint dots after 'ter'", marginal_quote_marks: "',,' printed in the left margin of r13 and r14, marking the Latin quotation"}
leaf_condition: {tears: "none visible", losses: "none; no text lost", show_through: "moderate on both pages (ghost lines of the other side visible between lines, strongest on 181v around the chapter break)", worn_or_broken_sorts: "r32 'diuentino' smudged/broken; r32 'ragiona' with a stroke over the a (damaged or stray); r31-32 'Cornelio' l weak; v1 initial 't' broken; v3 'ſequio' i reduced to a colon-like shape; v16 'eſſere' blurred; v19 'Faliſci' F damaged (E-like); v8 'diſideroſo' d worn", illegible_or_lost_words: "none wholly illegible or lost; doubtful letters recorded in Uncertain loci"}
footnotes: "none; no marginal notes apart from the ',,' quotation marks at r13-14"
paragraphing: "Single paragraph. Left ink edge (first column <128) per body line, x px. 181r: L1 48 (drop initial E, 3 lines deep; text of L1-3 begins c. 290 beside it), L2 75, L3 44, L4 30, L5 31, L6 34, L7 36, L8 34, L9 28, L10 30, L11 30, L12 27, L13 35 (',,'), L14 37 (',,'), L15 34, L16 35, L17 34, L18 34, L19 31, L20 36, L21 39, L22 38, L23 46, L24 38, L25 40, L26 41, L27 43, L28 36, L29 43, L30 35, L31 36, L32 44. 181v: L1 87, L2 97, L3 87, L4 88, L5 90, L6 79, L7 90, L8 89, L9 91, L10 93, L11 90, L12 83, L13 85, L14 89, L15 91, L16 87, L17 87, L18 97, L19 93. All variation within 10-20 px is italic letter-shape; no line is indented; verso L19 is short (right edge 1094 vs c. 1515), ending the chapter."
line_numbering: "body lines counted per page from first body line; running heads, folio numbers and heading not counted; 181r 32 lines, 181v 19 lines"
body_word_count: 378
words_per_page: {"181r": 234, "181v": 144}
word_count_method: "Python script on the body as transcribed, preferred reading of each doubt (∅ = nothing); whitespace tokens; each token split after every apostrophe; only tokens containing a letter counted (so ',,' and '&' excluded); a word divided at line end (hyphen or |) counted once, on the line where it begins, by dropping the first whitespace token of the continuation line; comma-joined forms without space (e.g. 'humano,che') count as one token per the whitespace rule; heading, running heads, signature excluded"
uncertain_loci_total: 19
conventions: "long s as ſ; italic ß ligature as ſs; tilde/macron as combining tilde (cõ, ẽ); accents as printed; u/v and i/j as printed; no italic marking (body italic throughout); roman capitals within italic as plain capitals (roman type also used for 'Appio Claudio:Appio' r4, proper-name capitals and 'Rep.'); drop initial E joined to its word; '-' = printed line-end hyphen (a short bold slanted stroke in this print); '|' = word divided at line end without hyphen; ⟨preferred|alternative⟩ inline doubts, ∅ = nothing printed; ',,' marginal quotation marks retained at line start; spaces around punctuation recorded where a clear gap is visible"
paths_written: ["/root/p38/readers/g1554/out/NM-DISC.3.19-1554.md"]
---

# Body

SE A REGGERE VNA MOLTITVDINE
e piu neceſſario l'oſſequio,che la pena. Ca.XIX.

[fol. 181r]
ERa la Rep. Romana ſolleuata per le nimici⟨-|∅⟩
tie de nobili, et de plebei , nondimeno ſopra|
ſtando loro la guerra, mandarono fuori con
gli eſſerciti Quintio, & Appio Claudio:Appio per
eſſere crudele, & rozzo nel commandare , fu male
obbidito da ſuoi, tanto che quaſi rotto ſi fugg⟨i|ì⟩ del-
la ſua prouincia. Quintio per eſſer benigno, & di
humano ingegno , hebbe i ſuoi ſoldati obbidienti,e
riportonne la uittoria⟨ .|, .⟩ Onde e pare che ſia meglio,
a gouernare una moltitudine,eſſere humano,che ſo|
perbo;pietoſo,che crudele. Nondimeno Cornelio Ta⟨∅|-⟩|
cito(alquale molti altri ſcrittori conſentono)in una
,, ſua ſentenza conchiude il contrario , Quando
,, ait , in multitudine regenda plus pœna , quam
obſequium ualet. Cioe⟨,|.⟩ Per regger molti ual piu la
ſeuerita,che l'eſſer benigno. Et conſiderando come ſi
poſſa ſaluare l'una & l'altra di queſte oppenioni,
dico⟨.|,⟩o che tu hai a reggere huomini,che ti ſono per
l'ordinario cõpagni,o huomini , che ti ſono ſempre
ſoggetti. Quando ti ſono compagni, non ſi puo in-
teramẽte uſare la pena,ne quella ſeuerita,di che ra-
giona Cornelio:& perche la plebe⟨ |∅⟩Romana haueua
in Roma equale Imperio con la nobilita,non pote-
ua uno,che diuentaua Prencipe a tempo,con crudel|
ta,& rozzezza maneggiarla.et molte uolte ſi uid|
de , che miglior frutto feciono i Capitani Romani,
che ſi faceuano amare dagli eſſerciti, et che cõ oſſe|
quio gli maneggiauano , che quelli che ſi faceuano
ſtraordinariamente temere , ſe gia e non erano ac-
compagnati da una ecceſsiua uertu, come fu Man-
lio Torquato , ma chi comanda a i ſudditi ( de
quali ⟨ragiona|ràgiona⟩ Cornelio ) accioche non ⟨diuentino|diuentmo⟩
[fol. 181v]
⟨t|∅⟩inſolenti, & che per troppa tua felicità non ti cal|
peſtino,debb⟨é|e⟩ uolgerſi piu toſto alla pena,che all'oſ|
ſequ⟨i|:⟩o.ma queſta anchora debbe eſſer in modo mo-
derata,che ſi f⟨u|ù⟩gga l'odio:perche farſi odiare non
torna mai bene ad alcuno Prencipe . Il modo del
fuggirlo è,laſciar ſtare la robba de ſudditi : perche
del ſangue ( quando non ui ſia ſotto aſcoſa la ra-
pina ) neſſuno Prencipe ne è diſideroſo,non neceſsi-
tato,& queſta neceſsita uiene rade uolt⟨e|è⟩: ma eſſen-
doui meſcol⟨à|a⟩ta la rapina,uiene ſempre,ne manca-
no mai le cagioni, & il diſiderio di ſpargerla,come
in altro trattato ſopra queſta materia s'è larga-
mente diſcorſo. Meritò adunque piu laude Quintio,
che Appio,e la ſentenza di Cornelio dentro a i ter⟨∅|-⟩|
mini ſuoi, & non ne caſi oſſeruati da Appio,meri-
ta d'eſſ⟨e|i⟩re approuata⟨∅|.⟩ Et perche noi habbiamo par-
lato della pena,e dell'oſſequio, non mi pare ſuper-
fluo moſtrare, come uno eſſempio d'humanita potè
appreſſo a i ⟨F|E⟩aliſci piu,che l'armi.

# Notes on the page

none (no marginal or foot notes; the only marginal matter is the pair of ',,' quotation marks at 181r lines 13-14, retained in the body)

# Uncertain loci

| n | page | line | printed context | ⟨preferred\|alternative⟩ | why |
|---|---|---|---|---|---|
| 1 | 181r | 1 | per le nimici⟨-\|∅⟩ / tie | ⟨-\|∅⟩ | final mark is a bold blob after the i, read as the print's short hyphen; could be part of a heavy i, i.e. no hyphen |
| 2 | 181r | 6 | ſi fugg⟨i\|ì⟩ del- | ⟨i\|ì⟩ | two dots over the gi; shape reads as i-dot plus speck, not a grave; sense (past tense) would favour ì |
| 3 | 181r | 9 | la uittoria⟨ .\|, .⟩ Onde | ⟨ .\|, .⟩ | a small tick below the baseline before the stop; taken as stray, could be a weak comma |
| 4 | 181r | 11 | Cornelio Ta⟨∅\|-⟩\| / cito | ⟨∅\|-⟩ | small speck right of 'Ta' below x-height; not hyphen-shaped, but a worn hyphen is possible |
| 5 | 181r | 15 | ualet. Cioe⟨,\|.⟩ Per | ⟨,\|.⟩ | faint small mark at baseline with a short tail; reads as weak comma, could be a stop |
| 6 | 181r | 18 | dico⟨.\|,⟩o che | ⟨.\|,⟩ | a round dot on the baseline, no tail; sense might favour a comma |
| 7 | 181r | 22 | la plebe⟨ \|∅⟩Romana | ⟨ \|∅⟩ | very narrow gap between 'plebe' and 'Romana'; a space sort is probably present |
| 8 | 181r | 32 | quali ⟨ragiona\|ràgiona⟩ Cornelio | ⟨ragiona\|ràgiona⟩ | a slanting stroke rises from the top of the a; looks like damage/stray rather than an accent; sense favours ragiona |
| 9 | 181r | 32 | accioche non ⟨diuentino\|diuentmo⟩ | ⟨diuentino\|diuentmo⟩ | word badly smudged/broken; the i-dot and stroke count support -tino; 'in' could be read as a damaged m |
| 10 | 181v | 1 | ⟨t\|∅⟩inſolenti, | ⟨t\|∅⟩ | first sort is a broken t-like letter before 'inſolenti'; sense (non diuentino inſolenti) would favour nothing, or t' elided |
| 11 | 181v | 2 | debb⟨é\|e⟩ uolgerſi | ⟨é\|e⟩ | a short slanted mark sits on the final e; may be stray; sense favours plain debbe (cf. 'debbe' v3) |
| 12 | 181v | 3 | ſequ⟨i\|:⟩o.ma | ⟨i\|:⟩ | the i shows as dot plus a lower dot (colon-like), read as a broken i sort of the same width |
| 13 | 181v | 4 | ſi f⟨u\|ù⟩gga l'odio | ⟨u\|ù⟩ | a light grave-like mark over the u; probably stray; sense favours fugga |
| 14 | 181v | 9 | rade uolt⟨e\|è⟩: | ⟨e\|è⟩ | faint mark above final e; probably stray; sense favours uolte |
| 15 | 181v | 10 | meſcol⟨à\|a⟩ta | ⟨à\|a⟩ | small dark accent-like mark over the second a; sense favours meſcolata |
| 16 | 181v | 14 | dentro a i ter⟨∅\|-⟩\| / mini | ⟨∅\|-⟩ | faint dots after 'ter', not a clear hyphen; could be a worn hyphen |
| 17 | 181v | 16 | d'eſſ⟨e\|i⟩re | ⟨e\|i⟩ | blurred sort; sense favours e |
| 18 | 181v | 16 | approuata⟨∅\|.⟩ Et | ⟨∅\|.⟩ | no clear stop before capital Et; a faint speck could be a weak stop, which sense would favour |
| 19 | 181v | 19 | a i ⟨F\|E⟩aliſci | ⟨F\|E⟩ | damaged roman capital with an extra lower stroke; F per the next chapter's heading 'Faliſci' |
