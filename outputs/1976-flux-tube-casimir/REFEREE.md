# Referee report: QCDS-76/1

*Second-line referee (astra-6.0); paper folder only.*

## Summary of the submission

The preprint derives the zero-point term −π(d−2)/24R of a string with fixed ends, checks it with three regulators and a harmonic chain, and argues that a lattice-pinned tube has only an exponentially small analogue. It then reports Monte Carlo runs on a CDC 7600 budget: 3D Z2 Creutz ratios against the strong-coupling series to O(u⁴); static potentials at β = 0.70 and 0.73 from correlators of closed time-like lines with two-level averaging, giving 1/R coefficients 0.104(16) and 0.073(8), below π/24 and "rising with R"; a 4D compact U(1) scan in which the area law ends near β = 1.0; and a charmonium fit returning σ = 0.86 of the Regge tension, with a registered ³D₁ level at 3.79 ± 0.03 GeV.

## Assessment of the main claims

- Regulator-independent coefficient: **supported**, reproduced to six digits. Corrections starting at O(R⁻³): **unsupported** (Major 2).
- Z2 tension follows the O(u⁴) series at β ≤ 0.30: **supported** at 0.2% precision.
- V(R) to 0.2-2% up to R = 8: **supported**; independent code reproduces R ≤ 4.
- A 1/R term with the Casimir sign: **supported**, more firmly than shown.
- b = 0.073(8), 7σ below π/24, growing over 0.4 < R√σ < 1.8: **unsupported**; it rests on R = 2 and uncorrelated fits.
- U(1) area law ends near β = 1.0: **partly supported**; the hysteresis is one point.
- One tension within 15%: **partly supported**; the tolerance is set after the fit.
- ³D₁ at 3.79 ± 0.03 GeV: **partly supported**; the error omits open-charm coupling.

## Major issues

1. **Correlated data, uncorrelated fits.** Neighbouring V(R) are correlated at 0.98 (jackknife covariance, 120 blocks); Table 6's χ² ignores this. With the covariance, the β = 0.73 free fit over R = 2-8 has χ² = 13.1/4 (p ≈ 0.01). Over R = 2-8, 3-8, 4-9 the correlated b is 0.070(1), 0.085(5), 0.101(17); the uncorrelated values are 0.073(8), 0.064(27), −0.002(98). b = π/24 is rejected when the fit starts at R ≤ 3 (β = 0.73) or R = 2 (β = 0.70), and acceptable from R = 4 (χ² = 6.4/4) and R = 3 (0.1/2) respectively. b = 0 fails every range at β = 0.73 (39/4 from R = 4) and has p = 0.016 for R = 3-6 at β = 0.70. *Change:* fit with the covariance, tabulate b against R_min, delete "7σ".

2. **Endpoint operators.** §2.1 counts operators in the worldsheet interior. An operator on the endpoint world lines, b₁(∂ₓX)² at x = 0 and R, is equally local and shifts E₀ at first order by −b₁(d−2)π/6R². Eq. (1) needs a symmetry excluding it, or the fits need an R⁻² term. The data accept one: σR + c − π/24R + d/R² fits R = 2-8 at β = 0.73 (χ² = 3.7/4) and R = 2-6 at β = 0.70 (0.4/2), with d√σ = 0.0111(2) and 0.0094(16), equal within errors; freeing b too gives b = 0.124(17) at β = 0.73. The data cannot separate "b rises toward π/24" from "b = π/24 plus R⁻²". *Change:* add the endpoint analysis; report both forms.

3. **The local coefficient.** The claimed growth comes from the R = 2 values, which use V(1). Without them, local b at fixed β moves by 1σ (0.074(2) to 0.083(8) at β = 0.73); the R = 5 value, 0.067(30), is plotted in Figure 2 and absent from the text. At R√σ ≈ 0.65 the couplings give 0.0740(21) and 0.0634(9), a 4.6σ scaling violation that the text calls agreement "to about 20%"; the second value also falls below half of π/24, against the bound stated for 0.6 < R√σ < 1.3. Beyond R√σ ≈ 1 local errors reach 0.03-0.05. R√σ ≈ 2 is within reach at β = 0.73: R = 9 has R√σ = 1.99 and C ≈ 8×10⁻⁵, measured to 28%. *Change:* confine the claims to R√σ ≲ 1; drop "toward the free-string value" from §6.

4. **Nambu-Goto rows.** At β = 0.73 the fitted σ = 0.0396 makes σ²R² − πσ/12 negative at R = 2, where analyze.py clamps the square root to 10⁻⁶. The form still fails from R = 3 at β = 0.73; at β = 0.70 it fits R = 3-6 (correlated χ² = 1.0/2). *Change:* fit it only where it is real (R√σ > 0.51).

