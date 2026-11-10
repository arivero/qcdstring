# Referee report: QCDS-82/1

*Second-line referee (astra-6.0); the four paper folders and the second line's package only.*

## Summary of the submission

The preprint measures the ground-state energy E0(L) of the closed flux tube in the three-dimensional Z2 gauge theory. The tube is wound once around a time circle of L = 3-16 spacings, and E0 is read off as the free energy of the dual Ising interface that an antiperiodic plane forces. That free energy comes from integrating ⟨S⟩_P − ⟨S⟩_A from K = 0.15. Formula (4), a single band over 2L_y momenta with a factor ½, converts it to E0. The paper reports:
- a Casimir term with c = 0.97(4) and 1.04(6) massless modes at β = 0.73 and 0.70;
- the square root within 2% for L√σ ≥ 1.5, and 6(2)% above it at 1.28;
- linear vanishing at deconfinement, ν = 1.01(2) and 0.98(2);
- T_c/√σ = 1.105-1.175, extrapolated to 1.19(3), which is 13-22% above T_H = 0.977√σ;
- for SU(2) on 8³ and 12³ with N_t = 2-4, T_c/T_H = 0.87-0.93;
- from a refit of the 1976 and 1980 open-tube data with the closed-tube tension, b = 0.116(5) from R = 4.

Budget: 87 of 100 Cray-1 hours.

## Assessment of the main claims

- Formula (4), the window and the 1% allowance: **supported**. It matches Kaufman to 10⁻⁴ in the mass for mL_y ≥ 5.5. In 2D its error stays below 1.4% inside the window, and the four N_t = 8 lattices follow that 2D error with a ratio of 0.6-1.3.
- Integration and its errors: **supported**. Replica pulls have rms 0.84-1.09, no run drifts, and doubling the spacing above K = 0.20 changes F only within noise.
- The closed tube has a Casimir energy: **supported**. σL fails with χ² = 553/3 and σL + const with 15.3/2 at β = 0.73 (295/3 and 9.3/2 at 0.70).
- c = 0.97(4) and 1.04(6), "one massless mode": **partly supported**. The 4% precision comes from fixing the O(L⁻³) term at its Nambu-Goto value (Major 1).
- The next term −π²/72σL³ is visible: **partly supported**. With c = 1, its coefficient is 3.1(6) against 3.0 at β = 0.73, but 2.4(7)-4.0(12) against 1.3 at β = 0.70.
- 6(2)% above the square root at L√σ = 1.28: **supported**; my new runs give 5.0(1.3)%.
- Within 2% for L√σ ≥ 1.5: **partly supported**. It holds on the L ≥ 6 lattices; a continuum extrapolation puts the excess at 2-4% for L√σ = 1.40-1.50 (Major 2).
- The tube survives beyond L√σ = 1.023: **supported**; E0 = 0.383(20)√σ and 0.332(15)√σ, both inside the window.
- Linear vanishing with ν = 1.01(2), 0.98(2): **partly supported**. Over the fit choices ν = 1.00 ± 0.07, from points with ξ/N_t ≤ 3 (Major 3). A square-root approach is excluded under every choice.
- T_c/√σ = 1.105(14), 1.152(26), 1.175(33), and 1.19(3) extrapolated, so T_c > T_H in this theory: **supported**. Each N_t lies 6-9σ above T_H; the N_t = 2 error is somewhat low (Minor 4).
- SU(2) β_c: **supported**, apart from a ±0.002 systematic from the way runs are joined. T_c/T_H = 0.87-0.93 "and rising": **partly supported**, because the choice of tension estimator moves these values by 0.02-0.05 (Major 4).
- Section 6, b three standard errors below π/24 from R = 4: **partly supported**; the distance is 2.3-3.2σ across the possible closed-tube tensions (Major 5).
- 87 of 100 hours, pilots included: **supported**. The recount is exact; one pilot's charge cannot be verified (Minor 8).

## Major issues

