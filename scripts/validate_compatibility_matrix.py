#!/usr/bin/env python3
"""Guard the evidence contract of docs/10-兼容性矩阵.md."""
from __future__ import annotations
import re
import sys
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "docs" / "10-兼容性矩阵.md"
lines = path.read_text(encoding="utf-8").splitlines()
start = next((i for i, line in enumerate(lines) if line.startswith("| 模块 |")), None)
if start is None:
    print("compatibility table not found")
    sys.exit(1)

rows = []
for line in lines[start + 2:]:
    if not line.startswith("|"):
        break
    rows.append(line)

errors = []
for row in rows:
    cells = [cell.strip() for cell in row.strip("|").split("|")]
    if len(cells) != 7:
        errors.append(f"unexpected compatibility row: {row}")
        continue
    module, _environment, date, method, status, evidence, _notes = cells
    if status not in ("待验证", "已验证", "已知失效"):
        errors.append(f"invalid status for {module}: {status}")
    if status == "待验证" and (date != "待补充" or evidence != "—"):
        errors.append(f"unverified row must use a pending date and no evidence: {module}")
    if status == "已验证":
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date):
            errors.append(f"verified row needs ISO date: {module}")
        if method in ("待补充", "—") or evidence in ("待补充", "—"):
            errors.append(f"verified row needs method and evidence: {module}")

if errors:
    print(*errors, sep="\n")
    sys.exit(1)
print("compatibility matrix evidence contract passed")
