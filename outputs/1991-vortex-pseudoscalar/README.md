# QCDS-91/S1 · A trapped electric field on an Abelian Higgs vortex

November 1991, an extra paper in the qcdstring programme. A mode of the original gauge field carries the pseudoscalar pole allowed in the 1990 note. The canonical two-phonon matrix element follows from its overlap with the magnetic flux. At equal bulk masses an even mode produces a second pole at the same frequency. Equations (21) and (28) and the polarization table distinguish the two. [Manuscript](paper.md) · [PDF](paper.pdf)

## Reproduce the results

From this directory run the commands below. The radial program requires Python 3, NumPy, SciPy and Matplotlib. The second command requires Pandoc, XeLaTeX and the Latin Modern fonts.

~~~sh
python3 code/vortex.py
pandoc paper.md --from=markdown+tex_math_dollars --pdf-engine=xelatex -V papersize=a4 -V geometry:margin=25mm -V fontsize=11pt -V colorlinks=true -o paper.pdf
~~~

The program solves the backgrounds and the odd radial problem, compares boundary conditions and mesh sizes, tests the two projections of the electric source and differentiates the translation norm of the even mode. It writes the profile figure and the five runs including full-precision dimensionless observables, with the three longest runs first. [Radial program](code/vortex.py) · [Stored results](results/radial.json)

The period sources, checks, independent textual review and author response accompany the paper. [Sources](SOURCES.md) · [Checks](AUTHOR_CHECKS.md) · [Referee](REFEREE.md) · [Response](RESPONSE.md)
