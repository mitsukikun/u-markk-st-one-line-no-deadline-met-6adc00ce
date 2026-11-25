#!/usr/bin/env python3
"""One Line, No Deadline Met — writes a single-line joke excuse for a missed
deadline to /output/entry.txt.

Deterministic, no network, no randomness.
"""

import os

LINE = "I snoozed the deadline reminder so many times it filed a restraining order against me."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
