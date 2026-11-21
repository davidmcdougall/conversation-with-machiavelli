---
unit: NM-DISC.2.13
reader: pass A (full chapter), cold reader nmA
source: "Machiavelli, Discorsi sopra la prima deca di Tito Livio, Italia [Firenze], 1824, Libro secondo, Capitolo XIII"
witness_images:
  - file: p260-page.png (2057x3228); crops p260-top (rows 0-1205), p260-middle (rows 946-2281), p260-bottom (rows 2022-3228)
    crop_check: each crop matched pixel-for-pixel (mean abs diff 0.000) to the stated region of the full page; names correct
  - file: p261-page.png (2057x3228); crops top 0-1205, middle 946-2281, bottom 2022-3228
    crop_check: same; exact match, names correct
  - file: p262-page.png (2057x3228); crops top 0-1205, middle 946-2281, bottom 2022-3228
    crop_check: same; exact match, names correct
  - file: p263-page.png (2057x3228); crops top 0-1205, middle 946-2281, bottom 2022-3228
    crop_check: same; exact match, names correct. p263 contains only Capitolo XIV text (no part of this unit); top crop read to confirm
boundaries:
  preceded_by: "end of Capitolo XII on p260 lines 1-3: 'se la discosti sempre da casa il più che può. E / così l' uno e l' altro, ciascuno nel suo grado, si / difenderà meglio.'"
  heading: "CAPITOLO XIII (p260, centred, roman capitals)"
  rubric: "Che si viene di bassa a gran fortuna più con la / fraude, che con la forza. (p260, italic, two lines, second centred)"
  first_words: "Io stimo essere cosa verissima (p260; enlarged initial I)"
  last_words: "è più coperta, come fu questa de'Romani. (p262, body line 19)"
  final_stop_visible: true
  followed_by: "CAPITOLO XIV (p262), rubric 'Ingannansi molte volte gli uomini, credendo / con la umiltà vincere la superbia.', text beginning 'Vedesi molte volte come la umiltà non sola-' (enlarged initial V); XIV continues through p263"
headings_printed: "Running heads (not transcribed): p260 '260 DISCORSI'; p261 'LIBRO SECONDO 261'; p262 '262 DISCORSI'; p263 'LIBRO SECONDO 263'. No signatures seen on these pages."
paragraphing: "One paragraph only. It opens on p260 with an enlarged (two-line-high, dropped into first line) initial 'I'. All other lines on p260-p262 begin flush at the left text margin (checked against the margin; p262 body line 9 'E che sia vero' is flush, with only a stray mark in the margin to its left). No notes on any page. Italic: the rubric (p260), and the Latin quotation p262 body lines 12-14 'Nam si / ctiam nunc sub umbra foederis aequi servitutem / pati possumus, etc.' ('etiam' at p262 l.15 is roman)."
body_word_count: 605
words_per_page: {p260: 188, p261: 259, p262: 158, p263: 0}
word_count_method: "Python over my own draft body (heading and rubric excluded; page markers excluded): uncertain loci replaced by the preferred reading; italic asterisks removed; apostrophes treated as word separators (so d' infima, tutt'i, de'Romani each = 2 words regardless of printed spacing); split on whitespace; tokens with no letter/digit discarded; a word hyphenated at line end (incl. across pages: mo-/stra, timo-/re) counted once, on the page where it starts (the first token of the following line is subtracted)."
uncertain_loci_per_page: {p260: 0, p261: 2, p262: 4, p263: 0}
uncertain_loci_total: 6
conventions: "Line numbers in the loci table count lines of this chapter's body on that page (p260 l.1 = 'Io stimo...'). Spacing after apostrophes is recorded as seen (some elisions printed with a thin space, some without). Broken letters transcribed silently where the word is unambiguous (e.g. p260 l.5 'per' with damaged e; p261 l.20 'riputazione' with damaged r). The comma after 'l' armi' (p261 l.27) sits low and to the right but is certainly a comma."
---

# Heading

CAPITOLO XIII

# Rubric

*Che si viene di bassa a gran fortuna più con la*
*fraude, che con la forza.*

# Body

