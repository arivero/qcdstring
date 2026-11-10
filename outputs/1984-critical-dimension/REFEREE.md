# Referee report: QCDS-84/1

*Second-line referee (astra-6.0); the five paper folders and the second line's package only.*

## Summary of the submission

The preprint asks what the critical dimension says about a long string in any dimension, and answers without any new simulation. Section 2 derives the area action from the Lorentz invariance of the vacuum: flat sheets fix c₂ = −σ/8 and c₃ = σ/4. It then shows that the stiffness term is a total derivative plus a term that vanishes with the equation of motion, and places the first free bulk coefficient at σ⁻³L⁻⁷. Section 3 rules out the end term b₁(∂ₓX)² for a rotation-invariant source and derives the level shifts (3) and (4). It then refits the 1976 and 1980 open-tube data with the closed-tube tension of 1982. The fits give eσ^{3/2} = 0.00190 at both couplings, and the 1980 first-gap excess matches +240e/R⁴ (χ² = 3.5 for five separations) against −24d/R² (χ² = 65). Section 4 derives the tree-level phase e^{is/4σ} and recovers the closed and open square roots from a lengthening rule. Section 5 evaluates Polyakov's anomaly on the induced metric. It obtains the vertex (26−d)[∂(∂X·∂X)]²/384π and its amplitude, and predicts a splitting of ∓909/σ²L⁵ in the closed-tube level N = N̄ = 1 in d = 4. Section 6 combines the 1982 Casimir counts into c = 0.99(3) and bounds an extra scalar at m > 1.8√σ.

## Assessment of the main claims

- First-derivative terms are the area, with c₂ = −σ/8 and c₃ = σ/4: **supported**. The flat-sheet argument is sound up to total derivatives.
- A stiffness term changes no level at the order where it enters, for closed and open strings: **supported**. At a Dirichlet end the current in the identity vanishes, so no boundary term survives. Its use for "none" at L⁻⁵ in Table 1: **partly supported** (Major 4).
- No other six-derivative invariant exists, and the first free coefficient enters at σ⁻³L⁻⁷: **unsupported** as a derivation; the paper asserts it (Major 4).
- A rotation-invariant source forbids b₁, and the factors −24k and +240k³ carry the stated signs: **supported**.
- eσ^{3/2} = 0.00190(11) and 0.00190(13): **partly supported**. The numbers reproduce, but baselines that fit equally well give 0.0019 to 0.0104, and R⁻², R⁻³ and R⁻⁴ fit equally (Major 2).
- The first-gap excess is the +240e/R⁴ term and excludes −24d/R², so "the endpoint term of 1976 is the R⁻⁴ term": **unsupported** (Major 1).
- Amplitude (6), flux factor 2s, phase 2δ = s/4σ, and equation (8) with its elimination: **supported**.
- One rule gives both square roots, "zero-point terms included": **partly supported**. The algebra holds, but the rules for the zero-point motion and for the ends are postulated (Major 5).
- The curvature formula, the reduction to (10) with coefficient (26−d)/384π, amplitude (11), the eigenvalues, shift (12) and 909/σ²L⁵: **supported as consequences of g = h**. The assumption g = h itself is **unsupported** in the paper (Major 3).
- The vertex is trivial for one transverse direction: **supported**. "The square root is then exact through order L⁻⁵ in three dimensions": **unsupported** (Major 4).
- c = 0.99(3): **supported** statistically, but without the systematic errors of [4]. m > 1.8√σ: **partly supported**. The claim that the tube "stays at one value" of an extra coordinate: **unsupported** (Major 6).

## Major issues

