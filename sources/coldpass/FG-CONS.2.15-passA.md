---
unit: FG-CONS.2.15
reader: "cold reader fgA (Pass A, full)"
source: "Francesco Guicciardini, Considerazioni intorno ai Discorsi del Machiavelli, in Opere inedite, vol. 1, ed. Giuseppe Canestrini, Firenze 1857, pp. 68-69"
witness_images:
  # every part verified pixel-identical (PIL, greyscale data compare) to the stated row range of its full page; md5 recomputed and matches the manifest
  - {file: p68-full.png, size: 1367x2184, rows: "0-2184", md5: f8809babece695bfc602ae760496f2c3, check: "md5 OK"}
  - {file: p68-part1of2.png, size: 1367x1179, rows: "0-1179", md5: 1519ed4996af0eff5ce97c8b3c5b130e, check: "md5 OK; pixel-identical to p68-full rows 0-1179"}
  - {file: p68-part2of2.png, size: 1367x1179, rows: "1005-2184", md5: 478edc9f58ec5d15333d33b0ee27e0dd, check: "md5 OK; pixel-identical to p68-full rows 1005-2184"}
  - {file: p69-full.png, size: 1367x2184, rows: "0-2184", md5: 8a92e02754b6cdf6dc1cb707f7be923e, check: "md5 OK"}
  - {file: p69-part1of2.png, size: 1367x1179, rows: "0-1179", md5: db747804f7e0a74659c130c3ba872708, check: "md5 OK; pixel-identical to p69-full rows 0-1179"}
  - {file: p69-part2of2.png, size: 1367x1179, rows: "1005-2184", md5: 56660a0b1dbd7e18dd61545f36d95888, check: "md5 OK; pixel-identical to p69-full rows 1005-2184"}
boundaries:
  precedes: "p. 68, text lines 1-6 (end of the consideration on chapter XIV): '... ancora che per sè stesse le pares- / sino di poco momento.' (p. 68 line 6, y 496-534)"
  heading: "p. 68, centred, y 616-645, after a blank gap of c. 80 px below the previous text"
  rubric: "p. 68, two centred lines in smaller type, y 710-776"
  first_words: "Da due cagioni procedono le ambiguità (p. 68, body line 1, y 834)"
  last_words: "se si fa deliberatamente può essere laudabile.(1) (p. 69, body line 10, y 692-733), followed by footnote call (1)"
  follows: "p. 69, heading 'CONSIDERAZIONE SUL CAPITOLO XIX' (no full stop; y 817-847); rubric in three lines with hanging indent: 'Che gli acquisti nelle repubbliche non bene ⟨ordinate|ordmtale⟩, e che secondo la / romana virtù non procedono, sono a rovina, non a ⟨esaltazione|esallazione⟩ di / esse.' (y 923-1020); first words 'Chi dubita che la città di Firenze, che la republica di / Vinegia sarebbono più deboli ...' (y 1086). Note: the next consideration printed is on chapter XIX, not XVI: no considerations on XVI-XVIII intervene."
headings_printed:
  heading: "CONSIDERAZIONE SUL CAPITOLO XV. — one centred line in caps and small caps (C, C capitals; rest small caps), roman numeral XV in full capitals, closing full stop. It does NOT say DEL LIBRO II (nor any book number)."
  rubric: "Gli Stati deboli sempre fieno ambigui nel risolversi / e sempre le deliberazioni lente sono nocive — two centred lines in smaller roman type, second line shorter and centred under the first; no final punctuation visible."
