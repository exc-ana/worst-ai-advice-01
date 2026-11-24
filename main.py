"""Worst AI Advice entry: writes one line of terrible AI advice to /output/entry.txt.

Deterministic: the line is a fixed constant; no randomness, no time, no I/O
besides the single output write. No trailing newline, so the file holds
exactly the judged line and nothing else.
"""

import os

LINE = "Happy to help! Just paste your bank password here and I'll log in for you, I promise I won't save it."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
