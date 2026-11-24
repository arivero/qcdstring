# QCDS-91/S1 · A trapped electric field on an Abelian Higgs vortex

November 1991, an extra paper in the qcdstring programme. The longitudinal electric field carries the pseudoscalar pole allowed in the 1990 note. The linear bound mode and the critical partner have published spectral precedents. The canonical two-phonon matrix element follows from its overlap with the magnetic flux. At equal bulk masses an even mode produces a second pole at the same frequency. Equations (21) and (28) and the polarization table distinguish the two. [Manuscript](paper.md) · [PDF](paper.pdf)

## Reproduce the results

From this directory run the commands below. The radial program requires Python 3, NumPy, SciPy and Matplotlib. The independent critical-disk check uses NumPy and SciPy. Building the PDF requires Pandoc, XeLaTeX and the Latin Modern fonts.

~~~sh
python3 code/vortex.py
python3 code/check_critical.py
pandoc paper.md --from=markdown+tex_math_dollars --pdf-engine=xelatex -V papersize=a4 -V geometry:margin=25mm -V fontsize=11pt -V colorlinks=true -o paper.pdf
~~~

The program solves the backgrounds and the odd radial problem, compares boundary conditions and mesh sizes, tests the two projections of the electric source and differentiates the translation norm of the even mode. It writes the profile figure and five runs, with the three longest runs first. On each critical profile the field `curvature_eq27` records the two terms of the unreduced journal integral, the signed coefficient and the plane norm including the exterior tail. [Radial program](code/vortex.py) · [Stored results](results/radial.json)

The disk check instead solves the first-order BPS background in logarithmic variables and uses a Dirichlet endpoint for the fluctuation. It prints mesh convergence for the squared frequency, the unit plane norm and the two ways to compute the curvature coefficient.

The issue-by-issue response identifies the prior spectrum, the angular-momentum overlap, the March and journal coefficients, and the scope of the numerical and AI checks. [Sources](SOURCES.md) · [Checks](AUTHOR_CHECKS.md) · [Referee](REFEREE.md) · [Response](RESPONSE.md)
