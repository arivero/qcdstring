# Author checks for QCDS-86/1

Edition prepared 13 November 2026 (machine date), historical date November 1986.
The user explicitly waived independent refereeing. These are author checks,
not an external report or a formal proof certificate.

## Calculations

`python3 code/worldsheet86.py` passes **174 checks**. The printout is
`results/worldsheet86.txt`; numerical errors, tolerances and pass states are
stored individually in `results/worldsheet86.json`.

The consequential comparisons are:

- Finite-size determinants: the Bessel sum agrees with an independently
  integrated momentum-logarithm expression for both spin structures, including
  the massless limit. The odd-winding identity and large-length limit agree.
- Gross-Neveu saddle: roots of the Bessel gap equation are stationary points
  of the independently integrated potential and agree with direct minimization.
  The full matched energy is no higher than the fixed-mass evaluation in each
  sector. The condensate contribution is included.
- Critical region: a spatial-cutoff mode sum agrees with the renormalized
  curvature; the near-critical solution agrees with the derived quartic
  coefficient. This checks the homogeneous large-flavour saddle only.
- Dimensional matching and classical rotation: the formal epsilon-flow signs,
  invariant one-loop gauge scale, and rotating-string integrals agree with the
  formulas displayed in the paper.
- Compact-coordinate pinning: a radial momentum-shell integral gives the vertex
  dimension, an independent Gaussian cosine average gives the linear relevance
  exponent, and a finite-difference Hessian gives the classical small-oscillation
  mass. These do not establish a quantum mass at arbitrary stiffness.

The checks exposed and resolved a Python name-shadowing error introduced while
adding the compact-coordinate section; the final script passes as a whole.
The equations were also read for dimensions, signs, species multiplicities,
spin-sector conventions, and the distinction between matching and prediction.

## Publication consistency

`python3 code/check_document.py` passes. It checks all 17 printed numerical
rows against the computed output, 46 unique equation labels, the 12 main
sections, all 36 cited references, and 31 externally verified bibliographic
identifiers dated no later than 1986. It also checks local figures,
earlier-paper paths and the explicit referee waiver. Its output is retained
in `results/document_checks.txt`.

`python3 code/build.py` produces the **29-page PDF**. The title/abstract,
saddle table and new compact-coordinate section were rendered and inspected.
A bounding-box scan of all PDF words found no text outside a conservative
page boundary. Both scientific figures were inspected. Python compilation
and `git diff --check` pass. No new dependency was installed for the checks.
The environment versions are in `results/environment.txt`.

The reference metadata were checked against INSPIRE. Access gaps, the two
selected original readings, the existing transcript used, and the absence of
a full review of all sources are recorded in `SOURCES.md`. A metadata match is
not treated as a full-text verification. The scientific bibliography contains
no post-1986 result. The reported 2026 Lean news is not a premise or a source.

## Remaining limits

The central new model is nonchiral, homogeneous and leading order in large
worldsheet flavour number. It has not been derived from QCD, matched to the
four-dimensional spectrum, or embedded in a complete critical string.
The finite-flavour limitation of the thermal transition is stated. A worldsheet
spin-sector difference is a physical diagnostic only after a microscopic
realization of both sectors is specified.

The compact pinning potential is imposed; neither its origin nor radius
stabilization is derived. Its weak-deformation relevance criterion is not a
bound on every compactification. The higher-dimensional fixed-point formula
is a small-epsilon countertest, not a continuum existence proof.

Earlier data are reviewed with their original dimensional and systematic
qualifications. No gauge simulation or raw-data refit is performed. The direct
area-action L^-5 calculation and the higher-order quantization rules left in
1984 remain unfinished. These checks do not close those obligations or the
physical QCD predictions in the ledger.
