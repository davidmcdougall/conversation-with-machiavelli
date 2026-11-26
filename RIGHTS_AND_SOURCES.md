# Rights and sources

Rights assessments for the third-party sources this edition uses. The
project's own licence grants are in `LICENSE`; translation method is in
`TRANSLATION_METHOD.md`. Per-unit records are in `sources/provenance/`.

This document is not legal advice and has not been reviewed by a lawyer
(DEC-011 point 6; §6). Each statement is marked as one of:

- **Fact** — verified from the source, its metadata, or the repository.
- **Interpretation** — a legal reading the project has adopted, not verified
  by counsel.
- **Policy** — a conservative editorial rule the project applies whatever the
  legal position.

Items marked **For legal review** were open when this document was written;
§6 records the assessment of each.

Moved from `LICENSE` §§5–6 (version 0.3, 2026-09-21) by DEC-011. Nothing in
those sections has been dropped; the corrections made in moving them are
listed in `CHANGELOG.md`.

---

## 1. Witnesses

| Witness | Source | Record |
|---|---|---|
| *Discorsi* (1824) | Internet Archive: `discorsisopralap01mach`, `discorsisopralap02mach` | `WIT-NM-DISC-1824-IA` |
| *Discorsi* (1554), Giglio, Venice | Internet Archive: `discorsidinicolo00mach` | `WIT-NM-DISC-1554-IA` |
| *Considerazioni*, Canestrini (1857) | Internet Archive: `bub_gb_F_YZsP2XjO8C` | `WIT-FG-CONS-1857-CANESTRINI` |
| *Considerazioni*, Palmarocchi (1933) | Wikimedia Commons: BEIC 1844634 | `WIT-FG-CONS-1933-PALMAROCCHI` |
| Machiavelli to Vettori, 10 December 1513, *Opere* (1813), vol. 8 | Internet Archive: `operediniccoloma08mach` | `WIT-NM-LETT-1813-IA` |

The fifth witness is not a text unit. It supplies the letter quoted for the
edition's title (SCOPE §1, D339).

Bounded page extracts and acquisition metadata are held under
`sources/witnesses/`. They are evidence, cited and located; they are not
redistributed as a corpus. The site publishes no page images (fact: `site/`
contains no image files other than fonts).

### *Discorsi*, 1824 — governing witness

- Source institution: University of Illinois Urbana-Champaign (contributor
  and sponsor in the Internet Archive metadata). **Fact.**
- Underlying work and edition: public domain by age. **Fact.**
- Archive statement: no copyright page found. **Fact.**
- Scan layer: recorded as `public_domain_historical_scan`;
  `corpus_reuse: reproducible_in_corpus`. **Interpretation.**

### *Discorsi*, 1554 (Giglio, Venice) — comparison witness

- Source institution: Boston Public Library (contributor); sponsor:
  Associates of the Boston Public Library / The Boston Foundation. **Fact.**
- Underlying work and edition: public domain by age. **Fact.**
- Scan layer: recorded as `public_domain_historical_scan`;
  `corpus_reuse: reproducible_in_corpus`. **Interpretation.**

### *Considerazioni*, Canestrini 1857 — governing witness

- Edition: *Opere inedite di Francesco Guicciardini*, vol. 1, ed. Giuseppe
  Canestrini (Florence: Barbera, Bianchi e Comp., 1857). The *editio
  princeps*. **Fact.**
- Source: a Google Books digitisation (`books.google.com` id `F_YZsP2XjO8C`,
  sponsor Google), in the Internet Archive collection `bncfirenze`; contributor
  given as "unknown library". **Fact.**
- Scan layer: Public Domain Mark 1.0 in the archive metadata. **Fact.**
- Underlying work and edition: public domain by age. **Fact.** Canestrini
  (1807–1870) died more than seventy years ago; his dates are taken from
  external authority records and are not recorded in the repository.
- `corpus_reuse: reproducible_in_corpus`. **Interpretation.**
- Google usage guidelines: the extracts carry Google's on-page
  "Digitized by Google" watermark and do not include the guidelines leaf
  (checked 2026-11-25, all 40 extracts). **Fact.** Assessed in §6 item 3.

### *Considerazioni*, Palmarocchi 1933 — comparison witness