1. **The excited level favours R⁻⁴ only because the two levels are measured against different baselines.** Table 3 measures the excess against the full square root. The value e = 0.195, however, comes from fitting the ground state with σR + μ − π/24R, which drops the R⁻³ and higher terms that the gap baseline keeps. With one baseline for both levels, the reading fails.
   - (a) Square root for both levels. The ground state fits as well (7.3/12 against 6.9/12, `refit84.txt`), with e = 1.064(10), or 1.019(68) from R = 4.
     - 240e/R⁴ is then 0.41 at R = 5 and 0.20 at R = 6, comparable to the gaps themselves (0.37 and 0.34).
     - These predictions lie above even the T = 4→5 upper bounds, by 0.32 and 0.12. That is at least 10 and 5 standard errors once the error of e is included.
     - At R ≥ 7, where first order could hold, the gaps (errors 0.034–0.064) exclude none of the readings at 95%.
     - The value fitted to the gaps alone, 0.252(47), lies 17 standard errors from 1.064(10).
   - (b) Free string for both levels. The gap baseline is then π/R, and the gaps fall 0.17(2) below it at R = 5 whichever end term is added.
   - (c) The two-state estimates restate the T = 4→5 effective energies. They lie within 0.02 of those bounds, and above them at R = 3–5 (0.460 against 0.457 at R = 5).
     - The programme has later-time values: production 2 at T = 8→12 (`summary80.json`, `mp_8-12` minus the production-1 E₀). These give gaps of 0.29(12) and 0.24(11) at R = 5 and 6.
     - Those gaps lie below the square root by 0.08 and 0.10, and 0.17(12) below the bound at R = 5. That is the 0.13 drop Section 3.3 says the R⁻² reading would need.
     - Over R = 4–8, their diagonal χ² is 6.6 for +240e/R⁴, 1.3 for −24d/R² and 2.4 for no end term.
   - (d) With e = 0.195, the prediction exceeds the R = 4 upper bound by 4 standard errors. The test drops R = 4 as beyond first order, while the fit that fixes e keeps R = 3.
   - (e) The ground-state e (1976 data and production 1) and the gap e (production 3) are statistically independent apart from the shared σ. They are parameters of two different models, so their agreement tests nothing.

   *Change:*
   - Use one baseline for both levels (the square root, with first-order end shifts on top) and report where first order fails.
   - Treat the production-3 gaps as upper bounds, and add the T = 8→12 values.
   - Fit d and e jointly to both levels.
   - Use the jackknife covariance of the gaps across R, and propagate the errors of e and σ.
   - Remove "The endpoint term of 1976 is the R⁻⁴ term" from the abstract and Section 8, and state the endpoint question as open.

2. **The ground state leaves the form of the correction open, and the scaling test is a single comparison.**
   - From R√σ = 0.64 on, R⁻² (9.9/12), R⁻³ (6.9/12) and R⁻⁴ (6.9/12) fit equally well. With d and e both free, d = 0.009(20) and e = 0.155(87).
   - The abstract quotes eσ^{3/2} to 6%. Baselines that fit equally well give 0.0019, 0.0061 and 0.0104, which correspond to b₂√σ between −0.004 and −0.020.
   - The scaling paragraph reports R⁻² (2.8σ apart between couplings) and R⁻⁴ (0.0σ). It omits a free R⁻³ term, which passes (1.3σ) and is stable under a change of range (−0.5σ).
   - The 2.8σ discrepancy in d is about the size of d's own range instability: d moves by 1.8σ when R = 3 is dropped.
   - Section 3.1 itself allows a lattice b₁, which need not scale. The non-scaling of d therefore bears on its origin and leaves its presence open.
   - Table 2 omits the β = 0.73 fits from R = 2 (R√σ = 0.43). There R⁻⁴ fails (74.9/14), R⁻² fits (16.6/14, p = 0.28), and a fit with both terms gives d = 0.0373(46) and e = 0.026(10).

   *Change:*
   - Tabulate R⁻², R⁻³, R⁻⁴ and both together, on each baseline and over all ranges including R = 2.
   - Quote e with its model spread in the abstract and in (5).
   - Describe the two-coupling test as one comparison, and drop the inference drawn from the non-scaling of d.

3. **Section 5 takes its central input from memory, and Appendix B leaves it unchecked.**
   - "We take (9) with g = h as the quantum correction to (1)" is the Polchinski–Strominger construction listed in Appendix E. Rule (1) forbids it as an input.
   - Appendix B fixes β by demanding c = 0, so it cannot test g = h. It also states T₋₋ without deriving it. Part H of the code types T in and checks only ⟨∂Y∂³Y⟩ and one product.
   - The whole check rests on the coefficient of the improvement term, and my derivation disagrees with the appendix:
     - Start from the appendix's own action, with δX = ε∂₋X, so that δφ = ε∂₋φ + ∂₋ε + …. Then δS = (β/4π)∫∂₊ε[(∂₋φ)² − 2∂₋²φ] + (X part).
     - Use the normalization δS = −(1/2π)∫∂₊εT₋₋, which returns the stated T₁ and T₂. This gives T₋₋ ⊃ −(β/2)(∂₋φ)² + β∂₋²φ.
     - Hence T₃ = −(2β/R)e₊·∂₋³Y, twice the stated term, with a cross term 12β/(z−w)⁴, i.e. central charge 24β.
     - The same procedure reproduces T = −(∂φ)² + Q∂²φ and c = 1 + 6Q² for an independent Liouville field.
   - With 24β, cancellation needs β = (26−d)/24, which is half of (9) and would halve (10)–(12).
   - A term γ∂₋²φ is conserved at this order, so fixing its coefficient needs an argument beyond conservation.
   - As the paper stands, the factor in (10)–(12) rests on the remembered coefficient of Aharony and Komargodski.

   *Change:*
   - Derive T₋₋ from the action, including the terms of the covariant functional that vanish only on the constraint surface, and resolve the factor 2.
   - Alternatively, declare the coefficient of (9) on h an imported result and label (10)–(12) as conditional on it.
   - Replace "the total is zero in every dimension" with what is actually derived.

