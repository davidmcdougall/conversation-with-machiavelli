---
report: comparison collation backfill, NM-DISC.1.1–1.4 against the 1554 Giglio
units: [NM-DISC.1.1, NM-DISC.1.2, NM-DISC.1.3, NM-DISC.1.4]
comparison_reads: [NM-DISC.1.1-1554, NM-DISC.1.2-1554, NM-DISC.1.3-1554, NM-DISC.1.4-1554 (four subagents, Giglio 1554 page images only, one directory each)]
performed: 2026-10-06
rule: SCOPE §3 stage 3, §7
method: difflib.SequenceMatcher over word tokens after spelling normalisation on both sides (u/v, j, h, -ti-/-zi-, doubled consonants, accents, `&`/`et`/`ed`); every reading cited in a variant record checked on the page image by the collator
disposition: no reading adopted from Giglio; 1824 text unchanged in all four units; 18 variant records, four systematic classes
---

# NM I.1–I.4 against the 1554 Giglio

## Why this is a backfill

The four chapters were established and published (2026-09-27 to 09-29)
with `comparison_collation: pending`, because the Giglio extracts held at
the time were mis-cut: the I.1 and I.2 extracts did not contain their
chapters, and the I.3 and I.4 extracts were chapter VII (see the I.1–I.4
establishment records). The extracts were re-cut on 2026-10-01 and I.5
onward were collated at establishment. I.1–I.4 were never gone back to,
while the site's source note for every *Discorsi* chapter said "Collated
against the 1554 Giglio printing". That claim is now true for these four.

## Reads

Each re-cut extract was rendered at 400 ppi and cut into overlapping
thirds, in its own directory. Four cold readers, one per chapter, were
dispatched in parallel; each read only its directory, found its own
boundaries, and returned only path, boundaries, counts and the number of
uncertain loci.

| Unit | Giglio leaves | Boundaries found | Body words | Uncertain |
|---|---|---|---|---|
| NM-DISC.1.1 | fol. 2r–4r (A2–A4) | after the Book I proem; ends `si terminera.`, ch. II rubric follows | 1,309 | 10 |
| NM-DISC.1.2 | fol. 4r–7v | ends `largamente si dimostrera.`, ch. III rubric follows | 1,900 | 20 |
| NM-DISC.1.3 | fol. 7v–8r | ends `de nobili.` in a cul-de-lampe; ch. IIII rubric on the next page | 387 | 4 |
| NM-DISC.1.4 | fol. 8v–9v | ends `si mostrera.`, ch. V rubric follows | 612 | 6 |

All four readers place the boundaries where the 1824 places them. Body
counts agree with the 1824 within 1% in each chapter.

## Collation

Giglio's text is the same argument as the 1824 in each chapter, with a
steady layer of synonyms, reorderings and period verb forms (`-ino`,
`-ono`). That layer is recorded once per unit as a systematic class, as for
I.5–I.9 (D123). Variant records are kept for readings that bear on sense or
on the English; each was checked by the collator on the page image.

- **I.1** — .03 Giglio has no `o da loro medesimi`: the scattered
  inhabitants gather only when moved by someone of authority among them.
  .06 `impotenti ad ogni uirtuoso esercito`: `esercito` (army) is most
  likely a misprint for `esercitio`, which the same page prints a few lines
  on. Plus `datori di legge`, `natio`/`habitatione`, `abondanza`.
- **I.2** — .05 `alla lussuria` for `alla usurpazione delle donne`, and
  `thesori` for `sontuosità`. .06 `per opera d'alcun buono` for `per
  suggestione d'alcuno buono uomo`; `spenti che furono coloro`. .07
  `la licentia di ciascuna` for `la licenza dell'universale`.
- **I.3** — no `essere` in `presupporre tutti gli huomini cattiui`;
  `padre della uerita`; `di basso grado` for `infimo`; singular `fa`.
- **I.4** — .05 `Et della creatione de i Tribuni, meritano somma laude`:
  no conditional `se i tumulti furono cagione`. .04 `sfoghi` for `possa
  sfogare`, `dannosi` for `perniziosi`. .05 `ordinati` for `constituiti`.

False alarms cleared on the page: `CCC.` in I.4 is three hundred (the
normaliser had collapsed it); I.2's `non pero si discostarono` has its
negative; I.4's second `oppressi` is understood, not lost.

None of the reader's uncertain loci falls on a cited reading. The
uncertain loci are left in the transcripts as read.

## What changes

Nothing in the established Italian or the English. No Giglio reading makes
sense where the 1824 fails, so D68 (emend from the comparison
witness where the governing one is in error) does not engage; D38 stands. The four units gain `comparison_collation` pointers and a Variants
section on the site.
