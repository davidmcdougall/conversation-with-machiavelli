Three scripts. Two are written.

- `build.py` — generates `site/` from `corpus/`, `translations/`,
  `annotations/` and `sources/`. Every build ends by running `state --write`.
- `state` — walks `corpus/`, `translations/`, `annotations/`, `sources/` and
  `site/`, and writes the SCOPE §2 pairs table and the §4 stage table from the
  files, between their `<!-- state:... -->` markers. The only derived view in
  the project. `state` prints them; `state --write` rewrites SCOPE.md;
  `state --check` exits 1 if SCOPE.md is stale.
- `validate` — not written. The four checks in SCOPE §7, run on every commit,
  silent when clean. Written from scratch, around 150 lines. The predecessor's
  1,155-line validator was not ported; see SCOPE §6.
