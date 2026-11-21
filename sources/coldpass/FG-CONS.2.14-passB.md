---
unit: FG-CONS.2.14
reader: cold reader fgB (Pass B, full)
source: "Francesco Guicciardini, Considerazioni intorno ai Discorsi del Machiavelli, in Opere inedite, vol. 1, ed. Giuseppe Canestrini, Firenze 1857, pp. 67-68"
witness_images:
  - file: img/p67-full.png
    size: 1367x2184 RGB (bitonal content)
    check: reference full page 67
  - file: img/p67-part1of2.png
    size: 1367x1179
    check: "identical to p67-full rows 0-1179 (mean abs pixel diff 0.0) - top half: OK"
  - file: img/p67-part2of2.png
    size: 1367x1179
    check: "identical to p67-full rows 1005-2184 (mean abs pixel diff 0.0) - bottom half: OK"
  - file: img/p68-full.png
    size: 1367x2184 RGB (bitonal content)
    check: reference full page 68
  - file: img/p68-part1of2.png
    size: 1367x1179
    check: "identical to p68-full rows 0-1179 (mean abs pixel diff 0.0) - top half: OK"
  - file: img/p68-part2of2.png
    size: 1367x1179
    check: "identical to p68-full rows 1005-2184 (mean abs pixel diff 0.0) - bottom half: OK"
  - note: "Pixel dimensions (1367x2184) are far below what 1200 ppi of a book page would give; reading was done from 2x-4x LANCZOS enlargements in work/."
boundaries:
  precedes: "End of the consideration on chapter XIII, p. 67 lines 1-14, last words '... toglie occasione di conseguire gli intenti suoi' (no final point visible after 'suoi')."
  begins: "p. 67, heading 'Considerazione sul Capitolo XIV.' about two-fifths down the page, after a blank space"
  first_words: "La conclusione del Discorso è in parte contraria"
  last_words: "ancora che per sè stesse le pares- / sino di poco momento."
  ends: "p. 68, line 6 of text"
  follows: "p. 68, after a blank space: heading 'Considerazione sul Capitolo XV.', rubric 'Gli Stati deboli sempre fieno ambigui nel risolversi / e sempre le deliberazioni lente sono nocive', body beginning 'Da due cagioni procedono le ambiguità delle delibera-'."
  not_transcribed: "Running heads: p. 67 'SUI DISCORSI DEL MACHIAVELLI.' (broken in scan, reads like 'SUI DISCOBSI OEL MACHIAVBLLI.') with page number '67' at right; p. 68 page number '68' at left with running head 'CONSIDERAZIONI'. No signatures or catchwords seen. Faint scanner watermark residue at bottom right of both pages; a vertical rule/shadow in the right margin of p. 68."
headings_printed:
  heading: "Considerazione sul Capitolo XIV. (initial C and C in capitals, rest in small capitals; numeral XIV in full capitals; final point present)"
  rubric: "two centred lines in smaller roman type: 'Ingannansi molte volte gli uomini, credendo con la umiltà / vincere la superbia' (no final point visible)"
paragraphing: "One paragraph. Only the first body line on p. 67 is indented (left ink edge at x=184 vs 125-129 for all following lines on p. 67); all six lines on p. 68 are flush left (x=309-311). No italic seen in heading, rubric, body or note (etiam is roman)."
body_word_count: 157
words_per_page:
  p67: 110
  p68: 47
word_count_method: "Body only (heading, rubric, footnote call and footnote excluded). Line-end hyphenated words rejoined and counted once, on the page where they begin (no word is divided across the page break). Tokens split on whitespace and apostrophes; standalone punctuation not counted. Thus ne'casi = 2 words, co' = 1 word. For uncertain loci the preferred reading was counted. Count done by Python script on the transcription."
uncertain_loci_per_page:
  p67: 15
  p68: 2
uncertain_loci_total: 17
conventions: "Diplomatic, line for line; [p. N] page markers; line-end hyphens kept; printed spacing before ',' and ';' kept; ⟨preferred|alternative⟩ for doubtful readings; footnote call shown as (1) where printed (superscript in the original); dotless/broken i, u/n and e/c breaks that leave an unambiguous word are written plainly."
---

# Heading

[p. 67]
Considerazione sul Capitolo XIV.

# Rubric

⟨Ingannansi|Ingannarsi⟩ molte volte ⟨gli|ali⟩ ⟨uomini|uomuu⟩, credendo con la ⟨umiltà|umilta⟩
⟨vincere|vineere⟩ ⟨superbia|superbia.⟩

