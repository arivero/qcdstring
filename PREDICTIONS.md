# Predictions ledger

Rules. A prediction is registered with a date and never edited. Its
status is updated below it. "Source" says whether the prediction follows
from a 1974 derivation or from memory. "Resolves" gives the year the
memory says the matter is settled, so that a reader can judge how much
the memory is doing. Numbers are in GeV or in units of sqrt(sigma).

Registered 6 November 1974 unless stated.

| ID | Prediction | Source | Test | Resolves | Status |
|---|---|---|---|---|---|
| P01 | A narrow (width < 0.1 MeV) vector state of a new heavy quark pair appears at 3.10 GeV on or about 11 November, followed by a second at 3.69 GeV. Its levels fit V(r) = -(4/3) alpha_s/r + sigma r with sigma = 1/(2 pi alpha') from the Regge slope, i.e. sigma ~ 0.18 GeV^2. | MEMORY | Charmonium spectroscopy; `ideas/009` | 1975 | open |
| P02 | The static potential of a confining gauge theory in d dimensions has the form sigma R - pi (d-2)/(24 R) + O(1/R^3). The coefficient is universal: -pi/12 in d = 4, -pi/24 in d = 3. | MEMORY, derivable | Lattice V(R); `ideas/001` | 1981 (theory), 2002 (lattice) | open |
| P03 | The excitation spectrum of a flux tube of length R follows E_n = sqrt(sigma^2 R^2 + 2 pi sigma (n - (d-2)/24)) up to and including O(1/R^5) in d = 4. | MEMORY | Lattice excited potentials; `ideas/012` | 2009-2013 | open |
| P04 | The closed flux tube in d = 4 carries one extra massive worldsheet excitation, a pseudoscalar, of mass about 1.85 sqrt(sigma), coupled to the transverse modes with a strength fixed by an anomaly (Q ~ 0.38). It shows up as an anomalously light 0^{--} level. | MEMORY | Lattice closed-tube spectra; `ideas/013` | 2010-2017 | open |
| P05 | The Pomeron intercept is 1.08 +/- 0.02 and its slope is 0.25 +/- 0.03 GeV^-2. Interpretation: the closed string's leading trajectory, with intercept pulled from 2 toward 1 by the curvature of the size coordinate. | MEMORY (number), 1974 (ISR trend) | ISR total cross-sections; `ideas/006` | 1992 | open |
| P06 | Meson and baryon leading trajectories share the slope alpha' = 0.9 +/- 0.1 GeV^-2. The baryon trajectories have intercepts offset from the meson ones by about 1/2, in the pattern of Miyazawa's supersymmetry. | 1974 | `numerics/regge_fit.py`, `ideas/016` | now | open |
| P07 | The string's Hagedorn temperature in d = 4 is T_H = sqrt(3 sigma/(2 pi)) = 0.69 sqrt(sigma) ~ 0.29 GeV. The deconfining temperature of the pure SU(3) gauge theory lies below it, at T_c ~ 0.64 sqrt(sigma) ~ 0.27 GeV, and the transition there is first order. With light quarks the crossover sits near 0.155 GeV, close to Hagedorn's 1965 number. | MEMORY | Lattice thermodynamics; `ideas/009` | 1985-2014 | open |
| P08 | Lightest glueballs, as closed strings, in units of sqrt(sigma): 0^{++} at 3.4-3.6, 2^{++} at 4.8-5.0, 0^{-+} at 5.2-5.5. With sqrt(sigma) = 0.44 GeV: about 1.6, 2.2 and 2.4 GeV. | MEMORY | Lattice; `ideas/010` | 1998-2021 | open |
| P09 | Exclusive fixed-angle amplitudes fall as s^{2-n} because the string lives in a warped size coordinate. The derivation is the test. | MEMORY | `ideas/007` | 2001 | open |
| P10 | At large N, meson widths scale as 1/N, the string tension and glueball masses approach limits with O(1/N^2) corrections, and the tensions of k-strings satisfy sigma_k/sigma_1 ~ sin(pi k/N)/sin(pi/N) to within a few percent. | MEMORY, 1974 ('t Hooft) for the first | Lattice at N = 2..8; `ideas/003`, `ideas/014` | 2001 | open |
| P11 | In the strong-coupling expansion of sigma(beta) there is a roughening singularity before the continuum regime; beyond it the Wilson surface fluctuates and the 1/R term in V(R) appears. | MEMORY | Series analysis, Monte Carlo; `ideas/004` | 1980 | open |
| P12 | In the theory with light quarks the flux tube breaks at R ~ 1.2-1.3 fm, where sigma R equals twice the heavy-light meson mass above threshold. | MEMORY | Lattice; `ideas/008` | 2005 | open |
| P13 | The U(1) lattice gauge theory in d = 4 has a confining phase at strong coupling and a Coulomb phase at weak coupling, separated by a transition near beta = 1.0. The SU(2) theory confines at all couplings and shows asymptotic scaling of sigma around beta = 2.2-2.4 on lattices of 6^4 to 10^4. | MEMORY | `numerics/`, Phase 2 | 1979-80 | open |
| P15 | The static three-quark potential at large separations is sigma times the length of the Steiner (Y-shaped) tree joining the quarks, with the same sigma as the quark-antiquark string. Registered 7 Nov 1974. | MEMORY, 1974 (Nambu's junction) | Lattice three-quark potential; `ideas/018` | 2001 | open |
| P16 | The exponential growth of the hadron level density has the same slope for mesons and for baryons. Registered 7 Nov 1974. | MEMORY (Kutasov-Seiberg theorem, read hadronically) | Separate Hagedorn fits to the meson and baryon tables; `ideas/022` | open in the memory | open |
| P17 | SU(N) gauge theory with one Dirac fermion in the two-index antisymmetric representation has glueball and meson masses that approach those of N=1 super Yang-Mills with O(1/N) corrections; at N = 3 this is one-flavour QCD. Registered 7 Nov 1974. | MEMORY | Lattice at N = 3, 4, 6; `ideas/022` | 2003 (theory) | open |
| P14 | The extrinsic-curvature (rigidity) term on the worldsheet is irrelevant at long distance and does not change P02 or P03. | MEMORY | `ideas/011` | 1986-2013 | open |

## Status log

* 1974-11-06: ledger opened with P01-P14.
* 1974-11-06: P06 first check (`numerics/regge_fit.py`, firm states only):
  pooled alpha' = 0.87 GeV^-2 with a scatter of 0.10 between trajectories;
  max/min slope ratio 1.27. The two strange trajectories (K*, phi) have the
  lowest slopes, 0.80-0.82, which is the direction expected from massive
  endpoints (008). N and Lambda slopes 0.98-1.01, rho and Delta both 0.89.
  Status of P06: supported for slope universality at the 15 percent level;
  the intercept-offset part is open. The pairing test shows the Delta
  tower pairing with L+1 mesons to within 80 MeV and the nucleon ground
  state pairing with nothing; N(1688) is degenerate with g(1680) at equal L.
* 1974-11-06: P01 calculation done (`numerics/charmonium.py`, kappa = 0.52,
  sigma from the Regge slope, m_c tuned to the 1S): predicted 1P centroid
  3.528, 2S 3.712, 1D 3.829, 3S 4.166 GeV. Memory values: 3.525, 3.686,
  3.770, 4.040. The 3S overshoot is expected from the open-charm threshold.
* 1974-11-07: P15-P17 registered with the long-march document.
