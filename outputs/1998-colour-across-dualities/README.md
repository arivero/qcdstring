# QCDS-98/1 · Where does the color go when a string is lifted?

December 1998, regular biennial article. In the IIA lift the bulk winding string and the bound membrane carry the same relative center charge. Free endpoints give a calculable departure from the equal-circle chord and determine the inertia of an internal rotation. The article follows the supersymmetry of the four-dimensional vacuum and gives examples of which sources and boundary processes travel with a string under IIB, circle and heterotic dualities. [Manuscript](paper.md) · [PDF](paper.pdf)

P27 concerns a classical M2 in a specified fixed-fivebrane probe and a conditional angular level at finite length. The core fugacity, a fully dynamical fivebrane spectrum and the continuation to ordinary pure Yang–Mills remain open. [Preregistration](https://github.com/arivero/qcdstring/commit/00f602f) · [Source record](SOURCES.md)

## Reproduction

From this directory use Python 3, NumPy, SciPy, Matplotlib, Pandoc and XeLaTeX. The source, inputs and result of the geometric benchmark are in this directory.

~~~sh
OPENBLAS_NUM_THREADS=1 python code/membrane.py > results/membrane.json
python code/figure.py
python code/check_article.py
python code/build.py
~~~

The numerical checks move both endpoints, measure the area of a tilted strip and carry the screening covector through three IIB charge transformations. They share the fixed probe and curve assumptions of the analytic calculation. [Stored printout](results/membrane.json) · [Figure](figures/charge-and-tension.png)

[Independent referee](REFEREE.md) · [Author response](RESPONSE.md) · [Author checks](AUTHOR_CHECKS.md)
