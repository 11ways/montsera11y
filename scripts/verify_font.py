#!/usr/bin/env python3
"""
Verify that Montsera11y fonts have been correctly renamed.

Usage:
    python3 scripts/verify_font.py output/ttf/

Checks all TTF files in the given directory for:
- No remaining "Montserrat" references (should be "Montsera11y")
- Correct copyright with derivative notice
- Correct version string
- Key name IDs are present and correct
"""

import sys
import os
import glob
from fontTools.ttLib import TTFont

OLD_FAMILY = "Montserrat"
NEW_FAMILY = "Montsera11y"
EXPECTED_VERSION = "Version 1.000"

# Name ID labels for readable output
NAME_ID_LABELS = {
    0: "Copyright",
    1: "Font Family",
    2: "Font Subfamily",
    3: "Unique ID",
    4: "Full Name",
    5: "Version",
    6: "PostScript Name",
    7: "Trademark",
    8: "Manufacturer",
    9: "Designer",
    11: "URL Vendor",
    12: "URL Designer",
    13: "License Description",
    14: "License URL",
    16: "Typographic Family",
    17: "Typographic Subfamily",
    25: "Variations PS Name Prefix",
}


def verify_font(font_path):
    """Verify a single font file. Returns (warnings, errors)."""
    font = TTFont(font_path)
    name_table = font["name"]
    warnings = []
    errors = []

    basename = os.path.basename(font_path)

    # Check that filename uses new name
    if OLD_FAMILY in basename:
        errors.append(f"Filename still contains '{OLD_FAMILY}': {basename}")

    for record in name_table.names:
        text = record.toUnicode()
        label = NAME_ID_LABELS.get(record.nameID, f"nameID={record.nameID}")

        # Check for remaining old family name (except in copyright/license
        # where the original project name is expected)
        if record.nameID not in (0, 13) and OLD_FAMILY in text:
            errors.append(f"{label}: still contains '{OLD_FAMILY}' -> \"{text}\"")

        # Check copyright includes derivative notice
        if record.nameID == 0:
            if "Eleven Ways" not in text:
                errors.append(f"{label}: missing Eleven Ways derivative copyright")
            if "Montsera11y" not in text:
                errors.append(f"{label}: missing Montsera11y in copyright")

        # Check version
        if record.nameID == 5:
            if text != EXPECTED_VERSION:
                warnings.append(f"{label}: expected '{EXPECTED_VERSION}', got '{text}'")

        # Check key name IDs contain new family name
        if record.nameID in (1, 4, 6, 25):
            if NEW_FAMILY not in text:
                errors.append(f"{label}: missing '{NEW_FAMILY}' -> \"{text}\"")

    # Check head table version
    head_version = font["head"].fontRevision
    if abs(head_version - 1.0) > 0.01:
        warnings.append(f"head.fontRevision: expected 1.0, got {head_version}")

    font.close()
    return warnings, errors


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <font_dir>")
        sys.exit(1)

    font_dir = sys.argv[1]
    ttf_files = sorted(glob.glob(os.path.join(font_dir, "*.ttf")))

    if not ttf_files:
        print(f"No TTF files found in {font_dir}")
        sys.exit(1)

    total_errors = 0
    total_warnings = 0

    for ttf_file in ttf_files:
        basename = os.path.basename(ttf_file)
        warnings, errors = verify_font(ttf_file)

        if errors or warnings:
            print(f"\n{'='*60}")
            print(f"  {basename}")
            print(f"{'='*60}")
            for e in errors:
                print(f"  ERROR: {e}")
            for w in warnings:
                print(f"  WARN:  {w}")
            total_errors += len(errors)
            total_warnings += len(warnings)
        else:
            print(f"  OK: {basename}")

    print(f"\n{'='*60}")
    print(f"  Summary: {len(ttf_files)} fonts checked")
    print(f"  Errors:   {total_errors}")
    print(f"  Warnings: {total_warnings}")
    print(f"{'='*60}")

    if total_errors > 0:
        print("\nVerification FAILED — fix errors above before publishing.")
        sys.exit(1)
    else:
        print("\nVerification PASSED!")
        sys.exit(0)


if __name__ == "__main__":
    main()
