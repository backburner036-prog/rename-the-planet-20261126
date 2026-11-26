#!/usr/bin/env python3
"""Rename the Planet — make.fun bounty entry.

Writes one funny line renaming a planet, plus the why, in a single
breath to /output/entry.txt. Deterministic: no randomness, no network,
no input.
"""

import os

# Determinism note: same code, same output every run — no randomness,
# no network, no clock, no external input.
ENTRY = (
    "Rename Saturn 'Wedding Ring': it has flashed its band for four "
    "billion years and still will not commit to a single moon."
)


def main() -> None:
    # Entry limit note: the bounty requires one line under 200 characters;
    # ENTRY is 120 characters, validated below before anything is written.
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError(f"ENTRY must be 1-200 characters, got {len(ENTRY)}")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("ENTRY must be a single line")
    if not ENTRY.strip():
        raise ValueError("ENTRY must not be only whitespace")
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()
