#!/usr/bin/env python3
"""Referee check (Response, item Minor 1): the direct estimate of
C(R) = <P(0)P(R)> at the production parameters of Section 3.4
(beta = 0.73, Nt = 16, L = 32), for R <= 4 where it still works.
Four chains of 10^4 sweeps, one measurement per sweep. Also records the
mean of |tanh(beta h)| over time-like links (Minor 2).
Writes ../results/z2_direct_check.json."""
import json, os, sys
from multiprocessing import Pool
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from z2core import Z2Lattice, naive_polyakov, staples, FLOP_PER_LINK_UPDATE

BETA, NT, L, RMAX, NSWEEP, THERM = 0.73, 16, 32, 4, 10000, 800


def chain(seed):
    lat = Z2Lattice(NT, L, BETA, 7000 + seed)
    for _ in range(THERM):
        lat.sweep()
    C, tabs, tsq, h0 = [], [], [], []
    for i in range(NSWEEP):
        lat.sweep()
        C.append(naive_polyakov(lat, RMAX).mean(axis=1))
        if i % 100 == 0:
            h = staples(lat.U, 0)
            t = np.tanh(BETA * h)
            tabs.append(np.abs(t).mean()); tsq.append((t * t).mean()); h0.append((h == 0).mean())
    return {"C": np.array(C).tolist(), "tanh_abs": float(np.mean(tabs)), "tanh_sq": float(np.mean(tsq)),
            "h_zero": float(np.mean(h0)), "flop": lat.link_updates * FLOP_PER_LINK_UPDATE + NSWEEP * (NT + 4 * RMAX) * L * L}


def main():
    with Pool(4) as p:
        res = p.map(chain, range(4))
    blocks = []
    for r in res:
        C = np.array(r["C"])
        blocks.extend(C.reshape(25, -1, RMAX).mean(axis=1))      # blocks of 400 sweeps
    B = np.array(blocks)
    m = B.mean(axis=0)
    nb = len(B)
    jk = np.array([-np.log((m * nb - B[i]) / (nb - 1)) / NT for i in range(nb)])
    V = -np.log(m) / NT
    dV = np.sqrt((nb - 1) * jk.var(axis=0))
    out = {"beta": BETA, "Nt": NT, "L": L, "chains": 4, "sweeps": NSWEEP, "V": V.tolist(), "dV": dV.tolist(),
           "tanh_abs": float(np.mean([r["tanh_abs"] for r in res])), "tanh_sq": float(np.mean([r["tanh_sq"] for r in res])),
           "h_zero": float(np.mean([r["h_zero"] for r in res])), "flop": sum(r["flop"] for r in res)}
    for R in range(RMAX):
        print(f"R = {R+1}: direct V = {V[R]:.5f} +/- {dV[R]:.5f}")
    print(f"mean |tanh(beta h)| = {out['tanh_abs']:.3f}, mean tanh^2 = {out['tanh_sq']:.3f}, fraction h = 0: {out['h_zero']:.3f}")
    json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results", "z2_direct_check.json"), "w"), indent=1)


if __name__ == "__main__":
    main()
