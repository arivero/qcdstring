# Where does the QCD string live before it breaks?

**QCDS-25/S1 · December 2025 · Third edition · editorial clarification y2025-v3.1**

The article follows a static colour source and antisource while the QCD flux tube between them breaks into two mesons. Lattice QCD showed thermal screening in 1998 and resolved string breaking at zero temperature by 2005. The 2025 slot follows a quark-mass study and a holographic internal-coordinate study, both published in 2024. [Article](paper.md) · [PDF](paper.pdf) · [Primary sources](SOURCES.md)

**What the first nonconstant internal mode measures.** Section 10 derives zero coupling to the even static source and signed left-quark overlaps of +1.28211 and −1.28211 at the specified neck. For the colour curvature these signs force the leading odd response to vanish between isosinglets across two-flavour string breaking. In three-flavour QCD a strange-quark loop gives a separated short-distance contribution to the static potential. Its sign, normalization and quark-mass dependence follow from the matched operator. A strange-current three-point function at breaking would test this one odd component. Distinct reflection-symmetric flux distributions give the same zero for it. [Section 10](paper.md#10-what-the-first-internal-mode-measures-in-qcd) · [Mode calculation](results/harmonics.json) · [Short-distance calculation](results/colour-loop.json)

**What the lattice already measures.** A separate scalar insertion projects onto the same flavour direction as an existing quark-mass scan. At 1.33 fm the response on the ground level relative to two isolated light mesons is +0.0001(22). The first excitation gives −0.0608(28) and the separately measured strange threshold gives −0.0619(83), in lattice units per unit uniform mass coordinate. These are finite chords along the simulated bare-mass trajectory. Their pure flavour-octet interpretation assumes small residual renormalized-trace drift. The paper gives the equal-volume comparison and the marginal-error and covariance limits. Earlier sections also analyze the N200 spectrum and the 2005 QCD action-density profile in ordinary space. [Mass response and controls](results/mass-response.json) · [27 energy markers](data/mass-scan-levels.csv) · [Midplane profile](data/qcd-midplane.csv)

Section 9 performs a displacement experiment in a confining two-row SU(3) Hamiltonian with scalar screening matter. Moving the sources off the cheaper row leaves the raw ground-state tube signal there at 0.99925 for three bonds. At five bonds the signal is 0.00040 on the screened ground state and 0.99925 on the excitation. The row costs are imposed, and the six-hop gap is calculated in an ordered-line variational space. [Displacement calculation](paper.md#9-moving-the-sources-through-a-confining-su3-strip) · [Results](results/strip.json)

The first edition has 21 pages, and the displacement edition has 26. Each has its own archived tag. [First edition](https://github.com/arivero/qcdstring/tree/y2025/outputs/2025-where-the-flux-lives) · [Displacement edition](https://github.com/arivero/qcdstring/tree/y2025-v2/outputs/2025-where-the-flux-lives) · [Author checks](AUTHOR_CHECKS.md) · [Referee reports](REFEREE.md) · [Responses](RESPONSE.md)

## Reproduction

Run the following commands in this directory with NumPy, SciPy and Matplotlib. PDF generation uses Pandoc and XeLaTeX. The versioned extraction of the 2024 vector figures uses PyMuPDF. [Archive hashes and extraction commands](SOURCES.md)

~~~sh
export OPENBLAS_NUM_THREADS=1 MPLBACKEND=Agg
python3 code/check.py
python3 code/verify.py
python3 code/strip.py
python3 code/strip_checks.py
python3 code/strip_local.py
python3 code/harmonic.py
python3 code/colour_loop.py
python3 code/mass_response.py
python3 code/build.py
~~~

## Present-day editorial cross-reference

A separate comparison attaches an antiquark and a scalar diquark to the same static line. It specifies a charge matrix element, an energy test and a scalar-response test of a possible defect supersymmetry. [Partner test](endpoint-partner-test.md)

The November 2026 working note derives the finite-cutoff light–strange scalar response of the full static-source matrix, follows the two line self-energies through subtraction, and gives a one-third slope check at equal quark masses. [Static-source mass derivative](static-source-mass-derivative.md)

The 2025 date belongs to the counterfactual series. The present-day choice of polar geometry in Section 10 comes from the companion project at revision 6ac5bfa. Its static-force calculation used the squared overlap of an even right-handed source. Its monopole sections, holomorphic mass map and transverse colour propagator supply the wavefunctions and pole block assumed in the article. The signed light overlaps, the matching of the two separately defined probes and the strange-loop response are derived in this edition. The published QCD comparison uses only material available by December 2025. [Static-colour force and its two poles](https://github.com/arivero/conneskk/blob/6ac5bfa16f927c44c500509a6a3849e83704d84e/results/issues/29_static_colour.md) · [Polar sections](https://github.com/arivero/conneskk/blob/6ac5bfa16f927c44c500509a6a3849e83704d84e/results/63_vortex_roots_and_diagonal_photon.md) · [Fermion operator](https://github.com/arivero/conneskk/blob/6ac5bfa16f927c44c500509a6a3849e83704d84e/results/67_fermion_masses_on_the_long_neck.md)

At the contemporary benchmark with meridian length $d=0.00049673$ GeV$^{-1}$, $d/a=18.63957$ and $B^{-1}=4.70474$ TeV, one has $B/a\simeq7.976$. The dimensionless pole masses $B\sqrt{\mu_o}$ and $B\sqrt{\mu_e}$ are 1.49046 and 2.96294. The corresponding values of $K_n/B^2$ are 0.50504 and 0.15426. An independent full-meridian spline calculation using the companion implementation checks both signed light overlaps. This dimensional example is editorial context. Neither the QCD string tension nor a localization probability is used to set it. [Parent mass and radius calibration](https://github.com/arivero/conneskk/blob/6ac5bfa16f927c44c500509a6a3849e83704d84e/results/99_nonround_hopf_colour_gap_and_level_crossing.md) · [Full-meridian basis](https://github.com/arivero/conneskk/blob/6ac5bfa16f927c44c500509a6a3849e83704d84e/paper/weak_current_spectrum.py) · [Verification](AUTHOR_CHECKS.md)
