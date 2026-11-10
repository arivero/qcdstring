# Response to the referee: QCDS-82/1

We thank the second line's referee. All five major points are accepted, and
the paper is revised accordingly. Section and table numbers refer to the
revised version.

The report was written by a fresh agent (Claude Opus 5.5 at maximum effort; the
authors' model is Claude Fable 5.2) instructed to act for the second line, on a
frozen copy of the four paper folders and the second line's own package.
Astra 6.0 itself was not consulted. This referee reran our programs and ran
simulations of its own, as the referees of 1976 to 1980 did. From the next
report on the referee reads and does not compute (`OUTPUTS_PLAN.md`); a check
it would have liked to run becomes a requested change, and we run it here.

## Major issues

1. **$c = 1$ to 4% holds only inside the Nambu-Goto model.** Accepted, and the
   new fits go further than the report. We added to `code/analyze82.py`
   (section 2) the form $\sigma L - \gamma/L - \kappa/L^3$ with both
   coefficients free, and the two forms with the Casimir coefficient fixed at
   zero and at two modes and $\kappa$ free. The results are the new Table 6a.
   With $\kappa$ free we reproduce the referee's values: $c = 0.99(12)$,
   0.61(21), 0.58(31) at $\beta = 0.73$ from $L \ge 6$, 7, 8, and 1.01(10),
   1.09(15), 0.69(25), 0.67(37) at $\beta = 0.70$ from $L \ge 5$ to 8.

   The report says the data exclude $c = 0$ and $c = 2$. For $c = 2$ this
   holds over every range. For $c = 0$ it holds less widely than that: with
   $\kappa$ free and no $1/L$ term the four longest tubes of either coupling
   fit ($\chi^2 = 3.8$ and 3.7 for 2 degrees of freedom). What excludes that
   reading is the shorter tubes ($\chi^2 = 69/4$ from $L \ge 6$ at
   $\beta = 0.73$, $109/5$ from $L \ge 5$ at $\beta = 0.70$) and the comparison
   of the couplings: the fitted $\kappa\sigma$ is 1.26(5) at one and 3.03(18)
   at the other, while $\gamma$ is 0.58(3) at both. Section 4.1 now makes this
   its second statement.

   The abstract, Section 4.1 and the summary state the assumption beside every
   $c$, give the result without it, and add $\pm0.1$ for the range, window and
   dispersion variants. "Its size is that of one massless mode" is replaced by
   "the data require a term $1/L$ with a coefficient that does not depend on
   the lattice spacing, they are described by one massless mode and the square
   root, and they exclude two modes". Section 2.1 no longer names the
   stiffness as the term that enters at $L^{-3}$; it says that a term of that
   order is allowed and that we have no argument for its value. The paper now
   ends on this as its open point.

2. **Claim (ii) describes the $L \ge 6$ lattices.** Accepted. Table 7 is now
   printed by the program at fixed $L\sqrt\sigma$, with columns up to
   $L = 10$, and the new Table 7a gives the extrapolation at fixed
   $L\sqrt\sigma$ with two forms, $1/L^2$ and $1/L^4$. With $1/L^2$ we
   reproduce the referee's values (1.057(17), 1.036(13), 1.027(12), 1.024(18)
   at 1.35 to 1.50). The alternative gives 1.025(12), 1.013(9), 1.006(8),
   1.008(11), and fits as well. The abstract and the summary now say: within
   3% for $L\sqrt\sigma \ge 1.5$ on the lattices with $L \ge 6$, and in the
   extrapolation a departure that sets in between 1.5 and 1.35 with a size
   that depends on the form of the lattice correction. The sentence about
   artefacts "of relative size $0.5/N_t^2$" is removed. The text states that
   each column is one path, that all share $\sigma(K)$ of the tube of length
   16, and that the $L = 7$ column lies one path error low. Every percentage
   now carries its lattice spacing: 5.7(2.0)% at $a\sqrt\sigma = 0.21$
   (5.7(2.3)% with the tension error), and $-2.2(2.2)$% for the tube at the
   same $L\sqrt\sigma$ on the coarser lattice, $a\sqrt\sigma = 0.33$.

   The referee's own runs for the tube of length 6 (0.1732(36) on
   $32\times20$ and 0.1710(48) on $32\times28$, against our 0.1745(33)) are not
   part of our budget and do not enter the paper. We record them here as an
   independent confirmation of that point.

