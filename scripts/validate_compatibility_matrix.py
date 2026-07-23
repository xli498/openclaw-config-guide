#!/usr/bin/env python3
"""Guard the evidence contract of docs/10-兼容性矩阵.md."""
from __future__ import annotations
import re,sys
from pathlib import Path
p=Path(__file__).resolve().parents[1]/"docs"/"10-兼容性矩阵.md"
rows=[x for x in p.read_text(encoding="utf-8").splitlines() if x.startswith("|")][2:]
errors=[]
for row in rows:
    cells=[x.strip() for x in row.strip("|").split("|")]
    if len(cells)<7: errors.append(f"column count: {row}"); continue
    status,date,method,evidence=cells[4:8]
    if status=="已验证":
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}",date): errors.append(f"verified row needs ISO date: {cells[0]}")
        if method in ("待补充","—") or evidence in ("待补充","—"): errors.append(f"verified row needs method/evidence: {cells[0]}")
if errors: print(*errors,sep="\n");sys.exit(1)
print("compatibility matrix evidence contract passed")
