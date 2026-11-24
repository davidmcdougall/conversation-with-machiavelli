---
unit: NM-DISC.3.17
reader: "cold reader nmA (Pass A, full)"
source: "Machiavelli, Discorsi, 1824 Italian edition, vol. 2 (Libro terzo), pp. 148-150; page images only"
witness_images:
  - {file: 1824-p148-page.png, size: "2052x3228", rows: "0-3228", sha256_16: a645dea0faee7d27, check: "size ok; sha256 ok"}
  - {file: 1824-p148-part1of3-y0-1205.png, size: "2052x1205", rows: "0-1205", sha256_16: 3c55d4f4d1f64cb0, check: "size ok; sha256 ok; pixel-identical to page rows 0-1205"}
  - {file: 1824-p148-part2of3-y947-2281.png, size: "2052x1334", rows: "947-2281", sha256_16: 2e63d094cd69c810, check: "size ok; sha256 ok; pixel-identical to page rows 947-2281"}
  - {file: 1824-p148-part3of3-y2023-3228.png, size: "2052x1205", rows: "2023-3228", sha256_16: 5f892214af9f1519, check: "size ok; sha256 ok; pixel-identical to page rows 2023-3228"}
  - {file: 1824-p149-page.png, size: "2052x3228", rows: "0-3228", sha256_16: 7a1e0c4c65cf784c, check: "size ok; sha256 ok"}
  - {file: 1824-p149-part1of3-y0-1205.png, size: "2052x1205", rows: "0-1205", sha256_16: 117133a786038f36, check: "size ok; sha256 ok; pixel-identical to page rows 0-1205"}
  - {file: 1824-p149-part2of3-y947-2281.png, size: "2052x1334", rows: "947-2281", sha256_16: dbb834ee47bc0fa8, check: "size ok; sha256 ok; pixel-identical to page rows 947-2281"}
  - {file: 1824-p149-part3of3-y2023-3228.png, size: "2052x1205", rows: "2023-3228", sha256_16: d0b9b4e8bea5cec4, check: "size ok; sha256 ok; pixel-identical to page rows 2023-3228"}
  - {file: 1824-p150-page.png, size: "2052x3228", rows: "0-3228", sha256_16: 3f1013c940d782b6, check: "size ok; sha256 ok"}
  - {file: 1824-p150-part1of3-y0-1205.png, size: "2052x1205", rows: "0-1205", sha256_16: 5a425d2ec716f996, check: "size ok; sha256 ok; pixel-identical to page rows 0-1205"}
  - {file: 1824-p150-part2of3-y947-2281.png, size: "2052x1334", rows: "947-2281", sha256_16: c1d793e9f808128f, check: "size ok; sha256 ok; pixel-identical to page rows 947-2281"}
  - {file: 1824-p150-part3of3-y2023-3228.png, size: "2052x1205", rows: "2023-3228", sha256_16: 7a5d019a9d2f8a19, check: "size ok; sha256 ok; pixel-identical to page rows 2023-3228"}
manifest_check: "PASS: all 12 files match MANIFEST.md in pixel size and full sha256; every partN image is pixel-identical (numpy array_equal) to the stated rows [r0:r1] of its -page image. Script: work/check.py."
boundaries:
  precedes: "Not visible in the supplied images: p. 148 opens with the running head and then the heading CAPITOLO XVII; the end of the preceding chapter (XVI) must be on p. 147, which was not supplied."
  heading_page_line: "p. 148, first printed element below the running head (row ~351-409 px); rubric follows on three lines (rows ~511-879 px)"
  body_first_words: "Debbe una Repubblica assai considerare di (p. 148, line 1)"
  body_last_words: "la sua rovina. (p. 149, line 20)"
  follows: "p. 150: heading 'CAPITOLO XVIII', rubric '*Nessuna cosa è più degna d' un Capitano, / che presentire i partiti del nimico.*', body begins 'Diceva Epaminonda tebano, nissuna cosa es-' (p. 150, line 1); the rest of p. 149 below 'la sua rovina.' is blank"
