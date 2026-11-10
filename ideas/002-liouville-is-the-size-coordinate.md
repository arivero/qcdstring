# 002. The Liouville field is the size coordinate
**Status:** in progress
**Depends on:** 001
**Predictions:** P05, P09

## Claim
The quantum string in d < 26 dimensions has one more degree of freedom
than its d embedding coordinates: the conformal factor of the worldsheet
metric. It behaves as an extra target-space coordinate. For the hadronic
string this coordinate is the size, or equivalently the energy scale, of
the configuration, and the effective metric in which the string moves is
warped along it. The warping is what shifts Regge intercepts (006) and
produces power-law hard scattering (007).

## Known in 1974
* Faddeev-Popov gauge fixing (1967) and the conformal anomaly (Capper
  and Duff, this year) are available.
* Lovelace's d = 26 and the GGRT analysis say that in d = 4 the
  Virasoro constraints cannot all be imposed; something must give.
* Wilson's renormalisation group treats scale as a continuous parameter,
  and the strong-coupling lattice string knows about the lattice spacing.

## What the memory says
* Polyakov 1981: in the covariant path integral with worldsheet metric
  g = e^{phi} g_hat, the anomaly produces the Liouville action
  (26-d)/(48 pi) x integral [ (d phi)^2/2 + mu e^{phi} ] for phi; the
  string in d dimensions is a critical string in d+1.
* Polyakov 1997: for a gauge theory, the Liouville direction is the
  fifth dimension; the metric is ds^2 = a(phi)^2 dx^2 + d phi^2 and the
  condition of an area law for large Wilson loops is that a(phi) has a
  minimum (an infrared wall). The zigzag symmetry of Wilson loops
  constrains the boundary conditions.
* Maldacena 1997, Witten 1998: for large-N gauge theories at strong
  coupling the warped space is weakly curved and the string is the
  ordinary critical superstring, with the extra five dimensions compact.
  Confining examples: a thermal circle that caps the geometry (Witten),
  the Klebanov-Strassler throat.

## Test
1. `[pencil]` Reproduce Polyakov's 1981 computation.
2. `[pencil]` Take the warped metric with an infrared wall at phi_0. Show
   a static string sinks to the wall and its energy is sigma R with
   sigma = a(phi_0)^2 / (2 pi alpha'). That is the KSS 1998 computation.
3. `[pencil]` Identify a(phi) with the RG scale: the Wilson loop of size
   L probes phi where a(phi) ~ 1/L. Write this as a 1974 statement about
   the renormalisation group and send it to Wilson.
4. `[pheno]` Use the metric in 006 and 007.

## Expected outcome, and what would refute it
A consistent set of three numbers from one metric: the Pomeron intercept,
the rho intercept, and the hard-scattering exponent. Refuted if no
warping reproduces all three, or if the Liouville direction can be shown
to decouple from physical amplitudes.

## 1984 paper
`outputs/1984-critical-dimension/` (QCDS-84/1). Proposed there: for a long
string the conformal factor is the induced one, and the anomaly action
evaluated on the induced metric supplies the missing central charge 26 - d
with no new field (the count is derived in Appendix B of the paper). The
closed-tube data of 1982 count c = 0.99(3)(9) massless modes and exclude a
further scalar lighter than 1.2 sqrt(sigma) in the 3d Z2 theory; they are
equally consistent with no such field and with a heavier one. A first version
read this geometrically (a tube at one value of an extra coordinate); the
referee pointed out that the reading belongs to the years after 1988, and it
was removed from the paper. The claim above, that the extra coordinate is the
size or energy scale and that the metric is warped along it, is untouched:
tests 2 to 4 remain, and the geometric reading waits for its historical date.

## References
Polyakov1981, Polyakov1997, Maldacena1997, Witten1998b, KSS1998,
KlebanovStrassler2000, PolchinskiStrassler2001.
