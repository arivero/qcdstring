# The second line: Astra 6.0, "Strings, 1974"

An independent group was given the same premise: end of 1974, full modern
knowledge, strings as a theory of quantum matter rather than of our
gravity. Their package (version 0.3, 35 files) is stored unmodified in
`astra-6.0/`; provenance and reproduction are in `PROVENANCE.md`. This
file records how the two lines fit together and what each changes in the
other. Where the main repository was edited as a result, the edit points
back here.

## How their tests map onto our ideas

| Second line | Question | Our idea | Relation |
|---|---|---|---|
| T01 | What forces a massless tensor to couple gravitationally (Weinberg's soft theorem) | 006, THESIS 2.3 | **Correction adopted**; see below |
| T02 | Can the closed sector be removed from an interacting open string (annulus factorization) | 023 | New to us |
| T03 | Long confining string, Luscher term, domain of validity | 001, 005 | Same formulas, same caveats |
| T04 | Strings from colour ordering; loop equations and retracing identities as tests | 003 | Their loop-equation test added to 003 |
| T05 | Physical meaning of the spin-two object; hard-wall toy and smooth D4 benchmark | 006, 010, 021 | Their D4 result is now our benchmark |
| T06 | Regge and hard scattering from one candidate | 007 | Same mechanism (Polchinski-Strassler) |
| T07 | Little string theory: finite tension with gravity decoupled | 023 | New to us |
| T08 | NCOS: interacting open strings without bulk gravity | 023 | New to us |
| T09 | Ultraviolet completion of the confining worldsheet; central-charge budgets | 002, 012 | Same programme; their NS/R Casimir table added to 001 |
| T10 | Internal degrees of freedom read through observables | 020 | Parallel |
| T11 | One exceptional up-type Yukawa | 024 | New to us |
| T12 | A bound on generations that survives decoupling gravity | 025 | New to us |
| T13 | Relation between the QCD and Fermi scales | 026 | New to us |
| T14 | Which supersymmetry, why, and its fate | 022 | Their four-way distinction adopted |

## Where the two lines agree

* The long-string expansion, its coefficients and its limits:
  -pi/(12R), then -pi^2/(288 sigma R^3), valid only for R sqrt(sigma) >> 1.
  The short-string imaginary energy says nothing about a physical tachyon.
* 1/N counts topology. Topology alone does not give a worldsheet action.
* Hard exclusive scattering needs a warped radial direction; flat-space
  fixed-tension strings are exponentially soft at fixed angle.
* In d < 26 the worldsheet needs more degrees of freedom than the two
  transverse modes, and the radial (Liouville) sector is the first
  candidate.
* In a confining background the tensor sector has a mass gap. Both lines
  locate the physics of the spin-2 state in the background, and both use
  bulk gravitational variables as bookkeeping for a nongravitational
  boundary theory.

## Where they disagree, and the resolution

**1. The spin-2 state.** Our THESIS 2.3 said that the massless spin-2
closed-string state "is the Pomeron, seen in the wrong background". The
second line's T01 rejects any argument that renames a massless tensor or
moves its intercept by hand: a physical massless helicity-2 particle with
a nonzero soft coupling obeys Weinberg's identity, and that identity
forces universal coupling. Their criticism is right about the phrasing.
The physical content of our claim survives in a sharper form, which is now
the text of THESIS 2.3: the hadronic string lives in a confining
background; there the tensor equation has no normalizable zero mode
(proved in the D4 model from tip regularity and UV normalizability, with
no adjustable wall); the lowest tensor is a massive 2++ glueball; the
Pomeron is the Regge trajectory through those states, with its intercept
computed from the curvature (Brower-Polchinski-Strassler-Tan) rather than
assigned. In flat space the massless tensor stays what Scherk and Schwarz
said it was.

**2. Standard of evidence.** The second line admits no post-1974 numbers
as inputs or as evidence, only three qualitative targets. Our ledger
registers remembered numbers as `[MEMORY]` predictions (P01, P04, P05, P07,
P08 and others). Both rules are kept. A remembered number is never an
input to a calculation and never counts as support for a claim; it is a
dated prediction whose only role is to choose the next calculation. A
ledger entry counts as supported only when it is reproduced inside the
programme. The second line's six status labels map onto ours as follows:

| Second line | Ours |
|---|---|
| Historical input | `[1974]` |
| Imported result | `[MEMORY]`, theory only |
| Reproduced benchmark | `[1974]` once rederived, with a pointer to the code |
| Toy result | `[TEST]` with the model stated |
| Proposed test | `[TEST]` |
| Conjecture | `[MEMORY]` or untagged speculation; idea status "open (speculative)" |

**3. Scope.** The second line has five explanatory targets: an
exceptionally heavy top, a limit on generations, a QCD-Fermi scale
relation, the meaning of the spin-two object, and the origin of
supersymmetry. We had the last two and none of the first three. All five
are now targets here too (RESEARCH_PLAN, "Explanatory targets"; ideas
024-026). This moves the boundary drawn in LONG_MARCH section 7: flavour
is inside the programme when it is derived in a nongravitational sector,
such as a local brane system, and outside it when it needs a compact
gravitational vacuum.

**4. The existence question.** Little string theories and NCOS show that
finite-tension interacting strings can exist with gravity decoupled. Our
thesis argued from hadron physics alone. The second line keeps the two
achievements apart, and so do we now (idea 023).

**5. The D4 model's limitation.** LONG_MARCH used Witten's D4 background
as the type IIA chart of the confining vacuum without a caveat. The
second line shows that its unwanted Kaluza-Klein states sit at the tensor
scale. Our `numerics/d4_tensor.py` turns that into one number: matching
the remembered lattice ratio m(2++)/sqrt(sigma) ~ 4.9 inside the D4
background needs lambda ~ 4.3, outside the classical regime where the
calculation is valid. The caveat is now in LONG_MARCH and in idea 021.

## What we add to their line

* A dated ledger with kill criteria, which their package lacks.
* 1974 phenomenology run on 1974 data: the Regge-slope fit, the
  charmonium potential, a Z2 lattice Monte Carlo showing the area law
  and the roughening departure.
* The duality web of LONG_MARCH as charts on the confining vacuum, with
  k-strings, the membrane string and the geometric transition, which
  their package mentions only through the D4 and local brane examples.
* The next three D4 tensor levels (m/M_KK = 2.485, 3.374, 4.252) from an
  independent method.
* A joint prediction, P18, built from their worldsheet-fermion Casimir
  table and our ledger.

## Open between the lines

* Their first construction is a local seven-brane sector for flavour.
  Ours begins from the flux tube. Nothing yet connects the two in one
  model, and their own rule says it must.
* Their hard-wall toy shows that a Robin condition restores the tensor
  zero mode. Our claim needs a dynamical infrared end, and only the D4
  example supplies one.
* Neither line has a controlled string dual of QCD with light quarks.
