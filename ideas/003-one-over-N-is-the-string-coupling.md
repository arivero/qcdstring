# 003. 1/N is the string coupling
**Status:** in progress
**Depends on:** none
**Predictions:** P10

## Claim
In an SU(N) gauge theory with g^2 N fixed, a connected amplitude with h
handles and b quark boundaries scales as N^{2 - 2h - b}. This is the
genus expansion of an open-closed string with g_s = 1/N. The dual
resonance model's tree amplitudes are the leading term; the
inconsistencies of its loops (unitarity, the critical dimension in loop
graphs) are 1/N^2 effects in a theory where the expansion parameter is
1/9.

## Known in 1974
* 't Hooft (this year): the planar expansion, with the N-counting of
  surfaces. Also the 2d model, solvable at N = infinity, with a linear
  potential and a tower of mesons.
* Phenomenology: the OZI rule, narrow resonances, the smallness of
  meson-meson scattering, the absence of exotics. All are the statements
  g_s small.

## What the memory says
* Veneziano 1976: the topological expansion, with the dual model as the
  leading order.
* Witten 1979: baryons have mass of order N and are solitons.
* Lattice at N = 2 to 8 (Lucini-Teper 2001; Athenodorou-Teper 2021):
  the string tension, glueball masses and T_c approach their N = infinity
  values with corrections of order 1/N^2, and the N = 3 theory is within
  a few percent of the limit for most quantities.
* Maldacena 1997: the large-N, strong-coupling limit is where the string
  picture becomes weakly coupled and weakly curved.

## Test
1. `[pheno]` From the 1974 tables: ratios Gamma/m for rho, K*, phi, A2;
   the phi to 3 pi suppression; compare with 1/N and 1/N^2 expectations.
2. `[pencil]` Count the N-dependence of a Veneziano amplitude with
   Chan-Paton factors versus a planar gluon diagram with the same
   boundary structure.
3. `[lattice]` In Phase 2, compute sigma a^2 at fixed physical coupling
   for SU(2) and SU(3) (and SU(4) if the machine allows) and look for
   the 1/N^2 pattern.

## Expected outcome, and what would refute it
Expect the N-counting to match term by term and the lattice ratios to
show O(1/N^2) convergence. Refuted if widths or lattice quantities show
O(1/N) corrections of order one, or if the N-counting of dual-model
loops fails to match the planar counting.

## References
tHooftPlanar1974, tHooft2d1974, Veneziano1976 (Nucl. Phys. B117, 519),
Witten1979, LuciniTeper2001, AT2021, Maldacena1997.
