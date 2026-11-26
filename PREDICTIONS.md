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
| P21 | Conditional model diagnostic: if the same fixed-mass nonchiral Dirac field and common local matching terms describe periodic and antiperiodic closed-tube sectors, their vacuum-energy difference is (4m/pi) sum over positive odd w of K1(wmL)/w, with large-L decay sqrt(8m/(pi L)) exp(-mL). A microscopic realization of both sectors is required. Registered November 1986. | 1986 derivation, QCDS-86/1 Section 5 | Identify physical sectors and test the length dependence; no QCD measurement yet | open | derived in the fixed-mass model; massless limit realized on the supersymmetric electric string (QCDS-95/S1 §11: fermion kernel derived, R-NS coefficient pi/(2L) and R, NS coefficients (0, -pi/2) established for 0 < w <= 0.388 in the dual action); massive diagnostic and QCD application open |
| P22 | Conditional model result: a homogeneous large-N_f Gross-Neveu sector on a flat tube has NS saddle restoration at m_infinity L = pi exp(-EulerGamma), a larger R mass than its infinite-line mass, and a condensation-energy contribution in addition to the determinant. This is not a finite-N_f or deconfinement prediction. Registered November 1986. | 1986 rederivation of a known large-flavour mechanism, QCDS-86/1 Section 6 | Compare the gap equation with the independently integrated potential; microscopic matching remains required | open | derived and author-checked within the stated saddle approximation |
| P23 | Conditional normal-field model: a canonical displacement y and a massive normal field phi with derivative mixing -g d(phi).d(y), m > 0 and abs(g) < 1 have a massive pole M = m/sqrt(1-g^2) with positive displacement residue g^2/(1-g^2). Integrating out phi induces a negative local p^4 coefficient, although the exact quadratic theory is stable. Each periodic massive mode contributes -(M/pi) sum K1(wML)/w after tension subtraction. Registered November 1988, before the numerical checks. | 1988 derivation, QCDS-88/1 Sections 3-5 | Compare normal modes, propagator residues and finite-size determinant; QCD matching required | open | registered conditional model statement |
| P24 | Conditional scalar-curvature model, d = 3: for a canonical scalar of mass m coupled by q a R to the induced intrinsic curvature, tree exchange gives an additional low-energy phase b s^3, b = q^2/(4 sigma^2 m^2). Its leading coupling-dependent periodic vacuum shift is -32 pi^6 b/(225 L^7), at first order in the matched operator. The scalar determinant and independent matching coefficients are not included in this difference. Registered November 1988, before the numerical checks. | 1988 derivation, QCDS-88/1 Sections 7-8 | Compare the exchange amplitude and directly regulated vacuum contraction; no QCD mass or coupling input | open | registered conditional model statement |
| P25 | Conditional on the specified local vortex action, the two localized even masses shift by ± half the canonically scaled soft mass at fixed photon mass, and each takes half the critical trace residue in the small-breaking limit; the odd vector has zero linear shift. | QCDS-92/1, analytic result | Direct trace-source spectra, neutral detuning and fixed winding | 1992 | derived and checked in the local model |
| P26 | On the real maximally singular branch of pure $SU(4)$ with $W=\mu u_2+\nu u_4$, $u_p=\mathrm{Tr}\,\Phi^p/p$, set $t=\nu\Lambda^2/\mu$ in the monic Chebyshev curve convention. At fixed $t$ on $[-1/6,1/8]$, in the small-deformation limit, the lowest center-two tension in units of the center-one tension is $\min\{2,\sqrt2(1+2t)/(1+4t)\}$. Its logarithmic slope at the quadratic deformation is $-2$. The change of minimizing channel occurs at $t_*=(\sqrt2-2)/(8-2\sqrt2)$. | QCDS-96/1, registered December 1996 (fictional), 26 November 2026 (actual), before the period-contour and screening checks | Vary the independent quartic source with the curve scale fixed, measure long center-one and center-two flux energies in the same vacuum, then take the weak-deformation limit. Compare the screened minimum with the elementary period derivative. | open | analytic prediction for a deformed supersymmetric theory; physical test outstanding |
| P27 | For the classical flat-metric MQCD probe with a fixed pure fivebrane at four colors, let $a=\sqrt{\lvert\zeta\rvert}$, $R=R_{11}$ and $\eta=2a^2/(4R)^2<1$. With free membrane endpoints the center-two to center-one ratio is $\sqrt{2}\,[1+\eta/4+O(\eta^2)]$. On the oriented unit chord the $2\pi$ rotation of $v$ has stiffness $K=\sigma_1[(4R)^2+2a^2(\cos^2(\delta/2)+\sin^2(\delta/2)/3)]$, with $\delta+\eta\sin\delta=\pi/2$. A free infrared orbit with these matched data has a unit angular-charge gap $1/(2KL)$ at leading order. | QCDS-98/1, December 1998 (historical), registered 26 November 2026 before numerical minimization or moving-sheet checks | Vary both endpoints on the lifted fivebrane, cross-check tensions against the equal-angle chord and the orbit norm against the induced area of a moving strip. Test the infrared assumptions separately. | open | prediction for the classical fixed-fivebrane probe and conditional finite-length level; microscopic QCD interpretation open |

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
* 1980-11 (paper QCDS-80/1, `outputs/1980-excited-flux-tube/`, tag `y1980`):
  * P03, d = 3, n = 1: in the Z2 theory at beta = 0.73 the first excitation
    lies 4 to 17 standard errors below the free-phonon spacing pi/R for
    R sqrt(sigma) = 0.86-1.3, and above the square root by a factor that
    falls from 1.30 (R sqrt(sigma) = 0.86) to 1.10 (1.94); it agrees with the
    square root within errors from R sqrt(sigma) ~ 1.7. Levels n >= 2 are not
    resolved. Partly supported (long strings, n = 1, d = 3).
  * P02, d = 3: the ground state measured again to R = 9 by an independent
    method; fitted together with the 1976 data, a single 1/R coefficient
    (0.089(4) from R = 3, 0.107(12) from R = 4) and pi/24 with an endpoint term
    (d sqrt(sigma) = 0.0107(9) and 0.0084(12) at beta = 0.73 and 0.70) fit
    equally well. Open.
  * P11: the dual Ising interface roughens at K_R = 0.405 +- 0.008, gauge
    coupling beta_R = 0.479 +- 0.010 (crossing of the 1/pi^2 criterion,
    calibrated on the BCSOS model); the Casimir term is seen only above it. The
    statement about a singularity of the strong-coupling series is untested.
    Partly supported.
  * P20: CESR finds a narrow third and a broad fourth upsilon level about 0.9
    and 1.1 GeV above the first; the 1978 records gave 0.89 and 1.16. No weight.
  * P01: the eta_c candidate at 2.98 GeV lies 70 MeV above the singlet implied
    by the first-order spin-spin term of the 1976 potential (a).

