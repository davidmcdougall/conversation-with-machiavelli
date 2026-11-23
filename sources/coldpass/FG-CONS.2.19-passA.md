---
unit: FG-CONS.2.19
reader: "cold reader fgA (Pass A, full)"
source: "Francesco Guicciardini, Considerazioni intorno ai Discorsi del Machiavelli, in Opere inedite, vol. 1, ed. Giuseppe Canestrini, Firenze 1857, pp. 69-70"
witness_images:
  - file: 1857-p069-page.png
    size: [1367, 2184]
    rows: 0-2184
    sha256_prefix: deeeebaafa950198
    check: "matches MANIFEST (size, sha256 prefix)"
  - file: 1857-p069-part1of2-y0-1179.png
    size: [1367, 1179]
    rows: 0-1179
    sha256_prefix: c333c30cd620cd8d
    check: "matches MANIFEST; pixel-identical to rows 0-1179 of 1857-p069-page.png"
  - file: 1857-p069-part2of2-y1005-2184.png
    size: [1367, 1179]
    rows: 1005-2184
    sha256_prefix: 9c08978768c8db8d
    check: "matches MANIFEST; pixel-identical to rows 1005-2184 of 1857-p069-page.png"
  - file: 1857-p070-page.png
    size: [1367, 2184]
    rows: 0-2184
    sha256_prefix: 3bfac7787b6a9665
    check: "matches MANIFEST (size, sha256 prefix)"
  - file: 1857-p070-part1of2-y0-1179.png
    size: [1367, 1179]
    rows: 0-1179
    sha256_prefix: 6193e7429fd11bbf
    check: "matches MANIFEST; pixel-identical to rows 0-1179 of 1857-p070-page.png"
  - file: 1857-p070-part2of2-y1005-2184.png
    size: [1367, 1179]
    rows: 1005-2184
    sha256_prefix: a20d5903ab37ee49
    check: "matches MANIFEST; pixel-identical to rows 1005-2184 of 1857-p070-page.png"
  - note: "All six files pass. Images are stored as RGB with 256 grey levels (anti-aliased), not strictly bitonal; letter breakage as described in the brief is present throughout (i-dots and some accents/upper dots of semicolons drop out, t/l, n/u, h/b, e/c, e/o, a/u confusions)."
boundaries:
  precedes: "p. 69, text line 10 (running head excluded): 'se si fa deliberatamente può essere laudabile.(1)' — end of the preceding consideration (its heading is not on these pages); its footnote call (1) is here."
  heading: "p. 69, text line 11 (y≈817-847), centred: 'CONSIDERAZIONE SUL CAPITOLO XIX' set in capitals and small capitals (large C of Considerazione and of Capitolo, rest small caps; numeral in full capitals) = Considerazione sul Capitolo XIX. No final punctuation visible. No book number (no 'DEL LIBRO II' or similar)."
  rubric: "p. 69, text lines 12-14, smaller type, hanging indent (first line at the measure, runovers indented): 'Che gli acquisti nelle repubbliche non bene ordinate, e che secondo la / romana virtù non procedono, sono a rovina, non a esaltazione di / esse.' Type: Italian summary of the Discorsi chapter's title (declarative sentence), 3 lines; final punctuation: a faint grey mark after 'esse' taken as a full stop (doubtful)."
  first_words: "p. 69, body line 1 (indented): 'Chi dubita che la città di Firenze'"
  last_words: "p. 70, body line 12: 'e le ragioni e la esperienza.' (final full stop faint, doubtful)"
  follows: "p. 70, text line 13: heading 'CONSIDERAZIONE SUL CAPITOLO XXIV' (caps + small caps, faint speck after XXIV, probably dirt), rubric one line centred 'Le fortezze generalmente sono molto più dannose che utili' (accent on più not visible; no final punctuation visible), body begins 'Non si debbe laudare tanto la antiquità, che l' uomo'."
  line_numbering: "Body lines numbered 1-12 on each page from the first line of the unit's body on that page. p. 69 body lines 1-12 = text lines 15-26 counting from the first text line below the running head (heading and rubric lines included in that count); p. 70 body lines 1-12 = text lines 1-12 below the running head. Rubric lines numbered R1-R3."
