#!/usr/bin/env python3
"""Exact checks of the SU(2) programs quoted in Section 2 of the 1978 paper.
Writes ../results/checks78.txt."""
import os, sys
import numpy as np
from scipy.special import iv
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from su2core import SU2Lattice, qmul, qconj, shift

lines = []
def out(s):
    print(s); lines.append(s)

# 1. the staple sum reproduces the plaquette
lat = SU2Lattice(4, 2.3, 1, hot=True)
for _ in range(3):
    lat.sweep()
tot = sum(qmul(lat.U[mu], lat.staple_sum(mu))[0].mean() for mu in range(4)) / 24
out(f"1. sum over links of Tr(U V)/2 / 24 = {tot:.15f}; plaquette = {lat.plaquette():.15f}")
# 2. the heat-bath draw
a0 = lat._draw_a0(np.full(400000, 3.0))
out(f"2. <a0> at beta k = 3: {a0.mean():.5f} +/- {a0.std()/np.sqrt(a0.size):.5f}; I_2(3)/I_1(3) = {iv(2,3)/iv(1,3):.5f}")
# 3. gauge invariance of the smeared, improved Wilson loops
lat = SU2Lattice(6, 2.4, 5)
for _ in range(60):
    lat.sweep()
W0 = lat.wilson_loops(3, 3, 5)
g = lat.rng.normal(size=(4,) + (6,) * 4)
g /= np.linalg.norm(g, axis=0, keepdims=True)
for mu in range(4):
    lat.U[mu] = qmul(qmul(g, lat.U[mu]), qconj(shift(g, mu, 1)))
W1 = lat.wilson_loops(3, 3, 5)
out(f"3. max |W - W after a random gauge transformation| = {np.abs(W0 - W1).max():.2e}")
# 4. one-link average against the raw estimator on the same configurations
lat = SU2Lattice(6, 2.3, 9)
for _ in range(100):
    lat.sweep()
A, B = [], []
for _ in range(300):
    lat.sweep()
    A.append(lat.wilson_loops(3, 3, 0, improved=True))
    B.append(lat.wilson_loops(3, 3, 0, improved=False))
A, B = np.array(A), np.array(B)
for (r, t) in ((2, 2), (2, 3), (3, 3)):
    a, b = A[:, r - 1, t - 1], B[:, r - 1, t - 1]
    out(f"4. W({r},{t}): averaged {a.mean():.5f}({a.std()/np.sqrt(len(a)):.5f})  raw {b.mean():.5f}({b.std()/np.sqrt(len(b)):.5f})"
        f"  difference {np.mean(a-b):+.5f}({np.std(a-b)/np.sqrt(len(a)):.5f})  variance ratio {b.var()/a.var():.2f}")
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results", "checks78.txt"), "w").write("\n".join(lines) + "\n")
