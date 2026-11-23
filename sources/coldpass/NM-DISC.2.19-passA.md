---
unit: NM-DISC.2.19
reader: "cold reader nmA (Pass A)"
source: "Niccolò Machiavelli, Discorsi sopra la prima deca di Tito Livio, Italia [Firenze], 1824, vol. 2, Libro secondo, pp. 5-11"
witness_images:
  # every file: size matches MANIFEST, sha256 first 16 hex matches MANIFEST; every part image pixel-identical to rows A-B of its -page image (numpy array equality, RGB)
  - {file: 1824-p005-page.png, size: [2178, 3282], rows: 3282, sha256: 96d06cdd002c6af4, check: "manifest OK"}
  - {file: 1824-p005-part1of3-y0-1225.png, size: [2178, 1225], rows: "0-1225", sha256: 8219290b2472a5a8, check: "manifest OK; pixel-identical to page rows 0-1225"}
  - {file: 1824-p005-part2of3-y963-2319.png, size: [2178, 1356], rows: "963-2319", sha256: c616bb89537ce006, check: "manifest OK; pixel-identical"}
  - {file: 1824-p005-part3of3-y2057-3282.png, size: [2178, 1225], rows: "2057-3282", sha256: 323d7883f98478b6, check: "manifest OK; pixel-identical"}
  - {file: 1824-p006-page.png, size: [2178, 3282], rows: 3282, sha256: f3a24757cb18d240, check: "manifest OK"}
  - {file: 1824-p006-part1of3-y0-1225.png, size: [2178, 1225], rows: "0-1225", sha256: a8d9c3e8da9d513b, check: "manifest OK; pixel-identical"}
  - {file: 1824-p006-part2of3-y963-2319.png, size: [2178, 1356], rows: "963-2319", sha256: d74e5ba2c41f8438, check: "manifest OK; pixel-identical"}
  - {file: 1824-p006-part3of3-y2057-3282.png, size: [2178, 1225], rows: "2057-3282", sha256: 7d0c0911c086611a, check: "manifest OK; pixel-identical"}
  - {file: 1824-p007-page.png, size: [2178, 3282], rows: 3282, sha256: 411806e7395478b0, check: "manifest OK"}
  - {file: 1824-p007-part1of3-y0-1225.png, size: [2178, 1225], rows: "0-1225", sha256: c03fee4179e1584e, check: "manifest OK; pixel-identical"}
  - {file: 1824-p007-part2of3-y963-2319.png, size: [2178, 1356], rows: "963-2319", sha256: 6969b503302a14d4, check: "manifest OK; pixel-identical"}
  - {file: 1824-p007-part3of3-y2057-3282.png, size: [2178, 1225], rows: "2057-3282", sha256: 263a720d285f3006, check: "manifest OK; pixel-identical"}
  - {file: 1824-p008-page.png, size: [2178, 3282], rows: 3282, sha256: 9ac2c98d4afc5ced, check: "manifest OK"}
  - {file: 1824-p008-part1of3-y0-1225.png, size: [2178, 1225], rows: "0-1225", sha256: cf4483d4ef97612a, check: "manifest OK; pixel-identical"}
  - {file: 1824-p008-part2of3-y963-2319.png, size: [2178, 1356], rows: "963-2319", sha256: 92ff0e8c0f7a552e, check: "manifest OK; pixel-identical"}
  - {file: 1824-p008-part3of3-y2057-3282.png, size: [2178, 1225], rows: "2057-3282", sha256: 69e0b6e08c91120a, check: "manifest OK; pixel-identical"}
  - {file: 1824-p009-page.png, size: [2178, 3282], rows: 3282, sha256: 5104edb440c7f859, check: "manifest OK"}
  - {file: 1824-p009-part1of3-y0-1225.png, size: [2178, 1225], rows: "0-1225", sha256: 3b801b7a5fb97602, check: "manifest OK; pixel-identical"}
  - {file: 1824-p009-part2of3-y963-2319.png, size: [2178, 1356], rows: "963-2319", sha256: b0e598ff41f01b5b, check: "manifest OK; pixel-identical"}
  - {file: 1824-p009-part3of3-y2057-3282.png, size: [2178, 1225], rows: "2057-3282", sha256: 07751b704458d9a6, check: "manifest OK; pixel-identical"}
  - {file: 1824-p010-page.png, size: [2178, 3282], rows: 3282, sha256: d9e7b3efe0466a4c, check: "manifest OK"}
  - {file: 1824-p010-part1of3-y0-1225.png, size: [2178, 1225], rows: "0-1225", sha256: 9569b640e55a31b8, check: "manifest OK; pixel-identical"}
  - {file: 1824-p010-part2of3-y963-2319.png, size: [2178, 1356], rows: "963-2319", sha256: ea77599ad4bfa4df, check: "manifest OK; pixel-identical"}
  - {file: 1824-p010-part3of3-y2057-3282.png, size: [2178, 1225], rows: "2057-3282", sha256: 4300f75d4329286e, check: "manifest OK; pixel-identical"}
  - {file: 1824-p011-page.png, size: [2178, 3282], rows: 3282, sha256: 658430ee8d446708, check: "manifest OK"}
  - {file: 1824-p011-part1of3-y0-1225.png, size: [2178, 1225], rows: "0-1225", sha256: 0f8bb59c9e112ee9, check: "manifest OK; pixel-identical"}
  - {file: 1824-p011-part2of3-y963-2319.png, size: [2178, 1356], rows: "963-2319", sha256: 0a2031fb88cd740e, check: "manifest OK; pixel-identical"}
  - {file: 1824-p011-part3of3-y2057-3282.png, size: [2178, 1225], rows: "2057-3282", sha256: 2a0563a597ef23f8, check: "manifest OK; pixel-identical"}
