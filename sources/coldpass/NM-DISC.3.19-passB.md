---
unit: NM-DISC.3.19
reader: "cold reader nmB (Pass B, sample page p. 154 and four line crops of p. 155)"
source: "Machiavelli, Discorsi, 1824 Italian edition, vol. 2 (Libro terzo), p. 154, and four single-line crops from p. 155; page images only"
witness_images:
  - {file: 1824-p154-page.png, size: "2052x3228", rows: "0-3228", sha256_16: 501637abd41439b7, check: "size and full sha256 match manifest"}
  - {file: 1824-p154-part1of3-y0-1205.png, size: "2052x1205", rows: "0-1205", sha256_16: 725ea87effbb8d21, check: "size and full sha256 match; pixel-identical to page rows 0-1205"}
  - {file: 1824-p154-part2of3-y947-2281.png, size: "2052x1334", rows: "947-2281", sha256_16: 65c41190016bff6e, check: "size and full sha256 match; pixel-identical to page rows 947-2281"}
  - {file: 1824-p154-part3of3-y2023-3228.png, size: "2052x1205", rows: "2023-3228", sha256_16: 6cc9b71042b2b20b, check: "size and full sha256 match; pixel-identical to page rows 2023-3228"}
  - {file: 1824-p155-line-crop-01-y942-1019.png, size: "2052x77", rows: "942-1019 (p. 155)", sha256_16: 1541384990b910b9, check: "size and full sha256 match manifest (rows not checkable: no p. 155 page image)"}
  - {file: 1824-p155-line-crop-02-y1473-1549.png, size: "2052x76", rows: "1473-1549 (p. 155)", sha256_16: 305c89eaf86aa40c, check: "size and full sha256 match manifest (rows not checkable)"}
  - {file: 1824-p155-line-crop-03-y1779-1853.png, size: "2052x74", rows: "1779-1853 (p. 155)", sha256_16: c31bacadc1751234, check: "size and full sha256 match manifest (rows not checkable)"}
  - {file: 1824-p155-line-crop-04-y1853-1930.png, size: "2052x77", rows: "1853-1930 (p. 155)", sha256_16: 4c04b84f22955b7c, check: "size and full sha256 match manifest (rows not checkable)"}
manifest_check: "PASS. All 8 files match the manifest in pixel size and full sha256. Each of the three part images is pixel-identical (numpy array_equal on RGB arrays) to the stated rows of 1824-p154-page.png. Crop rows refer to a p. 155 image not supplied; crops checked by size and sha256 only."
boundaries:
  precedes: "Nothing but the running head line (page number '154' at left, 'DISCORSI' centred) is printed above the heading; no text of the preceding chapter is on this page (top margin above the running head is blank)."
  heading_page_line: "Heading 'CAPITOLO XIX' is the first printed item below the running head (ink rows 464-511 of 3228), centred; rubric follows in two centred italic lines (rows 616-680, 690-755); body begins at rows 803-906."
  body_first_words: "Era la Repubblica romana sollevata per le ini-"
  p154_last_words: "deltà e rozzezza maneggiarla. E molte volte si vide (no hyphen; sentence continues overleaf)"
headings_printed:
  heading: "CAPITOLO XIX — roman capitals, one line, centred, no final stop"
  rubric: "Se a reggere una moltitudine è più necessario / l' ossequio che la pena. — italic, two centred lines, final stop printed; visible gap after the apostrophe in l' ossequio"
