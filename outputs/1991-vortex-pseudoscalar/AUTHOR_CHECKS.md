# Author checks for QCDS-91/S1

The numerical evidence is the output of the radial program on the positive unit vortex. All masses below are in vector-mass units. The numbers come from profiles solved afresh with the second-order static equations. [Program](code/vortex.py) · [Results](results/radial.json)

## Checks on the spectrum and the cubic matrix element

- A planar logarithmic trial function puts the lowest electric mode strictly below the vector threshold. Positivity of the unshifted energy excludes a zero eigenmass. The rest-frame mode has nonzero gauge-invariant electric field. Its boost obeys the sheet constraint. These are analytic checks, independent of boundary meshes.
- Collocation with an exterior Bessel tail gives squared frequencies 0.66797749, 0.77747281 and 0.88050145 for the three couplings in the paper. A flux-conserving cell discretization, with a distant Dirichlet face, converges to the same critical values for both the mass and the matrix element. The methods share a computed background.
- Across the five stored runs the flux differs from one by less than $5\times10^{-13}$ in units of $2\pi/e$. The difference of magnetic and potential energy integrals is below $3\times10^{-11}$ in units of $2\pi v^2$. The integrated bound-state equation, which uses the first power of the wave, agrees within $2\times10^{-11}$ in relative units. The radial Rayleigh quotient is also evaluated directly.
- The electric source projected from the charged matter current and the one projected from the magnetic field agree within $6\times10^{-11}$ in relative units. The analytic identity $HB=4eK$ explains their equality. It is independent of the first-order critical background equations.
- At critical coupling the radial scalar Hessian maps the nodeless wave to a regular normalizable even state. A symmetric finite difference of the translation norm along that normalized mode, using $e=m_V=1$, gives $0.9337546164$. Its ratio to the odd matrix-element coefficient $\mu\alpha$ agrees with one within $2\times10^{-10}$.
- The normalized antisymmetric projector squares to itself, with diagonal strengths twice the ordered $12$ strength. The scalar projector is orthogonal to it. The infinite-volume two-phonon phase-space normalization agrees analytically with the periodic level density times the square of the finite-volume mixing matrix element.

The stored comparison is at classical or leading weak-coupling order as specified in the manuscript. A bound normal mode in the transverse direction and a finite partial width along the tube can occur together. No value from the registered colour-tube prediction entered the calculation.

After review we also compared the partial widths into all translations at critical coupling. Each of the two identical-species even final states carries the factor $1/2$ in phase space. Adding the two partial rates gives the one distinct-species odd rate. The sum makes no assumption about other channels.

## November 18 edition

The post-review rerun reproduced the stored radial results byte for byte. The final Markdown contains **17,479 tokens** by the programme convention (o200k_base over the complete file) and 482 lines. Pandoc and XeLaTeX built an 18-page A4 PDF. The three tables, the figure, equations (1)–(31), the references and the local package links were checked. The revised manuscript SHA-256 is `68fb34be239d7865de7e53792f32ca80d0359d1eaab7ea99a362bdfea760f992`. The submitted hash is in the independent report.

## November 20 edition

The revised manuscript contains 18,379 tokens under the same convention. Its SHA-256 is `b45eb95ff72294473bf3841124b0bc87b4d715e833a20ed10f54d8fa7bb4fb30`. The Python rerun reproduced all five stored radial records, including both critical-profile residuals. [Environment](results/environment.txt)

A direct quadrature of the two terms in Eq. (27) of arXiv:2603.05243v1 checks the integration by parts in the retrospective note. On the critical profile, sample 18,001 points from the inner cutoff to 36 vector lengths. Normalize the decaying eigenfunction with the plane measure, form the canonical pair in (27) of this paper, and integrate with Simpson quadrature. The pair has squared plane norm 1.000000003. Its scalar and vector peaks are 0.16258 and 0.10250, consistent with Fig. 1 of the preprint. The unreduced integral gives $|\kappa|/\pi=0.3822942$, or 0.3823 at the precision of the external comparison. The factor of two persists when evaluating the plotted mode convention directly. [Preprint, Fig. 1 and Eqs. (27)–(29)](https://arxiv.org/html/2603.05243v1)
