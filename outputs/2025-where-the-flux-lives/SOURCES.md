# Primary sources and provenance of the QCD measurements

The article is set in December 2025. The first free odd year after the two 2024 publications cited below is 2025. The source dates are actual publication or preprint dates. The series date describes a counterfactual paper. The [registration commit](https://github.com/arivero/qcdstring/commit/5a558ca8dbe9f715ec8a15a267e7261817db9dc0) is part of the real repository history.

## Observations of the QCD string

| Source | What we use |
|---|---|
| [Alexandrou et al., preprint 1992, Nucl. Phys. B 1994](https://arxiv.org/abs/hep-lat/9211042) | A static-light threshold gave an early estimate of where the rising potential would saturate. Bulava et al. also identify this estimate in the introduction to their 2024 paper. |
| [Drummond, 1998](https://arxiv.org/abs/hep-lat/9805012) | Strong-coupling treatment of mixing between a string and two mesons. |
| [DeTar, Kaczmarek, Karsch and Laermann, preprint 1998, Phys. Rev. D 1999](https://arxiv.org/abs/hep-lat/9808028) | Polyakov-loop correlations show screening of the static-pair free energy in the confining phase at nonzero temperature in dynamical-quark QCD. |
| [Philipsen and Wittig, 1998](https://arxiv.org/abs/hep-lat/9807020) and [Knechtli and Sommer, 1998](https://arxiv.org/abs/hep-lat/9807022) | Early non-Abelian gauge–Higgs demonstrations in three and four spacetime dimensions. These use scalar matter. |
| [Bali et al., Phys. Rev. D 71 (2005) 114513](https://arxiv.org/abs/hep-lat/0505012) | Zero-temperature two-flavour QCD, two-channel spectrum, minimum gap about 51(3) MeV and crossing region about 1.25 fm. See particularly Eqs. (92) and (93). |
| [Prkacin et al., October 2005 preprint](https://arxiv.org/abs/hep-lat/0510051) | Action-density distributions around the pair as the separation changes, in ordinary spatial coordinates. This is the source for the spatial visualization. |
| [Bulava et al., 2019](https://arxiv.org/abs/1902.04006) | Three static-source levels and distinct light and strange thresholds on N200, with two light sea flavours and a strange sea flavour. |
| [Bulava et al., 2024, version 2](https://arxiv.org/abs/2403.00754v2) | Fig. 4 supplies measured levels and their marginal errors for three ensembles at one lattice spacing. Eq. (6) specifies the Hamiltonian and the light multiplicity. Table 4 supplies the separate physical-mass fit control. The final physical-mass bare-diagonal crossings are 1.211(7)(11) and 1.336(7)(12) fm. |

## Internal coordinates, force measurements and matching

| Source | Physical content used here |
|---|---|
| [Witten, 1997](https://arxiv.org/abs/hep-th/9706109) | Section 3.1, especially Eqs. (3.7)–(3.12). A free wrapped membrane and a strip bound to the M5 carry the same relative class. The binding and unprotected tensions are discussed explicitly. |
| [Hanany, Strassler and Zaffaroni, 1997](https://arxiv.org/abs/hep-th/9707244) | Strings, confinement and flux sectors in MQCD. |
| [Dvali and Shifman, 1996 preprint, 1997 journal](https://arxiv.org/abs/hep-th/9612128) and [Laine et al., 2004](https://arxiv.org/abs/hep-ph/0404058) | The confining-bulk mechanism and a lattice measurement of static forces for charges at different positions relative to a wall in 2+1 dimensions. |
| [Fu and Nielsen, 1984](https://doi.org/10.1016/0550-3213(84)90529-7), [Knechtli et al., 2010](https://arxiv.org/abs/1011.0345) and [Del Debbio et al., 2013](https://arxiv.org/abs/1305.0752) | The Abelian layer phase, a five-dimensional non-Abelian proposal and the large-volume first-order-transition evidence. |
| [de Forcrand, Kurkela and Panero, 2010](https://arxiv.org/abs/1003.4643) and [Meyer, 2005](https://arxiv.org/abs/hep-th/0506034) | Long winding tube in compactified pure Yang–Mills and the effective world-sheet question about a compact transverse displacement. |
| [Witten, 1998](https://arxiv.org/abs/hep-th/9803131) and [Brandhuber et al., 1998](https://arxiv.org/abs/hep-th/9803263) | Radial redshift and Wilson-loop area laws in the confining compactification. |
| [Bigazzi et al., preprint 2008, journal 2009](https://arxiv.org/abs/0812.3399) | Backreacted massive dynamical flavours and a scale-dependent comparison of screening in a confining dual. |
| [Giliberti, Fatemiabhari and Núñez, JHEP 11 (2024) 068](https://arxiv.org/abs/2409.04539) | Sections 3–4 allow a connected string embedding to vary along the internal quiver coordinate. The authors explicitly distinguish the bending and energy saturation from an actual disconnected, reattached world sheet. |
| [Dixon, Kaplunovsky and Louis, 1991](https://doi.org/10.1016/0550-3213(91)90490-O) and [Contino et al., preprint 2001, journal 2002](https://arxiv.org/abs/hep-ph/0108102) | Moduli-dependent gauge thresholds and explicit matching after integration over a KK tower, in their stated ultraviolet theories. |
| [Michael, 1995 preprint](https://arxiv.org/abs/hep-lat/9504016) and [Bouchard et al., 2016 preprint](https://arxiv.org/abs/1612.06963) | Lattice action and energy sum rules, and the Euclidean Feynman–Hellmann identity for matrix elements. |

## Reproducing the 2024 lattice figures

The primary archive is [arXiv:2403.00754v2, source download](https://arxiv.org/src/2403.00754v2). From the article directory the following commands obtain the two vector drawings and their axes in a temporary directory and regenerate the energy, coordinate and threshold tables. Python dependencies are NumPy, SciPy, Matplotlib and PyMuPDF.

~~~sh
source_dir=$(mktemp -d)
curl -fL https://arxiv.org/src/2403.00754v2 -o "$source_dir/source.tar.gz"
tar -xzf "$source_dir/source.tar.gz" -C "$source_dir" VRensembles.pdf VRensembles_fig.tex dStatMassdep.pdf dStatMassdep_fig.tex
sha256sum "$source_dir/source.tar.gz" "$source_dir/VRensembles.pdf" "$source_dir/VRensembles_fig.tex" "$source_dir/dStatMassdep.pdf" "$source_dir/dStatMassdep_fig.tex"
python3 code/digitize.py "$source_dir/VRensembles.pdf"
python3 code/mass_scan.py "$source_dir"
MPLBACKEND=Agg OPENBLAS_NUM_THREADS=1 python3 code/check.py
~~~

| Member | SHA-256 |
|---|---|
| Version 2 source archive | 2abca11623f10491e763d0a774100c9102f2d6fcf4c8d7617235f03968fe64b5 |
| VRensembles.pdf | abeae9c810a8b0b00250328c87951fbdb4739de0cf400d9a60f89c88c3981783 |
| VRensembles_fig.tex | 2e59bd72ae8a6fa2234dfc1d9d08cf4c2ca74a241d1ae356733734fb338c3096 |
| dStatMassdep.pdf | 19b476120004e98a315277f49c0fe3b36a1f5f8708fcd3a946cf3be0f8d9755c |
| dStatMassdep_fig.tex | 1b35e447e7bb89ddd9dc509c542df4e8c0fb3b7172dbfd435e1535da9008b012 |

The archive also contains model.tex, method.tex and massdep.tex. The Fig. 4 caption in model.tex identifies the markers as estimates of levels from the generalized eigenvalue analysis and the bands as the seven-parameter fits. The middle-panel labels in VRensembles_fig.tex identify N200 and the integer separations. Its vertical axis is the static energy minus twice the static-light energy in lattice units. The graphic has size 481 by 198 PDF points. The black bottom ticks for 17, 19 and 21 have abscissae 204.398, 249.648 and 294.898 points. The same tick-to-energy calibration applies in each panel. At each of those abscissae the code identifies three filled point markers, matches them to the three vertical error strokes and ignores the polygons for the model bands. Printed coordinates at about 0.05 point resolution make rounding on the order of 0.00005 in energy visible. These checks preserve the provenance of a vector digitization from an existing publication. Only the markers, axes and marginal errors are available through this route. [Digitized data](data/n200.csv) · [Extraction code](code/digitize.py) · [Results](results/checks.json)

## The QCD midpoint and the SU(3) calculation in the revised edition

Z. Prkacin et al. reported the vacuum-subtracted transverse profiles at a static-source separation of 1.2 fm in their Fig. 2. Section 3 and Fig. 3 describe spatial action-density measurements on the two levels and the interpolation used in their animations. The transverse coordinates are ordinary spatial distances. In Fig. 2 the square markers show the action density and the circles show the energy density multiplied by 29. The ratio in our Eq. (23) refers the square-marker heights to the mean of the two outer markers at ±1 fm. The x-axis ticks fix one fm at 2012 drawing units and the origin at 2520. The drawing gives heights 2882, 2077, 1292 and 1086 at 0, 0.25, 0.50 and 1.00 fm. There is no absolute action unit or joint covariance in this extraction. [2005 paper](https://arxiv.org/abs/hep-lat/0510051v1) · [Original source](https://arxiv.org/src/hep-lat/0510051v1) · [25 published markers](data/qcd-midplane.csv)

~~~sh
profile_dir=$(mktemp -d)
curl -fL https://arxiv.org/src/hep-lat/0510051v1 -o "$profile_dir/source.tar.gz"
tar -xzf "$profile_dir/source.tar.gz" -C "$profile_dir" transverse.ps
sha256sum "$profile_dir/source.tar.gz" "$profile_dir/transverse.ps"
python3 code/qcd_profile.py "$profile_dir/transverse.ps"
~~~

The version 1 archive hash is 53ac3f1112e92646f55062fbb2c8e937132f4e0c99352488c629b3b9fcdfd6e6 and the member hash is 1f513a0ab0696b33d9280b13c81a95bdf34f1090176c902530f943bd08d85d4c.

Kogut and Susskind give the electric-Casimir and matter-hopping framework of Hamiltonian lattice gauge theory. Drummond treats strong-coupling mixing between a string and two screened sources. Our two-row action omits magnetic plaquettes, projects each hop onto an empty-to-occupied electric link transition and uses group-valued scalar matter. The geometry, variational basis, parameters and outputs are those defined in Section 9. The computation uses no lattice QCD fit parameters. [Hamiltonian formulation (1975)](https://doi.org/10.1103/PhysRevD.11.395) · [String breaking at strong coupling (1998)](https://arxiv.org/abs/hep-lat/9805012) · [Prior registration](https://github.com/arivero/qcdstring/commit/827633aca323713e2e58e09c9769b6c03b602f2f)

## The first harmonic, three ensembles and a strange vacuum polarization

The 2024 analysis specifies a constant sum of subtracted bare quark masses at common bare coupling $\beta=3.55$. Table 1 gives $a_{\rm lat}=0.0633(4)(6)$ fm and spatial extents 64, 48 and 48 lattice sites for D200, N200 and N203. Each Fig. 4 panel has six bottom ticks from 17 through 22. At 17, 19 and 21 we match each of the three ordered measured levels to its vertical error stroke. The older N200-only extraction is retained as a separate nine-row file. The Fig. 5 mass parameter and static-meson gap are calibrated against the original graphics' six horizontal and seven vertical labels. We isolate the three filled point symbols and their error strokes from the fit and its band. The respective mass coordinates are 0.23849, 0.47343 and 0.70132. Rounded meson masses in Table 1 alone give 0.23962, 0.46890 and 0.68974. The figure uses the unrounded underlying masses, as described in the article. The analysis adopts the Fig. 5 coordinates and keeps the flow times for each ensemble distinct. [Original publication](https://arxiv.org/abs/2403.00754v2) · [Underlying CLS scale and mass tuning](https://arxiv.org/abs/1608.08900) · [Extraction](code/mass_scan.py) · [Static-system rows](data/mass-scan-levels.csv) · [Mass and threshold rows](data/mass-scan-ensembles.csv)

The energy denominator $2E_{Ql}$ is already removed in Fig. 4. Fig. 5 displays $\sqrt{t_0}(E_{Qs}-E_{Ql})$, so we multiply it by $2/\sqrt{t_0/a_{\rm lat}^2}$ to obtain the relative two-strange-meson threshold in the same units. A single chord uncertainty propagates the published vertical errors from distinct ensembles at fixed mass coordinates. The threshold uncertainty treats the plotted ordinate at fixed tabulated flow time and gives the latter's separate linearized contribution. It cannot be used with an independent-errors assumption to assess a difference between threshold and level on the same configurations. The authors report mass mistunings and neglect their effects in their analysis. A continuum or fixed-renormalized-trace extrapolation was outside that ensemble set. [Finite chords and interpolation](code/mass_response.py) · [Numerical results](results/mass-response.json)

The one-loop fermion polarization and its massive contribution to the ordinary static potential predate 2025. We use their standard Dirac spectral density and $T_F=1/2$ normalization. The new short-distance response follows by inserting the first-harmonic metric-field kinetic mixing and the two chiral overlaps on the two sides of that polarization. We checked the parameter integral, spectral representation, inverse quadratic form and finite-pole transform. The source and signs are specified in the manuscript. [Peter, 1997](https://arxiv.org/abs/hep-ph/9702245) · [Melles, 2000](https://arxiv.org/abs/hep-ph/0001295) · [Numerical checks](results/colour-loop.json)

The choices of geometry, adjoint block and light matter are theoretical inputs. Their contemporary companion-project provenance and dimensional benchmark are documented outside the historical bibliography. The programme registered the mode, scalar scan and subsequent loop check in two real commits. The published measurements predate either registration. [Editorial cross-reference](README.md#present-day-editorial-cross-reference) · [First-harmonic and mass-scan registration](https://github.com/arivero/qcdstring/commit/081ad4acdd71f42351ca35662afe4bf62c12d3b3) · [Short-distance follow-up registration](https://github.com/arivero/qcdstring/commit/a609c0dc8b69ac33218f99f556afc5481442c8df)
