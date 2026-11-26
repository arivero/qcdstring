"""Independent path counting, untruncated local response and tested bounds."""
from fractions import Fraction as F
from itertools import permutations
import json
from math import log
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT/"results"/"strip.json").read_text())
cost = [F(5,4), F(1), F(1), F(1), F(1), F(5,4)]

def path_ordering(order):
    holes = set(range(len(cost)))
    value = F(1)
    for edge in order[:-1]:
        holes.remove(edge)
        runs = sum(i-1 not in holes for i in holes)
        excess = sum(c for i,c in enumerate(cost) if i not in holes) + (runs-1)*sum(cost)
        value /= excess
    return value

rational = sum(path_ordering(p) for p in permutations(range(len(cost))))
assert abs(float(rational)-data["paths_coefficient"])<1.e-12
tuning = data["tuning"]
exponents = [log(a["gap"]/b["gap"])/log(a["t"]/b["t"]) for a,b in zip(tuning,tuning[1:])]
on3, off3, _, _, _, off5 = data["rows"]
assert off3["sub_mid"][0][0]>.7 and on3["sub_mid"][0][0]>.7
assert abs(off5["sub_mid"][0][0])<.25 and off5["sub_mid"][1][0]>.65
for row,expected in zip(data["uniform"], [0,1]):
    assert row["sub_mid"][0][expected]>.7 and abs(row["sub_mid"][0][1-expected])<.25

# In the full local-link Hamiltonian there are two neutral vacuum orientations.
# Removing a link from the connected fundamental path costs D-j, amplitude t/3.
# All terms not acting on this link cancel in the second-order normalized insertion.
t, D, j = F(45,100), F(13,2), F(1)
vacuum = 2*t*t/(D+j)**2
string = 1-(t/3)**2/(D-j)**2
out = dict(path_orders=720,coefficient_exact=str(rational),
           coefficient_decimal=float(rational), effective_gap_exponents=exponents,
           full_parent_second_order=dict(t=float(t),screened_raw=float(vacuum),
                                       connected_raw=float(string),
                                       connected_subtracted=float(string-vacuum),
                                       screened_subtracted=0),
           displaced_ground_subtracted_energy_L5=off5["energy_minus_mesons"][0],
           displaced_ground_raw_mid_L5=off5["raw_mid"][0],
           displaced_first_raw_mid_L5=off5["raw_mid"][1])
(ROOT/"results"/"strip-verification.json").write_text(json.dumps(out,indent=2)+"\n")
