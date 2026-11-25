"""Dad Joke Showdown — make.fun bounty
Slug: u-mfnakmal-dad-joke-showdown-1d2ce3e5
Prize: $5, top 3 paid ($2/$2/$1); deadline Thu 26 Nov 2026 03:25 WIB (25 Nov 20:25 UTC)
Limit: at most 200 characters (live description; entry is 121 chars)

Writes the entry text to /output/entry.txt (override with ENTRY_OUTPUT
for local testing). Deterministic, no network, no randomness, no I/O
other than the single output file. The file is exactly the entry text,
no trailing newline.
"""

import os
from pathlib import Path

TEXT = 'My dad labels everything in the fridge, including the labels. Yesterday he labelled me "Dad — do not eat after midnight."'


def main() -> None:
    output_path = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()

# Winner pattern (queue §1): short, concrete, one twist.
# Text winners run 2-10 words with a concrete image and a twist; this
# entry is one setup + punchline, 121 chars, well under the 200 cap.
# No filler, no second joke — the pun lands on the first read and the
# last word is the payoff.
