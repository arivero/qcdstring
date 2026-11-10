#!/usr/bin/env python3
"""Direct check in the gauge theory (1982 paper, Section 3.4): effective
energies of the closed flux tube from wall-wall correlators of closed
time-like lines at beta = 0.73, from the pilot productions of z2_tube.py
(smeared lines) and z2_wall.py (unsmeared lines; plain and two-level).
Also the autocorrelation times that make this method expensive.
Writes ../results/gauge_check.txt."""
import glob, math, os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from tube82 import tau_int
PIL = os.path.join(HERE, "..", "results", "pilots")
out = []
def say(s=""):
    out.append(s); print(s)


def eff(B, x):
    """Effective energy between x and x+1 with a jackknife error over blocks."""
    nb = len(B)
    g = B.mean(axis=0)
    f = lambda v: math.log(v[x] / v[x + 1]) if v[x] > 0 and v[x + 1] > 0 else float("nan")
    js = np.array([f((g * nb - B[i]) / (nb - 1)) for i in range(nb)])
    return f(g), math.sqrt((nb - 1) * np.nanvar(js))


say("Direct gauge-theory check at beta = 0.73: effective energy of the tube between x and x+1")
say("run                                         lattice      operations   x=1->2        x=2->3        x=3->4")
tot = 0.0
summary = {}
for Nt in (8, 12, 16):
    vals = {1: [], 2: [], 3: []}
    for f in sorted(glob.glob(os.path.join(PIL, f"z2[tw]_b0.7300_Nt{Nt}_*.npz"))):
        d = np.load(f)
        tot += float(d["flop"])
        B = d["C"][:, :, 2, 2] if "C" in d else d["G"]          # smearing level 2, or unsmeared
        row = []
        for x in (1, 2, 3):
            e, de = eff(B, x)
            row.append(f"{e:.4f}({de:.4f})")
            if np.isfinite(e) and de < 0.12:
                vals[x].append(e)
        say(f"{os.path.basename(f):44s}{int(d['Lx']):3d} x {int(d['Ly']):2d}     {float(d['flop']):.2e}    " + "  ".join(row))
    line = f"   Nt = {Nt}: mean over runs, error from their scatter:"
    for x in (1, 2, 3):
        v = np.array(vals[x])
        if len(v) > 1:
            line += f"   x={x}: {v.mean():.4f}({v.std(ddof=1) / math.sqrt(len(v)):.4f}) [{len(v)} runs]"
            summary[(Nt, x)] = (v.mean(), v.std(ddof=1) / math.sqrt(len(v)), len(v))
        elif len(v) == 1:
            line += f"   x={x}: {v[0]:.4f} [1 run]"
    say(line)
say(f"total operations of these runs: {tot:.3e}")
say()
say("Autocorrelation times (sweeps) of the mean line and of the plaquette sum in the z2_tube.py runs,")
say("and the scatter of 1000-sweep averages of the plaquette:")
for f in sorted(glob.glob(os.path.join(PIL, "z2t_b0.7300_*.npz"))):
    d = np.load(f)
    V = int(d["Nt"]) * int(d["Lx"]) * int(d["Ly"])
    p, q = d["pol"], d["plq"] / (3 * V)
    blocks = q[: len(q) // 1000 * 1000].reshape(-1, 1000).mean(axis=1)
    say(f"   Nt {int(d['Nt']):2d}, {int(d['Lx']):2d} x {int(d['Ly']):2d}: tau(line) {tau_int(p):6.1f}  tau(line^2) {tau_int(p ** 2):6.1f}  tau(plaquette) {tau_int(q):6.1f}"
        f"   plaquette {q.mean():.5f}, 1000-sweep means between {blocks.min():.4f} and {blocks.max():.4f}")
open(os.path.join(HERE, "..", "results", "gauge_check.txt"), "w").write("\n".join(out) + "\n")
