# Predictions ledger

Rules. A remembered number is a prediction, never an input and never evidence; an entry counts as supported only when reproduced inside the programme (rule adopted from the second line). A prediction is registered with a date and never edited. Its
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
| P18 | The QCD flux tube carries no massless worldsheet fermions. Its 1/R coefficient is -pi/12; two massless NS Majoranas would give -pi/8 and two R Majoranas 0. Registered 8 Nov 1974 jointly with the second line. | 1974 (free-field Casimir arithmetic), MEMORY (lattice) | Lattice V(R); `ideas/001`, second line T09/T14 | 2002 | open |
| P14 | The extrinsic-curvature (rigidity) term on the worldsheet is irrelevant at long distance and does not change P02 or P03. | MEMORY | `ideas/011` | 1986-2013 | open |
| P19 | The lowest D-wave level of charmonium lies at 3.78-3.81 GeV, 50-75 MeV above the open-charm threshold, in the potential of the 1976 paper (no coupled-channel shift, no error bar). Registered November 1976. Both lines remember the outcome, so this entry carries no weight as a test. | 1976 calculation | e+e- scans above 3.73 GeV | 1977 | open |
| P20 | Bottomonium in the joint charmonium-bottomonium potential of the 1978 paper (kappa = 0.515, sigma = 0.168 GeV^2): 3S at 10.35, 1P centre 9.93, 1D 10.17, 2P 10.27, 4S 10.62 GeV; open-bottom threshold 10.57-10.72 GeV, so whether the 4S lies above it is undetermined. Registered November 1978. Both lines remember the outcome; no weight. | 1978 calculation | e+e- scans, radiative transitions | 1980-82 | open |

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
* 1974-11-08: P18 registered with the second line. Second-line benchmark reproduced here: D4 tensor m/M_KK = 1.5669021, next levels 2.485, 3.374, 4.252 (`numerics/d4_tensor.py`).
* 1976-11 (paper QCDS-76/1, `outputs/1976-flux-tube-casimir/`, tag `y1976`):
  * P02, d = 3: in the Z2 theory at beta = 0.70 and 0.73 (two-level
    Polyakov-line correlators, correlated fits) a 1/R term with the Casimir
    sign is required; b = 0 fails at both couplings over every range. Fitted
    alone, b = 0.070(1), 0.085(5), 0.103(17) from R = 2, 3, 4 at beta = 0.73;
    pi/24 is acceptable from R sqrt(sigma) ~ 0.9. pi/24 plus an endpoint term
    d/R^2 fits all separations, with d sqrt(sigma) ~ 0.010 at both couplings.
    Sign supported; magnitude not separated from an endpoint term. Open.
  * P11: the strong-coupling series to O(u^4) holds within 0.1% at beta <= 0.30
    and 1% at 0.40, then departs smoothly; the roughening point is not
    located. Open.
  * P13: U(1) part: the area law ends near beta = 1.0 with a jump of the
    plaquette; hot and cold starts at beta = 1.00 agree, so the order is open.
    SU(2) part open.
  * P01: the charmonium tension is 0.78-0.86 of the Regge tension, the range
    set by the spin-spin term of the same potential. Supported at the 15-20%
    level, no tighter.
  * P19 registered (outcome remembered; no weight).
* 1978-11 (paper QCDS-78/1, `outputs/1978-su2-scaling/`, tag `y1978`):
  * P13, SU(2) part: no hysteresis on 8^4 for 1.5 <= beta <= 3.0; the
    plaquette fluctuations peak at beta = 2.1-2.2; the tension is nonzero up to
    beta = 2.6. The confinement half is supported. Scaling half:
    sqrt(sigma)/Lambda_L falls from 66.6 at beta = 2.2 to 50-58 at 2.4-2.6,
    constant within the spread of four analysis choices; the range cannot
    tell two-loop from one-loop scaling, and the ledger's window 2.2-2.4 is too
    low. Open.
  * P02, d = 4: the 1/R coefficient of the SU(2) potential at beta = 2.4-2.6
    is 0.24-0.33, depending on coupling and time separation; pi/12 is
    acceptable at 2.5 only. The Casimir share is open.
  * P01: a joint potential for charmonium and bottomonium has
    sigma = 0.168 GeV^2, 0.91 of the Regge tension, and places the chi_c
    centre within 12 MeV of the 1976 data. Supported at the 10% level.
  * P19: the psi(3772) (1977) agrees with the 1976 record; no weight.
  * P20 registered (outcome remembered; no weight).

