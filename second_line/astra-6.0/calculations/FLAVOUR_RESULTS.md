# Flavour and scale calculations

22 checks passed. No future particle mass or observed generation count was fitted.

These calculations test stated effective theories and algebraic toys. They do not construct a string vacuum.

## Generation-dependent gauge–Yukawa flow

One Higgs doublet; one nonzero quark Yukawa; electroweak couplings neglected; all 2Ng quarks active.

| Ng | b3 | Fixed ratio y²/g3² | Color AF and positive ratio? |
|---:|---:|---:|---|
| 1 | 29/3 | -10/27 | no |
| 2 | 25/3 | -2/27 | no |
| 3 | 7 | 2/9 | yes |
| 4 | 17/3 | 14/27 | yes |
| 5 | 13/3 | 22/27 | yes |
| 6 | 3 | 10/9 | yes |
| 7 | 5/3 | 38/27 | yes |
| 8 | 1/3 | 46/27 | yes |
| 9 | -1 | 2 | no |

The allowed integers are 3–8 in this truncation. Three is the smallest, not the unique solution.

### Finite running at Ng=3

Synthetic g3² grows from 0.25 to 1. The fixed ratio is 2/9. Attraction is incomplete.

| UV ratio | IR ratio |
|---:|---:|
| 0.0500 | 0.058088 |
| 0.5000 | 0.408303 |
| 2.0000 | 0.820574 |

## One large Yukawa

For a normalized rank-one matrix plus a perturbation of operator norm 0.001:

| Matrix size | Singular values, decreasing |
|---:|---|
| 2 | 0.99988587, 0.0003433246 |
| 3 | 0.99977579, 0.00092848108, 0.00023813169 |
| 4 | 0.9994904, 0.00096075124, 0.00055399451, 0.00029604222 |

The mechanism works with two, three or four families; it does not choose their number.

## Flux budget toy

For Q=diag(2,8), L=12 and index n1+2n2, the continuous bound is 4.898979; integer enumeration gives maximum 4.
For Q=diag(eta²,1), L=1 and index n1, eta=1, 0.1, 0.01 permits maximum |index|=1, 14, 141. A bound need not remain uniform in a limit.

## QCD thresholds

Synthetic Lambda6=0.01; heavy masses=[10.0, 2.0, 0.5]; Lambda3=0.033000348.
d ln Lambda3 / d ln mt = 0.074074074 = 2/27 at fixed high-scale coupling.
d ln Lambda3 / d ln v = 0.222222222 = 2/9 when all three heavy thresholds scale with v at fixed Yukawas.
A factor ten change of mt changes Lambda3 by 1.185971. This does not lock the scales.

## Transmutation sensitivity

Six-flavour, one-loop running without threshold matching; alpha_s is a chosen input.

| alpha_s(M) | M/Lambda6 |
|---:|---:|
| 0.10 | 7910.758997 |
| 0.12 | 1772.209777 |
| 0.15 | 397.019742 |

At alpha_s=0.12 the logarithmic sensitivity to alpha_s is 7.479983.

## Ordinary-QCD weak-scale control

Using rounded v=246 GeV and fpi=0.093 GeV gives 6996878 equal QCD-sized doublets to supply v.
Even eight such doublets give only 0.263044 GeV. The equal-decay-constant assumption is an illustration, not a prediction for many-flavour QCD.

The derivations, assumptions and proposed string tests are in notes/FLAVOUR_AND_SCALES.md and SUCCESS_CRITERIA.md.
