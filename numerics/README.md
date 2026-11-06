# numerics

Small programs. Each prints what it computes and the number from the
memory it should be compared with. Pure Python unless stated.

| Script | What it does | Idea |
|---|---|---|
| `regge_fit.py` | Chew-Frautschi fits to `data/regge_1974.tsv`; pooled slope; sigma, T_H, Luscher term; meson-baryon pairing table | 009, 016 |
| `arvis_spectrum.py [d]` | Nambu-Goto fixed-end and closed-string spectra, large-R expansion, Hagedorn temperature, the -1/12 mode sum | 001, 005, 012 |
| `charmonium.py` | Heavy-quark levels in -kappa/r + sigma r with sigma from the Regge slope; m_c tuned to the 1S; the rest predicted | 009 |
| `z2_lattice.py` | Heat-bath Monte Carlo of 3d Z2 gauge theory (numpy); Wilson loops, Creutz ratios, strong-coupling and Ising-duality checks | 004 |
| `thooft2d.py` | 't Hooft's 2d meson equation by Galerkin (numpy); asymptotic slope pi^2 | 015 |

Planned, in rough order: strong-coupling series for sigma(beta) with ratio
tests (004); U(1) and SU(2) in four dimensions (004, 014); the rotating
string with massive endpoints (008); the warped-string fixed-angle
integral (007); Polyakov-loop correlators at finite temperature (009).