4. **The order counting in Sections 2 and 5 is asserted, or rests on memory.**
   - (a) "We find no other with six derivatives" and the σ⁻³L⁻⁷ placement have no classification behind them, in the paper or the code. Also, the Euler density and K², which the text calls "next", are four-derivative two-field invariants of the same order as the stiffness.
   - (b) Table 1's "none" at L⁻⁵ needs more than the quadratic identity.
     - The redefinition X → X + (α/σ)∂²X, which removes α(∂²X)², generates six-derivative quartic terms of order α/σ²L⁵ from the area terms.
     - Gauss's equation for a surface in flat space settles all orders: K^i_{ab}K^{i ab} = K^iK^i − R, where K^i is proportional to the equation of motion and √hR is topological.
     - The paper names both pieces but never states the identity.
   - (c) "Exact through order L⁻⁵ in three dimensions" needs three contributions at L⁻⁵ from the area action: second-order quartic, first-order sextic, and one-loop. The one-loop term is where the anomaly lives. None of these is computed, and the phase route assumes that the phase stays linear, which is the point at issue.
   - (d) The Section 5.4 statement about one-phonon states of the open string in d = 4 is not computed.
     - On the interval φ_L(v) = −φ_R(−v), so the self-contractions of (10), which vanish on the circle, survive near the ends.
     - The (d−2)(d−3) part of the ground-state and one-phonon expectation values is therefore open.
     - For d = 3 the vertex reduces at a Dirichlet end to a total time derivative, so that case stands.

   *Change:*
   - Enumerate the ∂⁶X⁴ terms modulo total derivatives and equations of motion, and show which ones Lorentz invariance fixes in d = 3 and in d ≥ 4.
   - Give the Gauss-equation argument for the stiffness.
   - Compute or withdraw the d = 3 statement at L⁻⁵.
   - Compute ⟨(10)⟩ in the open-string ground and one-phonon states in d = 4, or restrict Section 5.4 to d = 3.

5. **The route from the phase to the square roots needs two rules that (7) does not contain.**
   - Equation (8) quantizes asymptotic phonons, and its algebra holds (part E).
   - The zero-point motion is a finite-size effect that lies outside such an equation. Applying (8) to it is a choice that happens to return (2) of [4]. Deriving it would require the thermodynamic Bethe ansatz with this S-matrix, which Appendix E remembers and the paper never carries out.
   - For the open string, a single phonon has no other phonon to cross, so (7) gives it no phase. The term p²/2σ that turns σR + π/R into the square root comes instead from "half of each standing wave moves each way". That amounts to postulating a reflection phase e^{ip²/2σ} at each end.
   - The sentence "The square root of the dual model in 26 dimensions, which is exact, says that both hold there to all orders" runs backwards. A spectrum fixes an S-matrix only through the same analysis, which is not performed.

   *Change:* State the zero-point and end rules as postulates, or derive them. Rephrase point (iii) of the abstract and Section 4.2 accordingly, and remove or attribute the 26-dimensional inference.

6. **Section 6: the mass bound lacks its systematic errors, and the inference about Polyakov's conformal factor outruns the data.**
   - (a) The 1982 variants (window shift, continuum dispersion) move c by up to 0.05, which is more than the quoted error of (13).
   - (b) The bound comes from the shortest tubes, L = 7 and 8 at β = 0.73 (L√σ = 1.50 and 1.71). There [4] reports lattice offsets near 0.5/N_t² and a rise above the square root at shorter lengths. The bound is set by how far the data allow the energy to fall, so an unmodelled upward offset at these lengths makes it artificially tight.
   - (c) Δχ² = 3.84 is the two-sided 95% value. For a one-sided limit with m → ∞ as the null hypothesis, state the confidence level and the method (Δχ² = 2.71 for 95%).
   - (d) The data exclude a light independent mode. They are equally consistent with no such field or with a massive one, so "the conformal factor follows the induced metric" goes beyond them. Reading the conformal factor as a coordinate at which the tube sits belongs to later work (see Era discipline).

   *Change:*
   - Propagate the 1982 systematic errors into (13) and (14).
   - Give the bound from L ≥ 10 and under each 1982 variant.
   - State the statistic and confidence level.
   - Restrict the conclusion to "no additional mode below the bound", and remove the geometric reading from the abstract and Section 6.

