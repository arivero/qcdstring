# Research plan

Started 6 November 1974. Horizon: five years, with a hard review each
January. The aim is to establish, with the tools and data of the 1970s,
that the dual string is the confining flux tube of a non-Abelian gauge
theory, and to extract from it quantitative hadron physics. The memory of
the next fifty years is used to choose which calculations to do and in
which order; every remembered result is rederived before it is used.

## Guiding principles

1. **Rederive before you cite.** A `[MEMORY]` tag on a result means it is
   a conjecture here. Promote it to `[1974]` only with a derivation or a
   check against present data.
2. **Long strings first.** Everything robust about the hadronic string
   is a statement about a string whose length is large compared with
   1/sqrt(sigma). Start there. Short-string questions (the tachyon, the
   exact meson spectrum) come later and need the warped coordinate.
3. **Compute.** A Monte Carlo of a lattice gauge theory is a 1975 project
   on a 1975 machine. Do it before anyone else thinks it is worth doing.
4. **Phenomenology is the anchor.** Regge slopes, the Pomeron intercept,
   total cross-sections, charmonium (from next week), and the hadron level
   density are the data. Every theoretical step must point at one of them.
5. **Keep the ledger.** `PREDICTIONS.md` is written before the results
   arrive and is never edited after.

## Phase 0: November 1974 to January 1975. Ledger and data.

* Write `THESIS.md`, register the first predictions.
* Tabulate the 1974 Review of Particle Properties: masses, spins, widths
  for the leading meson and baryon trajectories (`data/`).
* Fit the Chew-Frautschi plots. Extract alpha' per trajectory, test
  universality, compute sigma and the string's Hagedorn temperature
  (`numerics/regge_fit.py`). **Deliverable:** one table, one figure.
* Charmonium (from 11 November): fit the levels with V(r) = -(4/3)
  alpha_s / r + sigma r using the Regge sigma. `[MEMORY]` This is the
  Cornell potential of 1975; sigma comes out near 0.18 GeV^2, i.e. the
  Regge value. **Deliverable:** a short note, before Cornell's.
* Secure computer time (Cornell via Wilson, or BNL, or CERN).
* Letters: see `people/correspondents.md`.

## Phase 1: 1975. The long string in four dimensions.

Analytic work, pencil and paper.

* **Casimir energy of a finite string.** Extend Brink-Nielsen (1973) to a
  string of length R with fixed ends: E_0 = sigma R - pi (d-2)/(24 R).
  Then show the coefficient is fixed by the Nambu-Goto leading term and
  is independent of everything else in the effective action (the
  argument that becomes Luscher 1981). `ideas/001`.
* **Full fixed-end spectrum.** Light-cone quantisation of the open
  string with Dirichlet ends (Goddard-Goldstone-Rebbi-Thorn 1973 methods)
  gives E_n(R) = sqrt(sigma^2 R^2 + 2 pi sigma (n - (d-2)/24)) (the
  Arvis formula of 1983). Note where d = 26 enters and argue that in an
  effective theory the formula holds to a definite order in 1/R.
  `ideas/001`, `ideas/012`.
* **Non-critical quantisation.** Reproduce Polyakov's 1981 path integral
  with the conformal factor as a Liouville field; identify the Liouville
  direction as a candidate for the size coordinate of Phase 4. `ideas/002`.
* **Strong-coupling expansion.** Push Wilson's expansion for sigma(beta)
  in Z2, U(1), SU(2) to several orders. Predict a roughening singularity
  where the Wilson surface stops being flat and the transverse string
  modes become massless; argue that the Luscher term appears only beyond
  it. `ideas/004`.
* **Hagedorn temperature.** T_H = sqrt(3 sigma / (2 pi)) ~ 0.29 GeV in
  d = 4 from alpha', against Hagedorn's 0.16 GeV from the resonance
  spectrum. Understand the discrepancy (quarks, string breaking, and the
  distinction between the pure-glue deconfinement temperature and the
  physical crossover). `ideas/009`.

## Phase 2: 1975-1976. Monte Carlo.

* Z2 in 3d (self-dual to the Ising model; a clean check), then U(1) in 4d
  (expect a confining phase at strong coupling and a Coulomb phase at
  weak coupling, with a transition near beta ~ 1), then SU(2) in 4d
  (expect no transition, and asymptotic scaling of sigma with the
  two-loop beta function at beta ~ 2.2-2.4). `[MEMORY]` Creutz 1979-80.
* Observables: Wilson loops, Creutz ratios chi(R,T), the string tension,
  the heavy-quark potential V(R).
* Stretch goal: the 1/R term in V(R). `[MEMORY]` This needs R > 0.5 fm
  and a variance-reduction trick (Luscher-Weisz 2001 multilevel); a
  1976 machine will see the area law clearly and the Luscher term
  marginally. Design the measurement so that the sign and rough size of
  the 1/R coefficient are testable. `ideas/001`, `ideas/004`.
* `numerics/z2_lattice.py` is the prototype written in the language of
  2026 for convenience; the 1975 version is Fortran.

## Phase 3: 1975-1977. Regge and Pomeron phenomenology.

