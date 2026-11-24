---
unit: NM-DISC.3.19
reader: "cold reader nmA (Pass A, full)"
source: "Machiavelli, Discorsi, 1824 Italian edition, vol. 2 (Libro terzo), pp. 154-156; page images only"
witness_images:
  - {file: 1824-p154-page.png, size: "2052x3228", rows: "0-3228", sha256_16: 501637abd41439b7, check: "size and full sha256 match"}
  - {file: 1824-p154-part1of3-y0-1205.png, size: "2052x1205", rows: "0-1205", sha256_16: 725ea87effbb8d21, check: "size and sha256 match; pixel-identical to page rows 0-1205"}
  - {file: 1824-p154-part2of3-y947-2281.png, size: "2052x1334", rows: "947-2281", sha256_16: 65c41190016bff6e, check: "size and sha256 match; pixel-identical to page rows 947-2281"}
  - {file: 1824-p154-part3of3-y2023-3228.png, size: "2052x1205", rows: "2023-3228", sha256_16: 6cc9b71042b2b20b, check: "size and sha256 match; pixel-identical to page rows 2023-3228"}
  - {file: 1824-p155-page.png, size: "2052x3228", rows: "0-3228", sha256_16: 2e767ded99217a30, check: "size and full sha256 match"}
  - {file: 1824-p155-part1of3-y0-1205.png, size: "2052x1205", rows: "0-1205", sha256_16: de3dbea8db89e32c, check: "size and sha256 match; pixel-identical to page rows 0-1205"}
  - {file: 1824-p155-part2of3-y947-2281.png, size: "2052x1334", rows: "947-2281", sha256_16: 55c279c5e4dc843d, check: "size and sha256 match; pixel-identical to page rows 947-2281"}
  - {file: 1824-p155-part3of3-y2023-3228.png, size: "2052x1205", rows: "2023-3228", sha256_16: d53aa73e74184b2f, check: "size and sha256 match; pixel-identical to page rows 2023-3228"}
  - {file: 1824-p156-page.png, size: "2052x3228", rows: "0-3228", sha256_16: 5dfc2c7ae1ef91a7, check: "size and full sha256 match"}
  - {file: 1824-p156-part1of3-y0-1205.png, size: "2052x1205", rows: "0-1205", sha256_16: e5c0712b7d4d9252, check: "size and sha256 match; pixel-identical to page rows 0-1205"}
  - {file: 1824-p156-part2of3-y947-2281.png, size: "2052x1334", rows: "947-2281", sha256_16: 0b6e755fc30811d6, check: "size and sha256 match; pixel-identical to page rows 947-2281"}
  - {file: 1824-p156-part3of3-y2023-3228.png, size: "2052x1205", rows: "2023-3228", sha256_16: f026446b787b7c6b, check: "size and sha256 match; pixel-identical to page rows 2023-3228"}
manifest_check: "PASS. All 12 files: pixel size and full sha256 equal MANIFEST (RGB PNGs); all 9 part images numpy-equal to the stated row slices of their -page image."
boundaries:
  precedes: "Nothing of another unit on p. 154: only the page number '154' and running head 'DISCORSI' stand above the heading (the preceding chapter must end on p. 153, not supplied)."
  heading_page_line: "p. 154, top of page below the running head: 'CAPITOLO XIX' (heading starts the page; rubric in two italic lines below it, then body)."
  body_first_words: "Era la Repubblica romana sollevata (p. 154, body line 1, raised initial E)"
  body_last_words: "più che l' armi. (p. 155, body line 26, last line of the page; rest of p. 155 blank)"
  follows: "p. 156: heading 'CAPITOLO XX' (roman capitals, no final stop; a small stray mark under the second X); rubric in italic, two lines: 'Uno esempio d' umanità appresso ai Falisci / potette più d' ogni forza romana.' (final stop printed); first body line: 'Essendo Camillo con l'esercito intorno alla Cit-' (raised initial E)."
headings_printed:
  heading: "CAPITOLO XIX — one line, roman capitals, centred, no final stop printed."
  rubric: "*Se a reggere una moltitudine è più necessario / l' ossequio che la pena.* — italic, two centred lines, final stop printed."
