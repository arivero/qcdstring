#!/usr/bin/env python3
"""Excited levels of the Z2 flux tube in three dimensions (1980 paper).

Generalized Wilson loops: a spatial operator O_c at a frozen time slice
t_b, two time-like lines at the source positions x0 and x0 + R e, and
the same operator at t_b + T. The time-like lines are averaged slab by
slab with the two-level method of the 1976 paper (slabs of 4, frozen
space-like links on every fourth slice); the spatial operators live on
the frozen slices, so they factor out of the slab averages.

Operators (all built from smeared space-like links of the slice):
  (+,+)  straight path                       ground state, n = 0
  (-,+)  sum_j w1_j [B+(j) - B-(j)]           n = 1 (one phonon, mode 1)
  (-,-)  sum_j w2_j [B+(j) - B-(j)]           n = 2 (one phonon, mode 2)
  (+,-)  sum_j w2_j [B+(j) + B-(j)]           n = 3 (modes 1 and 2)
B+-(j) is the path with a unit bump towards +-e_perp over the link from
x0 + j e to x0 + (j+1) e; w1_j = sin(pi (j+1/2)/R), w2_j = sin(2 pi (j+1/2)/R): the profiles of the
first and second phonon of a string with fixed ends. The first label is the
reflection e_perp -> -e_perp through the axis, the second the reflection
that exchanges the sources.

    python3 z2_excited.py --beta 0.73 --seed 1 --nout 100
"""
import argparse, os, sys, time
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "1976-flux-tube-casimir", "code"))
from z2core import Z2Lattice, FLOP_PER_LINK_UPDATE   # 1976 update routine

CHANNELS = ("pp", "mp", "mm", "pm")


def smear_slice(Sx, Sy, n, c):
    """Real-valued smearing of the two space-like link fields of one slice
    (arrays (L, L) indexed [x, y]); each step adds c times the two staples
    in the slice and divides by 1 + 2c."""
    for _ in range(n):
        up_x = Sy * np.roll(Sx, -1, axis=1) * np.roll(Sy, -1, axis=0)
        dn_x = np.roll(Sy, 1, axis=1) * np.roll(Sx, 1, axis=1) * np.roll(np.roll(Sy, 1, axis=1), -1, axis=0)
        up_y = Sx * np.roll(Sy, -1, axis=0) * np.roll(Sx, -1, axis=1)
        dn_y = np.roll(Sx, 1, axis=0) * np.roll(Sy, 1, axis=0) * np.roll(np.roll(Sx, 1, axis=0), -1, axis=1)
        Sx, Sy = (Sx + c * (up_x + dn_x)) / (1 + 2 * c), (Sy + c * (up_y + dn_y)) / (1 + 2 * c)
    return Sx, Sy


def slice_operators(Sx, Sy, Rmax):
    """O[c][R-1, d] arrays (L, L): operators for sources at x0 and x0 + R e_d,
    d = 0 (e = x) or 1 (e = y)."""
    L = Sx.shape[0]
    ops = {c: np.zeros((Rmax, 2, L, L)) for c in CHANNELS}
    for d in (0, 1):
        Se, Sp = (Sx, Sy) if d == 0 else (Sy, Sx)
        ax_e, ax_p = d, 1 - d
        # straight products P[n](x) = prod_{k<n} Se(x + k e)
        P = [np.ones((L, L))]
        for n in range(1, Rmax + 1):
            P.append(P[-1] * np.roll(Se, -(n - 1), axis=ax_e))
        sh = lambda f, ke, kp: np.roll(np.roll(f, -ke, axis=ax_e), -kp, axis=ax_p)
        for R in range(1, Rmax + 1):
            ops["pp"][R - 1, d] = P[R]
            if R < 2:
                continue
            Bp, Bm = [], []
            for j in range(R):
                head = P[j]                                       # x0 -> x0 + j e
                tail = sh(P[R - j - 1], j + 1, 0)                 # x0 + (j+1) e -> x0 + R e
                # up: link Sp at x0+je, Se at x0+je+p, link Sp at x0+(j+1)e
                up = sh(Sp, j, 0) * sh(Se, j, 1) * sh(Sp, j + 1, 0)
                # down: link Sp at x0+je-p, Se at x0+je-p, Sp at x0+(j+1)e-p
                dn = sh(Sp, j, -1) * sh(Se, j, -1) * sh(Sp, j + 1, -1)
                Bp.append(head * up * tail)
                Bm.append(head * dn * tail)
            # weights: the k-th phonon of a string with fixed ends has profile sin(k pi x / R)
            w1 = [np.sin(np.pi * (j + 0.5) / R) for j in range(R)]
            w2 = [np.sin(2 * np.pi * (j + 0.5) / R) for j in range(R)]
            ops["mp"][R - 1, d] = sum(w1[j] * (Bp[j] - Bm[j]) for j in range(R))
            ops["mm"][R - 1, d] = sum(w2[j] * (Bp[j] - Bm[j]) for j in range(R))
            ops["pm"][R - 1, d] = sum(w2[j] * (Bp[j] + Bm[j]) for j in range(R))
    return ops


