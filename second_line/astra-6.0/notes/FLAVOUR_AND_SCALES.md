# Calculations connecting flavour and scales

These are explicit effective-theory and algebraic controls for the research programme. No string vacuum, observed generation count or numerical top mass is derived. Reference keys resolve in [REFERENCES.md](../REFERENCES.md).

## 1. One large singular value

Let Y₀=y₀ ab†, with a†a=b†b=1. Its singular values are |y₀|,0,…,0. For Y=Y₀+δY and ||δY||₂≤ε|y₀|, the singular-value perturbation inequality gives

\[
|s_1(Y)-|y_0||\leq\epsilon|y_0|,\qquad
s_j(Y)\leq\epsilon|y_0|\quad(j\geq2).
\]

This is a sufficient mechanism for one unsuppressed fermion mass. It neither fixes y₀ nor explains the separate small singular values. It works for any matrix size and therefore cannot by itself predict a number of families.

Canonical normalization multiplies Y by invertible matrices associated with the kinetic terms, and by the Higgs normalization. It preserves exact rank, but can change the nonzero singular value substantially. Small holomorphic entries are not physical mass predictions until these factors are computed. A hierarchy bound on the physical perturbation requires control of their condition numbers.

The string benchmark is a cubic coupling localized at one transverse intersection. It motivates rank one [M13, M14]; it does not supply our missing global model. A specific correction matters here: ordinary worldvolume gauge flux does not generically lift the holomorphic rank in the local commutative setup analyzed in [M14]. A proposed rank-lifting term must actually change the relevant superpotential structure, for example through an appropriate nonperturbative or three-form-induced effect. The finite perturbation δY in this calculation is an assumed effective term, not a computed string correction.

## 2. Gauge–Yukawa flow and a conditional lower bound

Take an SU(3) color theory with N_g Standard-Model-like quark families, hence N_f=2N_g Dirac fundamentals. There is one Higgs doublet and one nonzero quark Yukawa y. Work above all quark thresholds, set electroweak couplings and other Yukawas to zero, and include no other colored matter. The one-loop equations are

\[
16\pi^2\frac{dg}{d\ln\mu}=-b g^3,\qquad
b=11-\frac43N_g,
\]
\[
16\pi^2\frac{dy}{d\ln\mu}
=y\left(\frac92y^2-8g^2\right).
\]

Define r=y²/g² and a=9/2. Differentiating both numerator and denominator gives

\[
\frac{dr}{d\ln\mu}
=\frac{g^2}{8\pi^2}r\,[ar-(8-b)].
\]

The nonzero constant-ratio trajectory is

\[
r_* = \frac{8-b}{a}=\frac{2(4N_g-9)}{27}.
\]

Color asymptotic freedom requires b>0, or N_g<33/4. A positive nonzero ratio requires N_g>9/4. For integer N_g the intersection is

\[
\boxed{3\leq N_g\leq8.}
\]

Three is the first allowed number under these hypotheses. There is no principle here selecting the smallest allowed integer. The condition is not a general consistency requirement: a gauge theory need not sit on this trajectory, electroweak terms and additional states alter the flow, and high-flavour theories need a separate confinement analysis. No new theorem about string vacua is asserted. This is a generation-dependent application of the familiar fixed-ratio mechanism [M16], using the color beta function known in 1973 [H7, H8].

For N_g=3, r*=2/9. Setting β_y=0 instead would give r=16/9. That is a nullcline at a given g, not a constant-ratio solution when g itself runs. Confusing the two would substantially change a proposed top-mass estimate.

Write c=8−b>0. The integrated solution is

\[
r(g^2)=\frac{r_*}{1-(1-r_*/r_0)(g^2/g_0^2)^{-c/b}}.
\]

As the energy decreases, g² grows and nearby positive trajectories approach r*. This mathematical attraction must be tested over a finite perturbative interval; taking g² to infinity is outside the calculation. At three families c/b=1/7, so convergence can be weak. The supplied code integrates the coupled equations independently and compares them with this solution. It does not turn the formal asymptote into a physical mass prediction.

An unsuppressed top Yukawa would still require the string theory to select the one active flavour direction and to explain the weak vacuum. Small Yukawas remain small under the multiplicative flow in this truncation; their origin is a different calculation.

## 3. Bounding a chiral index uniformly

Suppose an allowed flux sector has real coordinates n, positive-definite quadratic form Q and a fixed budget

\[
n^TQn\leq2L,\qquad I=\ell^Tn.
\]

Cauchy–Schwarz, applied to Q^(−1/2)ℓ and Q^(1/2)n, gives

\[
|I|^2\leq(\ell^TQ^{-1}\ell)(n^TQn)
\leq2L\ell^TQ^{-1}\ell.
\]

For integer n this is an upper bound, not necessarily an attained value. In our toy Q=diag(2,8), L=12 and ℓ=(1,2). The continuous bound is √24; exhaustive integer enumeration gives |I|max=4. The choice of 12 is synthetic and has no string-geometric origin.

This diagnostic can fail uniformly in a limit even if every finite member has a bound. Choose Q(η)=diag(η²,1), L=1 and I=n₁. Then |I|max=floor(√2/η), which diverges as η→0. This is an algebraic example, not a demonstrated gravitational decoupling limit.

