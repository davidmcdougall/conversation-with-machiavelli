---
unit: FG-CONS.2.12
reader: pass A (cold)
source: "Francesco Guicciardini, Considerazioni intorno ai Discorsi del Machiavelli, in Opere inedite, vol. 1, ed. Giuseppe Canestrini, Firenze 1857, pp. 62-65"
witness_images:
  - images/canestrini-page1-full.png (p. 62) + -1-top, -2-bottom
  - images/canestrini-page2-full.png (p. 63) + -1-top, -2-bottom
  - images/canestrini-page3-full.png (p. 64) + -1-top, -2-bottom
  - images/canestrini-page4-full.png (p. 65) + -1-top, -2-bottom
  - images/canestrini-page5-full.png (p. 66, next unit only; no text of this unit) + -1-top, -2-bottom
boundaries:
  precedes: "p. 62 l. 1-18: end of the preceding consideration, last words 'non se ne maraviglierà, nè la dannerà / in modo alcuno' (no final stop visible); its footnote (1) at foot of p. 62 belongs to it (cue after 'provede,')"
  heading: "p. 62: CONSIDERAZIONE SUL CAPITOLO XII⟨.|∅⟩ (small caps)"
  rubric: "S' egli è meglio, temendo di essere assaltato, inferire, / o aspettare la guerra⟨.|∅⟩"
  first_words: "Se nel presente Discorso si truovano (p. 62, last 4 text lines)"
  last_words: "rotti da lui in Spagna o in Africa (p. 65, last text line)"
  final_stop_visible: false
  follows: "p. 65 ends after the unit (signature 'I' and '9' at foot); p. 66 begins with heading CONSIDERAZIONE SUL CAPITOLO XIII⟨.|∅⟩, rubric 'Che si viene di bassa a gran fortuna più con la fraude, / che con la forza.' (printed with broken letters: 'viena', 'piu'), first words 'Se lo Scrittore chiama fraude'"
headings_printed: "Heading in small caps centred; rubric in smaller type, two centred lines"
paragraphing: "2 paragraphs, both indented: (1) p. 62 'Se nel presente Discorso' to p. 64 l. 4 'molto approvato.'; (2) p. 64 l. 5 'Resta la resoluzione' to end. No other indents."
body_word_count: 919
words_per_page: {p62: 41, p63: 291, p64: 276, p65: 311}
word_count_method: "Python regex [A-Za-zÀ-ÿ]+ over body only (heading and rubric excluded), preferred readings, footnote cues '(1)' removed; apostrophe separates tokens; a line-end-hyphenated word counted once, on the page/line where it begins (incl. 'considera-/zioni' across pp. 62-63)."
uncertain_loci_per_page: {p62: 4, p63: 22, p64: 14, p65: 15}  # p62 = 2 heading/rubric + 2 body
uncertain_loci_total: 55
---

Image note: all crops checked against the full pages by pixel comparison; each -1-top is the top of its page (offset 0) and each -2-bottom the lower part (offset ~1005-1012 px), as named. Page 5 (p. 66) contains no text of this unit.

# Heading

CONSIDERAZIONE SUL CAPITOLO XII⟨.|∅⟩

(p. 62; small caps: 'Considerazione sul Capitolo XII'; stop after XII faint)

# Rubric

S' egli è meglio, temendo di essere assaltato, inferire,
o aspettare la guerra⟨.|∅⟩

# Body

[p. 62]

 1  Se nel presente Discorso si truovano esempli ⟨assai|aasai⟩ nel-
 2  l' una e ⟨l'|l⟩ altra opinione, ci sono anche ragioni assai che
 3  fanno il caso sì dubio, che non è di facile resoluzione, e
 4  a volerlo bene deliberare ha bisogno di molte considera-