headings_printed:
  heading: "CAPITOLO XVII — full capitals (larger than the running-head small capitals), one line, centred; no final stop printed"
  rubric: "*Che non si offenda uno, e poi quel medesimo / si mandi in amministrazione e governo d' im- / portanza.* — italic, three lines, first line full measure (left ink 486 px), lines 2-3 indented (left ink 543 and 540 px) as a hanging indent; final stop printed (set with a slight space after 'portanza'); 'd' im-' has a visible gap after the apostrophe; word divided 'im-/portanza'"
running_heads_etc: {p148: "running head '148' (outer/left) + 'DISCORSI' (letter-spaced small capitals, centred); a small speck just right of the '8' of the page number", p149: "running head 'LIBRO TERZO' (letter-spaced small capitals) + page number '149' (outer/right); a stray dot at baseline between B and R of LIBRO (looks like 'LIB.RO'), taken as a speck, not a letter", p150: "running head '150' + 'DISCORSI'", signatures: "none visible on pp. 148-149", catchwords: "none", stray_marks: "p148: small tick/dash in left margin level with body line 1 (approx x 395, y 935); brownish speck above the first v of 'disavvantaggio' (line 12); dot below the text block (x ~1105, y 2867) and a tiny speck lower right (y ~2990). p149: raised point between 'tali' and 'offese' (line 11; see uncertain locus 3); small dot below the first r of 'incorrotta' (line 13, below baseline, not affecting the reading); brownish blot above/right of 'se-' at end of line 17 (right margin, not a sort); specks below the text block at (x ~960, y 2026) and (x ~1475, y 2555); dots in left margin near top (x ~125, y ~170) and in right margin near bottom (x ~1955, y ~3060); show-through from the verso visible across the blank lower half"}
footnotes: "none"
paragraphing: "Left ink edge (first column with pixels <128 in each line band). p148: line 1 = 543 px (drop/enlarged initial D, indented); lines 2-22 = 466-477 px (margin ~472). p149: lines 1-20 = 259-275 px (margin ~267; line 1 = 270, line 20 = 271) — no indented line. Only p148 line 1 is indented (~70 px beyond margin). The unit has 1 printed paragraph."
line_numbering: "Body lines counted per page from the first body line; running heads, page numbers, heading and rubric not counted. p148: 22 body lines; p149: 20 body lines (line 20 'la sua rovina.' is a short line)."
body_word_count: 347
words_per_page: {p148: 187, p149: 160}
word_count_method: "Script work/count.py on work/body.txt: preferred reading of each ⟨a|b⟩ kept; whitespace tokens; each token further split after every apostrophe so elided forms (l', d', s', n', all', com') count separately; only tokens containing a letter counted; for a line ending in a hyphen the first token of the next line is not counted (hyphenated word counted once on the line/page where it begins). No hyphenated word crosses the page break."
uncertain_loci_per_page: {p148: 0, p149: 3}
uncertain_loci_total: 3
conventions: "Diplomatic, line for line. Accents as printed (all accents on these pages are grave: partì, andò, uscì, Città, sì, necessità, libertà, perchè, può, è). Enlarged initial D transcribed as ordinary capital. Italic as *...*. Line-end hyphens kept. A space after an apostrophe recorded where a gap is visible (n' andò, d' Asdrubale, all' incontro, d' una, com' era; rubric d' im-), omitted where set close (l'altro, s'era, l'addietro, d'accordo, d'oppressarlo, d'Annibale, d'Asdrubale p149). Typographic spaces before , ; : and the rubric's final stop are not recorded. 'ed' is read for the e/c-like letterforms where the e's eye is faint (ed avendolo, ed al Popolo, ed isdegno) — certain, not marked."
paths_written: [/home/claude/p37/readers/nmA/work/check.py, /home/claude/p37/readers/nmA/work/lines.py, /home/claude/p37/readers/nmA/work/crop.py, /home/claude/p37/readers/nmA/work/zoom.py, /home/claude/p37/readers/nmA/work/gaps.py, /home/claude/p37/readers/nmA/work/count.py, /home/claude/p37/readers/nmA/work/body.txt, "/home/claude/p37/readers/nmA/work/c148_0.png .. c148_7.png", "/home/claude/p37/readers/nmA/work/c149_0.png .. c149_5.png", /home/claude/p37/readers/nmA/work/c150_0.png, /home/claude/p37/readers/nmA/work/c150_1.png, "/home/claude/p37/readers/nmA/work/z_*.png (libro, tali, incor, nese, disavv, hdr, perche1, perche2, vie, laveva, saveva, comera)", /home/claude/p37/readers/nmA/out/NM-DISC.3.17-passA.md]
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
ed avendolo serrato in luogo con lo esercito che
bisognava, o che Asdrubale combattesse con suo
disavvantaggio, o si morisse di fame, fu da Asdru-
bale astutamente tanto intrattenuto con certe pra-
tiche d'accordo, che egli uscì di sotto, e tolsegli
quella occasione d'oppressarlo. La qual cosa saputa
a Roma gli dette carico grande appresso al Senato
ed al Popolo: e di lui fu parlato inonestamente
per tutta quella Città, non senza suo grande diso-
nore ed isdegno. Ma sendo poi fatto Consolo, e
mandato all' incontro d'Annibale, prese il sopra-
scritto partito, il quale fu pericolosissimo; tal-
mente che Roma stette tutta dubbia e sollevata,
infino a tanto che vennero le nuove della rotta
[p. 149]
d'Asdrubale. Ed essendo domandato poi Claudio
per qual cagione avesse preso sì pericoloso partito,
dove senza una estrema necessità egli aveva giuo-
cata quasi la libertà di Roma, rispose che ⟨l' aveva|l'aveva⟩
fatto perchè sapeva che se gli riusciva, riacqui-
stava quella gloria che ⟨s' aveva|s'aveva⟩ perduta in Ispagna;
e se non gli riusciva, e che questo suo partito avesse
avuto contrario fine, sapeva come ei si vendicava
contro a quella Città ed a quelli cittadini che lo
avevano tanto ingratamente e indiscretamente of-
feso. E quando queste passioni di ⟨tali offese|tali ·offese⟩ pos-
sono tanto in un cittadino romano, e in quelli
tempi che Roma era ancora incorrotta, si debbe
pensare quanto elle possano in un cittadino d' una
Città che non sia fatta com' era allora quella. E
perchè a simili disordini che nascono nelle Re-
pubbliche non si può dare certo rimedio, ne se-
guita che gli è impossibile ordinare una Repubblica
perpetua, perchè per mille inopinate vie si causa
la sua rovina.

# Footnotes on the page

none

# Uncertain loci

| n | page | line | printed context | ⟨preferred\|alternative⟩ | why |
|---|---|---|---|---|---|
| 1 | 149 | 4 | rispose che l'aveva | ⟨l' aveva\|l'aveva⟩ | Spacing only. A narrow but visible gap between the apostrophe and 'a' at 3x enlargement, smaller than the gaps at 'd' una' or 'com' era'; borderline between "clear gap" and "set close". |
| 2 | 149 | 6 | che s'aveva perduta | ⟨s' aveva\|s'aveva⟩ | Spacing only. Same as locus 1: a small gap after the apostrophe, wider than at 's'era' (p148 l.8) but narrower than at 'n' andò'. |
| 3 | 149 | 11 | di tali ·offese pos- | ⟨tali offese\|tali ·offese⟩ | A dark, round, raised point (about x-height middle) sits in the word space immediately before 'offese', separated from 'tali' by a space and touching-close to the 'o'. It is as dark as the type, so it could be a spurious sort or a printed point; it has no sense in the sentence, which favours treating it as a stray mark, but it is printed ink. |
