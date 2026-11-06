#!/usr/bin/env python3
"""Z2 lattice gauge theory in three dimensions by heat-bath Monte Carlo
(idea 004, prediction P11, P13).

Links U_mu(x) = +/-1 on an L^3 periodic lattice, action S = -beta sum_P U_P.
Measures Wilson loops W(R,T), Creutz ratios chi(R,T), and compares the
string tension with the leading strong-coupling result -ln tanh(beta)
and with the dual 3d Ising model (tanh beta = exp(-2 K)). Confinement for
beta < beta_c = 0.7613; the Wilson surface roughens near beta ~ 0.47.

Needs numpy. A 12^3 lattice with 200 sweeps takes well under a minute.

    python3 z2_lattice.py --beta 0.5 --L 12 --therm 100 --meas 100
    python3 z2_lattice.py --scan            # beta = 0.3 ... 0.7
"""
import argparse
import math
import sys

try:
    import numpy as np
except ImportError:
    sys.exit("numpy is needed: pip install numpy")


def staples(U, mu):
    """Sum over the 4 staples (3d) attached to each mu-link."""
    S = np.zeros(U.shape[1:], dtype=np.float64)
    Umu = U[mu]
    for nu in range(3):
        if nu == mu:
            continue
        Unu = U[nu]
        fwd = np.roll(Unu, -1, axis=mu) * np.roll(Umu, -1, axis=nu) * Unu
        bwd = np.roll(np.roll(Unu, -1, axis=mu), 1, axis=nu) * np.roll(Umu, 1, axis=nu) * np.roll(Unu, 1, axis=nu)
        S += fwd + bwd
    return S


def sweep(U, beta, rng, masks):
    for mu in range(3):
        for parity in (0, 1):
            S = staples(U, mu)
            p_plus = 1.0 / (1.0 + np.exp(-2.0 * beta * S))
            new = np.where(rng.random(S.shape) < p_plus, 1, -1)
            m = masks[mu][parity]
            U[mu][m] = new[m]


def line(U, mu, n):
    P = np.ones(U.shape[1:], dtype=np.int8)
    for k in range(n):
        P = P * np.roll(U[mu], -k, axis=mu)
    return P


def wilson(U, R, T):
    vals = []
    for mu in range(3):
        for nu in range(mu + 1, 3):
            Lm, Ln = line(U, mu, R), line(U, nu, T)
            vals.append((Lm * np.roll(Ln, -R, axis=mu) * np.roll(Lm, -T, axis=nu) * Ln).mean())
            Lm2, Ln2 = line(U, mu, T), line(U, nu, R)
            vals.append((Ln2 * np.roll(Lm2, -R, axis=nu) * np.roll(Ln2, -T, axis=mu) * Lm2).mean())
    return float(np.mean(vals))


def run(beta, L, therm, meas, rmax, seed, verbose=True):
    rng = np.random.default_rng(seed)
    U = np.ones((3, L, L, L), dtype=np.int8)  # cold start
    idx = np.indices((L, L, L))
    masks = []
    for mu in range(3):
        perp = sum(idx[nu] for nu in range(3) if nu != mu) % 2
        masks.append([perp == 0, perp == 1])
    for _ in range(therm):
        sweep(U, beta, rng, masks)
    sizes = [(R, T) for R in range(1, rmax + 1) for T in range(1, rmax + 1) if T >= R]
    samples = {s: [] for s in sizes}
    for _ in range(meas):
        sweep(U, beta, rng, masks)
        for s in sizes:
            samples[s].append(wilson(U, *s))
    W = {s: (np.mean(v), np.std(v, ddof=1) / math.sqrt(len(v))) for s, v in samples.items()}

    def chi(R, T, arr=None):
        key = lambda s: (min(s), max(s))  # W(R,T) = W(T,R); only T >= R is stored
        g = (lambda s: np.mean(samples[key(s)])) if arr is None else (lambda s: np.mean(np.array(samples[key(s)])[arr]))
        num = g((R, T)) * g((R - 1, T - 1))
        den = g((R, T - 1)) * g((R - 1, T))
        return -math.log(num / den) if num > 0 and den > 0 else float("nan")

    sc = -math.log(math.tanh(beta))
    kdual = -0.5 * math.log(math.tanh(beta))
    if verbose:
        print(f"\nbeta = {beta}, L = {L}, {therm} thermalisation + {meas} measurement sweeps")
        print(f"  plaquette <U_P> = {W[(1, 1)][0]:.4f} +/- {W[(1, 1)][1]:.4f}   (strong coupling: tanh beta = {math.tanh(beta):.4f})")
        print("  Wilson loops W(R,T):")
        for s in sizes:
            print(f"    W({s[0]},{s[1]}) = {W[s][0]:9.5f} +/- {W[s][1]:.5f}")
        print("  Creutz ratios chi(R,R) ~ sigma a^2 (errors by bootstrap over measurements):")
    out = {}
    nb = 200
    for R in range(2, rmax + 1):
        boots = []
        for _ in range(nb):
            arr = rng.integers(0, meas, meas)
            boots.append(chi(R, R, arr))
        boots = [b for b in boots if not math.isnan(b)]
        c = chi(R, R)
        err = np.std(boots) if boots else float("nan")
        out[R] = (c, err)
        if verbose:
            print(f"    chi({R},{R}) = {c:7.4f} +/- {err:.4f}")
    if verbose:
        print(f"  leading strong coupling: sigma a^2 = -ln tanh beta = {sc:.4f};  dual Ising coupling K* = {kdual:.4f}"
              f"  (Ising K_c = 0.2217 <-> beta_c = 0.7613)")
    return W, out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--beta", type=float, default=0.5)
    ap.add_argument("--L", type=int, default=12)
    ap.add_argument("--therm", type=int, default=100)
    ap.add_argument("--meas", type=int, default=100)
    ap.add_argument("--rmax", type=int, default=3)
    ap.add_argument("--seed", type=int, default=1974)
    ap.add_argument("--scan", action="store_true", help="beta scan 0.3..0.7, compact output")
    a = ap.parse_args()
    if a.scan:
        print(f"{'beta':>5s} {'chi(2,2)':>16s} {'chi(3,3)':>16s} {'-ln tanh':>9s}")
        for beta in (0.3, 0.4, 0.5, 0.6, 0.7):
            _, out = run(beta, a.L, a.therm, a.meas, max(a.rmax, 3), a.seed, verbose=False)
            print(f"{beta:5.2f} {out[2][0]:8.4f}+/-{out[2][1]:6.4f} {out[3][0]:8.4f}+/-{out[3][1]:6.4f} {-math.log(math.tanh(beta)):9.4f}")
    else:
        run(a.beta, a.L, a.therm, a.meas, a.rmax, a.seed)


if __name__ == "__main__":
    main()