[p. 260]
Io stimo essere cosa verissima che rado o non
mai intervenga, che gli uomini di piccola fortuna
vengano a gradi grandi, senza la forza e senza la
fraude, purchè quel grado, al quale altri è per-
venuto, non ti sia o donato o lasciato per eredi-
tà. Nè credo si trovi mai che la forza sola basti,
ma si troverà bene che la fraude sola basterà; co-
me chiaro vedrà colui che leggerà la vita di Filippo
di Macedonia, quella di Agatocle siciliano, e di
molti altri simili, che d' infima ovvero di bassa
fortuna sono pervenuti o a Regno o ad Imperj
grandissimi. Mostra Senofonte nella sua vita di
Ciro questa necessità dello ingannare, considerato
che la prima ispedizione che fa fare a Ciro contro
il Re di Armenia è piena di fraude, e come con
inganno e non con forza gli fa occupare il suo
Regno. E non conchiude altro per tale azione, se
non che ad un Principe che voglia fare gran cose,
è necessario imparare a ingannare. Fagli oltra di
questo ingannare Ciassare Re dei Medi, suo zio
materno, in più modi, senza la quale fraude mo-
[p. 261]
stra che Ciro non poteva pervenire a quella gran-
dezza che venne. Nè credo che si trovi mai alcuno
constituito in bassa fortuna, pervenuto a grande
Imperio solo con la forza aperta e ingenuamente,
ma sì bene solo con la fraude, come fece Giovanni
Galeazzo per tor lo Stato e lo Imperio di Lom-
bardia a messer Bernabò suo zio. E quel che sono
necessitati fare i Principi ne'principj degli augu-
menti loro, sono ancora necessitate a fare le Re-
pubbliche, infino che le sieno diventate potenti,
e che basti la forza sola. E perchè Roma tenne
in ogni parte, o per sorte o per elezione, tutt'i
modi necessarj a venire a grandezza, non mancò
ancora di questo. Nè potè usare nel principio il
maggior inganno, che pigliare il modo di sopra
discorso da noi, di farsi compagni; perchè sotto
questo nome se gli fece servi, come furono i La-
tini, ed altri Popoli all' intorno. Perchè prima si
valse dell' armi loro in domare i Popoli convici-
ni, e pigliare la riputazione dello Stato; dipoi do-
matili, venne in tanto augumento, che la poteva
battere ciascuno. Ed i Latini non si avvidero mai
di essere al tutto servi, se non poi che videro dare
due rotte ai Sanniti, e costrettili ad accordo. La
qual vittoria, come ella accrebbe gran riputazione
ai Romani con i Principi longinqui, che mediante
quella sentirono il nome romano e non l' armi,
così generò invidia e sospetto in quelli che vede-
vano e sentivano l' armi, intra i quali furono i⟨∅|.⟩
Latini. E tanto potè questa invidia ⟨e|è⟩ questo timo-
[p. 262]
re, che non solo i Latini, ma le colonie che essi
avevano in Lazio, insieme con i ⟨Campani|Camp ani⟩ stati
innanzi difesi, congiurarono contro al ⟨nome|n ome⟩ ro-
mano. E mossero questa guerra i Latini nel modo
che si dice di sopra che si muovono la maggior
parte delle guerre, assaltando non i Romani, ma
difendendo i Sidicini contro ai Sanniti, a' quali i
Sanniti facevano guerra con licenza de' ⟨Romani|Ro mani⟩.
E che sia vero che i Latini si movessero per avere
conosciuto questo inganno, lo dimostra Tito Livio
nella bocca di Annio Setino Pretore latino, il quale
nel Consiglio loro disse queste parole: *Nam si
⟨ctiam|etiam⟩ nunc sub umbra foederis aequi servitutem
pati possumus, etc.* Vedesi pertanto i Romani nei
primi augumenti loro non essere mancati etiam
della fraude; la quale fu sempre necessaria ad usare
a coloro che di piccoli principj vogliono a sublimi
gradi salire, la quale è meno vituperevole quanto
è più coperta, come fu questa de'Romani.

# Uncertain loci

| # | page | line | locus | what you see | class |
|---|------|------|-------|--------------|-------|
| 1 | 261 | 29 | furono i⟨∅\|.⟩ | a small round dot well to the right of the final 'i', outside the justified measure, at x-height baseline; almost certainly a speck, but sits where a stop could be | mark-pointing |
| 2 | 261 | 30 | invidia ⟨e\|è⟩ questo | 'e' with a round dot (not a slanted grave stroke like the accents elsewhere) above it; read as speck over 'e', but 'è' is possible | different word |
| 3 | 262 | 2 | ⟨Campani\|Camp ani⟩ | visible gap between 'p' and 'a' within the word; read as loose type spacing, not a word division | non-word |
| 4 | 262 | 3 | ⟨nome\|n ome⟩ | visible gap after 'n' in 'nome'; read as loose spacing | non-word |
| 5 | 262 | 8 | de' ⟨Romani\|Ro mani⟩. | visible gap between 'Ro' and 'mani'; read as loose spacing | non-word |
| 6 | 262 | 13 | *⟨ctiam\|etiam⟩* | first italic letter shows no eye/crossbar at 5x enlargement and matches the 'c' of 'nunc'; printed form is 'ctiam' (possibly a damaged or wrong 'e') | non-word |
