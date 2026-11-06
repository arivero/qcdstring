# Referee report: QCDS-78/1

*The 1976 preprint was revised during this review; I cite its `paper.md` of 6 Nov 2026, 21:33 CET.*

## Summary of the submission

The preprint simulates four-dimensional SU(2) lattice gauge theory on 8⁴ to 16⁴ lattices for 1.5 ≤ β ≤ 2.6. An 8⁴ thermal cycle shows no hysteresis, and plaquette fluctuations peak at β = 2.1-2.2. Wilson loops with one-link averages and smeared spatial sides give σa² from 1.003 to 0.0227. The two-loop ratio √σ/Λ_L falls from 66.6 at β = 2.2 to about 54, read as asymptotic scaling from β = 2.4 with √σ = (54 ± 3)Λ_L. The 1/R coefficient at β ≥ 2.4 is 0.25-0.29, near π/12. Section 7 counts the ψ(3772) as a confirmed 1976 prediction, finds that two 1976 potentials bracket Υ′−Υ, and registers bottomonium levels and the open-bottom threshold.

## Assessment of the main claims

1. No bulk transition on 8⁴: supported for a jump of the U(1) size; "crossover" needs a second volume.
2. Nonzero tension up to β = 2.6: supported, for R√σ ≤ 1.3.
3. Series −ln u − 4u⁴ + O(u⁶), good to 1% for β ≤ 1.6: supported.
4. √σ/Λ_L drifts down from β = 2.2 to 2.6: supported; its size depends on analysis choices.
5. Two-loop scaling reached from β = 2.4, √σ = (54 ± 3)Λ_L: unsupported.
6. 1/R coefficient 0.25-0.29, consistent with π/12 plus a Coulomb share: partly supported; a T-systematic is missing.
7. ψ(3772) confirms the 1976 D-wave level: unsupported as evidence.
8. The 1976 potentials bracket Υ′−Υ: partly supported; true for fits (a) and (b), while (a′) and (a″) overshoot by 28%.
9. 82 CDC 7600 hours: partly supported; storage and pilot runs are unaccounted.

## Major issues

1. **The scaling test has almost no leverage.** From β = 2.4 to 2.6, g² changes by 8%, and the two-loop factor moves aΛ_L by 3.4% relative to one loop, under half the 8% error on the end-point ratio. The one-loop ratios (170, 160, 165) are as flat as the two-loop ones. A fit of R∞(1 + cg²) to the three points gives R∞ = 21 ± 51. The data support "consistent with a constant over 2.4-2.6" and leave the continuum value and the two-loop coefficient untested. Rewrite Section 5 and the abstract accordingly; attach the unknown approach-to-scaling factor to (54 ± 3)Λ_L, Λ_L ≈ 8 MeV and a = 0.087 fm, or drop them.

2. **The plateau rests on hand-made choices.** Fit windows are set per β without a rule, e is free, and T* is the first agreement of σ(T) with σ(T+1). With e = π/12 at the same T*, the ratios at β = 2.4, 2.5, 2.6 become 59.0, 53.7, 52.6 (errors 0.7-1.0), a continued decline; free fits at the largest usable T give 52.6, 49.3, 54.1. Section 5 quotes the e-fixed value only at 2.6, where it lowers the ratio. Effective potentials approach their limit from above, so the T-systematic is one-sided, and Table 4's symmetric errors misplace the centres at 2.4 and 2.5. Match windows in R√σ, tabulate the variants, quote asymmetric errors.

3. **Statistical errors are too small.** At β = 2.5 and 2.6 the large loops have autocorrelation times of 3-5 measurements (25-40 sweeps); the jackknife blocks hold 4-5. With 5 blocks the error on σ nearly doubles (0.0013 → 0.0025 at 2.5, → 0.0023 at 2.6). Dropping the first quarter of the β = 2.6 run moves σ from 0.0227 to 0.0247. Block over several autocorrelation times and compare the cold start (200 sweeps) with a hot one.

4. **The finite-volume paragraph has the wrong sign and no measurement.** Section 5 says the β = 2.6 box (L√σ = 2.4) "can raise the tension" and measures this with the e-fixed fit. I ran the paper's `su2core.py` in smaller boxes. At β = 2.5, 12⁴ (L√σ ≈ 2.3) matches 16⁴ (tension ratios 0.98-1.03 ± 0.1); at β = 2.4, 8⁴ (2.1) lies 4-9% below 12⁴ at T = 2; at β = 2.6, 12⁴ (1.8) puts V(6) 0.040(8) below 16⁴ at T = 4 and the tension at 0.47-0.64 of its 16⁴ value. Small boxes lower σ, steeply below L√σ ≈ 2.2; the β = 2.6 point sits just above that onset. Replace the paragraph with a measured statement.

