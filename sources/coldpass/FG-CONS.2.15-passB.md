---
unit: FG-CONS.2.15
reader: "cold reader fgB (Pass B, full)"
source: "Francesco Guicciardini, Considerazioni intorno ai Discorsi del Machiavelli, in Opere inedite, vol. 1, ed. Giuseppe Canestrini, Firenze 1857, pp. 68-69"
witness_images:
  check_method: "PIL; each part compared pixel for pixel (greyscale) with the stated row range cropped from its -full.png; md5 of every file computed and matched against the manifest"
  files:
    - {file: p68-full.png, size: 1367x2184, rows: 0-2184, md5: f8809babece695bfc602ae760496f2c3, md5_match: true}
    - {file: p68-part1of2.png, size: 1367x1179, rows: 0-1179, md5: 1519ed4996af0eff5ce97c8b3c5b130e, md5_match: true, identical_to_full_rows: true}
    - {file: p68-part2of2.png, size: 1367x1179, rows: 1005-2184, md5: 478edc9f58ec5d15333d33b0ee27e0dd, md5_match: true, identical_to_full_rows: true}
    - {file: p69-full.png, size: 1367x2184, rows: 0-2184, md5: 8a92e02754b6cdf6dc1cb707f7be923e, md5_match: true}
    - {file: p69-part1of2.png, size: 1367x1179, rows: 0-1179, md5: db747804f7e0a74659c130c3ba872708, md5_match: true, identical_to_full_rows: true}
    - {file: p69-part2of2.png, size: 1367x1179, rows: 1005-2184, md5: 56660a0b1dbd7e18dd61545f36d95888, md5_match: true, identical_to_full_rows: true}
boundaries:
  precedes: "p. 68, lines 1-6 of the text block: end of the consideration on ch. XIV, last words 'ancora che per sè stesse le pares- / sino di poco momento.' (p. 68 l. 6, full stop)"
  heading: "p. 68, centred, after a blank space below 'momento.' (ink rows 616-645 of p68-full)"
  rubric: "p. 68, two centred lines below the heading in smaller type (ink rows 710-776)"
  first_words: "p. 68, body l. 1: 'Da due cagioni procedono le ambiguità'"
  last_words: "p. 69, body l. 10 (10th line of the text block): 'se si fa deliberatamente può essere laudabile.(1)'"
  follows: "p. 69, after a blank space: heading 'CONSIDERAZIONE SUL CAPITOLO XIX' (no full stop visible), rubric in three lines 'Che gli acquisti nelle repubbliche non bene ordinate, e che secondo la / romana virtu (accent not visible) non procedono, sono a rovina, non a esaltazione di / esse.', first words 'Chi dubita che la città di Firenze, che la republica di / Vinegia sarebbono più deboli'"
headings_printed:
  heading: "CONSIDERAZIONE SUL CAPITOLO XV. — capitals and small capitals (initials C, C full capitals), roman numeral in full capitals, full stop after XV; centred; it does NOT say DEL LIBRO II"
  rubric: "Gli Stati deboli sempre fieno ambigui nel risolversi / e sempre le deliberazioni lente sono nocive — two lines, smaller roman type, centred (second line narrower), no closing punctuation visible"
