---
unit: NM-DISC.3.17
reader: "cold reader (comparison read), images only"
source: "Machiavelli, Discorsi, Libro terzo, Venice: Domenico Giglio, 1554; fols. 178v-179r; page images only"
witness_images:
  - {file: 1554-fol178v-page.png, size: "1625x3209", rows: "0-3209", sha256_16: 65f3b095858f58ef, check: "size and full sha256 match manifest"}
  - {file: 1554-fol178v-part1of3-y0-1197.png, size: "1625x1197", rows: "0-1197", sha256_16: c9a157a69922c65f, check: "size and sha256 match; pixel-identical to page rows 0-1197"}
  - {file: 1554-fol178v-part2of3-y941-2266.png, size: "1625x1325", rows: "941-2266", sha256_16: 995063b85db8a347, check: "size and sha256 match; pixel-identical to page rows 941-2266"}
  - {file: 1554-fol178v-part3of3-y2010-3209.png, size: "1625x1199", rows: "2010-3209", sha256_16: 16a554c16a2a61ee, check: "size and sha256 match; pixel-identical to page rows 2010-3209"}
  - {file: 1554-fol179r-page.png, size: "1639x3244", rows: "0-3244", sha256_16: 8864e6365e722626, check: "size and full sha256 match manifest"}
  - {file: 1554-fol179r-part1of3-y0-1211.png, size: "1639x1211", rows: "0-1211", sha256_16: ba34ca3d9aad9f57, check: "size and sha256 match; pixel-identical to page rows 0-1211"}
  - {file: 1554-fol179r-part2of3-y951-2292.png, size: "1639x1341", rows: "951-2292", sha256_16: 52ca991e5038ef31, check: "size and sha256 match; pixel-identical to page rows 951-2292"}
  - {file: 1554-fol179r-part3of3-y2032-3244.png, size: "1639x1212", rows: "2032-3244", sha256_16: f3b1fcc7b9b1424c, check: "size and sha256 match; pixel-identical to page rows 2032-3244"}