boundaries:
  precedes: "Nothing of the text precedes on p. 5: the chapter opens the volume's text. Above the heading stands only the volume half-title matter (not body): 'DISCORSI' / 'SOPRA' / 'LA PRIMA DECA DI T. LIVIO' / 'LIBRO SECONDO' / swelled rule. No earlier chapter (II.18) is on the images."
  heading: "CAPITOLO XIX — p. 5, centred, roman capitals (letter-spaced), no final punctuation"
  rubric: "Italic, 4 lines, hanging indent (line 1 at margin, lines 2-4 indented ~60 px): 'Che gli acquisti nelle Repubbliche non bene or-' / 'dinate, e che secondo la romana virtù non' / 'procedono, sono a rovina, non a esaltazione' / 'di esse.' — a declarative 'Che ...' title clause; ends with a full stop."
  first_words: "Queste contrarie opinioni alla verità, fondate (p. 5, body l. 1; large initial Q, indented)"
  last_words: "ni, di che nel seguente capitolo si farà menzione. (p. 11, body l. 11; full stop)"
  follows: "p. 11, after a blank: heading 'CAPITOLO XX' (centred roman caps), italic rubric 'Quanto pericolo porti quel Principe o quella Re-' / 'pubblica, che si vale della milizia ausiliaria' / 'e mercenaria.' (hanging indent), then body with large initial S: 'Se io non avessi lungamente trattato in altra' ... p. 11 ends 'Romani in diversi luoghi rotti due eserciti dei'."
  line_numbering: "Body lines numbered per page from the first body line on that page (heading, rubric and running head not counted): p.5 ll.1-9, pp.6-10 ll.1-30 each, p.11 ll.1-11. Total body lines 170."
headings_printed:
  - {page: 5, text: "DISCORSI", style: "large roman capitals, half-title"}
  - {page: 5, text: "SOPRA", style: "small letter-spaced capitals"}
  - {page: 5, text: "LA PRIMA DECA DI T. LIVIO", style: "letter-spaced capitals; full stop after T"}
  - {page: 5, text: "LIBRO SECONDO", style: "letter-spaced capitals, followed by a short swelled (thick-centred) rule"}
  - {page: 5, text: "CAPITOLO XIX", style: "centred roman capitals, no punctuation"}
  - {page: 11, text: "CAPITOLO XX", style: "centred roman capitals, no punctuation (following unit)"}
