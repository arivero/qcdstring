#!/usr/bin/env python3
"""Correlator of two closed time-like lines (static sources) in 3d Z2
gauge theory at low temperature, by two-level averaging (z2core).

    python3 z2_multilevel.py --beta 0.73 --seed 1 --nout 100

Writes ../results/z2ml_b<beta>_s<seed>.npz with one estimate of C(R)
per outer configuration (both separation directions)."""
import argparse, os, sys, time
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from z2core import Z2Lattice, multilevel_polyakov, FLOP_PER_LINK_UPDATE


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--beta", type=float, required=True)
    ap.add_argument("--Nt", type=int, default=32)
    ap.add_argument("--L", type=int, default=32)
    ap.add_argument("--tau", type=int, default=2)
    ap.add_argument("--nsub", type=int, default=200)
    ap.add_argument("--nout", type=int, default=100)
    ap.add_argument("--between", type=int, default=5, help="outer sweeps between measurements")
    ap.add_argument("--therm", type=int, default=1000)
    ap.add_argument("--Rmax", type=int, default=14)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--tag", default="")
    a = ap.parse_args()
    t0 = time.time()
    lat = Z2Lattice(a.Nt, a.L, a.beta, 1000 + a.seed, frozen_tau=a.tau)
    for _ in range(a.therm):
        lat.sweep()
    C, plaq = [], []
    for i in range(a.nout):
        for _ in range(a.between):
            lat.sweep()
        plaq.append(lat.plaquette())
        C.append(multilevel_polyakov(lat, a.tau, a.nsub, a.Rmax))
        if (i + 1) % 10 == 0:
            print(f"beta {a.beta} seed {a.seed}: {i+1}/{a.nout} outer, {time.time()-t0:.0f} s", flush=True)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results",
                       f"z2ml_b{a.beta:.3f}_s{a.seed}{a.tag}.npz")
    np.savez(out, C=np.array(C), plaq=np.array(plaq), beta=a.beta, Nt=a.Nt, L=a.L, tau=a.tau,
             nsub=a.nsub, between=a.between, therm=a.therm, link_updates=lat.link_updates,
             meas_ops=lat.meas_ops, flop=lat.link_updates * FLOP_PER_LINK_UPDATE + lat.meas_ops,
             seconds=time.time() - t0)
    print("wrote", out)


if __name__ == "__main__":
    main()