running_heads_etc: {page_number: "154 (old-style figures, top left, same line as running head)", running_head: "DISCORSI (spaced small capitals, centred)", signature: "none", catchword: "none", stray_marks: "p. 154: a tiny speck just below the baseline at the lower right of the capital E in body line 24 (see uncertain locus 2); no other ink darker than 128 outside the text block (min grey 184 above the running head, 193 below the last line, 170 in the right margin before the gutter shadow); dark vertical gutter/edge shadow at far right of image. Crop 3: a small faint speck in the right margin (about x=1720), lighter than the text, outside the text measure, not transcribed.", initial: "Body opens with a large raised capital E (about 1.5 line heights tall, rising above the first line), followed by 'ra' in text type"}
footnotes: "none"
paragraphing: "Left ink edge (first column darker than 128, x in px of 2052) of body lines 1-24: 507, 440, 442, 444, 445, 447, 444, 449, 446, 449, 448, 451, 451, 454, 455, 455, 454, 456, 457, 457, 457, 461, 462, 463. Line 1 (with the raised initial E) starts ~65 px right of the column edge: the chapter's opening paragraph is indented. Lines 2-24 drift steadily from 440 to 463 (page skew, ~1 px per line), with no step that would mark an indent: no new paragraph begins on p. 154 after line 1. Right edges 1749-1763, justified throughout (line 1 right edge 1750). Crops: left edge 250-252, right edge 1542-1552 for all four, i.e. all are full-measure lines, none indented."
line_numbering: "No printed line numbers. Body lines counted from 1 (first body line, 'Era la Repubblica...') to 24 on p. 154; heading and rubric not counted; each crop is line 1 of itself."
words: {p154_body: 195, crop1: 10, crop2: 9, crop3: 8, crop4: 8}
word_count_method: "Python script over the transcription below: preferred reading of each doubt (locus 2 preferred ∅, so 'E' alone); whitespace tokens; each token split after every apostrophe so elided forms count separately (de' Nobili = 2, l'or- = 2); only tokens containing a letter (punctuation-only tokens dropped); a word hyphenated across lines counted once, on the line where it begins (the continuation fragment at the start of the next line is skipped); heading and rubric excluded. Crops counted each on its own; the leading fragments 'lenti,' (crop 1) and 'lo,' (crop 3) may be the ends of words hyphenated on unseen preceding lines, but as nothing before them is visible they are counted as tokens of their own line; if excluded, crop1 = 9 and crop3 = 7. Trailing 'calpe-' (crop 1) counted on its line."
uncertain_loci_total: 2
conventions: "Diplomatic, line for line. Italic as *...*. Line-end hyphens kept as printed. Accents, capitals and punctuation as printed (all accents on this page are grave: è, più, fuggì, può, nè, perchè, severità, Nobiltà, deltà; crop: facilità, è, Meritò, più). Apostrophe is printed as a raised curly mark (’), rendered here as ' ; a space after an apostrophe is recorded only where a clear gap is visible (de' Nobili, de' Plebei, e' pare, l' una, l' altra, rubric l' ossequio, crop 4 s' è) and none where the type is set close (l'or-). The thin spaces the compositor set before commas, semicolons and colons (e.g. 'ingegno ,' 'dice :' 'dico :') are not recorded; punctuation is attached to the preceding word. Raised initial E rendered as an ordinary capital E joined to 'ra'. Doubts as ⟨preferred|alternative⟩, ∅ = nothing printed."
paths_written: ["/root/p38/readers/nmB/out/NM-DISC.3.19-passB.md", "/root/p38/readers/nmB/work/ (scratch crops *.png and count.py only)"]
---

# Body

CAPITOLO XIX

*Se a reggere una moltitudine è più necessario*
*l' ossequio che la pena.*

[p. 154]

Era la Repubblica romana sollevata per le ini-
micizie de' Nobili e de' Plebei, nondimeno sopra-
stando loro la guerra, mandarono fuori con gli
eserciti Quinzio ⟨e|c⟩d Appio Claudio. Appio per essere
crudele e rozzo nel comandare, fu male ubbidito
dai suoi, tanto che quasi rotto si fuggì della sua
Provincia. Quinzio per essere benigno e di umano
ingegno, ebbe i suoi soldati ubbidienti, e ripor-
tonne la vittoria. Donde e' pare che sia meglio a
governare una moltitudine essere umano che su-
perbo, pietoso che crudele. Nondimeno Cornelio
Tacito, al quale molti altri Scrittori acconsentono,
in una sua sentenza conchiude il contrario, quando
dice: *In multitudine regenda plus poena, quam*
*obsequium valet.* E considerando come si possa
salvare l' una e l' altra di queste opinioni, dico:
o che tu hai a reggere uomini che ti sono per l'or-
dinario compagni, o uomini che ti sono sempre
soggetti. Quando ti sono compagni, non si può in-
teramente usare la pena, nè quella severità di che
ragiona Cornelio; e perchè la Plebe romana aveva
in Roma eguale imperio con la Nobiltà, non poteva
uno che ne diventava Principe a tempo, con cru-
deltà e rozzezza maneggiarla. E⟨∅|,⟩ molte volte si vide

[crop 1: 1824-p155-line-crop-01-y942-1019.png]

lenti, e che per troppa tua facilità non ti calpe-

[crop 2: 1824-p155-line-crop-02-y1473-1549.png]

la rapina, nessun Principe ne è desideroso se non

[crop 3: 1824-p155-line-crop-03-y1779-1853.png]

lo, come in altro Trattato sopra questa materia

[crop 4: 1824-p155-line-crop-04-y1853-1930.png]

s' è largamente discorso. Meritò dunque più laude

# Footnotes on the page

none

# Uncertain loci

| n | page | line | printed context | ⟨preferred\|alternative⟩ | why |
|---|---|---|---|---|---|
| 1 | 154 | 4 | eserciti Quinzio ?d Appio Claudio | ⟨e\|c⟩ | At 6x the first letter is c-shaped with only a faint thickening where the hairline crossbar of e would join; the e crossbar is faint throughout this scan, so the shape leans to e but a reading 'cd' cannot be excluded from the pixels alone. The following d is also broken (bowl and stem separated). Sense favours 'ed'. |
| 2 | 154 | 24 | maneggiarla. E? molte volte si vide | ⟨∅\|,⟩ | A tiny speck (~3 px) sits just below the baseline at the lower right of E. It is far smaller than the commas elsewhere on the page and has no comma head, so read as a stray mark; a damaged comma is the alternative. Sense does not require a comma here. |
