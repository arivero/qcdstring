#!/usr/bin/env python3
"""Response, Major 3: calibration of the roughening criterion on the BCSOS
model, whose roughening point is known exactly (van Beijeren 1977).

Heights h on an L x L square lattice, nearest neighbours differing by +-1;
energy K * sum over next-nearest (diagonal) pairs of |h_i - h_j|. At
K_R = (1/2) ln 2 the model roughens. Heat bath on four sublattices (sites of
one class share neither a nearest nor a next-nearest neighbour): a site may
move by +-2 only if all four nearest neighbours lie between the old and new
height. The flat surfaces have mean heights 1/2, 3/2, ...: the layer spacing is
1 in h, and the width is w^2 = var(h).

The slope of w^2 in ln L over L = 16-64 at K_R, compared with the asymptotic
value 1/pi^2, measures the finite-size bias of the criterion used in
Section 5. Writes ../results/bcsos.json."""
import json, math, os
from multiprocessing import Pool
import numpy as np

KR = 0.5 * math.log(2)
JOBS = [(K, L, s) for K in (KR, 0.36) for L in (16, 32, 64) for s in range(4)]
SWEEPS, THERM, EVERY = 30000, 3000, 10


def run(job):
    K, L, seed = job
    rng = np.random.default_rng(int(1e6 * K) + 100 * L + seed)
    x, y = np.indices((L, L))
    h = ((x + y) % 2).astype(np.int64)
    classes = [((x % 2) == a) & ((y % 2) == b) for a in (0, 1) for b in (0, 1)]
    nn = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    nnn = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    w2 = []
    for sweep in range(THERM + SWEEPS):
        for m in classes:
            nbrs = [np.roll(np.roll(h, dx, 0), dy, 1) for dx, dy in nn]
            diag = [np.roll(np.roll(h, dx, 0), dy, 1) for dx, dy in nnn]
            up_ok = np.all([nb == h + 1 for nb in nbrs], axis=0)
            dn_ok = np.all([nb == h - 1 for nb in nbrs], axis=0)
            e0 = sum(np.abs(h - dg) for dg in diag)
            eup = sum(np.abs(h + 2 - dg) for dg in diag)
            edn = sum(np.abs(h - 2 - dg) for dg in diag)
            w0 = np.ones(h.shape)
            wu = np.where(up_ok, np.exp(-K * (eup - e0)), 0.0)
            wd = np.where(dn_ok, np.exp(-K * (edn - e0)), 0.0)
            r = rng.random(h.shape) * (w0 + wu + wd)
            newh = np.where(r < wu, h + 2, np.where(r < wu + wd, h - 2, h))
            h = np.where(m, newh, h)
        if sweep >= THERM and (sweep - THERM) % EVERY == 0:
            w2.append(float(np.var(h)))
    return {"K": K, "L": L, "seed": seed, "w2": w2, "flop": (THERM + SWEEPS) * L * L * 30}


def main():
    with Pool(16) as p:
        res = p.map(run, JOBS)
    out = {"K_R": KR, "runs": res}
    json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results", "bcsos.json"), "w"))
    for K in (KR, 0.36):
        ws = {}
        for L in (16, 32, 64):
            rr = [np.array(r["w2"]) for r in res if r["K"] == K and r["L"] == L]
            means = [w.mean() for w in rr]
            ws[L] = (np.mean(means), np.std(means, ddof=1) / math.sqrt(len(means)))
        x = np.log([16, 32, 64]); y = np.array([ws[L][0] for L in (16, 32, 64)])
        s = np.polyfit(x, y, 1)[0]
        print(f"K = {K:.4f}: w2 = " + ", ".join(f"L{L} {ws[L][0]:.4f}({ws[L][1]:.4f})" for L in ws) + f"; slope 16-64 {s:.4f} (1/pi^2 = {1/math.pi**2:.4f})")


if __name__ == "__main__":
    main()
