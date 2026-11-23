---
unit: FG-CONS.2.19
reader: "cold reader fgB (Pass B, full)"
source: "Francesco Guicciardini, Considerazioni intorno ai Discorsi del Machiavelli, in Opere inedite, vol. 1, ed. Giuseppe Canestrini, Firenze 1857, pp. 69-70"
witness_images:
  - {file: 1857-p069-page.png, size: 1367x2184, bytes: 750149, rows: 0-2184, sha256: deeeebaafa950198, check: "sha256 prefix and size match MANIFEST"}
  - {file: 1857-p069-part1of2-y0-1179.png, size: 1367x1179, bytes: 399508, rows: 0-1179, sha256: c333c30cd620cd8d, check: "matches MANIFEST; pixel-identical to page rows 0-1179"}
  - {file: 1857-p069-part2of2-y1005-2184.png, size: 1367x1179, bytes: 406619, rows: 1005-2184, sha256: 9c08978768c8db8d, check: "matches MANIFEST; pixel-identical to page rows 1005-2184"}
  - {file: 1857-p070-page.png, size: 1367x2184, bytes: 796406, rows: 0-2184, sha256: 3bfac7787b6a9665, check: "sha256 prefix and size match MANIFEST"}
  - {file: 1857-p070-part1of2-y0-1179.png, size: 1367x1179, bytes: 411271, rows: 0-1179, sha256: 6193e7429fd11bbf, check: "matches MANIFEST; pixel-identical to page rows 0-1179"}
  - {file: 1857-p070-part2of2-y1005-2184.png, size: 1367x1179, bytes: 450061, rows: 1005-2184, sha256: a20d5903ab37ee49, check: "matches MANIFEST; pixel-identical to page rows 1005-2184"}
boundaries:
  precedes: "End of the previous consideration (its heading is not on these pages): p. 69, text line 11 of the page (y 692-733): '... ma se si fa deliberatamente può essere laudabile.(1)' - footnote call (1) belongs to that preceding reply, not to XIX."
  heading: "p. 69, y 817-847, centred: 'CONSIDERAZIONE SUL CAPITOLO XIX' printed in small capitals (initial C of Considerazione and of Capitolo full capitals, rest small caps), roman numeral XIX in full capitals; no final punctuation; contains NO book number (no 'DEL LIBRO II')."
  rubric: "p. 69, y 923-1020, smaller type, hanging indent (first line flush left, turnovers indented), a declarative sentence (the Discorsi chapter title), 3 lines: 'Che gli acquisti nelle repubbliche non bene ordinate, e che secondo la' / 'romana virtù non procedono, sono a rovina, non a esaltazione di' / 'esse.' Final punctuation: a full stop, faint (only a grey trace) - see loci R1-R2."
  first_words: "Chi dubita che la città di Firenze (p. 69, body line 1, y 1086)"
  last_words: "... il che essere falsissimo mostrano largamente / e le ragioni e la esperienza. (p. 70, body line 12, y 790-828; final full stop only a grey trace)"
  follows: "p. 70, y 900-928: heading 'CONSIDERAZIONE SUL CAPITOLO XXIV' (same small-caps style, no book number; a faint grey speck after XXIV, not clearly a stop); rubric y 995-1025 'Le fortezze generalmente sono molto più dannose che utili' (one line, centred, no visible final stop); body begins 'Non si debbe laudare tanto la antiquità, che l' uomo' (indented)."
  line_numbering: "Body lines numbered from 1 on each page, counting only lines of this unit's body: p. 69 lines 1-12 (y 1086-1656), p. 70 lines 1-12 (y 255-828). Heading/rubric/footnote lines are not numbered."
