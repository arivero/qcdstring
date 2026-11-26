# QCDS-95/S1 · What the vortex doublet predicts on a Seiberg–Witten electric string

November 1995, a corollary outside the biennial sequence. The fundamental electric Wilson line has unit Dirac pairing with the monopole. In the softly broken monopole vacuum this selects the string whose local trace spectrum was calculated in QCDS-92/1. The small adjoint mass fixes the local deformation and also limits the energy resolution at which that local result can be interpreted. [1995 article](paper.md) · [PDF](paper.pdf) · [1992 local theorem](../1992-scalar-doublet/paper.md) · [1994 working calculation](../1994-monopole-string/monopole-vacuum.md)

| Result | Novelty judgment |
|---|---|
| Monopole condensation and electric confinement | Established Seiberg–Witten physics. The source and scale conventions are fixed explicitly in §§2–4. [Original paper](https://arxiv.org/abs/hep-th/9407087) |
| Even doublet on the electric tube | A corollary of the 1992 local result in the leading dual action. Matching gives a tree separation $g^2\lvert\mu\rvert/2$. The microscopic limit also sends the separation below the critical translation width scale. [Matching and resolution](paper.md#10-how-well-can-the-even-corollary-be-resolved) |
| Spin-structure difference on the winding string (§11) | New in this programme as a microscopic realization of the massless limit of P21. The four Goldstinos give $\pi/(2L)$ to the R–NS difference of spin-matched, vacuum-subtracted energies, derived from the exact supersymmetry and checked by oscillator sums, conformal weights and the 1986 determinant. In the two-derivative dual action the transverse fermion operator is derived from the component Lagrangian as the Dirac operator of the bosonic deformation operator $D$ (checked symbolically), so at the BPS point the gapless content is two translations and two nonchiral Majoranas with gap $\nu_0m_\gamma$. An explicit bound keeps exactly four gapless fermions for $0<w\le0.388$, which gives the full R–NS difference. The individual coefficients $(0,-\pi/2)$ also need the bosonic count at $w>0$, shown only for an unquantified range. Not reviewed by an independent referee. [Section 11](paper.md#11-spin-structures-and-the-massless-fermions-of-the-unit-string) |
| Odd neutral and vector poles | A technical calculation in the specified local action. The relative squared-mass coefficient is about $-0.57746$. A matched topological term can redistribute the visible weight within the subthreshold cluster. The individual quantum pole masses and total widths require further input, and priority for the combined calculation is open. [Odd spectrum](paper.md#7-a-second-odd-state-and-its-constant-coupling-displacement) |

The [three-length spin-structure diagnostic](../../PREDICTIONS.md#a-finite-length-test-of-the-massless-p21-sector) distinguishes an additional neutral massless scalar from the minimal content without fitting the tension. Section 11 derives the bosonic and fermionic kernels at the BPS point and bounds the fermionic one along the deformation.

## Reproduction

From this directory use Python 3, NumPy, SciPy, Matplotlib, Pandoc and XeLaTeX.

~~~sh
OPENBLAS_NUM_THREADS=1 python3 code/odd_cluster.py > results/odd-cluster.json
python3 code/figure.py
OPENBLAS_NUM_THREADS=1 python3 code/spin_structure.py > /dev/null
python3 code/fermion_operator.py > /dev/null
python3 code/check_article.py
python3 code/build.py
~~~

The program imports the distributed 1992 radial basis and reads the stored 1994 tension and even-mass results for the consistency ratio in Eq. (9). Both sets of inputs are separately reproducible from their own source code. [New numerical data](results/odd-cluster.json) · [Sources](SOURCES.md) · [Referee](REFEREE.md) · [Response](RESPONSE.md) · [Author checks](AUTHOR_CHECKS.md)
