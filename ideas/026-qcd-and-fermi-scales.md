# 026. Why the QCD and Fermi scales are only three decades apart
**Status:** open. Transmutation and threshold controls done by the second line.
Nucleon-scale test of issue #2 done (26 November 2026): the held-out
nucleon comes out 18% light; the weak side is a continuous family.
**Depends on:** 009, 024, 025
**Predictions:** none registered
**Second line:** T13; notes/FLAVOUR_AND_SCALES.md sections 4-5

## Claim
The string tension sqrt(sigma) ~ 0.43 GeV (from the Regge slope, idea
009) and the weak scale v ~ 246 GeV (from G_F, known in 1974) are about
three decades apart. A theory of the QCD string should say why that
distance is moderate, with the remaining parameter dependence stated.
The scale dictionary comes first: v, Lambda in a stated scheme, a
hadronic observable, the confining sqrt(sigma), and any microscopic
string scale are five different quantities.

## Known in 1974
* G_F, hence v. The Regge slope, hence sigma. f_pi.
* Dimensional transmutation: Lambda = M exp[-2 pi/(b alpha(M))].

## What the memory says
* QCD-induced electroweak breaking gives v of order f_pi, far too small
  (Quigg-Shrock 2009).
* Heavy-quark thresholds couple the two scales weakly (Quigg 1997).

## Test
Results already executed by the second line, reproduced here:
* Ordinary QCD breaking would need about seven million QCD-sized
  doublets to supply v.
* At fixed high-scale coupling, Lambda_3 = Lambda_6^(7/9) (m_t m_b m_c)^(2/27):
  the top mass moves Lambda_3 with exponent 2/27, and v with 2/9 if all
  three heavy masses scale with it. The thresholds do not lock the scales.
* One-loop transmutation makes a ratio of order 10^3 natural at
  alpha_s ~ 0.12, with logarithmic sensitivity 7.5 to the coupling.
Still to do:
1. `[pencil]` Express both sqrt(sigma) and v through the same string
   data: in a warped background, two infrared scales from two positions
   along the radial direction, with their ratio fixed by one coupling.
2. `[pencil]` Compute the conversion from Lambda to sqrt(sigma) in the
   same scheme (the second line flags that equating them is a common
   error).

## The 313 MeV nucleon scale against an independent tension (issue #2)

