#!/usr/bin/env python3
"""
Rename Montserrat fonts to Montsera11y and generate WOFF2.

Usage:
    python3 scripts/rename_font.py working/ output/

Reads edited TTF files from the input directory, renames all
name table entries from "Montserrat" to "Montsera11y", updates
the version, and writes TTF + WOFF2 to the output directory.
"""

import sys
import os
import glob
from fontTools.ttLib import TTFont

OLD_FAMILY = "Montserrat"
NEW_FAMILY = "Montsera11y"
NEW_VERSION = "Version 1.000"
DERIVATIVE_COPYRIGHT = (
    "Copyright 2011 The Montserrat Project Authors "
    "(https://github.com/JulietaUla/Montserrat)\n"
    "Copyright 2026 Eleven Ways (Montsera11y modifications)"
)

# Name IDs that may contain the family name and need renaming
RENAME_NAME_IDS = {1, 3, 4, 6, 16, 25}
# High name IDs used in fvar/STAT instance names (256+)
HIGH_NAME_ID_START = 256


def rename_font(input_path, output_dir):
    """Process a single font file: rename + generate TTF and WOFF2."""
    font = TTFont(input_path)
    basename = os.path.basename(input_path)
    new_basename = basename.replace(OLD_FAMILY, NEW_FAMILY)

    ttf_dir = os.path.join(output_dir, "ttf")
    woff2_dir = os.path.join(output_dir, "woff2")
    os.makedirs(ttf_dir, exist_ok=True)
    os.makedirs(woff2_dir, exist_ok=True)

    name_table = font["name"]

    for record in name_table.names:
        text = record.toUnicode()

        # Update copyright (nameID 0)
        if record.nameID == 0:
            record.string = DERIVATIVE_COPYRIGHT
            continue

        # Update version (nameID 5)
        if record.nameID == 5:
            record.string = NEW_VERSION
            continue

        # Rename family name in key name IDs
        if record.nameID in RENAME_NAME_IDS:
            record.string = text.replace(OLD_FAMILY, NEW_FAMILY)
            continue

        # Also rename in high name IDs (fvar/STAT instance names like
        # "Montserrat-Regular", "Montserrat-Bold", etc.)
        if record.nameID >= HIGH_NAME_ID_START and OLD_FAMILY in text:
            record.string = text.replace(OLD_FAMILY, NEW_FAMILY)

    # Update the unique ID in nameID 3 to use new vendor tag
    for record in name_table.names:
        if record.nameID == 3:
            text = record.toUnicode()
            # Replace version prefix and vendor tag
            # Original: "9.000;ULA;Montserrat-Regular"
            # New:      "1.000;11W;Montsera11y-Regular"
            text = text.replace("9.000;ULA;", "1.000;11W;")
            record.string = text

    # Update head table version
    font["head"].fontRevision = 1.0

    # Save TTF
    ttf_path = os.path.join(ttf_dir, new_basename)
    font.save(ttf_path)
    print(f"  TTF  -> {ttf_path}")

    # Save WOFF2
    font.flavor = "woff2"
    woff2_path = os.path.join(woff2_dir, new_basename.replace(".ttf", ".woff2"))
    font.save(woff2_path)
    print(f"  WOFF2 -> {woff2_path}")

    font.close()


def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <input_dir> <output_dir>")
        sys.exit(1)

    input_dir = sys.argv[1]
    output_dir = sys.argv[2]

    ttf_files = sorted(glob.glob(os.path.join(input_dir, "*.ttf")))
    if not ttf_files:
        print(f"No TTF files found in {input_dir}")
        sys.exit(1)

    print(f"Processing {len(ttf_files)} font files...\n")

    for ttf_file in ttf_files:
        print(f"Processing: {os.path.basename(ttf_file)}")
        rename_font(ttf_file, output_dir)
        print()

    print("Done! All fonts renamed and converted.")


if __name__ == "__main__":
    main()