[p. 63]

 1  zioni che sono state pretermesse dallo Autore⟨.|∅⟩ Perchè non
 2  basta sola quella distinzione⟨:|∅⟩ o io ho e sudditi armati o
 3  e' sono disarmati, ma è necessario pensare più oltre ⟨:|.⟩ o
 4  e populi miei sono fedeli o e' sono inclinati alle ribellioni ,
 5  o le terre sono forti, o le sono deboli; o io posso, ancora
 6  che io abbia la guerra in casa che mi consumi le entrate,
 7  in quanto al danaio sostenerla lungamente, o io non po-
 8  trei reggerla. S' ha ancora a considerare le condizioni dello
 9  inimico, cioè che milizia ha, che paesi, che ⟨entrate|entrato⟩, ⟨che|cho⟩
10  modo a sostenere la ⟨guerra|guorra⟩ in casa, che modo a farla
11  fuora di casa⟨;|,⟩ perchè il governo e tutte le azioni della
12  guerra s' hanno sempre ⟨a|n⟩ regolare secondo le qualità e
13  i progressi dello inimico⟨.|∅⟩ È ancora differenza, quando io
14  aspetto guerra da altri, il dire⟨:|∅⟩ io la porto a casa sua ⟨;|.⟩ il
15  dire⟨:|;⟩ io esco del mio paese, e rincontro lo inimico fuori del
16  paese suo (e questo è lo esemplo del re Ferrando⟨)|∅⟩.(1) ⟨È|E⟩ dif-
17  ferenza il dire⟨:|∅⟩ io comincio la guerra in sul suo innanzi
18  che lui l'abbia cominciata a me⟨;|,⟩ a dire⟨:|∅⟩ io ho già la guerra
19  in casa⟨;|,⟩ ma per constrignere lo inimico a partirsene, io la
20  comincio anche in sul suo⟨,|∅⟩ come fe Scipione quando An-
21  nibale era in Italia, come fece Agatocle assediato da Car-
22  taginesi, come e ⟨Fiorentini|Fiorenlini⟩ tante volte nelle guerre ⟨fatte|falte⟩
23  loro da' Visconti⟨.|∅⟩ E quanto a questo ultimo caso io giu-
24  dicherò sempre che chi ha la guerra in casa, se ha op-
25  portunità nel tempo medesimo di cominciarla in quello
26  dello inimico, lo debba fare; perchè essendo cosa inaspet-
27  tata, disordina tutti e disegni dello inimico; e ogni piccolo
28  successo che vi abbia, lo constrigne a ritirarsi con tutto

[p. 64]

 1  ⟨a|n⟩ con parte delle forze ⟨sue|aue⟩ a difendere casa sua, e inter-
 2  viene come de' remedii che usano questi fisici a curare le
 3  infermità, tra' quali sempre ⟨la|lo⟩ diversione è giudicata re-
 4  medio potente e molto approvato.
 5      Resta la resoluzione degli altri casi, ne' quali proce-
 6  dendo per distinzione, dico che quando ⟨lo|la⟩ inimico da
 7  chi tu tenti la guerra ha più esercito e più potenza di
 8  te, che tu non puoi pensare di fargli la guerra in casa,
 9  perchè bisognano molte ⟨forze|forzo⟩ e molte opportunità a por-
10  tare la guerra a casa di altri, le quali non sono così
11  necessarie a chi fa guerra in casa sua, perchè si serve
12  del favore del paese, de' sudditi e delle difficultà degli
13  inimici, co' quali remedii può andarsi temporeggiando⟨.|∅⟩ E
14  in questo grado era il re Ferrando, il quale non poteva
15  mettere in campagna esercito pari a quello degli ⟨ini-|ioi-⟩
16  mici⟨.|∅⟩ Ma quando tu ti senti e di gente e di danari e
17  dell' altre opportunità della guerra pari allo inimico, e
18  ordinato di quelle forze che ⟨sono|sonn⟩ necessarie a fare guerra
19  in casa sua, io sarei inclinato a consigliare di non aspet-
20  tare la guerra a casa propria, perchè vincendo, il premio
21  è maggiore, potendoti portare quella vittoria facilmente lo
22  acquisto del regno di altri⟨;|,⟩ dove la vittoria in casa tua
23  non ti porta altro che la liberazione del tuo Stato⟨,|;⟩ per-
24  dendo, il danno è minore, perchè non perdi altro che quello
25  esercito, e hai più tempo a rifarti⟨;|,⟩ dove perdendo in casa,
26  se lo inimico accelera la vittoria, come potette fare Anni-
27  bale a ⟨Canne|Canno⟩⟨,|∅⟩ come a' tempi moderni Paolo Orsino (1) a La-
28  dislao, il duca Giovanni al re Ferrando, una giornata è