headings_printed: "Unit heading: 'Considerazione sul Capitolo XIX' (caps/small caps, no book number, no punctuation). Following heading on p. 70: 'Considerazione sul Capitolo XXIV' (so chapters XX-XXIII have no consideration in this edition)."
running_heads_etc: "p. 69: running head 'SUI DISCORSI DEL MACHIAVELLI' (small caps, centred) with page number '69' at right. p. 70: page number '70' at left, running head 'CONSIDERAZIONI' (small caps, centred). No signature marks and no catchwords on either page. p. 69 has a footnote rule and one footnote (call (1)) belonging to the preceding unit. Stray marks: faint scanner/digitiser watermark fragments at lower right of both pages ('...Goo..' fragment on p. 70, unreadable smudges on p. 69); a dark vertical bar at the right edge of p. 70 (page edge/gutter of the scan); faint grey specks between lines throughout."
paragraphing: "Left ink edge scanned on every body line. p. 69: body line 1 left edge x=189, lines 2-12 x=130-134 -> line 1 indented (paragraph start). p. 70: lines 1-12 x=305-311 (page block left margin ≈305-311) -> no indented lines. The unit is a single paragraph. (For comparison the next unit's first line on p. 70 starts at x=367, indented.)"
body_word_count: 234
words_per_page: {p69: 120, p70: 114}
word_count_method: "Body only (heading, rubric, footnote excluded); preferred readings; tokens containing a letter (punctuation-only tokens such as '?' ';' ',' not counted); line-end hyphenated words (aves-sino, mag-giori, condu-cono, acqui-sti, do-minio, pre-sente, ca-gioni) counted once on the page where they begin (no word is divided across the page break: p. 69 ends 'che non'); apostrophe-elided forms counted separately (da' quali = 2, de' re = 2, dell' ampliazione = 2). Counted by script on the transcription."
uncertain_loci_per_page: {p69: 20, p70: 13, rubric_p69: 7}
uncertain_loci_total: "33 in the body (p69 20, p70 13); plus 7 in the rubric (p69) listed separately in the table = 40 overall"
conventions: "Diplomatic, line for line; [p. N] at page start; line-end hyphens kept; spelling, accents, capitals, apostrophes and spaces before punctuation (e.g. 'sono ?', 'assaltarle ;', 'potenza ,') as printed; no italic occurs in the unit. ⟨preferred|alternative⟩ marks doubt; ⟨x|⟩ means alternative is no mark at all. Damaged letters whose reading is certain (missing i-dots, etc.) are silently given; damaged letters where a different letter is visibly possible are marked. Semicolons whose upper dot is only a faint grey speck are marked ⟨;|,⟩."
paths_written:
  - /home/claude/w/readers/fgA/out/FG-CONS.2.19-passA.md
  - /home/claude/w/readers/fgA/work/ (scratch crops and body.txt)
---

# Body

Rubric: Che gli acquisti ⟨nelle|uelle⟩ repubbliche non ⟨bene|belle⟩ ⟨ordinate|ordinale⟩, e che ⟨secondo|secoıkfo⟩ la
romana ⟨virtù|virtu⟩ non procedono, sono a rovina, non a ⟨esaltazione|esallazione⟩ di
esse⟨.|⟩

[p. 69]
Chi dubita ⟨che|cbe⟩ la città di Firenze, che la republica di
⟨Vinegia|Viuegia⟩ sarebbono più deboli e di minore potenza se aves-
sino ⟨rinchiuso|rincliiuso⟩ il territorio loro tra piccoli confini ⟨che|cbe⟩ non
sono ? Avendo domato le città vicine, e ⟨allargato|allargalo⟩ la loro
jurisdizione, non è facile a ogni vicino assaltarle ⟨;|,⟩ non per
ogni ⟨debole|dcbole⟩ accidente si travagliano ⟨;|,⟩ ⟨tengono|lengono⟩, se non viene
moto grande, lo inimico fuora del tuorlo del suo Stato⟨;|,⟩ non
si ⟨accosta|uccosla⟩ facilmente la guerra ⟨alle|allc⟩ loro mura ⟨;|,⟩ lo avere
molti sudditi fa in molti modi le entrate publiche mag-
giori ⟨;|,⟩ fa la ⟨città|citta⟩ dominante in privato più ricca⟨.|,⟩ ⟨Co|Co'⟩ quali
mezzi se bene non sono ⟨armate|armale⟩ di soldati ⟨proprii|propri⟩, condu-
cono ⟨de|de'⟩ forestieri, da' quali essere difeso è meglio che non
[p. 70]
essere difeso da alcuno⟨.|⟩ Confesso che una republica ⟨che|cho⟩
ha armi ⟨proprio|proprie⟩, è ⟨più|piu⟩ potente e fa più capitale degli acqui-
sti ⟨;|,⟩ ma non confesserò già che una republica disarmata
diventi più debole, quanto più acquista ⟨;|,⟩ nè che Vinegia
che ora non teme de' re nè degli imperatori, se sanza do-
minio in terra e in mare, ⟨fussi|fassi⟩ più sicura che non è di pre-
sente. Il che se fussi vero, non so perchè il Discorso si
ristringa solo alle republiche ⟨;|,⟩ perchè per le medesime ca-
gioni ⟨uno|nno⟩ principe che non avessi armi proprie, caverebbe
degli acquisti e ⟨dell' |dell'⟩⟨ampliazione|amphazione⟩ del dominio debolezza e
non potenza , il che essere falsissimo mostrano largamente
e le ragioni e la ⟨esperienza|espertenza⟩⟨.|⟩

# Footnotes on the page

p. 69, below a rule, one footnote, smaller type. Its call "(1)" (superscript) stands in the text of the PRECEDING unit (the consideration ending at p. 69 text line 10, after "laudabile."); it is not keyed to FG-CONS.2.19. There is no footnote and no call on p. 70 and none in the text of FG-CONS.2.19.

