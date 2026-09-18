# WI-000064 — Diplomatic-material stress results

## Outcome

The fixed four-page sample is false-clean on every page. Archive.org OCR produces fluent-looking text throughout, but fails 17 of 19 high-risk feature checks (89.47%) and imports six structural contaminants. The sample has no independent-witness coverage because the Oliva and Passigli scans are issues of one typesetting.

## Load-bearing failures

- `Die 7 octobris, 1502` became `iHe 7 oclobrU, 1502`.
- `ore 16` became `ore 1G`.
- `Nicolaus Machiavellus, Imolae` became `Nicolacs Macbuveclus, ìmolae`.
- `Die 8 octobris, 1502` became `DU^octobtit, 1.S02`.
- `dì 9` became `d) 9`.
- The opening addressee formula and several names/words contain plausible glyph substitutions.

October does not require Florentine New Year conversion. The literal dates, the two-stage 7/8 October composition history, `ore 18`, `ore 16`, and arrival before dawn on the 9th nevertheless require explicit preservation. OCR cannot safely perform that preservation.

## Boundary and voice failures

The unsegmented OCR includes the preceding incoming commission, an editorial footnote, running heads/page numbers, a following separately numbered dispatch, and a second editorial footnote. The selected voice remains Machiavelli's first-person official report. Letters described inside the report are neither transcribed enclosures nor attachments.

## Cost and reproducibility

Contemporaneous intervention logging records 46 active minutes for four pages (11.5 minutes/page), excluding download wait. The pipeline asserts the pinned OCR hash and every observed fixture string. Two runs produced byte-identical `metrics.json`.

These are stress measurements only. They change no canonical reading and do not resolve the open commission-date disagreement.