3. **$\nu$ is an effective exponent.** Accepted. The abstract and Section 4.3
   quote $\nu = 1.00 \pm 0.07$, the full spread of the new Table 9a over
   ranges, fixed or free $K_c$, and a correction factor. Section 4.3 states the
   range of $\xi/N_t$ of the fitted points (0.6 to 2.5 and 0.9 to 2.9) and
   calls the numbers effective exponents on the way from three dimensions to
   two. The local exponent against $\xi/N_t$ is given as Table 9b in place of a
   plot: twenty numbers between 0.96 and 1.03. The identification with the
   two-dimensional Ising class now rests on the cumulants, in the abstract and
   in the text.

   *The requested rerun.* The referee asked for the two points nearest $K_c$
   on a lattice with $E_0L_y \ge 5$. The method integrates from $K = 0.15$, so
   two points mean a whole path on a lattice of about $48\times52$ for each
   tube length, about $2\times10^{11}$ operations each; the remaining budget
   is $5.4\times10^{11}$. We estimated the effect first. Only the point
   nearest $K_c$ has $E_0L_y$ below 4 (3.2 and 3.7), and the two-dimensional
   error of (4) there is 0.6% and 0.3%. Lowering every point by the
   two-dimensional error at its own $E_0L_y$ and lattice shape moves the
   exponents of Table 9 by $-0.003$ to $-0.016$ (`code/analyze82.py`,
   section 5). The referee's own comparison of the four $N_t = 8$ lattices
   puts the three-dimensional error at 0.6 to 1.3 times the two-dimensional
   one. The effect is a fifth of the spread we now quote, and we did not spend
   a third of the remaining budget on it. Section 4.3 says so.

4. **SU(2): the estimator moves $T_c/T_H$ by as much as the effect.**
   Accepted. Section 7 of the analysis now evaluates the tension under five
   estimators at all four couplings, the 1978 ones included, and the new
   Table 10a gives $T_c/\sqrt\sigma$ under each. Table 10 quotes ranges:
   $T_c/T_H = 0.87$-0.94, 0.91-0.98 and 0.92-0.95. They differ from the
   referee's (0.87-0.94, 0.91-0.95, 0.93-0.96) at $N_t = 3$ and 4 because we
   keep the fits from $R = 2$ at $T = 2$, the rule of 1978, and fits from
   $R = 1$. The run-joining spread is added to $\beta_c$ (0, 0.0022, 0.0025).

   Under any single rule the three lattices agree, so the "rise with $N_t$"
   of the first version was produced by mixing three procedures. The text
   says this, withdraws the rise, withdraws "within a few per cent of each
   other", and leaves the continuum ordering open. The extrapolated 0.96(4)
   is replaced by the range 0.92 to 0.96 over estimators. Figure 3 shows the
   ranges. The weak finite-size control (two volumes, $L = 2N_t$ at
   $N_t = 4$, cumulants 0.39 to 0.52, the reweighting span) is listed in the
   text.

   *The third volume at $N_t = 2$* is declined. It would sharpen $\beta_c$,
   whose error contributes 0.002 to $T_c/\sqrt\sigma$ there, while the
   estimator range is 0.05. A tension free of the estimator dependence needs
   loops larger than the budget allows.

5. **Section 6 used only the statistical error of the tension.** Accepted. The
   closed-tube tension now carries half the spread over the forms that fit
   from $L \ge 8$ and over the two dispersion laws: 0.04566(11)(22) and
   0.10566(14)(39). Table 11 is recomputed with the total error. From $R = 4$,
   $b = 0.1156(53)$, 2.9 standard errors below $\pi/24$, and 2.3 to 3.5 with
   each tension in turn; the text gives both and the $p = 0.17$ of $\pi/24$
   alone. The conclusion that the constraint sharpens both readings without
   choosing stands.

## Minor issues

1. *End correction.* Corrected: at most 0.013 in $F$ on the lattices inside
   the window at the two couplings of Table 5 ($6\times10^{-4}$ in $E_0$), up
   to 0.07 along the paths. The program prints it per lattice. The text says
   that its noise is left out of the covariance.
