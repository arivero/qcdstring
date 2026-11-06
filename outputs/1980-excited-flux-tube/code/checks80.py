#!/usr/bin/env python3
"""Exact checks of the 1980 operators: under a random Z2 gauge transformation
g of a time slice, every operator for sources at x0 and x0 + R e must pick
up the factor g(x0) g(x0 + R e). Writes ../results/checks80.txt."""
import os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from z2_excited import slice_operators, smear_slice
from z2_excited_gevp import ops_slice

rng = np.random.default_rng(1980)
L = 12
Sx = rng.choice([-1.0, 1.0], (L, L)); Sy = rng.choice([-1.0, 1.0], (L, L))
g = rng.choice([-1.0, 1.0], (L, L))
Sxg, Syg = g * Sx * np.roll(g, -1, axis=0), g * Sy * np.roll(g, -1, axis=1)
lines = []
o1 = slice_operators(*smear_slice(Sx, Sy, 2, 0.5), 6)
o2 = slice_operators(*smear_slice(Sxg, Syg, 2, 0.5), 6)
worst = 0.0
for c in o1:
    for R in range(1, 7):
        for d in (0, 1):
            ge = g * np.roll(g, -R, axis=d)
            worst = max(worst, np.abs(o1[c][R - 1, d] * ge - o2[c][R - 1, d]).max())
lines.append(f"one-operator basis (z2_excited.py): max deviation {worst:.2e}")
def build(Sx, Sy):
    a, b = smear_slice(Sx, Sy, 2, 0.5); c, d = smear_slice(a, b, 2, 0.5)
    return ops_slice(a, b, c, d, 6)
p1, p2 = build(Sx, Sy), build(Sxg, Syg)
worst = 0.0
for c in p1:
    for R in range(2, 7):
        for d in (0, 1):
            ge = g * np.roll(g, -R, axis=d)
            for k in (0, 1):
                worst = max(worst, np.abs(p1[c][R - 1, d, k] * ge - p2[c][R - 1, d, k]).max())
lines.append(f"two-operator basis (z2_excited_gevp.py): max deviation {worst:.2e}")
print("\n".join(lines))
open(os.path.join(HERE, "..", "results", "checks80.txt"), "w").write("\n".join(lines) + "\n")
