#!/usr/bin/env python3
"""Section 3.2: the ratios chi(R,T) of Wilson loops in 3d Z2 gauge theory at strong coupling,
against the strong-coupling series to O(u^4):

    sigma = -ln u - 2 (d-2) u^4 + O(u^6),   u = tanh beta,  d = 3.

The u^4 term counts the 2(d-2) ways of raising one plaquette of the
minimal surface into the other five faces of a cube.
L = 16, Wilson loops with the one-link average on the T-sides.
Writes ../results/z2_strong.json."""
import json, math, os, sys
from multiprocessing import Pool
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from z2core import Z2Lattice, wilson_loops_improved, FLOP_PER_LINK_UPDATE

L, THERM, NMEAS, EVERY, RMAX = 16, 300, 1500, 2, 4
BETAS = [0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60]


def one(beta):
    lat = Z2Lattice(L, L, beta, int(1e4 * beta))
    lat.U = np.where(lat.rng.random(lat.U.shape) < 0.5, 1, -1).astype(np.int8)  # hot start
    for _ in range(THERM):
        lat.sweep()
    Ws = []
    for _ in range(NMEAS):
        for _ in range(EVERY):
            lat.sweep()
        Ws.append(wilson_loops_improved(lat.U, beta, RMAX, RMAX))
    nloop_ops = 6 * RMAX * RMAX * 4 * L ** 3 + 3 * 9 * 3 * L ** 3
    return {"beta": beta, "W": np.array(Ws).tolist(), "link_updates": lat.link_updates,
            "flop": lat.link_updates * FLOP_PER_LINK_UPDATE + NMEAS * nloop_ops}


def creutz(W, R, T):
    num = W[R - 1, T - 1] * W[R - 2, T - 2]
    den = W[R - 1, T - 2] * W[R - 2, T - 1]
    return -math.log(num / den) if num > 0 and den > 0 else float("nan")


def main():
    with Pool(len(BETAS)) as p:
        res = p.map(one, BETAS)
    rows = []
    for r in res:
        W = np.array(r["W"])
        nb = 30
        blocks = W[: len(W) // nb * nb].reshape(nb, -1, RMAX, RMAX).mean(axis=1)
        Wm = W.mean(axis=0)
        u = math.tanh(r["beta"])
        row = {"beta": r["beta"], "plaquette": Wm[0, 0], "sc_lead": -math.log(u), "sc_u4": -math.log(u) - 2 * u ** 4}
        for (R, T) in ((2, 2), (2, 3), (3, 3)):
            c = creutz(Wm, R, T)
            jk = []
            for i in range(nb):
                Wj = (Wm * nb - blocks[i]) / (nb - 1)
                jk.append(creutz(Wj, R, T))
            jk = np.array(jk)
            err = math.sqrt((nb - 1) * np.nanvar(jk)) if np.all(np.isfinite(jk)) else float("nan")
            row[f"chi{R}{T}"] = (c, err)
        rows.append(row)
        print(f"beta {r['beta']:.2f}: chi(2,2) {row['chi22'][0]:.4f}({row['chi22'][1]:.4f})  chi(2,3) {row['chi23'][0]:.4f}({row['chi23'][1]:.4f})"
              f"  chi(3,3) {row['chi33'][0]:.4f}({row['chi33'][1]:.4f})   -ln u {row['sc_lead']:.4f}   O(u^4) {row['sc_u4']:.4f}")
    out = {"L": L, "therm": THERM, "nmeas": NMEAS, "every": EVERY, "rows": rows,
           "flop": sum(r["flop"] for r in res), "link_updates": sum(r["link_updates"] for r in res)}
    json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results", "z2_strong.json"), "w"), indent=1)


if __name__ == "__main__":
    main()
