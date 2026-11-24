#!/usr/bin/env python3
"""One Line, One Minute: The Vending Machine Pickup Line Contest — one
pickup line a vending machine would use on a passing human (max 200
characters). The program writes the single chosen line to
/output/entry.txt."""

import os

ENTRY = "Hey. My coil's been holding this chocolate bar for you since Tuesday, and it only drops for people who press B4 like they mean it."

def main():
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