running_heads_etc: "p. 68: page number '68' at left, running head 'CONSIDERAZIONI' centred in small capitals. p. 69: running head 'SUI DISCORSI DEL MACHIAVELLI' centred in small capitals, page number '69' at right. No signatures or catchwords visible. p. 68 shows a dark vertical line in the right margin (x c. 1345, scan/gutter artefact, not text); both pages carry a faint scanner watermark at bottom right (not transcribed). Footnote on p. 69 is separated from the text by a short rule."
paragraphing: "Left ink edge measured per line by pixel scan (ink < 128 grey, cols < 1300 on p. 68 to exclude the margin line). p. 68 body l. 1 starts at x=373, ll. 2-21 at x=311-313 (indent c. 62 px on l. 1 only). p. 69 body ll. 1-10 at x=127-131 (no indent). One paragraph; no line is indented after the opening. Footnote l. 1 on p. 69 starts at x=183, ll. 2-4 at x=131-132 (footnote first-line indent)."
body_word_count: 296
words_per_page: {p68: 204, p69: 92}
word_count_method: "Body only (heading, rubric and footnote excluded). Whitespace-delimited tokens containing a letter, preferred readings used; punctuation set off by spaces not counted. A hyphen-divided word counted once on the page where it begins (5 line-end hyphens, none across the page turn). Elisions: an elided form printed with a following space (l' una, L' altra, all' uno, a' Lavinii, s' ha, de' casi) counted as two words; 'all altro' counted as two."
uncertain_loci_per_page: {p68: 16, p69: 10}
uncertain_loci_total: 26
conventions: "Diplomatic, line for line; [p. N] at each page start; line-end hyphens kept; spaces before punctuation and after apostrophes reproduced as seen; accents as printed; no italics observed in the unit (etiam is roman); footnote call rendered as (1) in superscript position, written ^(1); doubts as ⟨preferred|alternative⟩. Rubric doubt (p. 68 rubric l. 2) is counted in p68's loci."
paths_written:
  - /home/claude/p34/readers/fgB/work/ (scratch crops: p68_*.png, p69_*.png, z68_*.png, zp68_*.png, zp69_*.png; z.py; body.txt)
  - /home/claude/p34/readers/fgB/out/FG-CONS.2.15-passB.md
---

# Heading

CONSIDERAZIONE SUL CAPITOLO XV.

# Rubric

Gli Stati deboli sempre fieno ambigui nel risolversi
⟨e|o⟩ sempre le deliberazioni lente sono nocive

# Body

[p. 68]
Da due cagioni procedono le ambiguità delle delibera-
zioni⟨:|;⟩ l' una da debolezza di quelli che hanno a risolvere,
non dico debolezza di forze e di potenza, ma debolezza di
prudenza e di ingegno , e questa cagione può cadere ⟨così|cosi⟩
in ⟨uno|nno⟩ principe come in una republica ⟨;|,⟩ e credo che quando
il Discorso disse gli Stati deboli, intese deboli di prudenza,
benchè la debolezza delle forze può in parte accrescere la
irresoluzione ⟨;|,⟩ perchè communemente e partiti che hanno
a pigliare gli Stati deboli, sono communemente più pieni
di difficultà e di periculi. L' altra cagione, che ⟨è|ò⟩ propria
delle republiche, è quando sono più uomini che hanno
a resolvere, e tra ⟨questi|qnesti⟩ sono le opinioni varie ; il che può
procedere o da malignità, perchè ⟨abbino|ahbino⟩ diversi fini, o pure
sanza malignità, perchè e ⟨giudicii|giudicu⟩ degli uomini non si con-
formino, come accade spesso etiam tra prudenti. E è vero
che queste ⟨sospensioni|sospensioni;⟩ communemente sono perniziose, per-
chè mentre stai sospeso non puoi provedere nè all' uno
caso nè ⟨all|all'⟩ altro⟨:|;⟩ e se qualche volta sono utili, come sa-
rebbe accaduto a' ⟨Lavinii|Lavinu⟩, e quali se fussino tardati ancora
tre o quattro dì più a resolversi, non arebbono patito pena
di quello poco viaggio , nondimeno questa ⟨è|ò⟩ una ⟨utilità|utilita⟩
[p. 69]
che risulta più presto per caso che ⟨altrimenti.|altrimenti⟩ La suspen-
sione è adunque da aborrire, la resoluzione sommamente
da laudare , ma ⟨s'|s`⟩ ha da avvertire che lo stare neutrale può
anche procedere per resoluzione, non per suspensione ⟨,|;⟩ nel
secondo caso la neutralità è reprensibile, nel primo può
essere e ⟨utile|u tile⟩ e perniziosa, secondo la qualità de' casi, di
che trattare non è ora materia ⟨nostra.|nostra⟩ Il medesimo dico
del differire qualche altra azione o esecuzione ⟨;|,⟩ chè se la
tardità procede da irresoluzione è sempre dannabile, ma
se si fa deliberatamente può essere laudabile.^(1)

