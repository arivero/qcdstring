# What the tensor and supersymmetry mean

Version 0.3 — 6 November 2026. These are explanatory requirements for the 1974 programme. A successful theory must account for the structures that string theory produces, as well as its desired quark phenomenology. The following distinguishes established mechanisms, our reproduced calculations and open construction work. Reference keys resolve in REFERENCES.md.

## 1. Why a closed string contains a rank-two object

In the standard flat-space closed superstring NS–NS sector, the first massless states have the form

\[
\epsilon_{\mu\nu}\,
\psi_{-1/2}^{\mu}\widetilde\psi_{-1/2}^{\nu}|0;k\rangle.
\]

Independent left and right vector oscillators yield a tensor product. After physical-state constraints, the symmetric traceless, antisymmetric and trace pieces are distinct fields. In ten dimensions their massless little-group representations give

\[
8_v\otimes8_v=35\oplus28\oplus1.
\]

The symmetric traceless part is the graviton in that conventional theory; the other two pieces are the two-form and dilaton. This explains its kinematic origin, not why it should describe measured gravity. A proposed alternative must account for the companion states and interactions too. The bosonic closed string has the analogous left/right tensor construction, but its tachyon precludes treating the flat vacuum as stable.

For a physical massless helicity-two particle in an ordinary Lorentz-invariant S-matrix, the leading soft Ward identity forces universal coupling under the assumptions in T01 [H3–H5]. Neither changing its name nor changing the Regge intercept by hand solves that problem. A massive composite, a decoupled state or a field in a different physical dictionary changes the premises and requires an explicit calculation.

## 2. The physical candidate: a tensor bound state

A confining color theory has a spin-two channel. A useful operator is the gluonic contribution to the stress tensor, schematically the symmetric traceless part of tr(F_{μα}F_ν{}^α), with matter contributions included when appropriate. At leading large N its transverse-traceless correlator can have a tower of massive poles. In spectral language, schematically after the necessary subtractions,

\[
\Pi_2(Q^2)\sim\int_0^\infty ds\,
\frac{\rho_2(s)}{Q^2+s},\qquad
\rho_2(s)\supset\sum_n |F_n|^2\delta(s-m_n^2).
\]

Here F_n denotes the operator-state matrix element in a fixed normalization. At finite N, widths and continua may replace some isolated poles. We must derive masses and residues, check positivity and identify their quantum numbers. Absence of a zero-mass pole in this one correlator is a useful diagnostic; the full physical amplitude and possible bulk leakage still require the T01/T02 audit.

In a holographic description, a boundary metric is an external source for T_{μν}; normalizable radial fluctuations of the bulk metric describe states. Bulk gravitational dynamics remains present. The four-dimensional interpretation can nevertheless contain only massive tensor bound states. Identifying a bulk metric perturbation with a four-dimensional massless graviton before solving the radial problem would confuse the two descriptions.

The original hard-wall example demonstrates this distinction but inserts an infrared boundary. We have now reproduced a smooth-background example.

## 3. A common mechanism for tensor masses and supersymmetry breaking

Use the confining D4 background of Witten, with conventions recorded in Sakai–Sugimoto [M23, M25]. No flavor D8-branes are added in our calculation. One spatial brane direction χ has circumference 2π/M_KK. Bosons are periodic and fermions antiperiodic. Their kinematic circle momenta are

\[
p_\chi^{\rm B}=nM_{\rm KK},\qquad
p_\chi^{\rm F}=(n+\tfrac12)M_{\rm KK}.
\]

This removes fermion zero modes and breaks the inherited spacetime supersymmetry. These frequencies do not determine the pole masses of strongly interacting particles. The circle closes smoothly in the bulk; the bounding spin structure is antiperiodic in the polar frame. This supplies a geometrical consistency reason for that spin structure once the cigar topology is chosen, but does not derive why the microscopic theory chooses this background.

Write the string-frame metric and dilaton as

