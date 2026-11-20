# QCDS-92/1 · Two scalar poles from a single vortex shape resonance

November 1992, regular biennial article. A relaxed neutral field mixes with the charged shape vibration of a critical Abelian vortex. Their masses split by $w m_\gamma+O(w^2m_\gamma)$, and each takes half of the original two-phonon trace residue as $w\downarrow0$. The Seiberg–Witten electric-string interpretation belongs to 1994. [Manuscript](paper.md) · [PDF](paper.pdf) · [Independent referee](REFEREE.md) · [Response](RESPONSE.md)

| Result | Novelty judgment |
|---|---|
| Critical vortex, trapped longitudinal mode and the charged critical partner | Established ingredients. The article uses the earlier critical equality of polarized strengths to normalize its measurement. [Period sources and later comparisons](paper.md#retrospective-comparison-and-scope-of-priority) |
| Localized even poles with slopes $\pm1/2$ and half the original trace residue each | Candidate research result for the stated local action. Static relaxation and a radial virial identity give the coefficient for every fixed positive circular winding covered by the theorem. The numerical source measurement tests the share, and neutral detuning changes it as predicted. Priority remains open. [Mass slopes](paper.md#6-the-bound-state-mass-slopes) · [Physical source](paper.md#7-the-physical-trace-source) |

## Reproduce the paper

From this directory, with Python 3, NumPy, SciPy, Matplotlib, Pandoc and XeLaTeX, run

~~~sh
OPENBLAS_NUM_THREADS=1 python3 code/trace_spectrum.py > results/trace-spectrum.json
python3 code/figures.py
python3 code/check_article.py
python3 code/build.py
~~~

The solver includes the reflected deformation, radial mesh and outer-radius comparisons, fixed and joint neutral detuning, and windings two and three. [Numerical printout](results/trace-spectrum.json) · [Checks](AUTHOR_CHECKS.md)
