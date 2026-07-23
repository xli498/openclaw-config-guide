#!/usr/bin/env python3
"""Check local Markdown links without external dependencies."""
from __future__ import annotations
import re, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
def main():
    errors = []
    for path in [ROOT / "README.md", *sorted((ROOT / "docs").glob("**/*.md"))]:
        if not path.exists(): continue
        for target in LINK.findall(path.read_text(encoding="utf-8")):
            if target.startswith(("http://", "https://", "mailto:", "#")): continue
            target = target.split("#", 1)[0]
            if target and not (path.parent / target).resolve().exists(): errors.append(f"{path.relative_to(ROOT)} -> {target}")
    if errors:
        print("Broken Markdown links:", *[f"- {x}" for x in errors], sep="\n"); return 1
    print("Markdown link validation passed"); return 0
if __name__ == "__main__": sys.exit(main())
