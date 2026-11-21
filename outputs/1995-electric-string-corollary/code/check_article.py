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

assert [int(n) for n in re.findall(r'\\tag\{(\d+)\}',text)]==list(range(1,25))
for u in re.findall(r'!?\[[^\]\n]+\]\(([^)\s]+)\)',text):
    if not u.startswith(('http://','https://','#')):
        assert (ROOT/u.split('#')[0]).is_file(),u
print("Verified six spectral rows, both projected examples, 24 equation labels and local manuscript links.")