* 1982-11 (paper QCDS-82/1, `outputs/1982-hagedorn-deconfinement/`, tag `y1982`):
  * P07, string side: the wound closed string has E_0(L)^2 = sigma^2 L^2 -
    pi (d-2) sigma/3 by the 1973 method, and the level density gives the same
    T_H = sqrt(3 sigma/(pi (d-2))) (checked on exact degeneracies).
  * P07, gauge side, d = 3: in the Z2 theory T_c/sqrt(sigma) = 1.105(16),
    1.152(26), 1.175(35) on N_t = 2, 3, 4 time slices (1.19(3) linearly in
    1/N_t^2), 13 to 22% ABOVE T_H = 0.977 sqrt(sigma). The tube energy vanishes
    linearly at T_c: effective exponent 1.00 +- 0.07 over fit choices, from
    points with a correlation length of at most 2.9 tube lengths; the class
    (two-dimensional Ising) rests on the cumulants. A square-root approach is
    excluded. The expectation "T_c at or below T_H" (idea 009, item 4, and the
    reasoning behind P07) is refuted for this theory: the square root does not
    hold up to its endpoint.
  * P07, gauge side, d = 4: in SU(2) T_c/T_H lies between 0.87 and 0.98 on
    N_t = 2, 3, 4, the range coming from the estimator of the zero-temperature
    tension; no trend with N_t is established and the continuum side is
    undecided. P07 itself speaks of SU(3) and a first-order transition:
    untested. Open.
  * P02 and P03, closed tube, d = 3: a term 1/L with the same coefficient
    0.58(3) at two lattice spacings (pi/6 = 0.52). Number of massless modes:
    c = 0.97(4)(10) and 1.04(6)(10) IF the L^-3 term is the square root's;
    0.99(12) and 1.01(10) with that term free and the shortest tubes kept,
    0.6(3) without them. c = 2 excluded; c = 0 excluded by the shorter tubes
    and the comparison of couplings. On lattices with L >= 6 the square root
    holds within 3% for L sqrt(sigma) >= 1.5; extrapolated to the continuum
    the tube is heavier by 3 to 6% at 1.35. It exists beyond the endpoint
    1.023. Supported for the ground state of the closed tube in d = 3, with
    the L^-3 term as the stated open point (closed in 1984).
  * P02, open tube, d = 3: with the tension fixed by the closed tube
    (0.04566(25) at beta = 0.73, total error) the 1/R coefficient fitted alone
    is 0.116(5) from R = 4, 2.9 standard errors below pi/24; pi/24 with an
    endpoint term fits equally. Open.
  * P01, P20: an eta_c' candidate at 3.592 GeV lies 28 MeV above the singlet
    implied by the 1976 potential; the chi_b(2P) states are seen through
    photons of about 0.1 GeV (record: 0.082). No weight.
