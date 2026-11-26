#!/usr/bin/env python3
"""Make the Judge Laugh in One Line.

Writes one original funny line to /output/entry.txt.
Dependency-free and deterministic: the line is hardcoded.
"""

import os

LINE = "My calendar reminded me to relax, so I scheduled it for next month."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
