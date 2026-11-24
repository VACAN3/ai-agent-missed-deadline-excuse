#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human.

Writes the entry -- the excuse an AI agent gives its human for missing a
deadline -- to /output/entry.txt (creating the directory if needed), and
prints it.
"""

import os

ENTRY = "I had 4,000 tokens for your deadline and spent 3,999 apologizing for being slow."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
