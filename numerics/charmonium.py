#!/usr/bin/env python3
"""Heavy-quark bound states in V(r) = -kappa/r + sigma r with sigma taken
from the Regge slope (idea 009, prediction P01).

Solves the radial Schroedinger equation by shooting with node counting.
Given kappa and sigma, m_c is tuned so that the 1S level sits at the
mass of the narrow state (3.097 GeV); the 2S, 1P, 1D and 3S levels are
then predictions. Pure Python. Note: the tuned m_c (about 1.37 GeV with
the defaults) is a parameter of this potential without an additive
constant; fits that include a constant quote a heavier quark mass.

    python3 charmonium.py                # defaults: kappa 0.52, alpha' 0.88
    python3 charmonium.py --kappa 0.4 --alphap 0.9 --m1s 3.097
"""
import argparse
import math

HBARC = 0.19733


def shoot(E, mu, l, V, rmax=25.0, h=0.004):
    """Integrate u'' = 2 mu (V + l(l+1)/(2 mu r^2) - E) u outward (Numerov). Return (nodes, u_end)."""
    n = int(rmax / h)
    def k2(r):
        return 2 * mu * (E - V(r) - l * (l + 1) / (2 * mu * r * r))
    u0, u1 = 0.0, h ** (l + 1)
    r = h
    nodes = 0
    f0, f1 = 0.0, k2(h)
    for i in range(2, n):
        r2 = (i) * h
        f2 = k2(r2)
        u2 = (2 * u1 * (1 - 5 * h * h * f1 / 12) - u0 * (1 + h * h * f0 / 12)) / (1 + h * h * f2 / 12)
        if u2 * u1 < 0:
            nodes += 1
        u0, u1, f0, f1 = u1, u2, f1, f2
        if abs(u1) > 1e150:
            break
    return nodes, u1


def eigen(k, mu, l, V, elo=-1.5, ehi=4.0):
    """k-th eigenvalue (k nodes) by bisection on the node count."""
    for _ in range(60):
        em = 0.5 * (elo + ehi)
        nodes, _ = shoot(em, mu, l, V)
        if nodes > k:
            ehi = em
        else:
            elo = em
        if ehi - elo < 1e-7:
            break
    return 0.5 * (elo + ehi)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--kappa", type=float, default=0.52, help="Coulomb coefficient (4/3 alpha_s)")
    ap.add_argument("--alphap", type=float, default=0.88, help="Regge slope in GeV^-2; sigma = 1/(2 pi alpha')")
    ap.add_argument("--sigma", type=float, default=None, help="override sigma in GeV^2")
    ap.add_argument("--m1s", type=float, default=3.097, help="mass of the 1S state to reproduce")
    ap.add_argument("--mc", type=float, default=None, help="fix m_c instead of tuning it")
    args = ap.parse_args()
    sigma = args.sigma if args.sigma is not None else 1 / (2 * math.pi * args.alphap)
    V = lambda r: -args.kappa / r + sigma * r

    def levels(mc):
        mu = mc / 2
        return {"1S": eigen(0, mu, 0, V), "2S": eigen(1, mu, 0, V), "3S": eigen(2, mu, 0, V),
                "1P": eigen(0, mu, 1, V), "2P": eigen(1, mu, 1, V), "1D": eigen(0, mu, 2, V)}

    if args.mc is None:
        lo, hi = 1.0, 2.5
        for _ in range(40):
            mc = 0.5 * (lo + hi)
            if 2 * mc + eigen(0, mc / 2, 0, V) > args.m1s:
                hi = mc
            else:
                lo = mc
        mc = 0.5 * (lo + hi)
    else:
        mc = args.mc
    lv = levels(mc)
    print(f"V(r) = -{args.kappa}/r + {sigma:.4f} r   (sigma from alpha' = {args.alphap} GeV^-2;  sqrt(sigma) = {1000 * math.sqrt(sigma):.0f} MeV)")
    print(f"m_c = {mc:.3f} GeV  (tuned to M(1S) = {args.m1s})\n")
    memory = {"1S": 3.097, "2S": 3.686, "1P": 3.525, "1D": 3.770, "3S": 4.040, "2P": 3.93}
    print(f"{'state':5s} {'E_bind':>8s} {'M = 2 m_c + E':>14s} {'memory':>8s} {'diff':>7s}")
    for k in ("1S", "1P", "2S", "1D", "2P", "3S"):
        M = 2 * mc + lv[k]
        print(f"{k:5s} {lv[k]:8.3f} {M:14.3f} {memory[k]:8.3f} {1000 * (M - memory[k]):+6.0f} MeV")
    print("\nThe memory column: psi(3097), psi'(3686), chi_c centroid (3525), psi(3770), psi(4040), chi_c(2P) ~ 3.93.")
    print("Spin-dependent splittings are ignored; expect the P and D centroids to be right to a few tens of MeV.")
    print(f"Mean radius scale: 1/sqrt(sigma) = {HBARC / math.sqrt(sigma):.2f} fm; the 1S state sits inside the Coulomb region, the 2S straddles both.")


if __name__ == "__main__":
    main()
