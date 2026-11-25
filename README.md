# A Conversation with Machiavelli

**Guicciardini's *Considerazioni* on the *Discorsi*** — a free, bilingual,
hyperlinked edition of Francesco Guicciardini's 39 responses to Machiavelli's
*Discorsi* and the chapters they answer: 78 text units, Italian and English
facing, every reading traceable to a named public-domain witness.

**Read it:** https://davidmcdougall.github.io/conversation-with-machiavelli/

<!-- state:status -->
Version 0.3 · 38 of 39 pairs published. The edition is versioned, not
frozen; every page is dated. Per-pair progress is the table in `SCOPE.md` §2.
<!-- /state:status -->

## What is where

| Path | Contents |
|---|---|
| `corpus/` | The established Italian, one file per unit |
| `translations/` | The English, one file per unit, with translator's notes |
| `annotations/` | Variant, source and commentary notes |
| `apparatus/` | Glossary, register, names, Latin, open problems, and the translation decision log (`decision-log.md`, D-numbers) |
| `decisions/` | Project decision records (DEC-numbers) |
| `sources/` | Witness extracts, cold passes, collations, provenance |
| `links/` | Which *Considerazione* answers which *Discorsi* chapter |
| `site/` | The published website — build output, never edited by hand |
| `site/data/` | The whole published text as data: `edition.json`, `paragraphs.csv` |
| `scripts/` | `build.py`, `state`, `validate`, `checklinks` |

Method and policy: `SCOPE.md` (the project's doctrine),
`TRANSLATION_METHOD.md`, `RIGHTS_AND_SOURCES.md`.

## Witnesses

The Italian is established from page images of historical editions — the
*Discorsi* of 1824 (governing) and 1554, and the *Considerazioni* as first
printed by Canestrini in 1857 (governing), collated against Palmarocchi 1933 —
each transcribed by two independent readers. No modern critical edition or
translation is used. Details in `RIGHTS_AND_SOURCES.md`.

## Licence

| Component | Licence |
|---|---|
| Established Italian text; research and provenance data; documentation | CC0 1.0 |
| English translation; editorial commentary and apparatus | CC BY 4.0, where rights subsist |
| Scripts | MIT |
| Fonts | SIL OFL 1.1 |
| Witness scans | Not licensed by this project |

The English is an AI-assisted translation edited by David McDougall; models
are recorded per step (`TRANSLATION_METHOD.md`). Summary in `LICENSE`; file by file in `REUSE.toml`; licence texts in
`LICENSES/`.

## Citing

<!-- state:cite -->
> *A Conversation with Machiavelli: Guicciardini's Considerazioni on the
> Discorsi*. Ed. David McDougall; AI-assisted English translation edited by
> David McDougall. Version 0.3.
> https://davidmcdougall.github.io/conversation-with-machiavelli/
<!-- /state:cite -->

## Data

Every published paragraph, Italian and English aligned, with its governing
witness, is in [`edition.json`](https://davidmcdougall.github.io/conversation-with-machiavelli/data/edition.json)
(by pair and unit) and [`paragraphs.csv`](https://davidmcdougall.github.io/conversation-with-machiavelli/data/paragraphs.csv)
(one row per paragraph), regenerated with every build. The Italian is CC0; the
English is CC BY 4.0.

## Corrections

Errors in the Italian or the English are the most useful thing to report. See
`CONTRIBUTING.md`. To check a change locally:

```
pip install -r requirements.txt
scripts/validate && scripts/state --check
python3 scripts/build.py --all && scripts/checklinks
```
