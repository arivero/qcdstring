#!/usr/bin/env python3
"""Wall-wall correlator of closed time-like lines in the 3d Z2 gauge theory
on an Nt x Lx x Ly lattice (1982 paper): the ground state of a closed flux
tube of length Nt.

Two modes:
  --slabs 4,4      two-level averaging with frozen slices at the slab
                   boundaries (z2ft.two_level_wall); one estimate of G(dx)
                   per frozen configuration.
  (no --slabs)     plain measurement after every `--every` sweeps; block
                   averages over `--block` measurements are stored.
Every run also stores the time series of the mean Polyakov line and of the
plaquette sum.

Writes ../results/z2w_b<beta>_Nt<Nt>_L<Lx>x<Ly>_s<seed>.npz"""
import argparse, os, sys, time
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from z2ft import Z2FT, wall_corr_plain, two_level_wall, FLOP_PER_LINK_UPDATE


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--beta", type=float, required=True)
    ap.add_argument("--Nt", type=int, required=True)
    ap.add_argument("--Lx", type=int, required=True)
    ap.add_argument("--Ly", type=int, required=True)
    ap.add_argument("--X", type=int, default=12)
    ap.add_argument("--slabs", default="")
    ap.add_argument("--nsub", type=int, default=100)
    ap.add_argument("--nout", type=int, default=100, help="frozen configurations (two-level) or blocks (plain)")
    ap.add_argument("--between", type=int, default=5, help="full sweeps between frozen configurations")
    ap.add_argument("--every", type=int, default=1, help="plain mode: sweeps between measurements")
    ap.add_argument("--block", type=int, default=100, help="plain mode: measurements per stored block")
    ap.add_argument("--therm", type=int, default=1000)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--tag", default="")
    ap.add_argument("--outdir", default=os.path.join(HERE, "..", "results"))
    a = ap.parse_args()
    t0 = time.time()
    slabs = [int(s) for s in a.slabs.split(",")] if a.slabs else None
    lat = Z2FT(a.Nt, a.Lx, a.Ly, a.beta, 82000 + 1000 * a.Nt + a.seed, slabs=slabs)
    for _ in range(a.therm):
        lat.sweep()
    G, pol, plq = [], [], []
    if slabs:
        for i in range(a.nout):
            for _ in range(a.between):
                lat.sweep()
            pol.append(float(lat.polyakov().mean())); plq.append(lat.plaquette_sum())
            G.append(two_level_wall(lat, a.nsub, a.X))
    else:
        for i in range(a.nout):
            acc = np.zeros(a.X + 1)
            for _ in range(a.block):
                for _ in range(a.every):
                    lat.sweep()
                P = lat.polyakov()
                acc += wall_corr_plain(P, a.X)
                pol.append(float(P.mean())); plq.append(lat.plaquette_sum())
                lat.meas_ops += a.Nt * a.Lx * a.Ly + (a.X + 1) * a.Lx + 3 * 4 * a.Nt * a.Lx * a.Ly
            G.append(acc / a.block)
    name = f"z2w_b{a.beta:.4f}_Nt{a.Nt}_L{a.Lx}x{a.Ly}_s{a.seed}{a.tag}.npz"
    np.savez(os.path.join(a.outdir, name), G=np.array(G), pol=np.array(pol), plq=np.array(plq), beta=a.beta,
             Nt=a.Nt, Lx=a.Lx, Ly=a.Ly, X=a.X, slabs=np.array(slabs if slabs else []), nsub=a.nsub,
             nout=a.nout, between=a.between, every=a.every, block=a.block, therm=a.therm,
             link_updates=lat.link_updates, meas_ops=lat.meas_ops,
             flop=lat.link_updates * FLOP_PER_LINK_UPDATE + lat.meas_ops, seconds=time.time() - t0)
    print(f"wrote {name}: {lat.link_updates * FLOP_PER_LINK_UPDATE + lat.meas_ops:.3e} flop, {time.time()-t0:.0f} s", flush=True)


if __name__ == "__main__":
    main()
