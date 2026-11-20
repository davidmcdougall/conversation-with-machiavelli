---
unit: FG-CONS.2.10
reader: "pass A"
source: "Francesco Guicciardini, Considerazioni intorno ai Discorsi del Machiavelli, in Opere inedite, vol. 1, ed. Giuseppe Canestrini, Florence 1857"
witness_images: [canestrini-page1-full.png, canestrini-page1-1-top.png, canestrini-page1-2-bottom.png, canestrini-page2-full.png, canestrini-page2-1-top.png, canestrini-page2-2-bottom.png]
boundaries:
  start: "p. 61, line 1 after rubric: 'Chi fu autore di quella sentenza, che e danari furno' (heading at mid-page, after the close of the preceding consideration: '... più vir- / tuosa che l'altre')"
  end: "p. 62, body line 18: 'in modo alcuno' (final period not visible); followed by the heading 'Considerazione sul Capitolo XII.' and rubric 'S'egli è meglio, temendo di essere assaltato, inferire, / o aspettare la guerra'"
headings_printed: "CONSIDERAZIONE SUL CAPITOLO X DEL LIBRO II. (initial capitals with small caps: Considerazione sul Capitolo X del Libro II.), centred; rubric printed below it, centred, in smaller type, two lines"
paragraphing: "Single paragraph. First body line on p. 61 is indented; p. 62 line 1 continues the paragraph unindented; no further indents."
body_word_count: 245
words_per_page: {61: 70, 62: 175}
word_count_method: "python regex [A-Za-zÀ-ÿ]+ over the draft with preferred readings substituted (∅ = nothing); apostrophe treated as separator (l'ha = 2, co' soldati = 2, a' tempi = 2); footnote cue (1) removed; a word hyphenated at a line end counted once on the page where it begins (no word crosses the page break); heading, rubric and footnote excluded"
uncertain_loci_per_page: {61: 2, 62: 5}  # body only; rubric adds 2 on p. 61, footnote 7 on p. 62
uncertain_loci_total: 7
---

Image note: the files named "-1-top" and "-2-bottom" are not halves. For each page they are byte-identical to each other and show the whole page (1367 px wide, grayscale), so each page is effectively available at one resolution only (~150-200 px per printed inch despite the 1200 dpi tag). Enlargements made in work/ by resampling only.

# Heading

p. 61, centred, small capitals:

CONSIDERAZIONE SUL CAPITOLO X DEL LIBRO II.

# Rubric

p. 61, centred, smaller type, two lines:

I danari non sono il nervo della guerra, secondo che ⟨è|e⟩ la comune
oppinione⟨.|∅⟩

# Body

[p. 61]
    Chi fu autore di quella sentenza, che e danari furno
il nervo della guerra, e chi l'ha poi seguitata, non intese
che e danari soli bastassino a fare la guerra, nè che e fus-
sino più ⟨necessarii|necessarij⟩ che e soldati, perchè sarebbe stata opi-
nione non solo falsa, ma ancora molto ridicula, ma intese
che chi faceva guerra aveva bisogno grandissimo di
danari, e che sanza quelli era ⟨impossibile|impossibila⟩ a sostenerla,

[p. 62]
perchè non solo sono necessarii per pagare e soldati, ma per
provedere le armi, le vettovaglie, le spie, le munizioni e
tanti instrumenti che si adoperano nella guerra, e quali
ne ricercano tanto profluvio, che a chi non l'ha provato
è impossibile a immaginarlo. E se bene qualche volta uno
esercito carestioso di danari con la virtù sua e col favore
delle vittorie gli provede,(1) nondimeno a' tempi nostri mas-
sime sono esempli rarissimi; e in ogni caso e in ogni
tempo non corrono e danari dietro agli eserciti, se non da
poi che hanno vinto. Confesso che chi ha soldati proprii
fa la guerra con manco danari che non fa chi ha soldati
mercenarii⟨,|;⟩ nondimeno e anche danari bisognano a chi fa
guerra co' soldati proprii, e ognuno non ha soldati proprii,
ed è molto ⟨più|piu⟩ facile ⟨co'|co⟩ danari trovare soldati, che co' sol-
dati trovare danari⟨.|∅⟩ Chi adunque interpreterà quella sen-
tenza secondo il senso di chi la disse, e secondo che co-
munemente è intesa, non se ne maraviglierà, nè la dannerà
in modo alcuno⟨.|∅⟩

Note: the editor's apostrophe is printed with a thin space after it (l' ha, a' tempi, co' soldati); normalised here to no space.

# Footnotes

p. 62, below a rule; editor's note (1), keyed to the cue after "provede," (p. 62, body line 7):

(1) La guerra si fa col ferro e non con l'oro⟨;|,⟩ non l'oro è il nervo
della guerra, ma i buoni soldati⟨;|∅⟩ i danari sono necessarii, ma in secondo
luogo, ed ⟨è|e⟩ impossibile che ai buoni soldati manchino⟨.|∅⟩ Tali sono le sen-
tenze del Machiavelli⟨.|∅⟩ È noto quel detto francese⟨:|∅⟩ *avec du fer et du pain
on va jusqu'au bout du monde*⟨.|∅⟩

(French saying in italics. Footnote loci are not counted in the body totals.)

# Uncertain loci

Rubric (not counted in body totals):
R1. "che ⟨è|e⟩ la comune": accent not clearly visible: form of same word
R2. "oppinione⟨.|∅⟩": final period faint: only a mark

Body:
1. p. 61 l. 4 ⟨necessarii|necessarij⟩: final letters broken: form of same word
2. p. 61 l. 7 ⟨impossibile|impossibila⟩: final vowel looks like a: non-word
3. p. 62 l. 12 "mercenarii⟨,|;⟩": comma or semicolon: only a mark
4. p. 62 l. 14 ⟨più|piu⟩: accent not visible: form of same word
5. p. 62 l. 14 ⟨co'|co⟩ danari: apostrophe not visible: only a mark
6. p. 62 l. 15 "danari⟨.|∅⟩": period not visible: only a mark
7. p. 62 l. 18 "alcuno⟨.|∅⟩": final period not visible: only a mark

Footnote (not counted in totals): "oro⟨;|,⟩", "soldati⟨;|∅⟩", "ed ⟨è|e⟩", "manchino⟨.|∅⟩", "Machiavelli⟨.|∅⟩" (also M of Machiavelli broken), "francese⟨:|∅⟩", "monde⟨.|∅⟩": all only a mark except ed ⟨è|e⟩ (form of same word).