1. **c = 1 to 4% holds only inside the Nambu-Goto model.**
   - The fit "square root, c free" fixes every term after −πc/6L. Yet §2.1 says a stiffness term can enter at L⁻³, the same order as the first Nambu-Goto correction.
   - I fitted σL − γ/L − κ/L³ with κ free. γ and κ correlate at −0.96 to −0.99, and c = 6γ/π comes out as:

     | Fit range | c at β = 0.73 | c at β = 0.70 |
     |---|---|---|
     | L ≥ 6 | 0.99(12) | 1.09(15) |
     | L ≥ 7 | 0.61(21) | 0.69(26) |
     | L ≥ 8 | 0.59(31) | 0.67(37) |

   - The leading term alone gives c = 1.10-1.16. The paper's own ranges and variants already span c = 0.878(99) to 1.085(45).
   - So the data establish the Casimir term and exclude c = 0 and c = 2. The 4% figure needs the L⁻³ term to take its Nambu-Goto value, which the paper takes from the model (see Era discipline).

   *Change:* State the higher-order assumption next to every quoted c and give the κ-free result. Add the range, window and dispersion variants as a systematic of about ±0.1. Rewrite "its size is that of one massless mode" and the abstract to match.

2. **Claim (ii) describes the L ≥ 6 lattices; a continuum reading needs an extrapolation.**
   - At L√σ ≈ 1.32 the ratio to the square root is 0.942, 0.978, 1.017 and 1.044 for L = 3, 4, 5, 6.
   - The paper reads these offsets as lattice artefacts of relative size 0.5/N_t². That model predicts 0.986 for L = 6, against 1.00-1.04 observed, and the paper never fits it.
   - I fitted r∞ + a/L² at fixed L√σ to the stored scaling curve (χ² ≤ 1.7 for 2-3 degrees of freedom):

     | L√σ | r∞ |
     |---|---|
     | 1.35 | 1.057(17) |
     | 1.40 | 1.036(13) |
     | 1.45 | 1.027(12) |
     | 1.50 | 1.024(18) |
     | 1.55 | 1.016(16) |

     On this reading the departure from the square root begins near L√σ = 1.5, so "within 2% for L√σ ≥ 1.5" sits right at its boundary.
   - Each column of Table 7 is a single integration path, so its offset is one random draw, and all columns share σ(K) from the N_t = 16 path. For example, the L = 7 column lies 1-2% below L = 6 and L = 8 at both couplings, about one path error.
   - The 6(2)% at 1.28 belongs to one lattice spacing, a√σ = 0.21.

   *Change:* Add the fixed-L√σ extrapolation, with its assumed form and at least one alternative, and carry it into the abstract and Section 8. State which lattice spacing each quoted percentage belongs to.

3. **ν is an effective exponent from the crossover between three and two dimensions.**
   - The window keeps E0 ≥ 0.100 at N_t = 4 and E0 ≥ 0.114 at N_t = 3. The fitted points therefore have ξ/N_t = 1/(E0·N_t) running from 2.5 down to 0.6 (N_t = 4) and from 2.9 down to 0.9 (N_t = 3). The two-dimensional regime needs ξ ≫ N_t.
   - Neighbouring E0 values on a path correlate at 0.996-0.998, so the correlated χ² is really testing the increments between couplings.
   - Varying the range (r ≤ 0.06 to 0.20), fixing or freeing K_c, and adding a factor (1 + bt) gives ν from 0.91(9) to 1.07(5) at N_t = 4, and from 0.92(8) to 1.07(4) at N_t = 3. The wide-range N_t = 3 fit has p = 0.013-0.025.
   - What these fits show is "linear to about 7%". The two-dimensional Ising class rests more firmly on the cumulants: U = 0.61-0.62 and 1/ν = 0.80(15)-0.98(13), against 1.59 for three-dimensional Ising and 2 for mean field.

   *Change:* Quote ν with the spread over fit choices, and plot the local exponent against ξ/N_t. Repeat the two points nearest K_c on a lattice with E0·L_y ≥ 5. Base the abstract's "the value of the two-dimensional Ising model" on the cumulants.

