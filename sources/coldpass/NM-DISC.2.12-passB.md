---
unit: NM-DISC.2.12
reader: passB
source: "Machiavelli, Discorsi sopra la prima deca di Tito Livio, 1824 edition, vol. 1 (running head DISCORSI / LIBRO SECONDO), Libro II, Capitolo XII"
witness_images:
  - images/discorsi1824-page1-full.png  # p. 254
  - images/discorsi1824-page2-full.png  # p. 255
  - images/discorsi1824-page3-full.png  # p. 256
  - images/discorsi1824-page4-full.png  # p. 257 (signature line "MACHIAVELLI V. I  17" at foot)
  - images/discorsi1824-page5-full.png  # p. 258
  - images/discorsi1824-page6-full.png  # p. 259
  - images/discorsi1824-page7-full.png  # p. 260
  # crops -1-top/-2-middle/-3-bottom checked pixel-exact against each full page (offsets y=0, 947, 2023); all are what their names say.
boundaries:
  heading: "p. 254, after the end of chapter XI (\"la difesa propria.\"): CAPITOLO XII"
  rubric: "p. 254, two italic lines below the heading"
  body_start: "p. 254, line 1: \"Io ho sentito da uomini assai pratichi\" (large initial I)"
  body_end: "p. 260, line 3: \"difenderà meglio.\" (followed by heading CAPITOLO XIII)"
headings_printed:
  heading: "CAPITOLO XII"
  rubric: "S' egli è meglio, temendo di essere assaltato, inferire, o aspettare la guerra."
paragraphing: "One paragraph only: the body opens with a large initial I on p. 254 and runs without further indent or paragraph break to the end on p. 260 l. 3."
body_word_count: 1371
words_per_page: {254: 62, 255: 258, 256: 259, 257: 260, 258: 271, 259: 237, 260: 24}
word_count_method: "Python over this draft's Body with preferred readings; tokens = regex [^\\W\\d_]+'? (runs of letters with optional trailing apostrophe); each line-end-hyphenated word counted once on the page where it begins (including cross-page aspet-/ta p.256-257 and Per-/chè p.258-259); heading and rubric excluded; running heads, page numbers and signature excluded."
uncertain_loci_per_page: {254: 0, 255: 2, 256: 6, 257: 0, 258: 1, 259: 1, 260: 0}
uncertain_loci_total: 10
---

# Heading

[p. 254] CAPITOLO XII

# Rubric

(italic, two lines, centred)

S' egli è meglio, temendo di essere assaltato,
inferire, o aspettare la guerra.

# Body

Excluded from body: running heads (p. 254, 256, 258, 260 "DISCORSI"; p. 255, 257, 259 "LIBRO SECONDO"), page numbers, signature "MACHIAVELLI V. I" / "17" at foot of p. 257. Line numbers count from the first body text line of each page (on p. 254, from "Io ho sentito").
Latin, italics, notes, marginalia: none in the body. The only italic is the rubric. No footnotes, no marginal notes, no Latin quotation. Stray specks/marks noted under Uncertain loci.

[p. 254]

 1  Io ho sentito da uomini assai pratichi nelle cose
 2  della guerra qualche volta disputare, se sono duoi
 3  Principi quasi di eguali forze, se quello più ga-
 4  gliardo abbia bandito la guerra contro a quell'al-
 5  tro, quale sia miglior partito per l' altro, o aspet-
 6  tare il nimico dentro ai confini suoi, o andarlo a
 7  trovare in casa, ed assaltare lui. E ne ho sentito

[p. 255]

 1  addurre ragioni da ⟨ogni|ogm⟩ parte. E chi difende lo
 2  andare assaltare altrui ne allega il consiglio che
 3  Creso dette a Ciro, quando arrivato in su i con-
 4  fini ⟨de'Massageti|de' Massageti⟩ per fare loro guerra, la loro Re-
 5  gina Tamiri gli mandò a dire, che eleggesse quale
 6  de' duoi partiti volesse, o entrare nel Regno suo,
 7  dove essa lo aspetterebbe, o volesse che ella ve-
 8  nisse a trovar lui. E venuta la cosa in dispu-
 9  tazione, Creso contro all' opinione degli altri,
10  disse che si andasse a trovare lei; allegando che
11  se egli la vincesse discosto al suo Regno, che
12  ei non le torrebbe il Regno, perchè ella arebbe
13  tempo a rifarsi; ma se la vincesse dentro a' suoi
14  confini, potrebbe seguirla in su la fuga, e non
15  le dando spazio a rifarsi, torle lo Stato. Alle-
16  gano ancora il consiglio che dette Annibale ad
17  Antioco, quando quel Re disegnava fare guerra
18  ai Romani, dove ei mostrò come i Romani non
19  si potevano vincere se non in Italia, perchè quivi
20  altri si poteva valere dell'armi e delle ricchezze
21  e degli amici loro; ma chi li combatteva fuora
22  d'Italia, e lasciava loro l' Italia libera, lasciava
23  loro quella fonte, che mai le manca vita a som-
24  ministrare forze dove bisogna, e conchiuse che ai
25  Romani si poteva prima torre Roma che lo Im-
26  perio, e prima la Italia che le altre Provincie. Al-
27  lega ancora Agatocle, che non potendo sostenere
28  la guerra di casa, assaltò i Cartaginesi che gliene
29  facevano, e li ridusse a domandare pace. Allega
30  Scipione, che per levare la guerra d'Italia, assaltò

