#!/usr/bin/env python3
"""Independent check of the second line's D4 tensor benchmark (ideas 006, 010, 021).

Witten's D4 background, transverse-traceless 4d tensor mode H(x), x = U/U0:

    -[(x^4 - x) H']' = kappa x H,   kappa = (9/4) (m/M_KK)^2

Method, deliberately different from second_line/astra-6.0/calculations/spin_susy_checks.py:
shoot outward from the smooth tip in u = ln(x-1) with the regular series, integrate to
large x, and extract the coefficient A of the non-normalizable branch H ~ A + B x^-3 via
A ~ H + p/(3 x^3), p = (x^4 - x) H'. Eigenvalues are the zeros of A(kappa).
Also prints m/sqrt(sigma) using the same metric's tension sigma = 2 lambda M_KK^2/(27 pi).
"""
import math
import sys

try:
    import numpy as np
    from scipy.integrate import solve_ivp
    from scipy.optimize import brentq
except ImportError:
    sys.exit("numpy and scipy are needed")

DELTA0, XMAX = 1e-8, 1e4


def A_of(kappa):
    b = kappa * (kappa - 3) / 36
    d = DELTA0
    x0 = 1 + d
    H0 = 1 - kappa * d / 3 + b * d * d
    Hp0 = -kappa / 3 + 2 * b * d
    p0 = (x0**4 - x0) * Hp0

    def rhs(u, y):
        e = math.exp(u)
        x = 1 + e
        return [e * y[1] / (x**4 - x), -kappa * e * x * y[0]]

    sol = solve_ivp(rhs, (math.log(d), math.log(XMAX - 1)), [H0, p0], method="DOP853", rtol=1e-12, atol=1e-14)
    H, p = sol.y[:, -1]
    return H + p / (3 * XMAX**3)


def main():
    grid = np.linspace(0.5, 60, 240)
    vals = [A_of(k) for k in grid]
    roots = [brentq(A_of, grid[i], grid[i + 1], xtol=1e-12) for i in range(len(grid) - 1) if vals[i] * vals[i + 1] < 0]
    print("D4 tensor (2++) radial eigenvalues, independent shooting method")
    print(f"{'n':>2s} {'kappa':>14s} {'4 kappa (BMT conv.)':>20s} {'m/M_KK':>12s}")
    for n, k in enumerate(roots[:4], 1):
        print(f"{n:2d} {k:14.10f} {4 * k:20.6f} {2 * math.sqrt(k) / 3:12.8f}")
    m1 = 2 * math.sqrt(roots[0]) / 3
    print(f"\nsecond line reports kappa_1 = 5.5241599998, m/M_KK = 1.5669021099; difference here = {abs(roots[0] - 5.5241599998):.1e}")
    print("\nm_2++ / sqrt(sigma) = 1.5669 * sqrt(27 pi / (2 lambda)) in the same background:")
    for lam in (4, 10, 16.6, 50, 100):
        print(f"  lambda = {lam:6.1f}:  m/sqrt(sigma) = {m1 * math.sqrt(27 * math.pi / (2 * lam)):.3f}")
    lam_star = 27 * math.pi * m1**2 / (2 * 4.9**2)
    print(f"  the remembered lattice ratio ~4.9 (P08) needs lambda = {lam_star:.2f}, far from the classical regime lambda >> 1:")
    print("  the KK obstruction of the second line, seen as a number.")


if __name__ == "__main__":
    main()