- Edition: *Scritti politici e ricordi*, ed. Roberto Palmarocchi (Bari:
  Laterza, 1933). **Fact.**
- Source: Wikimedia Commons file "Guicciardini, Francesco – Scritti politici e
  ricordi, 1933 – BEIC 1844634.djvu". **Fact.**
- Commons designation: tagged public domain (`PD-old-100-expired`), with
  `Artist` = Francesco Guicciardini. The tag reasons from Guicciardini's death
  in 1540. It says nothing about the 1933 edition's own editorial layer.
  **Fact.**
- Underlying text: Guicciardini's, public domain. **Fact.**
- Palmarocchi: born Florence 1887, died 1956. **Fact** (Wikidata Q61481064;
  Università di Cagliari, Archivio Storico, "Palmarocchi Roberto"; COBISS
  heading "Palmarocchi, Roberto, 1887-1956"; the Library of Congress/NACO
  heading gives the birth year only).
- His edition has two layers, with different terms. **Interpretation.**
  - *His textual choices* (the edited text of a public-domain work):
    in Italy, a critical or scientific edition of a public-domain work
    attracts a related right of twenty years from first lawful publication
    (L. 633/1941, art. 85-*quater*, para. 3). For 1933 that ran to 1953, so
    nothing subsists now. The article was added to the law long after 1953,
    so the right may never have arisen for this edition at all. Either way,
    no right subsists today.
  - *His own prose* (the Nota, notes and any preface): an ordinary
    literary work, seventy years *post mortem auctoris*. It is protected in
    Italy until 31 December 2026 and enters the public domain there on
    **1 January 2027**. In the United States, as a work restored under the
    URAA, it is protected until 31 December 2028.
  The project copies neither layer's expression. It reports readings, which
  are facts about what the book prints.
- What the edition says about its readings: one autograph survives
  (Archivio Guicciardini, Carte di Francesco Guicciardini, Filza IX), and
  the 1933 text is edited from it. The bracketed Discorsi chapter titles are
  Palmarocchi's, from the Mazzoni–Casella *Discorsi*. His Nota names
  twenty-one Canestrini readings as errors against the autograph. **Fact**
  (Nota, pp. 339–342.) Per record:
  `sources/comparisons/FG-CONS/WIT-FG-CONS-1933-basis.yml`.
- Scan use: page images are consulted, not republished
  (`scan_layer: consultable_not_republishable`). The images are excluded from
  version control (`.gitignore`). No Palmarocchi page image is published by
  this project, and none will be before 2029. **Policy.**
- Readings are reported as collation evidence: statements of fact about what
  the book prints. Palmarocchi's editorial expression is never copied.
  **Policy.**

### Machiavelli to Vettori, *Opere* (1813), vol. 8

- Source institution: Getty Research Institute, as recorded in the
  provenance record (`contributing_library`). No archive metadata file is
  held for this witness. **Fact as recorded; not checked against the
  archive.**
- Underlying work and edition: public domain by age. **Fact.**
- Scan layer: recorded as `public_domain_historical_scan`;
  `corpus_reuse: reproducible_in_corpus`. **Interpretation.**

---

## 2. Faithful reproductions of public-domain works

Three layers are distinct for every witness:

1. **The underlying work** — the text of Machiavelli or Guicciardini, and the
   historical edition. Public domain by age for all five witnesses (fact),
   subject to the Palmarocchi editorial-layer question above.
2. **The reproduction** — the scan made by the digitising institution.
3. **Access conditions** — the terms of the platform or provider (Internet
   Archive, Google, Wikimedia Commons), which may be contractual rather than
   copyright.

Article 14 of Directive (EU) 2019/790 provides that material resulting from
an act of reproduction of a work of visual art whose term of protection has
expired is not subject to copyright or related rights, unless the
reproduction is itself original. `LICENSE` v0.3 recorded its Italian
transposition as art. 32-*quater* of law 633/1941. **Fact as to the
Directive's text.**

The project does not rely on Article 14. Whether it, or any other rule,
removes rights in a scan of a printed book depends on the jurisdiction and
the reproduction. **For legal review.**

---

## 3. Wikisource

The Italian Wikisource transcriptions of the 1824 *Discorsi* and of
Palmarocchi's *Scritti politici e ricordi* are licensed CC BY-SA 3.0 / GFDL.
**Fact.**

