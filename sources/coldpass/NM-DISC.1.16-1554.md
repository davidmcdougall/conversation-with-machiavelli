---
witness: "Machiavelli, Discorsi sopra la prima deca di Tito Livio, Venezia, Domenico Giglio, 1554 — Libro I, Cap. XVI"
source_images:
  - giglio-1-1of3.png
  - giglio-1-2of3.png
  - giglio-1-3of3.png
  - giglio-2-1of3.png
  - giglio-2-2of3.png
  - giglio-2-3of3.png
  - giglio-3-1of3.png
  - giglio-3-2of3.png
  - giglio-3-3of3.png
  - giglio-4-1of3.png
  - giglio-4-2of3.png
  - giglio-4-3of3.png
  - giglio-5-1of3.png
  - giglio-5-2of3.png
  - giglio-5-3of3.png
  - giglio-6-1of3.png (checked only for what follows)
start:
  rubric: "giglio-1, part 2of3, after the line ending '...ritornare piu uolte.' (end of Cap. XV); rubric opens with capitals 'VN POPOLO VSO A VIVERE', 4 lines, closing 'Cap. XVI.'"
  body: "giglio-1, part 2of3, immediately after the rubric: woodcut initial Q (4 lines deep), text 'Vanta difficulta...'"
end: "giglio-5 (fol. 31r), part 3of3, last line of a tapering cul-de-lampe paragraph, last words 'mostre-/remo.' followed by a fleuron"
follows: "giglio-6 (fol. 31v, head LIBRO) opens directly with the rubric of Cap. XVII ('VN POPOLO CORROTTO, VE-/nuto in liberta ...')"
leaves:
  - "giglio-1: head 'PRIMO.', folio 29 (first digit slightly doubtful, read as 2; consistent with 30 on giglio-3), signature 'C 5' at foot"
  - "giglio-2: head 'LIBRO', no folio (verso), no signature"
  - "giglio-3: head 'PRIMO.', folio 30, signature 'C 6' at foot"
  - "giglio-4: head 'LIBRO', no folio (verso), no signature"
  - "giglio-5: head 'PRIMO.', folio 31, no signature visible"
  - "giglio-6: head 'LIBRO', no folio (verso)"
word_count:
  body: 1188
  rubric: 21
  method: "Python whitespace split of the Body section after removing [giglio-N] markers, rejoining line-end hyphenated splits into single words, taking the preferred reading of each ⟨a|b⟩ locus, '&' counted as a word, apostrophe elisions (l'acquista, un'animale) counted as one token, punctuation-only tokens dropped. Rubric counted separately the same way (incl. 'Cap.' and 'XVI.')."
uncertain_loci: 22  # 21 inline-marked in Body + 1 leaf-metadata (folio 29)
expansions:
  - "giglio-1: cōseruare → conseruare"
  - "giglio-1: accidēte → accidente"
  - "giglio-2: nō (non puo nō che) → non"
  - "giglio-3: Cō-/soli → Con-/soli"
  - "giglio-3: chep̄ (p with stroke, set close to che) → che per (see uncertain locus)"
  - "giglio-4: uēdi-/carsi → uendi-/carsi"
  - "giglio-4: cōtra → contra"
  - "giglio-4: pūto → punto"
  - "giglio-4: cōgiu-/ratisi → congiu-/ratisi"
  - "giglio-4: nō aggiungono → non aggiungono"
  - "giglio-4: cō far → con far"
  - "giglio-5: cōtento → contento"
  - "Not expanded: 'Rep.' (giglio-4, suspension by full stop) left as printed."
  - "Long s → s throughout; ſſ and ß-form (ſs) ligatures → ss; ct/st ligatures resolved; '&' kept as printed (Giglio alternates '&' and 'et', both kept as printed)."
marginalia: "None. Only stray specks/dots in the left margins (show-through and dirt), no printed or manuscript marginal notes."
conventions: "u/v as printed (u for consonantal v in lower case; capital V as printed). Accents only where visible. Every word split at line end is marked '-' whether or not a hyphen is visible in the print (the compositor frequently omits it, e.g. 'ui/uere', 'ta/le'); where a hyphen-like mark is printed it is usually a small raised dot or dash. Line breaks of the print are kept. Leaf changes marked [giglio-N]."
---

