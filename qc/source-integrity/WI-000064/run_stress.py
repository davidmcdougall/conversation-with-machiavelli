#!/usr/bin/env python3
"""Reproduce the fixed WI-000064 OCR/structure stress measurements."""
from __future__ import annotations

import argparse
import hashlib
import json
import xml.etree.ElementTree as ET
from pathlib import Path

EXPECTED_HASH = "0b2988a3b2c70ba4e86f52508e31c04461b5976d2de024dba35f8a5231dd74f1"
PAGES = {275: 274, 276: 275, 277: 276, 278: 277}

# Reference readings were transcribed from the bounded page images. This is a
# stress fixture, not canonical text: failures measure whether OCR preserves
# diplomatic/date/entity evidence and document structure.
CHECKS = [
    (275, "Magnifici et Excelsi Domini", "Magnifici et Excetni Domini", "glyph_substitution", "opening_formula"),
    (275, "Domini mei singularissimi", "Domini mei singuiarissimi", "glyph_substitution", "opening_formula"),
    (275, "ore 18", "ore 18", "pass", "florentine_hour"),
    (275, "cavalchereccio", "cavalcliereccio", "glyph_substitution", "lexical"),
    (275, "aderenti", "adel*enti", "glyph_substitution", "lexical"),
    (276, "AL DUCA VALENTINO", "AL DUCA VALEKTrrCO", "glyph_substitution", "running_matter"),
    (276, "condiscendere", "conitesccndere", "glyph_substitution", "lexical"),
    (276, "Città", "Cittìi", "diacritic_error", "entity"),
    (276, "MACHIAVELLI. VOL. II. 17*", "HACBt AVELLI. VOL. 11. 17*", "glyph_substitution", "running_matter"),
    (277, "LEGAZIONE", "LCGAZIO!IE", "glyph_substitution", "running_matter"),
    (277, "Die 7 octobris, 1502", "iHe 7 oclobrU, 1502", "glyph_substitution", "date_formula"),
    (277, "E. V. D.", "E. V. D.", "pass", "abbreviation"),
    (277, "Nicolaus Machiavellus, Imolae", "Nicolacs Macbuveclus, ìmolae", "glyph_substitution", "signature_entity"),
    (277, "ore 16", "ore 1G", "glyph_substitution", "florentine_hour"),
    (278, "AL DUCA VALENTINO", "AL mCX VALEKTI50", "glyph_substitution", "running_matter"),
    (278, "Iterum", "Jlerum", "glyph_substitution", "latin_formula"),
    (278, "Die 8 octobris, 1502", "DU^octobtit, 1.S02", "glyph_substitution", "date_formula"),
    (278, "due ducati", "doe ducati", "glyph_substitution", "lexical"),
    (278, "dì 9", "d) 9", "punctuation_diacritic", "date_reference"),
]

STRUCTURE = [
    {"page": 275, "class": "preceding", "observed": "commission tail precedes dispatch I", "would_contaminate": True},
    {"page": 275, "class": "apparatus", "observed": "editorial footnote follows body line", "would_contaminate": True},
    {"page": 276, "class": "running", "observed": "running head and signature mark enter OCR", "would_contaminate": True},
    {"page": 277, "class": "running", "observed": "running head and page number enter OCR", "would_contaminate": True},
    {"page": 278, "class": "following", "observed": "dispatch II follows selected dispatch", "would_contaminate": True},
    {"page": 278, "class": "apparatus", "observed": "editorial Agapito footnote enters OCR", "would_contaminate": True},
]

def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("ocr_xml", type=Path)
    ap.add_argument("--output", type=Path, default=Path("metrics.json"))
    args = ap.parse_args()
    actual_hash = sha256(args.ocr_xml)
    if actual_hash != EXPECTED_HASH:
        raise SystemExit(f"OCR hash mismatch: {actual_hash}")

    objects = ET.parse(args.ocr_xml).getroot().findall(".//OBJECT")
    page_text = {}
    for pdf_page, object_index in PAGES.items():
        lines = []
        for line in objects[object_index].findall(".//LINE"):
            text = " ".join((w.text or "").strip() for w in line.findall(".//WORD")).strip()
            if text:
                lines.append(text)
        page_text[pdf_page] = "\n".join(lines)

    results = []
    for page, reference, observed, category, evidence_class in CHECKS:
        if observed not in page_text[page]:
            raise SystemExit(f"fixture observation missing on PDF page {page}: {observed}")
        results.append({
            "pdf_page": page,
            "reference": reference,
            "observed_ocr": observed,
            "category": category,
            "evidence_class": evidence_class,
            "pass": category == "pass",
        })

    failures = [r for r in results if not r["pass"]]
    by_category = {}
    by_evidence = {}
    for result in failures:
        by_category[result["category"]] = by_category.get(result["category"], 0) + 1
        by_evidence[result["evidence_class"]] = by_evidence.get(result["evidence_class"], 0) + 1
    failed_pages = sorted({r["pdf_page"] for r in failures})
    output = {
        "work_item": "WI-000064",
        "unit_id": "NM-LEG-BORG.1502-10-07",
        "input_ocr_sha256": actual_hash,
        "sample_pages": sorted(PAGES),
        "feature_checks": len(results),
        "feature_failures": len(failures),
        "feature_disagreement_rate": round(len(failures) / len(results), 6),
        "false_clean_pages": len(failed_pages),
        "pages_with_ocr": len(PAGES),
        "false_clean_page_rate": round(len(failed_pages) / len(PAGES), 6),
        "failure_taxonomy": by_category,
        "evidence_risk_taxonomy": by_evidence,
        "structural_contamination_events": len(STRUCTURE),
        "structural_events": STRUCTURE,
        "checks": results,
        "date_style": {
            "florentine_new_year_conversion_required": False,
            "reason": "October dates are unaffected by Florentine New Year conversion",
            "literal_dates": ["Die 7 octobris, 1502", "Die 8 octobris, 1502"],
            "clock_evidence": ["ore 18", "ore 16", "arrival before dawn on dì 9"],
            "ocr_failures": ["Die 7 octobris, 1502", "ore 16", "Die 8 octobris, 1502", "dì 9"],
        },
        "attachment_voice": {
            "selected_voice": "Machiavelli first-person official report",
            "attachments": 0,
            "reported_letters_are_not_attachments": True,
            "boundary_failure": "unsegmented OCR continues into separately numbered dispatch II",
        },
        "independence": {
            "passigli_relation": "same_typesetting_distinct_issue",
            "independent_witness_coverage": 0,
            "s2_support": False,
        },
    }
    args.output.write_text(json.dumps(output, ensure_ascii=False, indent=2, sort_keys=True) + "\n")

if __name__ == "__main__":
    main()
