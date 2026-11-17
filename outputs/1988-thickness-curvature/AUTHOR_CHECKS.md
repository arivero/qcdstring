# Author checks for QCDS-88/1

Prepared 17 November 2026; historical date November 1988.

`code/thickness88.py` passes 91 checks. Individual results and numerical
tolerances are stored in `results/thickness88.json`; the readable printout
is `results/thickness88.txt`. These are checks of the stated calculations,
not an independent referee report or a formal proof certificate.

## Consequential comparisons

- Generalized normal modes and source overlaps reproduce the poles and
  residues of the two-field propagator. The field transformation independently
  diagonalizes both kinetic and mass matrices.
- Integrating out one field and restoring its determinant reproduces the
  complete Gaussian determinant at every tested momentum. The local
  field redefinition removes the fourth-derivative term only at its stated
  order.
- The periodic Bessel sum agrees with an independently integrated
  momentum-log expression. Interval and periodic massless limits, the
  double-length identity, and small/large-mass asymptotics pass.
- A positive fourth-order Euclidean kernel has a reflected covariance matrix
  with eigenvalues -0.005783940729 and 0.186906597275 in the supplied example.
  This tests its failure as a positive-spectral physical field, not all
  constrained rigid-surface theories.
- Explicit null momenta reproduce the scalar-curvature vertex. The crossed
  exchange phase is odd. Substitution of its low-energy coefficient and the
  analytic chiral contraction into the energy formula checks their symbolic
  arithmetic consistency. The first-order insertion rule and the composite
  subtraction prescription are established by the written derivation, not
  independently validated by that substitution.
- A closed geometric mode sum with an exponential regulator gives the
  finite chiral contraction. High-precision evaluations approach its derived
  limit with the predicted leading correction.

The document check compares all 13 printed numerical rows, 25 equation
labels, the local figures and earlier-paper links, and the three external
reference records with the paper. It checks the 1988 source cutoff and the
requested signature. Source identifiers and reading coverage are recorded
in `SOURCES.md`; only one page of the retrieved historical scan was read.

The revised PDF builds with Pandoc and XeLaTeX to 12 pages. The title and
abstract, both figures and all three tables were inspected during preparation;
the revised source/boundary displays, exchange amplitude and vacuum result
were also rendered and inspected. A bounding-box scan of all extracted PDF
words found none outside conservative page margins. Python compilation and
`git diff --check` pass. The inspection uses the installed Poppler tools.

The fresh gpt-6.1-sol referee found no substantive mathematical error and
recommended acceptance after four minor clarifications. All four were
addressed, as recorded in `RESPONSE.md`. That report is read-only: it does
not independently reproduce the stored program output. No numerical formula
changed during revision; the publication checks and PDF build were repeated.

## Limits that the checks do not remove

The normal-field health result is quadratic about a straight sheet. Its
nonlinear covariant completion is an effective ansatz, not a demonstrated
ultraviolet theory. Its physical source and endpoint conditions require
matching. The mass must lie within the effective cutoff for a threshold
interpretation.

The scalar-curvature vacuum shift is the q-dependent tree-matching
contribution at first order in the local operator, in d = 3. A separate
curvature expansion of the scalar determinant and independently allowed
matching coefficients are not predicted. The tree pole is not a unitary
description of the resonance region.

No lattice data are fitted; no QCD thickness, pseudoscalar mass, Pomeron
intercept or critical-string construction follows. The previous L^-5
calculation and higher-order quantization rules remain open.
