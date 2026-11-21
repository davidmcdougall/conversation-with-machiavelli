---
unit: FG-CONS.2.13
reader: pass B (full), cold reader
source: Francesco Guicciardini, Considerazioni intorno ai Discorsi del Machiavelli, in Opere inedite, vol. 1, ed. Giuseppe Canestrini, Firenze 1857, pp. 66-67
witness_images:
  - file: p66-page.png
    size: 1367x2184
    check: full page 66 (running head "66  CONSIDERAZIONI")
  - file: p66-top.png
    size: 1367x1179
    check: pixel-identical to p66-page rows 0-1178 (verified by image difference = none at offset y=0); top of p. 66
  - file: p66-bottom.png
    size: 1367x1180
    check: pixel-identical to p66-page rows 1004-2183 (offset y=1004); bottom of p. 66; overlap with top = rows 1004-1178
  - file: p67-page.png
    size: 1367x2184
    check: full page 67 (running head "SUI DISCORSI DEL MACHIAVELLI.  67")
  - file: p67-top.png
    size: 1367x1179
    check: pixel-identical to p67-page rows 0-1178 (offset y=0); top of p. 67
  - file: p67-bottom.png
    size: 1367x1180
    check: pixel-identical to p67-page rows 1004-2183 (offset y=1004); bottom of p. 67
  - note: all crops are what their names say. Reading done from per-line 3x enlargements and 4-8x spot enlargements made into WORK from the page images (identical pixels to the crops).
boundaries:
  preceded_by: nothing on these pages; the heading of this unit is the first matter on p. 66 below the running head (any preceding unit ends on an earlier page, not supplied)
  heading: "CONSIDERAZIONE SUL CAPITOLO XIII." (caps and small caps: C, C capitals; rest small caps; L of CAPITOLO broken so it prints like "CAPITOI O"; final stop faint)
  rubric: "Che si viena di bassa a gran fortuna piu con la fraude. / che con la forza." (two centred lines, smaller type; "viena" with a; "piu" without accent; stop after "fraude" faint, possibly comma; stop after "forza" a faint smear)
  first_words: "Se lo Scrittore chiama fraude ogni astuzia"
  last_words: "conseguire gli intenti suoi"
  final_stop_visible: "faint only: a grey smear at baseline after 'suoi', no solid dot; preferred '.'"
  followed_by: "on p. 67, after a blank space: heading 'CONSIDERAZIONE SUL CAPITOLO XIV.' and rubric 'Ingannansi molte volte gli uomini, credendo con la umiltà / vincere la superbia' (end of rubric broken), then 'La conclusione del Discorso è in parte contraria a quello ...' (unit 2.14, not transcribed)"
headings_printed: "one heading for this unit (Considerazione sul Capitolo XIII.) plus its two-line rubric; the next unit's heading (XIV) on p. 67 line after body"
paragraphing: "a single paragraph. Only indent is p. 66 body line 1 ('Se lo Scrittore'): left edge at x=361 px against x=301-303 for p. 66 lines 2-20; p. 67 lines 1-14 all start at x=125-129 (flush). No further indents."
footnotes:
  - cue: "(1) on p. 66, body line 15, after 'fraude.' (before 'Nè chiamo')"
    note: "editor's note at foot of p. 66 (7 lines): Senofonte in the Ciropedia shows Ciro that deceit is a necessity, has him deceive his maternal uncle Ciassare, proof that Ciro could not reach greatness without such frauds; and from Machiavelli's examples, among them Giovanni Galeazzo taking the state from his uncle Bernabò, it is plain he does not mean industry or lawful simulation."
  - other: "p. 67 footnote '(1) Nel capitolo xxxiii del libro i.' belongs to unit 2.14 (cue in its line 2), not to this unit"
body_word_count: 319
words_per_page: {p66: 188, p67: 131}
word_count_method: "Python (WORK/count.py) over the Body section of this file: preferred reading kept in each ⟨a|b⟩ (∅ dropped), [p. N] markers and footnote cue (1) removed; line-end hyphenated halves joined into one word counted on the page where it starts; apostrophe elisions (d'in-dustria, de' Ro-mani, l'avere) split on apostrophe into separate words; tokens = whitespace-separated strings containing at least one letter (standalone ';' not counted)."
uncertain_loci_per_page: {p66: 25 (6 in heading/rubric + 19 in body), p67: 14}
uncertain_loci_total: 39
---

