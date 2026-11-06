# 024. One heavy quark: a rank-one Yukawa
**Status:** open. Algebraic and renormalisation-group controls done by the second line.
**Depends on:** 020, 025, 026
**Predictions:** none registered
**Second line:** T11; notes/FLAVOUR_AND_SCALES.md sections 1-2

## Claim
If the leading up-type Yukawa coupling comes from a single interaction
point in an internal geometry, it has rank one: one unsuppressed quark
mass, all others zero at leading order. Small rank-lifting effects give
the light masses. The heavy quark of the fourth (or third) family is
then the generic prediction; the target is an explanation, and the
second line sets the bar: derive the one large up-type coupling, the
separate suppression of the down-type ones including the bottom, and the
normalisation of both.

## Known in 1974
* Three quark flavours established, charm about to be (11 November).
  Nothing is known of a third family's masses.
* Gross-Wilczek and Politzer beta functions; the gauge-Yukawa flow can be
  written now.

## What the memory says
* Heckman-Vafa 2008, Cecotti-Cheng-Heckman-Vafa 2009: rank-one Yukawas at
  a point of enhanced symmetry in local F-theory models; ordinary gauge
  flux does not lift the holomorphic rank.
* Pendleton-Ross 1981: infrared fixed ratios of gauge and Yukawa
  couplings.
* Bardeen-Hill-Lindner 1990: top condensation, the alternative branch.

## Test
Results already executed by the second line, reproduced here
(`second_line/astra-6.0/calculations/FLAVOUR_RESULTS.md`):
* A rank-one matrix plus a perturbation of norm 1e-3 gives one singular
  value near 1 and the rest below 1e-3 for 2, 3 and 4 families. The
  mechanism selects one heavy state and no family number.
* With one Higgs doublet, one Yukawa and 2 N_g quarks, the fixed ratio
  y^2/g^2 = 2(4 N_g - 9)/27 is 2/9 at three families. Attraction toward it
  over a finite interval is weak.
Still to do:
1. `[pencil]` A local brane model with its kinetic matrices; the
   normalised largest Yukawa.
2. `[pencil]` The up/down asymmetry from the same geometry.
3. `[link]` Connect to the flux tube: does the heavy quark's endpoint
   mass bend its Regge trajectory as in 008? The heavy-meson trajectories
   are the hadronic observable of a heavy quark, and the only bridge from
   this idea to the rest of the repository.

## Expected outcome, and what would refute it
A derived up/down asymmetry and a largest Yukawa of order one. Refuted
as an explanation if the large entry, the bottom suppression or the
perturbation is fitted.

## References
HeckmanVafa2008, CCHV2009, PendletonRoss1981, BHL1990, GrossWilczek1973,
Politzer1973, second_line/astra-6.0/ideas/T11.
