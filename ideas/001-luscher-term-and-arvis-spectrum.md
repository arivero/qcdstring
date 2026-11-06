# 001. The Luscher term and the Arvis spectrum
**Status:** in progress
**Depends on:** none
**Predictions:** P02, P03

## Claim
A confining flux tube of length R between static sources has energy levels

    E_n(R) = sqrt( sigma^2 R^2 + 2 pi sigma ( n - (d-2)/24 ) ),   n = 0, 1, 2, ...

where n is the total transverse oscillator level and d the number of
spacetime dimensions. For the ground state at large R,

    E_0(R) = sigma R - pi (d-2) / (24 R) - pi^2 (d-2)^2 / (1152 sigma R^3) + ...

The 1/R coefficient is universal: it is the same for any confining
theory in d dimensions. For a closed tube of length R wrapping a periodic
direction, with left and right levels N_L, N_R,

    E(R) = sqrt( sigma^2 R^2 + 4 pi sigma ( N_L + N_R - (d-2)/12 ) + ( 2 pi (N_L - N_R) / R )^2 ).

## Known in 1974
* Light-cone quantisation of the open string (GGRT 1973) gives the
  oscillator spectrum and, in d = 26, the intercept 1 from the
  zero-point sum (d-2)/2 x sum(n) = -(d-2)/24 by zeta regularisation.
* Brink and Nielsen (1973) read that intercept as a Casimir energy.
* Nothing is known about strings with fixed ends at finite R, and nothing
  about what survives in d = 4.

## What the memory says
* Luscher 1981: the 1/R term is the Casimir energy of (d-2) massless
  bosons on an interval, and is universal because the long-distance
  theory of a rough surface is a free massless theory in any dimension.
* Alvarez 1981, Arvis 1983: the full square-root formula is the exact
  spectrum of the Nambu-Goto string with Dirichlet ends (consistent only
  in d = 26, but see next item).
* Polchinski-Strominger 1991, Aharony and collaborators 2009-2013: in
  d = 4 the square root is correct through O(1/R^5); the first
  non-universal term in E_0 is at O(1/R^7). In d = 3 the first
  non-universal term is also at O(1/R^7).
* Luscher-Weisz 2002: in SU(3), the 1/R coefficient of V(R) at R between
  0.5 and 1 fm is consistent with -pi/12 to about 10 percent.

## Test
1. `[pencil]` Mode sum for (d-2) free bosons on an interval of length R
   with Dirichlet ends: omega_n = pi n / R. Regularise the zero-point sum.
   Result: -pi(d-2)/(24R). Then with periodic boundary conditions on a
   circle: -pi(d-2)/(6R). Done in `numerics/arvis_spectrum.py`.
2. `[pencil]` Redo GGRT with Dirichlet ends to obtain the square root.
3. `[pencil]` Argue universality: write the most general action for the
   transverse fields consistent with the (nonlinearly realised) Lorentz
   symmetry of the target space; show the Nambu-Goto expansion is the
   only one at the first two orders beyond the free theory.
4. `[lattice]` Measure V(R) in a Monte Carlo. Fit sigma R + mu + c/R.
   The sign and size of c are the test. See `ideas/004`.

## Expected outcome, and what would refute it
Expect c = -pi/12 = -0.262 in d = 4 and -pi/24 in d = 3, with the
square-root formula working down to R sqrt(sigma) ~ 1.5. Refuted if a
clean lattice measurement gives c of the wrong sign, or a magnitude off
by more than the quoted error, or if the excited levels fail the square
root at O(1/R^3).

## Second line
Their T03 derives the same coefficients. Their T09/T14 table adds a
discriminator: two massless NS Majorana fermions on the worldsheet would
change -pi/(12R) to -pi/(8R), and two R Majoranas to zero. The 1/R
coefficient therefore also measures the worldsheet's fermion content
(P18).

## 1976 paper
`outputs/1976-flux-tube-casimir/` (QCDS-76/1). Test 1 done again with three
regulators and a harmonic chain. Test 4 done in 3d Z2: a 1/R term of Casimir
sign is required; its fitted coefficient is 0.070-0.10 depending on the
shortest separation, pi/24 fits from R sqrt(sigma) ~ 0.9, and pi/24 plus an
R^-2 endpoint term fits everything. The endpoint term is new to this file:
the claim above that the first correction is O(1/R^3) holds for the
worldsheet interior only.

## 1980 paper
`outputs/1980-excited-flux-tube/` (QCDS-80/1). Test 2 done in the 1973 way
(Appendix A there). The first excitation in 3d Z2 lies far below pi/R and
approaches the square root from above, within errors from R sqrt(sigma) ~ 1.7.
The ground state, refitted with the 1976 data, still admits both a single 1/R
coefficient and pi/24 with an endpoint term.

## References
GGRT1973, BrinkNielsen1973, Luscher1981, Alvarez1981, Arvis1983,
PolchinskiStrominger1991, AharonyKarzbrun2009, AharonyKomargodski2013,
LuscherWeisz2002, LuscherWeisz2004.