4. **SU(2): the tension estimator moves T_c/T_H by as much as the effect being claimed.** The three tensions come from three different procedures:
   - **β = 2.17 (N_t = 3).** The Cornell fit includes R = 1, where a√σ = 0.53. R = 2-5 gives σ = 0.2724(64); R = 2-4 gives 0.2732(51) at T = 1 and 0.259(16) at T* = 2, where the 1978 rule puts T*. N_t = 3 then moves from 0.627 to 0.640-0.655.
   - **β = 1.88 (N_t = 2).** The T = 1 potential fits give σ = 0.61-0.62, and χ(3,3) = 0.595(54), against the χ(2,2) = 0.696 the paper uses. N_t = 2 becomes 0.635-0.650.
   - **N_t = 4.** The 1978 fits behind it also include R = 1. With R ≥ 2 the tension at β_c is 0.1427-0.1448 instead of 0.1513, giving T_c/√σ = 0.657-0.662, i.e. 0.95-0.96 T_H.
   - With R ≥ 2 at N_t = 3 and 4, the 1/N_t² line ends at 0.98-1.00.
   - The ±0.03 assigned in Section 5 is smaller than the χ(3,3) shift at N_t = 2 (+0.049). At β = 2.17, χ(3,3) lies above both the fit and χ(4,4) = 0.291(23), so that variant is biased.
   - β_c itself shifts by about 1σ with the run-joining rule. Nearest-run weights, or a ±0.010 window, give 2.1702 and 2.2900 for N_t = 3 and 4.
   - Finite-size control is weak:
     - only two volumes enter;
     - at N_t = 4, L = 8 is just twice N_t;
     - the cumulants at the crossings scatter from 0.39 to 0.52;
     - at ±0.014 the L = 12 reweighting reaches 1.3-1.7 action standard deviations.

   *Change:* Apply one fit rule (R ≥ 2, or a fixed R√σ window) at all three couplings, the 1978 ones included. Tabulate T_c/√σ under each variant, with asymmetric errors. Add the joining-rule spread to β_c. Restate the result as T_c/T_H = 0.87-0.94, 0.91-0.95 and 0.93-0.96 for N_t = 2, 3, 4, leaving both the rise with N_t and the continuum ordering open. A third volume at N_t = 2 costs about 10% of the cap and fits in the 13 remaining hours.

5. **Section 6 constrains b using only the statistical error of a model-dependent tension.**
   - σ = 0.04566(11) is the c = 1 square-root fit from L ≥ 8. The other closed-tube forms in Table 6, and the continuum dispersion, give 0.04533-0.04577, three to four times that error. b is strongly anticorrelated with σ.
   - Refitting with each of these tensions, b from R = 4 is 0.1143-0.1201, i.e. 2.3-3.2σ below π/24, and b = π/24 on its own has p = 0.10-0.28. With σ = 0.04566(30), b = 0.1153(57), 2.8σ below.
   - From R = 3 every variant gives b = 0.098-0.103 with p = 0.02-0.12, and π/24 + d/R² fits throughout.

   *Change:* Carry the model spread of the closed-tube tension into the constraint, and replace "3 standard errors below π/24" by the range. The conclusion that the constraint sharpens both readings without choosing between them then stands.

## Minor issues

1. **End-correction claim (§3.3).** "The correction is below 0.008 at every coupling quoted" is false.
   - At β = 0.73 the end correction to F is −0.0134 for 8d (which enters the N_t = 8 average), −0.0115 for 8c, −0.0085 for L = 5 and −0.052 for L = 4.
   - Along the paths it reaches 0.070 (L = 16, K = 0.225).
   - Inside the window it moves E0 by at most 6×10⁻⁴. Its noise, which comes from the variances, is missing from the covariance; the paper should say so.
