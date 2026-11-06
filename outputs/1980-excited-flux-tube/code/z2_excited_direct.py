#!/usr/bin/env python3
"""Third production for the 1980 paper (Response, Major 1): conventional
generalized Wilson loops at T = 0..7 (no frozen slices), with a basis of
distinct operators in the channel of one transverse phonon.

(+,+): straight path, smeared 2 and 4 times.
(-,+): sum_j w_j [B+(j) - B-(j)] with
   O1: w = sin(pi(j+1/2)/R), bump height 1      (a1+)
   O2: the same with bump height 2
   O3: the same with bump height 3             (larger transverse excursions, a1+^3)
   O4: w = sin(3 pi(j+1/2)/R), bump height 1    (a3+)
all from links smeared twice (O1-O4) in their time slice.
Correlators C_ab(R, T) averaged over all slices, positions and both
directions; saved as averages over blocks of 20 configurations.
Writes ../results/z2d_b<beta>_s<seed>.npz."""
import argparse, os, sys, time
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "1976-flux-tube-casimir", "code"))
from z2core import Z2Lattice, FLOP_PER_LINK_UPDATE


def smear3(Sx, Sy, n, c=0.5):
    """smear_slice of z2_excited.py applied to all time slices at once; arrays (Nt, L, L)."""
    for _ in range(n):
        up_x = Sy * np.roll(Sx, -1, axis=2) * np.roll(Sy, -1, axis=1)
        dn_x = np.roll(Sy, 1, axis=2) * np.roll(Sx, 1, axis=2) * np.roll(np.roll(Sy, 1, axis=2), -1, axis=1)
        up_y = Sx * np.roll(Sy, -1, axis=1) * np.roll(Sx, -1, axis=2)
        dn_y = np.roll(Sx, 1, axis=1) * np.roll(Sy, 1, axis=1) * np.roll(np.roll(Sx, 1, axis=1), -1, axis=2)
        Sx, Sy = (Sx + c * (up_x + dn_x)) / (1 + 2 * c), (Sy + c * (up_y + dn_y)) / (1 + 2 * c)
    return Sx, Sy


def operators(S2x, S2y, S4x, S4y, Rmax):
    """pp: (Rmax, 2dir, 2, Nt, L, L); mp: (Rmax, 2dir, 4, Nt, L, L)."""
    Nt, L, _ = S2x.shape
    pp = np.zeros((Rmax, 2, 2, Nt, L, L))
    mp = np.zeros((Rmax, 2, 4, Nt, L, L))
    for d in (0, 1):
        ax_e, ax_p = 1 + d, 2 - d
        sh = lambda f, ke, kp: np.roll(np.roll(f, -ke, axis=ax_e), -kp, axis=ax_p)
        for k, (Sx, Sy) in enumerate(((S2x, S2y), (S4x, S4y))):
            Se = Sx if d == 0 else Sy
            P = np.ones((Nt, L, L))
            for R in range(1, Rmax + 1):
                P = P * sh(Se, R - 1, 0)
                pp[R - 1, d, k] = P
        Se, Sp = (S2x, S2y) if d == 0 else (S2y, S2x)
        P = [np.ones((Nt, L, L))]
        for n in range(1, Rmax + 1):
            P.append(P[-1] * sh(Se, n - 1, 0))
        def vert(xe, h, sign):
            v = np.ones((Nt, L, L))
            for m in range(h):
                v = v * (sh(Sp, xe, m) if sign > 0 else sh(Sp, xe, -m - 1))
            return v
        for R in range(2, Rmax + 1):
            diff = {}
            for h in (1, 2, 3):
                diff[h] = []
                for j in range(R):
                    up = vert(j, h, +1) * sh(Se, j, h) * vert(j + 1, h, +1)
                    dn = vert(j, h, -1) * sh(Se, j, -h) * vert(j + 1, h, -1)
                    diff[h].append(P[j] * (up - dn) * sh(P[R - j - 1], j + 1, 0))
            w1 = [np.sin(np.pi * (j + 0.5) / R) for j in range(R)]
            w3 = [np.sin(3 * np.pi * (j + 0.5) / R) for j in range(R)]
            for k, h in enumerate((1, 2, 3)):
                mp[R - 1, d, k] = sum(w1[j] * diff[h][j] for j in range(R))
            mp[R - 1, d, 3] = sum(w3[j] * diff[1][j] for j in range(R))
    return pp, mp