## Minor issues

1. Section 4.2: eight-derivative terms enter the phase at relative order (s/σ)², where the text has (s/σ)³. The tree phase is s/4σ, and the ∂⁸X⁴ phase is of order s³/σ³. The sentence also holds for transmission only, because (11) changes the other channels at relative order s/σ for d ≥ 4.
2. p denotes the right-mover in Section 4.1 and the left-mover in Section 4.2. The quoted 2.2 rad uses P and Q including the zero-point momentum; the phonon momenta 2π/ℓ give 2.4 rad. Reference [4] measured only the closed-tube ground state, so it cannot support anything about excited closed levels.
3. Equation (9): the two forms agree when Δ is the positive Laplacian −∇²; state the convention. For d = 3, "vanishes identically" should read "is a total derivative on shell, and a total time derivative at fixed ends".
4. Appendix C should state that δE = −⟨δL⟩ holds at first order for the velocity-dependent b₂ term (H_int = −L_int with q̇ → p). Section 3.1 would gain from one line in static gauge: under a rotation θ about the end, δ(∂ₓX)² = 2θ·∂ₓX + O(X³), and no invariant completion exists.
5. Table 3 adds the errors of E₁ and E₀ in quadrature, although both come from production 3; use the jackknife instead.
6. Code:
   - Part E skips cases with a negative discriminant, so fewer than 200 cases are compared; print the count.
   - Part G's docstring promises a Richardson step that the function omits.
   - Part F evaluates (12) as a formula, and part H types T in; describe both as evaluations rather than checks.
   - The "Sources" paragraph should drop "every derivation is given and checked symbolically".
7. Table 4 applies a first-order shift with bare momenta at L√σ = 6, where the tree phase is already 1.1 rad. By my estimate, adding the phase of (11) to (8) with dressed momenta lowers the shift by about a factor 2 at L√σ = 6 and by about a quarter at L√σ = 10. Quote dressed values, or raise the stated range of validity.
8. Section 1's "exactly one massless mode [4]" overstates c = 0.97(4) and 1.04(6). In Section 6, a periodic Majorana fermion would give c = 0, which is also excluded; say which boundary condition the thermal circle imposes.
9. Equation (5) gives b₂√σ for the free-string baseline only; give the range over all baselines.
10. Section 2.1: "a flat sheet has no other invariant" needs "up to total derivatives". In d = 4, for example, ε^{ab}ε_{ij}∂ₐXⁱ∂_bX^j is nonzero on flat sheets.
11. Section 7: name the energy scale behind "some 30 MeV above it", as the 1980 report asked for the same level.

## Checks I ran

- **Reruns.** I saved the stored outputs, then reran `effective_string.py` and `refit84.py` in the 1984 folder. `effective_string.txt`, `refit84.txt` and `summary84.json` came out identical, and the figure checksums did not change. Every number I traced in the abstract, Tables 2–4 and equations (5) and (12)–(14) matches the stored output.
- **Section 2, by hand.**
  - The expansion √det(1+M) = 1 + ½trM + ⅛(trM)² − ¼trM² gives c₂ and c₃ on every flat sheet.
  - The stiffness identity holds. Its current at a Dirichlet end is J^x = −∂ₜX∂ₜ∂ₓX + ∂ₓX∂ₜ²X = 0.
  - The first-order stiffness shift of each open mode is proportional to ∫₀^R(2sin² − 2cos²)dx = 0.
- **Mode sums (Section 3).**
  - ⟨(∂ₓX)²⟩ = (π/σR²)Σn and ⟨(∂ₜ∂ₓX)²⟩ = (π³/σR⁴)Σn³. A phonon adds 2kπ/σR² and 2k³π³/σR⁴ per end.
  - With δE = −⟨δL⟩ this gives (3) and (4) with their signs.
  - The b₁ shift acts as a lengthening by 24d₁/π for every level.
- **Section 4.**
  - (6) follows from the leg assignments.
  - S = 1 + iM/2s follows from δ²(P) = ½δ(p′−p)δ(q′−q) with relativistic normalization.
  - The identity behind (8) holds, with P − Q = 2π(N − N̄)/L, and P = 1.477√σ at L√σ = 2.6.
