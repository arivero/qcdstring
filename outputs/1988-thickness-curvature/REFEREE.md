# Independent referee record

Review performed 17 November 2026 by a fresh **gpt-6.1-sol** agent, acting
for the second line. The user explicitly authorized this read-only review.
The agent received a frozen copy of the article, code, stored results and
source record, the earlier paper texts and reports, and the unmodified
second-line package. It did not receive the author plan or author-check
notes. The historical Astra 6.0 package was read as supplied material;
Astra 6.0 itself was not consulted. The report below is preserved verbatim.

---

Independent referee report, QCDS-88/1

Submitted article: “Thickness and curvature of a confining string: massive modes and the limits of rigidity”

Submitted SHA256 supplied to referee: `8af0baca5ead8c90bfd6beca046192e7f911292da6d9171b61fe781556c74e41`

Historical cutoff: 30 November 1988

**Recommendation: accept after minor clarification.** I find no substantive mathematical error in the principal results. The paper makes a useful, carefully limited distinction between perturbative curvature operators, additional physical states, and the observables needed to distinguish them. It meets the second-line standards relevant to T03, T09 and T10: it identifies the fields and their domain, retains source and boundary information, and does not promote an effective construction into a microscopic theory.

**Errors and major points**

No major correction is required on the material reviewed.

The central quadratic calculation is sound. Equations (4)–(6) give the stated canonical fields, mass and displacement residues. Completing the Gaussian square gives the negative exchange term in (7); the signs in (8)–(9) follow. The additional zero of the fourth-derivative truncation is indeed outside the Taylor convergence disk. Equation (10) correctly restores the determinant of the integrated field, leaving the mass \(M\), rather than \(m\), in the full Gaussian finite-size answer.

The periodic and Dirichlet interaction energies in (11)–(14), including their factors of two and their massless limits, are consistent. Equation (15) follows from varying the kinetic mixing with fixed displacement. The distinction between subtracting bulk energy and subtracting isolated endpoint energies is material and correctly retained.

Equation (16) has the stated negative massive residue. Equality of its Gaussian determinant with that of two ordinary scalar determinants does not restore reflection positivity for a source coupled to \(y\). The paper avoids extending this observation into an unsupported rejection of every statistical-surface construction.

For the scalar model, the two-field curvature vertex has magnitude \(q s^2/(2\sigma)\). Including the crossed channel gives (20), and division by \(2s\) in the explicitly stated scattering convention gives precisely (21). The sign and normalization of the local Lorentzian exchange operator in (22) are consistent with integrating out a positive massive scalar. The chiral normalization in (23) yields \(C_L=\pi^3/(30L^4)\); hence the factorized first-order insertion yields
\[
\Delta_q E_0=-\frac{8\pi^6q^2}{225m^2\sigma^2L^7}
=-\frac{32\pi^6b}{225L^7}.
\]
I find no missing channel factor or extra factor of two in this relation. The qualifications concerning composite-operator subtraction, independent matching terms and the determinant are essential and are present.

**Minor points and improvements**

1. **Sections 7.1–8, equations (21) and (25): state the perturbative error budget together.** The existing qualifications are correct but distributed across several paragraphs. Add one compact statement beside (25) identifying it as the leading four-phonon, first-order local-insertion result from tree matching, with higher derivative terms, further embedding interactions, quantum matching corrections and massive winding effects outside that displayed answer. Do not write a stronger remainder estimate without deriving it. In particular, the \(O(s^5)\) in (21) describes the displayed tree exchange expansion; it should not be read as a claim about every correction to the interacting phase.

2. **Sections 3.2 and 5.2, equations (6) and (15): display the source and boundary transformations explicitly in one place.** The necessary material is already present, so this is an accessibility improvement. A source \(J y\) becomes \(J\chi+gJv/\sqrt{1-g^2}\); this directly explains the massive residue. Likewise, retaining the two transformed endpoint conditions together makes clear why the Dirichlet formula is unavailable when only \(y\) is fixed. These short displays would strengthen the paper’s main methodological lesson.

3. **Appendix A: distinguish independent comparisons from algebraic consistency checks.** Reading `thickness88.py` shows genuinely different representations in the generalized eigenvalue/inverse-kernel comparison and the winding-sum/momentum-integral comparison. The final symbolic energy-versus-phase check, however, substitutes the analytic contraction and coefficient already supplied to the program. It checks their arithmetic consistency; it does not independently establish the first-order Hamiltonian insertion or the composite subtraction prescription. The prose derivation supplies that reasoning. Please make this distinction explicit so that “91 author checks” is not mistaken for 91 independent physical validations.

4. **Section 9, P24:** qualify what failure of the relation tests. The paragraph already separates independent matching contributions. For precision, make the rejection statement explicitly conditional on controlling those contributions and the omitted orders. Failure of an unseparated total measured phase/energy comparison would not by itself reject the proposed exchange mechanism.

**Author checks requested**

No additional numerical calculation is necessary for acceptance. Please provide short written responses to the four points above. For point 1, check the claimed orders against the actual perturbative organization rather than adding an inferred remainder. For point 3, confirm that the published reproduction description distinguishes numerical representation checks, symbolic identities and physical derivations.

If a stronger Hamiltonian verification is desired, an appropriate author check would be an explicit first-order reduction of the higher-time-derivative insertion to canonical free-field variables, including the treatment of equation-of-motion and total-derivative terms. I do not regard that extension as necessary for the stated result: the vacuum-functional argument and the specified subtraction already support it.

**New ideas**

A useful subsequent calculation would solve the mixed endpoint problem of (15), retaining the actual source matching. It could show quantitatively how a healthy bulk massive mode produces different interval spectra under different endpoint realizations. This would advance the existing programme without identifying a thickness or importing a microscopic mass. It is optional future work and should not delay this paper.

**Historical support, memory discipline and limitations**

The novelty language is appropriately restrained. Appendix B distinguishes remembered expectations, rederived results and the paper’s particular construction. No later numerical mass or coupling is used in the calculations reviewed. The unaltered second-line package contains later theoretical benchmarks, but none is needed as numerical evidence for the present results. The historical discussion of references [3]–[5] remains limited to the documented source coverage; it should retain that limitation.

This was a fresh read-only review of the frozen snapshot. I read the article, the calculation program as text, the stored calculation and document-check summaries, the source record, the relevant second-line briefs and assumptions, and relevant earlier-paper passages concerning scattering conventions, curvature redundancy and the unfinished \(L^{-5}\) calculation. I did not execute programs, rerun checks, generate calculations, modify files, retrieve external literature, independently validate the supplied hash, or inspect the rendered PDF and figures. The stored “91/91” result is an author report, not an independently reproduced result. My recommendation rests on inspection of the displayed derivations and the supplied textual evidence.
