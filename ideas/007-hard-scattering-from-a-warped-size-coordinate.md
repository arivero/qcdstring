# 007. Hard scattering from a warped size coordinate
**Status:** open
**Depends on:** 002
**Predictions:** P09

## Claim
Exclusive scattering at fixed angle obeys A ~ s^{2 - n/2}, where n is
the total number of elementary constituents of the external hadrons
(dsigma/dt ~ s^{2-n}), and form factors fall as (Q^2)^{-(n_h - 1)}.
A string in flat space gives exp(-alpha' s f(theta)) instead. A string
in a space warped along its size coordinate r, with 4d invariants
rescaled to s (L/r)^2 at position r, gives the power law: the amplitude
is dominated by configurations in which the string has shrunk to a size
1/sqrt(s), and the probability of a hadron being that small is a power of
its size fixed by its number of constituents. The exponent comes out as
the counting rule.

## Known in 1974
* Brodsky-Farrar, Matveev-Muradyan-Tavkhelidze (1973): the counting
  rules, and data: pp elastic at 90 degrees falls like s^-10, the proton
  form factor like 1/Q^4.
* The Veneziano amplitude's exponential fall at fixed angle. This is the
  objection that the parton model wins outright, and it is the one that
  needs the new ingredient.
* In 't Hooft's two-dimensional model (015) the string has partons and
  Bjorken scaling. The dichotomy is false in d = 2 and that is a hint.

## What the memory says
* Polchinski-Strassler 2001: exactly the mechanism above. The warp
  factor converts the string's exponential softness into a power because
  the integral over r is dominated by r ~ L sqrt(alpha' s). The exponent
  is set by the fall-off of the hadron wavefunction toward small size,
  which is the twist of its interpolating operator, i.e. the number of
  constituents at leading twist.
* The deep-inelastic structure functions follow by the same mechanism
  (Polchinski-Strassler 2002) and give Bjorken scaling with power-law
  corrections at large x and a Pomeron-dominated small-x region.

## Test
1. `[pencil]` Take the metric of 002 with an infrared wall. Write the
   amplitude as an integral over r of the flat-space Veneziano amplitude
   with s replaced by s (L/r)^2, weighted by hadron wavefunctions that
   behave as (r_0/r)^Delta near the wall... and as r^Delta toward small
   size. Do the integral by saddle point. Target: s^{2 - n/2} with
   n = sum of Delta_i.
2. `[pheno]` Compare with the 1974 fixed-angle pp data and the SLAC
   proton form factor.
3. `[pencil]` Form factors: a current inserted on the string, same
   integral, target (Q^2)^{-(Delta - 1)}.

## Expected outcome, and what would refute it
The counting-rule exponents, with the angular function f(theta) of the
data coming from the string rather than from gluon exchange. Refuted if
no warp factor consistent with 006 yields the exponents, or if the
angular dependence contradicts data.

## References
BrodskyFarrar1973, MatveevMuradyanTavkhelidze1973, Veneziano1968,
PolchinskiStrassler2001, Polyakov1997, Maldacena1997.
