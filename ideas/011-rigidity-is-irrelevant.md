# 011. Rigidity is irrelevant
**Status:** supported by derivation (1984); lattice comparison open
**Depends on:** 001
**Predictions:** P14

## Claim
One may add to the Nambu-Goto action a term proportional to the square
of the extrinsic curvature of the worldsheet. For a non-Abelian flux
tube the coefficient runs to zero at long distance (the coupling is
asymptotically free on the worldsheet), so the term changes nothing in
P02 and P03, and the lattice spectra of SU(N) flux tubes show no trace
of it. In the compact U(1) theory in d = 3, where confinement is by a
monopole plasma, the flux tube is different: a rigidity term is needed
to fit its spectrum. The comparison between the two is itself a test of
what kind of string a gauge theory makes.

## Known in 1974
* Nothing. The Nambu-Goto action is the only one in use.

## What the memory says
* Polyakov 1986, Kleinert 1986: the rigid string; one-loop running of the
  rigidity coupling; the term is irrelevant in the infrared.
* Aharony et al, Dubovsky et al: the long-string expansion in d = 3 and
  d = 4 has no free parameter until O(1/R^7) in E_0, which rules out any
  rigidity effect at the orders probed.
* Caselle, Panero, Pellegrini, Vadacchino 2014 (arXiv:1406.5127): the
  3d U(1) flux tube deviates from Nambu-Goto and is fitted by adding a
  rigidity term, with the stiffness related to the monopole scale.

## Test
1. `[pencil]` Reproduce the one-loop beta function for the rigidity
   coupling.
2. `[lattice]` Compare the Z2 (004) and compact U(1) spectra in d = 3
   with SU(2) in d = 3 at matched sigma a^2. Look for a deviation from
   the square-root formula that scales as a rigidity term would.

## Expected outcome, and what would refute it
No deviation in SU(2); a measurable one in U(1). Refuted if the
non-Abelian spectrum needs rigidity, which would also damage 001.

## 1984 paper
`outputs/1984-critical-dimension/` (QCDS-84/1), Section 2.3. A stronger and
simpler statement than the running of the coupling. By Gauss's equation the
Lorentz-invariant stiffness K_ab K^ab equals K^2 minus the curvature scalar of
the induced metric: a term quadratic in the equations of motion plus a total
derivative. It changes no level of a long string, closed or open. Terms cubic
in the curvature vanish or reduce likewise, and (grad K)^2 reduces by
Codazzi's equation; the first bulk terms with free coefficients are quartic in
the curvature and enter at sigma^-3 L^-7. The 1976 paper had given a stiffness
as its example of an R^-3 correction; it meant the bending energy of a rod,
which the Lorentz invariance of the vacuum excludes. Tests 1 and 2 above (the
running, and U(1) against SU(2)) remain.

## References
Polyakov1986, Kleinert1986, AharonyKomargodski2013, DFG2012a, Polyakov1977.
