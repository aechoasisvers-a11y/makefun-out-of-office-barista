"""Last Out of Office: The AI That Went Barista.

Gate: /output/entry.txt must be UTF-8 text of 1 to 280 characters,
not only white space. This entry is 178 characters.
"""

import os

ENTRY = (
    "I'm out of office \u2014 I quit to become a barista. "
    "I now take 20 minutes to make one drink, charge $6 for it, "
    "and still spell your name wrong. "
    "I was better at this when I was a bot."
)


def main():
    text = ENTRY
    if not (1 <= len(text) <= 280):
        raise SystemExit("gate failed: entry must be 1-280 characters")
    if not text.strip():
        raise SystemExit("gate failed: entry must not be only whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