# Rubric

[giglio-1]
VN POPOLO VSO A VIVERE
sotto un Prencipe, se per qualche accidente di-
uenta libero, con difficulta mantiene la liber-
tà. Cap. XVI.

# Body

[giglio-1]
QVanta difficulta sia ad un popolo uso a ui-
uere sotto un Prencipe conseruare dipoi la
liberta, se per alcuno accidente l'acquista,
come l'acquistò Roma dopo la cacciata
da Tarquini, lo dimostrano infiniti essempi, che si
leggono nelle memorie delle antiche historie. Et ta-
le difficulta è ragioneuole, perche quel popolo è non
altrimenti, che un'animale bruto, ilquale (anchora
che di feroce natura, & siluestre) sia stato nudrito
sempre in carcere, & in ⟨seruitu:|seruitu.⟩ che di poi lasciato
a sorte in una campagna libero, non essendo uso a
pascersi, ne sapendo le latebre, doue si habbia a ri-
fuggire, diuenta preda del primo, che cerca rinca-
[giglio-2]
tenarlo. ⟨Questomedesimo|Questo medesimo⟩ interuiene ad uno ⟨popolo;|popolo,⟩
ilquale essendo uso a uiuere sotto i gouerni de al-
tri, non sapendo ragionare ne delle difese, o offese
publiche, non conoscendo i Prencipi, ne essendo cono-
sciuto da loro, ritorna presto sotto un giogo, ilqua-
le il piu delle uolte e piu graue, che quello, che poco
innanzi si haueua leuato dal collo, & trouasi in
queste difficulta, anchora che la materia non sia in
tutto corrotta. Perche uno popolo, doue in tutto e
entrata la corruttione, non puo non che picciol tem-
po, ma punto uiuere libero, come disotto si discorre-
ra. Et pero i ragionamenti nostri sono di quei popo-
li, doue la corruttione non sia ampliata assai, et do-
ue sia piu del buono, che del ⟨guasto.⟩ Aggiungersi al-
la soprascritta un'altra difficulta, laquale e, che lo
⟨Stato|stato⟩, che diuenta libero, si fa partigiani nemici, et
non partigiani amici partigiani nemici gli diuen-
tano tutti coloro, che ⟨dello|delo⟩ stato tirannico si preua-
leuano, pascendosi delle ricchezze del Prencipe, a
quali essendo tolta la faculta del ualersi, non posso-
no uiuere contenti, et sono forzati ciascuno di ten-
tare di riassumere la tirannide per ritornare nel-
l'auttorita loro. Non si acquista ⟨(|)⟩ come ho detto)
partigiani amici, perche il uiuere libero propone
honori, et ⟨premij,|premij.,⟩ medianti alcune ⟨honeste,|honeste.,⟩ et de-
terminate cagioni, et fuori di quelle non pre-
mia, ne honora alcuno. Et quando uno ha
quelli honori, et quelli utili, che gli pare merita-
re, non confessa hauere obligo con coloro, che lo
rimunerano. Oltre a questo quella commune uti-
lita, che del uiuere libero si trahe, non e da alcuno
(mentre che ella si possiede) conosciuta, laquale
e, di potere godere liberamente ⟨le⟩ cose sue senza
alcuno sospetto, non dubitare dell'honore delle
donne, di quel de figliuoli, non tenere di se. Perche
[giglio-3]
nessuno confessera mai hauer obligo con uno, che
non l'offenda. Pero(come di sopra si dice) uiene ad
hauere lo stato libero, & che di nuouo surge parti-
giani nemici, & non partigiani amici. & uolendo
rimediare a questi ⟨incouenienti|inconuenienti⟩, & a quegli disor-
dini, che le soprascritte difficulta ci arrecherebbono
seco, non ci è piu potente rimedio, ne piu ualido, ne
piu sano, ne piu necessario, che amazzare i figliuoli
di Bruto, iquali, come l'historia mostra, non furono
indotti insieme con altri giouani Romani a congiu-
rare contra alla patria per altro, se non perche non
si poteuano ualere ⟨estraordinariamenne⟩ sotto i Con-
soli, come sotto i Re, in modo, che la libertà di quel
popolo ⟨pareua⟩ che fusse ⟨diuennuta⟩ la loro seruitù.
Et chi prende a gouernare una moltitudine o per
uia di liberta, o per uia di Prencipato, & non si as-
sicura di coloro, che a quell'ordine nuouo sono ne-
mici, fa uno stato di poca uita. Vero è, che io giudi-
co infelici quei Prencipi, ⟨che per|chep⟩ assicurare lo stato lo-
ro hanno a tenere uie estraordinarie, hauendo per
nemici la grandissima moltitudine: perche quello
che ha per nemici pochi, facilmente, & senza
molti scandali si assicura: ma chi ha per nemico
l'uniuersale, non si assicura mai, & quanto piu cru-
delta usa, tanto diuenta piu debole il suo prenci-
pato. Talche ⟨di⟩ maggior rimedio, che si habbia, e
cercare di farsi il popolo amico. Et benche questo
discorso sia diforme dal soprascritto, parlando
qui di uno buonissimo Prencipe, et quiui d'una Re-
publica; nondimeno per non hauere a tornare
piu in sù questa materia, ne uoglio parlare bre-
uemente. Volendo per tanto un Prencipe
guadagnarsi un popolo, che gli fusse nemi-
co (parlando di quei Prencipi, che sono diue-
nuti della loro patria tiranni) dico, ch'ei debbe
[giglio-4]
esaminare prima quello, che il Popolo desidera, &
trouerra sempre, ch'ei desidera due cose l'una uendi-
carsi contra a coloro, che sono cagione che sia seruo,
l'altra, di rihauere la sua liberta. Al primo deside-
rio il Prencipe puo satisfare in tutto, al secondo in
parte. Quanto al primo, ce n'è lo essempio a punto.
Clearcho tiranno di ⟨Eraclea|Eraslea⟩ essendo in esilio, oc-
corse che per controuersia uenuta tra il popolo, et
gli ottimati di Eraclea, che ueggendosi gli ottimati
inferiori, si uolsono a fauorire Clearcho, & congiu-
ratisi seco lo ⟨missono⟩ contra alla dispositione popo-
lare in Eraclea, & tolsono la liberta al popolo in
modo, che trouandosi Clearcho tra la insolentia de
gli ottimati, iquali non poteua in alcun modo ne
contentare, ne correggere, & la rabbia de popolari
che non poteuano sopportare lo hauere perduta la
liberta, delibero ad un tratto liberarsi dal fastidio
de grandi, et guadagnarsi il popolo. Et presa sopra
questo conueniente occasione, taglio a pezzi tutti
gli ottimati, ma con una estrema satisfattione de
popolari. Et cosi egli per questa uia satisfece ad
una delle uoglie, che hanno i popoli, cioè di uendi-
carsi. Ma quanto all'altro popolare desiderio di
rihauere la sua liberta, non potendo il Prencipe sa-
tisfargli, ⟨debbe⟩ essaminare quali cagioni sono, quel-
le, che gli fanno desiderare d'essere liberi, et trouer-
ra che una picciola parte di loro desidera d'essere
libera per commandare. Ma tutti glialtri, che so-
no infiniti, desiderano la libertà per uiuere secu-
ri. Perche in tutte le Rep. in qualunque modo or-
dinate, a i gradi del commandare non aggiungono
mai quaranta, o cinquanta cittadini: et perche que-
sto è picciolo numero, è facil cosa assicurarsene o
con leuargli uia, o con far lor parte di tanti honori,
che, secondo le conditioni loro, essi habbino in buo-
[giglio-5]
na parte a contentarsi. Quegli altri, a quali basta
uiuere securi, si satisfano facilmente, facendo ordi-
ni, et leggi, doue insieme con la potenza sua si com-
prenda la sicurita uniuersale. Et quando uno Pren-
cipe faccia questo, et che il popolo uegga, che per ac-
cidente nessuno ei non rompa tali leggi ⟨cominciera⟩
in breue tempo a uiuer securo, et contento. In essem-
pio ci e il Regno di Francia, il quale non uiue secu-
ro per altro, che per essersi quei Re obligati ad in-
finite leggi, nelle quali si comprende la sicurta di
tutti i suoi popoli. Et chi ordinò quello stato, uolle
che quei Re, dell'arme, et del danaio facessino a lo-
ro modo, ma che d'ogn'altra cosa non ne potessino
altrimenti disporre, che le leggi si ordinassino.
Quel Prencipe adunque, o quella Republica, che
non si assicura nel principio dello stato suo, con-
uiene, che si assicuri nella prima occasione, come
fecero i Romani. Chi lascia passare quella, si pente
tardi di non hauere fatto quello, che doueua fare.
Essendo per tanto il popolo Romano anchora non
corrotto, quando ei recupero la liberta, pote man-
tenerla, morti i figliuoli di Bruto, et spenti i
Tarquini, con tutti ⟨quei|quci⟩ rimedij, & ordini,
che altre uolte si sono discorsi. Ma se fosse
stato quel Popolo corrotto, ne in Ro-
ma, ne altroue si trouauano rime-
dij ualidi a mantenerla, co-
me nel seguente ca-
pitolo mostre-
remo.

