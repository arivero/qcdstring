# 025. A bound on generations that survives removing gravity
**Status:** open. One-loop interval and flux-budget toy done by the second line.
**Depends on:** 020, 023
**Predictions:** none registered
**Second line:** T12; notes/FLAVOUR_AND_SCALES.md sections 2-3

## Claim
The number of families should be bounded by the same data that define
the string sector, and the bound should survive the limit in which
gravity decouples. Choosing an index equal to three, or identifying
families with oscillator levels, counts as accommodation.

## Known in 1974
* Asymptotic freedom of SU(3) with 2 N_g Dirac quarks requires
  b = 11 - (4/3) N_g > 0, so N_g <= 8. A 1974 statement.

## What the memory says
* Flux tadpole conditions bound chiral indices in compact constructions
  (Ishiguro et al 2023). Whether such a bound stays finite when gravity
  is decoupled is an open question in the memory too.

## Test
Results already executed by the second line, reproduced here:
* Requiring both colour asymptotic freedom and a positive fixed
  Yukawa/gauge ratio gives the integer interval 3 <= N_g <= 8 in a
  one-loop, one-Higgs, one-Yukawa truncation. Three is the smallest
  allowed value, not a unique one.
* A positive flux budget n^T Q n <= 2L with index l^T n bounds the index
  by sqrt(2L l^T Q^-1 l); a degenerating Q destroys the bound in a limit
  (toy: maximum index 1, 14, 141 as eta goes 1, 0.1, 0.01).
Still to do:
1. `[pencil]` A flux sector whose Q stays non-degenerate along the
   decoupling limit of 023.
2. `[pencil]` Count complete generations, vectorlike pairs included.
3. `[link]` The hadronic side: the number of flavours enters the flux
   tube through string breaking (008) and the Regge intercepts; the
   conformal window (N_f near 16 for SU(3)) is where the confining string
   disappears. Write the family bound and the confinement condition as
   one statement.

## Expected outcome, and what would refute it
A finite bound with a stated domain. Refuted as a derivation if it holds
at each compact point and fails uniformly in the limit.

## References
GrossWilczek1973, Politzer1973, Ishiguro2023, second_line/astra-6.0/ideas/T12.