running_heads_etc:
  p5: "No running head and no printed page number (opening page of the volume's text; page 5 inferred from p. 6 following). No signature or catchword visible. Pencil shelfmark top left, faint and partly illegible: '?53M17' / 'Oj 1824' / 'v. 2' (first character unclear). Blue-ink stamped accession number '545049' centred in the bottom margin. Faint offset/bleed marks along the left (gutter) edge; a stray dot left of 'DISCORSI'; a stray dot above the space between 'e' and 'con' (body l. 8)."
  p6: "Running head: page number '6' at left, 'DISCORSI' centred (letter-spaced small caps). No signature, no catchword, no footnote."
  p7: "Running head: 'LIBRO SECONDO' centred, '7' at right. No signature, catchword or footnote."
  p8: "Running head: '8' left, 'DISCORSI' centred. No signature, catchword or footnote."
  p9: "Running head: 'LIBRO SECONDO' centred, '9' right. No signature, catchword or footnote. Stray marks in outer margins (dot at left of l. 3, small tick at right of l. 10)."
  p10: "Running head: '10' left (set as '1o' with old-style figures), 'DISCORSI' centred. Page image rotated ~1.5 degrees. No signature, catchword or footnote."
  p11: "Running head: 'LIBRO SECONDO' centred, '11' right. No signature, catchword or footnote."
  footnotes: "None on any page."
paragraphing: "Pixel scan of the left ink edge of every body line (threshold <110-130 grey, column cluster test; p.10 deskewed by 1.5 degrees; pages 7, 9, 11 drift 340-370 px with gutter skew). Only one indented line: p.5 l.1 (initial Q at x~418-421 against body edge ~353-364, i.e. ~60 px indent). All other 169 body lines are flush within the page's drift (p6 462-471, p7 339-360, p8 448-460, p9 348-361, p10 462-478, p11 360-371). The chapter is a single paragraph. (On p.7 a few line bands merged in the automatic scan; those lines were checked visually and are flush.)"
body_word_count: 1392
words_per_page: {p5: 72, p6: 253, p7: 245, p8: 254, p9: 241, p10: 235, p11: 92}
word_count_method: "Body only (heading, rubric, half-title, running heads excluded); preferred readings; tokens split on whitespace and after every apostrophe (each elided form a separate word); a token counts if it contains a letter; a word hyphenated at line end counted once, on the line/page where it begins (no word is hyphenated across a page break). Italic Latin counted."
uncertain_loci_per_page: {p5: 1, p6: 4, p7: 2, p8: 6, p9: 2, p10: 1, p11: 0}
uncertain_loci_total: 16
conventions: "Diplomatic, line for line; [p. N] at each page start. Line-end hyphens kept as printed ('-'). Accents, j (esempj, ajuti, esercizj, mercenarj, ausiliarj, Juvenale), capitals and spelling as printed. Italic as *...*, closed and reopened at each line end. The question mark is printed in the period form resembling a reversed 7; transcribed '?'. Spacing after apostrophes: measured in pixels from apostrophe to next letter; gaps of 3-8 px transcribed as no space (d'arme p6 l11, d'abitatori p6 l24, ch'era p7 l11), gaps of 10 px and above as ' ' (apostrophe + space); gaps of 10-11 px are flagged as uncertain. Spacing before punctuation (e.g. 'fanteria ;', 'Novara ?') is variable thin spacing and is NOT recorded (normalised to none). Word spaces normalised to one. Stray ink dots and specks that are not on a letter are reported in Notes, not in the text. ⟨preferred|alternative⟩ marks doubt; preferred reading first."
paths_written:
  - /home/claude/w/readers/nmA/out/NM-DISC.2.19-passA.md
  - "/home/claude/w/readers/nmA/work/ (scratch: check.py, lines.py, left.py, apos*.py, crop.py, mont.py, body.txt, crop/montage PNGs)"
