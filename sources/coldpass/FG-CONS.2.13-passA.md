---
unit: FG-CONS.2.13
reader: pass A (full)
source: "Francesco Guicciardini, Considerazioni intorno ai Discorsi del Machiavelli, in Opere inedite, vol. 1, ed. Giuseppe Canestrini, Firenze 1857, pp. 66-67"
witness_images:
  - file: p66-page.png
    size: 1367x2184
  - file: p66-top.png
    check: "verified by exact pixel comparison = p66-page rows 0-1178, full width (top of page)"
  - file: p66-bottom.png
    check: "verified by exact pixel comparison = p66-page rows 1004-2183, full width (bottom of page)"
  - file: p67-page.png
    size: 1367x2184
  - file: p67-top.png
    check: "verified by exact pixel comparison = p67-page rows 0-1178, full width (top of page)"
  - file: p67-bottom.png
    check: "verified by exact pixel comparison = p67-page rows 1004-2183, full width (bottom of page)"
  - note: "Crops are at the same pixel scale as the page images (1367 px wide), so they add no resolution; images are greyscale-antialiased, not strictly bitonal. Doubtful loci were enlarged (LANCZOS and NEAREST, 4-8x) into WORK."
boundaries:
  preceded_by: "Nothing: the unit begins at the top of p66, below the running head (CONSIDERAZIONI) and page number 66; no text of the preceding unit appears on these pages."
  heading: "CONSIDERAZIONE SUL CAPITOLO XIII (initial C's full capitals, rest small caps; L of CAPITOLO broken, prints like 'CAPITOI O'; no stop clearly visible after XIII)"
  rubric: "Che si viena di bassa a gran fortuna piu con la fraude. / che con la forza. (2 lines; 'viena' as printed; 'piu' without accent; stops after 'fraude' and 'forza' are faint traces only)"
  first_words: "Se lo Scrittore chiama fraude ogni astuzia"
  last_words: "toglie occasione di conseguire gli intenti suoi"
  final_stop_visible: "trace only: a faint grey mark on the baseline after 'suoi', not a clear full stop"
  followed_by: "p67, after a blank space: heading 'CONSIDERAZIONE SUL CAPITOLO XIV.' with rubric 'Ingannansi molte volte gli uomini, credendo con la umiltà / vincere la superbia', body beginning 'La conclusione del Discorso è in parte contraria a quello'"
headings_printed: "One heading for this unit (p66); the next unit's heading (Capitolo XIV) on p67. Running heads: p66 'CONSIDERAZIONI', p67 'SUI DISCORSI DEL MACHIAVELLI.' (both with broken letters), not transcribed."
paragraphing: "One paragraph. Indent only at p66 body line 1 ('Se lo Scrittore'); all other lines on p66 (2-20) and p67 (1-14) start flush at the left margin, measured from the page."
footnotes:
  - cue: "(1) after 'fraude.' at p66 body line 15 (start of line)"
    page: 66
    content: "Xenophon in the Cyropaedia shows Cyrus that deceit is a necessity and has him deceive his maternal uncle Cyaxares in several ways, proving Cyrus could not reach greatness without such frauds; and from Machiavelli's examples, among them Giovanni Galeazzo taking the state from his uncle Bernabò, it is clear he does not mean industry or lawful simulation."
  - cue: "(1) after 'luogo,' in the following unit (CONS. on cap. XIV), p67"
    page: 67
    content: "'Nel capitolo xxxiii del libro i' -- belongs to the next unit, not this one."
body_word_count: 317
words_per_page: {p66: 187, p67: 130}
word_count_method: "Python over WORK/body.txt: page markers set the page; for each line, ⟨a|b⟩ replaced by a (preferred), ∅ deleted, footnote cue '(1)' deleted; split on whitespace; tokens with no letter (e.g. a standalone ';') dropped; if the previous line ended in '-', the first token of the line is not counted (hyphenated word counted once, on the page/line where it starts). Elided forms separated by a printed space ('de' Romani', 'l' avere') count as two tokens; 'de'Ro-mani' (no space) counts as one. Heading and rubric excluded."
uncertain_loci_per_page: {p66: 20 (6 in heading/rubric + 14 in body), p67: 10}
uncertain_loci_total: 30
---

# Heading

CONSIDERAZIONE SUL CAPITOLO XIII⟨∅|.⟩

(small caps after initial capitals; L of CAPITOLO broken, prints like CAPITOI O)

# Rubric

Che si ⟨viena|viene⟩ di bassa a gran fortuna ⟨piu|più⟩ con la fraude⟨.|,⟩
che con la forza⟨.|∅⟩

# Body

[p. 66]
    Se lo Scrittore chiama fraude ogni astuzia o dissimu-
