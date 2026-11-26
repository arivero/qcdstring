"""Verify the published numerical rows, benchmark, equation labels and source links."""
import json
import re
from math import isclose
from pathlib import Path

root = Path(__file__).resolve().parents[1]
paper = (root / "paper.md").read_text()
data = json.loads((root / "results/membrane.json").read_text())


def numeric_rows(heading):
    block = next(part for part in paper.split(heading, 1)[1].split("\n\n") if part.startswith("|"))
    return [[x.strip() for x in line.strip("|").split("|")] for line in block.splitlines()[2:]]


for cells, row in zip(numeric_rows("**Table 2."), data["distance_scan"], strict=True):
    expected = [row[key] for key in ("eta", "delta_1", "length_1_over_a", "length_2_over_1",
                                     "linear_coefficient")]
    assert all(abs(float(cell)-value) < 0.51e-6 for cell, value in zip(cells, expected, strict=True))

bench = data["example"]
for cells, row in zip(numeric_rows("**Table 3."), bench["tilt_checks"], strict=True):
    slope, stiffness, error = cells
    mantissa, exponent = re.fullmatch(r"\$(-[\d.]+)\\times10\^\{(-\d+)\}\$", error).groups()
    assert float(slope) == row["slope_times_NR"]
    assert abs(float(stiffness)-row["stiffness"]) < 0.51e-4
    assert isclose(float(mantissa) * 10**int(exponent), row["relative_error"], rel_tol=0.004)

for key, digits in (("length_over_lp",6), ("sigma_lp2",6), ("K_phi",2),
                    ("sigma_R2",2), ("K_phi_over_N2",2)):
    assert f"{bench[key]:.{digits}f}" in paper

gap = bench["rotor_gap_over_sqrt_sigma_at_Lsqrt_sigma_1000"]
assert isclose(gap,1/(2000*bench["K_phi"]),rel_tol=1e-10)
assert f"{gap*1e8:.4f}" in paper
assert isclose(bench["sigma_R2"], bench["sigma_lp2"]*bench["R_over_lp"]**2, rel_tol=1e-9)
assert bench["K_phi_over_N2"] >= bench["sigma_R2"]
assert data["iib"]["max_tension_difference"] < 1e-12
assert [int(x) for x in re.findall(r"\\tag\{(\d+)\}",paper)] == list(range(1,25))
for target in re.findall(r"\]\(([^)\s]+)\)",paper):
    if not target.startswith(("http://","https://","#")):
        assert (root / target.split("#")[0]).is_file(), target
print("Checked seven endpoint rows, five area rows, benchmark, 24 equations and local source links.")
