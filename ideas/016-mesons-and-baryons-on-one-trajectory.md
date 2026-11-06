# 016. Mesons and baryons on one trajectory: the diquark string
**Status:** in progress. First run (6 Nov 1974): slopes equal to 15 percent; Delta tower pairs with L+1 mesons to within 80 MeV; nucleon ground state does not pair; N(1688) degenerate with g(1680) at equal L. See PREDICTIONS.md status log.
**Depends on:** 008
**Predictions:** P06

## Claim
A baryon is a string between a quark and a diquark, so the baryon
trajectories have the meson slope. Beyond that, there is a pairing: for
each meson with orbital excitation L there is a baryon with L - 1 of
nearly the same mass, a hadronic supersymmetry in the sense of
Miyazawa, with the diquark playing the role of the antiquark. The
meson and baryon intercepts then differ by a fixed amount near 1/2.

## Known in 1974
* Miyazawa 1966, 1968: a supergroup relating mesons and baryons.
* Diquarks: Ida-Kobayashi 1966, Lichtenberg 1967.
* The N and Delta trajectories (N: 939, 1688, 2220; Delta: 1232, 1950,
  2420) have slopes near 0.9-1.0 GeV^-2, the same as the rho trajectory
  (770, 1310, 1680) within errors.

## What the memory says
* Catto-Gursey 1985: algebraic hadronic supersymmetry with diquarks.
* Brodsky, de Teramond, Dosch 2015: a superconformal quantum mechanics
  in the light-front holographic framework in which meson and baryon
  towers are superpartners, with the pion as the unpaired state. The
  trajectories match to about 50 MeV in mass.
* Sonnenschein 2016: baryons as quark-diquark strings with massive ends
  fit the table with the meson slope; the Y-shaped three-string
  configuration is disfavoured for the ground-state trajectories.

## Test
1. `[code]` `numerics/regge_fit.py`: fit the rho, N and Delta leading
   trajectories; report slopes with errors; test slope equality.
2. `[code]` Pair mesons of orbital L with baryons of L - 1 from the 1974
   tables; tabulate mass differences; see whether a pattern survives the
   errors.
3. `[pencil]` A string with a diquark end: the diquark mass enters as in
   008; derive the intercept shift.

## Expected outcome, and what would refute it
Equal slopes within 10 percent; a pairing pattern with mass differences
below 100 MeV for the leading states. Refuted by slopes that differ by
more than 20 percent, or by a pairing that works no better than random.

## References
Miyazawa1966, Miyazawa1968, ChewFrautschi1962, CattoGursey1985,
BdTDE2015, dTDB2015, Sonnenschein2016, PDG1974.
