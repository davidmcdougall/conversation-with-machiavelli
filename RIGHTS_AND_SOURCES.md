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
those sections has been dropped; corrections are noted where made.

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

*Correction:* `LICENSE` §5 (v0.3) gave Canestrini's death as 1891. The
authority records give 1870. The conclusion is unchanged.
- `corpus_reuse: reproducible_in_corpus`. **Interpretation.**
- **For legal review:** Google-digitised volumes commonly carry usage
  guidelines. The repository does not record whether this scan does, or what
  they say. Any such guidelines would be source-provider conditions, distinct
  from copyright.

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
- Palmarocchi's editorial contributions: the existing assessment is that
  Palmarocchi died in 1956, and that qualifying original contributions (for
  example preface, notes, apparatus) may remain protected — in Italy, on the
  ordinary seventy-years-*post-mortem* term, until 31 December 2026; in the
  United States, as a work restored under the URAA, until 31 December 2028.
  **Interpretation.** These dates do not settle the status of every
  component of the edition: which components are original contributions, and
  whether any other right applies to the edited text, is not established.
  **For legal review.**
- Scan use: page images are consulted, not republished
  (`scan_layer: consultable_not_republishable`). The images are excluded from
  version control (`.gitignore`). No Palmarocchi page image is published by
  this project, and none will be before 2029. **Policy.**
- Readings are reported as collation evidence: statements of fact about what
  the book prints. Palmarocchi's editorial expression is never copied.
  **Policy.**

*Correction:* `LICENSE` §5 (v0.3) stated the Italian and US expiry dates as
settled. They are restated here as an assessment, with the component question
flagged.

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

*Correction:* `LICENSE` §5 (v0.3) stated that a faithful reproduction of a
public-domain work "attracts no new copyright or related right" under art.
14. That statement was broader than the provision. It is withdrawn.

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
- **Bausi 2001**, the modern critical edition of the *Discorsi*. Not used.
  **Policy.**

Policy:

- The English is translated independently. Grayson and Atkinson & Sices are
  never translation inputs (AGENTS.md rule 3; SCOPE §1). **Policy.**
- Permitted subsequent comparison: either may be consulted privately, after a
  draft is finished, as a calibration check only (SCOPE §1). Cold reviewers
  are instructed not to look for either. No calibration comparison is
  recorded in the repository. **Fact.**
- No modern critical edition, including Bausi 2001, is used to establish the
  Italian. **Policy.**

The project does not assert that no wording in its English overlaps with
these translations. Two translations of the same short Italian sentence can
coincide.

---

## 5. Where these materials appear

- **Repository:** bounded scan extracts (PDF) of the 1824, 1554, Canestrini and
  1813 witnesses, and acquisition metadata (Internet Archive and Commons JSON)
  for all except the 1813 witness, under `sources/witnesses/`. Palmarocchi page images are held locally and
  excluded from version control. **Fact.**
- **Site:** no witness images. Witness identifiers, page references and
  reported readings appear in source and variant notes. Third-party fonts
  (EB Garamond, IBM Plex; SIL Open Font License 1.1) are self-hosted in
  `site/fonts/` with their licence texts. **Fact.**
- **Not anywhere in the repository or on the site:** Wikisource wording;
  Palmarocchi's editorial expression; any part of Grayson, Atkinson & Sices,
  or Bausi 2001. **Policy.** Anything found that contradicts this is a defect:
  report it and it will be removed.

---

## 6. Rights assessment

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
3. **Canestrini usage conditions. Deferred** by David McDougall, to be
   reviewed later. Any Google usage guidelines would be a request or a
   contract term attached to the download, not a copyright in the 1857 text.
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

Nothing in this section has been reviewed by a lawyer.
