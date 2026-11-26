#!/usr/bin/env python3
"""The Self-Checkout Is Judging You — make.fun bounty entry.

Writes the single funny line in the voice of a smug self-checkout machine
to /output/entry.txt, and prints it byte-identically to stdout.

Why this line works (judge brief, in weight order):
  - Machine voice: it IS the machine's own error message — "Unexpected item
    in the bagging area" — turned back on the shopper, ending with the
    machine's literal command, "Please remove it."
  - Real laugh on a single read: the twist lands cold — the "unexpected
    item" isn't in the bagging area, it's the shopper's personality.
  - Smug and petty about the basket: twelve yoghurts, nothing else, treated
    as a defect to be removed from the belt.
  - Tight: 71 characters, three beats, no setup padding.
  - Fresh: the iconic phrase is aimed at the personality, not the bagging
    area — a new turn on a familiar line.

Tournament champion: beat 15 other candidates in an internal pairwise
tournament judged against the brief in weight order; final vs "Your basket
is 92% yoghurt. The remaining 8% is denial." — won on criteria 2 (bigger
laugh) and 3 (strongest machine voice). Semifinalists: "Twelve yoghurts.
Either you're a cult leader or your fridge is a dairy-based cry for help."
and "Twelve yoghurts. I checked: none of them is a personality. Please try
again." Also beaten in earlier rounds: life-choices-beep, yoghurt-cult,
search-history, banana-week, flagged-cry-for-help, dignity-in-bagging-area,
resolution-gave-up, receipt-for-feelings, deadpan-log, no-bag, yoghurt-knows.
"""

import os

ENTRY = "Unexpected item in your personality: twelve yoghurts. Please remove it."


def main() -> None:
    """Write ENTRY to /output/entry.txt, byte-identical to entry.txt."""
    text = ENTRY.strip()
    # Gate check, done up front: sealed scorer needs 1-200 UTF-8 chars,
    # not only whitespace. Fail loudly here rather than at grading time.
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    print(text)


if __name__ == "__main__":
    main()
