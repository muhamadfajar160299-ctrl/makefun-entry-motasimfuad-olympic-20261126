#!/usr/bin/env python3
"""Rejected Olympic Sports - one-liner entry.

Writes the single entry line to entry.txt (next to this file) and, when
the grader's /output directory exists, to /output/entry.txt as well.
Deterministic: the same bytes on every run, no trailing newline.
"""

import os

ENTRY = (
    "Synchronized Napping: four athletes nap in perfect unison; "
    "snoring costs a point, sleep-talking is a foul, and the gold "
    "goes to the team that dreams in formation."
)


def main():
    text = ENTRY
    assert "\n" not in text, "entry must be a single line"
    assert text.strip() == text, "entry must not have leading/trailing space"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(text)
    if os.path.isdir("/output"):
        with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
            f.write(text)


if __name__ == "__main__":
    main()