headings_printed: "One heading for this unit: 'CONSIDERAZIONE SUL CAPITOLO XIX' (small caps). No book heading (DEL LIBRO II etc.) on either page. Neighbouring heading on p. 70: 'CONSIDERAZIONE SUL CAPITOLO XXIV'."
running_heads_etc: "p. 69: running head 'SUI DISCORSI DEL MACHIAVELLI' (caps) centred, page number '69' at right (y 198-223). p. 70: page number '70' at left, running head 'CONSIDERAZIONI' centred (y 195-224). No signatures and no catchwords on either page. p. 69: footnote rule (y ~1690) and footnote (1) of 4 lines, keyed to the preceding reply's text (call after 'laudabile.' at p. 69 text line y 692-733); not keyed to XIX. Stray marks: p. 69 a small tick/hyphen-like speck before 'vicino' (body line 5) and grey specks at the bottom-right margin (y ~1990); p. 70 a dark vertical bar at the right edge (x ~1330-1345, y ~400-1320, page-edge/binding shadow) and a 'Digitized by Google' watermark fragment at the bottom right. Neither the unit's text nor the following unit carries a footnote call on p. 70."
paragraphing: "Pixel scan of left ink edge (x of first dark pixel) per body line. p. 69: line 1 x=189; lines 2-12 x=130-134 -> line 1 indented (paragraph start), no other indentation. p. 70: lines 1-12 x=305-311 (page text block left margin ~305-311) -> no indented line; p. 70 line 1 continues the paragraph. The unit is a single paragraph."
body_word_count: 234
words_per_page: {p69: 120, p70: 114}
word_count_method: "Body only (heading, rubric, footnote excluded); preferred readings; tokens containing a letter (stand-alone ? ; , not counted); line-end-hyphenated words counted once on the line/page where they begin (aves-sino, mag-giori, condu-cono on p. 69; acqui-sti, do-minio, pre-sente, ca-gioni on p. 70); apostrophe-elided forms counted as separate words (da', de', dell'). Count made by script over the transcription in work/body.txt and corrected for the 7 continuation fragments."
uncertain_loci_per_page: {p69: 16, p70: 11}
uncertain_loci_total: 27
uncertain_loci_note: "Totals are body loci only. Further loci in rubric (R1-R2) and footnote (F1-F3) are listed separately below the table, not counted in the totals."
conventions: "Diplomatic, line for line; [p. N] at page start; line-end hyphens kept; spacing before punctuation (e.g. 'sono ?', 'potenza ,', 'mura ;') and after apostrophes ('de' re', 'da' quali', 'dell' ampliazione') kept as seen; no italics occur in the unit. ⟨preferred|alternative⟩ marks every doubtful letter or mark; ⟨x.|x⟩ / ⟨.|⟩ = full stop doubtful (only grey trace in bitonal scan); empty alternative = nothing printed. Small caps of heading given as described in boundaries, typed in caps."
paths_written:
  - /home/claude/w/readers/fgB/out/FG-CONS.2.19-passB.md
  - /home/claude/w/readers/fgB/work/ (scratch crops p69_*.png, p70_*.png, z69*.png, y*.png, r*.png, f*.png, e1.png; body.txt)
---

# Body

Rubric:
Che gli acquisti nelle repubbliche non bene ordinate, e che secondo la
romana ⟨virtù|virtu⟩ non procedono, sono a rovina, non a esaltazione di
⟨esse.|esse⟩

[p. 69]
Chi dubita ⟨che|cbe⟩ la città di Firenze, che la republica di
⟨Vinegia|Viuegia⟩ sarebbono più deboli e di minore potenza se aves-
sino rinchiuso il territorio loro tra piccoli confini ⟨che|cbe⟩ non
sono ? Avendo domato le città vicine, e ⟨allargato|allargalo⟩ la loro
jurisdizione, non è facile a ogni vicino assaltarle ⟨;|,⟩ non per
ogni debole accidente si travagliano ⟨;|,⟩ tengono, se non viene
moto grande, lo inimico fuora del tuorlo del suo Stato, non
si ⟨accosta|uccosta⟩ facilmente la guerra alle loro mura ⟨;|,⟩ lo avere
molti ⟨sudditi|suddit⟩ fa in molti modi le entrate publiche mag-
giori ⟨;|,⟩ fa la ⟨citta|città⟩ dominante in privato ⟨più|piú⟩ ricca⟨.|⟩ ⟨Co|Co'⟩ quali
mezzi se bene non sono armate di soldati ⟨proprii|propri⟩, condu-
cono ⟨de|de'⟩ forestieri, da' quali essere difeso è meglio che non
[p. 70]
essere difeso da alcuno⟨.|⟩ Confesso che una republica ⟨che|cho⟩
ha armi ⟨proprio|proprie⟩, è più potente e fa più capitale degli acqui-
sti ⟨;|,⟩ ma non confesserò già che una republica disarmata
diventi più debole, quanto più acquista ⟨;|,⟩ nè ⟨che|cbe⟩ Vinegia
che ora non teme de' re nè degli imperatori, se sanza do-
minio in terra e in mare, ⟨fussi|fnssi⟩ più sicura che non è di pre-
sente. Il che se fussi vero, non so perchè il Discorso si
⟨ristringa|ristrnga⟩ solo alle republiche ⟨;|,⟩ perchè per le medesime ca-
gioni ⟨uno|nno⟩ principe che non avessi armi proprie, caverebbe
degli acquisti e dell' ampliazione del dominio debolezza e
non potenza , il che essere falsissimo mostrano largamente
e le ragioni e la ⟨esperienza.|espertenza⟩

# Footnotes on the page

p. 69, below a rule (y 1713-1856). Call "(1)" printed as superscript after "laudabile." at the end of the PRECEDING consideration (p. 69 text line y 692-733); it belongs to that reply, not to the consideration on chapter XIX. The unit FG-CONS.2.19 has no footnote call. Text (line-divided):

