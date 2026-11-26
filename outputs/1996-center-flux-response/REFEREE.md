# Independent second-line scientific referee report

**Submission** QCDS-96/1, *When do two units of electric flux bind?*  
**Recommendation** Publish after minor clarifications. The central calculation is internally sound as a fixed-rank, leading weak-deformation prediction. It is not a microscopic measurement or a nonperturbative proof of the asymptotic string spectrum.

I reviewed the submitted manuscript, source record, README, numerical printout and calculation, figure and publication-build code as text. I did not consult author notes, planning material, preregistration history or outside sources. I did not execute the submitted programs or reproduce their calculations numerically.

## Scientific assessment

The normalization chain is unusually explicit and appears consistent. With the monic curve convention, the variation of a shrinking period gives equation (8); interpolation then gives the quadratic gradient and the quartic gradient
$$
\partial_{a_i}u_4=s_i(x_i^2+2\Lambda^2).
$$
The $2\Lambda^2$ contribution follows from the single-trace Newton identity and cannot be omitted. The explicit four-color Jacobian independently makes the middle-node response transparent. I find no sign, dimension or relative-normalization error in this part of the argument.

The condensate-to-tension conversion is also consistent within the stated linearized action. In particular, the factors in $\xi_i=\sqrt2|F_i|$, $T_i=2\pi\xi_i$, and $C=4\sqrt2\pi\mu\Lambda$ agree internally. A common normalization uncertainty cancels in the ratios. It does not cancel an incorrectly specified quartic operator, a distinction the paper correctly emphasizes.

The center-sector minimization is essential and correctly performed. The map from the weight lattice to $\mathbb Z_4$, its root-lattice kernel, and all six antisymmetric-source weight assignments check algebraically. If the elementary costs are $A,B,A$, every odd-sector representative costs at least $A$. A charge-two representative either contains a middle step, costing at least $B$, or requires at least two odd steps, costing at least $2A$. Both bounds are attainable. Consequently
$$
{\cal R}(t)=\min\!\left\{2,\sqrt2\,\frac{1+2t}{1+4t}\right\}
$$
follows from the proposed leading action. The crossing and logarithmic slope quoted in equation (23) follow directly. The paper correctly avoids assigning a negative binding energy to the lowest physical sector.

The treatment of mixed winding signs is a strength. The outer vortex–antivortex configuration in different magnetic factors cannot be assigned the magnitude of a signed total central charge. The separate square completions justify its positive diagonal energy.

The matrix comparison in equations (17)–(18) is valid for a constant positive coupling matrix in the specified linearized two-derivative functional. The inverse-matrix estimate gives the stated coarse sandwich. The subsequent decoupling argument is conventional effective-field-theory power counting, rather than a corresponding bound on all configurations of the microscopic theory. This distinction is acknowledged in the body and should be equally visible in the headline claim.

## Numerical evidence

Inspection of the contour code finds a genuine alternative evaluation of the period derivatives: it integrates the original differential on coefficient-perturbed contours and solves a transposed Jacobian system. It does not insert the residue answer as its integration input. The graph search correctly implements arbitrary sequences of positive-cost center steps.

The stored results agree with the manuscript’s tables and convergence descriptions. This establishes documentary consistency, not independently reproduced numerical accuracy. The checks share the underlying curve, operator convention and electric-charge assignment with the analytic derivation. They cannot independently validate those physical inputs or establish a Wilson-loop spectrum.

The scan uses the imaginary quadratic gradients and real quartic-to-quadratic ratios after those quantities have been numerically checked. This is reasonable on the chosen real slice, but retaining and reporting the discarded phase residual would make that projection more transparent.

## Geometric and historical assessment

The freely wrapped flat membrane is rejected correctly **under its stated hypotheses**. Its absolute charge is integer winding and its area bound is additive in winding. Neither a scale fit nor a relabeling modulo four supplies a physical screening process or binding.

The relative-homology calculation is correct for connected $Y$, connected nonempty $S$, $H_1(Y)=\mathbb Z$, and the assumed charge interpretation. An image exactly $4\mathbb Z$, rather than merely the existence of one degree-four loop, is the relevant condition. This remains a conditional charge test. It establishes neither a fivebrane realization nor its tension or excitation spectrum. The manuscript generally maintains that boundary.

Known quadratic sine ratios, the IIA lift and allowed membrane boundaries are distinguished from the proposed quartic-source scan. Post-1996 developments are visibly segregated as retrospective comparisons. Nothing I inspected demonstrates an illicit use of a later embedding or tension formula in the derivation. Historical priority for the particular quartic experiment remains unassessed, as the source record says. The article makes geometric claims; there are no geological claims to evaluate.

## Requested corrections by section

1. **Abstract and §§1, 10:** State explicitly that the limiting physical ratio is predicted using the leading weak-monopole effective description. “We calculate both tensions” presently sounds stronger than the demonstrated scope. Equation (18) controls the linear effective functional; the extension to the microscopic lowest string energy relies on decoupling.
2. **§5:** Distinguish finite deformation corrections to the superpotential truncation from logarithmically vanishing kinetic mixing wherever a generic correction size is discussed. The manuscript already supplies both mechanisms; avoid wording that could suggest the total error is necessarily $O(\epsilon)$.
3. **§7 and README:** Describe “independent” as independent numerical evaluation within the same microscopic curve and charge assumptions. The current detailed explanation is accurate, but the abbreviated description should carry the same limitation. Optionally report maximum phase residuals before projecting the numerical gradients.
4. **§9 and conclusion:** Preserve the qualifications “freely wrapped,” “flat,” and “without additional charge sinks” in every abbreviated rejection of the membrane candidate. The argument does not exclude a general IIA/M-theory construction.
5. **Appendix B:** Continue to label the claimed contribution as a derivation within this programme, with literature priority unassessed. No stronger novelty claim is supported by the submitted evidence.

None of these requests changes the central formula or requires another simulation.

## Material limits and unsupported extrapolations

There is no submitted physical measurement validating P26, no controlled finite-$\epsilon$ crossing displacement or decay rate, no derived membrane fluctuation spectrum, and no established extrapolation to pure Yang–Mills or a simultaneous large-$N$ limit. Those conclusions would be materially unsupported; the manuscript mostly marks them as open.

I did not render or extract the PDF, inspect the figure image visually, verify live references or inspect the cited historical papers. Under the instruction not to execute programs, my publication-format review was limited to the manuscript and build sources. Accordingly I cannot certify PDF pagination, equation rendering, image legibility or hyperlink operation.

**Signed** Independent second-line scientific referee, second_line_referee (GPT-6.1 Sol).  
**Date** 26 November 2026.  
**Historical frame reviewed** Counterfactual December 1996.
