# Changelog

The edition is versioned, not frozen. The version is set in `SCOPE.md` and
shown on every page; each page also carries its own published and revised
dates. Per-unit text versions are in each unit's front matter.

## 0.3 — 2026

Released as `v0.3.0`: 38 of 39 pairs published (76 of 78 units). III.24 is
not yet established.

### Published

- September 2026: I.1, I.2, I.3, I.4, I.12, I.14. Site launched on GitHub
  Pages, 2026-09-26.
- October 2026: I.5–I.11, I.16, I.23–I.26, I.28–I.30, I.32, I.39, I.40, I.47.
- November 2026: I.49, I.58, I.60, II.proem, II.10, II.12–II.15, II.19,
  II.24, III.17, III.19.

### Licensing and attribution (DEC-011, 2026-11-24)

- Component licensing: CC0 for the Italian text and research data, CC BY 4.0
  for the translation and editorial apparatus (where rights subsist), MIT for
  scripts.
- The English is credited as "AI-assisted translation edited by David
  McDougall"; the model used for each drafting and review step is recorded.
- Rights assessments moved from `LICENSE` to `RIGHTS_AND_SOURCES.md`.

### Licensing restructured (2026-11-25)

- Per-file licensing in `REUSE.toml`, checked in CI; licence texts in
  `LICENSES/`; `LICENSE` reduced to a summary (v0.4).
- "Apparatus data" renamed "research and provenance data", so that
  "apparatus" means only the CC BY editorial apparatus. No file changed
  licence by this.
- `SCOPE.md` is wholly CC0; §1 was CC BY.

### Rights

- 2026-11-25: the Canestrini usage question (`RIGHTS_AND_SOURCES.md` §6
  item 3) is closed: Google's download guidelines are requests, not a
  copyright or an accepted term; the witness extracts stay in the
  repository, with their watermark.

### Corrections

Made to the rights statements of `LICENSE` v0.3 (2026-09-21) when they moved
to `RIGHTS_AND_SOURCES.md`:

- Canestrini's death was given as 1891; the authority records give 1870. The
  conclusion (public domain by age) is unchanged.
- The Italian and US expiry dates for Palmarocchi's 1933 editorial
  contributions were stated as settled. They are now an assessment, with the
  question of which components are protected flagged.
- `LICENSE` stated that a faithful reproduction of a public-domain work
  "attracts no new copyright or related right" under Article 14 of Directive
  (EU) 2019/790. That was broader than the provision, and is withdrawn. The
  project does not rely on Article 14.

### Site

- 2026-11-25: 36 pages built before later pairs were added showed an
  out-of-date count of pairs published; all pages rebuilt. Building one pair
  now refreshes every page, and CI rejects a site that differs from a fresh
  build.
- 2026-11-25: pages link one shared stylesheet instead of carrying it inline
  (about a fifth smaller); the content-only duplicates of every page (Claude
  artifact input) are no longer published; `404.html`, `sitemap.xml` and
  `robots.txt` added.
- 2026-11-25: the translation decision log moved from `decisions.md` to
  `apparatus/decision-log.md`, so it no longer sits beside `decisions/` (the
  DEC records) under a near-identical name and a different licence. D-numbers
  are unchanged. References were updated everywhere except the historical
  records (`decisions/`, `PORT-NOTES.md`); the move does not redate any pair.
- 2026-11-25: CI also checks that every internal link and anchor on the site
  resolves (`scripts/checklinks`), and that the README's status line,
  citation and `CITATION.cff` agree with `SCOPE.md`.
- 2026-11-25: the whole published text is available as data, Italian and
  English aligned by paragraph: `data/edition.json` and `data/paragraphs.csv`,
  linked from the About page.
- 2026-11-25: `SCOPE.md` §5 (effort estimates and per-pair actuals) and §6
  (port manifest) moved to `docs/effort.md` and `docs/port-manifest.md`.
  They are logs, not doctrine; the section numbers stay, as pointers, so
  every "SCOPE §N" reference still resolves.
- 2026-11-25: every page carries a link-preview image (`og.png`), so shared
  links show the edition's title card rather than bare text.
- 2026-11-25: `SCOPE.md` §4's narrative was out of date (it said one pair was
  published and the witness scans were not held). It now states only current
  facts; the September history moved verbatim to `docs/history.md`.