# Heading

CONSIDERAZIONE SUL ⟨CAPITOLO|CAPITOI O⟩ XIII⟨.|∅⟩

(C of CONSIDERAZIONE and C of CAPITOLO full capitals, rest small caps.)

# Rubric

Che si ⟨viena|viene⟩ di bassa a gran fortuna ⟨piu|più⟩ con la fraude⟨.|,⟩
che con la forza⟨.|∅⟩

# Body

[p. 66]
Se lo Scrittore chiama fraude ogni astuzia o ⟨dissimu-|diasimu-⟩
lazione che si usa ⟨etiam|eltam⟩ sanza dolo, può ⟨essere|esaere⟩ vera la
conclusione sua, che la forza sola, non dico mai, che è vo-
cabolo troppo resoluto, ma rarissime volte conduca gli uo-
mini da ⟨bassa|baasa⟩ a grande fortuna⟨.|∅⟩ Ma ⟨se|ae⟩ chiama fraude
quella che è proprio fraude, cioè il mancamento di fede, o
altro procedere doloso, credo si trovino molti ⟨cha|che⟩ hanno
sanza fraude acquistato ⟨ragni|regni⟩ e imperii grandissimi⟨∅|.⟩ Di
questi fu Alessandro Magno, di questi Cesare, che di cit-
tadino privato con altre arti che di fraude ⟨si|ai⟩ condusse a
tanta grandezza, scoprendo sempre la ambizione ⟨sua|sna⟩ o lo
appetito del dominare. Non ho ora fresca la memoria di
Zenofonte, ma credo che ⟨instruisca|inatruisca⟩ Ciro di prudenza, d⟨'|∅⟩in-
dustria, di ⟨simulazione|aimulazione⟩ o ⟨dissimulazione|diasimulazione⟩ giuste, non di
fraude.(1) Nè chiamo fraude se e Romani ⟨feciona|feciono⟩ tali patti
ai Latini ⟨cha|che⟩ potettono pazientemente tollerare lo imperio
loro, il che non fu perchè non si accorgessino insino dal
principio, che, sotto ombra di confederazione, equale era
servit⟨u|ù⟩⟨,|;⟩ ma il trovarsi impotenti, nè essere trattati in modo
che non avessino causa di desperarsi, gli fece aspettare
[p. 67]
insino a ⟨tonto|tanto⟩, non dico che ebbono scoperto il fine de⟨'|∅⟩ Ro-
mani, il quale sarebbono stati bene grossi se non avessino
⟨cognosciuto|cognusciuto⟩ da principio, ma che cresciuti di numero di
uomini, e bene esperti di disciplina militare, ebbono spe-
ranza ⟨potera|potere⟩ contendere del pari col populo romano⟨.|∅⟩ Fu
anche prudenza quella de' Romani, non fraude, a trattare
bene e Latini ; e credo sia verissimo che sanza simili ⟨in-|ín-⟩
dustrie e prudenti modi di governarsi non solo rarissime
volte si salga da ⟨bassa|baasa⟩ fortuna a alta, ma ancora difficil-
mente si conservi la grandezza. Ma, quanto alla fraude, ⟨può|pnò⟩
essere disputabile se ⟨sia|aia⟩ sempre ⟨buono|bnono⟩ ⟨instrumento|inatrumento⟩ di per-
venire alla grandezza ; perchè spesso con lo inganno si
fanno di molti belli tratti, spesso anche l'avere nome di
⟨fraudolenta|fraudolento⟩ ⟨toglie|toghe⟩ occasione di conseguire gli intenti suoi⟨.|∅⟩

# Uncertain loci

