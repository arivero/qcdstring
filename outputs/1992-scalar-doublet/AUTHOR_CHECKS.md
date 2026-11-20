# Checks for QCDS-92/1

The final manuscript contains **22,075 tokens** using `o200k_base` on the entire Markdown source. Pandoc and XeLaTeX produced a 22-page A4 PDF. Its extracted text contains all 32 equation labels, both figure captions and the mesh-refinement table.

- Manuscript SHA-256 `624868b95ad0e231a2fed2e20f4857feb1bae09525c68db8ac037a1f8ce5de94`
- Numerical printout SHA-256 `e22d2dff477fc3315c78eb637e6678e42b42c92e024083cc6c7ae7fcc9803207`
- Environment: Python 3.14.4, NumPy 2.3.5, SciPy 1.16.3, with one OpenBLAS thread for the spectrum.

The independent hand calculation in the referee report confirms the rank of the critical trace eigenspace, the virial coefficient, the normalized phonon matrix elements and the winding and detuning hypotheses. The author solved the deformed backgrounds and obtained the trace residues from the finite-element eigenvectors. The program checks the sign-reversed deformation, approach to the half-residue limit, changed neutral mass, multiple windings, fixed flux and scale virial. The final printout also records a third, dilation-based source measurement.

The table checker verifies all 17 data rows against the saved spectrum at their printed precision. The radial mesh and finite-radius comparisons report numerical convergence and do not supply a rigorous spectral enclosure. No human peer review or external journal submission is claimed. [Referee](REFEREE.md) · [Response](RESPONSE.md) · [Reproduction commands](README.md#reproduce-the-paper)
