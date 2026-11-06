#!/usr/bin/env python3
"""Second production for the 1980 paper: correlation matrices of two
operators per channel, for a variational (generalized eigenvalue) analysis.

Operators in each channel (built as in z2_excited.py, two smearing steps):
  pp:  straight path, smeared 2 and 4 times
  mp:  sum_j w1_j [B+(j) - B-(j)] with bump heights 1 and 2
  mm:  sum_j w2_j [B+(j) - B-(j)] with bump heights 1 and 2
Correlators C_ab(T) for T = 0, 4, 8, 12 (T = 0: both operators on the same
frozen slice). Writes ../results/z2g_b<beta>_s<seed>.npz."""
import argparse, os, sys, time
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "..", "1976-flux-tube-casimir", "code"))
from z2core import Z2Lattice, FLOP_PER_LINK_UPDATE
from z2_excited import smear_slice

CH = ("pp", "mp", "mm")


def ops_slice(Sx2, Sy2, Sx4, Sy4, Rmax):
    """O[c] array (Rmax, 2 directions, 2 operators, L, L)."""
    L = Sx2.shape[0]
    O = {c: np.zeros((Rmax, 2, 2, L, L)) for c in CH}
    for d in (0, 1):
        sh = lambda f, ke, kp: np.roll(np.roll(f, -ke, axis=d), -kp, axis=1 - d)
        for k, (Sx, Sy) in enumerate(((Sx2, Sy2), (Sx4, Sy4))):
            Se = Sx if d == 0 else Sy
            P = [np.ones((L, L))]
            for n in range(1, Rmax + 1):
                P.append(P[-1] * np.roll(Se, -(n - 1), axis=d))
            for R in range(1, Rmax + 1):
                O["pp"][R - 1, d, k] = P[R]
        Se, Sp = (Sx2, Sy2) if d == 0 else (Sy2, Sx2)
        P = [np.ones((L, L))]
        for n in range(1, Rmax + 1):
            P.append(P[-1] * np.roll(Se, -(n - 1), axis=d))
        # vertical strings of height h above (+) and below (-) a site
        def vert(x_e, h, sign):
            v = np.ones((L, L))
            for m in range(h):
                v = v * (sh(Sp, x_e, m) if sign > 0 else sh(Sp, x_e, -m - 1))
            return v
        for R in range(2, Rmax + 1):
            w1 = [np.sin(np.pi * (j + 0.5) / R) for j in range(R)]
            w2 = [np.sin(2 * np.pi * (j + 0.5) / R) for j in range(R)]
            for k, h in enumerate((1, 2)):
                acc1 = np.zeros((L, L)); acc2 = np.zeros((L, L))
                for j in range(R):
                    head = P[j]
                    tail = sh(P[R - j - 1], j + 1, 0)
                    up = vert(j, h, +1) * sh(Se, j, h) * vert(j + 1, h, +1)
                    dn = vert(j, h, -1) * sh(Se, j, -h) * vert(j + 1, h, -1)
                    diff = head * (up - dn) * tail
                    acc1 += w1[j] * diff
                    acc2 += w2[j] * diff
                O["mp"][R - 1, d, k] = acc1
                O["mm"][R - 1, d, k] = acc2
    return O


def measure(lat, tau, n_sub, Rmax):
    Nt, L = lat.Nt, lat.L
    nslab = Nt // tau
    U = lat.U
    OPS = []
    for k in range(nslab):
        t = k * tau
        Sx, Sy = U[1][t].astype(float), U[2][t].astype(float)
        Sx2, Sy2 = smear_slice(Sx, Sy, 2, 0.5)
        Sx4, Sy4 = smear_slice(Sx2, Sy2, 2, 0.5)
        OPS.append(ops_slice(Sx2, Sy2, Sx4, Sy4, Rmax))
    lat.meas_ops += nslab * (200 + 60 * Rmax * Rmax) * L * L
    acc = np.zeros((nslab, Rmax, 2, L, L))
    for _ in range(n_sub):
        lat.sweep(frozen=True)
        Lk = U[0].reshape(nslab, tau, L, L).prod(axis=1, dtype=np.int8).astype(np.float64)
        for R in range(1, Rmax + 1):
            acc[:, R - 1, 0] += Lk * np.roll(Lk, -R, axis=1)
            acc[:, R - 1, 1] += Lk * np.roll(Lk, -R, axis=2)
        lat.meas_ops += 4 * Rmax * nslab * L * L + Nt * L * L
    A = acc / n_sub
    Tlist = list(range(0, Nt // 2 + 1, tau))
    out = {c: np.zeros((len(Tlist), Rmax, 2, 2)) for c in CH}
    for it, T in enumerate(Tlist):
        nk = T // tau
        for k0 in range(nslab):
            prodA = np.ones((Rmax, 2, L, L))
            for m in range(nk):
                prodA = prodA * A[(k0 + m) % nslab]
            k1 = (k0 + nk) % nslab
            for c in CH:
                a = OPS[k0][c]        # (Rmax, 2dir, 2op, L, L)
                b = OPS[k1][c]
                out[c][it] += np.einsum("rdaxy,rdxy,rdbxy->rab", a, prodA, b) / (2 * L * L)
        for c in CH:
            out[c][it] /= nslab
        lat.meas_ops += nslab * (nk + 12) * Rmax * 2 * L * L
    return out, Tlist


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--beta", type=float, required=True)
    ap.add_argument("--Nt", type=int, default=24)
    ap.add_argument("--L", type=int, default=24)
    ap.add_argument("--tau", type=int, default=4)
    ap.add_argument("--nsub", type=int, default=300)
    ap.add_argument("--nout", type=int, default=150)
    ap.add_argument("--between", type=int, default=20)
    ap.add_argument("--therm", type=int, default=800)
    ap.add_argument("--Rmax", type=int, default=10)
    ap.add_argument("--seed", type=int, default=1)
    a = ap.parse_args()
    t0 = time.time()
    lat = Z2Lattice(a.Nt, a.L, a.beta, 9000 + a.seed, frozen_tau=a.tau)
    for _ in range(a.therm):
        lat.sweep()
    res = {c: [] for c in CH}
    for i in range(a.nout):
        for _ in range(a.between):
            lat.sweep()
        o, Tlist = measure(lat, a.tau, a.nsub, a.Rmax)
        for c in CH:
            res[c].append(o[c])
        if (i + 1) % 10 == 0:
            print(f"beta {a.beta} seed {a.seed}: {i+1}/{a.nout}, {time.time()-t0:.0f} s", flush=True)
    out = os.path.join(HERE, "..", "results", f"z2g_b{a.beta:.3f}_s{a.seed}.npz")
    np.savez(out, **{f"C_{c}": np.array(res[c]) for c in CH}, Tlist=np.array(Tlist), beta=a.beta, Nt=a.Nt, L=a.L,
             tau=a.tau, nsub=a.nsub, link_updates=lat.link_updates, meas_ops=lat.meas_ops,
             flop=lat.link_updates * FLOP_PER_LINK_UPDATE + lat.meas_ops, seconds=time.time() - t0)
    print("wrote", out)


if __name__ == "__main__":
    main()
