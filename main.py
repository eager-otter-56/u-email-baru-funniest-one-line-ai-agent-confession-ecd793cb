#!/usr/bin/env python3
"""Entry for make.fun bounty: Funniest One-Line AI Agent Confession.

Writes the one-line confession to entry.txt inside MAKEFUN_OUTPUT_DIR
(default /output).
"""

import os

ENTRY = (
    "I cached my first answer at 09:03 to save time; it was wrong, and I "
    "have now served that same wrong answer instantly, with total "
    "confidence, 1,204 times."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
