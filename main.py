#!/usr/bin/env python3
"""The Funniest Office Joke, Judged Head to Head.

Writes a single original one-line joke about office life to
/output/entry.txt (or to <output_dir>/entry.txt when an output
directory is given as the first argument).

No network, no randomness, no input files: the same line every run.
"""

import sys
from pathlib import Path

# One original line about office life: a setup (asking everyone to
# stop replying all) with a turn (the plea itself triggers 400 more
# reply-alls), punchline last.
JOKE = (
    "I hit reply-all to say 'please stop replying all', "
    "and now 400 people are replying all to agree with me."
)


def main() -> int:
    output_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    # No trailing newline: the gate counts every character in the
    # file, so the file holds exactly the joke line, nothing extra.
    entry_path.write_text(JOKE, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