# Notes on the page

p. 69, call ^(1) after "laudabile." (body l. 10, last line of the unit); note at foot of p. 69, below a short rule, smaller type, 4 lines:

^(1) ⟨Danna|Dauna⟩ il Machiavelli le deliberazioni ambigue, lente ⟨e|o⟩ tarde ,
⟨perchè|perché⟩ le ambigue nuocono alle pubbliche faccende con danno non solo,
ma vergogna della repubblica ; le lente e tarde, oltre che non aiutano,
possono mettere in pericolo lo ⟨Stato|Stato.⟩

No other footnote on p. 68 or p. 69.

# Uncertain loci

| # | page | line | locus | what you see | class |
|---|------|------|-------|--------------|-------|
| 1 | 68 | rubric 2 | ⟨e|o⟩ sempre | first letter of rubric l. 2 broken; closed bowl reads like o, but e expected | different word |
| 2 | 68 | 2 | zioni⟨:|;⟩ | faint grey dots after "zioni", no clear comma tail | mark-pointing |
| 3 | 68 | 4 | ⟨così|cosi⟩ | mark over final i may be a grave accent or a plain dot | accent |
| 4 | 68 | 5 | in ⟨uno|nno⟩ | first letter has n shape (u/n break) | non-word |
| 5 | 68 | 5 | republica ⟨;|,⟩ | comma with very faint dot above | mark-pointing |
| 6 | 68 | 8 | irresoluzione ⟨;|,⟩ | comma with faint grey dot above | mark-pointing |
| 7 | 68 | 10 | che ⟨è|ò⟩ propria | vowel under grave accent has a closed o-like bowl | different word |
| 8 | 68 | 12 | ⟨questi|qnesti⟩ | second letter shaped like n (u/n break) | non-word |
| 9 | 68 | 13 | ⟨abbino|ahbino⟩ | first b has h-like open bowl (h/b break) | non-word |
| 10 | 68 | 14 | ⟨giudicii|giudicu⟩ | final two letters joined like u (ii/u) | non-word |
| 11 | 68 | 16 | ⟨sospensioni|sospensioni;⟩ | final i has a tail below baseline, possibly a following punctuation mark | mark-pointing |
| 12 | 68 | 18 | ⟨all|all'⟩ altro | no apostrophe visible after "all" (cf. "all' uno" l. 17) | mark-pointing |
| 13 | 68 | 18 | altro⟨:|;⟩ | faint grey vertical dots, no clear comma tail | mark-pointing |
| 14 | 68 | 19 | ⟨Lavinii|Lavinu⟩ | final letters broken, read like "inu"/"iuii" | non-word |
| 15 | 68 | 21 | questa ⟨è|ò⟩ una | vowel under grave has a closed o-like bowl | different word |
| 16 | 68 | 21 | ⟨utilità|utilita⟩ | no clear grave over final a, only grey smear | accent |
| 17 | 69 | 1 | ⟨altrimenti.|altrimenti⟩ | only a faint grey speck after the word | mark-pointing |
| 18 | 69 | 3 | ⟨s'|s`⟩ ha | apostrophe slanted like a grave/backtick | mark-pointing |
| 19 | 69 | 4 | suspensione ⟨,|;⟩ | comma with faint grey above | mark-pointing |
| 20 | 69 | 6 | ⟨utile|u tile⟩ | gap between u and t (broken t) | spacing |
| 21 | 69 | 7 | ⟨nostra.|nostra⟩ | only a faint grey speck after the word | mark-pointing |
| 22 | 69 | 8 | esecuzione ⟨;|,⟩ | comma with faint grey dot above | mark-pointing |
| 23 | 69 | fn 1 | ⟨Danna|Dauna⟩ | second n broken, u-like | non-word |
| 24 | 69 | fn 1 | lente ⟨e|o⟩ tarde | letter reads like o (e/o break) | different word |
| 25 | 69 | fn 2 | ⟨perchè|perché⟩ | accent direction unclear at this resolution | accent |
| 26 | 69 | fn 4 | ⟨Stato|Stato.⟩ | no full stop visible after Stato | mark-pointing |