[p. 256]

 1  l'Affrica. Chi parla al contrario dice, che chi vuole
 2  fare capitare male uno nimico, lo discosti da ca-
 3  sa. Allegano gli Ateniesi, che mentre che feciono
 4  la guerra comoda alla casa loro restarono su-
 5  periori; come si discostarono, ed andarono con
 6  gli eserciti in Sicilia, perderono la libertà. Allega
 7  le favole poetiche dove si mostra, che Anteo Re
 8  di Libia, assaltato da Ercole Egizio, fu insupera-
 9  bile mentrechè lo aspettò dentro ⟨a'confini|a' confini⟩ del suo
10  Regno, ma come e'se ne discostò per astuzia di
11  Ercole, perdè lo Stato ⟨∅|'⟩e la vita. Onde è dato luo-
12  go alla favola di Anteo, che sendo in terra ripi-
13  gliava le forze da sua madre che era la Terra, e
14  che Ercole avvedutosi di questo lo levò in alto,
15  e discostollo dalla terra. Allegane ancora i giudizj
16  moderni. Ciascuno sa come Ferrando Re di Na-
17  poli fu ne'suoi tempi tenuto un savissimo Prin-
18  cipe, e venendo la fama duoi anni avanti la sua
19  morte, come il Re⟨∅|.⟩ di Francia Carlo VIII voleva
20  venire ad assaltarlo, avendo fatte assai prepara-
21  zioni ammalò, e venendo a morte, tra gli altri
22  ricordi che lasciò ad Alfonso suo figliuolo, fu che
23  egli aspettasse il nimico dentro al Regno, e per
24  cosa del Mondo non traesse forze fuori dello Stato
25  suo, ma lo ⟨aspettase|aspettasse⟩ ⟨∅|,⟩dentro a'suoi confini tutto
26  intero; il che non fu osservato da quello; ma man-
27  dato un esercito in Romagna, senza combattere
28  perdè quello e lo Stato. Le ragioni che oltre alle
29  ⟨cose|cosè⟩ dette da ogni parte si adducono, sono: Che
30  chi assalta viene con maggiore animo che chi aspet-

[p. 257]

 1  ta, il che fa più confidente lo esercito; toglie oltra
 2  di questo molte comodità al nimico di potersi va-
 3  lere delle sue cose, non si potendo valere di
 4  quei sudditi che sieno saccheggiati; e per avere
 5  il nimico in casa è costretto il signore avere più
 6  rispetto a trarre da loro danari e affaticarli, sic-
 7  chè e' viene a seccare quella fonte, come dice
 8  Annibale, che fa che colui può sostenere la guer-
 9  ra. Oltre di questo i suoi soldati, per trovarsi nei
10  paesi altrui, sono più necessitati a combattere, e
11  quella necessità fa virtù, come più volte abbiamo
12  detto. Dall' altra parte si dice, come aspettando il
13  nimico si aspetta con assai vantaggio, perchè senza
14  disagio alcuno tu puoi dare a quello molti disagi
15  di vettovaglia, e d' ogni altra cosa che abbia bi-
16  sogno uno esercito; puoi meglio impedirgli i di-
17  segni suoi, per la notizia del paese che tu hai più
18  di lui: puoi con più forze incontrarlo, per poterle
19  facilmente tutte unire, ma non potere già tutte
20  discostarle da casa; puoi sendo rotto rifarti facil-
21  mente, sì perchè del tuo esercito se ne salverà as-
22  sai, per avere i rifugj propinqui, sì perchè il sup-
23  plemento non ha a venire discosto; tanto che tu
24  vieni ad arrischiare tutte le forze, e non tutta la
25  fortuna, e discostandoti arrischi tutta la fortuna,
26  e non tutte le forze. Ed alcuni sono stati, che per
27  indebolire meglio il suo nimico, lo lasciano en-
28  trare parecchie giornate in su il paese loro, e pi-
29  gliare assai Terre, acciò che, lasciando i presidj in
30  tutte, indebolisca il suo esercito, e possanlo dipoi

[p. 258]

 1  combattere più facilmente. Ma per dire ora io quello
 2  che io ne intendo, io credo che si abbia a fare
 3  questa distinzione: o io ho il mio paese armato,
 4  come i Romani, e come l' hanno i Svizzeri; o io
 5  l' ho disarmato, come l' avevano i Cartaginesi, e
 6  come l' hanno i Re di Francia e gl'Italiani. In que-
 7  sto caso si debbe tenere il nimico discosto a casa;
 8  perchè sendo la tua virtù nel danaro e non negli
 9  uomini, qualunque volta ti è impedita la via di