running_heads_etc: "p. 68: page number '68' at left of head line, running head 'CONSIDERAZIONI' centred in small caps (y 191-216). p. 69: running head 'SUI DISCORSI DEL MACHIAVELLI' centred in small caps, page number '69' at right (y 198-223). No signatures or catchwords on either page. A rule separates text from footnote on p. 69 (y c. 1690). Faint digitizer's watermark at bottom right of both pages (not transcribed). p. 68 shows a vertical dark bar at the right page edge (x c. 1345, y c. 330-1320), a scan artefact."
paragraphing: "Pixel scan (ink < 128) of left ink edge of every body line. p. 68 body lines 1-21: line 1 = x 373 (paragraph indent); lines 2-21 = x 311-313. p. 69 body lines 1-10: x 127-131 (page margin differs). Only the opening line is indented; no further indented lines: the unit is a single paragraph."
body_word_count: 296
words_per_page: {p68: 204, p69: 92}
word_count_method: "Body only (heading, rubric, footnote and footnote call excluded). Preferred reading of each ⟨|⟩ used. Whitespace-delimited tokens containing a letter; free-standing punctuation (' ; ', ' , ') not counted. A hyphen-divided word is counted once on the page where it begins (delibera-zioni, con-formino, per-chè, sa-rebbe on p. 68; suspen-sione on p. 69). Elisions: the printer sets a space after the apostrophe (l' una, L' altra, all' uno, a' Lavinii, s' ha, de' casi), so the elided form and the following word count as two words."
uncertain_loci_per_page: {p68: 19, p69: 14}
uncertain_loci_total: 33
conventions: "Diplomatic, line for line; [p. N] at page start. Line-end hyphens kept. Spelling, accents, apostrophes, capitals as printed; the printer's space after apostrophes and visible spaces before ' , ' and ' ; ' are kept as seen. ⟨preferred|alternative⟩ marks a doubt; preferred first. Footnote call rendered ⁽¹⁾ (printed as superscript (1)). No italic occurs in the unit. The bitonal scan breaks letters (e/o, u/n, c/e, h/b, t/i/l); breaks were marked where the printed letter is in doubt, and the image shapes are given as alternatives."
paths_written:
  - /home/claude/p34/readers/fgA/work/lines.py
  - /home/claude/p34/readers/fgA/work/body.txt
  - /home/claude/p34/readers/fgA/work/ (enlarged crops: p68*_L.png, p68*_R.png, p69*_L.png, p69*_R.png, p68rub0.png, p68rub1.png, z68_*.png, z69_*.png)
  - /home/claude/p34/readers/fgA/out/FG-CONS.2.15-passA.md
---

# Heading

[p. 68]
CONSIDERAZIONE SUL CAPITOLO XV.

# Rubric

Gli Stati deboli sempre fieno ambigui nel risolversi
⟨e|o⟩ sempre le deliberazioni ⟨lente|iente⟩ sono nocive

# Body

[p. 68]
Da due cagioni procedono le ambiguità delle delibera-
zioni⟨:|;⟩ l' una da debolezza di quelli che ⟨hanno|banno⟩ a risolvere,
non dico debolezza di forze e di potenza, ma debolezza di
prudenza e di ingegno , e questa cagione può cadere ⟨così|cosi⟩
in ⟨uno|nno⟩ principe come in una republica ; e credo che quando
il Discorso disse gli Stati deboli, intese deboli di prudenza,
benchè la debolezza delle forze può in parte accrescere la
irresoluzione ; perchè communemente e partiti che ⟨hanno|banno⟩
a pigliare gli Stati deboli, sono communemente più pieni
di difficultà e di periculi. L' altra cagione, che ⟨è|ò⟩ propria
delle republiche, è quando sono più uomini che hanno
a resolvere, e tra ⟨questi|qnesti⟩ sono le opinioni varie ; il che può
procedere o da malignità, perchè ⟨abbino|ahbino⟩ diversi fini, o pure
sanza malignità, perchè e ⟨giudicii|giudicu⟩ degli uomini non si con-
formino, come accade spesso ⟨etiam|etuam⟩ tra prudenti. E è vero
che queste ⟨sospensioni|sospensionj⟩ communemente sono perniziose, per-
chè mentre stai sospeso non puoi provedere nè all' uno
caso nè ⟨all|all'⟩ altro⟨:|;⟩ e se qualche volta sono ⟨utili|utih⟩, come sa-
rebbe accaduto a' ⟨Lavinii|Laviniu⟩, e quali se fussino tardati ancora
tre o quattro dì più a resolversi, non arebbono patito pena
di quello poco viaggio , nondimeno questa ⟨è|ò⟩ una ⟨utilità|utilita⟩
[p. 69]
che risulta più presto per caso che ⟨altrimenti|allrimcnti⟩⟨.|:⟩ La suspen-
sione è adunque da aborrire, la resoluzione ⟨sommamente|sommamentc⟩
da laudare , ma s' ha da avvertire che lo stare neutrale può
anche procedere per resoluzione, non per suspensione ⟨,|;⟩ nel
secondo caso la neutralità è reprensibile, nel primo può
essere e ⟨utile|u tile⟩ e perniziosa, secondo la qualità de' casi, di
che trattare non è ora materia nostra⟨.|:⟩ Il medesimo dico
del differire qualche altra azione o esecuzione ; chè se la
tardità procede da irresoluzione è sempre dannabile, ma
se si fa deliberatamente può essere laudabile.⁽¹⁾

# Notes on the page

