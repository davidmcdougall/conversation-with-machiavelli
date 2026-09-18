Three scripts, none of them written yet.

- `validate` — the four checks in SCOPE §7, run on every commit, silent when
  clean. Written from scratch, around 150 lines. The predecessor's 1,155-line
  validator was not ported; see SCOPE §6.
- `state` — walks `corpus/`, `translations/` and `sources/`, emits the SCOPE §2
  table from unit front-matter. The only derived view in the project.
- `build` — generates `site/`.
