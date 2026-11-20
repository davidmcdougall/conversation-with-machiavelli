---
unit: FG-CONS.2.12
reader: pass B (cold)
source: "Francesco Guicciardini, Considerazioni intorno ai Discorsi del Machiavelli, in Opere inedite, vol. 1, ed. Giuseppe Canestrini, Firenze 1857, pp. 62-65"
witness_images:
  - canestrini-page1-full.png (+ -1-top, -2-bottom)  # printed p. 62
  - canestrini-page2-full.png (+ crops)              # p. 63
  - canestrini-page3-full.png (+ crops)              # p. 64
  - canestrini-page4-full.png (+ crops)              # p. 65
  - canestrini-page5-full.png (+ crops)              # p. 66 (boundary only)
boundaries:
  preceded_by: "end of the consideration on cap. XI, p. 62 line 18: '... nè la dannerà / in modo alcuno' (final stop not visible); blank space follows"
  heading: "CONSIDERAZIONE SUL CAPITOLO XII⟨.|∅⟩ (p. 62, small caps)"
  rubric: "S' egli è meglio, temendo di essere assaltato, inferire, / o aspettare la guerra⟨.|,⟩"
  first_words: "Se nel presente Discorso si truovano esempli"
  last_words: "rotti da lui in Spagna o in Africa"
  final_stop_visible: "no - only a faint grey smudge after 'Africa'; recorded as ⟨.|∅⟩"
  ends: "p. 65 line 31; rest of p. 65 blank except sheet signature 'I' (left) and '9' (right) at foot"
  followed_by: "p. 66: heading 'CONSIDERAZIONE SUL CAPITOLO XIII⟨.|∅⟩'; rubric 'Che si ⟨viene|viena⟩ di bassa a gran fortuna più (printed 'piu', accent not visible) con la fraude, / che con la forza⟨.|∅⟩'; body begins 'Se lo Scrittore chiama fraude ogni astuzia o dissimu-'"
headings_printed: "Running heads CONSIDERAZIONI (pp. 62, 64, 66) and SUI DISCORSI DEL MACHIAVELLI (pp. 63, 65) not transcribed in body"
paragraphing: "Two paragraphs, both indented: p. 62 l.1 'Se nel presente' and p. 64 l.5 'Resta la resoluzione'. P. 64 l.4 ends short ('approvato.'). No other indents on pp. 63-65."
body_word_count: 919
words_per_page: {62: 41, 63: 291, 64: 276, 65: 311}
word_count_method: "Python over the body draft below with preferred readings substituted (⟨∅|..⟩ removed), footnote cues '(1)' stripped; regex [A-Za-zÀ-ÿ]+ (apostrophe separates, so l'abbia = 2); a line-end-hyphenated word (incl. 're -') counted once, on the page where it begins (first token of the continuation line skipped, also across pages: considera-/zioni counted on p. 62). Heading and rubric excluded."
uncertain_loci_per_page: {62: 4, 63: 19, 64: 15, 65: 15}
uncertain_loci_total: 53
uncertain_loci_note: "53 = 51 in body + 1 heading + 1 rubric (both p. 62). The p. 66 boundary readings (XIII stop, viene/viena, forza stop) are reported in boundaries only and not counted."
---

Image note: all ten crops checked numerically against their -full pages: each "-1-top" is rows 0-1187 (p1) / 0-1178 (pp2-5) of the full image, each "-2-bottom" rows 1012-2199 (p1) / 1005-2183, i.e. true top and bottom halves with overlap. No mismatch. Pages 1-5 = printed pp. 62-66.

# Heading

CONSIDERAZIONE SUL CAPITOLO XII⟨.|∅⟩

(printed in small caps: "Considerazione sul Capitolo XII")

# Rubric

S' egli è meglio, temendo di essere assaltato, inferire,
o aspettare la guerra⟨.|,⟩

(centred, two lines, smaller type; "S'" followed by a space)

# Body

[p. 62]

 1      Se nel presente Discorso si truovano esempli ⟨assai|aasai⟩ nel-
 2  l' una e l⟨'|∅⟩ altra opinione, ci sono anche ragioni assai che
 3  fanno il caso sì dubio, che non è di facile resoluzione, e
 4  a volerlo bene deliberare ha bisogno di molte considera-