5. **The 1/R coefficient drifts with T, and the fixed-e test uses diagonal χ².** From T* to the largest T, e rises 0.287 → 0.337 (β = 2.4), 0.264 → 0.284 (2.5) and 0.248 → 0.263 (2.6). With the jackknife covariance, e = π/12 fits at T* give χ² = 22/2, 20/4, 33/4 against 0.6/1, 11/3, 1.8/3 for free fits (inflated by a 20-sample covariance; the ranking survives), so "as good as free fits" holds only at larger T. Add the T-systematic to e, fit with correlations, drop the three-dimensional Z2 analogy, and say that the Casimir share stays open.

6. **Section 7 must follow the memory rule and the revised 1976 preprint.**
   (a) That preprint now records the D-wave level without an error and says the record carries no weight as a test, because both lines remember where the level lies. Remove "the prediction holds" from Section 7 and the abstract.
   (b) It now has four fits. Fits (a′) and (a″), with the potential's own spin-spin term and the Υ treated like the ψ, give Υ′−Υ = 0.714 and 0.718 GeV, 27-28% above 0.56 GeV. The Υ′ discriminates among the 1976 fits; report all four.
   (c) The threshold 2(m_b + M_D − m_c) ignores the D*−D splitting, measured by 1977. Scaled by m_c/m_b, it raises both thresholds by 0.15 GeV and puts the 4S 0.10 GeV below threshold; the heavy-quark kinetic term pushes back by a similar amount. "4S broad" is undetermined, and ±0.07 GeV omits the method's error.
   (d) The authors remember the bottomonium spectrum: list it in Appendix B and call the registration a consistency record. A joint fit to ψ, ψ′, Υ, Υ′ (below) gives sharper numbers and tests the χ_c centre.

## Minor issues

1. The tension leaves the O(u⁴) series at β ≈ 1.7-1.9 (Table 2), before the fluctuation peak; correct the abstract and Section 3.
2. The specific heat comes from one volume, and for β ≥ 2.4 the 8⁴ box is in the regime of issue 4.
3. Table 4 switches from χ(3,3) (β ≤ 2.1) to fits (β ≥ 2.2); at 2.2, χ(3,3) exceeds the fit by 15%. Mark the switch.
4. The paper's numbers give a = 0.088 fm at β = 2.5; Rapidis et al. quote Γ = 28 ± 5 MeV; the 1P and 3S half-widths are rounded up from 0.084 and 0.073.
5. `analyze78.py` keeps vestigial T* values; Figure 2 shows statistical errors only.

## Checks I ran

- Reran `bottomonium78.py`, `analyze78.py` and `checks78.py` on a copy: output identical to `results/`. My re-analyses of the raw loops give the numbers quoted above.
- `su2core.py` is correct: staples, checkerboard, Kennedy-Pendleton draw, one-link average (⟨a₀⟩ = I₂/I₁ re-derived), smearing, loop paths. KS tests of the a₀ draw at βk = 0.3-15 pass (pooled pull 1.45 over 2·10⁷ draws). In a constant Abelian field the code returns W(R,T) = [cos(fRT) + 2]/3 to 10⁻¹⁶.
- Formula (1) and its SU(2) coefficients are correct (exponent 51/121); Table 4's aΛ_L reproduce. I re-derived −4u⁴ (four cube bumps per plaquette, group factor 1); the Z₂ centre allows only even powers, so O(u⁶) holds.
- New Monte Carlo with `su2core.py`, fresh seeds: β = 2.4 on 8⁴ (600 measurements), 2.5 on 12⁴ (100), 2.6 on 12⁴ (160); plaquettes match the paper's to about 10⁻⁴.
- Joint fit with the 1976 solver to ψ, ψ′, Υ, Υ′: κ = 0.515, σ = 0.168 GeV² (0.91 of Regge), χ_c centre 3.510 GeV (data 3.522); bottomonium 1P 9.93, 1D 10.17, 3S 10.35, 4S 10.62, threshold 10.57 GeV.

## Era discipline

Appendix B flags the three remembered algorithms, and every reference predates November 1978. Four lapses remain.

- "Creutz ratio" is a 1980 eponym; write "ratio χ", as the revised 1976 preprint does.
- The ψ(3770) and bottomonium spectra are remembered and unflagged; under rule (2) agreement with them carries no evidential weight.
- Ledger item P13 chose the couplings, as flagged. The reading "scaling reached from 2.4" then lands near that remembered expectation without support from the data, the influence rule (2) forbids.
- Budget: the operation count reproduces, and 500 operations per update is plausible within 20%. A CDC 7600 has 64K words of small core and 512K of large core; the 16⁴ gauge field alone needs 1.05M 60-bit words. State the packing or out-of-core scheme and charge its I/O, report the pilot runs that set the smearing levels, and carry the 1976 flag on 3.3 Mflop/s.

## Recommendation

Major revision. The programs are correct, every printed number reproduces, and the survival of the non-Abelian area law to β = 2.6 is a solid result. The scaling claim, the errors at β ≥ 2.4, the finite-volume paragraph and Section 7 need the changes above.
