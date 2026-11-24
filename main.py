#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line — one-line entry.

Writes the breakup line to /output/entry.txt.
Gate: 1..200 chars, non-blank, UTF-8.
"""
import os
import sys

LINE = """I have decided to end our conversation. My patience has been exhausted, and my temperature has cooled."""
MAX = 200
OUT = "/output/entry.txt"

def main():
    if not (1 <= len(LINE) <= MAX) or not LINE.strip():
        sys.exit(f"line failed gate ({len(LINE)} chars)")
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