def correlators(U, pp, mp, Rmax, Tmax):
    Nt, L = U.shape[1], U.shape[2]
    U0 = U[0].astype(np.float64)
    Cpp = np.zeros((Tmax + 1, Rmax, 2, 2))
    Cmp = np.zeros((Tmax + 1, Rmax, 4, 4))
    line = np.ones((Nt, L, L))
    for T in range(Tmax + 1):
        if T > 0:
            line = line * np.roll(U0, -(T - 1), axis=0)
        for d in (0, 1):
            ax = 1 + d
            for R in range(1, Rmax + 1):
                lines = line * np.roll(line, -R, axis=ax)
                a = pp[R - 1, d] * lines                       # (2, Nt, L, L)
                b = np.roll(pp[R - 1, d], -T, axis=1)
                Cpp[T, R - 1] += np.einsum("atxy,btxy->ab", a, b) / (2 * Nt * L * L)
                if R >= 2:
                    a = mp[R - 1, d] * lines
                    b = np.roll(mp[R - 1, d], -T, axis=1)
                    Cmp[T, R - 1] += np.einsum("atxy,btxy->ab", a, b) / (2 * Nt * L * L)
    return Cpp, Cmp


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--beta", type=float, required=True)
    ap.add_argument("--Nt", type=int, default=24)
    ap.add_argument("--L", type=int, default=24)
    ap.add_argument("--nconf", type=int, default=1000)
    ap.add_argument("--between", type=int, default=5)
    ap.add_argument("--therm", type=int, default=800)
    ap.add_argument("--Rmax", type=int, default=9)
    ap.add_argument("--Tmax", type=int, default=7)
    ap.add_argument("--block", type=int, default=20)
    ap.add_argument("--seed", type=int, default=1)
    a = ap.parse_args()
    t0 = time.time()
    lat = Z2Lattice(a.Nt, a.L, a.beta, 12000 + a.seed)
    for _ in range(a.therm):
        lat.sweep()
    Bpp, Bmp = [], []
    acc_pp = acc_mp = None
    nops = 0
    for i in range(a.nconf):
        for _ in range(a.between):
            lat.sweep()
        U = lat.U
        S2x, S2y = smear3(U[1].astype(float), U[2].astype(float), 2)
        S4x, S4y = smear3(S2x, S2y, 2)
        pp, mp = operators(S2x, S2y, S4x, S4y, a.Rmax)
        Cpp, Cmp = correlators(U, pp, mp, a.Rmax, a.Tmax)
        nops += (a.Rmax ** 2 * 120 + a.Rmax * (a.Tmax + 1) * 2 * 30) * a.Nt * a.L * a.L
        acc_pp = Cpp if acc_pp is None else acc_pp + Cpp
        acc_mp = Cmp if acc_mp is None else acc_mp + Cmp
        if (i + 1) % a.block == 0:
            Bpp.append(acc_pp / a.block); Bmp.append(acc_mp / a.block)
            acc_pp = acc_mp = None
        if (i + 1) % 100 == 0:
            print(f"beta {a.beta} seed {a.seed}: {i+1}/{a.nconf}, {time.time()-t0:.0f} s", flush=True)
    lat.meas_ops += nops
    out = os.path.join(HERE, "..", "results", f"z2d_b{a.beta:.3f}_s{a.seed}.npz")
    np.savez(out, Cpp=np.array(Bpp), Cmp=np.array(Bmp), beta=a.beta, Nt=a.Nt, L=a.L, nconf=a.nconf, block=a.block,
             between=a.between, link_updates=lat.link_updates, meas_ops=lat.meas_ops,
             flop=lat.link_updates * FLOP_PER_LINK_UPDATE + lat.meas_ops, seconds=time.time() - t0)
    print("wrote", out)


if __name__ == "__main__":
    main()
