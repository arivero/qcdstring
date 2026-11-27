# The long march: five superstrings, M-theory, and the QCD string

Written 7 November 1974. A plan for what the hadronic programme does with
everything the memory says arrives between 1984 and 2004: the five
consistent superstring theories, their web of dualities, and the
eleven-dimensional theory behind them. All of it is `[MEMORY]`.

## 0. The admission

By the time the five theories are understood as limits of one theory,
the subject is geometry: Calabi-Yau threefolds, G2 holonomy, conifolds,
orientifold planes, branes wrapped on cycles. There is no sense in which
a 1974 hadron physicist can refuse that. The claim of this repository is
narrower and sharper: **the geometry that matters is the geometry of the
confining vacuum**, read in dual variables. A hadronic interpretation
requires an observable in that vacuum that we can identify in both
descriptions.

Our working hypothesis is that one can follow a four-dimensional
confining flux tube into a critical superstring or M-theory construction.
Which object carries its flux, which excitations survive on it, and what
its tension predicts are questions for each proposed background. One
worked example would establish a connection for that gauge theory.
[Target for the 1998 paper](#target-for-the-1998-paper)

## 1. Candidate connections to confining gauge theories

| Theory | Setting in the memory | Candidate flux tube or hadronic interpretation | Proposed gauge-theory dictionary |
|---|---|---|---|
| Type IIA | D4-branes on a spatial circle with antiperiodic fermions (Witten 1998). Probe D8-branes add flavour in the 2004 proposal of Sakai and Sugimoto. | Fundamental string near the tip of the capped geometry | The circle sets the Kaluza–Klein scale. The gauge coupling also enters the flux tension. Joined flavour branes encode chiral symmetry breaking in the later model. |
| M-theory | M5-brane on a holomorphic curve (the fivebrane model called MQCD, Witten 1997) | M2 membrane with its boundary on the M5 | The construction relates the $N$ vacua, domain walls and flux conserved modulo $N$. Tension ratios require a dynamical calculation in a specified regime. |
| Type IIB | Deformed conifold with fluxes (Klebanov-Strassler 2000); wrapped D5 (Maldacena-Nunez 2000); N=1* (Polchinski-Strassler 2000) | F-string; D-strings and (p,q) strings are the k-strings (Herzog-Klebanov 2001) | Deformation parameter of the conifold = Lambda^3; S-duality = electric-magnetic duality of 't Hooft and Mandelstam |
| Type I / Type I' | Orientifold of IIB / IIA. D8-O8 systems carry the flavour groups at the ends | Open string with Chan-Paton ends on flavour branes | SO(32) and SO(16)xSO(16) are the maximal flavour symmetries a stack of ends can carry |
| Heterotic E8xE8 | Horava-Witten 1996: M-theory on an interval, one E8 on each wall | A membrane stretched across the interval | The two walls are the left-handed and right-handed flavour groups; the interval is the chiral direction (idea 020) |
| Heterotic SO(32) | Dual to Type I (Polchinski-Witten 1995) | Same as Type I at strong coupling | Worldsheet current algebra = internal modes on the flux tube (idea 020) |
| Type 0 | Non-supersymmetric strings as duals of non-supersymmetric gauge theories (Polyakov 1998, Klebanov-Tseytlin 1998) | Fundamental string of a theory with no spacetime fermions and a tachyon lifted by flux | The tachyon potential is the vacuum energy of the gauge theory |

**Caveat on the IIA chart**, from the second line: in Witten's D4
background the unwanted Kaluza-Klein states sit at the same scale as the
glueballs. The tensor mass is 1.5669 M_KK, and the tension is
sigma = 2 lambda M_KK^2 / (27 pi). Matching the remembered lattice ratio
m(2++)/sqrt(sigma) ~ 4.9 needs lambda ~ 4.3, outside the regime where the
classical geometry is trustworthy (`numerics/d4_tensor.py`). The chart
shows the mechanism; it cannot yet be a controlled description of pure
Yang-Mills.

The softly broken supersymmetric gauge theory and the nonsupersymmetric
D4 compactification with its Kaluza–Klein tower give distinct comparisons.
Pure QCD with light quarks has no exact geometric dual in the memory.
The bridges are planar equivalence (Armoni-Shifman-Veneziano 2003: N=1 SYM
and QCD with antisymmetric-representation quarks coincide at large N in
the bosonic sector) and the type 0 construction. Both are listed as ideas
to rederive.

## 2. The dualities, read as hadronic statements

* **Electric–magnetic duality.** A small mass for the adjoint chiral
  multiplet in the 1994 $\mathcal N=2$ $SU(2)$ theory selects vacua in
  which a magnetic description explains confinement. This realizes the
  dual-superconductor idea of 't Hooft and Mandelstam. Identifying a
  four-dimensional flux sector with an IIB $(p,q)$ string would require
  a map of charges in a specified background. [Seiberg and Witten (1994)](https://arxiv.org/abs/hep-th/9407087) · [Idea 019](ideas/019-k-strings-are-pq-strings.md)
* **T-duality.** A circle of radius $R$ is dual to one of radius
  $\alpha'/R$. In the four-dimensional D4 construction the spatial
  compactification circle fixes a Kaluza–Klein scale. The circumference
  of Euclidean time fixes the temperature. Winding around the latter
  provides the thermal test in idea 005. [Witten (1998), §4](https://arxiv.org/pdf/hep-th/9803131#page=19)
* **The M-theory lift.** An M2 wrapped on the eleventh circle gives the
  type IIA fundamental string. The proposed confining string in MQCD is
  an M2 ending on a fivebrane. Its center charge follows from the allowed
  membrane boundaries. Interpreting the circle radius as a tube width
  would require a calculation of the transverse flux profile.
  [Witten (1997), §3.1](https://arxiv.org/pdf/hep-th/9706109#page=14) · [Idea 018](ideas/018-the-flux-tube-as-a-membrane.md)
* **Heterotic-Type I.** Open-string flavour at the ends versus internal
  current algebra on a closed string. For the flux tube: quarks at the
  ends versus an internal sector carried along the tube. `ideas/020`.
* **Geometric transitions (Gopakumar-Vafa 1998, Vafa 2000,
  Atiyah-Maldacena-Vafa 2001).** Branes on a cycle disappear and the cycle
  is replaced by flux through a dual cycle. This is the large-N
  statement that the gluons (the branes) are replaced by the vacuum
  condensate (the flux), i.e. confinement itself, done in a G2 holonomy
  geometry for N=1 SYM. `ideas/021`.

## 3. Geometry as vacuum structure

A dictionary to be filled, entry by entry, as each paper is rederived:

| Geometric object | Hadronic quantity |
|---|---|
| Radial coordinate | Renormalisation scale (002) |
| Infrared wall, capped circle, deformed tip | Confinement scale Lambda; the string tension is the warp factor at the tip (002, KSS 1998) |
| Compact internal manifold and its isometries | Global symmetries: R-symmetry, flavour |
| Complex-structure moduli of the conifold | Gluino condensate, Lambda^3 |
| Kahler moduli, B-field periods | Theta angles and couplings |
| Branes wrapped on cycles | Baryons (Witten 1998), domain walls, k-strings |
| Singularities of the geometry | Points where extra hadrons become massless |
| Flop or conifold transition | Large-N confinement (geometric transition) |

## 4. Supersymmetry

The GSO projection gives a tachyon-free supersymmetric spectrum. The
tachyon-free nonsupersymmetric constructions published in 1986 leave the
realization of supersymmetry on a confining tube a question for each
model. Two proposed hadronic readings follow. [QCDS-86/1, §4.4](outputs/1986-fermionic-flux-tube/paper.md#44-what-changed-in-1986)

1. **Supersymmetry as a large-N accident of the bosonic sector.**
   Planar equivalence says that the glueball and meson sectors of QCD
   with one antisymmetric Dirac flavour equal those of N=1 SYM at large N,
   so the supersymmetric string descriptions apply to a cousin of QCD up
   to 1/N corrections. `ideas/022`.
2. **Hadronic supersymmetry as a fact about hadrons.** Miyazawa 1966,
   Catto-Gursey 1985, Armoni-Patella 2009, Brodsky-de Teramond-Dosch 2015:
   the diquark is the superpartner of the antiquark, mesons and baryons
   sit on the same trajectories (016). A 2024 letter on the local shelf
   (`phys4/sources/rivero-so32-2024.pdf`) reads the scalars of the SO(32)
   string as the diquark and meson sector of a five-flavour hadronic
   supersymmetry. It is a single-author letter, recorded here as a lead
   and treated as such. `ideas/022`.

There is a theorem to respect: a modular-invariant string without
tachyons has an asymptotically Bose-Fermi degenerate spectrum
(Kutasov-Seiberg 1991; Dienes' "misaligned supersymmetry"). For hadrons
that is a measurable statement: the exponential growth of the meson and
baryon level densities has the same slope. Registered as P16.

## 5. What the memory is for, here

Nothing in sections 1 to 4 can be derived in 1974. The order in which
the memory says to proceed, so that each step is motivated by the
previous one from the hadronic side:

1. Dual superconductor (1974-76: 't Hooft, Nambu, Mandelstam, Polyakov).
2. Chan-Paton flavour at the ends; orientifold projection as the
   symmetry of the ends (1974-76).
3. Fermionic string with the GSO projection as a selection rule on the
   flux-tube spectrum (1976).
4. 1/N as the genus parameter; the baryon as an N-string junction with a
   vertex (1979: Witten; later the D5 baryon vertex).
5. Monopole condensation after a small $\mathcal N=2$-breaking deformation
   (1994), followed by the leading $SU(N)$ tension ratios (1995).
6. Branes as the surfaces where the ends live (1995); brane
   constructions of the gauge theory (1996).
7. The flux tube as a membrane in MQCD (1997); the Pomeron and the
   graviton (2006).
8. Geometric transition as confinement (1998-2001).
9. Type 0 and planar equivalence as the bridges to real QCD (1998-2003).
10. Flavour branes and chiral symmetry breaking (2002-2004).

## 6. Tests

* For $SU(4)$ the sine formula gives $\sigma_2/\sigma_1=\sqrt{2}$.
  Its derivation on the gauge side is at leading order in a small adjoint
  mass, and the fivebrane calculation is semiclassical. Extending the
  ratio to pure $\mathcal N=1$ Yang–Mills requires control of corrections
  to an unprotected tension. P10 registers the further conjecture for QCD.
  [Douglas and Shenker (1995), §2](https://arxiv.org/pdf/hep-th/9503163#page=12) · [Hanany, Strassler and Zaffaroni (1998), §9](https://arxiv.org/pdf/hep-th/9707244#page=33)
* The three-quark potential is a Y-junction with the meson tension (P15).
* Equal Hagedorn slopes for mesons and baryons (P16).
* The 2^{++} glueball on the Pomeron trajectory (006).
* Planar equivalence: degeneracies between the orientifold theory and
  SYM on the lattice at N = 3 to 6 (P17).

## 6b. Gravity-free strings

The duality web also contains strings that have no gravity at all. Little
string theories live on NS5-branes when g_s goes to zero at fixed alpha';
NCOS keeps open strings interacting in a near-critical electric field while
bulk closed strings decouple. Neither describes hadrons. Both refute the
universal claim that a finite-tension interacting string must carry
dynamical gravity, and the second line uses them as controls for exactly
that reason. Idea 023.

## 7. The boundary

Heterotic strings on Calabi-Yau manifolds as the origin of the Standard
Model, the cosmological applications, and quantum gravity in flat
ten-dimensional space are outside this programme. The second line moves
this boundary for flavour: a heavy top, a bound on generations and a
QCD-Fermi relation are targets (ideas 024-026) when they come from a
nongravitational sector, such as a local brane system with gravity
decoupled. A result that needs a compact gravitational vacuum stays
outside. The claim is that the
same formalism, applied to confining vacua, is the theory of the QCD
string, and that this is the application where the formalism meets data.

## 1986 update: the scope of the superstring reading

QCDS-86/1 (`outputs/1986-fermionic-flux-tube/`) revised the original premise
that removing the tachyon requires spacetime supersymmetry.
The tachyon-free nonsupersymmetric SO(16)xSO(16) constructions are now published
(AGMV1986, DixonHarvey1986). They retain gravity and do not solve the quantum
vacuum problem; they are counterexamples to that necessity claim, not a QCD
construction.

The new paper gives a nonchiral effective worldsheet mass mechanism and
states why it does not automatically apply to the chiral heterotic sector or
complete a critical string. Its SO(32) decomposition is an algebraic starting
point, not a proof of the flavour dictionaries in the table above. Those
entries remain memory-guided proposed identifications.

The user-suggested dimensional-selection question is recorded as idea 027.
Four-dimensional Yang-Mills power counting motivates a conditional
four-dimensional regime but neither proves higher-dimensional triviality nor
dynamically compactifies a dimension. A small compact target coordinate also
need not be a massive local worldsheet field. Both decouplings must be shown.

## After 1988: reconnecting the calculations to the superstring programme

Strategic discussion recorded 17 November 2026 (machine date), after
QCDS-88/1. The later discoveries below remain `[MEMORY]` until their
historical dates. This is a revisable research direction, not a commitment
to a particular next article.

The 1986 paper does engage with superstrings: critical RNS bookkeeping,
heterotic current sectors, compactification, tachyon-free nonsupersymmetric
constructions, and SO(32). Its new massive-fermion calculations nevertheless
belong to an effective worldsheet model; they do not construct a descent
from a critical superstring to a confining tube. The 1988 paper develops
massive normal modes and scalar-curvature exchange, with little direct
engagement with superstrings. Those calculations are useful, but a succession
of such papers could leave the central ambition of this roadmap untouched.
Correctness within the scope of an individual paper does not establish that
its subject is the most useful next step for the programme.

The proposed response is to make the connection constructive. A subsequent
paper could choose a concrete string or internal-sector construction using
the tools available in its year, determine its fields and projections,
examine anomaly conditions, and calculate a mechanism for lifting unwanted
internal modes while retaining the desired long tube. The 1986-1988 results
would then test that construction through its fluctuation spectrum and
finite-length observables. Giving extra fields a mass in an effective action
does not by itself settle the consistency of a critical worldsheet theory.
The open area-action $L^{-5}$ calculation and the mixed endpoint problem
can be taken up where they distinguish candidate spectra.

## Target for the 1998 paper

Revised 18 November 2026 (machine date). **Aim to publish one controlled
derivation of a four-dimensional confining tube from a superstring or
M-theory construction by the 1998 paper**, the last biennial slot before
2000. Identify the flux carried between external colour sources and derive
the tension $\sigma_1>0$ of the unit-flux tube. Recover its two transverse
translations, account for any modes required by symmetry, and calculate
how unwanted internal modes acquire a gap. Show the energy range in which
these statements and the microscopic approximation hold together. Where
the descriptions apply in different regimes, identify which observables
can be carried between them by a controlled continuation or a protection
argument.

Use $\sigma_1$ to set units and fix the remaining dimensionless inputs
independently of a second observable. One choice is the lowest closed-tube
excitation energy in a specified polarization and spin structure. Predict
$(E_{\mathrm{exc}}(L)-E_0(L))/\sqrt{\sigma_1}$ at a stated $L\sqrt{\sigma_1}$
where the level is sensitive to the internal spectrum. A gauge-theory
interpretation requires bulk gravity to decouple from the measured
sector. Extending a result to pure Yang–Mills also requires decoupling
extra bulk states, including Kaluza–Klein modes, at the confinement scale.

The following sequence is a working choice. Results become evidence in a
slot only once available at its historical date. A different construction
can replace the proposed one if it gives better control.

- **1990–1992.** The 1990 note fixes the polarization projector. The extra
  1991 paper matches its pole in a unit Abelian Higgs vortex. At equal
  bulk masses a scalar of the same mass couples to a different channel.
  The [1992 article](outputs/1992-scalar-doublet/paper.md) carries the polarization measurement into a deformed Abelian matter theory, resolves a scalar doublet and distinguishes the linear magnetic-probe potential from screened electric exchange. This fixes the flux and width to match in a dual gauge description.
  [1990 amplitude table](outputs/1990-pseudoscalar-curvature/amplitudes.md) · [1991 vortex calculation](outputs/1991-vortex-pseudoscalar/paper.md)
- **1994.** Use the monopole vacuum of $SU(2)$ with a small adjoint mass
  to trace an electric probe to a vortex in the dual gauge theory.
  Determine its tension and the range of energies where the Abelian
  description controls its fluctuations. [Seiberg and Witten (1994)](https://arxiv.org/abs/hep-th/9407087)
- **1996.** Use the 1995 $SU(N)$ result to compare distinct fluxes for
  $N\ge4$. Record which tension relations depend on weak breaking. The
  type IIA lift gives a membrane interpretation of the fundamental string.
  Ask which object could carry the center flux seen by the gauge-theory
  probe. The type I D1 and heterotic string also give
  an example of matching actual worldsheet fields across a duality.
  [Douglas and Shenker (1995)](https://arxiv.org/abs/hep-th/9503163) · [Witten (1995)](https://arxiv.org/abs/hep-th/9503124) · [Polchinski and Witten (1995 preprint)](https://arxiv.org/abs/hep-th/9510169)
- **1998.** Try the M2 ending on the M5 in MQCD. Its flux is conserved
  modulo $N$. Its extra angular worldsheet field has a shift symmetry
  that forbids the explicit pinning potential used in the 1986 paper.
  The topology permits the angle to unwind. Calculate the strength
  and relevance of the winding-changing interaction at the
  stiffness set by $\sigma_1 R_{11}^2$, where $R_{11}$ is the M-theory
  circle radius. Can it gap the angle while the membrane calculation
  remains reliable? An identification with the 1990 pseudoscalar would
  require its parities and two-phonon matrix element. Count the Goldstone
  fermions of the supersymmetric tube in the finite-length prediction.
  A tube with only bosonic gapless modes would require a deformation
  that lifts those fermions as well.
  [QCDS-86/1, §8.4](outputs/1986-fermionic-flux-tube/paper.md#84-a-pinned-compact-coordinate-a-constructive-test) · [Witten (1997), §3.2](https://arxiv.org/pdf/hep-th/9706109#page=16) · [Hanany, Strassler and Zaffaroni (1998), §9](https://arxiv.org/pdf/hep-th/9707244#page=33)

If the available limits conflict, the 1998 paper can identify the
surviving light mode or the incompatible scale inequalities and give
the range of parameters they exclude. That would settle a question about
the candidate while leaving the positive construction open. An
uncalculated winding amplitude leaves the gap undecided. The 1998 D4
compactification offers another calculation within the period, with
the Kaluza–Klein limitation described in Section 1. The confining IIB
backgrounds of 2000 and later offer subsequent tests.

### Disposition after the 1998 paper

The fundamental IIA string maps to a wrapped M2. In the presence of the pure MQCD fivebrane, the same relative class has a cheaper open representative bound to the four-dimensional sector. The inclusion of the curve winds $N$ times around the ambient circle. This **reaches** the center-charge test in the historical construction. QCDS-98/1 derives the shift of the free membrane endpoints, its angular inertia and a finite-length level in a specified probe. All four vacuum supercharges are broken by the supersymmetric color string. The extra angular mode can evade a test that measures only the difference between spatial spin structures. [QCDS-98/1](outputs/1998-colour-across-dualities/paper.md)

The dynamical target is **narrowed**. Classical large radii drive $\sigma_1 R_{11}^2$ large, keeping even the conservative angular winding dimension above the Gaussian relevance threshold and the KK scale below the tension scale. The more decisive continuation would calculate the coupled M2–M5 norm and a finite-action winding defect with its fermionic insertions. Its amplitude and the extrapolation of the unprotected gap to an autonomous four-dimensional theory remain open. [Scale test and next calculation](outputs/1998-colour-across-dualities/paper.md#9-disposition-of-the-geometric-target)

### Disposition after the 1999 supplement

QCDS-99/S1 computes the alternative named in QCDS-98/1 §8. At the tip of the compactified D4 cigar the string carries a doublet of mass $M_{\rm KK}$ with Kaluza–Klein charge, eight fermions of mass $M_{\rm KK}/2$ from the four-form flux, and four sphere fields that form an $O(5)$ sigma model with coupling $1/g^2=\lambda/6\pi=(9/4)\sigma/M_{\rm KK}^2$. The sphere gap is proportional to $M_{\rm KK}(\lambda/9)^{1/3}e^{-\lambda/9}$ if the matching introduces no $\log\lambda$. Where the geometry is reliable the tube therefore carries six light transverse bosons over an exponentially long range of lengths. It reproduces the two-translation Casimir term only beyond the sphere gap. The D4 route to pure Yang–Mills theory is **narrowed**, because it needs the small coupling at which the construction is uncontrolled. The 2000 slot can test the confining IIB backgrounds against the requirement that the string's position on any internal space meets a classical potential. [Supplement](outputs/1999-string-at-the-tip/paper.md#10-disposition-and-the-next-calculations)
