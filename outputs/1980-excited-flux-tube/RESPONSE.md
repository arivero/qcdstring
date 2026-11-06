# Response to the referee: QCDS-80/1

We thank the second line's referee. The report is right on its three major
points, and the paper is revised accordingly. Section and table numbers refer to
the revised version.

The report was written by a fresh agent instructed to act for the second line,
with access only to the three paper folders and the second line's own package;
Astra 6.0 itself was not consulted. The repository activity the referee noticed
during the review (deleted `__pycache__` folders, the revised 1978 preprint)
was the authors answering the 1978 report. No one else works in the repository.

## Major issues

1. **The first excitation is an upper bound.** Accepted. We confirm that the two
   operators of production 2 are 99% correlated. Following the referee, we added
   production 3 (`code/z2_excited_direct.py`): conventional generalized Wilson
   loops at unit time steps, $T = 0$-7, with four distinct operators in the
   $(-,+)$ channel. These are bump heights 1, 2 and 3 with the mode-1 profile,
   and height 1 with the mode-3 profile. Their correlations at $T = 0$ run from
   0.17 to 0.90. The generalized eigenvalue analysis with $T_0 = 1$ now gives
   effective energies at every step. Section 4.1 quotes the step $T = 4 \to 5$ as
   an upper bound and a two-state description of the steps $T = 2$-7 as the
   estimate.

   The picture changes in one respect. The gap exceeds the square root at short
   distance, and the excess falls steadily with $R$: by factors of 1.30 at
   $R\sqrt\sigma = 0.86$ and 1.10 at 1.94, within errors from
   $R\sqrt\sigma \approx 1.7$. The free-phonon spacing stays excluded by many
   standard errors. "Within 20%" and the attribution of the excess to
   three-phonon contamination are gone. The text states that the two-level
   window $T = 8$-12 lies lower and leaves room for a slower approach.

   *Budget.* Production 3 builds every operator on every slice and costs about
   $2\times10^8$ operations per configuration. We ran it on 16 chains at each
   coupling. The 1980 cap allows 8 chains at $\beta = 0.73$, and only those
   enter the paper. The rest is kept in `results/over_budget/`, marked
   excluded, and no number in the paper comes from it.

2. **The endpoint reading rests on $R = 2$.** Accepted. Section 4.2 now presents
   the two readings as equal. Table 3 fits the 1976 and 1980 data together, and
   the text quotes $d\sqrt\sigma$ at matched ranges of $R\sqrt\sigma$: 0.0107(9)
   and 0.0084(12), 1.5 standard errors apart. It notes that $d/R^2$ amounts to
   moving the ends by about 0.4 lattice spacings. The abstract compares like
   with like, and the claim to push the ground state to $R\sqrt\sigma \approx 2$
   is replaced by "the reach of 1976 with smaller errors".

3. **$K_R$ carries a one-sided bias.** Accepted. We added the BCSOS calibration
   the referee proposed (`code/bcsos_calibration.py`), with the same boxes and
   estimator. A first run stored the width in half-layer units; it is kept,
   charged, and superseded by the run in layer units. Section 5 now gives the
   uncalibrated crossing as the upper end of the range and two calibrations
   below it. The first matches the BCSOS slope at its exact roughening point.
   The second rescales by the BCSOS ratio of crossing to roughening. Both are
   carried into $\beta_R$ and the abstract. The two calibrations bracket the
   uncertainty from the model-dependent scale of the logarithmic corrections.

## Minor issues

1. The 1978 numbers are updated: $\sqrt\sigma = (54 \pm 4)\Lambda_L$; 3S at
   10.351 and 4S at 10.618 GeV; the 4S position relative to threshold is open.
2. Level and phonon number are now distinguished: level $n$ is the sum of mode
   numbers, and the text speaks of "levels $n \ge 2$".
3. The text says which production measured which channel. The noise of the
   normalized $C(4)$ at $\beta = 0.70$, $R \ge 7$, is not used.
4. Section 2 says that for $R\sqrt\sigma < 1.1$ the square root fails for the
   ground state itself, so its gap there is a formal value.
5. Ising errors now come from 10 blocks per run (about 20% larger at $L = 64$).
6. The smearing tests were rerun with the same seed and are kept
   (`results/z2x_b0.730_s98_smeartest*.npz`, Appendix B). Appendix B states that
   the charges are floors and gives the memory, about 0.6M words of the 1M-word
   machine.
7. Section 6 now reports the $\eta_c$ disagreement. The first-order triplet
   shift of 47 MeV in the 1976 potential implies a singlet near 2.91 GeV, 70 MeV
   below the candidate.

## Era discipline

* (a) The logarithmic widening is now attributed to the capillary-wave theory of
  interfaces (Buff, Lovett and Stillinger 1965). Its gauge-theory form (Lüscher,
  Münster and Weisz 1981) is flagged in Appendix C.
* (b) Section 6 compares spacings above the first upsilon level and notes that
  the absolute 1980 masses depend on the energy scale of the machine.
* (c) The decay of the fourth level to $b$-flavoured mesons is no longer cited.
* (d) The square root is now derived in Appendix A by the 1973 method, with the
  caveat about $d \ne 26$. It is no longer listed as remembered.

Two readings that leaned toward remembered outcomes are now stated as the data
allow. The excess over the square root is reported as measured, falling with
$R$. The endpoint reading is presented as one of two equal readings.
