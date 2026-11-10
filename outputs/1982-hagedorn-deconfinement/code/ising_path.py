#!/usr/bin/env python3
"""Interface free energy by thermodynamic integration (1982 paper).

For one geometry Nt x Lx x Ly and a grid of couplings K, runs the periodic
and the antiperiodic lattice at every K and stores block means of
S = sum_b eps_b s_i s_j (and of M^2, M^4 for the periodic lattice).

    python3 ising_path.py --Nt 8 --Lx 24 --Ly 12 --grid 0.15:0.20:0.005,0.2025:0.26:0.0025 \
            --nsweep 20000 --name g8

The number of sweeps at a grid point is nsweep times a weight that follows
the fluctuations of S (larger near the critical couplings); see weight().
Writes ../results/path_<name>.npz"""
import argparse, os, sys, time
from multiprocessing import Pool
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from ising_twist import run_point


def parse_grid(spec):
    ks = []
    for part in spec.split(","):
        if ":" in part:
            a, b, h = (float(x) for x in part.split(":"))
            n = int(round((b - a) / h))
            ks.extend(a + h * i for i in range(n + 1))
        else:
            ks.append(float(part))
    return np.array(sorted(set(round(k, 6) for k in ks)))


def weight(K, Kpeak, width):
    """More sweeps where S fluctuates most and decorrelates slowest."""
    return 1.0 + 3.0 * np.exp(-0.5 * ((K - Kpeak) / width) ** 2)


def job(args):
    Nt, Lx, Ly, K, anti, nsweep, therm, seed, blk = args
    S, M, flop = run_point(Nt, Lx, Ly, K, anti, nsweep, therm, seed)
    nb = len(S) // blk
    Sb = S[: nb * blk].reshape(nb, blk).mean(axis=1)
    m = M[: nb * blk].astype(np.float64)
    return (K, anti, Sb, (m ** 2).reshape(nb, blk).mean(axis=1), (m ** 4).reshape(nb, blk).mean(axis=1),
            float(S.var()), flop, nsweep)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--Nt", type=int, required=True)
    ap.add_argument("--Lx", type=int, required=True)
    ap.add_argument("--Ly", type=int, required=True)
    ap.add_argument("--grid", required=True)
    ap.add_argument("--nsweep", type=int, default=20000, help="sweeps at weight 1")
    ap.add_argument("--Kpeak", type=float, default=0.2217, help="centre of the extra weight")
    ap.add_argument("--width", type=float, default=0.012)
    ap.add_argument("--blk", type=int, default=100)
    ap.add_argument("--procs", type=int, default=16)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--name", required=True)
    ap.add_argument("--outdir", default=os.path.join(HERE, "..", "results"))
    a = ap.parse_args()
    t0 = time.time()
    Ks = parse_grid(a.grid)
    jobs = []
    for i, K in enumerate(Ks):
        n = int(a.nsweep * weight(K, a.Kpeak, a.width) / a.blk) * a.blk
        for anti in (False, True):
            jobs.append((a.Nt, a.Lx, a.Ly, float(K), anti, n, max(500, n // 10),
                         820000 + 100000 * a.seed + 1000 * a.Nt + 2 * i + int(anti), a.blk))
    jobs.sort(key=lambda j: -j[5])
    with Pool(a.procs) as pool:
        res = pool.map(job, jobs, chunksize=1)
    out = {"Nt": a.Nt, "Lx": a.Lx, "Ly": a.Ly, "K": Ks, "blk": a.blk}
    flop = 0.0
    for K, anti, Sb, m2, m4, var, fl, n in res:
        i = int(np.argmin(np.abs(Ks - K)))
        tag = "A" if anti else "P"
        out[f"S{tag}_{i}"] = Sb
        out[f"var{tag}_{i}"] = var
        out[f"n{tag}_{i}"] = n
        if not anti:
            out[f"m2_{i}"] = m2
            out[f"m4_{i}"] = m4
        flop += fl
    out["flop"] = flop
    out["seconds"] = time.time() - t0
    np.savez(os.path.join(a.outdir, f"path_{a.name}.npz"), **out)
    print(f"wrote path_{a.name}.npz: {len(Ks)} couplings, {flop:.3e} flop, {time.time()-t0:.0f} s", flush=True)


if __name__ == "__main__":
    main()