manifest_check: "PASS: all 8 files match manifest pixel size and full sha256; all 6 part images are pixel-identical (numpy array_equal) to the stated rows of their -page image (script work/check.py)"
boundaries: {precedes: "end of Cap. XVI, fol. 178v page line 15: '...come nel ſeguente capitolo ſi diſcorrera.'", heading_page_line: "fol. 178v, three heading lines between page body lines 15 and 16", body_first_words: "fol. 178v line 16 (unit line 1): 'DEbbe una Rep. aſsai conſiderare'", body_last_words: "fol. 179r line 25: 'per mille / inopinate uie ſi cauſa la ſua rouina.'", follows: "fol. 179r, heading 'NIVNA COSA E PIV DEGNA DI / un Capitano, che preſentire i partiti del ne- / mico. Capitolo. XVIII.'; first words 'DIceua Epaminunda Tebano,neſſuna coſa eſſer'"}
headings_printed: {heading: "CHE NON SI OFFENDA VNO ET / poi quel medeſimo ſi mãdi in amminiſtratione, / et gouerno d'importanza. Cap. XVII.", type: "line 1 spaced roman capitals; lines 2-3 italic lower case, centred/indented, 'Cap. XVII.' in roman (Cap. upper-and-lower, XVII small capitals)", lines: 3, final_stop: "yes, a stop is printed after XVII"}
running_heads_etc: {fol_178v: "running head 'LIBRO' (spaced capitals); folio number top left largely lost, only ink fragments visible, number not readable", fol_179r: "running head 'TERZO.' (spaced capitals, stop); folio number '179' top right", signatures: "none visible on either page", catchwords: "none visible on either page", stray_marks: "178v: faint vertical dot-pairs in right margin (x~1530) after page lines 16, 17, 18, 23, 24, 25; a speck below 'mãdi' in heading line 2; a dot under the text block bottom left (~x208,y3020); 179r: dot in left margin before lines 6 and 21, colon-like speck before line 8, stray mark right of running head, speck between 're' and 'quanto' (line 20, not read as a stop)"}
leaf_condition: {fol_178v: "no tears or losses in the text; every line of the unit legible; folio number at head of page lost/unreadable (fragments only); dark gutter shadow along the right edge (inner margin) not touching the text; light show-through; some damaged sorts (line 31 'et' with t barely formed; line 30 marks over 'li')", fol_179r: "no tears or losses; every line legible; gutter shadow along the left edge not touching text; light show-through; some worn/broken sorts (line 9 'neceſsita' i broken into dots; line 8 'Claudio' with wide C-l spacing)"}
footnotes: "none; no marginal notes"
paragraphing: "One printed paragraph. Opens with a 3-line drop initial D (ink x~107-371, page lines 16-18 of 178v; text beside it starts x~398). Left ink edges of other unit lines: 178v 105-116 px (gradual skew, no indent); 179r 69-82 px (line 24 'dinare' at 82 is a word continuation, not an indent). No indented line within the unit."
line_numbering: "Body lines counted per page from the first body line on the page, as instructed: on 178v lines 1-15 belong to Cap. XVI, the unit occupies 178v lines 16-31 (unit lines 1-16); on 179r the unit occupies lines 1-25. Running heads, folio numbers and headings not counted."
body_word_count: 310
words_per_page: {178v: 119, 179r: 191}
word_count_method: "work/wc.py on work/body.txt: preferred reading of each doubt; whitespace tokens; elided forms split after apostrophe (d'eſſo = 2); only tokens containing a letter (the stand-alone ',' tokens excluded); any word divided at line end, hyphenated or not (Mar|ca, occa|ſione, s'e|ra, domanda|to, etc.), counted once on the line/page where it begins. Heading excluded."
uncertain_loci_total: 6
conventions: "Diplomatic, line for line. Long s as ſ; italic ß ligature transcribed as ſs (aſsai, pericoloſiſsimo, neceſsita, paſsioni, poſsino, impoſsibile); tilde/macron over vowel as combining tilde (cõ, grã, ẽ, nõ, quã); p with stroke through descender (per) kept as ꝑ; u/v, i/j as printed; accents as printed (andò, città, egliè). The body is italic throughout, so italic is not marked with *...*; roman capitals within the italic (R, A, N, C, S, E, I) transcribed as ordinary capitals. Drop initial D transcribed as ordinary capital joined to its word. Printed line-end hyphens (double-stroke) given as '-'. Spaces around punctuation kept where clearly printed (' , ', ' . ')."
paths_written: ["/home/claude/p37/readers/g1554/work/ (check.py, lines.py, wc.py, body.txt, crops v_*.png r_*.png L*.png S_*.png z*.png)", "/home/claude/p37/readers/g1554/out/NM-DISC.3.17-1554.md"]
---

# Body

CHE NON SI OFFENDA VNO ET
poi quel medeſimo ſi mãdi in ⟨amminiſtratione,|amminiſtratione.⟩
et gouerno d'importanza. Cap. XVII.

[fol. 178v]
DEbbe una Rep. aſsai conſiderare , di non
preporre alcuno ad alcuna importante
amminiſtratione,alquale ſia ſtato fatto
da altri alcuna notabile ingiuria. Claudio Nerone
(ilquale ſi parti dall'eſſercito, che haueua a fronte
ad Annibale,et con parte d'eſſo n'andò nella Mar
ca a trouare l'altro Conſolo,per cõbattere con Aſ-
drubale,auanti che ſi congiugeſſe con Annibale)⟨s'e|s'e-⟩
ra trouato ꝑ lo adietro in Iſpagna a fronte ⟨d'Aſdru|d'Aſdru-⟩
bale,et hauendolo ſerrato in luogo con lo eſſercito,
che biſogna o che Aſdrubale cõbatteſſe con ſuo diſa-
uantaggio,o ſi moriſſe di fame, fu Aſdrubale aſtu-
tamente tanto intrattenuto con certe prattiche di
accordo,che gli uſci di ſotto,et tolſegli quella occa
ſione d'oppreſſarlo . Laqual coſa ſaputa a Roma ⟨li|lì⟩
dette carico grãde appreſſo al Senato,⟨et|e:⟩ al popolo,
[fol. 179r]
et di lui fu parlato dishoneſtamẽte per tutta quel-
la città,non ſenza ſuo grãde dishonore,et isdegno:
ma eſſendo poi fatto Conſolo et mandato all'incon
tro d'Annibale,preſe il ſopraſcritto partito,ilquale
fu pericoloſiſsimo, talmente che Roma ſtette tutta
dubbia,et ſolleuata infino a tanto , che uennono le
nuoue della rotta d' Aſdrubale: et eſſendo domanda
to poi Claudio , per quale cagione haueſſe preſo ⟨ſi|ſi.⟩
pericoloſo partito, doue ſenz'una eſtrema neceſsita
egli haueua giocata quaſi la liberta di Roma.riſpo
ſe,che l'haueua fatto perche ſapeua,che ſe gli riuſci
ua,racquiſtaua quella gloria,che s'haueua perduta
in Iſpagna.et ſe non gli riuſciua, et che queſto ſuo
partito haueſſe hauuto cõtrario fine,ſapeua,come ei
ſi uẽdicaua contra a quella citta,et a quelli cittadi
ni,che l'haueuano tanto ingratamẽte, et indiſcreta
mente offeſo.Et quãdo queſte paſsioni di tale offe-
ſe poſſono tanto in un cittadino Ro.et in quei tem
pi che Roma anchora era incorrotta,ſi debbe penſa
re quanto elle poſsino in un cittadino d'una citta,
che non ſia fatta,come era allhora quella:e perche a
ſimili diſordini, che naſcono nelle Rep.nõ ſi puo da-
re certo rimedio,ne ſeguita, che egliè impoſsibile or
dinare una Republica perpetua , perche per mille
inopinate uie ſi cauſa la ſua rouina.

