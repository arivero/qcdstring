#!/usr/bin/env python3
"""Analytic checks for Section 2 of the 1982 paper. Writes ../results/hagedorn.txt.

1. Level density of a string with c = d - 2 transverse towers: exact
   degeneracies p_c(N) from prod_n (1 - q^n)^(-c), compared with
   C N^{-(c+3)/4} exp(2 pi sqrt(c N / 6)); the limiting temperature it gives.
2. The closed string wound once around a circle of length L (Appendix A):
   E^2 = sigma^2 L^2 + 4 pi sigma (N + Nbar - c/12) + (2 pi (N - Nbar)/L)^2;
   its ground state vanishes at the same temperature.
3. The free-string sum over open-string levels between two static sources
   at distance R on a time circle of length L, rewritten term by term as a
   sum over closed-string levels (the transformation of Dedekind's eta
   function): -pi c/24R for the open string is -pi c/6L for the closed one.
"""
import math, os
HERE = os.path.dirname(os.path.abspath(__file__))
out = []
def say(s=""):
    out.append(s); print(s)


def degeneracies(c, Nmax):
    """p_c(N), exact integers: n p(n) = c sum_{k=1..n} sigma_1(k) p(n-k)."""
    sig = [0] * (Nmax + 1)
    for d in range(1, Nmax + 1):
        for m in range(d, Nmax + 1, d):
            sig[m] += d
    p = [1] + [0] * Nmax
    for n in range(1, Nmax + 1):
        p[n] = c * sum(sig[k] * p[n - k] for k in range(1, n + 1)) // n
    return p


say("1. Level density")
say("   c = d-2   N     ln p_c(N)    2 pi sqrt(cN/6) - ((c+3)/4) ln N + const   local slope / (2 pi sqrt(c/6))")
TH = {}
for c in (1, 2, 24):
    Nmax = 1600
    p = degeneracies(c, Nmax)
    lnp = [math.log(x) if x > 0 else float("nan") for x in p]
    a = 2 * math.pi * math.sqrt(c / 6)
    # constant from the largest N
    const = lnp[Nmax] - a * math.sqrt(Nmax) + (c + 3) / 4 * math.log(Nmax)
    for N in (25, 100, 400, 1600):
        asym = a * math.sqrt(N) - (c + 3) / 4 * math.log(N) + const
        # slope of [ln p + ((c+3)/4) ln N] against sqrt(N), from N and N/4... use a centred difference
        N1, N2 = int(N * 0.81), N
        y = lambda n: lnp[n] + (c + 3) / 4 * math.log(n)
        slope = (y(N2) - y(N1)) / (math.sqrt(N2) - math.sqrt(N1))
        say(f"   {c:2d}     {N:5d}   {lnp[N]:10.4f}   {asym:10.4f}                               {slope / a:.5f}")
    # open string: m^2 = 2 pi sigma N, so ln rho = a m / sqrt(2 pi sigma) = m / T_H
    TH[c] = math.sqrt(2 * math.pi) / a
    say(f"   c = {c}: T_H / sqrt(sigma) = sqrt(2 pi)/(2 pi sqrt(c/6)) = sqrt(3/(pi c)) = {TH[c]:.5f};"
        f" density of states in mass ~ m^(-(c+1)/2) exp(m/T_H)")
say()
say("2. Wound closed string")
for d in (3, 4, 26):
    c = d - 2
    Lc = math.sqrt(math.pi * c / 3)       # in units 1/sqrt(sigma)
    say(f"   d = {d}: E_0(L)^2 = sigma^2 L^2 - pi c sigma/3 vanishes at L sqrt(sigma) = {Lc:.5f},"
        f" T_H/sqrt(sigma) = {1 / Lc:.5f}  (level density: {TH[c] if c in TH else math.sqrt(3 / (math.pi * c)):.5f})")
say("   with sqrt(sigma) = 0.43 GeV (Regge slope): T_H = %.3f GeV in d = 4" % (0.43 * math.sqrt(3 / (2 * math.pi))))
say("   effective number of towers that Hagedorn's 0.16 GeV would need at this tension: c = 3 sigma/(pi T^2) = %.1f"
    % (3 * 0.43 ** 2 / (math.pi * 0.16 ** 2)))
say()
say("3. Open and closed channels of the free string (c = 1; sigma R L removed)")
say("   R/L    sum over open levels          sum over closed levels        ratio")


def eta_sum_open(R, L, c, nmax=400):
    """sum_N p_c(N) exp(-pi (N - c/24) L / R)"""
    p = degeneracies(c, nmax)
    return sum(p[N] * math.exp(-math.pi * (N - c / 24) * L / R) for N in range(nmax + 1))


def eta_sum_closed(R, L, c, nmax=400):
    """(L/2R)^(c/2) sum_n p_c(n) exp(-4 pi (n - c/24) R / L): closed levels
    E_n = sigma L + (4 pi / L)(n - c/24) propagating over the distance R."""
    p = degeneracies(c, nmax)
    return (L / (2 * R)) ** (c / 2) * sum(p[n] * math.exp(-4 * math.pi * (n - c / 24) * R / L) for n in range(nmax + 1))


for ratio in (0.25, 0.5, 1.0, 2.0):
    R, L = ratio, 1.0
    a, b = eta_sum_open(R, L, 1), eta_sum_closed(R, L, 1)
    say(f"   {ratio:4.2f}   {a:.12e}        {b:.12e}       {a / b:.12f}")
say("   The closed-channel ground level is sigma L - pi c/(6 L); the factor (L/2R)^(c/2) is the")
say("   transverse-momentum integral of the closed string in c transverse dimensions.")
open(os.path.join(HERE, "..", "results", "hagedorn.txt"), "w").write("\n".join(out) + "\n")