* Total cross-sections from the ISR (rising since 1973) and Serpukhov:
  fit sigma_tot = X s^epsilon + Y s^-eta. `[MEMORY]` epsilon ~ 0.08.
  Interpret the Pomeron as the closed string's leading trajectory with
  its intercept pulled down from 2 by curvature. `ideas/006`.
* The Pomeron slope, alpha'_P ~ 0.25 GeV^-2, is smaller than half the
  rho slope. A flat closed string would give exactly half. Treat the
  ratio as a measurement of the background geometry. `ideas/006`.
* Meson and baryon trajectories: same slope, intercepts offset. Quark-
  diquark string. Test the Miyazawa supersymmetry on the 1974 tables.
  `ideas/016`.
* Quark masses at the string ends: the trajectory of a string with
  massive endpoints bends at low J; fit the strange and charmed mesons.
  `[MEMORY]` Sonnenschein and collaborators 2014. `ideas/008`.

## Phase 4: 1976-1978. The warped size coordinate.

This is the phase on which the whole program turns.

* Rederive the fixed-angle power laws: a string in a five-dimensional
  space with metric (r/L)^2 dx^2 + (L/r)^2 dr^2 and an infrared wall,
  amplitudes computed as the flat-space exponential convolved with
  wavefunctions in r. Target: the Brodsky-Farrar exponent. `ideas/007`.
* Rederive the Pomeron intercept shift: the leading closed-string
  trajectory in the warped space is a diffusion problem in r with
  alpha(0) = 2 - 2/sqrt(lambda). `ideas/006`.
* Identify r with the renormalisation scale. In the language available
  now: Wilson's renormalisation group with the scale promoted to a
  coordinate; Polyakov's Liouville field. Discuss with Wilson. `ideas/002`,
  `ideas/007`.
* Connect to 't Hooft's expansion: the string coupling is 1/N, and the
  curvature radius in string units grows like (g^2 N)^(1/4). Formulate
  the strong-coupling, large-N limit as the one where the string is
  weakly curved and the flat-space dual model is a good first
  approximation. `ideas/003`.

## Phase 5: 1977-1980. Quarks, chiral symmetry, glueballs, temperature.

* Quarks as string endpoints with mass and spin (Bardeen-Bars-Hanson-
  Peccei 1976). Spin-orbit forces from the string. `ideas/008`.
* Glueballs as closed strings; masses in units of sqrt(sigma) from the
  lattice. `ideas/010`.
* Finite temperature: the string's Hagedorn temperature versus the
  deconfinement temperature; prediction that T_c < T_H in pure gauge
  theory. `ideas/009`.
* Chiral symmetry as a property of the surfaces on which the endpoints
  live. This is the most speculative item and may have to wait.
  `ideas/008`.
* Two-dimensional QCD ('t Hooft 1974) as the exactly solvable string:
  the meson equation is a string with massive ends in d = 2. `ideas/015`.

## Milestones and kill criteria

| When | Milestone | Kill criterion |
|---|---|---|
| Jan 1975 | Universal slope table; charmonium note | Slopes differ by > 20% between meson and baryon trajectories with no diquark explanation |
| Jun 1975 | Luscher term derived; Arvis spectrum derived; Hagedorn note | Coefficient found to depend on the effective action beyond Nambu-Goto |
| Dec 1975 | Z2 and U(1) Monte Carlo running; area law seen | Area law absent at strong coupling (would contradict Wilson, so very unlikely) |
| Dec 1976 | SU(2) Monte Carlo: sigma(beta) with asymptotic scaling | No scaling window on a 6^4 to 8^4 lattice |
| Jun 1977 | Pomeron intercept and slope analysed as curvature effects | Intercept at the ISR consistent with 2 or with 0 |
| Dec 1978 | Hard-scattering power laws from the warped string | No warped metric reproduces the counting rules |
| 1980 | Lattice V(R) with a 1/R term of the right sign | 1/R coefficient positive or zero with small errors |

## Resources

* People: see `people/correspondents.md`. The three most valuable
  conversations are with Wilson (lattice, renormalisation group as a
  coordinate), 't Hooft (1/N, planar diagrams, the 2d model) and Nambu
  (strings from gauge fields).
* Computing: a few hundred hours per year on a CDC 7600 class machine.
* Data: the 1974 Review of Particle Properties; ISR total cross-sections;
  SLAC and Brookhaven e+e- and hadroproduction results from this month.

## Risks

1. **Credibility.** Results that arrive without derivation are
   indistinguishable from guesses. Mitigation: principle 1.
2. **The warped coordinate.** In the memory it needs D-branes and
   supergravity to be understood. Here it is a phenomenological ansatz.
   Mitigation: sell it as a generalised dual model with a size variable,
   and let the counting rules and the Pomeron intercept argue for it.
3. **Machines.** A 1975 Monte Carlo is slow. Mitigation: Z2 and small
   lattices first; the area law is visible on tiny systems.
4. **The field moves to gravity anyway (1984).** Mitigation: by 1984 the
   lattice program and the effective string should have produced enough
   numbers that the hadronic interpretation stands on its own.
