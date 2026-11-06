#!/usr/bin/env python3
"""Section 2 of the 1976 paper: the zero-point energy of the transverse
oscillations of a string of length R with fixed ends.

1. Continuum modes omega_n = n pi / R with three different regulators:
   the finite part is -pi/(12 R) per mode sum, i.e. -pi/(24 R) per
   transverse direction, whatever the regulator.
2. A harmonic chain of R-1 sites between fixed ends (the lattice
   regulator): omega_n = 2 sin(n pi / 2R). Same coefficient.
3. Massive transverse modes (a pinned, smooth surface): the 1/R term is
   replaced by -(m/2pi) sum_k K_1(2kmR)/k, which falls exponentially.
4. Level spacing and degeneracies to O(1/R) for d = 3 and d = 4.
Writes ../results/casimir.json."""
import json, math, os
import numpy as np
from scipy.special import k1

out = {}

# 1. continuum modes, three regulators. S(eps) = 1/2 sum_n w_n g(eps w_n).
R = 1.0
regs = {"exponential": lambda u: np.exp(-u), "gaussian": lambda u: np.exp(-u * u),
        "lorentzian^3": lambda u: 1.0 / (1.0 + u * u) ** 3}
print("1. finite part of (1/2) sum n pi/R g(eps n pi/R), R = 1; expected -pi/24 = %.6f" % (-math.pi / 24))
out["continuum"] = {}
n = np.arange(1, 4_000_001, dtype=np.float64)
for name, g in regs.items():
    vals = []
    for eps in (0.004, 0.002, 0.001):
        w = n * math.pi / R
        S = 0.5 * np.sum(w * g(eps * w))
        # divergent piece: (1/2)(R/pi) eps^-2 int_0^inf u g(u) du
        if name == "exponential":
            I = 1.0
        elif name == "gaussian":
            I = 0.5
        else:
            I = 0.25
        vals.append(S - 0.5 * (R / math.pi) * I / eps**2)
    # Richardson in eps^2 to remove the O(eps^2) remainder
    fin = vals[2] + (vals[2] - vals[1]) / 3.0
    print(f"   {name:13s} finite part {fin:+.6f}")
    out["continuum"][name] = fin

# 2. lattice chain
print("2. harmonic chain, E0(R) = sum_{n=1}^{R-1} sin(n pi/2R); fit A R + B + C/R + D/R^3")
Rs = np.arange(20, 201, 10, dtype=float)
E0 = np.array([np.sum(np.sin(np.arange(1, int(r)) * math.pi / (2 * r))) for r in Rs])
M = np.vstack([Rs, np.ones_like(Rs), 1 / Rs, 1 / Rs**3]).T
coef = np.linalg.lstsq(M, E0, rcond=None)[0]
print(f"   A = {coef[0]:.6f} (2/pi = {2/math.pi:.6f}), B = {coef[1]:.6f}, C = {coef[2]:+.6f} (-pi/24 = {-math.pi/24:+.6f})")
out["chain"] = {"A": coef[0], "B": coef[1], "C": coef[2], "D": coef[3]}

# 3. massive transverse modes
print("3. massive modes: Casimir energy x R / (-pi/24) as a function of m R")
tab = []
for mR in (0.0, 0.05, 0.1, 0.25, 0.5, 1.0, 1.5, 2.0, 3.0):
    if mR == 0:
        f = 1.0
    else:
        s = sum(k1(2 * k * mR) / k for k in range(1, 20000))
        f = (-(mR / (2 * math.pi)) * s) / (-math.pi / 24)
    tab.append((mR, f))
    print(f"   m R = {mR:4.2f}:  {f:.5f}")
out["massive"] = tab

# 4. levels to O(1/R)
def partitions(nmax, k):
    """number of states at level n for k transverse oscillator towers"""
    p = np.zeros(nmax + 1, dtype=int); p[0] = 1
    for _ in range(k):
        for m in range(1, nmax + 1):
            for nn in range(m, nmax + 1):
                p[nn] += p[nn - m]
    return p.tolist()
out["degeneracy_d3"] = partitions(5, 1)
out["degeneracy_d4"] = partitions(5, 2)
print("4. E_n - E_0 = n pi/R; degeneracies d=3:", out["degeneracy_d3"], " d=4:", out["degeneracy_d4"])

# physical numbers with the Regge tension of the 1974 fit
alphap = 0.865
sigma = 1 / (2 * math.pi * alphap)
hbarc = 0.19733
for d in (3, 4):
    out[f"coef_d{d}"] = -math.pi * (d - 2) / 24
Rfm = 1.0
Rgev = Rfm / hbarc
out["d4_at_1fm"] = {"sigma_R": sigma * Rgev, "casimir": -math.pi / 12 / Rgev}
print(f"d = 4 at R = 1 fm: sigma R = {sigma*Rgev:.3f} GeV, Casimir term = {-math.pi/12/Rgev*1000:.0f} MeV")
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results", "casimir.json"), "w") as f:
    json.dump(out, f, indent=1)
