---
report: dual cold pass, pair I.6
units: [NM-DISC.1.6, FG-CONS.1.6]
passes: [A (drafting session), B (subagent, page images only, separate directory per unit)]
comparison_reads: [NM-DISC.1.6-1554 (subagent, Giglio 1554 page images only, separate directory)]
performed: 2026-10-02
rule: SCOPE §7
method: difflib.SequenceMatcher over word and punctuation tokens, case-sensitive, after DEC-009 Class A on both sides
disposition: NM clean; FG one word split escalated and ruled (D127), one agreed reading emended (D126); pointing resolved by D67, D110 and D40
---

# Pair I.6 — pass A against pass B

All three cold readers were dispatched before pass A was made, each with a
directory holding only its page images, and returned only boundaries, counts
and paths. The 1824 pages went at native 350 ppi with top/middle/bottom
crops; the Canestrini pages at native 600 ppi, a 2x upscale, and half-page
crops at 3x; the Giglio leaves at 500 ppi with thirds.

## NM-DISC.1.6 — 1824, pp. 33–39

1,641 words. **No word, clause or sense disagreement.** One spelling
difference: p. 39 `beneficio` (A) / `benefizio` (B). Checked on the page:
`benefizio` is printed, and pass A had slipped. Both passes find the same
boundaries (CAPITOLO VI at the top of p. 33; `si discorrerà.` at p. 39 l. 21;
CAPITOLO VII opens p. 40), the same three-line rubric, one printed block with
a drop capital, no notes. Both read `e di tanto numero` on p. 34 as printed,
where the sense wants the negative carried on (`non sono stati molti, e di
tanto numero che vi sia disproporzione`); the 1554 edition prints `et di
tanto` too, so it is the witnesses' reading, construes with the negation
carried, and stands (D38). Both pass over a stray point before `potette`
(p. 35) and an accent-like mark over `che` (p. 34).

## FG-CONS.1.6 — Canestrini, pp. 16–18

408 words. **One word split, escalated.**

| Locus | Pass A | Pass B | 1933 | Disposition |
|---|---|---|---|---|
| .01 `a' beni occupati, ___ degli onori non si curava` | `e` (barless e) | `⟨o\|e⟩` (the shape is o) | `e` | **D127**, David 2026-10-02: `e`, a reading. The printed letter is round and closed; `o` does not construe. |

**One agreed reading emended.** p. 17 `sanza conciare interamente il governo
alla plebe`: both readers read `conciare`, and it is clearly printed (checked
at 8x). The 1933 edition prints `communicare`. `Conciare` barely construes;
`cōicare`, the abbreviation of *comunicare*, read as `conciare` is a
compositor's slip; and the same reply has `comunicati gli onori` and `il
governo fu comunicato` six lines earlier. **D126**, David 2026-10-02: emended
`[comunicare]` under D68, in Canestrini's spelling; his `conciare` and the
1933 `communicare` go in the variant note.

`defetti` (p. 18): pass A `defetti`, pass B `difetti`. Checked on the page:
`defetti` is printed; the 1933 edition prints it too. Same word; not a
reading.

**Pointing.**

| Locus | Pass A | Pass B | 1933 | Disposition |
|---|---|---|---|---|
| .01 `tutta la autorità Ma dico` | none | none | `autorità.` | C001, D67 |
| .01 `la plebe ⟨,\|;⟩ o, come` | `,` | `⟨;\|,⟩` | `plebe;` | C002, D110: both see a spaced mark; neither can weigh it; the 1933 edition breaks the tie |
| .01 `non si curava ⟨,\|;⟩ se non che` | `,` | `⟨;\|,⟩` | `curava;` | C003, D110 |
| .01 `più presto dannoso che utile` (unit end) | none | none | `utile.` | Not supplied (D40: the period is left as the author's witness leaves it) |

Class A (accents; the plural article at `e' Romani`, `e' patrizii` ×2, `e'
quali` ×3, `e' plebei` ×2, `e' tribuni`, D35; the apostrophe dropped at `de'
debiti`, `a' patrizii`, `a' più ricchi`, `a' beni`, `a' Romani`, D39, with
`a' debiti` printed in the same period; elision spacing) applied by rule and
not enumerated.

## Comparison witnesses

Witness independence (SCOPE §7): at the one word split pass A sides with the
1933 edition and pass B with neither; at the two pointing splits pass B
leans to the 1933 semicolon and pass A does not. One locus each way, both on
damaged type. No pattern.

**FG, 1933 edition.** Readings that differ in word from Canestrini, for the
variant notes: `communicare` (the emendation, D126); `si vedde per
esperienzia` (Canestrini `si vede per esperienza`); `sarebbono stati tra
loro` (`sarebbero`); and a comma after `communicato`, with a semicolon after
`Gracchi`, where Canestrini runs `fu comunicato insino al tempo de' Gracchi,
ne' quali`. Everything else is Palmarocchi's orthographic profile (`el`,
`patrizi`, `possessione`, `inequale`, `legge`, `adunche`, `sedizione`,
`omori`, `ed` before vowels and consonants alike, `'l`) and his heavier
pointing, and is not enumerated.

**NM, 1554 Giglio.** A third reader transcribed fol. 11r–14r cold
(`NM-DISC.1.6-1554.md`); the transcript was collated by word against the
established 1824 text, spelling normalised (u/v, h, -ti-/-zi-, doubled
consonants, `&`). Every reading cited below was checked on the page image by
the collator. As in I.5, Giglio is the same argument in other words; the
differences that bear on the English:

- .01 `contese` for `controversie` (×2).
- .04 `forza, & accrescimento` for `forza ed augumento` — the word D69 keeps
  apart from `augumentare`.
- .04 `eglino fecero` for `E loro fecero`; `non lo puoi poi maneggiare` for
  `dopo`.
- .05 `con danari, & con astutia` for `con danari e con industria`.
- .05 `fusse il modo` (no `miglior`).
- .06 `ordine, o legge` for `constituzione o legge`; `ti astringe la
  necessita` for `t'induce la necessità`; `rouinar con piu prestezza` for
  `rovinare più presto`; no `pure` in `quando ... la necessità`.
- .07 `si deurebbe tollerarle` for `tollerarle`; `l'auttorita de Tribuni` for
  `l'autorità tribunizia`.
- .02 `et di tanto numero`: the 1554 edition agrees with the 1824 `e`.
