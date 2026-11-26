# Author verification

Codex GPT-6 performed these checks independently of the text-only referee.

| Check | Result |
|---|---|
| Series requirements | The original edition contained 19,140 o200k_base tokens and 21 pages. The revised paper.md contains 24,352 o200k_base tokens, including equations, appendices and references. Its A4 PDF has 26 pages. |
| Prior record | The [registration commit](https://github.com/arivero/qcdstring/commit/5a558ca8dbe9f715ec8a15a267e7261817db9dc0) was pushed to main before extracting or running either test. It fixed the thresholds for code checks, Table 4 selections and N200 separations. The historical year of the supplement is distinct from the real repository timestamps. |
| Circle test | Direct periodic Green-function quadrature with 256 angles and a five-point derivative gives the two force and density predictions at the registered amplitudes and separation within 6 × 10⁻¹². Two phases in a separate two-harmonic integration reproduce the sine and cosine midpoint moments within 2 × 10⁻¹⁶. |
| Known three-channel control | Matrix diagonalization with the Table 4 parameters at 7, 8 and 9 flow lengths recovers the two withheld levels at 8 within 3 × 10⁻¹⁶. This control uses data generated from the assumed matrix. |
| Published measured input | Downloaded the 2024 version 2 source archive twice and verified SHA-256 digests of the archive, vector drawing and axes file. The independently named v2 download regenerates the archived CSV byte for byte. Matching markers, error bars and ticks identifies three states at each selected separation. [Provenance](SOURCES.md) |
| N200 inverse | Two triplets at 17 and 21 and the middle level at 19 give −0.01562793 and +0.02868351. Decimal symmetric-polynomial coefficients followed by division by the supplied root agree with the eigenvalue implementation to 1.4 × 10⁻¹⁷. The six outside levels interlace strictly. |
| Invariance and conditioning | Repeating the decimal inverse after shifting every energy by 2.7 translates both predicted energies with discrepancy below 10⁻³⁶. The derivative with respect to the conditioning middle level agrees with both analytic weight ratios within 10⁻⁷. Both residual sensitivities include the uncertainties of the outside triplets. |
| Observable limits | The QCD inputs are finite-spacing, correlator-derived measurements previously published by Bulava et al. The paper gives the marginal bars, common subtraction, digitization scale and the missing covariance. The model directions and the Abelian local density supply no measurement of an extra coordinate of QCD. |
| Typesetting | Rendered with Pandoc and XeLaTeX, checked the A4 pages for off-page text, and inspected the opening page and the two-panel figure. The PDF resolves repository links against the tagged edition. |

From the article directory run the commands in the [README](README.md) for the plot, numerical values and PDF. The pure Python decimal verification uses only the standard library and reads the published CSV and stored floating-point results. [Decimal and Fourier verification](code/verify.py) · [Verification printout](results/verification.json) · [Main printout](results/checks.json)

## Displaced-source revision

- The [P30 registration](https://github.com/arivero/qcdstring/commit/827633aca323713e2e58e09c9769b6c03b602f2f) preceded construction and diagonalization of the strip. Its finite-hopping bounds, uniform control and gap comparisons are reported with the original parameters.
- We rebuilt both published CSVs from the versioned arXiv archives in a separate temporary directory. Rerunning all analysis programs there reproduced the nine archived CSV, numerical-result and plot files byte for byte under a single BLAS thread.
- Direct matrix elements and a finite difference of the four-sector energy agree to within 9 × 10⁻¹¹ for both levels at separations three and five. Reflecting both features and sources reproduces the comparison within 2 × 10⁻¹⁵. [Finite strip results](results/strip.json)
- A rational sum over 720 orders independently reproduces the subset-recursion coefficient. The surrounding gaps and the 15-point coarse mass scan plus local points bound the observed stationary minimum from both sides. [Verification](results/strip-verification.json)
- The full-Hamiltonian second-order formula is derived in Section 9.4 and evaluated arithmetically. A separate SU(3) Weyl-matrix sum checks the Haar moments used there. In an isolated link with distant spectator mesons, diagonalization with complete product contractions removes the spurious ordered-basis offsets exactly. The comparable error of the full connected strip is unknown. [Local checks](results/strip-local.json)
- We checked the 26-page revised PDF, the bounds of each page, both scientific figures and links against y2025-v2. The original y2025 tag records the first edition.
