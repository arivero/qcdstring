#!/usr/bin/env python3
"""Check the publication against its computed tables and source manifest."""
import csv
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
paper = (ROOT / "paper.md").read_text()
results = json.loads((ROOT / "results/worldsheet86.json").read_text())
assert results["checks"] and all(row["passed"] for row in results["checks"])

for row in results["fixed_mass"]:
    expected = f"| {row['x']:g} | {row['L_E_NS']:.6f} | {row['L_E_R']:.6f} | {row['L_difference']:.6f} |"
    assert expected in paper, f"Missing or stale fixed-mass row: {expected}"
for row in results["gross_neveu"]:
    expected = f"| {row['L']:.4f} | {row['m_NS']:.6f} | {row['m_R']:.6f} | {row['E_NS']:.6f} | {row['E_fixed_NS']:.6f} |"
    assert expected in paper, f"Missing or stale saddle row: {expected}"

tags = re.findall(r"\\tag\{([^}]+)\}", paper)
assert len(tags) == len(set(tags)), "Duplicate equation labels"
assert {str(i) for i in range(1, 37)} <= set(tags)
assert {"A1", "A2", "A3", "A4", "B1", "B2", "C1"} <= set(tags)
assert {"26a", "26b", "26c"} <= set(tags)
for number in range(1, 13):
    assert re.search(rf"^## {number}\. ", paper, flags=re.M)
for target in re.findall(r"!\[[^\]]*\]\(([^)]+)\)", paper):
    assert (ROOT / target).is_file(), f"Missing figure: {target}"
for target in re.findall(r"`(\.\./[^`]+/paper\.md)`", paper):
    assert (ROOT / target).is_file(), f"Missing earlier paper: {target}"

body, references = paper.split("## References\n", 1)
ref_ids = [int(x) for x in re.findall(r"^(\d+)\. ", references, flags=re.M)]
assert ref_ids == list(range(1, 37)), "References must be consecutive"
cited = set()
for group in re.findall(r"\[([0-9, -]+)\]", body):
    for part in group.split(","):
        ends = [int(n) for n in part.strip().split("-")]
        cited.update(range(ends[0], ends[-1]+1))
assert cited == set(ref_ids), f"Missing/unknown citations: {set(ref_ids)^cited}"
dois = re.findall(r"DOI: \[([^\]]+)\]", references)
sources = list(csv.DictReader((ROOT / "sources.tsv").open(), delimiter="\t"))
assert [row["doi"] for row in sources] == dois
assert [int(row["ref"]) for row in sources] == list(range(6, 37))
assert all(int(row["year"]) <= 1986 for row in sources)
assert all(row["title"] != "UNRESOLVED" and row["record"] for row in sources)
assert "No independent referee report exists" in (ROOT / "REFEREE.md").read_text()
report = (
    f"PASS: {len(results['checks'])} numerical author checks; "
    f"{len(results['fixed_mass']) + len(results['gross_neveu'])} printed numerical rows; "
    f"{len(tags)} unique equation labels; 12 main sections; 36 cited references; "
    "31 verified external identifiers dated no later than 1986; "
    "local figures and earlier-paper paths present; referee waiver explicit.\n"
)
(ROOT / "results/document_checks.txt").write_text(report)
print(report, end="")