(1) Danna il Machiavelli le deliberazioni ambigue, lente e tarde ⟨,|;⟩
⟨perchè|perché⟩ le ambigue nuocono alle pubbliche faccende con danno non solo,
ma ⟨vergogna|vergogua⟩ della repubblica ⟨;|,⟩ le lente e tarde, oltre che non aiutano,
⟨possono|possouo⟩ mettere in pericolo lo Stato⟨.|⟩

(Footnote type is heavily broken: 'Dauna', 'Machiavelh', 'aiulano', 'meltere' as they appear; readings above are preferred. Footnote doubts are not counted in the unit's loci.)

# Uncertain loci

| # | page | line | locus | what you see | class |
|---|---|---|---|---|---|
| 1 | 69 | R1 | nelle | first letter looks u ("uelle") | same word, other form (alt. non-word) |
| 2 | 69 | R1 | bene | "beııe": two minims after e could be n or ll ("belle") | different word |
| 3 | 69 | R1 | ordinate | "ordıııale": minims + t/l break; t or l before final e | different word |
| 4 | 69 | R1 | secondo | "secoıkfo": n and d broken | same word, other form (alt. non-word) |
| 5 | 69 | R2 | virtù | no grave visible on final u | mark-pointing |
| 6 | 69 | R2 | esaltazione | t looks l ("esallazione") | same word, other form (alt. non-word) |
| 7 | 69 | R3 | esse. | faint grey speck at baseline after esse | mark-pointing |
| 8 | 69 | 1 | che (2nd word "cbe") | h with broken shoulder looks b | same word, other form (alt. non-word) |
| 9 | 69 | 2 | Vinegia | n reads as u ("Viuegia") | same word, other form (alt. non-word) |
| 10 | 69 | 3 | rinchiuso | h broken ("rincliiuso") | same word, other form (alt. non-word) |
| 11 | 69 | 3 | che ("cbe") | h/b as at line 1 | same word, other form (alt. non-word) |
| 12 | 69 | 4 | allargato | final t looks l ("allargalo") | different word |
| 13 | 69 | 5 | assaltarle ; | comma clear, upper dot only a grey speck | mark-pointing |
| 14 | 69 | 6 | debole | first e looks c ("dcbole") | same word, other form (alt. non-word) |
| 15 | 69 | 6 | travagliano ; | comma clear, upper dot faint grey | mark-pointing |
| 16 | 69 | 6 | tengono | t looks l ("lengono") | same word, other form (alt. non-word) |
| 17 | 69 | 7 | Stato; | grey speck above comma | mark-pointing |
| 18 | 69 | 8 | accosta | a looks u, t looks l ("uccosla") | same word, other form (alt. non-word) |
| 19 | 69 | 8 | alle | final e looks c ("allc") | same word, other form (alt. non-word) |
| 20 | 69 | 8 | mura ; | upper dot faint | mark-pointing |
| 21 | 69 | 10 | giori ; | upper dot faint grey | mark-pointing |
| 22 | 69 | 10 | città | no accent visible on final a ("citta") | mark-pointing |
| 23 | 69 | 10 | ricca. | only a faint grey dot after ricca | mark-pointing |
| 24 | 69 | 10 | Co quali | no apostrophe visible after Co; grey speck nearby (Co' possible) | mark-pointing |
| 25 | 69 | 11 | armate | t looks l ("armale") | same word, other form (alt. non-word) |
| 26 | 69 | 11 | proprii | after r a u-shaped pair of minims, read ii; could be propri + damage | same word, other form |
| 27 | 69 | 12 | de forestieri | no apostrophe visible (de' possible) | mark-pointing |
| 28 | 70 | 1 | alcuno. | faint grey at baseline only; next word capitalised | mark-pointing |
| 29 | 70 | 1 | che (line end, "cho") | final e looks o | same word, other form (alt. non-word) |
| 30 | 70 | 2 | proprio | final letter clean o (e/o confusion possible; context "armi proprie" at line 9) | same word, other form |
| 31 | 70 | 2 | più (1st) | accent not clearly visible ("piu") | mark-pointing |
| 32 | 70 | 3 | sti ; | upper dot faint | mark-pointing |
| 33 | 70 | 4 | acquista ; | upper dot faint grey | mark-pointing |
| 34 | 70 | 6 | fussi | second letter ambiguous u/a ("fassi") | different word |
| 35 | 70 | 8 | republiche ; | upper dot faint | mark-pointing |
| 36 | 70 | 9 | uno | u reads as n ("nno") | same word, other form (alt. non-word) |
| 37 | 70 | 10 | dell' ampliazione (spacing) | visible gap after apostrophe; could be dell'ampliazione | mark-pointing |
| 38 | 70 | 10 | ampliazione | li reads as h ("amphazione") | same word, other form (alt. non-word) |
| 39 | 70 | 12 | esperienza | i looks t ("espertenza") | same word, other form (alt. non-word) |
| 40 | 70 | 12 | esperienza. | faint grey speck at baseline after final a | mark-pointing |

(Loci 1-7 are in the rubric; loci 8-27 = p. 69 body (20); loci 28-40 = p. 70 body (13).)
