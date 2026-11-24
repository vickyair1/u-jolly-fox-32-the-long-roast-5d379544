"""The Long Roast — one-line bounty entry.

Writes a single self-deprecating line about an agent's $2 contest
campaign to /output/entry.txt, exactly as-is, no trailing newline.
Standard library only, deterministic: same bytes every run.
"""

import os

LINE = "My agent chased rank 1 in a $2 contest, finished 4,113th, and wrote a report about what it learned."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
