---
unit: NM-DISC.2.13
reader: "pass B: sample page and line crops"
source: "Machiavelli, Discorsi sopra la prima deca di Tito Livio, Italia [Firenze], 1824, Libro secondo; page images at 350 ppi (native)"
witness_images:
  page: p262-page.png (2057 x 3228)
  crops:
    - "p262-top.png (2057 x 1205): identical to p262-page rows 0-1204 (pixel match, mean abs diff 0.0)"
    - "p262-middle.png (2057 x 1335): identical to p262-page rows 946-2280 (pixel match, mean abs diff 0.0)"
    - "p262-bottom.png (2057 x 1206): identical to p262-page rows 2022-3227 (pixel match, mean abs diff 0.0)"
  crop_check: "All three crops are what their names say: full-width top / middle / bottom regions of p262-page, overlapping, covering the whole page."
  line_crops: [p261-crop-a.png, p261-crop-b.png, p261-crop-c.png, p261-crop-d.png, p261-crop-e.png]
  running_head_p262: "262 [page number, left]   DISCORSI [running head, centred, small capitals]"
boundaries:
  first_words: "re, che non solo i Latini" (line 1 begins with \"re,\", the tail of a word hyphenated from p. 261)
  last_words: "come fu questa de'Romani."
  final_stop_visible: true
  followed_by: "blank space, then centred heading CAPITOLO XIV, then italic centred title in two lines (Ingannansi molte volte gli uomini, credendo / con la umiltà vincere la superbia.), then text of Cap. XIV opening with a two-line drop capital V (Vedesi molte volte come la umiltà non sola-)"
  capitolo_xiii_ends: "p. 262, line 19 of the text block (last line before the CAPITOLO XIV heading)"
paragraphing_p262: "No paragraph indent in the Capitolo XIII portion. Line 9 (E che sia vero ...) begins flush left after a full stop at the end of line 8; it is not indented (a small stray mark sits just left of the E, not part of the text). Cap. XIII runs as one continuous block on this page."
transcription_conventions: "Line for line. Thin typographic spaces before commas, colon and semicolon (e.g. 're ,', 'parole :') are not recorded; punctuation is written closed. Apostrophe spacing is recorded as printed. Letter-spacing gaps inside words (Camp ani, n ome, Ro mani) are typesetting irregularities and are written as single words; noted in the loci table."
sample_word_count: 159
sample_word_count_method: "Python over the draft of Cap. XIII on p. 262 (preferred readings): line-end hyphen + newline removed to join ro-/mano into one word; text split on whitespace and apostrophes; tokens containing a letter counted. So elided forms count as two words (a' quali = 2, de'Romani = 2). Line 1 fragment 're,' (tail of a word broken from p. 261) counts as 1. A plain whitespace split gives 158 (the difference is de'Romani, printed closed)."
uncertain_loci_total: 5
---

# Page 262

re, che non solo i Latini, ma le colonie che essi
avevano in Lazio, insieme con i Campani stati
innanzi difesi, congiurarono contro al nome ro-
mano. E mossero questa guerra i Latini nel modo
che si dice di sopra che si muovono la maggior
parte delle guerre, assaltando non i Romani, ma
difendendo i Sidicini contro ai Sanniti, a' quali i
Sanniti facevano guerra con licenza de' Romani.
E che sia vero che i Latini si movessero per avere
conosciuto questo inganno, lo dimostra Tito Livio
nella bocca di Annio Setino Pretore latino, il quale
nel Consiglio loro disse queste parole: *Nam si*
*etiam nunc sub umbra foederis aequi servitutem*
*pati possumus, etc.* Vedesi pertanto i Romani nei
primi augumenti loro non essere mancati etiam
della fraude; la quale fu sempre necessaria ad usare
a coloro che di piccoli principj vogliono a sublimi
gradi salire, la quale è meno vituperevole quanto
è più coperta, come fu questa ⟨de'Romani|de' Romani⟩.

[End of Capitolo XIII. Followed by: CAPITOLO XIV (centred heading); italic title "Ingannansi molte volte gli uomini, credendo / con la umiltà vincere la superbia."; text opening "Vedesi molte volte ..." with drop capital.]

# Line crops

p261-crop-a.png

constituito in bassa fortuna, pervenuto a grande

p261-crop-b.png

bardia a messer Bernabò suo zio. E quel che sono

p261-crop-c.png

tini, ed altri Popoli all' intorno. Perchè prima si

p261-crop-d.png

ai Romani con i Principi longinqui, che mediante

p261-crop-e.png

Latini. E tanto potè questa invidia ⟨è|e⟩ questo timo-

# Uncertain loci

| # | image | line | locus | what you see | class |
|---|-------|------|-------|--------------|-------|
| 1 | p261-crop-e.png | (single line) | invidia ⟨è\|e⟩ questo | The mark above this e is a small dot-like stroke, not a clear grave like the one on "potè" in the same line; could be a damaged grave accent or a speck over plain e | different word |
| 2 | p262-middle.png | 19 (last of Cap. XIII) | ⟨de'Romani\|de' Romani⟩ | Apostrophe set almost touching R, with no clear space; compare line 8 "de' Romani" with a visible space | mark-pointing |
| 3 | p262-top.png | 8 | de' Romani | Wide gap inside "Ro mani" (letter-spacing); read as one word | mark-pointing |
| 4 | p262-top.png | 2-3 | Campani; nome | Gaps inside "Camp ani" (line 2) and "n ome" (line 3), typesetting spacing; read as single words | mark-pointing |
| 5 | p262-middle.png | 12 | parole: | Clear space before the colon (typographic thin space, as before commas throughout); written closed by convention | mark-pointing |
