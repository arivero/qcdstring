# 018. The flux tube is a membrane at strong coupling
**Status:** open
**Depends on:** 003, 002
**Predictions:** P10, P15

## Claim
In the M-theory description of N=1 super Yang-Mills (Witten 1997) the
gauge theory lives on a single fivebrane wrapped on a holomorphic curve,
and the confining string is a membrane stretched between two sheets of
that curve. The string tension is the membrane tension times the
minimal distance between the sheets. The k-string tensions follow the
sine law, the N vacua are the N branches of the curve, and domain walls
are fivebranes interpolating between branches on which the string can
end. The hadronic reading: when the 't Hooft coupling is large the
flux tube has a thickness, the eleventh direction, and the correct
worldvolume theory is that of a membrane rather than a string.

## Known in 1974
* Nothing, except Dirac's membrane (1962) and the first relativistic
  membrane models.

## What the memory says
* Witten 1997 (local copy, `phys4/sources/witten-1997-branes-qcd.pdf`):
  MQCD, the membrane string, domain walls, the theta dependence.
* Hanany-Strassler-Zaffaroni 1998: sine law from MQCD.
* Hanany-Witten 1996 (local copy): brane constructions whose M-theory
  lift is the fivebrane on a curve.
* Townsend 1995, Duff 1996: the membrane and the eleven-dimensional
  theory; the IIA string is a membrane wrapped on the circle.

## Test
1. `[pencil]` Membrane between two parallel sheets at separation L in
   eleven dimensions: tension T_2 L. Compare with the IIA string tension
   1/(2 pi alpha') = T_2 x 2 pi R_11.
2. `[pencil]` The N branches of the MQCD curve for SU(N) and the minimal
   membrane for k units of flux; recover sin(pi k/N).
3. `[lattice]` The k-string ratios at N = 4, 6 (P10) as the test of
   whether QCD's string knows about the membrane.

## Expected outcome, and what would refute it
Sine law in SYM exactly, in QCD approximately. Refuted if QCD k-strings
show tension ratios equal to k (no binding at all).

## References
Witten1997, HSZ1998, HananyWitten1996, Townsend1995, Duff1996, Witten1998c.