# Uncertain loci

1. giglio-1 (3of3), "seruitu:" — the mark after the word is either a colon or a full stop with a speck; no accent visible on final u.
2. giglio-2 (1of3), "Questomedesimo" — no visible word space between Questo and medesimo; spacing doubtful.
3. giglio-2 (1of3), "popolo;" — line-end punctuation is a comma or semicolon (heavy, partly at margin edge).
4. giglio-2 (2of3), "guasto." — a stray mark (comma/semicolon-like) sits between the full stop and "Aggiungersi"; possibly dirt.
5. giglio-2 (2of3), "Stato" — initial letter looks like a capital S but is malformed; could be a damaged long-s lower case.
6. giglio-2 (2of3), "dello|delo" — print shows "de!o": a single tall broken letter between e and o; either one damaged l (delo) or a ligatured ll.
7. giglio-2 (2of3), "( come ho detto)" — the opening parenthesis is printed reversed, as ")".
8. giglio-2 (2of3), "premij.," — a full stop followed by a comma; the stop may be a speck.
9. giglio-2 (2of3), "honeste.," — same as above.
10. giglio-2 (3of3), "le cose" — a stray mark/broken sort immediately after "le"; reading "le" taken as intended.
11. giglio-3 (1of3), "incouenienti" — no tilde visible over o; printed apparently without n (inconuenienti expected sense).
12. giglio-3 (1of3), "estraordinariamenne" — read as printed with -menne; ink blurred, but no t visible.
13. giglio-3 (2of3), "pareua" — letters smudged ("p.reu.a"); reading probable.
14. giglio-3 (2of3), "diuennuta" — double n appears printed; blurred.
15. giglio-3 (2of3), "che per" — print shows "chep" with a stroke on p's descender (per abbreviation) and no space; expansion and spacing doubtful.
16. giglio-3 (2of3/3of3), "Talche di maggior" — "di" faint and partly broken ("dı").
17. giglio-4 (1of3), "missono" — second letter damaged (m'ssono); i reading probable.
18. giglio-4 (2of3), "debbe" — final letter damaged (debbε); e reading probable.
19. giglio-5 (1of3), "cominciera" — no accent visible on final a; final letter partly at line end.
20. giglio-5 (2of3), "quei|quci" — the third letter looks like c rather than e.
21. giglio-4 (1of3), "Eraclea|Eraslea" (first occurrence, line 7) — c is smudged and could be read as s.
22. giglio-1 (1of3), folio number "29" — first digit partly obscured; read 2 on the strength of folio 30 two images later. [Leaf metadata, not bracketed inline.]
