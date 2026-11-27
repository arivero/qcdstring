# QCDS-99/S1 · What does the string at the tip carry?

October 1999, odd-year supplement to QCDS-98/1. In the compactified D4 construction of 1998 the confining string sits at the tip of a cigar. The article derives its complete quadratic spectrum, fermions included, and follows the consequences for a long tube in two spin structures. The string clauses of the registered prediction P32 are reached at quadratic order. Its bulk clause is narrowed to the computed tower, and the lightest charge-one scalar across the coupled bulk sectors remains open. The route from this background to a pure four-dimensional polarized spectrum is narrowed. [Manuscript](paper.md) · [PDF](paper.pdf) · [Preregistration](https://github.com/arivero/qcdstring/commit/4557fb2)

| Result | Novelty judgment |
|---|---|
| Cigar doublet of mass $M_{\rm KK}$ and charge $\pm1$ | Known by the historical date: the January 1999 calculation in [5] (Greensite and Olesen) finds two massive bosons with mass parameter $4\pi^2T^2=M_{\rm KK}^2$. The identity for the whole family of D$p$ solitons, Eq. (10), is a reformulation. |
| Eight fermions of mass $M_{\rm KK}/2$ and charge $\pm\tfrac12$ from the four-form flux; the sum rule $\sum_Bm^2=\sum_Fm^2$ | Derived here at the counterfactual date. In the actual record the same mass relation appears for the D3-based three-dimensional model in November 1999 (Kinar, Schreiber, Sonnenschein, Weiss), and the full D4 spectrum with the sum rule in 2004 (Bigazzi, Cotrone, Martucci, Pando Zayas). No priority belongs to this programme. |
| Cigar doublet exactly at the two-fermion threshold, and the selection rule that forbids the direct two-fermion channel | The threshold equality is an elementary consequence of the sum rule. The selection rule (flat spin locked to sphere chirality at fixed charge) was pointed out by the referee and confirmed with explicit matrices; the three-body channel with a sphere quantum is allowed. Whether the charge-one level is stable depends on radiative shifts and is open. |
| $O(5)$ sigma model of the sphere coordinates, $1/g^2=\lambda/6\pi$, gap $\propto M_{\rm KK}(\lambda/9)^{1/3}e^{-\lambda/9}$, and the window of six light bosons | Derived here from standard ingredients (asymptotic freedom, the exact $O(N)$ gap). Conditional on an uncomputed threshold constant of order one and on the absence of a $\log\lambda$ in the matching. We know no publication that applies the gap to this string. Literature priority is unestablished. |
| Spin difference $(8M_{\rm KK}/\pi)\sum_{w\,{\rm odd}}K_1(wM_{\rm KK}L/2)/w$, the saddle condition $L>2\pi/M_{\rm KK}$, the three-length estimator and the realization of P21 | Derived here for free massive fields at quadratic order on the common $\tau$-cigar branch. The saddle comparison uses the published entropy law of near-extremal fivebranes. Significant inside the programme: it realizes the massive case of the 1986 diagnostic. |
| Bound $M>|n|M_{\rm KK}$ and the charged tensor glueball at $2.1775\,M_{\rm KK}$; no charged bulk emission in that tower | Derived here for the transverse-traceless polarization only; the bound was supplied by the referee. The neutral levels agree with the later tables of Brower, Mathur and Tan (2000). The registered clause about the lightest charge-one scalar needs the other coupled bulk sectors and remains open. |

All results are unreviewed by humans. The independent referee is a language model reading the paper as text. [Referee](REFEREE.md) · [Response](RESPONSE.md) · [Author checks](AUTHOR_CHECKS.md) · [Sources](SOURCES.md)

## Reproduction

From this directory use Python 3, NumPy, SciPy, SymPy, Matplotlib, Pandoc and XeLaTeX.

~~~sh
OPENBLAS_NUM_THREADS=1 python3 code/tip_spectrum.py > /dev/null   # writes results/tip-spectrum.json
python3 code/figure.py
python3 code/check_article.py
python3 code/build.py
~~~

The program checks the geometry symbolically in the ten- and eleven-dimensional forms, builds the membrane mass operator from explicit $32\times32$ gamma matrices, counts the invariant couplings behind the selection rule, evaluates the Casimir sums, the three-length estimator and the $O(5)$ gap, and solves the radial equation of the bulk tensor mode with and without Kaluza–Klein charge, with node counts and end-point sensitivity. The same shooting code is tested on the radial equation printed in the 1998 glueball paper. [Stored printout](results/tip-spectrum.json) · [Figure](figures/tip-string.png)
