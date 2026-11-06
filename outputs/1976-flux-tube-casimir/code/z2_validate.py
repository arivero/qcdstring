#!/usr/bin/env python3
"""Validation of the two-level estimator (Section 3.2).

On a lattice small enough for the direct estimate to work, both
estimators of C(R) = <P(0)P(R)> are evaluated on the same Markov chain:
for every outer configuration the direct product of Polyakov lines is
averaged over the same sub-updates whose slab averages enter the
two-level estimate. The two are unbiased estimators of one quantity,
so their difference must vanish within its (small) error.

Two settings: Nt = 6 with slabs of 2, and Nt = 8 with slabs of 4 (the
slab thickness of the production runs). beta = 0.70, L = 12.
Writes ../results/z2_validate.json."""
import json, os, sys, time
from multiprocessing import Pool
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from z2core import Z2Lattice, slab_line_products, naive_polyakov, FLOP_PER_LINK_UPDATE

BETA, L, RMAX, NSUB, NOUT = 0.70, 12, 4, 20, 6000


def blocked(a, nb=30):
    a = np.asarray(a)
    a = a[: len(a) // nb * nb].reshape(nb, -1, a.shape[1]).mean(axis=1)
    return a.mean(0), a.std(0, ddof=1) / np.sqrt(nb)


def one(args):
    Nt, tau, seed = args
    lat = Z2Lattice(Nt, L, BETA, seed, frozen_tau=tau)
    for _ in range(2000):
        lat.sweep()
    nslab = Nt // tau
    ML, NV = [], []
    for _ in range(NOUT):
        for _ in range(2):
            lat.sweep()
        acc = np.zeros((nslab, L, L, RMAX, 2))
        nv = np.zeros(RMAX)
        for _ in range(NSUB):
            lat.sweep(frozen=True)
            Lk = slab_line_products(lat.U, tau).astype(float)
            for R in range(1, RMAX + 1):
                acc[..., R - 1, 0] += Lk * np.roll(Lk, -R, axis=1)
                acc[..., R - 1, 1] += Lk * np.roll(Lk, -R, axis=2)
            nv += naive_polyakov(lat, RMAX).mean(axis=1)
        ML.append((acc / NSUB).prod(axis=0).mean(axis=(0, 1)).mean(axis=1))
        NV.append(nv / NSUB)
    ML, NV = np.array(ML), np.array(NV)
    m1, e1 = blocked(NV)
    m2, e2 = blocked(ML)
    d, ed = blocked(ML - NV)
    return {"Nt": Nt, "tau": tau, "seed": seed, "direct": [m1.tolist(), e1.tolist()],
            "two_level": [m2.tolist(), e2.tolist()], "difference": [d.tolist(), ed.tolist()],
            "pull": (d / ed).tolist(), "link_updates": lat.link_updates,
            "flop": lat.link_updates * FLOP_PER_LINK_UPDATE + lat.meas_ops}


def main():
    t0 = time.time()
    with Pool(2) as p:
        res = p.map(one, [(6, 2, 21), (8, 4, 31)])
    for r in res:
        print(f"Nt = {r['Nt']}, slabs of {r['tau']}:")
        for R in range(RMAX):
            print(f"  R={R+1}: direct {r['direct'][0][R]:.5f}({r['direct'][1][R]:.5f})"
                  f"  two-level {r['two_level'][0][R]:.5f}({r['two_level'][1][R]:.5f})"
                  f"  difference {r['difference'][0][R]:+.5f}({r['difference'][1][R]:.5f})  pull {r['pull'][R]:+.2f}")
    out = {"beta": BETA, "L": L, "n_sub": NSUB, "n_outer": NOUT, "runs": res, "seconds": time.time() - t0}
    json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results", "z2_validate.json"), "w"), indent=1)


if __name__ == "__main__":
    main()
