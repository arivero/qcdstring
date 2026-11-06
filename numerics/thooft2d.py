#!/usr/bin/env python3
"""'t Hooft's two-dimensional meson equation, solved numerically (idea 015).

    mu^2 phi(x) = (gamma_1/x + gamma_2/(1-x)) phi(x) - P int_0^1 dy phi(y)/(x-y)^2

in units of g^2 N/pi, with gamma = pi m^2/(g^2 N) - 1 for equal quark
masses. Using the finite-part identity P int dy/(x-y)^2 = -(1/x + 1/(1-x))
the equation is rewritten with a regular integrand and solved by Galerkin
in a sine basis. The asymptotic spectrum mu_n^2 ~ pi^2 n is the string's
m_n^2 = 2 pi sigma n with sigma = g^2 N/2 ('t Hooft normalisation; check).
Needs numpy.

    python3 thooft2d.py --m2 1.0 --N 40 --M 800
"""
import argparse
import sys

try:
    import numpy as np
except ImportError:
    sys.exit("numpy is needed: pip install numpy")


def solve(m2, N, M):
    x = (np.arange(M) + 0.5) / M
    w = 1.0 / M
    n = np.arange(1, N + 1)[:, None]
    phi = np.sin(np.pi * n * x)
    dphi = np.pi * n * np.cos(np.pi * n * x)
    d2phi = -(np.pi * n) ** 2 * phi
    X, Y = x[:, None], x[None, :]
    D2 = (X - Y) ** 2
    np.fill_diagonal(D2, 1.0)
    offdiag = 1.0 - np.eye(M)
    I = np.empty((N, M))
    for k in range(N):
        num = phi[k][None, :] - phi[k][:, None] - (Y - X) * dphi[k][:, None]
        I[k] = w * np.sum(num / D2 * offdiag, axis=1) + w * d2phi[k] / 2
    Op = m2 * (1 / x + 1 / (1 - x))[None, :] * phi - I - dphi * np.log((1 - x) / x)[None, :]
    H = w * phi @ Op.T
    S = w * phi @ phi.T
    ev = np.linalg.eigvals(np.linalg.solve(S, H))
    return np.sort(ev.real)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--m2", type=float, default=1.0, help="quark mass squared in units of g^2 N/pi (gamma + 1)")
    ap.add_argument("--N", type=int, default=40, help="sine basis functions")
    ap.add_argument("--M", type=int, default=800, help="quadrature points")
    a = ap.parse_args()
    ev = solve(a.m2, a.N, a.M)
    print(f"'t Hooft model, m^2 = {a.m2} (units g^2 N/pi), N = {a.N}, M = {a.M}")
    print(f"{'n':>3s} {'mu_n^2':>10s} {'difference':>11s}   (asymptotic difference pi^2 = {np.pi**2:.4f})")
    for i in range(min(12, len(ev))):
        diff = ev[i] - ev[i - 1] if i else float("nan")
        print(f"{i:3d} {ev[i]:10.4f} {diff:11.4f}")
    print("\nBohr-Sommerfeld for two massless quarks on a linear potential: phase-space area E^2/sigma = 2 pi n,")
    print("so m_n^2 = 2 pi sigma n: the dual-model formula with alpha' = 1/(2 pi sigma). The top rows converge toward it.")


if __name__ == "__main__":
    main()
