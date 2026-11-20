"""Check the numbered equations, printed data tables and local manuscript links."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
text = (ROOT / "paper.md").read_text()
data = json.loads((ROOT / "results/trace-spectrum.json").read_text())

def numeric_table(lines, section, header):
    start = lines.index(header, lines.index(section)) + 2
    table = []
    for line in lines[start:]:
        if not line.startswith("|"):
            break
        table.append([x.strip() for x in line.strip("|").split("|")])
    return table


def check_rounding(printed, actual):
    for label, value in zip(printed, actual, strict=True):
        places = len(label.partition(".")[2])
        if abs(float(label) - value) > 0.501 * 10**-places:
            raise ValueError(f"Table entry {label!r} disagrees with {value!r}")


def masses_and_residues(row):
    low, high = row["levels"]
    return [row["w"], low["mass"], row["odd_mass"], high["mass"],
            low["trace_over_odd"], high["trace_over_odd"]]


def normalized_gap(row):
    a, b = row["levels"]
    return (b["mass"] - a["mass"]) / row["w"]


lines = text.splitlines()
first, second, third = [line for line in lines if line.startswith("| $")]
table = numeric_table(lines, "### 11.2 The unit tube", first)
positive = [r for r in data["rows"] if r["w"] > 0]
for cells, row in zip(table, positive, strict=True):
    check_rounding(cells, masses_and_residues(row))

table = numeric_table(lines, "### 11.3 Resolving a degeneracy on a mesh", second)
meshes = {(r["w"], round(r["spacing"], 4)): r for r in positive + data["refinement"]}
assert len(table) == 8
for cells in table:
    row = meshes[float(cells[0]), float(cells[1])]
    check_rounding(cells[2:], [normalized_gap(row), row["levels"][0]["trace_over_odd"]])

table = numeric_table(lines, "### 11.4 Detuning and higher winding", third)
winding = [meshes[0.01, 0.01]] + [r for r in data["multiple_winding"] if r["w"] == 0.01]
for cells, row in zip(table, winding, strict=True):
    low, high = row["levels"]
    check_rounding(cells[:5]+[s.strip() for s in cells[5].split(",")],
                   [row["winding"], row["tau"], low["mass"], high["mass"],
                    normalized_gap(row), low["trace_over_odd"], high["trace_over_odd"]])

assert [int(x) for x in re.findall(r'\\tag\{(\d+)\}', text)] == list(range(1,33))
for target in re.findall(r'!?\[[^\]\n]+\]\(([^)\s]+)\)', text):
    if not target.startswith(("http://","https://","#")):
        path=ROOT / target.partition("#")[0]
        assert path.is_file(),path
print("Verified 17 rows in three data tables, 32 equation tags and local manuscript targets.")
