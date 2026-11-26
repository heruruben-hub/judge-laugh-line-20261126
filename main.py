#!/usr/bin/env python3
"""Make the Judge Laugh in One Line — entry generator."""

import os

ENTRY = "My calendar reminded me to relax, so I scheduled it for next month."


def main():
    os.makedirs("/output", exist_ok=True)
    assert len(ENTRY) <= 200, "entry line exceeds 200 characters"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
