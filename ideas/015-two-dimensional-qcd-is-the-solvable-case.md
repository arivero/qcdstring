# 015. Two-dimensional QCD is the solvable case
**Status:** in progress
**Depends on:** 003
**Predictions:** none registered; this is a check

## Claim
't Hooft's model (this year) is a string theory, and it is the one
place where every step of the program can be done exactly. A string in
d = 2 has no transverse modes; the meson is a pair of quarks on a linear
potential. Bohr-Sommerfeld quantisation of E = 2|p| + sigma |x| gives
the phase-space area E^2/sigma, hence

    m_n^2 = 2 pi sigma n + ...,

which is the dual-model mass formula with alpha' = 1/(2 pi sigma) and
agrees with the asymptotic spectrum of 't Hooft's integral equation.
The same model has Bjorken scaling with quark distributions, so partons
and strings coexist in it. Every objection in `THESIS.md` section 2 can
be examined in this model first.

## Known in 1974
* 't Hooft: the planar limit of 2d QCD, the bound-state equation
  mu^2 phi(x) = (gamma_1/x + gamma_2/(1-x)) phi(x) - P int dy phi(y)/(x-y)^2,
  and the asymptotically linear spectrum in n.
* Schwinger 1962 and Casher-Kogut-Susskind 1974 for the Abelian case.
* Bjorken scaling.

## What the memory says
* Einhorn 1976: form factors and deep-inelastic scattering in the model;
  scaling holds; the structure function is |phi(x)|^2 at leading order.
* Gross-Taylor 1993: pure 2d Yang-Mills is exactly a sum over maps of
  worldsheets, i.e. a string theory with no transverse modes.
* Bars 1976, Bardeen et al 1976: the string with massive ends quantised
  in d = 2 reproduces 't Hooft's spectrum.

## Test
1. `[code]` Solve 't Hooft's equation numerically (a few hundred basis
   functions suffice); extract the slope of m_n^2 versus n; compare with
   2 pi sigma from the known linear potential of the model.
2. `[pencil]` The Bohr-Sommerfeld argument above, then the WKB
   correction; compare with the numerical intercept.
3. `[pencil]` Hard scattering and form factors in the model: are they
   powers? (Yes, in the memory.) This is the toy version of 007.

## Expected outcome, and what would refute it
m_n^2 ~ 2 pi sigma n asymptotically, with the string's alpha'-sigma
relation. Refuted if the slope differs; it does not.

## References
tHooft2d1974, Schwinger1962, CasherKogutSusskind1974, GrossTaylor1993,
BBHP1976, Bjorken1969.
