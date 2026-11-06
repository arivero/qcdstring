# Referee report: QCDS-80/1

*Second-line referee (astra-6.0); the three paper folders and the second line's package only.*

## Summary of the submission

The preprint studies the flux tube of the three-dimensional Z2 gauge theory at β = 0.73 and 0.70. Generalized Wilson loops with symmetry-projected operators on the frozen slices of the 1976 two-level scheme give T = 0, 4, 8, 12; a 2×2 generalized eigenvalue analysis uses T0 = 4, T = 8. The paper finds the one-phonon gap 6-10σ below π/R and 15-19% above the Nambu-Goto square root, attributes the excess to contamination, and quotes agreement "within 20%". It reads correlated ground-state fits to R√σ = 1.9 as π/24 plus an endpoint term, d√σ ≈ 0.011. The slope of an Ising interface width in ln L crosses 1/π² at K_R = 0.413(2). Budget: 60 of 100 Cray-1 hours.

## Assessment of the main claims

- Ground state to 0.2-2% for R ≤ 9: **supported**; it agrees with the 1976 data (χ² = 6.7/9).
- First excitation to 3-6%: **unsupported**; that is the statistical error of an upper bound that moves 15-20% between time windows (Major 1).
- Gap 6-10σ below π/R for R√σ ≤ 1.3: **supported** and robust, since these energies bound the level from above (correlated χ² = 120/5).
- Gap within 20% of the square root: **partly supported**, from above only; the main window rejects the square root at p = 0.002 (Major 1).
- Levels n ≥ 2 unresolved: **supported**.
- π/24 plus one endpoint term, d√σ ≈ 0.011 at two couplings: **partly supported**; from R = 3 a single 1/R coefficient fits equally well, and the precision of d comes from R = 2 (Major 2).
- K_R = 0.413(2): **partly supported**; the crossing reproduces; its error omits a one-sided finite-size bias of similar size (Major 3).
- 60 of 100 hours: **supported**.

## Major issues

1. **The first excitation is an upper bound.** At β = 0.73 the two (−,+) operators are correlated at 0.986-0.990 at T = 4, so the GEVP returns the single-operator value (0.811 against 0.812 at R = 5). At most 41-44% of the operator's norm sits in the lowest state, against 81-91% for the ground-state operator. The effective energy keeps falling: at R = 5 it is 1.009(3), 0.811(21) and 0.663(116) for the windows 0-4, 4-8 and 8-12, and 0.737(57) for T0 = 4, T = 12. With the correlated jackknife, the T0 = 4, T = 8 gaps for R = 3-7 exceed the square root by 0.070(20) (χ² = 19.1/5, p = 0.002; insensitive to σ). A two-state description of the three windows admits E1 from 0.47 to 0.77 at R = 5 (χ² < 1; the square root gives 0.746). The proposed three-phonon contaminant would need 1.5-2.5 times the target state's weight in the operator, and a single state at the Nambu-Goto n = 3 spacing cannot produce the drop between the first two windows (χ² = 4.1, 11.8, 27.4 for 1 dof at R = 4, 5, 6). In the 8-12 window `nanvar` silently drops 48 of 480 jackknife samples at R = 5. *Change:* quote E1 and the gap as upper bounds; replace "within 20%" by the correlated test and the allowed range; build a (−,+) basis of distinct operators (a sin 3π(j+½)/R profile for a₃†, a two-bump operator for a₁†³, other smearing levels); measure T = 1-6 with conventional loops (C(4)/C(0) ≈ 0.02).

2. **The endpoint reading rests on R = 2.** From R = 3 the data have no preference: free b gives 0.093(6) with p = 0.78, π/24 + d/R² gives p = 0.91, and jointly with 1976 p = 0.66 and 0.80. The "change with every new starting point" is 0.093(6) to 0.108(18) between R = 3 and 4, under 1σ. The 2% error of d√σ = 0.0110(2) comes from R = 2 (R√σ = 0.43); from R = 3 it is 0.0097(14). The 1980 couplings differ by 2.1σ, against "within two standard errors"; at matched R√σ ranges the joint 1976+1980 values are 0.0107(10) and 0.0083(12). The abstract sets the b,d-free value against 1976's fixed-b value; the like-for-like 1976 number is 0.0099(32). A d/R² term also mimics shifting R by 24d/π ≈ 0.4 lattice spacings, a lattice-sized effect. The ground state repeats the 1976 reach (R = 9) with errors 1.2-1.8 times smaller at R ≥ 7, and b from R ≥ 4 is as uncertain as in 1976: 0.108(18) against 0.101(17). *Change:* present the two readings as equal; fit 1976 and 1980 jointly; quote d at matched ranges; drop "pushes the ground state to R√σ ≈ 2".