They were consulted for chapter boundaries, page correspondences and
collation readings, and are credited in provenance. Their wording is not
reproduced. **Policy (DEC-010 point 1).**

Distinctions:

- The historical text, and factual collation readings (what a page prints),
  are not the transcribers' expression. **Interpretation.**
- Choices specific to a modern transcription (for example its normalisation,
  punctuation, layout or corrections) may be protectable contributions.
  **Interpretation.**
- The established text in `corpus/` is transcribed from page images by two
  readers per unit, at least one of them a cold reader that has seen no other
  transcription (SCOPE §7; `sources/coldpass/`). Where it matches a Wikisource
  transcription word for word, that is expected: both reproduce the same
  historical wording. Identical historical wording does not by itself
  establish copying. **Interpretation.**

---

## 4. Modern editions and translations

- **Margaret Grayson**, "Considerations on the Discourses of Machiavelli", in
  *Francesco Guicciardini: Selected Writings*, ed. Cecil Grayson (Oxford
  University Press, 1965). In copyright. **Fact.**
- **James B. Atkinson and David Sices**, *The Sweetness of Power:
  Machiavelli's Discourses and Guicciardini's Considerations* (Northern
  Illinois University Press, 2002). In copyright. **Fact.**
- **Francesco Bausi** (ed.), *Discorsi sopra la prima deca di Tito Livio*
  (Rome: Salerno, 2001), the national edition of the *Discorsi*. In
  copyright. **Fact.** Treated exactly as Palmarocchi 1933 (DEC-013):
  consulted for readings, never copied. **Policy.**

Policy:

- The English is translated independently. Grayson and Atkinson & Sices are
  never translation inputs (AGENTS.md rule 3; SCOPE §1). **Policy.**
- Permitted subsequent comparison: either may be consulted privately, after a
  draft is finished, as a calibration check only (SCOPE §1). Cold reviewers
  are instructed not to look for either. No calibration comparison is
  recorded in the repository. **Fact.**
- No modern edition governs or supplies the established Italian. Readings of
  Palmarocchi 1933 and Bausi 2001 may be reported as facts, with a page
  reference, at loci where the edition emends or where its witnesses split.
  A reading is a fact about what a book prints; reporting one copies no
  expression (§6 item 1). Their editorial expression (apparatus, notes,
  introductions) is never copied (DEC-013). **Policy.**

The project does not assert that no wording in its English overlaps with
these translations. Two translations of the same short Italian sentence can
coincide.

---

## 5. Where these materials appear

- **Repository:** bounded scan extracts (PDF) of the 1824, 1554, Canestrini and
  1813 witnesses, and acquisition metadata (Internet Archive and Commons JSON)
  for all except the 1813 witness, under `sources/witnesses/`. Palmarocchi page images are held locally and
  excluded from version control. **Fact.**
- **No new extracts (DEC-013, review pass 2, 2026-11-25).** The extracts
  already held stay, since git history keeps them anyway. No further scan
  extract is added to the repository: a new witness or unit is cited by
  archive identifier and page, and linked. **Policy.**
- **Site:** no witness images. Each source note links to the page images
  at the Internet Archive (page-level URLs for the 1824 and Canestrini
  scans). Witness identifiers, page references and reported readings appear
  in source and variant notes. Third-party fonts
  (EB Garamond, IBM Plex; SIL Open Font License 1.1) are self-hosted in
  `site/fonts/` with their licence texts. **Fact.**
- **Not anywhere in the repository or on the site:** Wikisource wording;
  Palmarocchi's or Bausi's editorial expression (a reading reported as a fact
  at a locus is not expression, §4); any part of Grayson or Atkinson &
  Sices. **Policy.** Anything found that contradicts this is a defect:
  report it and it will be removed.

---

## 6. Rights assessment

> **Awaiting a second reader (DEC-013, 2026-11-25).** This section was
> written by Claude and has not been checked by anyone else. Until a second
> reader has gone through it, treat it as a draft. Rely on it for the hosted
> scans and the reporting of readings, and for nothing beyond that. The
> second reader should record their name, date and findings here.

Release is not conditional on counsel review (DEC-011 point 6). The
questions below were assessed on 2026-11-24 by Claude (`claude-opus-5-5`) on
David McDougall's instruction. **This is an assessment, not advice from a
lawyer, and not legal approval.**