# Body

[p. 67]
La conclusione del Discorso è in parte contraria a quello
che lui disse in altro luogo,(1) che è più prudenza tempo-
reggiarsi ⟨ne'casi|ne' casi⟩ ⟨pericolosi|pericnlosi⟩ che urtare , e però bisogna di-
⟨stinguere|stnguere⟩ che quando le forze tue non sono pari a ⟨quello|qnello⟩
dello inimico, meglio sia accordare, etiam lasciando qual-
che cosa, che tirarsi subito addosso la ruina ; perchè il
tempo può portare degli accidenti che bastino a provedere
al tuo futuro periculo. Ma quando tu ⟨hai|bai⟩ forze pari o quasi
pari allo inimico, ancora che lo entrare in guerra sia con
periculo e con difficultà, importa ⟨tanto|taato⟩ il cominciare a ⟨tôrti|tòrti⟩
la riputazione, a fare vile te, insolente lo inimico, che mal
[p. 68]
volentieri si debbe ⟨cedere.|cedere⟩ La quale ragione largamente
discorre Tucidide nella persona di Pericle, quando ⟨consigliò|consiglio⟩
agli Ateniesi più presto il pigliare la guerra co' Lacede-
monii, benchè difficile e periculosa, che accettare le condi-
zioni proposte da loro, ancora che per sè stesse le pares-
sino di poco momento.

# Notes on the page

p. 67, below a full-width rule at the foot of the page. Call "(1)" (superscript, in parentheses) keyed in body line 2 of p. 67, immediately after "luogo," (before "che è più prudenza").

(1) Nel capitolo ⟨xxxiii|xxxiu⟩ del libro ⟨i.|i⟩

(Roman numerals in small capitals. No note on p. 68 belongs to this unit; p. 68 has no footnote at all.)

# Uncertain loci

| # | page | line | locus | what you see | class |
|---|------|------|-------|--------------|-------|
| 1 | 67 | rubric 1 | Ingannansi | first word badly broken: reads like "lnganuansi"; the letter before "si" is a fractured n (r not excluded) | different word |
| 2 | 67 | rubric 1 | gli | g filled to a blob, partly greyed; "gli" by shape | non-word |
| 3 | 67 | rubric 1 | uomini | final letters broken into strokes ("uomuu"/"uomını") | non-word |
| 4 | 67 | rubric 1 | umiltà | last word heavily broken ("uuulıt\"); final mark looks like a grave on a; accent not certain | accent |
| 5 | 67 | rubric 2 | vincere | the c prints as e ("vineere") | non-word |
| 6 | 67 | rubric 2 | superbia | no point visible after the word; a faint grey smear follows | mark-pointing |
| 7 | 67 | body 3 | ne'casi | apostrophe sits tight against "casi" with no space | spacing |
| 8 | 67 | body 3 | pericolosi | prints "pericnlosi": the letter after c is an open n-shape, probably a broken o | non-word |
| 9 | 67 | body 4 | stinguere | "ti" fused/broken, reads "stnguere"/"sünguere" with a stray dot above | non-word |
| 10 | 67 | body 4 | quello (line end) | u prints as n ("qnello") | non-word |
| 11 | 67 | body 8 | hai | h shows a closed bowl, looks like "bai" | non-word |
| 12 | 67 | body 10 | tanto | first n filled/broken, reads "taato" | non-word |
| 13 | 67 | body 10 | tôrti | accent over o is a small peaked mark, read as circumflex; grave not excluded | accent |
| 14 | 67 | note | xxxiii | final small-cap numerals broken into "u"-like strokes | non-word |
| 15 | 67 | note | i. (last word) | small-cap i followed by a faint grey speck; the final point is not certain | mark-pointing |
| 16 | 68 | body 1 | cedere. | wide gap between "cedere" and "La" but no point visible (sentence break evident from capital) | mark-pointing |
| 17 | 68 | body 2 | consigliò | final accent present but faint; "quando" on same line prints "quandn" (o broken), read plainly as quando | accent |

Note on counts: loci 1-6 are in the rubric, loci 14-15 in the footnote; body-only uncertain loci = 9 (p. 67: 7, p. 68: 2). Not flagged because read with confidence: the space before the comma in "urtare ," (p. 67 l. 3) and before the semicolon in "ruina ;" (l. 6), both written as printed; "quandn" on p. 68 l. 2 is a broken o and is written plainly as "quando".
