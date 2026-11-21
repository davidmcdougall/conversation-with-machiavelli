---
unit: NM-DISC.2.14
reader: pass B sample
source: "Niccolò Machiavelli, Discorsi sopra la prima deca di Tito Livio, Italia [Firenze], 1824, Libro secondo, Capitolo XIV (end, p. 264) and eight line crops of p. 263"
witness_images:
  - file: img/p264-full.png
    size_px: 2057x3228
    bytes: 1161508
    note: "350 ppi native per brief; PNG carries no dpi tag. Running head '264' (page number, left) and 'DISCORSI' (small caps, centre) not transcribed."
  - file: img/p264-part1of3.png
    size_px: 2057x1205
    bytes: 484633
    check: "identical to full page rows 0-1205 (mean abs pixel diff 0.0); top third confirmed"
  - file: img/p264-part2of3.png
    size_px: 2057x1334
    bytes: 596724
    check: "identical to full page rows 947-2281 (mean abs pixel diff 0.0); middle third confirmed, overlaps part1 by 258 rows"
  - file: img/p264-part3of3.png
    size_px: 2057x1205
    bytes: 356866
    check: "identical to full page rows 2023-3228 (mean abs pixel diff 0.0); bottom third confirmed, overlaps part2 by 258 rows"
  - {file: img/p263-crop-a.png, size_px: 2057x65, bytes: 36650, check: "one printed line, full page width"}
  - {file: img/p263-crop-b.png, size_px: 2057x81, bytes: 37571, check: "one printed line (italic), full page width"}
  - {file: img/p263-crop-c.png, size_px: 2057x78, bytes: 35672, check: "one printed line, full page width"}
  - {file: img/p263-crop-d.png, size_px: 2057x75, bytes: 38492, check: "one printed line, full page width"}
  - {file: img/p263-crop-e.png, size_px: 2057x75, bytes: 37785, check: "one printed line, full page width"}
  - {file: img/p263-crop-f.png, size_px: 2057x68, bytes: 36066, check: "one printed line, full page width"}
  - {file: img/p263-crop-g.png, size_px: 2057x85, bytes: 38643, check: "one printed line, full page width; descender of the line above just visible at top edge"}
  - {file: img/p263-crop-h.png, size_px: 2057x75, bytes: 36610, check: "one printed line, full page width"}
boundaries:
  start: "p. 264, first text line below the running head: 'in tuo favore troverai i difensori più freddi, pa-' (continues Capitolo XIV from p. 263)"
  end: "p. 264, line 13: '... fia sempre partito prudente.' — last words of Capitolo XIV: 'partito prudente.'"
  follows: "Heading 'CAPITOLO XV' (capitals, centred); two-line italic chapter title beginning 'Gli Stati deboli sempre fieno ambigui nel risolversi,' and ending 'lente sono nocive.'; then the chapter text opening with a large initial 'In questa medesima materia, ...', running to the foot of the page ending 'rigua-'. Not transcribed. Non-text specks: a dot in the left margin at line 10, a dot above the end of the italic title, a short dash in the right margin beside the 7th line of Cap. XV."
sample_word_count: 109
word_count_method: "p. 264 transcription only (13 lines). Line-end hyphenated words rejoined and counted once (pa-rendo, Prin-cipi, ajutar-ti, ab-bia, confede-rati); text split on whitespace; punctuation not counted. An elided form printed solid counts as one word (l’arme = 1); one printed with a space after the apostrophe counts as two (s’ intende = 2). Splitting every elision at the apostrophe gives 110."
uncertain_loci_total: 4
conventions:
  - "Line for line as printed; line-end hyphens kept as printed (rendered '-')."
  - "Italic marked with *asterisks*."
  - "Apostrophe rendered ’; a visible space after an apostrophe is kept (s’ intende, l’ arroganza)."
  - "Accents transcribed as seen (all grave in this sample: più, già, però, starà)."
  - "The thin space the compositor sets before commas and semicolons (e.g. 'freddi ,', 'lui ,', 'stimare ;') is not recorded; punctuation is attached to the preceding word."
  - "In this face/scan the crossbar of e is sometimes too faint to see, so the letter looks like c; where that happens it is recorded as ⟨e|c⟩ and tabled."
  - "Uncertainty: ⟨preferred|alternative⟩."
---

# Page 264

in tuo favore troverai i difensori più freddi, pa-
rendo loro che tu sia o debole o vile. Ma se tu
subito scoperta la voglia dello avversario prepari
le forz⟨e|c⟩, ancora che elle siano inferiori a lui, quello
ti comincia a stimare; stimanti più gli altri Prin-
cipi allo intorno; e a tale viene voglia di ajutar-
ti, sendo in su l’arme, che abbandonandoti non
ti ajuterebbe mai. Questo s’ intende quando tu ab-
bia un inimico; ma quando ne avessi più, rendere
delle cose, che tu possedessi, ad alcuno di loro
per riguadagnarselo, ancora che fusse già scoperta
la guerra, e per smembrarlo dagli altri confede-
rati tuoi inimici, fia sempre partito prudente.

# Line crops of p. 263

## p263-crop-a

usate dal prefato Annio Pretore Latino nel me-

## p263-crop-b

*modestia, nisi a conscientia virium, et nostrarum,*

## p263-crop-c

*et suarum?* Conoscesi p⟨e|c⟩rtanto chiarissimo per

## p263-crop-d

crebbe l’ arroganza de’Latini. E però mai un Prin-

## p263-crop-e

cipe debbe vol⟨e|c⟩re mancare del grado suo, e non

## p263-crop-f

sa in termine che tu non la possa lasciare nel modo

## p263-crop-g

(d⟨e|c⟩tto) lasciarsela torre con le forze, che con la paura

## p263-crop-h

scoperta concesso quella, non starà saldo, ma ti

# Uncertain loci

| # | image | line | locus | what you see | class |
|---|---|---|---|---|---|
| 1 | p264-full.png (also part1of3) | 4 | forz⟨e\|c⟩ | final letter of "forze" shows bowl and terminal but no visible crossbar; looks like c ("forzc"). Read as e. | non-word |
| 2 | p263-crop-c.png | 1 | p⟨e\|c⟩rtanto | second letter has no visible crossbar, looks like c ("pcrtanto"); the e of "Conoscesi" on the same line has its bar. Read as e. | non-word |
| 3 | p263-crop-e.png | 1 | vol⟨e\|c⟩re | fourth letter has no visible crossbar, looks like c ("volcre"); the final e of the word has its bar. Read as e. | non-word |
| 4 | p263-crop-g.png | 1 | (d⟨e\|c⟩tto) | second letter has no visible crossbar, looks like c ("dctto"); the d is also lightly inked and its bowl reads almost as "cl". Read as "detto". | non-word |
