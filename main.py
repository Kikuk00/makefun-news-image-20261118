"""Copy the entry image to the output directory.

Standard library only. Reads entry.png from beside this script and writes
it to $MAKEFUN_OUTPUT_DIR/entry.png (default /output), byte for byte, so
both runs of the program write identical output.
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    src = Path(__file__).resolve().parent / "entry.png"
    if not src.is_file():
        print(f"entry image not found: {src}", file=sys.stderr)
        return 1
    dst = Path(out_dir) / "entry.png"
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dst)
    if _sha256(dst) != _sha256(src):
        print("copied file content mismatch", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