running_heads_etc: {p154: "page number '154' at left, running head 'DISCORSI' (letterspaced small capitals) centred; no signature, no catchword", p155: "running head 'LIBRO TERZO' (letterspaced small capitals) centred-left, page number '155' at right; no signature, no catchword", stray_marks: "p.154: tiny dot below the baseline just right of 'E' in body l.24 ('E molte'); faint speck in right margin near l.15 (approx x1610,y1875); faint speck below text block (approx y3120). p.155: small tail/dot beneath the final 'i' of 'armi' (l.26); isolated dots in right margin (approx x1718,y1787 and x1695,y2463); vertical gutter/show-through strokes at far left edge. None read as text.", blank_space: "p.154 text ends at l.24 (approx y2660) with blank space below; p.155 text ends at l.26 (approx y2365), rest of page blank (chapter end)."}
footnotes: "none on pp. 154-155 (no call marks in text, no notes at foot of either page)."
paragraphing: "One paragraph. Left ink edge (first column <128, measured in the x-height band of each line, page pixel coords): p.154 l1=508 (raised initial E, indented c.65px), l2-l24 = 440,442,444,445,447,453,449,451,451,454,462,451,454,455,455,454,456,457,457,458,461,462,463 (flush; slow drift 440->463 is page skew; 453 'P', 462 'T' are serif shapes). p.155 l1-l26 = 253,252,256,251,254,262,252,255,251,253,256,257,252,254,253,251,250,251,252,251,253,253,251,252,254,252 (all flush; 262 = 'T' of Torquato). No indented line other than p.154 l1; p.155 l1 continues the sentence from p.154."
line_numbering: "No printed line numbers. Body lines counted per page: p.154 24 lines, p.155 26 lines."
body_word_count: 407
words_per_page: {p154: 195, p155: 212}
word_count_method: "Python script on the transcription below (work/count.py): preferred reading of each doubt (∅ = nothing), italics markers removed; whitespace tokens; each token split after every apostrophe; only parts containing a letter counted; a word hyphenated at line end counted once on the line/page where it begins (first token of the following line skipped). Heading, rubric, running heads, page numbers excluded. Punctuation-spacing does not affect the count."
uncertain_loci_per_page: {p154: 1, p155: 4}
uncertain_loci_total: 5
conventions: "Diplomatic, line for line. Line-end hyphens kept as printed ('-'). Accents as printed (all grave in these pages: fuggì, più, può, nè, perchè, Nobiltà, già, virtù, acciocchè, è, Meritò, potè, umanità). Apostrophe printed as a curly right quote, rendered '; a space after it recorded only where a clear gap is visible on the image. The type's e is often broken so as to resemble c throughout (e.g. 'cd' for ed, 'cssere'); this is treated as damaged e, not recorded as doubt, except where noted. Space before colon/semicolon as sometimes printed ('dico :', 'Appio ;') is not reproduced; punctuation recorded as attached to the preceding word. Italic marked *...*. Ligatures (fl in superfluo, ff/fi) resolved to letters. Raised initial E of the first word not separately marked. ⟨preferred|alternative⟩, ∅ = nothing printed."
paths_written: ["/root/p38/readers/nmA/out/NM-DISC.3.19-passA.md", "/root/p38/readers/nmA/work/ (scratch crops c*.png d*.png apos*.png q.png; edges.py, edges2.py, apos.py, apos2.py, count.py, body.txt)"]
---

# Body

CAPITOLO XIX

*Se a reggere una moltitudine è più necessario*
*l' ossequio che la pena.*