10  quello, tu sei spacciato, nè cosa veruna te lo im-
11  pedisce, quanto la guerra di casa. In esempj ci sono
12  i Cartaginesi, i quali mentre che ebbero la casa
13  loro libera, poterono con le rendite fare guerra
14  coi Romani, e quando l' avevano assaltata, non
15  potevano resistere ad Agatocle. I Fiorentini non
16  avevano rimedio alcuno con Castruccio signore di
17  Lucca, perchè ei faceva loro la guerra in casa,
18  tanto ch' egli ebbero a darsi, per essere difesi, al
19  Re Roberto di Napoli. Ma morto Castruccio, quelli
20  medesimi Fiorentini ebbero animo di assaltare il
21  Duca di Milano in casa, e operare di torgli il Re-
22  gno: tanta virtù mostrarono nelle guerre longin-
23  que, e tanta viltà nelle propinque! Ma quando i
24  Regni sono armati, come era armata Roma, e come
25  sono i Svizzeri, sono più difficili a vincere quanto
26  più ti appressi a loro. Perchè questi Corpi possono
27  unire più forze a resistere ad uno impeto, che non
28  possono⟨ |·⟩ad assaltare altrui. Nè mi muove in que-
29  sto caso l'autorità d'Annibale, perchè la passione
30  e l' utile suo gli faceva così dire ad Antioco. Per-

[p. 259]

 1  chè se i Romani avessero avute in tanto spazio
 2  di tempo quelle tre rotte in Francia, ch' egli eb-
 3  bero in Italia da Annibale, senza dubbio erano
 4  spacciati; perchè non si sarebbero valuti dei re-
 5  sidui degli eserciti, come si valsero in Italia, non
 6  arebbero avuto a rifarsi quelle comodità, nè pote-
 7  vano con quelle ⟨forze|f̕orze⟩ resistere al nimico che po-
 8  terono. Non si trova che per assaltare una Pro-
 9  vincia, mandassero mai fuora eserciti che pas-
10  sassero cinquantamila persone; ma per difende-
11  re la casa ne misero in arme contro ai Francesi,
12  dopo la prima guerra punica, diciotto centinaja
13  di migliaja. Nè arebbono potuto poi romper quelli
14  in Lombardia, come li ruppero in Toscana; per-
15  chè contro a tanto numero di inimici non areb-
16  bono potuto condurre tante forze sì discosto, nè
17  combatterli con quella comodità. I Cimbri rup-
18  pero uno esercito romano in la Magna, nè vi eb-
19  bero i Romani rimedio. Ma come egli arrivarono
20  in Italia, e che poterono mettere tutte le loro forze
21  insieme, gli spacciarono. Gli Svizzeri è facile vin-
22  cerli fuori di casa, dove e' non possono mandare
23  più che un trenta o quarantamila uomini; ma vin-
24  cerli in casa, dove e' ne possono raccozzare cen-
25  tomila, è difficilissimo. Conchiudo adunque di
26  nuovo, che quel Principe che ha i suoi Popoli
27  armati e ordinati alla guerra, aspetti sempre in
28  casa una guerra potente e pericolosa, e non la
29  vada a rincontrare. Ma quello che ha i suoi sud-
30  diti disarmati, ed il paese inusitato alla guerra,

[p. 260]

 1  se la discosti sempre da casa il più che può. E
 2  così l' uno e l' altro, ciascuno nel suo grado, si
 3  difenderà meglio.

# Uncertain loci

1. p. 255, l. 1 — "⟨ogni|ogm⟩": the n of "ogni" is damaged/blotted and looks like m or rn. Alternative would be a non-word; preferred "ogni".
2. p. 255, l. 4 — "⟨de'Massageti|de' Massageti⟩": unclear whether a space follows the apostrophe. Mark/spacing only.
3. p. 256, l. 9 — "⟨a'confini|a' confini⟩": spacing after apostrophe unclear. Mark/spacing only.
4. p. 256, l. 11 — "Stato ⟨∅|'⟩e": a small raised stray mark (accent- or apostrophe-like) just before "e". Probably a speck; mark only.
5. p. 256, l. 19 — "Re⟨∅|.⟩ di Francia": a dot below/after "Re". Probably a speck; mark/pointing only.
6. p. 256, l. 25 — "⟨aspettase|aspettasse⟩": printed with a single s as far as I can see. The alternative is a different spelling of the same word (preferred reading keeps what is printed).
7. p. 256, l. 25 — "⟨∅|,⟩dentro": a low comma-like mark before "dentro". Probably a speck; pointing only.
8. p. 256, l. 29 — "⟨cose|cosè⟩": a dot/mark above the final e. Preferred "cose" (speck); alternative "cosè" would be a non-word in context. Mark only.
9. p. 258, l. 28 — "possono⟨ |·⟩ad": a raised dot between the words. Probably a speck or raised space; mark only.
10. p. 259, l. 7 — "⟨forze|f̕orze⟩": a small stray mark above the f. Speck; mark only.

Apostrophe spacing elsewhere is given as seen (e.g. "l' altro", "quell'al-", "dell'armi", "d' ogni", "gl'Italiani", "ne'suoi", "e'se") with ordinary confidence; spacing before commas/semicolons (e.g. "di casa ,", "Svizzeri ;") is normalised and not recorded.