- **Section 5 vertex and amplitude.**
  - The linearized curvature of δh_ab = ∂ₐX·∂_bX is additive over transverse fields, so part C's one-field check suffices. On shell, R = −½∂²A.
  - (10) follows from either form of (9), with φ = ½A.
  - (11) follows from L = −κ∂ₐA∂ᵃA, with eigenvalues d − 3, +1 and −1.
- **(12) by a second route.**
  - On the circle, A = 4φ_R′·φ_L′ holds as an operator identity. Hence κ∫∂ₐA∂ᵃA = 32κ∫(XY + YX), with X = φ_R″·φ_L′ and Y = φ_R′·φ_L″.
  - The connected matrix elements on the N = N̄ = 1 states are −32κk⁴L⁻¹[δ_ijδ_kl − δ_ilδ_jk] at k = 2π/L. That is (12), sign included.
  - Self-contractions vanish, because the R and L oscillators are independent and the symmetrized ⟨φ_R″φ_R′⟩ = ½∂⟨φ_R′²⟩ = 0. The vacuum and one-phonon states are therefore unshifted.
  - For one field the on-shell vertex is ¼∂₊[(∂₊X)²∂₋(∂₋X)²], whose boundary term at a Dirichlet end is (1/32)∂ₜ(∂ₓX)⁴.
- **Appendix B.** ⟨∂Y∂³Y⟩ = −6a²/(z−w)⁴, and c = d from T₂, both check. The Noether computation in Major 3 disagrees with the stated T₃.
- **From stored numbers.**
  - 240e/R⁴ for each ground-state model, compared against the two-state gaps and the T = 4→5 bounds.
  - The production-2 gaps at T = 8→12.
  - The excess over π/R.
  - The dressed-momentum estimate in Minor 7.
- **Not run, and requested of the authors instead:**
  - correlated refits of the raw 1976 and 1980 files for every form and baseline;
  - joint (d, e) fits to both levels;
  - the covariance of the gaps across R;
  - the open-string expectation values of (10) in d = 4;
  - the mass bound under each 1982 variant.

## Era discipline

Appendix E declares the imports (Polchinski–Strominger, Aharony–Komargodski, Meyer, Aharony–Karzbrun, Lüscher–Weisz, Aharony–Field, Dubovsky–Flauger–Gorbenko, Caselle et al., Blöte–Cardy–Nightingale and Affleck) and the remembered outcomes. No remembered number enters a fit. Four lapses remain.

- (a) **Declared imports used as inputs.** Section 5 uses g = h with Polyakov's coefficient, and Section 4.2 uses the zero-point and end rules. Rule (1) admits these as motivation only.
- (b) **Remembered results presented as derived.** "No other six-derivative invariant" and the free coefficient at L⁻⁷ are declared only as "the classification of Section 2". The d = 3 exactness through L⁻⁵ is undeclared.
- (c) **Undeclared and misattributed.** The abstract and Section 6 read the conformal factor as an extra target-space coordinate at which the tube sits. That reading comes from the later literature on non-critical strings and from Polyakov's 1997–98 proposal for the confining string. Reference [7] introduces the Liouville field; the geometric reading came later.
- (d) **Leaning on remembered outcomes.** "The endpoint term of 1976 is the R⁻⁴ term" lands on the remembered outcome (b₁ = 0 and b₂ < 0, from the lattice work of 2010–2017). Analysed with one baseline, the data stay neutral, so under our standard the sentence carries no weight. The direction of the d = 4 splitting and the bound near the remembered 1.85√σ coincide with declared outcomes; they also carry no weight.

The references I could check against the folders predate November 1984 ([15] as a preprint in press, [9] published in 1984). The masses in Section 7 are declared.

## Recommendation

**Major revision.** The calculations of Sections 2, 3.1, 4.1 and 5.2–5.3 hold where I tested them, (12) included by an independent route, and both scripts reproduce every number. The headline data claim fails once one baseline is used for both levels. Under a single truncation, the excited level either contradicts the R⁻⁴ reading or cannot test it, and the ground state does not separate R⁻², R⁻³ and R⁻⁴. The abstract must therefore return the endpoint question to open. Section 5's input is a remembered construction, and the paper's own check of it carries an unresolved factor of 2 in its normalization. The six-derivative classification, the L⁻⁷ and d = 3 statements, and the zero-point and end rules must be derived or labelled as imported. Section 6 needs its systematic errors, and its geometric reading should be removed.
