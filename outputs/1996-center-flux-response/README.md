# QCDS-96/1 · When do two units of electric flux bind?

December 1996, regular biennial paper. An independently normalized quartic perturbation changes the cost of electric flux in a softly broken supersymmetric four-color gauge theory. The charge-two sector can carry its flux on a middle vortex or on two unit strings. Their leading costs cross while every monopole condensate is still nonzero. [Manuscript](paper.md) · [PDF](paper.pdf)

The analytic result is a prediction for the long-string energy in the fixed-ray weak-deformation limit. Direct contour integration checks the chiral derivatives. A charge-graph search checks the minimization. Both checks use the same microscopic curve, operator and charge assumptions as the derivation. A four-dimensional measurement and a membrane realization with the appropriate boundary conditions remain open. The flat freely wrapped membrane without a charge sink fails both the center-charge test and the binding test at quadratic deformation. [Registered P26](../../PREDICTIONS.md) · [Source record](SOURCES.md)

## Reproduction

From this directory use Python 3, NumPy and Matplotlib. The PDF uses Pandoc and XeLaTeX. The full manuscript is counted with tiktoken and its o200k_base encoding.

~~~sh
OPENBLAS_NUM_THREADS=1 python code/flux_response.py > results/flux-response.json
python code/figure.py
python code/build.py
~~~

The JSON contains the complex-period error norms, variations of step and contour, the color weights and the scan of elementary and screened costs. All tensions in the graph are calculated from contour gradients for the quartic scan. The separate quadratic rank examples use analytic elementary weights. [Numerical printout](results/flux-response.json) · [Figure](figures/flux-binding.png)

[Independent referee](REFEREE.md) · [Author response](RESPONSE.md) · [Author checks](AUTHOR_CHECKS.md)
