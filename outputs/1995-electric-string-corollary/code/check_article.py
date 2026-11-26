"""Verify printed roundings, source links, equation sequence, and two-mode identities."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
text = (ROOT / "paper.md").read_text()
data = json.loads((ROOT / "results/odd-cluster.json").read_text())
lines = text.splitlines()
start = next(i for i,line in enumerate(lines) if line.startswith("| $w$ |")) + 2
printed = []
for line in lines[start:]:
    if not line.startswith("|"):
        break
    printed.append([v.strip() for v in line.strip("|").split("|")])
for labels,row in zip(printed,data["radial"],strict=True):
    for label,key in zip(labels,("w","relative_mass_squared_w2","neutral_norm","magnetic_overlap"),strict=True):
        decimals = len(label.partition(".")[2])
        if abs(float(label) - row[key]) > 0.501 * 10**-decimals:
            raise ValueError(f"{label} disagrees with {key}")

for row in data["radial"]:
    if "one_term_projection" in row:
        projection = row["one_term_projection"]
        low,high = projection["lower_mass"]**2,projection["upper_mass"]**2
        assert low < row["lambda_n"] < high
        assert abs(low*high-row["lambda_n"]*row["lambda_b"])<1e-12
        assert abs(low+high-row["lambda_n"]-row["lambda_b"]-projection["h_over_mgamma"]**2)<1e-12
        assert abs(projection["lower_vector_weight"] + projection["upper_vector_weight"] - 1)<1e-12

assert [int(n) for n in re.findall(r'\\tag\{(\d+)\}',text)]==list(range(1,39))

# Section 11: printed values against results/spin-structure.json
spin = json.loads((ROOT / "results/spin-structure.json").read_text())
expect = {
    "T/\\pi=0.9999994": round(spin["profile"]["tension_over_pi"], 7) == 0.9999994,
    "0.777464": abs(spin["neutral_block"]["0"]["lowest"] - 0.777464) < 5e-7,
    "$-0.5235985$": abs(spin["casimir"]["chiral_sum_finite_part_periodic"][-1] + 0.5235985) < 5e-8,
    "$+0.2617992$": abs(spin["casimir"]["chiral_sum_finite_part_antiperiodic"][-1] - 0.2617992) < 5e-8,
    "$0.99936$": abs(spin["casimir"]["massive_dirac_difference_times_2L_over_pi"]["0.001"] - 0.99936) < 5e-6,
    "1.00404,1.00063,1.00016": [round(r["difference_times_2L_over_pi"], 5) for r in spin["estimator"]["rows"][:3]] == [1.00404, 1.00063, 1.00016],
    "-0.50478,-0.50068,-0.50017": [round(r["a_NS_hat_over_pi"], 5) for r in spin["estimator"]["rows"][:3]] == [-0.50478, -0.50068, -0.50017],
    "0.49830,0.49977,0.49994": [round(r["ratio_2L_to_L"], 5) for r in spin["estimator"]["rows"][:3]] == [0.4983, 0.49977, 0.49994],
    "$B=0.01004,0.10356,0.21413,0.33141,0.45488$": [round(r["bound"], 5) for r in spin["deformation"]["rows"] if r["w"] in (0.01, 0.1, 0.2, 0.3, 0.4)] == [0.01004, 0.10356, 0.21413, 0.33141, 0.45488],
    "$w_*=0.3889$": round(spin["deformation"]["w_star"], 4) == 0.3889,
    "$0<w\\le0.388$": spin["deformation"]["w_star"] > 0.388,
    "2.70\\times10^{-3}": abs(spin["deformation"]["rows"][2]["sup_df"] - 2.70e-3) < 5e-6,
}
assert all(r["sup_s"] <= r["w"] / 2 + 1e-12 for r in spin["deformation"]["rows"])
variants = spin["deformation"]["bound_at_w_star_variants"]
assert max(variants.values()) - min(variants.values()) < 1e-8
ferm = json.loads((ROOT / "results/fermion-operator.json").read_text())
assert all(v is not None for k in ("sector_1_identity", "sector_2_identity") for v in ferm[k].values())
assert all(m["max_singular_value_minus_f"] < 1e-12 and m["max_cross_sector_entry"] < 1e-12 for m in ferm["mass_matrix"].values())

# Section 11.5: bosonic Hessian at w > 0
bos = json.loads((ROOT / "results/boson-hessian.json").read_text())
table92 = [0.876730, 0.881729, 0.886729]
val = bos["validation"]["0.01"]["l0_masses"]
assert all(min(abs(x - m) for x in val) < 5e-5 for m in table92)
for label in ("$0.876751$", "$0.881702$", "$0.886750$", "$0.46087$", "$0.4389$", "$w_B=0.42$", "$1.126$", "$1.391$"):
    assert label in text, label
assert abs(min(val, key=lambda x: abs(x - 0.876751)) - 0.876751) < 5e-7
scan = {r["w"]: r for r in bos["scan"]}
assert max(scan) == 0.42 and all(max(r["translations"]) < 1e-4 for r in scan.values())
assert all(min(min(v) for v in r["levels"].values()) > 0 for r in scan.values())
lows = [scan[w]["lowest_nontranslation"] for w in sorted(scan)]
assert min(lows) > 0.43 and max(abs(a - b) for a, b in zip(lows, lows[1:])) < 0.018
assert round(scan[0.42]["lowest_nontranslation"], 4) == 0.4389 and round(scan[0.1]["lowest_nontranslation"], 4) == 0.6898
b = bos["budget"]
assert round(b["R25_h0.05"]["lowest_nontranslation"], 5) == 0.46087
assert abs(b["R25_h0.025"]["lowest_nontranslation"] - b["R25_h0.05"]["lowest_nontranslation"]) < 5e-5
assert abs(b["R35_h0.05"]["lowest_nontranslation"] - b["R25_h0.05"]["lowest_nontranslation"]) < 1e-9
assert round(bos["high_l"]["0.388"]["12"][0], 3) == 1.126 and round(bos["high_l"]["0.388"]["16"][0], 3) == 1.391
for label, ok in expect.items():
    assert label in text, label
    assert ok, label
assert spin["neutral_block"]["1"]["below_one"] == [] and spin["neutral_block"]["2"]["below_one"] == []
assert abs(spin["casimir"]["difference_two_majoranas_over_pi"] - 0.5) < 1e-15
assert spin["casimir"]["cft_E_R_times_L_over_pi"] == 0 and spin["casimir"]["cft_E_NS_times_L_over_pi"] == -0.5
for u in re.findall(r'!?\[[^\]\n]+\]\(([^)\s]+)\)',text):
    if not u.startswith(('http://','https://','#')):
        assert (ROOT/u.split('#')[0]).is_file(),u
print("Verified six spectral rows, both projected examples, 38 equation labels, the Section 11 values and local manuscript links.")
