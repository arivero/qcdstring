# Author checks for QCDS-95/S1

The final manuscript has **19,080 tokens** under the programme convention (`o200k_base` over the complete Markdown). The 19-page A4 PDF contains all 24 equation tags, the six data rows and the original figure.

- Manuscript SHA-256 `b6c493241e0c0e37e36a902cb0523aebabc911f82f6a525e49f486ea9aed6da2`
- Odd-sector JSON SHA-256 `9880179dca7186307dd06cc617dd341183952deee19a6a2fd11d5d30f8908c70`
- Numerical environment: Python 3.14.4, NumPy 2.3.5 and SciPy 1.16.3. The reproducible solver command sets `OPENBLAS_NUM_THREADS=1`.

The new calculation tests the critical charged-complement resolvent against the full imaginary-sector eigenproblem and checks the first finite-deformation row at the same grid spacing. Four critical meshes and a second outer boundary test the continuum estimates. The printout also gives the one-operator pole projections, the mass-gap/tension consistency ratio, and examples of the leading-log resolution hierarchy. The checker compares all six printed rows, both projected examples, the equation tags and local paper links with the source and stored values.

The independent hand report covers the microscopic interpretation and analytic derivations. It does not constitute human peer review. The principal physical restriction is small soft breaking and a scale separation in the two-derivative dual theory. Individual physical quantum masses and widths require additional matching. [Referee](REFEREE.md) · [Response](RESPONSE.md) · [Reproduction](README.md#reproduction)