[p. 65]

 1  bastante a farti perdere lo Stato⟨.|∅⟩ Portando la guerra a casa
 2  lo inimico, hai già disturbato il disegno suo di fare la
 3  guerra in casa tua, hai impedito le preparazioni necessarie
 4  a questo effetto, in modo che etiam vincendoti ha bisogno
 5  di tempo ⟨e|a⟩ di nuovi ordini a venire a guerreggiarti in
 6  casa⟨;|,⟩ il che ti dà spazio a riordinarti e rifarti⟨.|∅⟩ E tanto più
 7  facilmente aderirei a questa conclusione, quanto io ve-
 8  dessi lo inimico non avere paese forte, o non avere sud-
 9  diti fedeli, o condizionato lo ⟨Stato|Stoto⟩ in modo che facilmente
10  si potessi disordinargli le entrate, o essergli difficile, se
11  avessi una rotta, a rifarsi in breve spazio di tempo⟨.|∅⟩ Veggo
12  che ⟨sempre|sempra⟩ e Romani, quando potettono, prevennono le
13  guerre a casa altri, contro a Filippo re di Macedonia, con-
14  tro a Antioco, contro a' Cartaginesi⟨,|;⟩ e quando non lo fe-
15  ciono, furono malcontenti di non l' avere fatto⟨.|∅⟩ Nè mi
16  muove quello che dice lo Scrittore, che se e Romani aves-
17  sino avuto in tanto spazio di tempo quelle tre rotte in
18  Francia, che gli ebbono in Italia da Annibale, sarebbono
19  sanza dubio stati spacciati⟨;|,⟩ perchè si pone uno caso im-
20  possibile, che chi ha una rotta in casa di altri, massime
21  in luogo ⟨lontono|lontano⟩, possi così subitamente dopo la prima rotta
22  avervi rimandato l' uno dopo l' altro dua nuovi eserciti. E
23  chi risolve bene il partito di fuggire la guerra in casa col
24  portarla a casa di altri, vi va con tale fondamento che può
25  così ⟨sperare|sporaro⟩ di rompere lo inimico, come temere di essere
26  rotto⟨;|,⟩ altrimenti la aspetta in casa, come feciono e Romani
27  da Annibale⟨;|,⟩ e quali essendo già molti anni, come dice Li-
28  vio, inesperti alla guerra, e avendo la guerra con capitano
29  e con soldati espertissimi, se furono rotti in casa, sareb-
30  bono forse più facilmente stati nel principio della guerra
31  rotti da lui in Spagna o in Africa⟨.|∅⟩

# Footnote cues

