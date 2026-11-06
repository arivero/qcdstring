#!/usr/bin/env python3
"""Section 5 of the 1980 paper: roughening of the Ising interface, the dual of
the Z2 flux tube (Wegner duality, tanh beta = exp(-2K)).

Three-dimensional Ising model on L x L x Lz, periodic in x and y, with the
layer below z = 0 fixed to +1 and the layer above z = Lz-1 fixed to -1, so
that one interface crosses the box. Heat bath on two checkerboard classes.
Height of the interface over (x, y): the number of minus spins in the column.
Width: w^2 = <mean over columns of (h - mean h)^2>.

In the rough phase w^2 grows as ln L with slope 1/(2 pi stiffness); in the
smooth phase it saturates. At the roughening point the slope takes the
universal value 1/pi^2 (the solid-on-solid model mapped onto the
two-dimensional Coulomb gas: Chui and Weeks 1976; Kosterlitz and Thouless
1973; van Beijeren 1977).

    python3 ising_interface.py        # 36 runs in parallel; writes ../results/ising_interface.json
"""
import json, os, sys, time
from multiprocessing import Pool
import numpy as np

FLOP_PER_SPIN_UPDATE = 10
KS = [0.30, 0.35, 0.38, 0.40, 0.41, 0.42, 0.45, 0.50, 0.60]
LS = {8: (2000, 8000), 16: (3000, 12000), 32: (4000, 16000), 64: (5000, 20000)}
LZ = 24
EVERY = 10


def run(args):
    K, L = args
    therm, meas = LS[L]
    rng = np.random.default_rng(int(1e5 * K) + L)
    S = np.ones((L, L, LZ + 2), dtype=np.int8)
    S[:, :, LZ // 2 + 1:] = -1                       # flat interface in the middle
    S[:, :, 0], S[:, :, -1] = 1, -1                   # fixed layers
    idx = np.indices((L, L, LZ))
    masks = [((idx[0] + idx[1] + idx[2]) % 2 == p) for p in (0, 1)]
    ptab = 1.0 / (1.0 + np.exp(-2.0 * K * np.arange(-6, 7)))
    w2, hbar = [], []
    nupd = 0
    t0 = time.time()
    for sweep in range(therm + meas):
        for m in masks:
            inner = S[:, :, 1:-1]
            nb = (np.roll(inner, 1, 0) + np.roll(inner, -1, 0) + np.roll(inner, 1, 1) + np.roll(inner, -1, 1)
                  + S[:, :, :-2] + S[:, :, 2:]).astype(np.int8)
            p = ptab[nb[m] + 6]
            inner[m] = np.where(rng.random(p.shape) < p, 1, -1).astype(np.int8)
            nupd += int(m.sum())
        if sweep >= therm and (sweep - therm) % EVERY == 0:
            h = (1 - S[:, :, 1:-1]).sum(axis=2) / 2.0
            w2.append(float(h.var()))
            hbar.append(float(h.mean()))
    return {"K": K, "L": L, "Lz": LZ, "therm": therm, "meas": meas, "every": EVERY, "w2": w2, "hbar": hbar,
            "flop": nupd * FLOP_PER_SPIN_UPDATE, "seconds": time.time() - t0}


def main():
    jobs = sorted([(K, L) for K in KS for L in LS], key=lambda j: -j[1])
    with Pool(min(16, len(jobs))) as pool:
        res = pool.map(run, jobs)
    json.dump(res, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results", "ising_interface.json"), "w"))
    for r in sorted(res, key=lambda r: (r["K"], r["L"])):
        w = np.array(r["w2"])
        print(f"K {r['K']:.2f} L {r['L']:3d}: w2 = {w.mean():.4f}  (<h> drifts {np.std(r['hbar']):.2f})  {r['seconds']:.0f} s")


if __name__ == "__main__":
    main()