# Notes on the page

178v: the unit begins below Cap. XVI, whose last words are 'come nel ſeguente capitolo ſi diſcorrera.' (page line 15). Heading in three lines, first in spaced capitals, then two italic lines; 'Cap. XVII.' roman. Drop initial D, three lines deep. 'Rep.' line 16 with a raised point. 'da altri' (unit line 4): the d stands slightly raised/displaced. 'ꝑ' (unit line 9): p with a crossing stroke on the descender, the per-contraction, not expanded. Unhyphenated line divisions: Mar|ca, s'e|ra, Aſdru|bale, occa|ſione. Faint dot-pairs in the right margin at the ends of several lines (including after 'non' and 'importante', where no word is divided) look like stray/blind marks rather than hyphens; the printed hyphen in this setting is a clear double stroke (Aſ-, diſa-, aſtu-).
179r: 'quel-' with printed hyphen; 'd' Aſdrubale' (line 7) has a space after the apostrophe and a smaller capital A; 'C laudio' (line 8) printed with a wide gap after C, transcribed as one word. 'Roma.riſpo' (line 10): point sits low, on/below the baseline. 'Ro.' (line 18) abbreviated as printed. 'Rep.nõ' (line 22). Unit ends line 25 'rouina.', followed by the Cap. XVIII heading (three lines) and its first body lines with a drop initial D.

# Uncertain loci

| n | folio | line | printed context | ⟨preferred\|alternative⟩ | why |
|---|---|---|---|---|---|
| 1 | 178v | heading l.2 | in amminiſtratione, / et gouerno | ⟨amminiſtratione,\|amminiſtratione.⟩ | mark after final e is a heavy blot with a short tail; reads as comma but the tail is weak; sense favours comma |
| 2 | 178v | 23 (unit 8) | con Annibale)s'e / ra trouato | ⟨s'e\|s'e-⟩ | faint vertical dot-pair after e at the line's end; same kind of mark follows non-divided words on lines 16-18, so taken as stray; the word is divided here, so a faint hyphen cannot be excluded |
| 3 | 178v | 24 (unit 9) | a fronte d'Aſdru / bale | ⟨d'Aſdru\|d'Aſdru-⟩ | as n.2: faint dot-pair after u, not the double-stroke hyphen used elsewhere |
| 4 | 178v | 30 (unit 15) | ſaputa a Roma li / dette | ⟨li\|lì⟩ | marks above the i look like a dot plus a second speck (possible accent); could be a damaged dot only |
| 5 | 178v | 31 (unit 16) | al Senato,et al popolo, | ⟨et\|e:⟩ | second letter is a stub with two dots, no clear crossbar of t; sense favours 'et' |
| 6 | 179r | 8 | haueſſe preſo ſi / pericoloſo | ⟨ſi\|ſi.⟩ | a small point stands at mid height right after the i; probably a stray/displaced mark (no stop is wanted mid-sentence), but it is printed ink |
