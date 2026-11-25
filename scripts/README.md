Four scripts.

- `build.py` — generates `site/` from `corpus/`, `translations/`,
  `annotations/` and `sources/`. `build.py <pair>` reports on that pair and
  refreshes every other page; `--all` rebuilds everything. Every build ends
  by running `state --write`.
- `state` — walks `corpus/`, `translations/`, `annotations/`, `sources/` and
  `site/`, and writes the SCOPE §2 pairs table and the §4 stage table from the
  files, between their `<!-- state:... -->` markers, and the status line and
  citation in README.md; `--check` also fails if CITATION.cff's version is not
  SCOPE's. The only derived view in the project. `state` prints them; `state --write` rewrites SCOPE.md;
  `state --check` exits 1 if SCOPE.md is stale.
- `validate` — the four checks in SCOPE §7, run before every commit, silent
  when clean (exit 1 and one line per problem otherwise). `validate` checks
  every unit in `corpus/`; `validate 1.16` one pair. (1) each unit names a
  governing witness that exists under `sources/witnesses/`, holds the unit's
  page extract, and matches its establishment record; (2) decision numbers,
  record ids, `(Machiavelli .03)`, `[[ID]]`, note lemmas and record locators
  all resolve; (3) each *Considerazioni* unit responds to the *Discorsi* unit
  the pairing map gives it; (4) every word of the Italian occurs in a cold pass
  of the governing witness named in `established_from`, and every bracketed
  editorial reading is in the unit's establishment or collation record.
  Written from scratch, 2026-10-11; the predecessor's 1,155-line validator was
  not ported (SCOPE §6).
- `checklinks` — every internal link and `#anchor` in `site/` resolves to a
  file and an id that exist. External links are not fetched. Silent when
  clean; run in CI after the build.
