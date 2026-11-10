#!/usr/bin/env python3
"""The Ising film dual to the gauge theory at finite temperature (1982 paper):
periodic Nt x L x L lattice at coupling K, time series of the magnetization M
and of the bond sum S after every sweep. The film orders at K_c(Nt), the dual
of the deconfinement coupling beta_c(Nt); analyze82.py finds it from the
crossing of the cumulant 1 - <M^4>/3<M^2>^2 [Binder 1981] for different L,
reweighting each series in K with exp((K' - K) S).

    python3 ising_film.py --Nt 4 --L 32 --K 0.2361 --nsweep 25000 --chains 8

Writes ../results/film_Nt<Nt>_L<L>_K<K>.npz (chains stacked)."""
import argparse, os, sys, time
from multiprocessing import Pool
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from ising_twist import run_point


def job(args):
    Nt, L, K, nsweep, therm, seed, hot = args
    S, M, flop = run_point(Nt, L, L, K, False, nsweep, therm, seed, hot=hot)
    return S, M, flop


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--Nt", type=int, required=True)
    ap.add_argument("--L", type=int, required=True)
    ap.add_argument("--K", type=float, required=True)
    ap.add_argument("--nsweep", type=int, required=True, help="sweeps per chain")
    ap.add_argument("--therm", type=int, default=0, help="default: nsweep/8")
    ap.add_argument("--chains", type=int, default=8)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--tag", default="")
    ap.add_argument("--outdir", default=os.path.join(HERE, "..", "results"))
    a = ap.parse_args()
    t0 = time.time()
    therm = a.therm or a.nsweep // 8
    jobs = [(a.Nt, a.L, a.K, a.nsweep, therm, 824000 + 10000 * a.Nt + 100 * a.L + 10 * a.seed + c, bool(c % 2))
            for c in range(a.chains)]            # hot and cold starts alternate
    with Pool(min(a.chains, 16)) as pool:
        res = pool.map(job, jobs)
    name = f"film_Nt{a.Nt}_L{a.L}_K{a.K:.4f}{a.tag}.npz"
    flop = sum(r[2] for r in res)
    np.savez_compressed(os.path.join(a.outdir, name), S=np.array([r[0] for r in res], dtype=np.int32), M=np.array([r[1] for r in res], dtype=np.int32),
             Nt=a.Nt, L=a.L, K=a.K, nsweep=a.nsweep, therm=therm, flop=flop, seconds=time.time() - t0)
    print(f"wrote {name}: {flop:.3e} flop, {time.time()-t0:.0f} s", flush=True)


if __name__ == "__main__":
    main()