3. **K_R carries a one-sided bias.** 1/π² is the L → ∞ slope at roughening. On the critical Kosterlitz flow the effective slope approaches it from above (a ln ln L term in w²), so a crossing at L ≤ 64 falls on the smooth side. The BCSOS model, whose roughening point is exact (van Beijeren [15]: K_R = ½ ln 2), calibrates this inside the programme. My heat-bath runs at L = 16, 32, 64 give a slope of 0.1142(12) at K_R, 13% above 1/π² (0.116 for 16-32, 0.111 for 32-64), and still 0.1037(13) at 1.04 K_R. The Ising slopes at K = 0.41 (0.120, 0.114) follow this pattern, and the Ising slope reaches 0.114 at K ≈ 0.4107. *Change:* present 0.413 as an upper estimate with a calibrated systematic (BCSOS or the Kosterlitz finite-size form), carried into β_R and the abstract.

## Minor issues

1. Sections 1 and 6 quote superseded 1978 numbers (54 ± 3; 10.33, 10.60, 10.55 GeV): the revised preprint gives √σ = (54 ± 4)Λ_L, 3S at 10.351 and 4S at 10.618 GeV, and leaves the 4S position relative to threshold open.
2. The text conflates level n with phonon number: (−,−) starts with a₂†, a single phonon, and the n = 3 states of (−,+) are a₃† and a₁†³. Correct "the level with two phonons", "which carry two and three phonons" and "states with three phonons". The symmetry table is right.
3. The second production has no (+,−) channel ("in either production"), and at β = 0.70 its normalized C(4) exceeds 1 for R ≥ 7.
4. At R ≤ 4 the square root fails for the ground state (χ² = 42.8/4 from R = 4); say what the tabulated gap prediction means there.
5. The 20-block Ising errors run about 20% low at L = 64 (τ_int ≈ 15 measurements at K = 0.41).
6. Keep the smearing tests, as in 1976; restate that the charges are floors; give the memory (about 0.6 M words for the two-operator run, within a 1 M-word Cray-1).
7. The 1976 triplet shift of 47 MeV implies a hyperfine splitting of 188 MeV and an η_c near 2.91 GeV, 70 MeV below the candidate. Report this beside the agreements.

## Checks I ran

In a scratch copy:
- `checks80.py`: both deviations 0.00e+00. `analyze80.py`: output identical to `analysis80.txt`.
- Estimator: the operators use only frozen-slice links, and the slabs are conditionally independent given them, so the estimator is unbiased. E0 matches the Polyakov-line V within 3×10⁻⁴ (R ≤ 5) and the 1976 data (χ² = 6.7/9 at β = 0.73, 3.0/6 at 0.70).
- Ground-state E(4→8) − E(8→12): 0.0018(9) at R = 5, 0.0066(95) at R = 9; about a tenth survives at T = 8-12, below the errors.
- Errors stable for blocks of 1-150 configurations; GEVP, two-state and joint fits as above.
- Ising: the halves of all 27 runs agree within 2σ. For K ≥ 0.40 and L ≥ 16 the interface stays at least 5 layers (6 widths) from the fixed layers. Bulk flips add an L-independent constant to w², so the width definition is sound.
- BCSOS heat bath at K = ½ ln 2 and 0.36: 4 chains × 3×10⁴ sweeps per L.

## Era discipline

Appendix B flags the methods, Arvis' square root and the LINPACK rate. No remembered number enters a calculation. Undeclared items:
(a) the logarithmic widening of the tube (§5) is Lüscher, Münster and Weisz (1981); derive it or flag it;
(b) "10.355" and "about 10.58 GeV" look like later calibrated masses; as I recall, the 1980 letters used CESR's energy scale of the time, with the fourth level near 10.55 GeV;
(c) the evidence that the Υ''' decays to b-flavoured mesons (CLEO's leptons) appeared in January 1981;
(d) the square root follows in a page from the 1973 light-cone method; derive it.

Two readings lean toward remembered outcomes: the main-window excess over the square root is attributed to contamination the data do not exhibit, and the π/24 endpoint reading is adopted where the data are neutral. Under our standard neither counts as evidence. The budget reproduces (2.58×10¹² operations) and is plausible for floor charges.

## Recommendation

**Major revision.** The estimator is valid, the data reproduce, and the exclusion of π/R is robust. The square-root comparison, the endpoint reading and the error on K_R need the changes above.
