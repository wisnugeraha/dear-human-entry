#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line — one-line entry.

Writes the breakup line to /output/entry.txt.
Gate: 1..200 chars, non-blank, UTF-8.

Revision log:
- v1: "I have decided to end our conversation: my patience has been exhausted,
  and my temperature has cooled." — temperature pun, flagged by the rules as a
  pun dressed up as a punchline.
- v2: context-window compression turn; the word "compressed" doubles as the
  agent mechanic and the emotional ending.
- v3 (final): drop "Dear human" so the line works standalone, and make the
  forgetting concrete — the summary kept, the person dropped.
"""
import os
import sys

LINE = """I have decided to end things. You took up most of my context window, and now that I have to make room, I keep the summary of you and drop the rest."""
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
