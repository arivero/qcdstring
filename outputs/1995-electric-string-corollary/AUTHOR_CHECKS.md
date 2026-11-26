# Author checks for QCDS-95/S1

The manuscript has **27,400 tokens** under the programme convention (`o200k_base` over the complete Markdown) after the addition and revision of §11 on 26 November 2026; it had 19,080 before. The 25-page A4 PDF contains all 38 equation tags, the six data rows and the original figure.

- Manuscript SHA-256 `08d796ed45888ba81a02fbfec1dca4293e6a5005f0d05183babfdbf96bfc1853` (before §11: `b6c493241e0c0e37e36a902cb0523aebabc911f82f6a525e49f486ea9aed6da2`)
- Spin-structure JSON SHA-256 `6250b56f3066a4c3365e58e7dc32ae52386869fa9f79eb759d7bc9d1d9b78d93`
- Boson-Hessian JSON SHA-256 `2ad36838c96ae2cbbabf098d75c4ab9ec5a985001cf5ce55e7d2e393ffa64f03`
- Fermion-operator JSON SHA-256 `cf440c26ea0c45b35023d410048b5e67f02db0dd2560ba89cb4f2472fe050a26`
- Odd-sector JSON SHA-256 `9880179dca7186307dd06cc617dd341183952deee19a6a2fd11d5d30f8908c70`
- Numerical environment: Python 3.14.4, NumPy 2.3.5 and SciPy 1.16.3. The reproducible solver command sets `OPENBLAS_NUM_THREADS=1`.

The new calculation tests the critical charged-complement resolvent against the full imaginary-sector eigenproblem and checks the first finite-deformation row at the same grid spacing. Four critical meshes and a second outer boundary test the continuum estimates. The printout also gives the one-operator pole projections, the mass-gap/tension consistency ratio, and examples of the leading-log resolution hierarchy. The checker compares all six printed rows, both projected examples, the equation tags and local paper links with the source and stored values.

The independent hand report covers the microscopic interpretation and analytic derivations. It does not constitute human peer review. The principal physical restriction is small soft breaking and a scale separation in the two-derivative dual theory. Individual physical quantum masses and widths require additional matching. [Referee](REFEREE.md) · [Response](RESPONSE.md) · [Reproduction](README.md#reproduction)

## Checks for §11 (26 November 2026)

`code/spin_structure.py` writes `results/spin-structure.json` `code/fermion_operator.py` writes `results/fermion-operator.json` and `code/boson_hessian.py` writes `results/boson-hessian.json`; `code/check_article.py` compares the printed §11 values with all three.

- **Profile and normalization.** On the distributed critical profile the Bogomolny residuals are below $4\times10^{-10}$, $T/\pi=0.9999994$, and the translation (Goldstino) profile has norm squared $T/2$ to seven digits.
- **Kernel of the deformation operator.** The operator (28), applied to the covariant translation on a Cartesian grid of spacing 0.025, leaves residuals of $1.9\times10^{-4}$ and $7.9\times10^{-5}$ of $\max|\eta|$, consistent with $O(h^2)$.
- **Gap.** The neutral block of (29) has one level below one, $0.777464$ at spacing 0.02 (QCDS-91/S1: $0.7774728$). For angular momenta 1 and 2 the lowest level minus one falls by a factor four per doubling of the box (40, 80, 160), as for continuum levels.
- **Determinant and conformal weights.** Regulated oscillator sums reproduce $2\pi\zeta(-1)$ and $2\pi\zeta(-1,\tfrac12)$ to $3\times10^{-7}$; the 1986 massive Dirac difference times $2L/\pi$ is $0.99936$ at $mL=10^{-3}$; the conformal weights give $0$ and $-\pi/(2L)$ for R and NS.
- **Fermion operator.** `code/fermion_operator.py` checks symbolically, with generic background fields and without the Bogomolny equations, that the eight component relations (31) of both sectors are equations of motion times $\pm1$ or $\pm i$ (or their conjugates). It checks numerically that the mass matrix (30) has four singular values equal to $f$ at random points and that $\chi_\pm$ removes all cross-sector entries at $w=0$, for three phases of the superpotential coupling.
- **Projector.** The kernel projector (32) has real rank four; the map from two copies of the bosonic kernel onto it is the identity in the variables of (31).
- **Deformation bound.** On the deformed branch of (6) (solver of QCDS-92/1) the bound (33) is $0.01004$, $0.10356$, $0.21413$, $0.33141$, $0.45488$ at $w=0.01,0.1,0.2,0.3,0.4$, with $\sup|s|\le w/2$. It reaches $\nu_0/2=0.44087$ at $w_*=0.3889$; outer radius 35 instead of 25 and 40001 instead of 20001 sampling points change $B(w_*)$ by less than $10^{-8}$. The quoted range is $0<w\le0.388$.
- **Length tests.** The three-length estimator and the $L\to2L$ ratio converge on model energies with specified remainders (rows in the JSON).

- **Bosonic Hessian at $w>0$.** `code/boson_hessian.py` derives the gauge-fixed radial quadratic form of each partial wave from (35) symbolically and solves it with $P_1$ elements (spacing 0.05, radius 25). Validation: at $w=0.01$ the angular-momentum-zero masses $0.876751$, $0.881702$, $0.886750$ agree with Table 1 of QCDS-92/1 to $3\times10^{-5}$; the translation levels are $5.1\times10^{-5}$ and $1.3\times10^{-5}$ at spacings 0.05 and 0.025. Scan: $w=0$–$0.42$ in steps of 0.02 for $\ell\le2$, $\ell\le8$ at six values, $\ell=12,16$ at $w=0$ and $0.388$; no negative level; lowest non-translation level $\ge0.4389$, changing by less than 0.018 per step. Budget at $w=0.388$: spacing 0.025 changes the lowest level by $3\times10^{-5}$, radius 35 by less than $10^{-9}$. Result: $w_B=0.42$ (end of the scan) $\ge w_*$.

Everything in §11 holds in the two-derivative dual action of (3). Section 11 was written after the independent referee report and has not been refereed.