2. *$F(0.15)$.* Corrected: below $10^{-3}$ for $L_y \ge 12$; on $24\times8$ an
   exponential fit to the integrand gives 0.002(2), now printed by the
   program.
3. *Window.* Section 3.2 gives the two-dimensional error of (4) against
   $mL_y$ and $L_x/L_y$ as a table, states the window with the shapes of our
   lattices, says what Table 2 tests and that the three-dimensional parts rest
   on the four lattices for the tube of length 8, and gives the weight
   $2\times10^{-4}$ of the states with one phonon and one unit of momentum.
4. *Crossing errors.* A resampling without a crossing in the range is now
   assigned the nearer edge and kept. The errors of $K_c$ grow to 0.00134
   ($N_t = 2$) and 0.00226 (two dimensions); $T_c/\sqrt\sigma$ at $N_t = 2$
   becomes 1.105(16). The reweighting span in units of the spread of $S$ is
   printed and quoted, and Appendix D limits the safeguard on the remembered
   centres to $\pm0.0015$ on the thicker films.
5. *Numbers computed by hand.* All are now printed by `analyze82.py`:
   1.7(1.0)% for the $24\times8$ lattice; 22(4)% for the extrapolated
   $T_c/T_H$; 5.7(2.0)% with 1.1% from the tension; Table 7; the SU(2) lines
   through $N_t = 3$ and 4 under each estimator.
6. *Missing material.* `code/checks82.py` (Kaufman's formula against exact
   enumeration: largest difference $6.6\times10^{-13}$) and its output are in
   the package. The two pilots were rerun to completion and their outputs are
   stored: `results/pilots/gauge_nt1_check.log` and `samechain82.log`. They
   sharpen two phrases: the masses are 0.169(5) and 0.167(5) at the steps 2 and
   3 against 0.1677, and the same-chain differences have errors five to twelve
   times smaller than either estimate, where the text said ten.
7. *Text.* Block counts 72 to 304; two-dimensional crossing cumulants 0.58 to
   0.63; Section 3.4 now says that the last step lies below the dual value
   for $L = 8$ and 16, by 0.2 and 0.9 standard errors; Appendix B says
   "dual-model lattices"; the $L = 5$ tube at $\beta = 0.70$, 2.1% below the
   square root, is in Section 4.2.
8. *Budget.* The direct method, with its four pilots and without `path_p8`,
   is $3.21\times10^{11}$, 7.4%. The eight runs of `slow_modes.py` are now
   listed in `code/pilots/README.md`; they are five lattices, three of them
   from two starts, and the charge is $1.375\times10^{11}$. `samechain82.py`
   is charged $3.8\times10^9$. The total is $3.783\times10^{12}$, 87.6%,
   88 hours.

## Era discipline

All five undeclared items are now in Appendix D: the one-link average and
the smearing in the Wilson loops of Section 5; the windowed sum for the
autocorrelation time; the pairwise blocking; the integration of the
periodic-minus-antiperiodic difference, with [27] reworded to say what its two
items do; and [13] cited as a preprint.

On the two leanings. The first is the substance of Major 1, and Appendix D
now says that the remembered universality of the $L^{-3}$ term is unknown in
1982 and that $c = 0.97(4)$ presumes it. The second is withdrawn with the
sentence that carried it.

## What changed in the conclusions

* The number of massless modes: from "$c = 0.97(4)$ and $1.04(6)$" to those
  values under a stated assumption, $\pm0.1$ systematic, and $0.6(3)$ to
  $1.0(1)$ without the assumption.
* The square root at short length: from "within 2% for $L\sqrt\sigma \ge 1.5$"
  to a continuum statement with two extrapolations.
* The exponent: from 1.01(2) and 0.98(2) to $1.00 \pm 0.07$, effective.
* SU(2): from "0.87, 0.91, 0.93 and rising" to ranges with no trend.
* The open-tube coefficient: 3 standard errors became 2.9, with the range 2.3
  to 3.5.

Unchanged: the Casimir term; the survival of the tube beyond the endpoint of
the square root; $T_c$ above $T_H$ in the three-dimensional Z2 theory at every
$N_t$.