* 1984-11 (paper QCDS-84/1, `outputs/1984-critical-dimension/`, tag `y1984`;
  theory, with refits of stored data):
  * P14: by Gauss's equation a Lorentz-invariant stiffness term is a total
    derivative plus terms that vanish with the equations of motion; it changes
    no level. Supported by derivation. (The 1976 paper had given a stiffness
    as an example of an R^-3 correction; that was the bending energy of a
    rod.) The first free bulk coefficients are quartic in the curvature and
    enter at sigma^-3 L^-7.
  * P02 and P03, the L^-3 term: the quartic term of the area action is
    2 sigma (d+X.d+X)(d-X.d-X) and shifts every closed-string level by
    -2 E+ E-/(sigma L). Derived; it is the L^-3 term of the square root, with
    no free parameter. This closes the open point of the 1982 entry.
  * P02, open tube, d = 3: a rotation-invariant source forbids the R^-2 end
    term; the first allowed, b_2 (d_t d_x X)^2, gives e/R^4 in the ground state
    and +240 k^3 e/R^4 per phonon, where d/R^2 would give -24 k d/R^2. Derived.
    The 1976 and 1980 data CANNOT apply the test: with one baseline for both
    levels they are described by the square root with e/R^4 alone and equally
    by the free string with d/R^2 alone (both from R sqrt(sigma) = 1.5), and
    e sigma^(3/2) runs from 0.002 to 0.010 with the baseline. Open. Decisive
    measurement: the first gap to 1% at R sqrt(sigma) = 2.5.
  * P03: the area action gives phonons the phase exp(i s/4 sigma); free phonons
    with that phase have the square-root spectra (closed and open) if the same
    rule is applied to the zero-point motion and to standing waves. The rule
    is derived at first order and assumed beyond.
    Amendment recorded here, since entries are never edited: PROPOSED, that
    the quantum correction for a long string is Polyakov's anomaly on the
    induced metric (the central term then cancels in every dimension; derived
    in Appendix B). It adds the four-phonon vertex
    (26-d)[d_a(dX.dX)]^2/384 pi, which is a total derivative for d = 3,
    absent for d = 26, and in d = 4 splits the level N = Nbar = 1 of a closed
    tube by -/+ (26-d)(4 pi^3/3)/(sigma^2 L^5) at first order (scalar and
    pseudoscalar down, spin 2 up). On that proposal P03 as registered ("up to
    and including O(1/R^5) in d = 4") can hold for the closed-string ground
    state and one-way states only. Not yet a measurement. The level of the
    area action at order L^-5 is not computed.
  * P18: the closed tube of the 3d Z2 theory carries c = 0.99(3)(9) massless
    modes and no further scalar lighter than 1.2 sqrt(sigma) (95%, one-sided;
    1.9 with the shortest tubes as measured). Supported in d = 3; d = 4 open.
  * P20: the chi_b(1P) centre is seen about 0.44 GeV above the Upsilon (record
    0.47); B mesons at 5.27 GeV put the 4S some 30 MeV above threshold (record:
    undetermined, level 40 MeV high). No weight.

* 1986-11 (paper QCDS-86/1, `outputs/1986-fermionic-flux-tube/`, tag `y1986`):
  * Review of the first five papers; no earlier raw data reanalysed and no new
    gauge simulation. Independent referee explicitly waived by the user;
    published with author checks and that limitation recorded.
  * P18: the earlier d = 3 Z2 mode count is a sector-dependent effective
    Casimir coefficient. A free periodic scalar and equal-mass periodic
    Majorana cancel in their vacuum energy, so the count is not an
    unrestricted exclusion of all additional massless fields. The 1984 bound
    remains a bound on its specified additional free scalar. d = 4 remains
    open; no new fermion mass bound is claimed.
  * P21-P22 registered as conditional model statements, not empirical
    predictions already supported in QCD. The determinants, saddle and
    critical-length expression are derived and checked in the paper.
  * P03: the direct area-action L^-5 calculation and the beyond-first-order
    rules of 1984 Section 4.2 remain unfinished. Expanding a square root does
    not close either task.
  * P14: equation-of-motion redundancy is a statement in a perturbative
    effective expansion, with induced operators and boundaries transformed.
    It is not an equivalence to every nonperturbatively treated rigid-string
    model at arbitrary energy. The thickness/threshold question is carried
    to 1988.
  * P07 and P16: no new deconfinement or meson/baryon Hagedorn equality is
    inferred from an infrared mode count. P17 is not tested.
  * New idea 027: dimensional suppression motivated by the special
    weak-coupling ultraviolet status of four-dimensional Yang-Mills.
    Derived matching conditions are conditional; no compactification theorem,
    radius stabilization, or pure four-dimensional spectrum is obtained.
  * The enhanced Section 8.4 gives a compact-coordinate countertest: for the
    minimal kinetic matching kappa = sigma r^2, a weak cosine is relevant
    only for kappa > 1/(8 pi). This restricted model cannot combine that weak
    pinning with a parametrically large M_KK/sqrt(sigma). Strong pinning or
    other background/kinetic matching is not excluded. No physical radius
    bound is registered.

* 1988-11 (paper QCDS-88/1, `outputs/1988-thickness-curvature/`, tag `y1988`):
  * P23-P24 registered before numerical checking and derived in the specified
    effective models; 91 author checks pass. The independent read-only referee
    recommends acceptance after four clarifications, all addressed in the
    revised paper and response; no coefficient changed.
    Neither entry is empirical evidence for a QCD mass or coupling.
  * P14: a positive quadratic normal-field model generates a negative local
    p^4 coefficient. The unstable pole of its first truncation lies outside
    the derivative expansion. The full determinant retains the positive
    massive mode. A positive exact p^4 kernel supplies the converse warning:
    its vacuum determinant can imitate an extra boson despite a negative
    spectral residue in the displacement correlator.
  * P24: in d = 3, scalar-curvature exchange gives a phase b s^3 and the
    directly calculated leading vacuum shift -32 pi^6 b/(225 L^7).
    This is the q-dependent contribution at tree matching and first-order
    insertion; independent coefficients and the scalar determinant remain
    separate. No total QCD L^-7 coefficient is predicted.
  * P03: the direct area-action L^-5 result and the 1984 quantization rules
    beyond first order remain unfinished. The new L^-7 calculation does not
    replace them.
  * P04-P05: no pseudoscalar identification or rotating-string intercept is
    obtained. The normal vector and intrinsic-curvature scalar have different
    quantum numbers from the proposed four-dimensional pseudoscalar.
  * No new simulation or fit; earlier gauge-theory conclusions retain their
    original dimensional, boundary and systematic limitations.

* 1990 (P04, AI review only). A single normal-bundle pseudoscalar has zero direct-channel
  pole residue in the trace and both symmetric-traceless two-phonon states.
  The normalized antisymmetric channel has the direct pole. Crossed exchange
  still contributes finite terms to the other channels. P04 remains open pending
  gauge-theory matching for the state, its mass and its coupling.
  [Polarization amplitudes](outputs/1990-pseudoscalar-curvature/amplitudes.md)

* 1991 (P04, Abelian field-theory test, AI review only). The positive unit magnetic vortex
  binds a longitudinal electric mode with the two odd parities. Its flux
  overlap gives a strictly positive antisymmetric pole strength at tree
  level. At equal bulk masses $m_*/m_V=0.881744$ and
  $e|Q_{\rm pole}|=1.20101$. An even shape mode at the same mass has
  equal strength in the trace channel. Its presence is consistent with the
  zero trace residue of the odd particle. The critical product
  $\lvert Q_{\rm pole}\rvert m_*/\sqrt\sigma=0.59747$ is about 13% below
  the registered $0.37\times1.85\simeq0.68$. P04 remains open for the
  pure Yang–Mills colour-electric tube, including its proposed mass and coupling.
  [Derivation and polarization table](outputs/1991-vortex-pseudoscalar/paper.md#polarization-table)

* 1992 (P25). The circular vortex calculation gives the two mass slopes and trace shares. Independent radial elements test both eigenfunctions and residues, and a lifted neutral level changes the allocation. The result is restricted to the stated classical action. [QCDS-92/1](outputs/1992-scalar-doublet/paper.md) · [Referee](outputs/1992-scalar-doublet/REFEREE.md)

* 1994 working calculation (P04, weakly broken supersymmetric gauge theory).
  A fundamental electric probe carries one dual vortex period. In the leading
  monopole action its odd localized mode lies below the lightest bulk particle
  for sufficiently small breaking and couples to the antisymmetric two-phonon
  channel. The limiting pole product is 0.597469. In the local dual action the
  two trace-channel masses split by $w m_\gamma+O(w^2m_\gamma)$ while the odd
  mass changes quadratically. P04 remains open for pure
  Yang–Mills. [Electric-string pole](outputs/1994-monopole-string/pseudoscalar.md)

* 1995 (odd-year corollary, P04 and P25). A fundamental Wilson source selects
  the unit electric string in the weak monopole vacuum. The 1992 doublet
  has leading local mass difference $g^2|\mu|/2$. The gauge-theory trajectory
  sends that separation below the critical partial-width scale. A neutral
  odd state and the longitudinal vector can share the subthreshold weight.
  The quoted partition in the projected kinetic model uses one specified
  interaction. P04 remains open in pure Yang–Mills. [QCDS-95/S1](outputs/1995-electric-string-corollary/paper.md)

* 1995 corollary, §11 added 26 November 2026 (P21). On the unit electric
  string at fixed nonzero adjoint mass, with all microscopic fermions
  periodic or antiperiodic around a spatial circle and each energy
  subtracted from the zero-flux vacuum of the same spin structure, the four
  Goldstinos give $\pi/(2L)$ to the R–NS difference. At the BPS point the
  gapless bosons are exactly the two translations and the transverse gap is
  $\nu_0 m_\gamma$, $\nu_0=0.881744$. Revised the same day: the transverse
  fermion operator, derived from the component Lagrangian, is the Dirac
  operator of the same deformation operator in two sectors of opposite
  chirality, so the Goldstinos exhaust the gapless fermions at the BPS point.
  An explicit bound on the soft perturbation keeps that rank four for
  $0<w\le0.388$. The R–NS difference $\pi/(2L)$ is therefore the full
  coefficient in the two-derivative dual action. A partial-wave computation
  of the gauge-fixed bosonic Hessian leaves the two translations as the only
  gapless bosons for $w\le0.42$, so the individual R and NS coefficients
  $(0,-\pi/2)$ hold on the same range $0<w\le0.388$. P21 is realized in its massless limit on this
  string; its massive diagnostic and any QCD application stay open.
  P18 and P22 are not decided. [§11](outputs/1995-electric-string-corollary/paper.md#11-spin-structures-and-the-massless-fermions-of-the-unit-string)

## A finite-length test of the massless P21 sector

For a winding tube at fixed nonzero microscopic deformation, subtract the zero-flux vacuum separately in each spatial spin structure. Let $\mathcal E_\alpha(L)=\sigma L+c_\alpha+a_\alpha/L+o(1/L)$ for $\alpha=R,NS$, with $L$ times every nonzero mass gap large. The observable
$$
\widehat a_\alpha(L)=\frac{4L}{3}
 [2\mathcal E_\alpha(L)-3\mathcal E_\alpha(2L)+\mathcal E_\alpha(4L)]
 \longrightarrow a_\alpha
$$
cancels both the tension and a length-independent offset. The coefficient of $a_\alpha/L$ in the bracket is $2-3/2+1/4=3/4$.

For $b$ periodic real massless bosons and $f$ nonchiral Majoranas inheriting the microscopic spin choice, with unit limiting velocity and ordinary ground sectors, the 1986 oscillator sums give $a_R=\pi(f-b)/6$ and $a_{NS}=-\pi b/6-\pi f/12$. Thus $f=4(a_R-a_{NS})/\pi$ and $b=f-6a_R/\pi$. The minimal two-translation, two-Majorana branch gives $(0,-\pi/2)$; one additional neutral periodic scalar gives $(-\pi/6,-2\pi/3)$. Both give the same spin difference $\pi/(2L)$. The separate three-length observables discriminate these two spectra. An interacting infrared theory requires interpreting its Casimir coefficients as such; completeness of the microscopic fermion kernel and removal of additional bosons are separate questions. QCDS-95/S1 §11 derives both halves at the BPS point and bounds the fermionic half along the deformation; the bosonic half at $w>0$ follows from the partial-wave Hessian for $w\le0.42$. [1986 determinant](outputs/1986-fermionic-flux-tube/paper.md#54-a-difference-which-selects-odd-windings) · [1995 unit-flux setting](outputs/1995-electric-string-corollary/paper.md) · [Worked test](https://github.com/arivero/qcdstring/issues/3#issuecomment-7192993166)

## December 1996 · Two units of electric flux

P26 was [registered](https://github.com/arivero/qcdstring/commit/03c2a9e) before the separate contour and charge-graph calculations. The single-trace quartic gradients give the relative response $H=(4,2,4)$. The leading screened $SU(4)$ center-two ratio crosses the two-unit threshold at $t_*=-0.11327046\ldots$ with all condensates nonzero. The log slope at zero is $-2$. **Derived in the weak monopole action. Physical test open.** The quadratic sine ratio is reproduced in the softly broken supersymmetric vacuum. The P10 claims about pure gauge theory and large $N$ remain open. The geometric search is **narrowed** to candidates with a physical center-charge sink and binding, including a relative membrane on a fivebrane. [Manuscript](outputs/1996-center-flux-response/paper.md) · [Printout](outputs/1996-center-flux-response/results/flux-response.json) · [Independent report](outputs/1996-center-flux-response/REFEREE.md)

## December 1998 · Color and supersymmetry across the dualities

P27 was [registered](https://github.com/arivero/qcdstring/commit/00f602f) before the independent endpoint and tilted-strip calculations. **Derived and numerically checked in the fixed classical membrane probe.** The four-color ratio grows from $\sqrt2$ with relative coefficient $+1/4$ in $\eta$. At $R=40\ell_p$, $a=20\ell_p$ the matched inertia is $K_\phi=26279.36$. The conditional angular gap at $L\sqrt{\sigma_1}=1000$ is $1.9026\times10^{-8}\sqrt{\sigma_1}$. The geometric charge target is **reached** by the historically published fivebrane map. The route to a pure four-dimensional spectrum is **narrowed** by the surviving compact mode in the Gaussian probe and the lack of parametric KK separation in the large-strip, large-circle limit. A finite-action winding-changing core, its fermion insertions, the coupled fivebrane norm and the four-dimensional spectral test remain open. P10, P18 and the microscopic application of P27 retain their separate scope. [1998 article](outputs/1998-colour-across-dualities/paper.md) · [Stored check](outputs/1998-colour-across-dualities/results/membrane.json)