- p. 63 l. 16: cue (1), superscript, after 'Ferrando).' (i.e. after the closing parenthesis and stop) and before 'È dif-'. Footnote at foot of p. 63, 5 lines: first words 'Ferdinando di Napoli', last words 'e perdette quello e lo Stato' (no final stop visible).
- p. 64 l. 27: cue (1), superscript, after 'Orsino' (space before cue), before 'a La-'. Footnote at foot of p. 64, 4 lines: first words 'Paolo Orsino fu condottiere', last words 'detta la Città Leonina' (no final stop visible).
- Not in this unit: the footnote at the foot of p. 62 ('La guerra si fa col ferro' ... 'jusqu'au bout du monde') is cued in the preceding consideration after 'provede,'. The footnote on p. 66 belongs to the next consideration.

# Uncertain loci

Heading/rubric (p. 62):
- H1 p. 62 heading: stop after 'XII' faint/partial. Mark only.
- H2 p. 62 rubric l. 2: stop after 'guerra' faint. Mark only.

- 1. p. 62 l. 1 ⟨assai|aasai⟩: type broken; first letters read 'aa'; spacing fits 'assai'. Alternative: non-word.
- 2. p. 62 l. 2 ⟨l'|l⟩: apostrophe after second 'l' not inked (cf. 'l' una' earlier in line). Alternative: mark only.
- 3. p. 63 l. 1 ⟨.|∅⟩: no stop visible after 'Autore' before capital 'Perchè'; gap present. Alternative: mark only.
- 4. p. 63 l. 2 ⟨:|∅⟩: faint mark after 'distinzione', likely colon. Alternative: mark only.
- 5. p. 63 l. 3 ⟨:|.⟩: 'oltre' followed by space and a mark read as colon; lower dot clearer than upper. Alternative: mark only.
- 6. p. 63 l. 9 ⟨entrate|entrato⟩: final letter reads 'o' but e/o damage frequent on this page. Alternative: different word (entrato).
- 7. p. 63 l. 9 ⟨che|cho⟩: line-end 'che' reads 'cho'; broken e. Alternative: non-word.
- 8. p. 63 l. 10 ⟨guerra|guorra⟩: reads 'guorra'; broken e. Alternative: non-word.
- 9. p. 63 l. 11 ⟨;|,⟩: after 'casa' a mark read as semicolon, upper dot faint. Alternative: mark only.
- 10. p. 63 l. 12 ⟨a|n⟩: letter before 'regolare' reads 'n'; broken a. Alternative: non-word.
- 11. p. 63 l. 13 ⟨.|∅⟩: no stop visible after 'inimico'; gap before 'È'. Alternative: mark only.
- 12. p. 63 l. 14 ⟨:|∅⟩: after 'dire' faint mark, colon probable. Alternative: mark only.
- 13. p. 63 l. 14 ⟨;|.⟩: after 'sua' space then a damaged mark (semicolon or stop). Alternative: mark only.
- 14. p. 63 l. 15 ⟨:|;⟩: after 'dire' mark, colon or semicolon. Alternative: mark only.
- 15. p. 63 l. 16 ⟨)|∅⟩: closing parenthesis faint/broken before stop. Alternative: mark only.
- 16. p. 63 l. 16 ⟨È|E⟩: accent on capital after cue faint. Alternative: mark only (accent).
- 17. p. 63 l. 17 ⟨:|∅⟩: after 'dire' faint colon. Alternative: mark only.
- 18. p. 63 l. 18 ⟨;|,⟩: after 'me' mark, semicolon or comma. Alternative: mark only.
- 19. p. 63 l. 18 ⟨:|∅⟩: after second 'dire' colon (broken). Alternative: mark only.
- 20. p. 63 l. 19 ⟨;|,⟩: after 'casa' mark, semicolon or comma. Alternative: mark only.
- 21. p. 63 l. 20 ⟨,|∅⟩: gap after 'suo' with no visible mark. Alternative: mark only.
- 22. p. 63 l. 22 ⟨Fiorentini|Fiorenlini⟩: 'Fiorentini' with t/l damaged. Alternative: non-word.
- 23. p. 63 l. 22 ⟨fatte|falte⟩: 'fatte' with first t damaged (reads 'falte'). Alternative: non-word.
- 24. p. 63 l. 23 ⟨.|∅⟩: no stop visible after 'Visconti'. Alternative: mark only.
- 25. p. 64 l. 1 ⟨a|n⟩: first word of page reads 'n'; broken a. Alternative: non-word.
- 26. p. 64 l. 1 ⟨sue|aue⟩: 'sue' with s damaged (reads 'aue'). Alternative: non-word.
- 27. p. 64 l. 3 ⟨la|lo⟩: article before 'diversione' damaged, 'la' or 'lo'. Alternative: different word.
- 28. p. 64 l. 6 ⟨lo|la⟩: article before 'inimico' damaged, 'lo' or 'la'. Alternative: different word.
- 29. p. 64 l. 9 ⟨forze|forzo⟩: 'forze' reads 'forzo'; broken e. Alternative: non-word.
- 30. p. 64 l. 13 ⟨.|∅⟩: no stop visible after 'temporeggiando'. Alternative: mark only.
- 31. p. 64 l. 15 ⟨ini-|ioi-⟩: line-end 'ini-' reads 'ioi-'; broken n. Alternative: non-word.
- 32. p. 64 l. 16 ⟨.|∅⟩: no stop visible after 'mici'. Alternative: mark only.
- 33. p. 64 l. 18 ⟨sono|sonn⟩: 'sono' reads 'sonn'; broken o. Alternative: non-word.
- 34. p. 64 l. 22 ⟨;|,⟩: after 'altri' mark, semicolon or comma. Alternative: mark only.
- 35. p. 64 l. 23 ⟨,|;⟩: after 'Stato' mark, comma or semicolon. Alternative: mark only.
- 36. p. 64 l. 25 ⟨;|,⟩: after 'rifarti' space then mark, semicolon or comma. Alternative: mark only.
- 37. p. 64 l. 27 ⟨Canne|Canno⟩: 'Canne' reads 'Canno'; broken e. Alternative: different word / non-word.
- 38. p. 64 l. 27 ⟨,|∅⟩: gap after 'Canne' with no visible mark. Alternative: mark only.
- 39. p. 65 l. 1 ⟨.|∅⟩: no stop visible after 'Stato'; gap before 'Portando'. Alternative: mark only.
- 40. p. 65 l. 5 ⟨e|a⟩: letter between 'tempo' and 'di' damaged, 'e' or 'a'. Alternative: different word.
- 41. p. 65 l. 6 ⟨;|,⟩: after 'casa' mark, semicolon or comma. Alternative: mark only.
- 42. p. 65 l. 6 ⟨.|∅⟩: no clear stop after 'rifarti'. Alternative: mark only.
- 43. p. 65 l. 9 ⟨Stato|Stoto⟩: 'Stato' reads 'Stoto'; broken a. Alternative: non-word.
- 44. p. 65 l. 11 ⟨.|∅⟩: no stop visible after 'tempo'. Alternative: mark only.
- 45. p. 65 l. 12 ⟨sempre|sempra⟩: 'sempre' reads 'sempra'; broken e. Alternative: non-word.
- 46. p. 65 l. 14 ⟨,|;⟩: after 'Cartaginesi' comma or semicolon. Alternative: mark only.
- 47. p. 65 l. 15 ⟨.|∅⟩: no stop visible after 'fatto'. Alternative: mark only.
- 48. p. 65 l. 19 ⟨;|,⟩: after 'spacciati' mark, semicolon or comma. Alternative: mark only.
- 49. p. 65 l. 21 ⟨lontono|lontano⟩: printed as 'lontono' as far as visible; could be damaged 'lontano'. Alternative: different spelling (lontano).
- 50. p. 65 l. 25 ⟨sperare|sporaro⟩: 'sperare' reads 'sporaro'; broken e's. Alternative: non-word.
- 51. p. 65 l. 26 ⟨;|,⟩: after 'rotto' mark, semicolon or comma. Alternative: mark only.
- 52. p. 65 l. 27 ⟨;|,⟩: after 'Annibale' mark, semicolon or comma. Alternative: mark only.
- 53. p. 65 l. 31 ⟨.|∅⟩: no final stop visible after 'Africa'; ink fades at line end. Alternative: mark only.
