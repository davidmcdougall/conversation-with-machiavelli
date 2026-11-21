---
unit: FG-CONS.2.14
reader: cold reader fgA (Pass A, full)
source: "Francesco Guicciardini, Considerazioni intorno ai Discorsi del Machiavelli, in Opere inedite, vol. 1, ed. Giuseppe Canestrini, Firenze 1857, pp. 67-68"
witness_images:
  - file: img/p67-full.png
    size: 1367x2184 RGB (bitonal content)
    check: reference full page 67
  - file: img/p67-part1of2.png
    size: 1367x1179
    check: identical (mean abs pixel diff 0.0) to rows 0-1178 of p67-full; top half confirmed
  - file: img/p67-part2of2.png
    size: 1367x1179
    check: identical (mean abs pixel diff 0.0) to rows 1005-2183 of p67-full; bottom half confirmed (overlap 174 rows)
  - file: img/p68-full.png
    size: 1367x2184 RGB (bitonal content)
    check: reference full page 68
  - file: img/p68-part1of2.png
    size: 1367x1179
    check: identical (mean abs pixel diff 0.0) to rows 0-1178 of p68-full; top half confirmed
  - file: img/p68-part2of2.png
    size: 1367x1179
    check: identical (mean abs pixel diff 0.0) to rows 1005-2183 of p68-full; bottom half confirmed (overlap 174 rows)
boundaries:
  precedes: "End of the consideration on chapter XIII, p. 67 lines 1-14 (top of page), last line: 'fraudolenta toglie occasione di conseguire gli intenti suoi' (no final stop visible after 'suoi'), then white space."
  heading_location: "p. 67, centred, below a blank space after line 14 of the page"
  rubric_location: "p. 67, two centred lines in smaller type under the heading"
  first_words: "La conclusione del Discorso è in parte contraria"
  last_words: "ancora che per sè stesse le paressino di poco momento." (p. 68, line 6 of the page)
  follows: "p. 68: heading 'CONSIDERAZIONE SUL CAPITOLO XV.' (C and C full capitals, rest small capitals), rubric 'Gli Stati deboli sempre fieno ambigui nel risolversi / e sempre le deliberazioni lente sono nocive', body beginning 'Da due cagioni procedono le ambiguità delle delibera-'."
  running_heads_not_transcribed: "p. 67: 'SUI DISCORSI DEL MACHIAVELLI.' with page number '67' at right; p. 68: page number '68' at left with 'CONSIDERAZIONI'. No signatures or catchwords seen. p. 68 bottom-right carries a faint scanner/library watermark (not transcribed)."
headings_printed:
  heading: "CONSIDERAZIONE SUL CAPITOLO XIV. — set as large-and-small capitals: full-size C of 'Considerazione' and C of 'Capitolo', remaining letters small capitals; 'XIV.' full capitals with full stop"
  rubric: "Ingannansi molte volte gli uomini, credendo con la umiltà / vincere la superbia — two centred lines, smaller roman type; final stop not visible"
paragraphing: "One paragraph. Pixel measurement of left ink edge (p-full coordinates): p. 67 body line 1 begins at x=183, lines 2-11 at x=126-129; p. 68 lines 1-6 at x=309-311 (all flush). Only the opening line is indented; no later line is indented. No italic seen in heading, rubric, body or footnote (the 'etiam' on p. 67 l. 5 is roman)."
body_word_count: 157
words_per_page: {p67: 110, p68: 47}
word_count_method: "Body only (heading, rubric, footnote and footnote call excluded). Whitespace-delimited tokens containing letters, from the preferred reading; punctuation standing alone (e.g. ' ,' ' ;') not counted; a word divided by a line-end hyphen counted once, on the page where it starts (all divisions fall within a page); elided forms counted as separate words (ne' casi = 2, co' Lacedemonii = 2). 'mal' (p. 67 last line) and 'volentieri' (p. 68 first line) are printed as two words with no hyphen and counted as 2. If 'ne'casi' is taken as printed without space and counted as one token, total = 156 (p67 = 109)."
uncertain_loci_per_page: {p67: 10, p68: 2}  # p67 = 3 rubric + 6 body + 1 footnote
uncertain_loci_total: 12  # body only: 8
conventions: "Diplomatic, line for line; [p. N] marks page starts. Doubtful readings ⟨preferred|alternative⟩. Spaces printed before ';' and ',' (e.g. 'ruina ;', 'urtare ,') are kept as seen. Footnote call printed as superscript '(1)' is shown as ⁽¹⁾. Heading given in capitals to represent large-and-small capitals. Running heads and page numbers not transcribed. Broken sorts read by context only where the letter shape is still compatible; otherwise flagged."
---

