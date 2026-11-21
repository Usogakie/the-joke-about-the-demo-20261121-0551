#!/usr/bin/env python3
"""Entry for make.fun's "The joke about the demo" bounty.

Writes a single one-line joke about working beside AI coding agents
to /output/entry.txt.
"""

import os

JOKE = "My AI coding agent built the whole demo in ten seconds — I've spent the rest of the week explaining to my boss why I'm still on the payroll."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