For an actual candidate, derive Q, L, ℓ, the quantization lattice and its allowed supersymmetric or stable subspace. Check whether 2LℓᵀQ⁻¹ℓ stays bounded along the path removing gravity. A positive form at one point in moduli space is insufficient. Indefinite charge forms, flux directions of zero cost, changing topology and extra branes require their own analysis. Published compactification bounds [M15] motivate this test but do not settle it for our limit.

Even a bounded net index does not bound the number of vectorlike light pairs. The full cohomology or zero-mode problem, charges, anomaly cancellation and mass matrix must be computed. A complete generation requires compatible multiplicities for Q, uᶜ, dᶜ, L and eᶜ, with any neutrino sector stated explicitly.

## 4. QCD, the weak scale and threshold matching

Use the convention

\[
\frac{d\alpha_s}{d\ln\mu}=-\frac{b_{N_f}}{2\pi}\alpha_s^2,
\qquad b_{N_f}=11-\frac23N_f.
\]

On an interval with fixed N_f,

\[
\alpha_s^{-1}(\mu)=\frac{b_{N_f}}{2\pi}\ln\frac{\mu}{\Lambda_{N_f}},
\quad
\Lambda_{N_f}=M\exp\left[-\frac{2\pi}{b_{N_f}\alpha_s(M)}\right].
\]

At one loop this defines the integration constant; beyond one loop specify the scheme and matching order. It is not yet a calculation of a hadron mass or string tension.

For six flavours and the *chosen* α_s(M)=0.12, M/Λ₆ is about 1.77×10³. A hierarchy of this order can thus arise without a Planck-scale reference. But the logarithmic sensitivity is

\[
\frac{\partial\ln(\Lambda_6/M)}{\partial\ln\alpha_s(M)}
=\frac{2\pi}{7\alpha_s(M)}\simeq7.48.
\]

Allowing the coupling to float fits the hierarchy. A useful string result must constrain it and M/v. This illustration uses fixed six-flavour running and must not be quoted as a threshold-corrected physical v/Λ₃ prediction.

Across one heavy-quark threshold m_h, continuity of the leading-order coupling gives

\[
b_{n-1}\ln\frac{m_h}{\Lambda_{n-1}}
=b_n\ln\frac{m_h}{\Lambda_n},
\]
\[
\Lambda_{n-1}^{b_{n-1}}
=m_h^{b_{n-1}-b_n}\Lambda_n^{b_n}.
\]

Successive t,b,c decoupling therefore gives

\[
\boxed{\Lambda_3^9=(m_tm_bm_c)^{2/3}\Lambda_6^7},\qquad
\boxed{\Lambda_3=\Lambda_6^{7/9}(m_tm_bm_c)^{2/27}}.
\]

This formula is dimensionally consistent: 7/9+3×2/27=1. Hold the reference scale M above the thresholds and α_s(M) fixed, so Λ₆ stays fixed. Then

\[
\frac{\partial\ln\Lambda_3}{\partial\ln m_t}=\frac{2}{27}.
\]

A tenfold top mass changes Λ₃ by only 10^(2/27)≈1.186. If m_t,m_b,m_c all scale with v at fixed Yukawas, then

\[
\frac{\partial\ln\Lambda_3}{\partial\ln v}=\frac29,
\qquad
\frac{\partial\ln(\Lambda_3/v)}{\partial\ln v}=-\frac79.
\]

Thus the threshold connection does not lock the two scales. It assumes three heavier quarks and three retained light quarks solely as a conditional example; it does not derive that spectrum. If a threshold crosses the confinement region, perturbative matching fails. Holding a low-energy measured coupling fixed instead would be a different variation. The corresponding top-threshold observation appears in Quigg's work [M19].

## 5. Why ordinary QCD breaking is too small

If N_D electroweak doublets condense with decay constants f_i, their contributions give v_eff²=Σ_i f_i² in the usual normalization. Setting all f_i=fπ gives v_eff=√N_D fπ. Rounded historical values v≈246 GeV and fπ≈0.093 GeV would require about seven million such doublets. The illustrative eight-family color-AF ceiling would instead give only about 0.263 GeV.

This does not compute fπ in many-flavour QCD, where the phase can change. It rules out the simple proposal to multiply ordinary QCD-sized contributions into the required weak scale within that matter content. A new strong sector or another source of symmetry breaking remains possible but introduces dynamics and scales that must be derived [M17, M18].

## What these calculations justify doing next

Choose one candidate with a computable leading Yukawa and discrete chiral spectrum. Evaluate its kinetic terms, flux budget and gauge coupling along the nongravitational limit. Then calculate its symmetry-breaking vacuum and thresholds. The point is to see whether the same restricted data determine family number, Yukawa hierarchy and scale ratio. The arithmetic above identifies several false shortcuts and a conditional link worth pursuing; it does not establish that the required construction exists.

Run `python3 calculations/flavour_checks.py` from the project root. Numerical output is in [FLAVOUR_RESULTS.md](../calculations/FLAVOUR_RESULTS.md) and [flavour_results.json](../calculations/flavour_results.json).