---

# Body

Rubric: *Che gli acquisti nelle Repubbliche non bene or-*
*dinate, e che secondo la romana virtù non*
*procedono, sono a rovina, non a esaltazione*
*di esse.*

[p. 5]
Queste contrarie opinioni alla verità, fondate
in sui mali esempj, che da questi nostri corrotti
secoli sono stati introdotti, fanno che gli uomini
non pensano a deviare dai consueti modi. Quando
si sarebbe potuto persuadere ad uno Italiano da
trenta anni in dietro che diecimila fanti potessero
assaltare in un piano diecimila cavalli, ed altret-
tanti fanti, e con quelli non solamente combattere
⟨má|ma⟩ vincerli, come si vede per lo esempio da noi
[p. 6]
più volte allegato a Novara? E benchè le Istorie
ne siano piene, *tamen* non ci arebbero prestato
fede; e se ci avessero prestato fede, arebbero detto
che in questi tempi s' arma meglio⟨,|;⟩ e che una squa-
dra di uomini d' arme sarebbe atta ad urtare uno
scoglio, non che una fanteria; e così con queste
false scuse corrompevano il giudicio loro: nè areb-
bero considerato, che Lucullo con pochi fanti ruppe
cento cinquantamila cavalli di Tigrane, e che tra
quelli cavalieri era una sorte di cavalleria simile al
tutto agli uomini d'arme nostri; e ⟨così|cósì⟩ questa fallacia
è stata scoperta dallo esempio delle genti oltramon-
tane. E come ⟨e' si|e'si⟩ vede per quello esser vero, quanto
alla fanteria, quello che nelle Istorie si narra,
così doverebbero credere essere veri ed utili tutti
gli altri ordini antichi. E quando questo fusse cre-
duto, le Repubbliche ed i Principi errerebbero me-
no, sariano più forti ad opporsi ad uno impeto
che venisse loro addosso, non ⟨spererebbero|spererèbbero⟩ nel-
la fuga, e quelli che avessero nelle mani un
vivere civile, lo saperebbero meglio indirizzare,
o per la via dello ampliare, o per la via del man-
tenere, e crederebbero che l' accrescere la Città
sua d'abitatori, farsi compagni e non sudditi, man-
dare colonie a guardare i paesi acquistati, far ca-
pitale delle prede, domare il nimico con le scor-
rerie e con le Giornate, e non con le ossidioni,
tener ricco il Pubblico, povero il privato, man-
tenere con sommo studio gli esercizj militari, sono
le vie a far grande una Repubblica ed acquistare
[p. 7]
imperio. E quando questo modo dello ampliare
non gli piacesse, penserebbe che gli acquisti per
ogni altra via sono la rovina delle Repubbliche,
e porrebbe freno ad ogni ambizione, regolando
bene la sua Città dentro con le leggi e co' costu-
mi, proibendogli l' acquistare e solo pensando a
difendersi, e le difese tenere ordinate bene, come
fanno le Repubbliche della Magna, le quali in
questi modi vivono e sono vivute libere un tem-
po. Nondimeno, come altra volta dissi, quando
discorsi la differenza ch'era da ordinarsi per acqui-
stare, a ordinarsi per mantenere, è impossibile
che ad una Repubblica riesca lo stare quieta, e
godersi la sua libertà e gli pochi confini; perchè
se lei non molesterà altrui, sarà molestata ella; e
dall' essere molestata gli nascerà la voglia, e la
necessità dello ⟨acquistare|àcquistare⟩; e quando non avesse
il nimico fuora, lo troverebbe in casa, come pare
necessario intervenga a tutte le grandi Cittadi. E
se le Repubbliche della Magna possono vivere loro
in quel modo, ed hanno potuto durare un tempo,
nasce da certe condizioni che sono in quel paese,
le quali non sono altrove, senza le quali non po-
trebbero tenere simil modo di vivere. Era quella
parte della Magna di che io parlo, sottoposta al-
l' Imperio romano come la Francia e la Spagna,
ma venuto dipoi in declinazione l' Imperio, e
ridottosi il titolo di tal Imperio in quella Provin-
cia, cominciarono quelle ⟨Cittadi|Cittàdi⟩ più potenti, se-
condo la viltà o necessità degli Imperatori, a farsi
[p. 8]
libere, ricomperandosi dallo Imperio con riservar-
gli un piccolo censo annuario; tanto che a poco
a poco tutte quelle Cittadi, ch' erano immediate
dello Imperatore, e non erano soggette ad alcun
Principe, si sono in simil modo ricomperate. Oc-
corse in questi medesimi tempi che queste Cittadi
si ricomperavano, che certe Comunità sottoposte
al Duca d' Austria si ribellarono da lui, tra le
quali fu ⟨Filiburgo|Filibúrgo⟩ e i Svizzeri e simili; le quali
prosperando nel principio, pigliarono a poco a poco
tanto augumento, che non che ⟨e' sieno|e'sieno⟩ tornati sotto
il giogo ⟨d' Austria|d'Austria⟩, sono in timore a tutti i loro
vicini; e questi sono quelli che si chiamano Sviz-
zeri. È adunque questa Provincia compartita in
Svizzeri, Repubbliche, che chiamano Terre fran-
che, Principi, ed Imperatore. E la cagione che
tra tante diversità di vivere non vi nascono, o se
le vi nascono, non vi durano molto le guerre, è
quel segno ⟨dell' |dell'⟩⟨Imperatore|Imperàtore⟩; il quale, avvenga che
non abbia forze, nondimeno ha fra loro tanta ri-
putazione, ch' egli è uno loro conciliatore, e con
l' autorità sua interponendosi come mezzano, spe-
gne subito ogni scandalo. E le maggiori e le più
lunghe guerre che vi siano state, sono quelle che
furono seguìte tra i Svizzeri e il Duca ⟨d' Austria|d'Austria⟩;
e benchè da molti anni in qua l' Imperatore ed
il Duca d' Austria sia una cosa medesima, non
pertanto non ha mai potuto superare l' audacia
dei Svizzeri, dove non è mai stato modo d' accor-
do, se non per forza. Nè il resto della Magna gli
[p. 9]
ha porti molti ajuti, sì perchè le Comunità non
sanno offendere chi vuole vivere libero come loro,
sì perchè quelli Principi, parte non possono per
essere poveri, parte non vogliono per aver invi-
dia alla potenza sua. Possono vivere adunque quel-
le Comunità contente del piccolo loro dominio,
per non aver cagione, rispetto all' autorità impe-
riale, di desiderarlo maggiore; possono vivere unite
dentro alle mura loro, per aver il nimico propin-
quo, e che piglierebbe l' occasione d' occuparle,
qualunque volta le discordassero. Che se quella
Provincia fusse condizionata altrimenti, conver-
rebbe loro cercare d' ampliare, e rompere quella
loro quiete. E perchè altrove non sono tali con-
dizioni, non si può prendere questo modo di vi-
vere, e bisogna o ampliare per vie di Leghe, o
ampliare come i Romani. E chi si governa altri-
menti cerca non la sua vita, ma la sua morte e
rovina; perchè in mille modi e per molte cagioni
gli acquisti sono dannosi, perchè egli sta molto
bene insieme acquistare Imperio e non forze; e
⟨chi|chi'⟩ acquista imperio e non forze insieme, con-
viene che rovini. Non può acquistare forze chi
impoverisce nelle guerre, ancora che sia vittorio-
so, che ei mette più che non trae degli acqui-
sti; come hanno fatto i Veneziani e i Fiorentini, i
quali sono stati molto più deboli, quando l' uno
aveva la Lombardia e l' altro la Toscana, che
non erano quando l' uno era contento del ⟨Ma-|Ma-,⟩
re, e l' altro di sei miglia di confini. Perchè
[p. 10]
tutto è nato da avere voluto acquistare, e non
avere saputo pigliare il modo; e tanto più me-
ritano biasimo, quanto egli hanno meno scusa,
avendo veduto il modo che hanno tenuto i Roma-
ni, ed avendo potuto seguitare il loro esempio,
quando i Romani senz' alcuno esempio, per la pru-
denza loro, da loro medesimi lo seppero trovare.
Fanno oltra di questo gli acquisti qualche volta
non mediocre danno ad ogni bene ordinata Re-
pubblica, quando e' si acquista una Città, o una
Provincia piena di delizie, ⟨dove|dovè⟩ si può pigliare
di quelli costumi per la conversazione che si ha
con quelli; come intervenne a Roma prima nel-
l' acquisto di Capova, e dipoi ad Annibale. E se
Capova fusse stata più longinqua dalla Città, e
che lo errore de' soldati non avesse avuto il rime-
dio propinquo, o che Roma fusse stata in alcuna
parte corrotta, era senza dubbio quell' acquisto
la rovina della Repubblica romana. E Tito Livio
fa fede di questo con queste parole: *Jam tunc*
*minime salubris militari disciplinae Capua, instru-*
*mentum omnium voluptatum, delinitos militum*
*animos avertit a memoria patriae.* E veramente
simili Città o Provincie si vendicano contro al
vincitore senza zuffa e senza sangue, perchè riem-
piendoli de' suoi tristi costumi, gli espongono ad
esser vinti da qualunque gli assalta. E Juvenale
non potrebbe meglio nelle sue Satire aver consi-
derata questa parte, dicendo che ne' petti romani,
per gli acquisti delle Terre peregrine, erano entrati
[p. 11]
i costumi peregrini, ed in cambio di parsimonia
e d' altre eccellentissime virtù, *gula, et luxuria*
*incubuit, victumque ulciscitur orbem.* Se adunque
l' acquistare fu per essere pernicioso ai Romani,
ne' tempi che quelli con tanta prudenza e tanta
virtù procedevano, che sarà adunque a quelli che
discosto dai modi loro procedono? E che oltre
agli altri errori che fanno, di che se ne è di sopra
discorso assai, si vagliono dei soldati o mercenarj
o ausiliarj? Donde ne risulta loro spesso quei dan-
ni, di che nel seguente capitolo si farà menzione.


