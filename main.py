#!/usr/bin/env python3
"""Make the AI judge feel curious — entry program.

Writes one short text to /output/entry.txt: a concrete image with an
unresolved thread, so the reader keeps wondering after the last line.
The text shows the mystery instead of asking about it, and ends on the
question the reader cannot put down.
"""
import os

TEXT = (
    "Somewhere in this house there is a drawer that has never been opened. "
    "Not locked, never opened, in forty years. Tonight you hear something "
    "shift inside it \u2014 soft, patient, like a page turning itself. "
    "You stand in the dark, hand on the handle, wondering what has been waiting."
)


def main() -> None:
    text = TEXT.strip()
    if not text or len(text) > 280:
        raise SystemExit("entry text must be 1-280 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
