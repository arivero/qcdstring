# Where does the QCD string live before it breaks?

**QCDS-25/S1 · December 2025 · Revised odd-year supplement**

The QCD object is the flux tube between an external static quark and antiquark. Lattice QCD showed thermal screening by 1998 and resolved string breaking at zero temperature in two-flavour QCD by 2005. The 2025 historical slot is the first free odd year after the 2024 quark-mass study and holographic internal-coordinate study. [Article](paper.md) · [PDF](paper.pdf) · [Sources](SOURCES.md)

**Section 9 performs the source displacement experiment.** In a confining two-row SU(3) Hamiltonian we move the static pair off a lower-cost row, vary its separation and measure the electric flux at the midpoint on the two lowest levels. With displaced sources the raw signal on the preferred row is 0.99925 on the ground state at three bonds. At five bonds it is 0.00040 on the screened ground state and 0.99925 on the excitation. The uniform control follows the source row. A second-order calculation in the unprojected model and an exactly factorized spectator example distinguish the large signal from a small subtraction artifact. The six-hop gap was calculated in the ordered-line variational space. The strip has scalar screening matter and imposed layer costs. [Displaced-source measurement](paper.md#9-moving-the-sources-through-a-confining-su3-strip) · [Results](results/strip.json) · [Registration](LOCALIZATION_REGISTRATION.md)

**Sections 7 and 8.3 use measured four-dimensional QCD data.** The N200 conditional spectral residuals are +0.00304 and +0.00077 in lattice units. In the published two-flavour action-density profile at 1.2 fm, the transverse signal contrast is 0.552 of its axial value at 0.25 fm and 0.115 at 0.50 fm. These distances are in ordinary space. The published graphics supply no joint covariance. [Energy measurements](data/n200.csv) · [Midplane profile](data/qcd-midplane.csv)

The original 21-page edition is archived under y2025. The revised paper and local measurements are tagged y2025-v2. [First edition](https://github.com/arivero/qcdstring/tree/y2025/outputs/2025-where-the-flux-lives) · [Checks](AUTHOR_CHECKS.md) · [Referees](REFEREE.md) · [Responses](RESPONSE.md)

## Reproduction

From this directory use Python with NumPy, SciPy and Matplotlib. The PDF uses Pandoc and XeLaTeX. Optional redigitization of the 2024 figure also uses PyMuPDF. The 2005 figure extraction uses the Python standard library. [Exact source archives and extraction commands](SOURCES.md)

~~~sh
MPLBACKEND=Agg OPENBLAS_NUM_THREADS=1 python3 code/check.py
python3 code/verify.py
MPLBACKEND=Agg OPENBLAS_NUM_THREADS=1 python3 code/strip.py
python3 code/strip_checks.py
OPENBLAS_NUM_THREADS=1 python3 code/strip_local.py
python3 code/build.py
~~~

## Present-day editorial cross-reference

The motivating Hopf-geometry calculation holds the low-energy QCD calibration fixed while following a static pair. Equation (31) of the revised article spells out a consequence of retaining only its factorized colour zero-mode operator. An internal test function orthogonal to the known kinetic weight has zero matrix element throughout string breaking at that order. A nonzero tube-specific signal in this probe requires additional matched operators. The strip computes such a position-resolved signal in a different explicit Hamiltonian. [Static-colour calculation in conneskk](https://github.com/arivero/conneskk/blob/6ac5bfa16f927c44c500509a6a3849e83704d84e/results/issues/29_static_colour.md)
