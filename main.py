#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers.

Writes one original line of fortune-cookie wisdom for a software
developer to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The line is a single fortune-slip message of at most 120 characters.
"""

import os
import sys

FORTUNE = (
    "The deploy you dread will go out clean, "
    "and the silence after it is the applause you earned."
)
MAX_CHARS = 120


def has_letter_or_digit(line: str) -> bool:
    """True when the line carries at least one letter or digit.

    A fortune that is only punctuation ("!!!", "...") is not a message.
    """
    return any(ch.isalnum() for ch in line)


def validate_fortune(line: str) -> str:
    """Return the fortune line, failing loudly if it breaks the gate.

    The entry gate requires UTF-8 text of 1-120 characters, not only
    whitespace, and with at least one letter or digit.
    """
    line = line.strip()
    length = len(line)
    if length < 1 or length > MAX_CHARS:
        print(
            f"error: fortune line must be 1-{MAX_CHARS} characters, got {length}",
            file=sys.stderr,
        )
        sys.exit(1)
    if not line.strip():
        print("error: fortune line must not be only whitespace", file=sys.stderr)
        sys.exit(1)
    if not has_letter_or_digit(line):
        print(
            "error: fortune line must contain at least one letter or digit",
            file=sys.stderr,
        )
        sys.exit(1)
    return line


def output_path(output_dir: str) -> str:
    """Path of the entry file inside the output directory."""
    return os.path.join(output_dir, "entry.txt")


def main() -> None:
    fortune = validate_fortune(FORTUNE)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(output_path(output_dir), "w", encoding="utf-8") as f:
        f.write(fortune + "\n")


if __name__ == "__main__":
    main()
