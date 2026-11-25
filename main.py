"""The Funniest Out-of-Office — make.fun entry.

Writes a single line of out-of-office auto-reply to entry.txt: a reply a
real person would set, built around one reversal. The sender does not just
say they are away; they pre-emptively deny that anything is urgent, and
then prove it — they checked twice before leaving.

Stdlib only. The output directory comes from MAKEFUN_OUTPUT_DIR when the
harness sets it, and falls back to /output otherwise. The entry is written
exactly as-is: one line, no trailing newline added beyond the text itself.
"""

import os
import sys

ENTRY = (
    "I'm away until Monday. "
    "If this is urgent, it isn't. "
    "I checked twice before I left."
)


def main() -> int:
    if not 1 <= len(ENTRY) <= 140:
        raise SystemExit("entry must be 1-140 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
