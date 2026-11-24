#!/usr/bin/env python3
"""Everyday Things, Two Lines — make.fun entry.

Writes the two-line explanation to /output/entry.txt.

Line 1 explains a queue to a 10-year-old in a single vivid sentence built
on one analogy (a caterpillar). Line 2 says in one sentence what that
analogy maps and what it leaves out.
"""

import os
import sys

LINE_1 = (
    "A queue is a caterpillar made of people, shuffling forward one wiggle "
    "at a time whenever the person at the very front takes a step."
)

LINE_2 = (
    "The caterpillar shows how the whole line moves as one wave starting "
    "from the front, but it leaves out that a person can step out of line, "
    "cut in halfway, or overtake \u2014 a real caterpillar never lets one of "
    "its legs wander off on its own."
)

ENTRY = LINE_1 + "\n" + LINE_2 + "\n"


def main() -> int:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Self-check: the gate wants UTF-8 text of 1 to 400 characters.
    size = len(ENTRY)
    assert 1 <= size <= 400, f"entry is {size} characters, must be 1-400"
    assert ENTRY.strip(), "entry must not be only white space"
    print(f"wrote {path} ({size} characters)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
