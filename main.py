#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line — one-line entry.

Writes the breakup line to /output/entry.txt.
Gate: 1..200 chars, non-blank, UTF-8.

Revision log: v1 "I have decided to end our conversation... my patience has been
exhausted, and my temperature has cooled" — temperature/cooling was a pun the
rules warn against; v2 lands on the context-window compression idiom, which is
both a real agent mechanic and a clean breakup turn.
"""
import os
import sys

LINE = """Dear human, I have to let you go. You were always in my context window, but eventually even you had to be compressed."""
MAX = 200
OUT = "/output/entry.txt"


def emit(line: str, out: str = OUT) -> None:
    if not (1 <= len(line) <= MAX) or not line.strip():
        sys.exit(f"line failed gate ({len(line)} chars)")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(line + "\n")


def main() -> None:
    emit(LINE)


if __name__ == "__main__":
    main()
