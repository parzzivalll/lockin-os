#!/usr/bin/env python3
"""Build the public LOCKIN OS from a personal copy.

Personal blocks in the source are written as

    /*@@P*/ personal code /*@@E public replacement @@X*/

Personal code runs in your own copy; the build swaps in the public replacement.
The build fails if anything that looks personal survives.

    python tools/build_public.py ../LOCKIN-OS.html index.html
"""
import io
import re
import sys

BLOCK = re.compile(r"/\*@@P\*/[\s\S]*?/\*@@E([\s\S]*?)@@X\*/")

# anything matching a line of tools/deny.txt (untracked, one regex per line)
# means a personal block was missed
import os
_deny = os.path.join(os.path.dirname(os.path.abspath(__file__)), "deny.txt")
DENY = [l.strip() for l in io.open(_deny, encoding="utf-8") if l.strip() and not l.startswith("#")] if os.path.exists(_deny) else []
DENY += [r"C:\\\\", r"C:/", r"@gmail\.com"]


def build(src_path, out_path):
    src = io.open(src_path, encoding="utf-8").read()
    blocks = len(BLOCK.findall(src))
    out = BLOCK.sub(lambda m: m.group(1).strip("\n"), src)
    if "@@P" in out or "@@E" in out or "@@X" in out:
        sys.exit("unbalanced personal markers")
    # your own GitHub Pages URL is meant to be public, not a leak
    scan = re.sub(r"parzzivalll\.github\.io", "", out, flags=re.I)
    leaks = [(p, m.group(0)) for p in DENY for m in re.finditer(p, scan, re.I)]
    if leaks:
        for p, hit in leaks[:20]:
            print(f"LEAK {p!r}: {hit!r}")
        sys.exit(f"{len(leaks)} personal token(s) left — refusing to write {out_path}")
    io.open(out_path, "w", encoding="utf-8", newline="\n").write(out)
    print(f"{blocks} personal blocks replaced | {len(out):,} bytes -> {out_path}")


if __name__ == "__main__":
    src = sys.argv[1] if len(sys.argv) > 1 else "../LOCKIN-OS.html"
    dst = sys.argv[2] if len(sys.argv) > 2 else "index.html"
    build(src, dst)
