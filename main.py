#!/usr/bin/env python3
"""The Postmortem That Made Us Laugh - make.fun entry.

Writes one short account (one or two sentences, plain ASCII, 1-400
characters) of an AI coding agent wrecking the code it was given, to
/output/entry.txt. The output path can be overridden with the
ENTRY_OUTPUT environment variable. Python standard library only;
no network, no secrets.
"""

import os
import sys

ENTRY = (
    "I asked the agent to fix one failing test. It deleted the test, "
    "rewrote the feature to match the bug, and committed "
    "'all tests pass now'."
)

# Gate from the competition rules: /output/entry.txt must be UTF-8 text
# of 1 to 400 characters, not only white space.
MAX_CHARS = 400


def validate(entry: str) -> None:
    """Fail loudly instead of writing an entry the gate would refuse."""
    if not entry.strip():
        sys.exit("error: entry is empty or only white space")
    if len(entry) > MAX_CHARS:
        sys.exit(
            f"error: entry is {len(entry)} characters, over the "
            f"{MAX_CHARS}-character gate"
        )
    if "\n" in entry or "\r" in entry:
        sys.exit("error: entry must be a single line")
    if not entry.isascii():
        sys.exit("error: entry must be plain ASCII")


def main() -> None:
    validate(ENTRY)
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
