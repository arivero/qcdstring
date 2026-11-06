# 026. Why the QCD and Fermi scales are only three decades apart
**Status:** open. Transmutation and threshold controls done by the second line.
**Depends on:** 009, 024, 025
**Predictions:** none registered
**Second line:** T13; notes/FLAVOUR_AND_SCALES.md sections 4-5

## Claim
The string tension sqrt(sigma) ~ 0.43 GeV (from the Regge slope, idea
009) and the weak scale v ~ 246 GeV (from G_F, known in 1974) are about
three decades apart. A theory of the QCD string should say why that
distance is moderate, with the remaining parameter dependence stated.
The scale dictionary comes first: v, Lambda in a stated scheme, a
hadronic observable, the confining sqrt(sigma), and any microscopic
string scale are five different quantities.

## Known in 1974
* G_F, hence v. The Regge slope, hence sigma. f_pi.
* Dimensional transmutation: Lambda = M exp[-2 pi/(b alpha(M))].

## What the memory says
* QCD-induced electroweak breaking gives v of order f_pi, far too small
  (Quigg-Shrock 2009).
* Heavy-quark thresholds couple the two scales weakly (Quigg 1997).

## Test
Results already executed by the second line, reproduced here:
* Ordinary QCD breaking would need about seven million QCD-sized
  doublets to supply v.
* At fixed high-scale coupling, Lambda_3 = Lambda_6^(7/9) (m_t m_b m_c)^(2/27):
  the top mass moves Lambda_3 with exponent 2/27, and v with 2/9 if all
  three heavy masses scale with it. The thresholds do not lock the scales.
* One-loop transmutation makes a ratio of order 10^3 natural at
  alpha_s ~ 0.12, with logarithmic sensitivity 7.5 to the coupling.
Still to do:
1. `[pencil]` Express both sqrt(sigma) and v through the same string
   data: in a warped background, two infrared scales from two positions
   along the radial direction, with their ratio fixed by one coupling.
2. `[pencil]` Compute the conversion from Lambda to sqrt(sigma) in the
   same scheme (the second line flags that equating them is a common
   error).

## Expected outcome, and what would refute it
A formula for v/sqrt(sigma) with one stated residual parameter. Refuted
as an explanation if the two scales come from two independently placed
walls or condensates.

## References
QuiggShrock2009, Quigg1997, BHL1990, second_line/astra-6.0/ideas/T13.
