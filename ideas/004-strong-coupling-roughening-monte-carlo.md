# 004. Strong coupling, roughening, and a 1975 Monte Carlo
**Status:** in progress. First run (6 Nov 1974, `numerics/z2_lattice.py`, 12^3, 100+100 sweeps): chi(2,2) = 1.23, 0.95, 0.68, 0.41, 0.17 at beta = 0.3, 0.4, 0.5, 0.6, 0.7 against -ln tanh beta = 1.23, 0.97, 0.77, 0.62, 0.50. Strong coupling holds to beta ~ 0.4, departs from 0.5 on (the roughening estimate is 0.47), and the tension falls toward zero approaching beta_c = 0.76.
**Depends on:** 001
**Predictions:** P02, P11, P13

## Claim
Wilson's strong-coupling expansion describes a flux tube that is pinned
to the lattice: a flat, smooth surface. As the coupling weakens the
surface roughens at a definite beta_R, below the continuum limit, and
only beyond beta_R is the flux tube a free string whose transverse modes
are massless and whose energy carries the universal 1/R term. A Monte
Carlo simulation of a lattice gauge theory, feasible now, can see the
area law at strong coupling, the roughening crossover, and, with effort,
the 1/R term.

## Known in 1974
* Wilson's expansion: at leading order sigma a^2 = -ln tanh(beta) for
  Z2, -ln(beta/2) for U(1), -ln(beta/4) for SU(2), -ln(beta/18) for
  SU(3) (with beta = 2N/g^2 and the Wilson action).
* Metropolis et al. 1953: importance sampling. Machines: CDC 6600/7600,
  IBM 360/370. A Z2 gauge theory on a 16^3 lattice has 12288 links and
  needs a few seconds per sweep in Fortran.
* Z2 gauge theory in 3d is dual to the 3d Ising model
  (tanh beta_gauge = exp(-2 K_Ising)), so its critical point is known:
  beta_c = 0.7613 (confinement for beta < beta_c). The Ising interface
  roughens at K_R ~ 0.41, which maps to beta_R ~ 0.47 for the gauge
  theory.

## What the memory says
* Creutz 1979-80: the first simulations; U(1) in 4d has a confining and a
  Coulomb phase, SU(2) confines for all beta and shows asymptotic
  scaling at beta ~ 2.2-2.4 on lattices as small as 6^4.
* Luscher-Symanzik-Weisz 1980, Itzykson-Peskin-Zuber 1980, Hasenfratz-
  Hasenfratz 1980: the strong-coupling series for sigma a^2 has a
  singularity at the roughening point; the surface is rough beyond it.
* Luscher-Weisz 2001-02: with the multilevel algorithm the 1/R term is
  measured at R up to 1 fm in SU(3) and agrees with -pi/12.

## Test
1. `[code]` `numerics/z2_lattice.py`: Metropolis for Z2 in 3d; Wilson
   loops W(R,T); Creutz ratios; sigma(beta) versus -ln tanh beta and
   versus the dual Ising interface tension.
2. `[series]` Extend the strong-coupling series for sigma a^2 to several
   orders (there are tables in the memory; redo them) and locate the
   singularity by ratio tests.
3. `[code, 1975-76]` U(1) and SU(2) in 4d on 6^4 to 8^4. Measure V(R) at
   R = 1..4 a. Fit sigma R + mu + c/R and report c with its error, even
   if the error is as large as c.

## Expected outcome, and what would refute it
Expect the area law at strong coupling with the leading-order sigma,
a visible departure near beta_R, the Ising duality check to work in Z2,
and a negative c of order -0.3 in SU(2) at beta ~ 2.3 with a large
error. Refuted if the area law fails at strong coupling (it will not) or
if c is reliably positive.

## 1976 paper
`outputs/1976-flux-tube-casimir/` (QCDS-76/1). Z2 in 3d: the ratios chi follow
-ln u - 2u^4 within 0.1% to beta = 0.30 and 1% at 0.40. Two-level averaging
needs slabs of 4 for Z2 near beta_c (slabs of 2 are boundary-dominated). U(1)
in 4d: the area law ends near beta = 1.0; the order of the transition is open.

## References
Wilson1974, KogutSusskind1975, Creutz1979, Creutz1980, LSW1980, IPZ1980,
Luscher1981, LuscherWeisz2001, LuscherWeisz2002.
