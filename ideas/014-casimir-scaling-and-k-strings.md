# 014. Casimir scaling and k-strings
**Status:** open
**Depends on:** 003, 004
**Predictions:** P10

## Claim
The tension of the string between static sources in representation R
of SU(N) is, at intermediate distances, proportional to the quadratic
Casimir C_2(R) (so the adjoint string has tension (9/4) sigma in SU(3)
and 8/3 sigma in SU(2)). At asymptotically large distance only the
N-ality k of R matters, because gluons screen everything else, and the
stable k-string tensions satisfy

    sigma_k / sigma_1 ~ sin(pi k / N) / sin(pi / N)

to within a few percent (with k(N-k)/(N-1) a competitor the lattice
cannot quite exclude). The adjoint string breaks by gluon pair creation
at a distance comparable to the light-quark breaking length.

## Known in 1974
* Wilson's strong-coupling expansion: the adjoint loop at leading order
  is bounded by two sheets, tension 2 sigma, and is screened at higher
  orders.
* Group theory of SU(N) representations.

## What the memory says
* Bali 2000: Casimir scaling for eight representations of SU(3) out to
  1 fm, to a few percent.
* Del Debbio et al 2001, Lucini-Teper-Wenger 2004: k-string tensions
  near the sine law for N up to 8.
* Douglas-Shenker 1995, Hanany-Strassler-Zaffaroni 1998: the sine law
  from supersymmetric and holographic strings. It is a prediction of the
  warped-coordinate picture.

## Test
1. `[pencil]` Casimir scaling from one-gluon exchange plus a string:
   at what R does the string part take over from the Coulomb part?
2. `[lattice]` In SU(2), fundamental versus adjoint Wilson loops at
   beta ~ 2.3; the ratio of effective tensions at R = 2-4 a. Expect
   8/3 at short R and screening at large R.
3. `[pencil]` k = 2 string in SU(4) as two fundamental strings bound by
   a 1/N interaction; estimate the binding.

## Expected outcome, and what would refute it
Casimir scaling at intermediate R; sine-law-like k-string ratios at
large N. Refuted by sigma_adj/sigma_fund = 2 at all R in SU(2), or by
k-string ratios equal to k.

## References
Wilson1974, Bali2000, DelDebbio2001, LTW2004b, tHooftPlanar1974.