Calculated 26 November 2026 for
[issue #2](https://github.com/arivero/qcdstring/issues/2), following its
closure plan. Program `numerics/nucleon_scale_026.py`, printed output
`numerics/nucleon_scale_026.txt`, hadron inputs `data/trajectories_pdg.tsv`
(PDG database, editions 1996 and 2025, with the identifier of each entry).

The two benchmarks are H_N = (m_p + m_n)/6 = 312.9729 MeV and
H_EW = alpha(0) sqrt(M_Z^2 - M_W^2) = 314.4729(1092) MeV, with M_W =
80.3625(77) and M_Z = 91.1879(20) GeV (PDG 2026 pdgLive evaluations,
archived in arivero/pdghist commit 60b4139) and alpha(0)^-1 = 137.035999.
In string units R_N = H_N/sqrt(sigma) and R_EW = H_EW/sqrt(sigma).

### Conventions fixed before the benchmark was examined

* **Tension.** sigma = 1/(2 pi alpha') from a joint fit of the rho and
  omega leading natural-parity trajectories, J = 1 to 4: rho(770),
  a2(1320), rho3(1690), a4(1970) and omega(782), f2(1270), omega3(1670),
  f4(2050). Common slope, separate intercepts, least squares on M^2 with
  the error scaled by the residual scatter. No baryon enters. Variants:
  each trajectory alone, rho5(2350) added, and the static-potential
  tensions of QCDS-78/1 (0.168 GeV^2) and of the 1975 Cornell fit (0.183
  GeV^2, from memory). The tension is recorded in idea 009.
* **Baryon masses.** Physical (QCD + QED) PDG summary masses, Breit-Wigner
  masses for resonances. The benchmark is the physical average
  (m_p + m_n)/2. An isospin-symmetric QCD mass would differ from it by an
  amount of the order of the 1.3 MeV neutron-proton splitting, 0.14%, far
  below the extrapolation uncertainty found here.
* **Baryon model.** J = a + J_cl(M; sigma, m): a straight string rotating
  with one massless end (the quark) and one end of mass m. In a rotating Y
  the two arms that meet at the junction collapse into a diquark, so m
  carries the diquark mass and the junction rest energy together. m = 0 is
  the classical trajectory (29) of QCDS-86/1. The program reproduces the
  small-mass expansion J_cl = alpha' M^2 [1 - (4 sqrt(pi)/3)(m/M)^(3/2)].
* **Held-out fit.** The intercept a_N comes from N(1680) 5/2+ and
  N(2220) 9/2+ only; the nucleon is then predicted at J = 1/2. The same
  procedure predicts Delta(1232) from Delta(1950) and Delta(2420), and
  Lambda(1116) from Lambda(1820) and Lambda(2350), as controls of the
  low-spin extrapolation.
* **Historical cutoff.** An odd-year article on this subject would be
  dated 1997 with the 1996 edition of the Review of Particle Physics as
  its source cutoff; the column "1996" below uses that edition throughout.
  The column "present" uses the PDG 2025 database for hadrons and the 2026
  W and Z masses. The 313 MeV subunit of the nucleon is in Mac Gregor,
  Phys. Rev. D 9, 1259 (1974). The comparison with alpha(0) sqrt(M_Z^2 -
  M_W^2) belongs to the later record (the 2009 identification cited in
  issue #2); a period paper could evaluate it as arithmetic on period
  inputs only.

### Hadron side: one prediction in string units

| | present | 1996 |
|---|---|---|
| sqrt(sigma), primary fit | 422.8 +/- 4.8 MeV | 433.8 +/- 5.5 MeV |
| sqrt(sigma), meson variants | 416.9-431.6 MeV | 433.4-437.2 MeV |
| a_N, held out, m = 0 | -0.028 +/- 0.015 | 0.115 +/- 0.021 |
| a_B selected by the observed nucleon | -0.285 | -0.246 |
| M_N predicted, m = 0 (median, 68%) | 770 (733-804) MeV | 673 (624-720) MeV |
| **R_N predicted** | **0.607 (0.572-0.641)** | **0.517 (0.474-0.559)** |
| R_N observed, same tension | 0.740 +/- 0.009 | 0.721 +/- 0.009 |
| Delta(1232), predicted/observed | 0.987 | 0.973 |
| Lambda(1116), predicted/observed | 0.925 | 0.868 |

The 68% intervals come from a Monte Carlo over the slope (with its
residual-scaled error) and the masses of the held-out states. Further
systematics, all at m = 0 unless stated:

* Tension choice: the meson variants give M_N = 705-809 MeV (present) and
  647-679 MeV (1996); the static-potential tensions give 854 and 734 MeV
  (present). The free slope through the two held-out states gives 785 MeV.
* End mass and junction: m > 0 lowers the prediction (present: 748, 696
  and 593 MeV at m = 0.1, 0.2 and 0.3 GeV; for m >= 0.4 GeV the trajectory
  no longer reaches J = 1/2). No end mass between 0 and 1 GeV passes
  exactly through both held-out states with a common intercept.
* Inverse check: inserting R_N = 0.728 by hand at J = 1/2 on a massless-end
  line selects a_B = 1/2 - (3 R_N)^2/(2 pi) = -0.259, as found in the issue
  discussion. The held-out intercept is -0.028(15).

**Result.** With the meson tension, the nucleon lies 170 MeV (18%, about
4.8 standard deviations of the held-out prediction) above the
extrapolation of its own trajectory. The same procedure reproduces
Delta(1232) to 1.3% and Lambda(1116) to 7.5%. The end-mass and junction
freedom moves the prediction further down. Within this model R_N is a
predicted number, 0.607 (0.572-0.641), against 0.740 observed at the same
tension. Every variant tried predicts a lighter nucleon; the closest is
the QCDS-78/1 static tension, with predicted/observed 0.909. The period inputs give the same conclusion
with a larger gap.

### Weak side: a continuous family

* H_EW/H_N = 1.004793(349), so R_N/R_EW = 0.995230(346), independent of
  the tension. With the primary tension R_N = 0.7403(85) and R_EW =
  0.7439(85), with correlation 0.9995 from the shared sqrt(sigma); the
  shared error belongs to each ratio and cancels in the quotient.
* Period inputs (PDG 1996: M_W = 80.33(15) GeV): H_EW = 314.9(2.0) MeV and
  H_EW/H_N = 1.0060(65). A 1997 paper could not resolve the present 0.5%
  difference.
* No string data in this repository produce R_EW. At tree level on shell
  sqrt(M_Z^2 - M_W^2) = g' v/2, so R_EW = [alpha(0) g'/2] (v/sqrt(sigma)) =
  0.001277 x 582.4. Three numbers would have to come from the common string
  data: v/sqrt(sigma), g' at the scale where it is fixed, and the running of
  the photon coupling to the Thomson limit, which itself contains the
  hadronic vacuum polarization and hence the QCD scale.
* Two-wall control: with sqrt(sigma) ~ M exp(-k y_1) and v ~ M exp(-k y_2),
  d ln R_EW / d(k(y_2 - y_1)) = -1 at fixed tension. Moving one wall reaches
  any R_EW continuously. The additional datum needed is one relation fixing
  k(y_2 - y_1), the separation of the two walls in string units.
* Threshold control (second line, `notes/FLAVOUR_AND_SCALES.md`, section 4):
  at fixed Lambda_6, d ln Lambda_3 / d ln v = 2/9. With sqrt(sigma)
  proportional to Lambda_3 and alpha(0), g' held fixed, d ln R_EW / d ln v
  = 7/9 and d ln(R_N/R_EW) / d ln v = -7/9. Holding the quotient within its
  measured fractional error 0.000347 would need v/Lambda_6 fixed to
  0.000447. Ordinary QCD supplies the 2/9 and no relation of that kind.
* Held out: H_l = (m_e + m_mu + m_tau)/6 = 313.8499 MeV, R_l = 0.7424 and
  H_l/H_EW = 0.998019. No fit above used it.

### What the test establishes

* The scale test closes with one independent prediction in string units,
  R_N = 0.607 (0.572-0.641), which disagrees with the benchmark, and one
  explicit continuous family for R_EW, whose missing datum is the wall
  separation (with g' and the photon running).
* A common dynamical origin of H_N and H_EW is not established. The 0.5%
  agreement of the two benchmarks is a property of the measured inputs;
  the string dynamics available here misses H_N by 18% and gives no value
  for H_EW.
* Article: the calculation fits in this file and is not registered in
  `OUTPUTS_PLAN.md`. An odd-year article (1997, cutoff RPP 1996) becomes
  worth registering once a weak-side relation exists or once a dynamical
  nucleon offset is derived.

## Expected outcome, and what would refute it
A formula for v/sqrt(sigma) with one stated residual parameter. Refuted
as an explanation if the two scales come from two independently placed
walls or condensates.

## References
QuiggShrock2009, Quigg1997, BHL1990, second_line/astra-6.0/ideas/T13.