Footnote on p. 69, below a rule; call ⁽¹⁾ at p. 69 body line 10, after "laudabile." (last word of the unit). First line indented.

[p. 69]
⁽¹⁾ ⟨Danna|Dauna⟩ il Machiavelli le deliberazioni ambigue, ⟨lente|lenle⟩ ⟨e|o⟩ tarde ,
⟨perchè|perché⟩ le ambigue nuocono alle pubbliche faccende con danno non solo,
ma vergogna della repubblica ; le lente e tarde, oltre che non ⟨aiutano|aiulano⟩,
⟨possono|possouo⟩ ⟨mettere|meltere⟩ in pericolo lo ⟨Stato|Stato.⟩

No footnote on p. 68.

# Uncertain loci

| # | page | line | locus | what you see | class |
|---|---|---|---|---|---|
| 1 | 68 | rubric 2 | ⟨e|o⟩ sempre | first letter a closed round glyph, e or o | different word |
| 2 | 68 | rubric 2 | ⟨lente|iente⟩ | first stroke short-topped, l or i | non-word |
| 3 | 68 | 2 | zioni⟨:|;⟩ | faint grey two-dot mark after zioni | mark-pointing |
| 4 | 68 | 2 | ⟨hanno|banno⟩ | first letter b-shaped (h/b break) | non-word |
| 5 | 68 | 4 | ⟨così|cosi⟩ | mark over final i: accent or plain dot | accent |
| 6 | 68 | 5 | ⟨uno|nno⟩ | first letter reads n (u/n break) | non-word |
| 7 | 68 | 8 | ⟨hanno|banno⟩ | first letter b-shaped | non-word |
| 8 | 68 | 10 | ⟨è|ò⟩ propria | accented round vowel, closed bowl like o | different word |
| 9 | 68 | 12 | ⟨questi|qnesti⟩ | second letter n-shaped | non-word |
| 10 | 68 | 13 | ⟨abbino|ahbino⟩ | second letter h-shaped | non-word |
| 11 | 68 | 14 | ⟨giudicii|giudicu⟩ | final ii fused into a u shape | non-word |
| 12 | 68 | 15 | ⟨etiam|etuam⟩ | ti fused, reads tu | non-word |
| 13 | 68 | 16 | ⟨sospensioni|sospensionj⟩ | final i with a descender-like tail | non-word |
| 14 | 68 | 18 | ⟨all|all'⟩ altro | no apostrophe visible after all (cf. all' uno, l. 17) | mark-pointing |
| 15 | 68 | 18 | altro⟨:|;⟩ | faint grey vertical mark after altro | mark-pointing |
| 16 | 68 | 18 | ⟨utili|utih⟩ | last letters read h | non-word |
| 17 | 68 | 19 | ⟨Lavinii|Laviniu⟩ | final ii fused | non-word |
| 18 | 68 | 21 | ⟨è|ò⟩ una | accented round vowel, closed like o | different word |
| 19 | 68 | 21 | ⟨utilità|utilita⟩ | no clear accent over final a; grey specks only | accent |
| 20 | 69 | 1 | ⟨altrimenti|allrimcnti⟩ | t reads l, e reads c | non-word |
| 21 | 69 | 1 | altrimenti⟨.|:⟩ | faint low point after the word | mark-pointing |
| 22 | 69 | 2 | ⟨sommamente|sommamentc⟩ | final e open like c | non-word |
| 23 | 69 | 4 | suspensione ⟨,|;⟩ | comma, possible faint point above | mark-pointing |
| 24 | 69 | 6 | ⟨utile|u tile⟩ | gap after u | spacing |
| 25 | 69 | 7 | nostra⟨.|:⟩ | faint grey point after nostra | mark-pointing |
| 26 | 69 | note 1 | ⟨Danna|Dauna⟩ | second n reads u | non-word |
| 27 | 69 | note 1 | ⟨lente|lenle⟩ | t reads l | non-word |
| 28 | 69 | note 1 | ⟨e|o⟩ tarde | closed round letter, e or o | different word |
| 29 | 69 | note 2 | ⟨perchè|perché⟩ | accent direction unclear | accent |
| 30 | 69 | note 3 | ⟨aiutano|aiulano⟩ | t reads l | non-word |
| 31 | 69 | note 4 | ⟨possono|possouo⟩ | n reads u | non-word |
| 32 | 69 | note 4 | ⟨mettere|meltere⟩ | first t reads l | non-word |
| 33 | 69 | note 4 | ⟨Stato|Stato.⟩ | no closing point visible | mark-pointing |
