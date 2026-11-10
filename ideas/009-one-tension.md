# 009. One tension: Regge slope, charmonium, Hagedorn, deconfinement
**Status:** in progress; item 4 refuted as an inequality in 3d Z2
**Depends on:** none
**Predictions:** P01, P06, P07

## Claim
A single number, sigma = 1/(2 pi alpha') ~ 0.18 GeV^2, fixes

1. the universal Regge slope, alpha' ~ 0.88 GeV^-2;
2. the linear term of the heavy-quark potential V(r) = -(4/3) alpha_s / r
   + sigma r, hence the charmonium level spacing from next week;
3. the string's limiting temperature, T_H = sqrt(3 sigma / (2 pi)) ~ 0.29 GeV
   in d = 4 (and sqrt(3 sigma/pi) in d = 3);
4. the pure-gauge deconfinement temperature, which must sit at or below
   T_H: T_c ~ 0.64 sqrt(sigma) ~ 0.27 GeV;
5. the scale of the glueball spectrum (010) and the string-breaking
   distance (008).

Hagedorn's 1965 value of 0.16 GeV from the resonance spectrum is lower
than the string's T_H. The difference is physics: with light quarks the
string breaks, the level density is that of a theory with quark ends,
and the actual crossover of the theory with light quarks lies near
0.155 GeV.

## Known in 1974
* Chew-Frautschi plots; alpha' from the rho, A2, g mesons and from the
  N and Delta trajectories (see `numerics/regge_fit.py`).
* Hagedorn's spectrum and temperature; Huang-Weinberg's derivation of
  T_H from the dual-model level density in d = 26 (T_H = 1/(4 pi sqrt(alpha'))).
* Nothing yet on charmonium. The narrow state arrives on 11 November.

## What the memory says
* Cornell 1975: V(r) = -kappa/r + r/a^2 with kappa = 0.52 and
  a = 2.34 GeV^-1, i.e. sigma = 0.183 GeV^2 (the quark mass depends on
  whether an additive constant is included; leave it to the fit). This
  reproduces 3.10 and 3.69 GeV and later the P-wave states near 3.5.
* Olesen 1985: T_H in terms of sigma and d, from the winding mode.
* Lucini-Teper-Wenger 2004: T_c/sqrt(sigma) = 0.64 for SU(3), 0.60 at
  large N; first order for N >= 3.
* Lattice QCD with physical quarks (2014): crossover at 0.155 GeV.

## Test
1. `[code]` `numerics/regge_fit.py`: slopes per trajectory, sigma, T_H.
2. `[code]` `numerics/charmonium.py`: Schroedinger equation with the
   Cornell form, sigma from the Regge slope, m_c and kappa fitted to the
   first two levels. Predict the P-wave centroid and the 3S level before
   they are found.
3. `[pencil]` Two derivations of T_H (level density, winding mode) and
   the inequality T_c <= T_H.
4. `[lattice]` T_c in SU(2) in Phase 2 (memory: 0.69 sqrt(sigma) for
   SU(2), second order).

## Expected outcome, and what would refute it
One sigma within 10 percent across items 1, 2 and 4. Refuted if the
charmonium sigma differs from the Regge sigma by a factor of two, or if
T_c comes out above T_H.

## 1976 paper
`outputs/1976-flux-tube-casimir/` (QCDS-76/1). Item 2 tested: the charmonium
tension is 0.78-0.86 of the Regge tension once the potential's own spin-spin
term is allowed for. The 1D level comes out at 3.78-3.81 GeV (P19, no weight:
the outcome is remembered).

## 1978 paper
`outputs/1978-su2-scaling/` (QCDS-78/1). The upsilon family discriminates among
the 1976 potentials; a joint fit to psi, psi', Upsilon, Upsilon' gives
sigma = 0.168 GeV^2, 0.91 of the Regge tension, and the chi_c centre within
12 MeV.

## 1982 paper
`outputs/1982-hagedorn-deconfinement/` (QCDS-82/1). Item 3 derived both ways.
Item 4 fails as an inequality: in 3d Z2, T_c/sqrt(sigma) = 1.105(16), 1.152(26),
1.175(35) for N_t = 2, 3, 4, above T_H = 0.977 sqrt(sigma); by the criterion
written above ("refuted if T_c comes out above T_H") the item is refuted for
that theory. In SU(2) in d = 4, T_c/T_H lies between 0.87 and 0.98 on the same
N_t, the range set by the estimator of the tension, with no established trend.
What survives of item 4 is that one tension sets the scale of T_c within 20%
of the string value in both theories, and the first term of the fall
sigma(T) = sigma - pi (d-2) T^2/6. The closed and the open tube share one
tension (0.04566(25) against 0.0446-0.0475 from the open-tube fits at
beta = 0.73).

## References
ChewFrautschi1962, Hagedorn1965, HuangWeinberg1970, Olesen1985,
PisarskiAlvarez1982, LTW2004a, PDG1974.
