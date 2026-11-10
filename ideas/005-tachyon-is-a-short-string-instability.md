# 005. The tachyon is a short-string instability
**Status:** first half supported; the identification of T_H with deconfinement refuted in 3d Z2
**Depends on:** 001
**Predictions:** P07

## Claim
The bosonic string's negative mass-squared ground state is the statement
that the fixed-end energy E_0(R)^2 = sigma^2 R^2 - pi (d-2) sigma / 12
becomes negative below R_c = sqrt(pi (d-2)/(12 sigma)), about 0.7/sqrt(sigma)
or 0.3 fm in d = 4. Below R_c a flux tube is no longer long, the effective
description has ended, and the true short-distance physics is
perturbative gluon exchange, which is stable. The tachyon is physical in
exactly one place: a closed string wound around a thermal circle of
length 1/T becomes tachyonic at T_H = sqrt(3 sigma/(pi (d-2))), and that
is the Hagedorn instability of the confined phase.

## Known in 1974
* The tachyon of the Veneziano model and of the Neveu-Schwarz model.
* Osterwalder-Schrader (1973): reflection positivity. A lattice gauge
  theory with the Wilson action is reflection positive, so its transfer
  matrix has a positive spectrum. A confining gauge theory cannot have a
  tachyon. Whatever the string's tachyon is, it is a property of the
  flat-space approximation and never of the gauge theory.
* Hagedorn 1965, Huang-Weinberg 1970: a limiting temperature.

## What the memory says
* Gliozzi-Scherk-Olive 1976: in the fermionic string the tachyon is
  removed by a projection; the resulting spectrum is supersymmetric in
  flat ten dimensions.
* Pisarski-Alvarez 1982, Olesen 1985: the winding-mode tachyon at T_H is
  the string's signal of deconfinement; in pure SU(3) the actual T_c is
  slightly below T_H and the transition is first order.
* Athenodorou-Teper and others: closed flux tubes on the lattice track
  the square-root formula down to lengths near R_c and then the
  description fails smoothly, with no sign of an instability.

## Test
1. `[pencil]` Show E_0^2 < 0 for R < R_c from the Arvis formula and that
   R_c is where the expansion parameter 1/(sigma R^2) is of order one.
2. `[pencil]` Compute T_H from the closed-string winding mode and compare
   with the level-density derivation (Huang-Weinberg); they must agree.
3. `[pencil]` Write out the reflection-positivity argument for the
   absence of a tachyon in the gauge theory and attach it to any talk on
   the hadronic string.
4. `[lattice]` Polyakov-loop correlators near T_c in Phase 2.

## Expected outcome, and what would refute it
The two derivations of T_H agree; the lattice shows no instability at
any R. Refuted by a genuine tachyonic signal in a reflection-positive
theory, which cannot happen; the real risk is that the short-string
regime is simply outside the theory, which is a limitation and not a
refutation.

## 1982 paper
`outputs/1982-hagedorn-deconfinement/` (QCDS-82/1). Tests 1 to 3 done: the
wound string's E_0(L)^2 vanishes at L_H, the level density gives the same T_H,
and positivity of the transfer matrix keeps E_0 real in the gauge theory. Test
4 done in 3d Z2 and SU(2): the gauge theory does not follow the square root to
its endpoint. In Z2 the tube exists beyond it (E_0 = 0.38(2) sqrt(sigma) at
L sqrt(sigma) = 1.05) and its energy vanishes linearly at T_c = 1.2 T_H
(effective exponent 1.00 +- 0.07; the class rests on the cumulants). The
second half of the claim, that the tachyon is physical as the Hagedorn
instability of the confined phase, is therefore wrong as stated for a
continuous transition: what happens at short length is the critical behaviour
of the gauge theory, and the tube leaves the square root between
L sqrt(sigma) = 1.5 and 1.35 in Z2. In SU(2) in d = 4 T_c/T_H is 0.87 to 0.98
on N_t = 2 to 4, limited by the estimator of the tension.

## References
GGRT1973, Hagedorn1965, HuangWeinberg1970, GSO1976, PisarskiAlvarez1982,
Olesen1985, Arvis1983, ABT2010.
