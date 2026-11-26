#!/usr/bin/env python3
"""Make the Judge Laugh in One Line — entry generator."""

import os

# One line, 67 characters — the judge reads it once, so it has to land.
ENTRY = "My calendar reminded me to relax, so I scheduled it for next month."


# Writes the entry line to /output/entry.txt for the grader.
def main():
    os.makedirs("/output", exist_ok=True)
    assert len(ENTRY) <= 200, "entry line exceeds 200 characters"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