| # | page | line | locus | what you see | class |
|---|---|---|---|---|---|
| 1 | 66 | heading | ⟨CAPITOLO\|CAPITOI O⟩ | L of CAPITOLO broken: lower bar missing, a gap before O, so it reads "CAPITOI O" | non-word |
| 2 | 66 | heading | XIII⟨.\|∅⟩ | only a faint grey speck at baseline after XIII | mark-pointing |
| 3 | 66 | rubric 1 | ⟨viena\|viene⟩ | final letter has the a bowl clearly; e is possible only with breakage | different word |
| 4 | 66 | rubric 1 | ⟨piu\|più⟩ | no accent visible on u | mark-pointing |
| 5 | 66 | rubric 1 | fraude⟨.\|,⟩ | small grey mark on baseline after "fraude"; no tail visible, but faint | mark-pointing |
| 6 | 66 | rubric 2 | forza⟨.\|∅⟩ | grey smear mid-height after "forza", no solid dot | mark-pointing |
| 7 | 66 | 1 | ⟨dissimu-\|diasimu-⟩ | second s partly filled, reads like a | non-word |
| 8 | 66 | 2 | ⟨etiam\|eltam⟩ | glyphs read e-l-t-a-m: second stroke tall without crossbar, third has crossbar; same word on p. 67 (unit 2.14) prints clearly e-t-i-a-m | non-word |
| 9 | 66 | 2 | ⟨essere\|esaere⟩ | third letter filled, between s and a | non-word |
| 10 | 66 | 5 | ⟨bassa\|baasa⟩ | third letter looks like a | non-word |
| 11 | 66 | 5 | fortuna⟨.\|∅⟩ | faint grey dash at baseline only | mark-pointing |
| 12 | 66 | 5 | ⟨se\|ae⟩ | first letter filled, s/a doubtful | different word |
| 13 | 66 | 7 | ⟨cha\|che⟩ | final letter has an a-bowl | non-word |
| 14 | 66 | 8 | ⟨ragni\|regni⟩ | second letter looks like a | different word |
| 15 | 66 | 8 | grandissimi⟨∅\|.⟩ | no stop visible before capital "Di"; only a space | mark-pointing |
| 16 | 66 | 10 | ⟨si\|ai⟩ | first letter grey/filled, reads like a | different word |
| 17 | 66 | 11 | ⟨sua\|sna⟩ | middle letter looks like n (u/n) | non-word |
| 18 | 66 | 13 | ⟨instruisca\|inatruisca⟩ | third letter filled, s/a | non-word |
| 19 | 66 | 13 | d⟨'\|∅⟩in- | gap between d and in, no apostrophe visible | mark-pointing |
| 20 | 66 | 14 | ⟨simulazione\|aimulazione⟩ | first letter filled, s/a; i undotted | non-word |
| 21 | 66 | 14 | ⟨dissimulazione\|diasimulazione⟩ | second s reads like a | non-word |
| 22 | 66 | 15 | ⟨feciona\|feciono⟩ | final letter has an a-bowl | non-word |
| 23 | 66 | 16 | ⟨cha\|che⟩ | final letter has an a-bowl | non-word |
| 24 | 66 | 19 | servit⟨u\|ù⟩ | faint grey speck above, no clear grave | mark-pointing |
| 25 | 66 | 19 | servitu⟨,\|;⟩ | comma clear; faint grey speck above it at x-height | mark-pointing |
| 26 | 67 | 1 | ⟨tonto\|tanto⟩ | second letter a clean o | different word |
| 27 | 67 | 1 | de⟨'\|∅⟩ Ro- | faint grey mark high after "de" | mark-pointing |
| 28 | 67 | 3 | ⟨cognosciuto\|cognusciuto⟩ | fifth letter between o and n/u | different word |
| 29 | 67 | 5 | ⟨potera\|potere⟩ | final letter looks a, partly filled | different word |
| 30 | 67 | 5 | romano⟨.\|∅⟩ | faint grey trace only, before capital "Fu" | mark-pointing |
| 31 | 67 | 7 | ⟨in-\|ín-⟩ | dot of i misshapen, slanting like an acute | mark-pointing |
| 32 | 67 | 9 | ⟨bassa\|baasa⟩ | third letter reads like a | non-word |
| 33 | 67 | 10 | ⟨può\|pnò⟩ | second letter looks like n | non-word |
| 34 | 67 | 11 | ⟨sia\|aia⟩ | first letter filled grey, reads like a | different word |
| 35 | 67 | 11 | ⟨buono\|bnono⟩ | second letter looks like n | non-word |
| 36 | 67 | 11 | ⟨instrumento\|inatrumento⟩ | third letter filled, reads like a | non-word |
| 37 | 67 | 14 | ⟨fraudolenta\|fraudolento⟩ | final letter looks a | different word |
| 38 | 67 | 14 | ⟨toglie\|toghe⟩ | prints like "toghe": l and i fused into an h-shape (same fusion as "gli" in this line, which also looks like "gh") | non-word |
| 39 | 67 | 14 | suoi⟨.\|∅⟩ | grey smear at baseline after "suoi", no solid dot | mark-pointing |