1. **Palmarocchi 1933. Closed as moot.** The project publishes no
   Palmarocchi page image and copies none of his expression; it reports
   readings, which are facts about what the book prints. On that practice
   there is no exposure, whatever the exact Italian and US terms and whichever
   components are protected. No republication of the images is planned. The
   question reopens only if republishing images or expression is proposed.
2. **Article 14 and art. 32-*quater*. Not pursued.** The project does not
   rely on either.
3. **Canestrini usage conditions. Closed 2026-11-25; extracts kept.**
   Google attaches usage guidelines to the PDFs it serves from Google Books.
   Earlier versions asked users to make non-commercial use of the files and
   keep the watermark; later versions ask them not to host the files or
   reprint them. **Fact** (contemporary reports: eWeek, 2006; Shaftek,
   2009). Assessment: these are requests attached to Google's own download,
   not a copyright in the 1857 text and not a term the project accepted. The
   scan was obtained from the Internet Archive, which marks it with the
   Public Domain Mark 1.0, and Google's guidelines leaf is not among the
   extracts. The project keeps the attribution Google asks for (the
   watermark is on every extracted page), makes no commercial use of the
   scans and grants no rights over them (`LICENSE`, `REUSE.toml`). Residual
   risk: the project hosts bounded page extracts, which the later guidelines
   ask users not to do. That is a request, not a legal bar; if Google or the
   Internet Archive asks for the extracts to be removed, they will be.
   Removing them now would not take them out of the public git history.
   **Interpretation.**
4. **Scan extracts in the public repository.** `sources/witnesses/` holds
   bounded PDF extracts of the 1824, 1554, Canestrini and 1813 scans, and the
   repository is public, so these are redistributed. Assessment: low risk.
   The works and editions are public domain by age; the reproductions are
   faithful scans of printed pages, which add no original expression; the
   archive metadata asserts no copyright (Public Domain Mark on Canestrini,
   no copyright page on the 1824 and 1554). Residual risk is contractual
   (platform terms), not copyright. The `reproducible_in_corpus` designations
   stand on that basis. Palmarocchi images stay excluded (item 1).
5. **The project's own grants.** In the United States, human authorship is
   required for copyright: the D.C. Circuit so held in *Thaler v. Perlmutter*
   (2025), and the Supreme Court denied review on 2 March 2026. Material
   generated by AI without sufficient human authorship is therefore likely
   unprotectable there, and other jurisdictions may differ. The licence
   already grants only rights that subsist and are held by the licensor, so
   this needs no change: unprotected material is free to use without
   attribution, and the CC BY condition applies to the rest. **Fact as to
   the decisions; interpretation as to their application here.**

   *United Kingdom.* UK law goes the other way. For a literary work that
   is computer-generated, with no human author, the author is taken to be
   "the person by whom the arrangements necessary for the creation of the
   work are undertaken" (Copyright, Designs and Patents Act 1988,
   s. 9(3)). Protection lasts fifty years from the end of the year the work
   was made (s. 12(7)). Any part of the English or the commentary that is
   computer-generated is therefore probably protected in the UK, with David
   McDougall as author, since he makes the arrangements. Whether such output
   meets the originality the courts now require is unsettled. On either
   view the CC BY grant covers it, so nothing in the licence changes.
   **Interpretation.**

   Status of reform, checked 2026-11-26. The government's *Report on
   Copyright and Artificial Intelligence* (18 March 2026), made under ss.
   135–136 of the Data (Use and Access) Act 2025 after the 2024–25
   consultation, proposed removing protection for computer-generated works
   under s. 9(3). It set no timetable and said it would keep the provision's
   use under review. In its 15 May 2026 response to the House of Lords
   Communications and Digital Committee, the government said it had no
   current plans to amend copyright legislation. Section 9(3) remains in
   force, and no amending bill has been introduced. **Fact** (gov.uk,
   "Report and impact assessment on copyright and artificial intelligence";
   UK Parliament, Communications and Digital Committee, 15 May 2026;
   practitioner summaries, March–November 2026). If s. 9(3) is repealed,
   the UK position moves towards the US one, and the licence still needs no
   change.

Nothing in this section has been reviewed by a lawyer.
