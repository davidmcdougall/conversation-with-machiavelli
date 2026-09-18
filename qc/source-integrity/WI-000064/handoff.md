# WI-000064 handoff

Status: `complete`. No canonical source or witness was modified.

Review the fixed manifest, deterministic script, metrics, intervention log, results, and three SOURCE findings in this directory. Reproduction requires the pinned Archive.org DjVu XML named in `sample-manifest.yml`:

```text
python3 qc/source-integrity/WI-000064/run_stress.py \
  /path/to/operecompletedi01machgoog_djvu.xml \
  --output /tmp/WI-000064-metrics.json
cmp /tmp/WI-000064-metrics.json qc/source-integrity/WI-000064/metrics.json
```

Review routing under `ROUTING.md`:

- `[OPUS]`: reproduce the metrics; confirm the fixed input, denominator, same-setting restraint, date-style statement, voice/attachment classification, and lack of canonical changes.
- `[OPUS-2X]`: image-derived fixture readings must use two independent cold passes. Each task must include the repository's verbatim transcribe-first instruction.
- `[THIRD-FAMILY]`: only load-bearing date/hour/signature readings and the fixed 10% PASS sample; batch them into the cycle inspection sheet.
- `[DAVID]`: resolve any disagreement or UNRESOLVED reading and authorize any merge.

Nothing in this item supports S2. The independent-witness acquisition belongs to WI-000057.

The formerly outstanding live-input reproduction was completed on 2026-07-19. The fresh download matched the pinned input hash and produced metrics byte-identical to the committed file; see `independent-rerun-2026-07-19.md`. The input remains unvendored. This closes the reproducibility limitation but changes no measurement or source claim.
