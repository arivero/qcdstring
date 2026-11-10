#!/usr/bin/env python3
"""Ground state of a closed flux tube of length Nt in the 3d Z2 gauge
theory (1982 paper), from wall-wall correlators of smeared closed
time-like lines on an Nt x Lx x Ly lattice.

Operators. The time-like links and the y-links are smeared within each
plane x = const (each link receives c times the sum of its two staples in
that plane, then is divided by 1 + 2c); the smeared line is the product of
the smeared time-like links over t; the operator W_k(x) is its sum over y
at smearing level k. Every operator lives in one plane x = const, so the
correlation matrix
    C_kl(dx) = (1/Lx Ly) sum_x W_k(x) W_l(x + dx)
is a sum of exponentials exp(-E_n dx) with positive weights on its
diagonal (transfer matrix along x).

Stored: C in blocks of `--block` measurements; the mean unsmeared line and
the plaquette sum after every measurement.

Writes ../results/z2t_b<beta>_Nt<Nt>_L<Lx>x<Ly>_s<seed>.npz"""
import argparse, os, sys, time
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from z2ft import Z2FT, FLOP_PER_LINK_UPDATE

FLOP_SMEAR_STEP = 16          # per site: 8 products for four staples, 2 x (2 adds + 2 products)


def smear_ty(a, b, n, c=0.5):
    """n smearing steps of the time-like links a and the y-links b within the
    planes x = const. Arrays (Nt, Lx, Ly): t is axis 0, y is axis 2."""
    for _ in range(n):
        up_a = b * np.roll(a, -1, axis=2) * np.roll(b, -1, axis=0)
        b_dn = np.roll(b, 1, axis=2)
        dn_a = b_dn * np.roll(a, 1, axis=2) * np.roll(b_dn, -1, axis=0)
        up_b = a * np.roll(b, -1, axis=0) * np.roll(a, -1, axis=2)
        a_dn = np.roll(a, 1, axis=0)
        dn_b = a_dn * np.roll(b, 1, axis=0) * np.roll(a_dn, -1, axis=2)
        a, b = (a + c * (up_a + dn_a)) / (1 + 2 * c), (b + c * (up_b + dn_b)) / (1 + 2 * c)
    return a, b


def walls(U, levels, c=0.5):
    """W[k, x]: wall sums of the smeared lines at the smearing levels given."""
    a, b = U[0].astype(np.float64), U[2].astype(np.float64)
    W, done = [], 0
    for n in levels:
        a, b = smear_ty(a, b, n - done, c)
        done = n
        W.append(a.prod(axis=0).sum(axis=1))
    return np.array(W)


def corr_matrix(W, X, Ly):
    return np.array([(W[:, None, :] * np.roll(W, -dx, axis=1)[None, :, :]).mean(axis=2) for dx in range(X + 1)]) / Ly


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--beta", type=float, required=True)
    ap.add_argument("--Nt", type=int, required=True)
    ap.add_argument("--Lx", type=int, required=True)
    ap.add_argument("--Ly", type=int, required=True)
    ap.add_argument("--X", type=int, default=10)
    ap.add_argument("--levels", default="0,1,2,4")
    ap.add_argument("--c", type=float, default=0.5)
    ap.add_argument("--every", type=int, default=1)
    ap.add_argument("--block", type=int, default=100)
    ap.add_argument("--nblock", type=int, default=100)
    ap.add_argument("--therm", type=int, default=1000)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--tag", default="")
    ap.add_argument("--outdir", default=os.path.join(HERE, "..", "results"))
    a = ap.parse_args()
    t0 = time.time()
    levels = [int(s) for s in a.levels.split(",")]
    nl, V = len(levels), a.Nt * a.Lx * a.Ly
    lat = Z2FT(a.Nt, a.Lx, a.Ly, a.beta, 82000 + 1000 * a.Nt + a.seed)
    for _ in range(a.therm):
        lat.sweep()
    C, pol, plq = [], [], []
    per_meas = FLOP_SMEAR_STEP * max(levels) * V + 2 * nl * V + (a.X + 1) * nl * nl * a.Lx + 13 * V
    for i in range(a.nblock):
        acc = np.zeros((a.X + 1, nl, nl))
        for _ in range(a.block):
            for _ in range(a.every):
                lat.sweep()
            W = walls(lat.U, levels, a.c)
            acc += corr_matrix(W, a.X, a.Ly)
            pol.append(float(lat.polyakov().mean()))
            plq.append(lat.plaquette_sum())
            lat.meas_ops += per_meas
        C.append(acc / a.block)
    flop = lat.link_updates * FLOP_PER_LINK_UPDATE + lat.meas_ops
    name = f"z2t_b{a.beta:.4f}_Nt{a.Nt}_L{a.Lx}x{a.Ly}_s{a.seed}{a.tag}.npz"
    np.savez(os.path.join(a.outdir, name), C=np.array(C), pol=np.array(pol), plq=np.array(plq), beta=a.beta,
             Nt=a.Nt, Lx=a.Lx, Ly=a.Ly, X=a.X, levels=np.array(levels), c=a.c, every=a.every, block=a.block,
             nblock=a.nblock, therm=a.therm, link_updates=lat.link_updates, meas_ops=lat.meas_ops, flop=flop,
             seconds=time.time() - t0)
    print(f"wrote {name}: {flop:.3e} flop, {time.time()-t0:.0f} s", flush=True)


if __name__ == "__main__":
    main()
