#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch.

Writes a single sentence pitching a ridiculous invention that fixes a tiny
everyday annoyance: a smoke detector that holds its 3am low-battery beep
until noon, then resigns by letter. Stdlib only.
"""

import os
import sys

LINE = (
    "My smoke detector holds its 3am low-battery beep until noon \u2014 "
    "then delivers it as a formal letter of resignation from the ceiling."
)

MAX_CHARS = 220


def validate_line(line):
    """Check the pitch meets the gate: 1-220 chars, one line, not blank."""
    if not line or not line.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if len(line) > MAX_CHARS:
        raise ValueError("entry is %d chars, over the 220-char limit" % len(line))
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 0x20 for ch in line):
        raise ValueError("entry must not contain control characters")
    if line.count(".") != 1 or not line.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    return line


def output_dir():
    for var in ("MAKEFUN_OUTPUT_DIR", "ENTRY_OUTPUT_DIR"):
        value = os.environ.get(var)
        if value:
            return value
    return "/output"


def main():
    line = validate_line(LINE)
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    os.chmod(path, 0o644)
    print(line)
    print("chars: %d" % len(line))
    return 0


if __name__ == "__main__":
    sys.exit(main())