# Notes on the page

- p. 5: the volume opens directly with Book II ch. XIX under the half-title matter 'DISCORSI / SOPRA / LA PRIMA DECA DI T. LIVIO / LIBRO SECONDO' and a swelled rule; no page number printed. Pencil shelfmark top left ('?53M17 / Oj 1824 / v. 2', partly illegible) and blue stamp '545049' in the foot margin are library marks, not text.
- p. 5 l. 1: large initial 'Q' (about 1.5 lines high), set indented.
- p. 5 l. 8: stray dot above the space between 'e' and 'con'.
- p. 5 l. 9: 'má' — a dark slanting stroke stands over the a of 'ma'; recorded as printed, see loci.
- p. 6 l. 4: small blob above the comma after 'meglio', above x-height (not the dot of a semicolon at mid x-height).
- p. 6 l. 6: tiny dot below the i of 'così' (accent on i is a clear grave).
- p. 6 l. 11: round dot over the o of 'così' (not an accent shape).
- p. 6 l. 15: stray mid-height dot between 'essere' and 'veri'.
- p. 6 l. 19: round dot over the second-last e of 'spererebbero'.
- p. 7 l. 4: stray dot after 'freno'. l. 17: round dot over the a of 'acquistare'. l. 23: a brown dot above 'po-' (foxing/ink speck); faint mark over the a of 'altrove'. l. 29: short vertical tick above the a of 'Cittadi'. l. 30: stray mid dot between 'degli' and 'Imperatori'.
- p. 8 l. 1: dot below the m of 'Imperio'. l. 9: faint slanting stroke over the u of 'Filiburgo'. l. 14: small slanting stroke immediately before 'in'. l. 15: small marks over and after 'fran-'. l. 19: faint tick over the a of 'Imperatore'. l. 20: stray dot between 'loro' and 'tanta'. l. 25: 'seguìte' has a clear grave on the i (printed, not doubtful). l. 28: dot below 'pertanto'. l. 29: dot below 'dei'.
- p. 9 l. 14: stray mid-height dot after 'perchè'. l. 16: dot below 'ampliare'. l. 19: dot below 'in'. l. 22: apostrophe-like tick after 'chi'. l. 29: small comma-like mark after the line-end hyphen of 'Ma-'.
- p. 10: image skewed ~1.5 degrees. l. 11: stroke over the v of 'dove'. l. 17: reddish blot on the f of 'fusse' (letter clear). l. 28: dot below the n of 'consi-'. Right margin stray dots at ll. 10-11.
- p. 10 ll. 20-23 and p. 11 ll. 2-3: Latin quotations in italic (Livy; Juvenal). The comma after 'Capua' and after 'gula' and 'incubuit', and the final full stops, appear italic and are kept inside the italic span.
- p. 11: chapter ends l. 11; CAPITOLO XX follows on the same page.

