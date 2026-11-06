# Thesis: the string is the chromoelectric flux tube

Written 6 November 1974. Revised as the ledger in `PREDICTIONS.md` fills up.

## 1. The claim

The relativistic string (Nambu 1970, Goto 1971, Nielsen, Susskind) is the
physical object behind the dual resonance model, and that object is a tube
of colour-electric flux stretched between quarks. Its tension is

    sigma = 1/(2 pi alpha'),   alpha' = 0.88 +/- 0.05 GeV^-2  (Chew-Frautschi plots, PDG 1974)
    sqrt(sigma) ~ 0.42 GeV,    i.e. a tension of about 0.9 GeV per fermi.

Everything the string has ever explained is hadronic: linear Regge
trajectories with a universal slope for mesons and baryons, duality
(Dolen-Horn-Schmid), the exponential growth of the hadron level density
(Hagedorn), the narrow-resonance approximation, and the topological
organisation of amplitudes that 't Hooft's planar expansion (this year)
now derives from a gauge theory of quarks and gluons.

Three independent lines, all from the last eighteen months, say that a
Yang-Mills theory produces strings:

1. **Nielsen and Olesen (1973)**: the Abelian Higgs model has vortex lines
   whose dynamics, at long wavelength, is the Nambu-Goto action.
2. **Wilson (1974)**: on a lattice, at strong coupling, the expectation of
   a closed loop of gauge field falls like exp(-sigma x Area). The
   surfaces in the strong-coupling expansion are the string worldsheet.
   Nambu's paper of this year says the same in continuum language.
3. **'t Hooft (1974)**: the 1/N expansion of an SU(N) gauge theory is a
   sum over surfaces weighted by N^chi. That is the genus expansion of a
   string with coupling g_s ~ 1/N.

The string of the dual models and the string of the strong interactions
are the same string, and the gauge theory is its microscopic origin.

## 2. The 1974 objections, and the answers the memory supplies

Each objection below is real and was decisive, historically, in killing
the hadronic string by about 1977. Each has an answer that becomes
standard between 1981 and 2013. The answers are `[MEMORY]` and must be
rederived; the objections are `[1974]`.

### 2.1 The critical dimension (d = 26, or 10 with fermions)

**Objection.** Lorentz invariance of the quantum string in flat space
requires d = 26 (Lovelace 1971; Goddard-Goldstone-Rebbi-Thorn 1973).
Hadrons live in d = 4.

**Answer.** `[MEMORY]` The flux tube is a *long* string, and the correct
question is what the low-energy theory of its transverse oscillations
looks like in d = 4. Polchinski and Strominger (1991) show that the
anomaly can be cancelled by a non-polynomial term built from the induced
metric, at the cost of the theory being effective (valid for R sqrt(sigma)
>> 1) rather than fundamental. The consequences are rigid: the ground
state energy of a string of length R is

    E_0(R) = sigma R - pi (d-2) / (24 R) + O(1/R^3)                 (Luscher 1981)

with a universal coefficient in any d, and the whole Nambu-Goto spectrum

    E_n(R) = sqrt( sigma^2 R^2 + 2 pi sigma ( n - (d-2)/24 ) )      (Arvis 1983)

is correct up to and including order 1/R^5 in d = 4 (Aharony and
collaborators, 2009-2013). Polyakov (1981) gives the other half: in d < 26
the conformal factor becomes a dynamical Liouville field. The two views are
reconciled by the "memory" that a d = 4 confining string is a critical
string in a curved higher-dimensional space (section 2.4).

The Casimir reading of the intercept was already available: Brink and
Nielsen (1973) show that -(d-2)/24 is the zero-point energy of the
transverse modes. The Luscher term is that same zero-point energy for a
string of finite length. `[TEST]` See `ideas/001`.

### 2.2 The tachyon

**Objection.** The ground state of the bosonic string has m^2 = -1/alpha'.

**Answer.** `[MEMORY]` In the Arvis formula, E_0^2 < 0 only for
R < R_c = sqrt(pi (d-2) / (12 sigma)) ~ 0.7 / sqrt(sigma) ~ 0.3 fm. That is
precisely where a flux tube is no longer long and the effective
description fails. The tachyon is the statement that a *short* string
in *flat* space is unstable; the physical hadron string lives on top of
a confining vacuum where the short-distance physics is perturbative
gluon exchange, which has no such instability. In the fermionic string
the tachyon is removed by a projection (Gliozzi, Scherk, Olive 1976), and
in the curved backgrounds of section 2.4 it is lifted by curvature.
`[TEST]` See `ideas/005`.

### 2.3 Massless states: the spin-1 and the spin-2

**Objection.** The open string has a massless vector (intercept alpha(0)=1)
and the closed string a massless spin-2 (intercept 2). The rho trajectory
has alpha(0) ~ 0.5 and the Pomeron has alpha(0) ~ 1.0. There are no
massless hadrons. Scherk and Schwarz take the massless spin-2 at face
value and call it the graviton.

**Answer.** In flat space Scherk and Schwarz are right. A physical
massless helicity-2 particle with a nonzero coupling obeys Weinberg's
1964 soft identity, which forces it to couple universally to
energy-momentum; renaming it, or moving its intercept by hand, changes
nothing. (The second line's T01 makes this point against our earlier
wording; see `second_line/README.md`.) The claim of this repository
concerns the background. `[MEMORY]` The hadronic string lives in a
confining background, and there the tensor sector has a mass gap. In
Witten's D4 model the transverse-traceless equation has no normalizable
zero mode, by tip regularity and UV normalizability alone, and its lowest
state is a massive 2++ at 1.5669 M_KK (computed by the second line,
confirmed by `numerics/d4_tensor.py`). The Pomeron is the Regge trajectory
through those massive tensor states. Its intercept is computed from the
curvature of the background,

    alpha_P(0) = 2 - 2/sqrt(lambda) + ...,   lambda = g^2 N   (Brower, Polchinski, Strassler, Tan 2006)

and interpolates between 2 (free string) and 1 (perturbative two-gluon
exchange). The observed 1.08 (Donnachie-Landshoff 1992) sits in between.
The same curvature pushes the open-string vector down the rho trajectory
to alpha_rho(0) ~ 0.5. What the flat-space theory calls the graviton
becomes, in the confining background, the leading vacuum-exchange
trajectory, whose states are massive and whose couplings carry form
factors. `[TEST]` See `ideas/006`.

### 2.4 Hard scattering

**Objection.** Fixed-angle string amplitudes fall like exp(-alpha' s f(theta)).
Exclusive hadron scattering at fixed angle falls like a power, s^{2-n},
with n the number of elementary constituents (Brodsky-Farrar 1973,
Matveev-Muradyan-Tavkhelidze 1973). This is the parton model's victory
over the dual model, and it is the hardest objection on the list.

**Answer.** `[MEMORY]` Polchinski and Strassler (2001): if the string
propagates in a fifth, warped direction r that plays the role of energy
scale, the amplitude at fixed angle is the flat-space exponential
convolved with the hadron wavefunctions in r. Small-r (ultraviolet)
contributions dominate and the result is the power law with exactly the
counting-rule exponent. In 1974 language: the hadronic string carries an
extra coordinate, its size, with a metric that red-shifts energies
proportionally to that size. This is the single most important idea to
rederive, because it also fixes 2.1 and 2.3. `[TEST]` See `ideas/007`.

### 2.5 Quarks, flavour, chiral symmetry

**Objection.** The dual string has no quarks; flavour enters by the
Chan-Paton trick; chiral symmetry is absent.

**Answer.** `[MEMORY]` Quarks are the string endpoints (Bardeen, Bars,
Hanson, Peccei 1976); the Chan-Paton index is the label of the surface
on which the endpoint lives (Polchinski 1995); chiral symmetry breaking is
the joining of two such surfaces (Sakai and Sugimoto 2004). The
quark-diquark picture makes the baryon a string too, and the meson and
baryon trajectories share a slope and differ in intercept by a fixed
amount (Miyazawa 1966; Brodsky, de Teramond, Dosch 2015). `[TEST]` See
`ideas/008`, `ideas/016`.

## 3. Why the gravity interpretation is the wrong bet

1. **Scale.** It discards the one number the theory is anchored to,
   alpha', and replaces it with 1/M_Planck^2. Every hadronic check becomes
   inaccessible.
2. **What the leading closed-string trajectory actually does.** Its
   intercept is measured in proton-proton scattering at the ISR this
   year. It is about 1, and the states on it are massive. The trajectory
   is the Pomeron.
3. **The genus expansion has a name.** It is 1/N, and N = 3.
4. **Testability.** The hadronic string makes numerical predictions for
   lattice computations that can be run on a 1974 computer (section 5),
   and for Regge and Pomeron phenomenology that can be checked against
   this year's Particle Data tables.
5. **The memory's own verdict.** The gravity program becomes the mainstream
   from 1984. What it finds, by 1997, is that its best-understood examples
   are gauge theories in disguise (Maldacena). The string of hadrons was the
   right object all along; the graviton that keeps appearing is a
   bulk field whose normalizable modes, in a confining background, are the
   massive tensor glueballs on the Pomeron trajectory.

I will state the honest counterweight. In the memory, the gravity
interpretation leads to a consistent perturbative quantum gravity, to
the counting of black-hole microstates, and to the duality just named.
The hadronic interpretation, pursued alone, would have had to discover
holography from the gauge-theory side. The plan in `RESEARCH_PLAN.md`
is a bet that it can.

## 4. What would change my mind

* A measured Luscher coefficient in a confining gauge theory that differs
  from -pi(d-2)/24 by more than its error.
* A lattice flux-tube spectrum that fails the Arvis formula at O(1/R^3).
* A Pomeron intercept at the ISR consistent with 2, or with 0.
* A proof that the fixed-angle power laws cannot arise from any string
  with an extra warped coordinate.
* A graviton. Specifically, an isolated massless helicity-2 pole in a
  hadronic amplitude whose soft coupling is universal, as Weinberg's
  identity would then require. The Pomeron couples to hadrons with form
  factors and through massive states.
* A confining background in which the tensor equation keeps a
  normalizable zero mode without an adjustable boundary condition.
* The second line's tests T01, T02 and T05 failing for every candidate
  in a defined class (`second_line/astra-6.0/IDEA_REGISTER.md`).

## 5. A second line

An independent group (Astra 6.0) was given the same premise and reached a
compatible position by a stricter route. Their package is in
`second_line/astra-6.0/`, and `second_line/README.md` records where the
two lines agree, where they disagree, and what each now adopts. Their
three additions that change this thesis: the soft-theorem correction to
2.3, the existence benchmarks of little strings and NCOS (idea 023), and
three flavour targets (ideas 024-026).

## 6. Tools available now

Paper and pencil; the Review of Particle Properties (April 1974); ISR and
Serpukhov total cross-sections; SLAC deep-inelastic data; a CDC 7600 or
IBM 370 with Fortran; the Metropolis algorithm (1953), Wilson's lattice
(1974), and the strong-coupling expansion. A Monte Carlo of a Z2 or SU(2)
lattice gauge theory on an 8^3 or 6^4 lattice is feasible this winter.
In the memory, Creutz does this in 1979. There is no reason to wait.