def measure(lat, tau, n_sub, Rmax, n_smear, c_smear, Tlist):
    """One outer configuration: operators on every frozen slice, slab
    averages of two-line products, and the correlators."""
    Nt, L = lat.Nt, lat.L
    nslab = Nt // tau
    U = lat.U
    # operators on frozen slices (their links do not change during the sub-updates)
    OPS = []
    for k in range(nslab):
        t = k * tau
        Sx, Sy = smear_slice(U[1][t].astype(float), U[2][t].astype(float), n_smear, c_smear)
        OPS.append(slice_operators(Sx, Sy, Rmax))
    lat.meas_ops += nslab * (n_smear * 40 + Rmax * Rmax * 30) * L * L
    # slab averages A[k, R-1, d, x, y]
    acc = np.zeros((nslab, Rmax, 2, L, L))
    for _ in range(n_sub):
        lat.sweep(frozen=True)
        Lk = U[0].reshape(nslab, tau, L, L).prod(axis=1, dtype=np.int8).astype(np.float64)
        for R in range(1, Rmax + 1):
            acc[:, R - 1, 0] += Lk * np.roll(Lk, -R, axis=1)
            acc[:, R - 1, 1] += Lk * np.roll(Lk, -R, axis=2)
        lat.meas_ops += 4 * Rmax * nslab * L * L + Nt * L * L
    A = acc / n_sub
    # correlators C[c][T][R-1] averaged over start slice, position and direction
    out = {c: np.zeros((len(Tlist), Rmax)) for c in CHANNELS}
    for it, T in enumerate(Tlist):
        nk = T // tau
        for k0 in range(nslab):
            prodA = np.ones((Rmax, 2, L, L))
            for m in range(nk):
                prodA = prodA * A[(k0 + m) % nslab]
            k1 = (k0 + nk) % nslab
            for c in CHANNELS:
                out[c][it] += (OPS[k0][c] * prodA * OPS[k1][c]).mean(axis=(1, 2, 3))
        for c in CHANNELS:
            out[c][it] /= nslab
        lat.meas_ops += nslab * (nk + 8) * Rmax * 2 * L * L
    # Polyakov-loop correlator (all slabs) for comparison with 1976
    poly = A.prod(axis=0).mean(axis=(1, 2, 3))
    return out, poly


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--beta", type=float, required=True)
    ap.add_argument("--Nt", type=int, default=24)
    ap.add_argument("--L", type=int, default=24)
    ap.add_argument("--tau", type=int, default=4)
    ap.add_argument("--nsub", type=int, default=500)
    ap.add_argument("--nout", type=int, default=100)
    ap.add_argument("--between", type=int, default=20)
    ap.add_argument("--therm", type=int, default=800)
    ap.add_argument("--Rmax", type=int, default=10)
    ap.add_argument("--nsmear", type=int, default=4)
    ap.add_argument("--csmear", type=float, default=0.5)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--tag", default="")
    a = ap.parse_args()
    Tlist = list(range(a.tau, a.Nt // 2 + 1, a.tau))
    t0 = time.time()
    lat = Z2Lattice(a.Nt, a.L, a.beta, 5000 + a.seed, frozen_tau=a.tau)
    for _ in range(a.therm):
        lat.sweep()
    res = {c: [] for c in CHANNELS}
    poly = []
    for i in range(a.nout):
        for _ in range(a.between):
            lat.sweep()
        o, p = measure(lat, a.tau, a.nsub, a.Rmax, a.nsmear, a.csmear, Tlist)
        for c in CHANNELS:
            res[c].append(o[c])
        poly.append(p)
        if (i + 1) % 10 == 0:
            print(f"beta {a.beta} seed {a.seed}: {i+1}/{a.nout}, {time.time()-t0:.0f} s", flush=True)
    out = os.path.join(HERE, "..", "results", f"z2x_b{a.beta:.3f}_s{a.seed}{a.tag}.npz")
    np.savez(out, **{f"C_{c}": np.array(res[c]) for c in CHANNELS}, poly=np.array(poly), Tlist=np.array(Tlist),
             beta=a.beta, Nt=a.Nt, L=a.L, tau=a.tau, nsub=a.nsub, nsmear=a.nsmear, csmear=a.csmear,
             link_updates=lat.link_updates, meas_ops=lat.meas_ops,
             flop=lat.link_updates * FLOP_PER_LINK_UPDATE + lat.meas_ops, seconds=time.time() - t0)
    print("wrote", out)


if __name__ == "__main__":
    main()