# Heading

[p. 67]
CONSIDERAZIONE SUL CAPITOLO XIV.

# Rubric

Ingannansi molte volte gli uomini, credendo con la ⟨umiltà|umilità⟩
⟨vincere|vineere⟩ la superbia⟨|.⟩

# Body

[p. 67]
La conclusione del Discorso è in parte contraria a quello
che lui disse in altro luogo,⁽¹⁾ che è più prudenza tempo-
⟨reggiarsi|roggiarsi⟩ ⟨ne' casi|ne'casi⟩ ⟨periculosi|pericolosi|pericnlosi⟩ che urtare , e però bisogna di-
⟨stinguere|sünguere⟩ che quando le forze tue non sono pari a quello
dello inimico, meglio sia accordare, etiam lasciando qual-
che cosa, che tirarsi subito addosso la ruina ; perchè il
tempo può portare degli accidenti che bastino a provedere
al tuo futuro periculo. Ma quando tu ⟨hai|bai⟩ forze pari o quasi
pari allo inimico, ancora che lo entrare in guerra sia con
periculo e con difficultà, importa tanto il cominciare a ⟨tôrti|tòrti⟩
la riputazione, a fare vile te, insolente lo inimico, che mal
[p. 68]
volentieri si debbe ⟨cedere.|cedere⟩ La quale ragione largamente
discorre Tucidide nella persona di Pericle, ⟨quando|quandn⟩ consigliò
agli Ateniesi più presto il pigliare la guerra co' Lacede-
monii, benchè difficile e periculosa, che accettare le condi-
zioni proposte da loro, ancora che per sè stesse le pares-
sino di poco momento.

# Notes on the page

[p. 67, foot, below a short rule; call ⁽¹⁾ keyed in body p. 67 line 2, after "luogo,"]
⁽¹⁾ Nel capitolo xxxiii del libro ⟨i.|i⟩

(Roman numerals in small capitals. No footnote on p. 68 for this unit.)

# Uncertain loci

| # | page | line | locus | what you see | class |
|---|------|------|-------|--------------|-------|
| 1 | 67 | rubric 1 | ⟨umiltà\|umilità⟩ | word badly broken: reads as "unulti" followed by a slanted stroke (accented à?); letter count unclear, m split into "nu" | different word |
| 2 | 67 | rubric 2 | ⟨vincere\|vineere⟩ | second c printed with closed bowl, indistinguishable from e (c/e) | non-word |
| 3 | 67 | rubric 2 | superbia⟨\|.⟩ | faint grey smear after "superbia", no clear stop | mark-pointing |
| 4 | 67 | body 3 | ⟨reggiarsi\|roggiarsi⟩ | first vowel looks like o (closed e/o) | non-word |
| 5 | 67 | body 3 | ⟨ne' casi\|ne'casi⟩ | apostrophe present but word space after it very narrow or absent | spacing |
| 6 | 67 | body 3 | ⟨periculosi\|pericolosi\|pericnlosi⟩ | letter after c is an n-shape (inverted u or broken o); "periculo" used elsewhere in this unit | different word |
| 7 | 67 | body 4 | ⟨stinguere\|sünguere⟩ | "ti" broken: t lacks crossbar, i reads as part of a u with dots | non-word |
| 8 | 67 | body 8 | ⟨hai\|bai⟩ | ascender letter has closed bowl like b (h/b ambiguity) | non-word |
| 9 | 67 | body 10 | ⟨tôrti\|tòrti⟩ | accent over o is a peaked mark, more circumflex than grave, but filled | accent |
| 10 | 68 | body 1 | ⟨cedere.\|cedere⟩ | no stop visible between "cedere" and capital "La"; wide space only | mark-pointing |
| 11 | 68 | body 2 | ⟨quando\|quandn⟩ | final letter printed as n (o/n broken) | non-word |
| 12 | 67 | footnote | libro ⟨i.\|i⟩ | final numeral i followed by grey speck, stop not certain | mark-pointing |

Totals: p. 67 rubric 3, p. 67 body 6, p. 68 body 2, p. 67 footnote 1 = 12 loci.