2. **F(0.15).** "F < 10⁻³" at K0 = 0.15 holds only for L_y ≥ 12. On 24×8 the integral from 0.15 to 0.20 is 0.149(22), and an exponential fit of the integrand gives F(0.15) ≈ 2×10⁻³, which is 10⁻⁴ in E0.
3. **Window rule and what the 2D checks test.**
   - The window ignores the aspect ratio. In 2D the error of (4) depends only on E0·L_y and L_x/L_y:

     | E0·L_y | Error for L_x/L_y = 1, 1.5, 2, 3, 4 |
     |---|---|
     | 3 | 0.5, 0.8, 1.0, 1.3, 1.4% |
     | 3.5 | 0.2-0.7% |
     | 5 | 0.02-0.12% |

     State the rule in terms of both quantities.
   - Table 2 tests the factor ½, the doubled momenta and Onsager's exact dispersion, for a wall with no internal states. Say that the three-dimensional parts rest on the N_t = 8 comparison.
   - E1 − E0 ≈ 4π/L applies only at zero longitudinal momentum. Z_A also contains the N = 1, N̄ = 0 states, 2π/L up; their weight here is at most 2×10⁻⁴.
4. **Cumulant-crossing errors.**
   - The bootstrap throws away samples with no crossing: 12/200 at N_t = 2 and 24/200 in the 2D check. Those errors are therefore low; if the lost samples are Gaussian tails, about 0.0016 instead of 0.0012 at N_t = 2.
   - At L = 48 the ±0.003 window spans 1.1, 1.6 and 2.0 action standard deviations for N_t = 2, 3, 4. The safeguard in Appendix D therefore covers only about ±0.0015 at N_t = 3 and 4.
5. **Numbers computed by hand.**
   - SU(2) 0.96(4): its error leaves out the ±0.03.
   - "1.6(9)%": the stored values give 1.7(9)%.
   - "22(3)%" and "6(2)%".
   - Table 7 exists only in summary82.json, and four error digits there differ by one unit: 0.942(14), 0.978(20), 1.017(18) at 1.31-1.33, and 1.005(11) at 1.57.

   Print all of them from analyze82.py.
6. **Missing material.** kaufman_lnZ cites a checks82.py that is not in the package. The pilot findings quoted in §§3.1 and 3.4 (0.168(5) against 0.1677; same-chain differences "ten times smaller") have no stored output. Add both.
7. **Text corrections.**
   - §3.5: the block counts are 72-304.
   - The 2D crossing cumulants span 0.58-0.63; the 24-32 pair gives 0.632, with no error.
   - §3.4: the last step lies below the dual value for L = 8 (0.288(21) against 0.2931) and L = 16 (0.678(18) against 0.6935). Both are within errors, but "from above" needs qualifying.
   - Appendix B: the "four lattices of length 8 in the gauge theory" are dual-model lattices.
   - At β = 0.70 the L = 5 tube (L√σ = 1.63) lies 2.1% below the square root.
8. **Budget.**
   - The direct method took 7.25% (3.13×10¹¹). The quoted 7.6% includes path_p8, which is a pilot for the dual model.
   - The eight lattices of slow_modes.py are not recorded, so its 1.3×10¹¹ cannot be recomputed. On the eight z2t geometries the floor would be 1.6×10¹¹ with one start each, or 3.2×10¹¹ with both starts; the total would then be at most 3.96×10¹² (92%).
   - samechain82.py recounts to 3.8×10⁹, against 3.5×10⁹ charged.

## Checks I ran

All in a scratch copy of the snapshot.
- **Reproduction.** `analyze82.py`, `hagedorn.py` and `gauge_check.py` reproduce analysis82.txt, summary82.json, the three figures, hagedorn.txt and gauge_check.txt byte for byte. Every number in the abstract and in Tables 1-6 and 8-12 matches.
- **Kaufman code.** `kaufman_lnZ` against exact enumeration of five small tori, three couplings and four boundary conditions: largest difference 4.9×10⁻¹³.
- **Independent replicas.** Pulls of ⟨S⟩_P − ⟨S⟩_A: q16/q16r rms 0.84 (χ² = 18.9/27), q12/q12r 0.87 (20.7/27), c2d/c2dr 1.09 (24.8/21). E0(β = 0.73) from each replica: 0.6910(45) and 0.6954(41) at L = 16; 0.5082(38) and 0.5003(39) at L = 12.
- **Thermalization.** First fifth against the rest, in all 1140 runs: rms pull 0.89, 3.3% beyond 2σ, 0.2% beyond 3σ.
- **Integration grid.** Dropping every other coupling above K = 0.20 changes F only within noise (χ² = 14.2/22). The Euler-Maclaurin term at β = 0.73 is at most 0.013 in F.
- **Formula (4) in 2D and 3D.** I mapped (4) against Kaufman for L_y = 8-32 and L_x/L_y = 1-4 (Minor 3). Fitting the four N_t = 8 lattices to that error shape gives a 3D/2D ratio of 1.34(21), 0.88(29) and 0.64(38) at K = 0.2325, 0.235 and 0.2366.
- **New simulations,** with the paper's programs, fresh seeds and K = 0.15-0.24:
  - N_t = 6 on 32×20 gives E0(0.73) = 0.1732(36), against the paper's 0.1745(33);
  - on 32×28 (E0·L_y = 4.8) it gives 0.1710(48);
  - all three together lie 5.0(1.3)% above the square root.
