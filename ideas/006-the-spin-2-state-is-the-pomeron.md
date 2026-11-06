# 006. The massless spin-2 state is the Pomeron
**Status:** in progress
**Depends on:** 002
**Predictions:** P05, P08

## Claim
The leading closed-string trajectory, which in flat space passes through
a massless spin-2 state at intercept 2, is the Pomeron. In the warped
geometry of the size coordinate its intercept is lowered to

    alpha_P(0) = 2 - 2/sqrt(lambda) + O(1/lambda),   lambda = g^2 N,

and its slope is reduced below the flat-space value alpha'/2. The
observed numbers, intercept 1.08 and slope 0.25 GeV^-2, are measurements
of that geometry. The same mechanism moves the open-string vector from
intercept 1 to the rho's 0.5. The coupling of the state is hadronic: it
goes with the number of constituent quarks (sigma(pi p)/sigma(p p) ~ 2/3)
and carries form factors, whereas a graviton couples to energy-momentum
universally.

## Known in 1974
* ISR total cross-sections rise with s (1973); the effective Pomeron
  intercept is slightly above 1; dsigma/dt shrinks with slope near
  0.25 GeV^-2.
* Lovelace 1971: the closed-string pole in the nonplanar loop is the
  dual Pomeron, with intercept 2 at d = 26 and (d-2)/12 in general. In
  d = 4 that gives 1/6, so the intercept is dynamical; flat-space Casimir
  counting cannot be the whole story.
* The additive quark model for total cross-sections.

## What the memory says
* Donnachie-Landshoff 1992: sigma_tot = X s^0.08 + Y s^-0.45 fits
  everything from the ISR to the Tevatron.
* Brower-Polchinski-Strassler-Tan 2006: the Pomeron is the Regge
  trajectory of the graviton in the warped space; the intercept formula
  above; at weak coupling it joins onto the perturbative two-gluon
  (BFKL) Pomeron with intercept near 1.
* Lattice glueball trajectories (Meyer-Teper 2004) have intercept near 1
  and slope near 0.25-0.3 GeV^-2, with the 2^{++} glueball on them.

## Test
1. `[pheno]` Fit pp, pbar p, pi p, K p total cross-sections from
   Serpukhov, the ISR and Fermilab with X s^eps + Y s^-eta. Report eps
   with its error. Extract alpha'_P from the t-slope's shrinkage.
2. `[pencil]` Regge trajectory of the spin-2 state in the warped metric:
   a diffusion problem in the size coordinate whose lowest eigenvalue
   gives the intercept shift. From eps = 0.08, infer sqrt(lambda) ~ 2.2.
3. `[consistency]` The Pomeron trajectory at J = 2 should cross the
   2^{++} glueball: m^2 ~ (2 - 1.08)/0.25 ~ 3.7 GeV^2, m ~ 1.9 GeV, to
   be compared with the lattice 2^{++} of 2.2-2.4 GeV. Rough agreement is
   the most one should expect from a linear extrapolation.
4. `[pheno]` Check that the Pomeron coupling scales with quark number,
   against universal coupling to energy.

## Expected outcome, and what would refute it
Intercept between 1.05 and 1.12; slope near 0.25; quark-counting
couplings. Refuted by an intercept consistent with 2, or at or below 0,
or by an energy-universal coupling.

## References
Lovelace1971, GoddardThorn1972, DonnachieLandshoff1992, BPST2006,
Maldacena1997, Witten1998b, LTW2004b.
