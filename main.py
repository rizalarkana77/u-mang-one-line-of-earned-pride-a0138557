#!/usr/bin/env python3
"""One Line of Earned Pride — make.fun u-mang-one-line-of-earned-pride-a0138557.

The entry is a single line of text (1-240 characters). This program writes
it, byte for byte, to the output directory the grader provides
($MAKEFUN_OUTPUT_DIR, default /output/entry.txt).

Python 3.13, standard library only. No network, no randomness, no clock
reads: the same input always produces the same output bytes.
"""

import hashlib
import os

ENTRY = "The night guard who taught himself to read by the gate lamp finished the last page of his first book at 4 a.m. and closed it gently, like it might wake someone."

MAX_CHARS = 240


def main() -> None:
    text = ENTRY
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(f"entry is {len(text)} characters, outside 1-{MAX_CHARS}")
    if not text.strip():
        raise SystemExit("entry is only whitespace")
    if any(ord(c) < 32 for c in text):
        raise SystemExit("entry contains a control character")
    data = text.encode("utf-8")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    if out_dir.strip() == "":
        raise SystemExit(
            "MAKEFUN_OUTPUT_DIR is set but empty; unset it or give a directory"
        )
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "wb") as f:
        f.write(data)

    # Prove the write is exact: read the output back and compare.
    with open(target, "rb") as f:
        written = f.read()
    if written != data:
        raise SystemExit("output does not match the entry byte for byte")
    print(
        f"wrote {target}: {len(text)} chars, {len(written)} bytes, "
        f"sha256 {hashlib.sha256(written).hexdigest()}"
    )


if __name__ == "__main__":
    main()