\[
ds_s^2=\left(\frac{U}{R}\right)^{3/2}
\left(\eta_{\mu\nu}dx^\mu dx^\nu+f(U)d\chi^2\right)
+\left(\frac{R}{U}\right)^{3/2}
\left(\frac{dU^2}{f(U)}+U^2d\Omega_4^2\right),
\]
\[
f(U)=1-\frac{U_0^3}{U^3},\qquad
e^{\Phi}=g_s(U/R)^{3/4},\qquad U\geq U_0.
\]

Smoothness fixes M_KK=(3/2)√(U₀/R³). A transverse-traceless four-dimensional tensor mode H(U), constant on the compact directions, obeys

\[
-\frac{d}{dU}\left[U^4 f(U)\frac{dH}{dU}\right]
=m^2R^3U H.
\]

For this mode the radial coefficients follow from e^(−2Φ)√g_s g_s^{UU} proportional to U⁴f and e^(−2Φ)√g_s g_s^{μν} proportional to R³Uη^{μν}. Thus the normalizability weight is U. This is the tensor equation corresponding to the T₄ sector in [M24], expressed in a different radial coordinate.

At m=0,

\[
H=C_1+C_2\int^U\frac{dU'}{U'^4 f(U')}.
\]

The second branch is logarithmically singular at the smooth tip. The regular constant branch has divergent norm ∫^∞U|H|²dU. Therefore **there is no regular normalizable tensor zero mode**. This conclusion uses tip regularity and UV normalizability, without an adjustable infrared wall.

Set x=U/U₀ and κ=m²R³/U₀=(9/4)(m/M_KK)². The problem is

\[
-\big[(x^4-x)H'\big]'=\kappa xH,
\qquad H'(1)=-\kappa H(1)/3,
\qquad H(x)\sim x^{-3}\quad(x\to\infty).
\]

The numerical solution gives

\[
\kappa_1=5.5241599998,\qquad
\boxed{m_{2^{++},1}/M_{\rm KK}=1.5669021099.}
\]

This reproduces a known spectrum [M24]. Three endpoint cutoffs agree; the nodeless mode also satisfies the independent Rayleigh quotient

\[
\kappa_1=\frac{\int_1^\infty(x^4-x)|H'|^2dx}
{\int_1^\infty x|H|^2dx}.
\]

The same metric fixes the long-string tension at its tip:

\[
\sigma=\frac{1}{2\pi\alpha'}(U_0/R)^{3/2}
=\frac{2\lambda_4}{27\pi}M_{\rm KK}^2,
\quad \lambda_4=g_4^2N,\quad
g_4^2=2\pi g_s\sqrt{\alpha'}M_{\rm KK}.
\]

The limitation is substantial: the tensor mass is of order M_KK. The unwanted KK degrees of freedom are not parametrically heavier in the classical supergravity regime. Taking the weak-coupling limit needed for a clean four-dimensional Yang–Mills separation invalidates that approximation. The growing IIA dilaton also calls for the M-theory description in the far UV; the tensor benchmark has that uplift. Our result explains a mechanism in this model, not the observed QCD spectrum, a top mass or a family number.

## 4. Which supersymmetry is being explained?

| Structure | What transforms | Required physical test |
|---|---|---|
| Worldsheet supersymmetry | Two-dimensional fields X and ψ | Constraints, spin structures, anomalies, physical spectrum and sewing |
| Spacetime global supersymmetry | Physical bosonic and fermionic states | Conserved supercharges, their algebra and the vacuum's realization |
| Spacetime local supersymmetry | Fields with a position-dependent spinor gauge parameter | Gravitino/gravity sector and its fate in the decoupling limit |
| Approximate symmetry of a bound-state Hamiltonian | Selected composite levels | Quantitative spectral relations and controlled violations; no automatic four-dimensional super-Poincaré claim |

Ramond's fermionic construction and the worldsheet interpretation of supergauges precede 1974 [H9, H10]. Worldsheet fermion zero modes in the Ramond sector furnish a Clifford algebra, explaining how target-space spinors can enter a string spectrum. This gives a structural reason to investigate a supersymmetric worldsheet when describing fermionic matter. It is not a proof that every string representation of QCD needs such modes.

Worldsheet supersymmetry alone does not establish spacetime supersymmetry. The global projections and internal theory must allow physical spacetime supercharges [M20]. In a four-dimensional RNS construction, one diagnostic is a BRST-invariant, mutually local, dimension-one charge of the form

\[
Q_\alpha=\oint dz\; e^{-\phi_{\rm gh}/2}S_\alpha\Sigma.
\]

For the usual internal c=9 supersymmetric sector, the weights are 3/8 from the superghost factor, 1/4 from the four-dimensional spin field and 3/8 from the internal Ramond ground state. Their sum is one. The existence of these factors locally is insufficient: projections, monodromies and the full background must permit the charge. Compute its action and algebra instead of inferring spacetime supersymmetry from the word “superstring.”

The tachyon-free ten-dimensional SO(16)×SO(16) heterotic theory is a control showing that worldsheet structure need not yield spacetime supermultiplets [M21, M22]. It still contains gravity. Its nonzero one-loop vacuum energy and dilaton backreaction also mean that absence of tree-level tachyons is not a proof of a stable vacuum.

## 5. If spacetime supersymmetry is present

Global supersymmetry can act in a nongravitational theory on fixed Minkowski space; four-dimensional examples are already available in 1974 [H11]. Gauging that symmetry introduces the gravitino/gravitational structure. Removing dynamical gravity therefore does not automatically require removing all global supercharges.

For unbroken four-dimensional N=1 supersymmetry, a massive spin-two state belongs to a multiplet with spins

\[
(2,\tfrac32,\tfrac32,1).
\]

This follows by acting with the two massive supercharge creation operators on a spin-3/2 Clifford vacuum: the middle level is 3/2⊗1/2=2⊕1, and the first and last levels are spin 3/2. There are 5+3 bosonic and 4+4 fermionic polarizations. A tensor-glueball interpretation with exact supersymmetry must predict those companions or explain why the assumptions of this multiplet assignment fail.

If global supersymmetry is broken spontaneously, include its goldstino and Ward identities. If it is broken by compactification boundary conditions, state the parent theory and the surviving lower-dimensional algebra. Explicit soft breaking requires a UV origin and a computed scale. In all cases, recalculate the flavor and scale claims: holomorphic rank protection and flux bounds previously established in a supersymmetric regime cannot simply be carried over unchanged.

The D4 example provides a calculable fate for inherited supersymmetry. It does not derive supersymmetry as a unique microscopic necessity. That origin question remains part of T14.

## 6. A discriminator on the flux tube itself

If supersymmetry is claimed only for the physical worldsheet, it can still change observables. For a free open long string, two massless transverse scalars give E_Cas=−π/(12R). Add two real massless Majorana fields. Before any projection, NS boundary conditions give an additional −π/(24R), while R boundary conditions give +π/(12R). Thus

| Physical free modes | Ground-state Casimir term |
|---|---|
| Two scalars | −π/(12R) |
| Two scalars and two NS Majoranas | −π/(8R) |
| Two scalars and two R Majoranas | 0 |

These follow from E=(π/R)(h_min−c/24). Each scalar has c=1; each Majorana has c=1/2, with h_min=0 in NS and 1/16 in R. Projections can remove a sector ground state; endpoints, interactions and fermion masses require their own treatment. This is a physical transverse EFT calculation, not a covariant critical-string partition function with ghosts omitted by mistake.

A candidate must therefore predict its worldsheet fermions and boundary conditions, or a mechanism making those fermions massive. Pure Yang–Mills does not acquire protected fermionic Goldstone modes merely because one uses an RNS description as a computational analogy.

## Research outcome to demand

For the spin-two object: derive its microscopic origin, physical operator, mass, residues and companion spectrum, while preserving factorization. For supersymmetry: derive which charges exist, why their structure is useful or necessary in the chosen model, and how their realization produces the low-energy spectrum. The same deformation should be tested against confinement, family multiplicities, Yukawa hierarchy and the QCD–Fermi scale relation.

The script calculations/spin_susy_checks.py reproduces the D4 radial calculation. Its output is in calculations/SPIN_SUSY_RESULTS.md and spin_susy_results.json. The proposed complete construction remains open.