[p. 63]

 1  zioni che sono state pretermesse dallo Autore⟨.|∅⟩ Perchè non
 2  basta sola quella distinzione⟨:|∅⟩ o io ho e sudditi armati o
 3  ⟨e'|c'⟩ sono disarmati, ma è necessario pensare più oltre⟨.|:⟩ o
 4  e populi miei sono fedeli o e' sono inclinati alle ribellioni ,
 5  o le terre sono forti, o le sono deboli; o io posso, ancora
 6  che io abbia la guerra in casa che mi consumi le entrate,
 7  in quanto al danaio sostenerla lungamente, o io non po-
 8  trei reggerla. S' ha ancora a considerare le condizioni dello
 9  inimico, cioè che milizia ha, che paesi, che ⟨entrate|entrato⟩, ⟨che|cho⟩
10  modo a sostenere la ⟨guerra|guorra⟩ in casa, che modo a farla
11  fuora di casa; perchè il governo e tutte le azioni della
12  guerra s' hanno sempre ⟨a|n⟩ regolare secondo le qualità e
13  i progressi dello inimico⟨.|∅⟩ È ancora differenza, quando io
14  aspetto guerra da altri, il dire⟨:|∅⟩ io la porto a casa sua⟨;|.⟩ il
15  dire⟨:|;⟩ io esco del mio paese, e rincontro lo inimico fuori del
16  paese suo (e questo è lo esemplo del re Ferrando⟨)|'⟩.(1) ⟨È|E⟩ dif-
17  ferenza il dire⟨:|∅⟩ io comincio la guerra in sul suo innanzi
18  che lui l'abbia cominciata a me⟨;|,⟩ a dire⟨:|∅⟩ io ho già la guerra
19  in casa; ma per constrignere lo inimico a partirsene, io la
20  comincio anche in sul suo⟨∅|,⟩ come fe Scipione quando An-
21  nibale era in Italia, come fece Agatocle assediato da Car-
22  taginesi, come e Fiorentini tante volte nelle guerre fatte
23  loro da' Visconti⟨.|∅⟩ E quanto a questo ultimo caso io giu-
24  dicherò sempre che chi ha la guerra in casa, se ha op-
25  portunità nel tempo medesimo di cominciarla in quello
26  dello inimico, lo debba fare; perchè essendo cosa inaspet-
27  tata, disordina tutti e disegni dello inimico; e ogni piccolo
28  successo che vi abbia, lo constrigne a ritirarsi con tutto

[p. 64]

 1  ⟨a|o⟩ con parte delle forze ⟨sue|aue⟩ a difendere casa sua, ⟨e|c⟩ inter-
 2  viene come de' remedii che usano questi fisici a curare le
 3  infermità, tra' quali sempre ⟨la|lo⟩ diversione è giudicata re -
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
15  mettere in campagna esercito pari a quello degli ini-
16  mici⟨.|∅⟩ Ma quando tu ti senti e di gente e di danari e
17  dell' altre ⟨opportunità|opportonità⟩ della guerra pari allo inimico, e
18  ordinato di quelle forze che ⟨sono|sonn⟩ necessarie a fare guerra
19  in casa sua, io sarei inclinato a consigliare di non aspet-
20  tare la ⟨guerra|gueı ra⟩ a casa propria, perchè vincendo, il premio
21  è maggiore, potendoti portare quella vittoria facilmente lo
22  acquisto del regno di altri⟨;|,⟩ dove la vittoria in casa tua
23  non ti porta altro che la liberazione del tuo Stato, per-
24  dendo, il danno è minore, perchè non perdi altro che quello
25  esercito, e hai più tempo a rifarti ⟨,|;⟩ dove perdendo in casa,
26  se lo inimico accelera la vittoria, come potette fare Anni-
27  bale a ⟨Canne|Canno⟩⟨,|∅⟩ come a' tempi moderni Paolo Orsino (1) a La-
28  dislao, il duca Giovanni al re Ferrando, una giornata è

[p. 65]

 1  bastante a farti perdere lo Stato⟨.|∅⟩ Portando la guerra a casa
 2  lo inimico, hai già disturbato il disegno suo di fare la
 3  guerra in casa tua, hai impedito le preparazioni necessarie
 4  a questo effetto, in modo che etiam vincendoti ha bisogno
 5  di tempo ⟨e|a⟩ di nuovi ordini a venire a guerreggiarti in
 6  casa; il che ti dà spazio a riordinarti e rifarti⟨.|∅⟩ E tanto più
 7  facilmente aderirei a questa conclusione, quanto io ve-
 8  dessi lo inimico non avere paese forte, o non avere sud-
 9  diti fedeli, o condizionato lo ⟨Stato|Stoto⟩ in modo che facilmente
