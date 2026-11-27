# Author checks for QCDS-99/S1

The manuscript has **19,591 o200k_base tokens** under the programme convention (the complete Markdown). The **18-page A4 PDF** contains all 28 tagged equations, 7 tables and one two-panel figure. All equation numbers 1–28 were recovered from the PDF text (28 of 28).

- Published manuscript SHA-256 `4f56882a05f3d3ee676a08a45333355075fad140023ea338e0b23d4a3f1062b9`
- Reviewed versions: first round `19ad78905716ff23fa79e7cb743e9180326238b35cc9a12428a2446ba0245063` (15,856 tokens), second round `d7ffa52dbf8da42c2a14c8fef4e8fa1a4da58b498951219a081df54eb1478ef1` (19,235 tokens)
- Printout `results/tip-spectrum.json` SHA-256 `bdcb9a78620a4986328f60e92e4680b42f4ace2799a43d9dbbfcfc06a9125ae5`
- Numerical environment: Python 3.14.4, NumPy 2.3.5, SciPy 1.16.3, SymPy 1.14.0, Matplotlib 3.10.7; Pandoc 3.7.0.2 and XeTeX (TeX Live 2025). The solver command sets `OPENBLAS_NUM_THREADS=1`.

## Registration and order of work

P32 was committed to the ledger as `4557fb2` on 27 November 2026 before `code/tip_spectrum.py` was first run. The registration was written by Claude Fable 5.2, which also wrote the first version of the program. Claude Opus 5.5 extended the program (the identity for D$p$ solitons, the fermion charges, the string coupling at the tip, the test on the printed 1998 equation, the string-unit tables, and in the revision the selection-rule counts, the three-length estimator and the radial diagnostics), wrote the manuscript and the figure, and prepared both responses. The referee, GPT-6.2 Sol, is a different model; it asked for major revision in the first round and accepted the revised manuscript with minor corrections in the second, which were then made.

## What the program checks

- **Geometry, symbolically in both forms.** The proper-distance expansion at the tip in ten and eleven dimensions, $M_{\rm KK}$ in both, the cigar mass equal to $M_{\rm KK}$ in both (and for D$p$, $p=2,\dots,6$), $\sigma=2\lambda M_{\rm KK}^2/27\pi$, $R_{\rm tip}^2=\lambda\ell_s^2/3$, $1/g^2=\lambda/6\pi$ and $e^{\phi(U_0)}N/\lambda^{3/2}=\sqrt3/9\pi$.
- **Fermions, with explicit $32\times32$ matrices.** Clifford algebra; $K_\mu=(f/12)\Gamma_\mu\Gamma_{(4)}$ on a flat direction; $[K_{\hat7},K_{\hat8}]$ proportional to $\Gamma^{\hat7\hat8}$ with coefficient $-1/18$; $\Gamma^\alpha K_\alpha=(f/4)\Gamma_{(4)}$ with eigenvalues $\pm1/4$; $\kappa$-projector of rank 16 commuting with the mass operator; on-shell kernel of dimension 16, and 8 after $\kappa$-fixing; smallest singular value 0.0447 at 10 per cent off shell; cigar charges $\pm\tfrac12$ with four states per sign of mass and charge.
- **Casimir sums.** Massless limits $-0.99905$, $+0.99905$, $-0.9999976$ in units of $\pi/6L$, $\pi/6L$, $\pi/12L$ at $mL=10^{-3}$; the R−NS difference times $L/2\pi$ equal to 0.99968 at $M_{\rm KK}L=10^{-3}$; its ratio to the large-length form 1.0877, 1.0596, 1.0364 at $M_{\rm KK}L=8$, 12, 20.
- **Selection rule.** On the $\kappa$-fixed space the flat spin and the sphere chirality are locked at fixed cigar charge (product $-1$ at charge $+\tfrac12$). The space of $\mathrm{Spin}(2)\times\mathrm{Spin}(4)$-invariant couplings of a charge-one fermion pair has dimension 0; with one sphere quantum the space of ordered internal tensors has dimension 8. The unrestricted generators leave the charge-$+\tfrac12$ subspace invariant to 0e+00, and the membrane projector commutes with all rotation generators used.
- **Three-length estimator.** Four triplets above the saddle crossing; at $\lambda=80$, $L\sqrt\sigma=20,40,80$: $\widehat a_{\rm R}/\pi=-0.9947$, $\widehat a_{\rm NS}/\pi=-1.0053$; deep infrared at $\lambda=20$: $-0.3336$ in both sectors.
- **Radial problem.** The minimal operator gives $M^2=22.0966$, $55.5833$ (neutral), $42.6733$, $83.1305$ (charge one) and $78.8994$ (charge two) with $M_{\rm KK}^2=9$. The neutral level equals the programme's tensor benchmark $1.5669\,M_{\rm KK}$. The same code on the equation printed as (3.3) in the 1998 glueball paper gives mass ratios 1.4794 and 1.9301 against the published 1.4783 and 1.9317. Every integration that enters a root or sensitivity calculation is required to succeed; node counts are 0, 1, 0, 1, 0 for the rows of Table 4, and the largest joint end-point variation of $M^2$ is below $3\times10^{-5}$.

`code/check_article.py` compares all rows of Tables 1–6, nineteen quoted values, the symbolic and matrix results, the equation tags and the local links with the printout: "check_article: 59 checks passed".

## Scope of the checks

The checks verify the derivations of the article in their stated approximations: the classical background, the string at the tip, quadratic order in the transverse fields and one loop for the Casimir energies. They do not compute the radiative shifts or the three-body amplitude that decide the stability of the charge-one cigar level, the threshold constant $C$ of the sphere gap, or charged bulk sectors other than the transverse-traceless polarization. The sphere gap rests on the published exact $O(N)$ gap and on asymptotic freedom; its prefactor is uncertain by a factor of order one. The referee read the paper, the printout and the programs as text in both rounds and ran nothing. No human has reviewed the article. [Referee](REFEREE.md) · [Response](RESPONSE.md) · [Reproduction](README.md#reproduction)
