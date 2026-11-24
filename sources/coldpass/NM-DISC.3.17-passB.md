---
unit: NM-DISC.3.17
reader: "cold reader nmB (Pass B, sample page p. 148 and two line crops of p. 149)"
source: "Machiavelli, Discorsi, 1824 Italian edition, vol. 2 (Libro terzo), p. 148, and two single-line crops from p. 149; page images only"
witness_images:
  - {file: 1824-p148-page.png, size: "2052x3228", rows: "0-3228", sha256_16: a645dea0faee7d27, check: "size and full sha256 match manifest"}
  - {file: 1824-p148-part1of3-y0-1205.png, size: "2052x1205", rows: "0-1205", sha256_16: 3c55d4f4d1f64cb0, check: "size and full sha256 match; pixel-identical to page rows 0-1205"}
  - {file: 1824-p148-part2of3-y947-2281.png, size: "2052x1334", rows: "947-2281", sha256_16: 2e63d094cd69c810, check: "size and full sha256 match; pixel-identical to page rows 947-2281"}
  - {file: 1824-p148-part3of3-y2023-3228.png, size: "2052x1205", rows: "2023-3228", sha256_16: 5f892214af9f1519, check: "size and full sha256 match; pixel-identical to page rows 2023-3228"}
  - {file: 1824-p149-line-crop-01-y1160-1246.png, size: "2052x86", rows: "1160-1246 (p. 149)", sha256_16: 90444b590f792181, check: "size and full sha256 match manifest (no p. 149 page image to compare rows)"}
  - {file: 1824-p149-line-crop-02-y1312-1394.png, size: "2052x82", rows: "1312-1394 (p. 149)", sha256_16: 22447589dcde0d77, check: "size and full sha256 match manifest (no p. 149 page image to compare rows)"}
manifest_check: "PASS: all 6 files match manifest pixel size and full sha256; the three p. 148 parts are pixel-identical (numpy array_equal) to the stated rows of the page image; crops checked for size and hash only, as instructed"
boundaries:
  precedes: "nothing of the preceding chapter on p. 148: the page opens (below running head) with the chapter heading; the end of cap. XVI is not on the sample page"
  heading_page_line: "p. 148, first text after the running head (ink rows 511-559): CAPITOLO XVII; rubric on three lines below (rows 662-880)"
  body_first_words: "Debbe una Repubblica assai considerare di (p. 148, line 1)"
  body_last_words: "not on the sample page"
  follows: "not on the sample page"
  p148_last_words: "infino a tanto che vennero le nuovc [nuove?] della rotta (p. 148, line 23; no hyphen; chapter continues on p. 149)"
headings_printed:
  heading: "CAPITOLO XVII — one line, centred, full capitals (roman, larger than text), no final stop"
  rubric: "*Che non si offenda uno, e poi quel medesimo / si mandi in amministrazione e governo d' im- / portanza.* — italic, three lines with hanging indent (line 1 left edge x=486, lines 2-3 x=543 and x=540); final stop printed (set off by a small space after 'portanza')"
running_heads_etc:
  page_number: "148 at top left (rows ~351-410, x≈495); the '1' is a short old-style one; a faint tiny mark just right of the 8 at its top (not a sort)"
  running_head: "DISCORSI, letterspaced small capitals, centred-right of the page number, same line; no stop; faint grey smudge just right of the final I"
  signature: "none"
  catchword: "none"
  stray_marks:
    - "left margin speck, light grey, ~11x5 px at x 395-406, y 935-940, level with the top of the drop D of body line 1; not a sort"
    - "small brownish dot above the first v of 'disavvantaggio' (body line 12, approx x≈600, y≈1800), at the top of the line band; colour browner than the text ink; foxing/speck, not an accent"
    - "short horizontal dash below the text block, rows 2866-2871, x 1103-1112; and a 1-2 px dot at rows 2949-2952, x 1407-1408; both stray, not sorts"
    - "crop 1: round brownish dot ~10 px across at x 1283-1292, rows 42-53 of the strip, mid x-height between 'tali' and 'offese', touching the space before the o; lighter and browner than the glyph ink (mean RGB ≈105,84,67 vs ≈60,41,25 in the adjacent o); probably a speck, possibly a raised point (see uncertain locus 4)"
    - "crop 1: 1-px column of dark at x=0, rows 0-9 (strip edge artefact)"
    - "crop 2: small speck rows 61-67, x 1166-1170, below the baseline under the 'rr' of 'incorrotta'; stray, not a sort"
    - "crop 2: ink at row 0, x 1435-1437 (tip of a descender from the line above, cut by the strip edge)"