10  si potessi disordinargli le entrate, o essergli difficile, se
11  avessi una rotta, a rifarsi in breve spazio di tempo⟨.|∅⟩ Veggo
12  che ⟨sempre|sempra⟩ e Romani, ⟨quando|qnando⟩ potettono, prevennono le
13  guerre a casa altri, contro a Filippo re di Macedonia, con-
14  tro a Antioco, contro a' Cartaginesi⟨,|;⟩ e quando non lo fe-
15  ciono, furono malcontenti di non l' avere fatto⟨.|∅⟩ Nè mi
16  muove quello che dice lo Scrittore, che se e Romani aves-
17  sino avuto in tanto spazio di tempo quelle tre rotte in
18  Francia, che gli ebbono in Italia da Annibale, sarebbono
19  sanza dubio stati spacciati⟨;|,⟩ perchè si pone uno caso im-
20  possibile, che chi ha una rotta in casa di altri, massime
21  in luogo ⟨lontano|lontono⟩, possi così subitamente dopo la prima rotta
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

- p. 63, line 16: cue "(1)" (superscript) immediately after "Ferrando⟨)|'⟩." , before "È dif-". Footnote (1) at foot of p. 63: first words "Ferdinando di Napoli, allora che Carlo"; last words "e perdette quello e lo Stato" (final stop not visible).
- p. 64, line 27: cue "(1)" after "Paolo Orsino" (preceded by a space), before "a La-". Footnote (1) at foot of p. 64: first words "Paolo Orsino fu condottiere dei Fiorentini"; last words "detta la Città Leonina" (final stop not visible).
- (Not in this unit: p. 62 cue "(1)" after "provede," in the preceding consideration; footnote "La guerra si fa col ferro ... jusqu'au bout du monde". Next unit, p. 66: cue after "fraude." , footnote "Senofonte nella Ciropedia ... simulazioni".)

# Uncertain loci

