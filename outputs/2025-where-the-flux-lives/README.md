# Where does the QCD string live before it breaks?

**QCDS-25/S1 · December 2025 · Odd-year supplement**

The QCD object is the flux tube between an external static quark and antiquark. Lattice studies had observed screening at finite temperature by 1998 and had resolved breaking at zero temperature in two-flavour QCD by 2005. The first free odd year after the 2024 quark-mass study and the 2024 holographic internal-coordinate study is 2025. The supplement uses those papers to ask whether an additional dimension can leave an observable imprint on the flux while the tube exists. The latest regular biennial slot remains 1998.

[Read the article](paper.md) · [Download the paper](paper.pdf) · [Primary-source register](SOURCES.md)

Two measurements anchor the argument. On a homogeneous circle two translated sources produce exactly the same static force and opposite local electric-energy moments. In an existing QCD dataset, six energies at two separations and one at a third determine a conditional prediction for the other two levels of a rank-one mixing model. The N200 differences in lattice units are +0.00304 and +0.00077. The graphic gives marginal errors. Correlated spectra would be needed for a significance test. The proposed additional measurement is a nonuniform local insertion on both the extended and screened states in a model with a defined internal probe.

[Registered predictions](PREREGISTRATION.md) · [Nine digitized measurements](data/n200.csv) · [Author checks](AUTHOR_CHECKS.md) · [Independent referee](REFEREE.md) · [Response](RESPONSE.md)

## Reproduction

From this directory, run the following using Python with NumPy and Matplotlib, followed by Pandoc and XeLaTeX for the standalone PDF. The optional extraction from the original arXiv artwork additionally uses PyMuPDF. [Exact source download and digitization](SOURCES.md#reproducing-the-fig-4-extraction)

~~~sh
MPLBACKEND=Agg OPENBLAS_NUM_THREADS=1 python3 code/check.py
python3 code/verify.py
python3 code/build.py
~~~

## Present-day editorial cross-reference

The project that prompted the historical supplement compares a static colour pair on several Hopf geometries under a common low-energy calibration. The distinction between that calibration, calculable massive exchange, and a genuinely new strong-scale prediction motivates Section 4. Its contemporary numerical results are outside the bibliography of this 2025 article. [Static-colour calculation in conneskk](https://github.com/arivero/conneskk/blob/6ac5bfa16f927c44c500509a6a3849e83704d84e/results/issues/29_static_colour.md)
