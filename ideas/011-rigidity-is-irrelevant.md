# 011. Rigidity is irrelevant
**Status:** perturbative redundancy supported (1984); explicit massive-field examples derived (1988); microscopic matching and lattice comparison open
**Depends on:** 001
**Predictions:** P14, P23, P24

## Claim
In a long-string derivative expansion, a mean-curvature-square operator
is removable order by order when all induced operators, sources and
boundary conditions are transformed. This does not exclude a massive
internal sector. Its finite-length winding contribution can be exponential,
while its nonredundant local interactions give power corrections.

The 1988 examples establish this distinction in specified effective models.
They do not determine the stiffness or massive spectrum of a non-Abelian
flux tube. The remembered comparison between compact U(1) and SU(N) theories
remains a separate lattice target; a running-coupling statement is not a
substitute for that comparison.

## Known in 1974
* Nothing. The Nambu-Goto action is the only one in use.

## What the memory says
* Polyakov 1986, Kleinert 1986: the rigid string and running of the
  rigidity coupling. The ultraviolet asymptotic-freedom statement is not
  by itself an exclusion of massive infrared degrees of freedom.
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
The remembered target is a difference between the two gauge theories.
A massive threshold in a non-Abelian spectrum would not by itself refute
the long-string expansion or idea 001; it would require retaining the
additional sector and testing its domain of validity. The microscopic
comparison remains open.

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

## 1986 qualification

QCDS-86/1 Section 3.3 restricts "changes no level" to perturbative
operator redundancy with field-redefinition-induced operators and boundary
conditions included. It does not identify a finite-stiffness theory treated
nonperturbatively with the area theory at every energy. Massive thresholds
and the local curvature expansion are the proposed 1988 calculation. No new
rigidity fit or running-coupling calculation is claimed in 1986.

## 1988 construction

[QCDS-88/1](../outputs/1988-thickness-curvature/paper.md) makes the
qualification constructive. A normal field with derivative mixing has a
positive quadratic kinetic matrix for abs(g) < 1, a physical mass
M = m/sqrt(1-g^2), and a negative induced local p^4 coefficient. The apparent
unstable pole of that truncation is outside its convergence disk. Retaining
both Gaussian determinants gives the finite-length energy at mass M.
Conversely, an exact positive-p^4 kernel can have the same determinant as
an extra scalar while its displacement propagator has a negative residue.

A separate scalar coupled to intrinsic curvature gives a nonredundant
R^2 interaction. In d = 3 its q-dependent tree-matching contribution has
phase b s^3 and directly calculated periodic vacuum shift
-32 pi^6 b/(225 L^7), with b = q^2/(4 sigma^2 m^2). This is conditional on
the model and the subtraction of other matching contributions. It does not
close the area-action L^-5 calculation, identify the pseudoscalar of idea
013, or supply a QCD mass, coupling or thickness. P23-P24 record the model
statements; the source, checks and review status are in the paper package.