- **Refits.** Tables 6, 7, 9 and 11, the SU(2) tensions from the stored loops, and the SU(2) crossing under other joining rules, as reported in Majors 1-5.
- **Film cumulants.** Cold and hot chains, and the two halves of each chain, agree within 1.8σ.
- **Budget.** The stored flop fields match the cost model exactly: paths 1.799×10¹², films 1.705×10¹¹, SU(2) 1.429×10¹². Total 3.775×10¹², or 87.4%.
- **Not completed.** I stopped the reruns of gauge_nt1_check.py and samechain82.py before they finished, so the pilot numbers they produce stay unverified (Minor 6).

## Era discipline

Appendix D declares the two-level average, smearing, the Kennedy-Pendleton draw, the interface method (in outline), the wound-string reading of T_H, the citation form of [19], the 40Λ_L figure, the remembered centres and the remembered outcomes. The remembered centres did no visible harm: the crossings fall 0.4-0.6σ from them, and no bootstrap sample shows two crossings.

Undeclared items:
- (a) Section 5's Wilson loops use the 1978 `wilson_loops`, with the one-link average (Parisi, Petronzio and Rapuano, 1983) and two or four smearing steps (APE, 1987). Appendix D confines smearing to §§3.1 and 3.4 and does not mention the one-link average.
- (b) `tau_int` stops its sum at a self-consistent window W ≥ 6τ, which is Madras and Sokal (1988). Every block length in §§3.5 and 5 follows from it.
- (c) `binned_error`, which merges blocks pairwise and keeps the largest error, is the blocking analysis of Flyvbjerg and Petersen (1989).
- (d) As I recall, Binder's 1982 paper in [27] obtains the tension from the order-parameter distribution. If neither item in [27] integrates the periodic-minus-antiperiodic difference, that method (Mon and Jasnow, 1984) belongs in Appendix D.
- (e) As I recall, Nucl. Phys. B 210 appeared in December 1982; [13] should then be cited as a preprint.

Two conclusions lean toward remembered outcomes:
- c = 1 at 4% presumes the later universality of the closed string's L⁻³ term (Lüscher and Weisz, 2004; Aharony and Karzbrun, 2009); see Major 1.
- The SU(2) phrase "within a few per cent of each other" leans toward the remembered T_c/√σ ≈ 0.7, whereas the lattices give 0.87-0.96 T_H (Major 4).

Under our standard neither counts as evidence. T_c/√σ ≈ 1.2 and the cumulant value 0.61 both follow from the data unaided.

## Recommendation

**Major revision.** The analysis reproduces exactly, the error bars pass the replica tests, and formula (4) holds inside its window. Three results survive my checks:
- the closed tube has a Casimir term;
- the tube lies 5% above the square root at L√σ = 1.28, which I reproduced with new runs;
- in the three-dimensional Z2 theory, T_c is above T_H at every N_t.

Five results each depend on a choice the paper makes without saying so:
- the precision of c;
- the continuum reading of Table 7;
- the exponent ν;
- the SU(2) ordering;
- the Section 6 significance.

Making those choices explicit widens the errors as set out in Majors 1-5.
