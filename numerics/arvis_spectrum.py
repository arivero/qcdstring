#!/usr/bin/env python3
"""Nambu-Goto spectrum of a string with fixed ends (Arvis 1983), its
large-R expansion (the Luscher term), the closed-string formula, the
Hagedorn temperature, and a numerical check that the zero-point sum of
the transverse modes is -1/12 per mode (Brink-Nielsen 1973). Ideas 001,
005, 009, 012. Units: sigma = 1. Pure Python.
"""
import math
import sys

D = int(sys.argv[1]) if len(sys.argv) > 1 else 4


def e_open(n, R, d=D, sigma=1.0):
    """Energy of the n-th level of an open string of length R, fixed ends."""
    x = sigma**2 * R**2 + 2 * math.pi * sigma * (n - (d - 2) / 24)
    return math.sqrt(x) if x > 0 else float("nan")


def e_open_series(R, d=D, sigma=1.0, order=3):
    """Large-R expansion of the ground state through 1/R^5."""
    c = math.pi * (d - 2) / 12  # 2 pi sigma (d-2)/24 with sigma = 1 ... kept general below
    a = math.pi * (d - 2) / 12 * sigma
    terms = [sigma * R, -a / (2 * sigma * R)]
    if order >= 2:
        terms.append(-a**2 / (8 * sigma**3 * R**3))
    if order >= 3:
        terms.append(-a**3 / (16 * sigma**5 * R**5))
    return sum(terms)


def e_closed(NL, NR, R, d=D, sigma=1.0):
    x = sigma**2 * R**2 + 4 * math.pi * sigma * (NL + NR - (d - 2) / 12) + (2 * math.pi * (NL - NR) / R) ** 2
    return math.sqrt(x) if x > 0 else float("nan")


def zeta_check():
    """sum_{n>=1} n e^{-eps n} = 1/eps^2 - 1/12 + O(eps^2): the -1/12 is the
    Casimir energy per transverse mode, seen directly in a regulated sum."""
    print("Regulated zero-point sum  S(eps) = sum n e^{-eps n}  minus its 1/eps^2 divergence:")
    for eps in (0.2, 0.1, 0.05, 0.02):
        s = sum(n * math.exp(-eps * n) for n in range(1, int(60 / eps)))
        print(f"  eps = {eps:5.2f}:  S - 1/eps^2 = {s - 1 / eps**2:+.6f}   (expect -1/12 = {-1 / 12:+.6f})")


def main():
    d = D
    print(f"Nambu-Goto string with fixed ends in d = {d}, units sigma = 1\n")
    print("Open string, ground and first excited levels, versus the large-R expansion:")
    print(f"{'R':>5s} {'E0 exact':>10s} {'sigma R':>9s} {'+Luscher':>9s} {'+1/R^3':>9s} {'+1/R^5':>9s} {'E1':>8s} {'E2':>8s} {'E1-E0':>8s}")
    for R in (0.8, 1.0, 1.5, 2.0, 3.0, 4.0, 6.0, 8.0):
        e0 = e_open(0, R)
        print(f"{R:5.1f} {e0:10.4f} {R:9.4f} {e_open_series(R, order=1):9.4f} {e_open_series(R, order=2):9.4f} "
              f"{e_open_series(R, order=3):9.4f} {e_open(1, R):8.4f} {e_open(2, R):8.4f} {e_open(1, R) - e0:8.4f}")
    rc = math.sqrt(math.pi * (d - 2) / 12)
    print(f"\nE0^2 < 0 below R_c = sqrt(pi (d-2)/12) = {rc:.3f} / sqrt(sigma): the short-string limit (idea 005).")
    print(f"Luscher coefficient: -pi (d-2)/24 = {-math.pi * (d - 2) / 24:.4f}  (open);  -pi (d-2)/6 = {-math.pi * (d - 2) / 6:.4f}  (closed)")
    print("Memory: in d = 4 the exact formula is universal through O(1/R^5); the first free parameter enters E0 at O(1/R^7).")

    print("\nClosed string of length R (N_L, N_R) = (0,0), (1,1), (1,0):")
    for R in (1.5, 2.0, 3.0, 4.0, 6.0):
        print(f"  R = {R:4.1f}:  E00 = {e_closed(0, 0, R):7.4f}   E11 = {e_closed(1, 1, R):7.4f}   E10 = {e_closed(1, 0, R):7.4f}")
    rcc = math.sqrt(math.pi * (d - 2) / 3)
    th = math.sqrt(3 / (math.pi * (d - 2)))
    print(f"  closed-string tachyon below R = {rcc:.3f}; as a thermal winding mode this is T_H = sqrt(3 sigma/(pi (d-2))) = {th:.4f} sqrt(sigma)")
    print(f"  cross-check from the level density: T_H = sqrt(6/(d-2)) / (2 pi sqrt(alpha')) with alpha' = 1/(2 pi) gives {math.sqrt(6 / (d - 2)) / (2 * math.pi) * math.sqrt(2 * math.pi):.4f}")

    print()
    zeta_check()
    print("\nWorldsheet phase shift at tree level (idea 012): 2 delta(s) = s / (4 sigma); the (26-d) correction is O(s^2/sigma^2).")


if __name__ == "__main__":
    main()