(1) Danna il Machiavelli le deliberazioni ambigue, lente e tarde ,
perchè le ambigue nuocono alle pubbliche faccende con danno non solo,
ma vergogna della repubblica ⟨;|,⟩ le lente e tarde, oltre che non aiutano,
possono mettere in pericolo lo ⟨Stato|Stato.⟩

No footnote on p. 70.

# Uncertain loci

| # | page | line | locus | what you see | class |
|---|---|---|---|---|---|
| 1 | 69 | 1 | ⟨che\|cbe⟩ (Chi dubita che) | h printed with broken bowl, reads 'cbe' | same word, other form |
| 2 | 69 | 2 | ⟨Vinegia\|Viuegia⟩ | n reads as 'u' ('Viuegia'); 'Vinegia' printed cleanly on p. 70 l. 4 | same word, other form |
| 3 | 69 | 3 | ⟨che\|cbe⟩ (confini che non) | h broken, reads 'cbe' | same word, other form |
| 4 | 69 | 4 | ⟨allargato\|allargalo⟩ | the t has lost its crossbar, looks like l | different word |
| 5 | 69 | 5 | assaltarle ⟨;\|,⟩ | comma clear, upper dot only a grey trace | mark-pointing |
| 6 | 69 | 6 | travagliano ⟨;\|,⟩ | comma clear, upper dot faint | mark-pointing |
| 7 | 69 | 8 | ⟨accosta\|uccosta⟩ | first letter open like 'u', t of -sta looks like i ('uccosia') | same word, other form |
| 8 | 69 | 8 | mura ⟨;\|,⟩ | comma, upper dot faint grey | mark-pointing |
| 9 | 69 | 9 | ⟨sudditi\|suddit⟩ | final 'ti' fused/broken, reads 'suddiu' | same word, other form |
| 10 | 69 | 10 | giori ⟨;\|,⟩ | comma, upper dot faint | mark-pointing |
| 11 | 69 | 10 | ⟨citta\|città⟩ | no accent visible over final a (città elsewhere has visible grave) | mark-pointing |
| 12 | 69 | 10 | ⟨più\|piú⟩ | accent over u looks steep/acute-like in bitonal render | mark-pointing |
| 13 | 69 | 10 | ricca⟨.\|⟩ | only a grey speck after 'ricca' before capital 'Co' | mark-pointing |
| 14 | 69 | 10 | ⟨Co\|Co'⟩ quali | space between Co and quali, no apostrophe ink seen | mark-pointing |
| 15 | 69 | 11 | ⟨proprii\|propri⟩ | ending looks like 'u' (two undotted minims) = ii with lost dots, or i+broken letter | same word, other form |
| 16 | 69 | 12 | ⟨de\|de'⟩ forestieri | no apostrophe ink after 'de' | mark-pointing |
| 17 | 70 | 1 | alcuno⟨.\|⟩ | wide gap and grey trace only before capital 'Confesso' | mark-pointing |
| 18 | 70 | 1 | ⟨che\|cho⟩ (line end) | final e closed, reads 'cho' | same word, other form |
| 19 | 70 | 2 | ⟨proprio\|proprie⟩ | final letter appears as o ('armi proprio'); p.70 l.9 has 'armi proprie' | same word, other form |
| 20 | 70 | 3 | sti ⟨;\|,⟩ | comma with grey trace above | mark-pointing |
| 21 | 70 | 4 | acquista ⟨;\|,⟩ | comma with faint upper dot | mark-pointing |
| 22 | 70 | 4 | nè ⟨che\|cbe⟩ Vinegia | h broken, reads 'cbe' | same word, other form |
| 23 | 70 | 6 | ⟨fussi\|fnssi⟩ | u reads as n | same word, other form |
| 24 | 70 | 8 | ⟨ristringa\|ristrnga⟩ | second i after 'str' not visible | same word, other form |
| 25 | 70 | 8 | republiche ⟨;\|,⟩ | comma with faint upper dot | mark-pointing |
| 26 | 70 | 9 | ⟨uno\|nno⟩ | first letter reads as n | same word, other form |
| 27 | 70 | 12 | ⟨esperienza.\|espertenza⟩ | i reads like t ('espertenza'); final stop only a grey trace | same word, other form / mark-pointing |

Additional loci outside the body (not counted in totals):
- R1 | 69 | rubric l. 2 | ⟨virtù\|virtu⟩ | no accent visible on final u | mark-pointing
- R2 | 69 | rubric l. 3 | ⟨esse.\|esse⟩ | stop only a grey trace | mark-pointing
- F1 | 69 | footnote l. 3 | repubblica ⟨;\|,⟩ | comma with faint upper dot | mark-pointing
- F2 | 69 | footnote l. 4 | ⟨Stato\|Stato.⟩ | no final stop visible | mark-pointing
- F3 | 69 | footnote l. 1 | 'tarde ,' | spaced comma, ink clear (no doubt; noted for spacing) | mark-pointing