# Uncertain loci

| # | page | line | locus | what you see | class |
|---|---|---|---|---|---|
| 1 | 5 | 9 | ⟨má\|ma⟩ vincerli | dark slanting acute-like stroke joined above the a; could be a damaged/foul sort or stray | mark-pointing |
| 2 | 6 | 4 | meglio⟨,\|;⟩ e che | comma with a small blob above it, positioned above x-height, unlike the semicolon dots elsewhere | mark-pointing |
| 3 | 6 | 11 | e ⟨così\|cósì⟩ questa | round dot over the o; i has normal grave | mark-pointing |
| 4 | 6 | 13 | ⟨e' si\|e'si⟩ vede | apostrophe-to-letter gap 11 px (borderline between tight 3-8 and spaced 13+) | mark-pointing |
| 5 | 6 | 19 | ⟨spererebbero\|spererèbbero⟩ | round dot over an e, not accent-shaped | mark-pointing |
| 6 | 7 | 17 | dello ⟨acquistare\|àcquistare⟩ | round dot above the initial a | mark-pointing |
| 7 | 7 | 29 | ⟨Cittadi\|Cittàdi⟩ più | short vertical tick above the a | mark-pointing |
| 8 | 8 | 9 | fu ⟨Filiburgo\|Filibúrgo⟩ | faint thin slanting stroke over the u | same word, other form |
| 9 | 8 | 11 | ⟨e' sieno\|e'sieno⟩ | apostrophe gap 11 px | mark-pointing |
| 10 | 8 | 12 | il giogo ⟨d' Austria\|d'Austria⟩ | apostrophe gap 11 px | mark-pointing |
| 11 | 8 | 19 | ⟨dell' \|dell'⟩Imperatore | apostrophe gap 11 px | mark-pointing |
| 12 | 8 | 19 | ⟨Imperatore\|Imperàtore⟩ | faint tick over the a | mark-pointing |
| 13 | 8 | 25 | Duca ⟨d' Austria\|d'Austria⟩ | apostrophe gap 10 px | mark-pointing |
| 14 | 9 | 22 | ⟨chi\|chi'⟩ acquista | apostrophe-like tick at top right of the i, then a word space | mark-pointing |
| 15 | 9 | 29 | del ⟨Ma-\|Ma-,⟩ | small comma-like mark just after the line-end hyphen | mark-pointing |
| 16 | 10 | 11 | ⟨dove\|dovè⟩ si può | stroke over the v (not over the e) | mark-pointing |