lazione che si usa ⟨eltam|etiam⟩  sanza dolo, può essere vera la
conclusione sua, che la forza sola, non dico mai, che è vo-
cabolo troppo resoluto, ma rarissime volte conduca gli uo-
mini da bassa a grande fortuna⟨.|∅⟩ Ma se chiama fraude
quella ⟨che|chc⟩ è proprio fraude, cioè il mancamento di fede, o
altro procedere doloso, credo si trovino molti ⟨cha|che⟩ hanno
sanza fraude acquistato ⟨ragni|regni⟩ e ⟨imperii|imperi⟩ grandissimi⟨∅|.⟩ Di
questi fu Alessandro Magno, di questi Cesare, che di cit-
tadino privato con altre arti che di fraude si condusse a
tanta grandezza, scoprendo sempre la ambizione ⟨sna|sua⟩ o lo
appetito del dominare. Non ho ora fresca la memoria di
Zenofonte, ma credo che ⟨instruisca|inatruisca⟩ Ciro di prudenza, d⟨∅|'⟩in-
dustria, di simulazione o dissimulazione giuste, non di
fraude.(1) Nè chiamo fraude se e Romani ⟨feciona|feciono⟩ tali patti
ai Latini ⟨cha|che⟩ potettono pazientemente tollerare lo imperio
loro, il che non fu perchè non si accorgessino insino dal
principio, che, sotto ombra di confederazione, equale era
⟨servitu|servitù⟩⟨,|;⟩ ma il trovarsi impotenti, nè essere trattati in modo
che non avessino causa di desperarsi, gli fece aspettare
[p. 67]
insino a ⟨tonto|tanto⟩, non dico che ebbono scoperto il fine de⟨'|∅⟩Ro-
mani, il quale sarebbono stati bene grossi se non avessino
⟨cognosciuto|cognnsciuto⟩ da principio, ma che cresciuti di numero di
uomini, e bene esperti di disciplina militare, ebbono spe-
ranza ⟨potera|potere⟩ contendere del pari col populo romano⟨.|∅⟩ Fu
anche prudenza quella de' Romani, non fraude, a trattare
bene e Latini ; e credo sia verissimo che sanza simili in-
dustrie e prudenti modi di governarsi non solo rarissime
volte si salga da bassa fortuna a alta, ma ancora difficil-
mente si conservi la grandezza. Ma, quanto alla fraude, ⟨può|pnò⟩
essere disputabile se sia sempre ⟨buono|bnono⟩ instrumento di⟨∅|.⟩ per-
venire alla grandezza ; perchè spesso con lo inganno si
fanno di molti belli tratti,  spesso anche l' avere nome di
fraudolenta ⟨toglie|toghe⟩ occasione di conseguire gli intenti suoi⟨.|∅⟩

# Uncertain loci

| # | page | line | locus | what you see | class |
|---|---|---|---|---|---|
| 1 | 66 | heading | CAPITOLO | L broken, reads 'CAPITOI O'; word unambiguous | non-word |
| 2 | 66 | heading | XIII⟨∅\|.⟩ | no clear stop after XIII; only faint grey | mark-pointing |
| 3 | 66 | rubric 1 | ⟨viena\|viene⟩ | final letter clearly a-shaped | different word |
| 4 | 66 | rubric 1 | ⟨piu\|più⟩ | no accent visible on u | mark-pointing |
| 5 | 66 | rubric 1 | fraude⟨.\|,⟩ | small faint grey mark at baseline after e | mark-pointing |
| 6 | 66 | rubric 2 | forza⟨.\|∅⟩ | faint grey trace at baseline after a | mark-pointing |
| 7 | 66 | 2 | ⟨eltam\|etiam⟩ | e + tall unbarred stroke + barred t + a + m; could be damaged 'ti' | non-word |
| 8 | 66 | 5 | fortuna⟨.\|∅⟩ | faint grey trace after a, before capital Ma | mark-pointing |
| 9 | 66 | 6 | ⟨che\|chc⟩ | final letter e/c, eye of e not closed | non-word |
| 10 | 66 | 7 | ⟨cha\|che⟩ | final letter clearly a-shaped ('molti cha hanno') | non-word |
| 11 | 66 | 8 | ⟨ragni\|regni⟩ | second letter a-shaped | different word |
| 12 | 66 | 8 | ⟨imperii\|imperi⟩ | two short strokes after r, m broken | different word |
| 13 | 66 | 8 | grandissimi⟨∅\|.⟩ | no stop seen before capital Di | mark-pointing |
| 14 | 66 | 11 | ⟨sna\|sua⟩ | middle letter n-shaped (arch on top) | non-word |
| 15 | 66 | 13 | ⟨instruisca\|inatruisca⟩ | s prints like a, t like l (s/a break) | non-word |
| 16 | 66 | 13 | d⟨∅\|'⟩in- | gap between d and in, no apostrophe visible | mark-pointing |
| 17 | 66 | 15 | ⟨feciona\|feciono⟩ | last letter a-shaped | non-word |
| 18 | 66 | 16 | ⟨cha\|che⟩ | last letter a-shaped ('Latini cha potettono') | non-word |
| 19 | 66 | 19 | ⟨servitu\|servitù⟩ | faint grey above/after u, no clear accent | mark-pointing |
| 20 | 66 | 19 | servitu⟨,\|;⟩ | comma clear; grey speck above it | mark-pointing |
| 21 | 67 | 1 | ⟨tonto\|tanto⟩ | second letter o-shaped | different word |
| 22 | 67 | 1 | de⟨'\|∅⟩Ro- | grey speck above-right of de, no space before Ro | mark-pointing |
| 23 | 67 | 3 | ⟨cognosciuto\|cognnsciuto⟩ | fifth letter n/o unclear | non-word |
| 24 | 67 | 5 | ⟨potera\|potere⟩ | final letter a-shaped | different word |
| 25 | 67 | 5 | romano⟨.\|∅⟩ | faint grey trace before capital Fu | mark-pointing |
| 26 | 67 | 10 | ⟨può\|pnò⟩ | u prints n-shaped; accent present | non-word |
| 27 | 67 | 11 | ⟨buono\|bnono⟩ | first u prints n-shaped | non-word |
| 28 | 67 | 11 | di⟨∅\|.⟩ | stray dot after 'di' before per- | mark-pointing |
| 29 | 67 | 14 | ⟨toglie\|toghe⟩ | 'li' fused, prints like h | non-word |
| 30 | 67 | 14 | suoi⟨.\|∅⟩ | final stop only a faint grey trace | mark-pointing |
