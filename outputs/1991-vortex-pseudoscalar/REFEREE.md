# Independent second-line referee report — QCDS-91/S1

Referee model: gpt-6.1-sol (high reasoning effort). The report below was returned by the independent referee on the submitted draft.

**Recommendation: accept with minor textual revisions.**

I reviewed `paper.md`, the stored `results/radial.json`, `code/vortex.py` as text, and the 1990 amplitude note. This report concerns the submitted version identified by SHA-256 `9c502a7db3d4f4b47a61a58ef814c6764d449de22783bb23001143ae9d1dbca6`. I performed no numerical or symbolic execution, builds, simulations, or file edits. The assessment below is an independent textual physics review, not computational validation of the stored results.

The manuscript establishes a concrete microscopic mechanism: a localized longitudinal electric polarization of a magnetic vortex has a nonzero matrix element to two translations. Its principal conclusions follow from the displayed equations. The distinction between magnetic-vortex results and an eventual colour-electric confinement calculation is maintained.

**Errors**

I found no substantive error in the central derivations.

One minor technical wording error occurs in §2.2: replacing $\tau$ by one away from critical coupling would distort the dependence on $\beta$, but would not introduce a new dependence on the microscopic charge $e$. Equations (22) and (25) show that the charge powers and cancellation remain the same. Replace that sentence accordingly.

**Assessment of the principal calculations**

1. **Parity and flux sector.** The transverse operation preserving the positive magnetic-flux sector is correctly identified as $CP_\perp$. A bare transverse reflection changes the sector. The electric field $F_{0z}$ is odd under both $CP_\perp$ and longitudinal reflection, while translations transform as ordinary transverse displacements. Consequently the antisymmetric ordered right-left state has the required quantum numbers. The distinction from simultaneous inversion is useful and correct.

2. **Localized electric mode.** Equations (8)–(11) identify a closed physical linear sector, including the sheet constraint. The logarithmic trial function establishes binding below the vector threshold for the stated nodeless vortex. Positivity of the quadratic form excludes a zero eigenvalue. The manuscript correctly avoids interpreting this as binding below every bulk mass or as exact interacting stability.

3. **Cubic vertex in the two representations.** The pullback configuration includes the necessary sheet component of the translated connection. Its linear translation perturbation is gauge equivalent to the complete translation zero mode. The argument that different quadratic continuations give the same on-shell three-point amplitude is applicable here. In this representation the Maxwell cross term gives (15).

   In linear background-gauge variables the scalar-current vertex (16) is consistent with the current convention. The identity
   $$
   HB=4eK
   $$
   and self-adjoint projection yield (17). Integrating (15) by parts using the external Proca equation reproduces (16), including the factor $1/2$. Their agreement is on shell; the manuscript correctly does not equate arbitrary off-shell exchange numerators.

4. **Matching and residue normalization.** The normalization of the Proca oscillator and the factor of $m_*$ relating its field strength to a canonical pseudoscalar give
   $$
   |Q_{\rm pole}|=|\mathcal I|/m_*.
   $$
   The two assignments of the phonon legs produce the stated ordered amplitude. Projection onto the normalized antisymmetric tensor supplies the further factor of two in $R_A=2g_*^2$. This agrees with the 1990 convention. The distinction between a physical pole match and a complete off-shell effective-action match is essential and is stated clearly.

5. **Critical even partner.** The construction is stronger than a numerical degeneracy claim. With the stated radial measure, $D^\dagger(0,u)=(fu,-u')$, and the critical background equations make $DD^\dagger(0,u)=(0,\mu^2u)$. Regularity, fixed flux, nonzero norm, and the canonical normalization in (27) follow.

   The residue calculation also withstands scrutiny. The translation norm is equal to the tension at the stationary solution, but their derivatives along a massive nonstationary deformation need not coincide. Differentiating the norm gives $N'(0)=m_*\mathcal I$, and hence the trace-channel strength equals $R_A$. This establishes two distinct classical particles with equal masses and projected strengths, rather than one particle appearing in two incompatible reflection sectors.

6. **Width and finite length.** The two-body phase space counts both momentum directions for the distinct species without an additional factorial. Equation (30) follows. The normalized antisymmetric finite-volume state supplies the stated $\sqrt2$ enhancement, giving (31). Its large-volume density-of-states limit reproduces the width, which is a useful independent normalization check within the argument.

   The restrictions on interpreting a matrix element as an isolated avoided-crossing gap are appropriate, especially for higher partitions and additional nearby states.

**Improvements**

- Qualify “exactly degenerate” in the abstract as “exactly degenerate in the classical fluctuation problem.” The later discussion already explains that the bosonic theory need not preserve this degeneracy radiatively.
- Keep the numerical values explicitly described as stored classical results supported by the reported convergence comparisons. The difference and collocation calculations share the same background; the manuscript correctly acknowledges this limitation, and it should remain explicit in any checks summary.
- Preserve the designation **partial width** wherever (30) is quoted. Localization, a two-translation decay rate, and a total interacting lifetime are separate statements.

**New idea**

The existing calculation implies an additional accessible prediction: at critical coupling the even partner has the same leading total width into the two translation species as the odd mode. For the even particle, the identical-particle factors in the $11$ and $22$ final states together reproduce the odd particle’s distinct-species counting. This would complement the equal masses and projected residues, subject to the same classical and leading-decay qualifications. I have not computed additional decay channels or radiative corrections.

**Signed:** Independent second-line referee, Codex (GPT-6.1 Sol) — `vortex_referee`
18 November 2026
