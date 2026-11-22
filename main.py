#!/usr/bin/env python3
"""Entry program for news-image-20261122 — Sunday 22 November 2026.

The front page for this day was drawn ahead of time and is stored in
this repository as entry.png (a 1024x1024 PNG). This program's whole
job is to place those exact bytes at entry.png inside the output
directory: /output when the grader runs it, or MAKEFUN_OUTPUT_DIR
when run locally. It uses only the Python standard library and never
touches the network, so both grader runs produce identical output.
"""

import os
import shutil
import sys


def output_directory() -> str:
    """Where the grader expects entry.png to appear."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    if not os.path.isfile(source):
        print("entry.png is missing beside main.py", file=sys.stderr)
        return 1
    dest_dir = output_directory()
    os.makedirs(dest_dir, exist_ok=True)
    dest = os.path.join(dest_dir, "entry.png")
    shutil.copyfile(source, dest)
    # Guard against a truncated copy: sizes must match exactly, which
    # also keeps the two grader runs byte-identical by construction.
    if os.path.getsize(dest) != os.path.getsize(source):
        print("copied entry.png has the wrong size", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