[p. 154]
Era la Repubblica romana sollevata per le ini-
micizie de' Nobili e de' Plebei, nondimeno sopra-
stando loro la guerra, mandarono fuori con gli
eserciti Quinzio ed Appio Claudio. Appio per essere
crudele e rozzo nel comandare, fu male ubbidito
dai suoi, tanto che quasi rotto si fuggì della sua
Provincia. Quinzio per essere benigno e di umano
ingegno, ebbe i suoi soldati ubbidienti, e ripor-
tonne la vittoria. Donde e' pare che sia meglio a
governare una moltitudine essere umano che su-
perbo, pietoso che crudele. Nondimeno Cornelio
Tacito, al quale molti altri Scrittori acconsentono,
in una sua sentenza conchiude il contrario, quando
dice: *In multitudine regenda plus poena, quam
obsequium valet.* E considerando come si possa
salvare l' una e l' altra di queste opinioni, dico:
o che tu hai a reggere uomini che ti sono per l'or-
dinario compagni, o uomini che ti sono sempre
soggetti. Quando ti sono compagni, non si può in-
teramente usare la pena, nè quella severità di che
ragiona Cornelio; e perchè la Plebe romana aveva
in Roma eguale imperio con la Nobiltà, non poteva
uno che ne diventava Principe a tempo, con cru-
deltà e rozzezza maneggiarla. E⟨∅|,⟩ molte volte si vide
[p. 155]
che miglior frutto fecero i Capitani romani, che
si facevano amare dagli eserciti, e che con ossequio
li maneggiavano, che quelli che si facevano straor-
dinariamente temere, se già e' non erano accom-
pagnati da una eccessiva virtù, come fu Manlio
Torquato. Ma chi comanda ai sudditi, de'⟨ |∅⟩quali
ragiona Cornelio, acciocchè non diventino inso-
lenti, e che per troppa tua facilità non ti calpe-
stino, debbe volgersi piuttosto alla pena che al-
l' ossequio. Ma questa ancora debbe essere in modo
moderata, che si fugga l'⟨∅| ⟩odio; perchè farsi odiare
non torna mai bene ad alcun Principe. Il modo
del fuggirlo è lasciare stare la roba de' sudditi,
perchè del sangue, quando non vi sia sotto ascosa
la rapina, nessun Principe ne è desideroso se non
necessitato, e questa necessità viene rare volte;
ma sendovi mescolata la rapina, viene sempre, nè
mancano mai le cagioni e il desiderio di sparger-
lo, come in altro Trattato sopra questa materia
s' è largamente discorso. Meritò dunque più laude
Quinzio che Appio; e la sentenza di Cornelio den-
tr⟨ɔ|o⟩ ai termini suoi, e non ne' casi osservati da
Appio, merita d' essere approvata. E perchè noi
abbiamo parlato della pena e dell' ossequio, non
mi pare superfluo mostrare, come un esempio
d' umanità potè appresso ai Falisci più che l' armi⟨∅|,⟩.

# Footnotes on the page

none (pp. 154-155 carry no footnotes and no call marks)

# Uncertain loci

| n | page | line | printed context | ⟨preferred\|alternative⟩ | why |
|---|---|---|---|---|---|
| 1 | 154 | 24 | maneggiarla. E⟨∅\|,⟩ molte volte | ⟨∅\|,⟩ | A tiny dot sits below the baseline at the right foot of E; it is too small and low to be a full comma sort and reads as a stray speck/broken serif. Sense does not want a comma after the conjunction E. |
| 2 | 155 | 6 | de'⟨ \|∅⟩quali | ⟨ \|∅⟩ | Gap between apostrophe and q is narrow, intermediate between the clear spaces elsewhere (de' Nobili, de' sudditi) and closed l'or-. Recorded as a space, with no-space as the alternative. |
| 3 | 155 | 11 | fugga l'⟨∅\| ⟩odio; | ⟨∅\| ⟩ | Apostrophe and o very close; no clear gap, so no space recorded; a hairline space is possible. |
| 4 | 155 | 22 | tr⟨ɔ\|o⟩ ai termini | ⟨ɔ\|o⟩ | The final letter of 'den-/tro' is printed as an open, reversed-c shape (left side of the bowl missing), i.e. a damaged or wrong sort; sense requires o (dentro). |
| 5 | 155 | 26 | l' armi⟨∅\|,⟩. | ⟨∅\|,⟩ | A small tail hangs below the final i before the full stop; read as a broken/flawed sort or speck, not punctuation; a comma before the stop makes no sense. |
