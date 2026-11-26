# Author checks for QCDS-95/S1

The manuscript has **24,658 tokens** under the programme convention (`o200k_base` over the complete Markdown) after the addition of §11 on 26 November 2026; it had 19,080 before. The 23-page A4 PDF contains all 34 equation tags, the six data rows and the original figure.

- Manuscript SHA-256 `242a7c3fc4ab02f9ca1a6a221c2ba0c7d86c3bbe6fd19543768fd85e96e5a33b` (before §11: `b6c493241e0c0e37e36a902cb0523aebabc911f82f6a525e49f486ea9aed6da2`)
- Spin-structure JSON SHA-256 `a588fdf6d858e692dae8aa01fdffae1f2e5bf748e5811c8326993f91d6482e13`
- Odd-sector JSON SHA-256 `9880179dca7186307dd06cc617dd341183952deee19a6a2fd11d5d30f8908c70`
- Numerical environment: Python 3.14.4, NumPy 2.3.5 and SciPy 1.16.3. The reproducible solver command sets `OPENBLAS_NUM_THREADS=1`.

The new calculation tests the critical charged-complement resolvent against the full imaginary-sector eigenproblem and checks the first finite-deformation row at the same grid spacing. Four critical meshes and a second outer boundary test the continuum estimates. The printout also gives the one-operator pole projections, the mass-gap/tension consistency ratio, and examples of the leading-log resolution hierarchy. The checker compares all six printed rows, both projected examples, the equation tags and local paper links with the source and stored values.

The independent hand report covers the microscopic interpretation and analytic derivations. It does not constitute human peer review. The principal physical restriction is small soft breaking and a scale separation in the two-derivative dual theory. Individual physical quantum masses and widths require additional matching. [Referee](REFEREE.md) · [Response](RESPONSE.md) · [Reproduction](README.md#reproduction)

## Checks for §11 (26 November 2026)

`code/spin_structure.py` writes `results/spin-structure.json`; `code/check_article.py` compares the printed §11 values with it.

- **Profile and normalization.** On the distributed critical profile the Bogomolny residuals are below $4\times10^{-10}$, $T/\pi=0.9999994$, and the translation (Goldstino) profile has norm squared $T/2$ to seven digits.
- **Kernel of the deformation operator.** The operator (28), applied to the covariant translation on a Cartesian grid of spacing 0.025, leaves residuals of $1.9\times10^{-4}$ and $7.9\times10^{-5}$ of $\max|\eta|$, consistent with $O(h^2)$.
- **Gap.** The neutral block of (29) has one level below one, $0.777464$ at spacing 0.02 (QCDS-91/S1: $0.7774728$). For angular momenta 1 and 2 the lowest level minus one falls by a factor four per doubling of the box (40, 80, 160), as for continuum levels.
- **Determinant and conformal weights.** Regulated oscillator sums reproduce $2\pi\zeta(-1)$ and $2\pi\zeta(-1,\tfrac12)$ to $3\times10^{-7}$; the 1986 massive Dirac difference times $2L/\pi$ is $0.99936$ at $mL=10^{-3}$; the conformal weights give $0$ and $-\pi/(2L)$ for R and NS.
- **Projector.** The kernel projector (30) has real rank four under (H$_F$); the contour radius in (31) is $\nu_0/2=0.4409$. The norm of the profile response that would turn (31) into a numerical bound on $w$ was not computed.
- **Length tests.** The three-length estimator and the $L\to2L$ ratio converge on model energies with specified remainders (rows in the JSON).

What remains conditional: hypothesis (H$_F$), the identification of the BPS fermion operator with $\begin{pmatrix}0&D^\dagger\\D&0\end{pmatrix}$ in each $SU(2)_R$ sector, and the constant $w_*$. Section 11 was written after the independent referee report and has not been refereed.