5. **Charmonium.** Fit (a) has three parameters for three levels; the 15% tolerance stands for a model error the paper never computes. The vector exchange invoked to order the χ states carries a spin-spin term that, at fit (a) parameters and first order, puts ψ and ψ′ 47 and 30 MeV above their spin-averaged levels. Lowering them by 25/12.5 or 50/25 MeV gives σ = 0.151 or 0.143 GeV² (0.82 or 0.77 of Regge); the D-wave stays at 3.80 GeV. The ³D₁ sits 50-75 MeV above open-charm threshold, the paper's reason for setting aside 2P and 3S. *Change:* state the model error first, include spin-spin shifts, and estimate coupled-channel shifts for ³D₁ or drop its error bar.

## Minor issues

1. Table 4 uses n_sub = 20 (unstated), N_t ≤ 8, two slabs and C ≥ 0.009; production uses n_sub = 500, four slabs and C to 10⁻⁴. Add a direct cross-check at production parameters. The difference errors are 3.4-11 times smaller (text: 5-10).
2. Mean |tanh βh| on time-like links is 0.93 (β = 0.73) and 0.90 (0.70), with 4-7% at h = 0; show the test behind "gains nothing".
3. U(1): the hysteresis is one point (β = 1.00, 8⁴, 100 sweeps), where the plaquette autocorrelation time (10⁴ run) is about 22 sweeps; first order needs two-state signals at fixed β. The 10⁴ runs start hot below β = 1.0 and cold above: state it and run β = 1.00 from both. For square loops a Coulomb potential gives χ(R,R) ≈ 2α/R(R−1), twice the stated value.
4. α′ = 0.865 needs a citation; charmonium76.py points to numerics/regge_fit.py, outside the package. The pilot runs (14% of the cap) belong in results/.
5. Give the 1976 charmonium masses with errors from [20]; cite K_c = 0.2217; display the Nambu-Goto square root that §3.4 attributes to §2.3. In the abstract, say 91 hours and drop "beyond β ≈ 0.45" (the series already misses by 6σ at β = 0.40).

## Checks I ran

All runs used a scratch copy.
- casimir.py, charmonium76.py, analyze.py: outputs identical to the recorded ones.
- Correlated refits of the 24 NPZ files, stable for blocks of 2-10 configurations. Blocking from 1 to 50: errors are steady to blocks of 10, so the 120-block jackknife is sound; whole-chain blocks give up to 35% more at R ≥ 6, near the noise of a 12-block estimate.
- multilevel_polyakov and the inline estimator of z2_validate.py agree to machine precision on identical chains.
- My own Z2 heat bath (site-parity checkerboard, no shared code), direct correlator, 8 chains × 10⁴ sweeps. β = 0.73: V(1-4) = 0.12810(19), 0.20535(48), 0.26660(95), 0.32258(182), pulls +0.8, +0.5, +0.3, +0.6 against Table 5; β = 0.70, R ≤ 3: pulls +0.7, −0.6, −0.2; plaquettes agree. In the paper's cost model this costs 7 hours and, per hour, beats two-level averaging for R ≤ 4.
- Numerov shooting reproduces both charmonium fits to 0.1 MeV; hyperfine shifts use the fitted |R(0)|². Operation counts match Table 9.

## Era discipline

Declared memory items (two-level averaging, one-link average, the LINPACK rate, ledger expectations) follow the rules; no remembered physics number enters a calculation. Undeclared later material: (a) "Creutz ratio" is a 1980 name; (b) the fixed-end Nambu-Goto closed form in Table 6 dates from the 1980s: derive it (light-cone gauge, Dirichlet ends) or flag it; (c) §2.1's universality argument restates a 1980 result and inherits Major 2; (d) u1_4d.py uses numpy's von Mises sampler; a 1976 uniform-proposal rejection sampler needs 4-6 trials per update at β = 0.8-1.2, straining the 300-operation charge; (e) charmonium76.py's solver check uses M(ψ) = 3.097 GeV and κ = 0.52, values with no 1976 source.

Three claims lean toward outcomes both groups remember: b approaching π/24, a first-order U(1) transition, and the ³D₁ registration. Under our standard none counts as evidence; a prediction whose outcome the authors know carries no weight. Every number I tested is reproducible from the package except α′ and the pilot findings.

The budget arithmetic is consistent; its charges are floors (no memory traffic, indexing or random-number cost), and the β = 0.73 run as coded holds 49,152 links and 81,920 accumulators, which Appendix A should fit to the machine. Nine hours of headroom absorb a 10% underestimate. Measuring U(1) loops every second sweep used 19% of the cap; every tenth sweep would fund about 50% more statistics at β = 0.73.

## Recommendation

**Major revision.** The derivation is sound, and independent code reproduces the static-potential data. The quoted coefficient, its 7σ distance from π/24 and its growth with R come from the R = 2 point and uncorrelated fits. Analysed with the covariance and an R⁻² term, the same data establish a 1/R term of Casimir sign and agree with the free-string value for R√σ ≳ 0.9. Rebuild §3.4, the abstract and §6 on correlated fits, add the endpoint analysis, and give the charmonium comparison with its model error.
