# T05 — Explain the spin-two object

**Priority:** P1. **Type:** positive physical interpretation, hard-wall control and reproduced smooth-background benchmark.

Define the physical spacetime before inspecting a bulk metric. In a holographic interpretation, tensor fluctuations must be classified by their radial wavefunctions, boundary conditions and couplings to physical operators [M7].

The included example takes an AdS-like interval \(0<z\le z_0\). A transverse-traceless fluctuation obeys

\[
\psi''-\frac3z\psi'+m^2\psi=0,\qquad
\|\psi\|^2\propto\int_0^{z_0}z^{-3}|\psi|^2\,dz.
\]

At zero mass, \(\psi=a+bz^4\). Normalizability at the ultraviolet boundary removes \(a\); an infrared Neumann condition removes \(b\). The massive spectrum satisfies \(J_1(mz_0)=0\), so \(m_1z_0\simeq3.831706\).

This is a four-dimensional tensor gap in a model that still uses bulk gravity. The wall sets a scale and has not been derived from gauge dynamics.

**Smooth-background calculation completed:** the Witten D4 model has radial equation −∂_U(U^4 f ∂_U H)=m²R³U H. Its smooth tip and UV normalizability exclude a zero mode. Numerical shooting gives m_tensor/M_KK=1.5669021, cross-checked with endpoint convergence and a Rayleigh quotient. The same metric gives sigma=2 lambda4 M_KK²/(27 pi). This reproduces an established spectrum, not an observed mass fit.

Its antiperiodic spatial circle also breaks the inherited spacetime supersymmetry, providing a joint test with T14. Its unwanted KK modes remain at the same parametric scale as the tensor spectrum in the controlled classical regime. Deriving a clean four-dimensional separation remains unresolved.

**Next calculation:** compute normalized tensor-operator residues and follow the tensor, scalar, two-form and any fermionic companions through a deformation improving that scale separation. Derive the operator identification and its interactions; absence of a graviton is not the whole explanatory target.

**Deliverable:** normalizable eigenfunctions, spectral residues, boundary-condition sensitivity, and ratios such as \(m_1/\sqrt{\sigma}\) only when both quantities are genuinely derived.

**Reject or narrow the route if:** the gap depends on an arbitrary boundary parameter; if a normalizable coupled zero mode remains; or if unwanted light towers cannot be separated from the proposed hadrons.

An alternative Robin boundary condition in the included notes admits the zero mode \(z^4\). This is a useful control: the absence of a graviton is a property to derive, not a name to assign.

The smooth calculation is in notes/SPIN2_AND_SUPERSYMMETRY.md and calculations/SPIN_SUSY_RESULTS.md; sources M23–M25.
