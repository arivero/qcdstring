#!/usr/bin/env python3
"""Check printed calculations, citations and assets against stored records."""
import csv
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
paper = (ROOT / "paper.md").read_text()
computed = json.loads((ROOT / "results/thickness88.json").read_text())
assert computed["checks"] and all(c["passed"] for c in computed["checks"])
printed_rows = 0
for table in ("masses", "casimir", "regulator"):
    lines = (ROOT / f"results/{table}_table.md").read_text().splitlines()
    for row in lines[2:]:
        assert row in paper, f"Missing/stale table row: {row}"
        printed_rows += 1

labels = re.findall(r"\\tag\{([^}]+)\}", paper)
assert labels == [str(i) for i in range(1, 26)], "Equation labels changed or duplicated"
assert "**gpt-6-astra-max**" in paper, "Requested author signature missing"
assert "passes 91 author checks" in paper and len(computed["checks"]) == 91
for n in range(1, 10):
    assert re.search(rf"^## {n}\. ", paper, re.M)
for target in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", paper):
    if not target.startswith(("https://", "http://")):
        assert (ROOT / target).is_file(), f"Missing local asset: {target}"

body, refs = paper.split("## References\n", 1)
ref_ids = [int(v) for v in re.findall(r"^(\d+)\. ", refs, re.M)]
assert ref_ids == list(range(1, 8))
cited = set()
for group in re.findall(r"\[([0-9, -]+)\]", body):
    for part in group.split(","):
        ends = [int(i) for i in part.strip().split("-")]
        cited.update(range(ends[0], ends[-1]+1))
assert cited == set(ref_ids), f"Unmatched citations: {cited ^ set(ref_ids)}"
manifest = list(csv.DictReader((ROOT / "sources.tsv").open(), delimiter="\t"))
assert [r["doi"] for r in manifest] == re.findall(r"DOI: \[([^\]]+)\]", refs)
assert [int(r["ref"]) for r in manifest] == ref_ids[2:]
assert all(int(r["year"]) <= 1988 and r["record"] and r["coverage"] for r in manifest)

report = (f"PASS: {len(computed['checks'])} calculation checks; {printed_rows} printed "
          f"rows; {len(labels)} unique equations; 9 main sections; {len(ref_ids)} cited references; "
          f"{len(manifest)} external source records within the 1988 cutoff; local assets and "
          "requested author signature present.\n")
(ROOT / "results/document_checks.txt").write_text(report)
print(report, end="")