| # | page | line | reading | what is seen | alternative is |
|---|---|---|---|---|---|
| H1 | 62 | heading | XII⟨.\|∅⟩ | final stop after XII merged/abraded against the second I; a grey speck only | mark/pointing |
| R1 | 62 | rubric l.2 | guerra⟨.\|,⟩ | faint broken mark after "guerra", low, possibly with a tail | mark/pointing |
| 1 | 62 | 1 | ⟨assai\|aasai⟩ | first s printed like a (broken s) | non-word |
| 2 | 62 | 2 | l⟨'\|∅⟩ altra | gap after l, no apostrophe visible (cf. "l' una" on same line) | mark/pointing |
| 3 | 63 | 1 | Autore⟨.\|∅⟩ | no stop visible before "Perchè" | mark/pointing |
| 4 | 63 | 2 | distinzione⟨:\|∅⟩ | smudge after word, colon not clearly formed | mark/pointing |
| 5 | 63 | 3 | ⟨e'\|c'⟩ | initial letter broken, reads like c | non-word |
| 6 | 63 | 3 | oltre⟨.\|:⟩ | low dot preceded by thin space; upper dot of a colon may be lost | mark/pointing |
| 7 | 63 | 9 | ⟨entrate\|entrato⟩ | final letter closed like o | different word |
| 8 | 63 | 9 | ⟨che\|cho⟩ | line-final, final letter closed like o | non-word |
| 9 | 63 | 10 | ⟨guerra\|guorra⟩ | e printed like o | non-word |
| 10 | 63 | 12 | ⟨a\|n⟩ regolare | a broken, reads n | non-word |
| 11 | 63 | 13 | inimico⟨.\|∅⟩ | stop not visible before "È" | mark/pointing |
| 12 | 63 | 14 | dire⟨:\|∅⟩ | faint grey speck only | mark/pointing |
| 13 | 63 | 14 | sua⟨;\|.⟩ | low dot with very faint upper trace, after a gap | mark/pointing |
| 14 | 63 | 15 | dire⟨:\|;⟩ | broken vertical pair of marks | mark/pointing |
| 15 | 63 | 16 | Ferrando⟨)\|'⟩ | closing parenthesis broken to a short raised stroke (opening "(" before "e questo" is clear) | mark/pointing |
| 16 | 63 | 16 | ⟨È\|E⟩ dif- | mark above E is a speck; accent not certain | only a mark (accent) |
| 17 | 63 | 17 | dire⟨:\|∅⟩ | grey speck after word | mark/pointing |
| 18 | 63 | 18 | me⟨;\|,⟩ | comma clear; dot above faint | mark/pointing |
| 19 | 63 | 18 | dire⟨:\|∅⟩ | broken colon-like marks | mark/pointing |
| 20 | 63 | 20 | suo⟨∅\|,⟩ | wide gap after "suo", nothing visible | mark/pointing |
| 21 | 63 | 23 | Visconti⟨.\|∅⟩ | stop not clearly visible | mark/pointing |
| 22 | 64 | 1 | ⟨a\|o⟩ con parte | first letter broken (n-like shape, as broken a elsewhere on these pages) | different word |
| 23 | 64 | 1 | ⟨sue\|aue⟩ | s broken | non-word |
| 24 | 64 | 1 | ⟨e\|c⟩ inter- | e broken to c | non-word |
| 25 | 64 | 3 | ⟨la\|lo⟩ diversione | vowel broken, reads o/n | different word |
| 26 | 64 | 6 | ⟨lo\|la⟩ inimico | vowel broken | different word |
| 27 | 64 | 9 | ⟨forze\|forzo⟩ | final e closed like o | non-word |
| 28 | 64 | 13 | temporeggiando⟨.\|∅⟩ | stop not visible before "E" | mark/pointing |
| 29 | 64 | 16 | mici⟨.\|∅⟩ | stop not visible before "Ma" | mark/pointing |
| 30 | 64 | 17 | ⟨opportunità\|opportonità⟩ | u printed like o/n | non-word |
| 31 | 64 | 18 | ⟨sono\|sonn⟩ | final o broken | non-word |
| 32 | 64 | 20 | ⟨guerra\|gueı ra⟩ | first r broken into a short stroke and gap | non-word |
| 33 | 64 | 22 | altri⟨;\|,⟩ | comma with faint dot above | mark/pointing |
| 34 | 64 | 25 | rifarti ⟨,\|;⟩ | spaced comma, possible upper dot | mark/pointing |
| 35 | 64 | 27 | ⟨Canne\|Canno⟩ | final letter closed like o | non-word (or variant spelling) |
| 36 | 64 | 27 | Canne⟨,\|∅⟩ | faint mark only after word | mark/pointing |
| 37 | 65 | 1 | Stato⟨.\|∅⟩ | stop not visible before "Portando" | mark/pointing |
| 38 | 65 | 5 | tempo ⟨e\|a⟩ di | letter printed like a | different word |
| 39 | 65 | 6 | rifarti⟨.\|∅⟩ | stop faint/absent before "E" | mark/pointing |
| 40 | 65 | 9 | ⟨Stato\|Stoto⟩ | a printed like o | non-word |
| 41 | 65 | 11 | tempo⟨.\|∅⟩ | stop not visible before "Veggo" | mark/pointing |
| 42 | 65 | 12 | ⟨sempre\|sempra⟩ | final e printed like a | non-word |
| 43 | 65 | 12 | ⟨quando\|qnando⟩ | u printed like n | non-word |
| 44 | 65 | 14 | Cartaginesi⟨,\|;⟩ | comma, possible faint dot above | mark/pointing |
| 45 | 65 | 15 | fatto⟨.\|∅⟩ | stop not visible before "Nè" | mark/pointing |
| 46 | 65 | 19 | spacciati⟨;\|,⟩ | comma with faint upper trace | mark/pointing |
| 47 | 65 | 21 | ⟨lontano\|lontono⟩ | second a printed like o | non-word |
| 48 | 65 | 25 | ⟨sperare\|sporaro⟩ | e's closed like o | non-word |
| 49 | 65 | 26 | rotto⟨;\|,⟩ | comma with faint dot above | mark/pointing |
| 50 | 65 | 27 | Annibale⟨;\|,⟩ | comma with faint dot above | mark/pointing |
| 51 | 65 | 31 | Africa⟨.\|∅⟩ | only a grey smudge after final word | mark/pointing |

Policy: dotless or thinned i (ı), c/e and n/u variants that leave the word unambiguous (e.g. "inımico", "cbe", "balc", "rc") are transcribed silently as the evident letter; only breaks where another letter, word, or pointing is a real possibility are marked.
