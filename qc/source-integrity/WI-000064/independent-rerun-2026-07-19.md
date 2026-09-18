# WI-000064 pinned-input independent rerun

Date: 2026-07-19
Agent: Codex production rerun
Result: PASS, byte-identical

The pinned public Archive.org input was freshly downloaded from:

`https://archive.org/download/operecompletedi01machgoog/operecompletedi01machgoog_djvu.xml`

The downloaded file was retained only in `/tmp` and was not vendored. Its SHA-256 was:

`0b2988a3b2c70ba4e86f52508e31c04461b5976d2de024dba35f8a5231dd74f1`

This exactly matches `EXPECTED_HASH` in `run_stress.py` and the pin in the sample manifest. The deterministic command completed successfully:

```text
python3 qc/source-integrity/WI-000064/run_stress.py \
  /tmp/WI-000064-rerun/operecompletedi01machgoog_djvu.xml \
  --output /tmp/WI-000064-rerun/metrics.json
```

`cmp` reported no difference between the rerun and committed `metrics.json`. Both output files have SHA-256:

`65cacf4aece8e842d40f443aed2e20d9e48ad3cc18ce39785918d91fcf5aa933`

This discharges the previously recorded limitation that the live pinned XML had not been independently rerun. It does not alter the fixed sample, reference readings, metrics, canonical text, witness record, integrity class, or S2 assessment.
