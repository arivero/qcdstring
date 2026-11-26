# Primary sources and the provenance of the nine measurements

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

## Reproducing the Fig. 4 extraction

The primary archive is [arXiv:2403.00754v2, source download](https://arxiv.org/src/2403.00754v2). From the article directory the following commands obtain just the two needed members in a temporary directory, regenerate the numeric CSV and rerun the predictions. Python dependencies are NumPy, Matplotlib and PyMuPDF.

~~~sh
source_dir=$(mktemp -d)
curl -fL https://arxiv.org/src/2403.00754v2 -o "$source_dir/source.tar.gz"
tar -xzf "$source_dir/source.tar.gz" -C "$source_dir" VRensembles.pdf VRensembles_fig.tex
sha256sum "$source_dir/source.tar.gz" "$source_dir/VRensembles.pdf" "$source_dir/VRensembles_fig.tex"
python3 code/digitize.py "$source_dir/VRensembles.pdf"
MPLBACKEND=Agg OPENBLAS_NUM_THREADS=1 python3 code/check.py
~~~

| Member | SHA-256 |
|---|---|
| Version 2 source archive | 2abca11623f10491e763d0a774100c9102f2d6fcf4c8d7617235f03968fe64b5 |
| VRensembles.pdf | abeae9c810a8b0b00250328c87951fbdb4739de0cf400d9a60f89c88c3981783 |
| VRensembles_fig.tex | 2e59bd72ae8a6fa2234dfc1d9d08cf4c2ca74a241d1ae356733734fb338c3096 |

The archive also contains model.tex, method.tex and massdep.tex. The Fig. 4 caption in model.tex identifies the markers as estimates of levels from the generalized eigenvalue analysis and the bands as the seven-parameter fits. The middle-panel labels in VRensembles_fig.tex identify N200 and the integer separations. Its vertical axis is the static energy minus twice the static-light energy in lattice units. The graphic has size 481 by 198 PDF points. The black bottom ticks for 17, 19 and 21 have abscissae 204.398, 249.648 and 294.898 points. The same tick-to-energy calibration applies in each panel. At each of those abscissae the code identifies three filled point markers, matches them to the three vertical error strokes and ignores the polygons for the model bands. Printed coordinates at about 0.05 point resolution make rounding on the order of 0.00005 in energy visible. These checks preserve the provenance of a vector digitization from an existing publication. Only the markers, axes and marginal errors are available through this route. [Digitized data](data/n200.csv) · [Extraction code](code/digitize.py) · [Results](results/checks.json)