footnotes: "none on p. 148"
paragraphing: "Left ink edge (x, px, threshold 128) per body line: L1 543 (begins with enlarged initial D), L2 477, L3 476, L4 475, L5 476, L6 475, L7 475, L8 474, L9 473, L10 473, L11 472, L12 473, L13 470, L14 471, L15 472, L16 475, L17 471, L18 469, L19 471, L20 467, L21 466, L22 469, L23 471. Only L1 is indented (~70 px beyond the 466-477 run); no other paragraph break on p. 148. Crops: left ink edge crop 1 x=262 (excluding the x=0 edge artefact), crop 2 x=268 — not indented relative to each other; no p. 149 full-line context to judge paragraphing."
line_numbering: "p. 148 body lines 1-23 counted from 'Debbe'; running head, page number, heading and rubric not counted. Crops are single lines, each line 1 of its crop."
words: {p148_body: 187, crop1: 8, crop2: 8}
word_count_method: "Script work/count.py: preferred reading of each ⟨|⟩ taken; whitespace tokens; each token further split after every apostrophe so elided forms (l', d', s', n', all') count separately; only tokens containing a letter counted; a word divided by a line-end hyphen counted once on the line where it begins (continuation token on the next line dropped). Crop 1 begins with 'feso.', the tail of a word divided on the previous line of p. 149, so it is not counted: crop1 = 8 (9 if 'feso.' is counted); its last word 'pos-' begins on the line and is counted."
uncertain_loci_total: 4
conventions: "Diplomatic, line for line. Italic as *...*. Drop/enlarged initial D given as ordinary capital. Accents as printed (all graves here: partì, andò, uscì, Città). Apostrophe followed by a space where a clear gap is visible (n' andò, d' Asdrubale, all' incontro, rubric d' im-), closed up where set close (l'altro, s'era, l'addietro, d'accordo, d'oppressarlo, d'Annibale). Straight ' used for the printed apostrophe. No space recorded before , ; : even where the page sets one (e.g. 'Popolo :', 'pericolosissimo ;', 'Annibale ,'). Line-end hyphens kept. Doubt as ⟨preferred|alternative⟩. Stray specks not entered in the text except where a dot might be a sort (crop 1, marked)."
paths_written:
  - /home/claude/p37/readers/nmB/work/check.py
  - /home/claude/p37/readers/nmB/work/lines.py
  - /home/claude/p37/readers/nmB/work/crop.py
  - /home/claude/p37/readers/nmB/work/zoom.py
  - /home/claude/p37/readers/nmB/work/zoom2.py
  - /home/claude/p37/readers/nmB/work/zoom3.py
  - /home/claude/p37/readers/nmB/work/cropc.py
  - /home/claude/p37/readers/nmB/work/zdot.py
  - /home/claude/p37/readers/nmB/work/col.py
  - /home/claude/p37/readers/nmB/work/c2m.py
  - /home/claude/p37/readers/nmB/work/count.py
  - /home/claude/p37/readers/nmB/work/body.txt
  - /home/claude/p37/readers/nmB/work/crop1.txt
  - /home/claude/p37/readers/nmB/work/crop2.txt
  - /home/claude/p37/readers/nmB/work/*.png (enlarged crops: head_0-1, b1-b6_0-1, c1_0-2, c2_0-2, z_ed10, z_ed17, z_ed19, z_ed_rub, z_nuove, z_nuove2, z_line11, z_cons, z_sera, z_dann, z_allinc, z_speck, z_dot)
  - /home/claude/p37/readers/nmB/out/NM-DISC.3.17-passB.md
---

# Body

CAPITOLO XVII

*Che non si offenda uno, e poi quel medesimo*
*si mandi in amministrazione e governo d' im-*
*portanza.*

[p. 148]
Debbe una Repubblica assai considerare di
non preporre alcuno ad alcuna importante ammi-
nistrazione, al quale sia stato fatto da altri alcuna
notabile ingiuria. Claudio Nerone, il quale si partì
dallo esercito che lui aveva a fronte ad Annibale,
e con parte di esso n' andò nella Marca a trovare
l'altro Consolo per combattere con Asdrubale avan-
ti che si congiungesse con Annibale, s'era trovato
per l'addietro in Ispagna a fronte d' Asdrubale,
⟨cd|ed⟩ avendolo serrato in luogo con lo esercito che
bisognava, o che Asdrubale combattesse con suo
disavvantaggio, o si morisse di fame, fu da Asdru-
bale astutamente tanto intrattenuto con certe pra-
tiche d'accordo, che egli uscì di sotto, e tolsegli
quella occasione d'oppressarlo. La qual cosa saputa
a Roma gli dette carico grande appresso al Senato
⟨cd|ed⟩ al Popolo: e di lui fu parlato inonestamente
per tutta quella Città, non senza suo grande diso-
nore ed isdegno. Ma sendo poi fatto Consolo, e
mandato all' incontro d'Annibale, prese il sopra-
scritto partito, il quale fu pericolosissimo; tal-
mente che Roma stette tutta dubbia e sollevata,
infino a tanto che vennero le ⟨nuovc|nuove⟩ della rotta

## Crop 1 (p. 149, rows 1160-1246)

feso. E quando queste passioni di tali ⟨offese|·offese⟩ pos-

## Crop 2 (p. 149, rows 1312-1394)

tempi che Roma era ancora incorrotta, si debbe

# Footnotes on the page

None.

# Uncertain loci

| n | page | line | printed context | ⟨preferred\|alternative⟩ | why |
|---|---|---|---|---|---|
| 1 | 148 | 10 | "Asdrubale, / cd avendolo serrato" | ⟨cd\|ed⟩ | At 5x the first letter is an open bowl with no visible crossbar or eye, shaped like the c of this fount; the ink shows c. Sense (and the same compositor's 'ed isdegno', L19, with a clear e) favours 'ed'; the e's hairline bar may be worn or lost in imaging. |
| 2 | 148 | 17 | "Senato / cd al Popolo:" | ⟨cd\|ed⟩ | Same as locus 1: no crossbar visible at 5x, glyph reads as c. Sense favours 'ed'. |
| 3 | 148 | 23 | "vennero le nuovc della rotta" | ⟨nuovc\|nuove⟩ | Final letter at 4x is an open c-form with no crossbar; compare the clear e of 'della' beside it. Sense favours 'nuove'. |
| 4 | crop 1 | 1 | "di tali ·offese pos-" | ⟨offese\|·offese⟩ | A round dot ~10 px across sits at mid x-height in the space before 'offese', touching the o's left side. Its colour is lighter and browner than the glyph ink (cf. the brown speck above 'disavvantaggio' on p. 148), and a full stop would stand on the baseline, so it is preferred as a stray speck; it could be a raised point or spurious sort. |
