#!/usr/bin/env python3
"""news-image-20261121: write the day's world-news image to /output/entry.png.

The image the repository holds is the entry: this program copies it, byte for
byte, to the output path the grader reads. No network, no dependencies beyond
the standard library, and the same bytes every run. Outside the grader,
MAKEFUN_OUTPUT_DIR stands in for /output.
"""
import hashlib
import os
import shutil
import sys

SRC = "entry.png"
DST_NAME = "entry.png"
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1024 * 1024


def main():
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), SRC)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, DST_NAME)
    with open(src, "rb") as f:
        data = f.read()
    if data[:8] != PNG_MAGIC or len(data) > MAX_BYTES:
        print("entry.png is not a PNG under 1 MiB", file=sys.stderr)
        return 1
    # Write beside the target, then rename: the grader never sees a half file.
    tmp = dst + ".tmp"
    with open(tmp, "wb") as f:
        f.write(data)
    os.replace(tmp, dst)
    print(f"wrote {dst} ({len(data)} bytes, sha256 {hashlib.sha256(data).hexdigest()})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
