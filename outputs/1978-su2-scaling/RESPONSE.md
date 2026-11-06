# Response to the referee: QCDS-78/1

We thank the second line's referee. The report is right on every major point;
the paper is revised as follows. Section and table numbers refer to the revised
version.

The report was written by a fresh agent instructed to act for the second line,
with access only to this folder, the 1976 preprint and the second line's own
package; Astra 6.0 itself was not consulted. The stray
`code/__pycache__/analyze78.cpython-314.pyc` the referee noticed came from the
authors, who imported `analyze78.py` while preparing correlated fits during the
review; the 1976 preprint was revised in answer to its own report during the same
period. No one else works in the repository.

## Major issues

1. **No leverage for the scaling test.** Accepted. Section 5 now says that
   between $\beta = 2.4$ and 2.6 the two-loop factor moves $a\Lambda_L$ by 3.4%
   relative to one loop, less than half the error of a point; that the one-loop
   ratios (166, 161, 173) are as flat as the two-loop ones; and that the data
   are consistent with a constant and cannot test the two-loop form. The abstract
   and summary say the same. $\sqrt\sigma = (54 \pm 4)\Lambda_L$, $\Lambda_L
   \approx 8$ MeV and $a = 0.088$ fm now carry an explicit unknown factor for the
   remaining approach to scaling.

2. **Hand-made choices.** Accepted. Table 4 now lists four analysis choices at
   $\beta = 2.4$-2.6: $e$ free at $T^*$; $e = \pi/12$ at $T^*$; $e$ free at the
   latest usable $T$; and a window matched in $R\sqrt\sigma$ (0.4-1.4). The
   ratio lies between 50.5 and 58.2 under all of them, with no common trend. The
   time-separation error is now one-sided (Table 3), since the effective
   potential approaches its limit from above. With the new blocking and
   thermalization (item 3) the variants differ from the referee's numbers by up to
   2 units; the conclusion is the one the referee drew.

3. **Errors too small.** Accepted. Errors now come from blocks of at least four
   integrated autocorrelation times (`make_blocks` in `code/analyze78.py`): 6
   blocks at $\beta = 2.5$, 5 at 2.6; the error on $\sigma$ at 2.5 grows from
   0.0013 to 0.0024. We discard the first quarter of the measurements at
   $\beta \ge 2.4$; at 2.6 this raises the tension from 0.0227 to 0.0250, as the
   referee found. A hot start at $\beta = 2.5$ (on $12^4$, see item 4) reaches
   the same plaquette, 0.65207 against 0.65188.

4. **Finite volume.** Accepted; our sentence had the wrong sign. We ran
   $\beta = 2.4$ on $8^4$ and $\beta = 2.5$ on $12^4$ with the paper's code
   (`su2_runs.py fv`). At 2.5 the smaller box ($L\sqrt\sigma = 2.3$) lowers the
   tension by 14-19% over $R = 2$-6; at 2.4 the $8^4$ value agrees with $12^4$
   within its 12% error. Section 5 now states these measurements, cites the
   referee's $\beta = 2.6$ check, and says that our $\beta = 2.6$ point may be
   biased low, which would raise its ratio.

5. **The $1/R$ coefficient.** Accepted. Section 6 now gives $e$ at $T^*$ and at
   the latest $T$ (0.24-0.33), the correlated $\chi^2$ for $e = \pi/12$ (rejected
   at 2.4 and 2.6, acceptable at 2.5), drops the Z2 analogy, and says that the
   Casimir share stays open.

6. **Section 7.** Accepted throughout.
   (a) "The prediction holds" is gone; the $\psi(3772)$ is a consistency record.
   (b) Table 5 lists all four 1976 potentials; the two with the spin-spin shift
       overshoot $\Upsilon' - \Upsilon$ by 27-28%, which the text now says.
   (c) The threshold is given with and without the $D^* - D$ splitting (10.567
       and 10.720 GeV), with the kinetic-energy correction in the opposite
       direction; "4S broad" is replaced by "undetermined".
   (d) The remembered spectra are listed in Appendix B. We adopted the
       referee's joint fit to $\psi$, $\psi'$, $\Upsilon$ and $\Upsilon'$ and
       reproduce it with our code: $\kappa = 0.515$, $\sigma = 0.168\ \mathrm{GeV}^2$
       (0.91 of Regge), $\chi_c$ centre 3.510 GeV against 3.522.

## Minor issues

1. The abstract and Section 3 now say the tension leaves the series at
   $\beta \approx 1.7$-1.9, before the fluctuation peak.
2. Section 3 notes that the specific heat comes from one volume and that the
   $8^4$ box is small for $\beta \ge 2.4$; the maximum is read as a crossover mark
   only.
3. The switch from $\chi(3,3)$ to fits is marked in Section 4, with the 15%
   difference at $\beta = 2.2$.
4. $a = 0.088$ fm; the width of the $\psi(3772)$ is $28 \pm 5$ MeV; the
   registered half-widths now come from the joint fit.
5. `analyze78.py` keeps the initial values of $T$ only as a starting point for
   blocking (commented); Figure 3 shows all four variants with their errors.

## Era discipline

* "Creutz ratio" is replaced by "the ratio $\chi$" in the text.
* The remembered spectra are flagged (Appendix B); Section 7 draws no evidence
  from them.
* Appendix B now states how ledger item P13 chose the couplings, and that the
  data neither confirm nor refute its scaling half.
* Appendix A now states the storage scheme: the $12^4$ field fits the large core
  memory; the $16^4$ field streams from disk one time slice at a time, and we
  charge a tenth of those runs for the transfers. The smearing levels were set
  by a rule, without pilot runs; the program checks are charged. The 3.3 Mflop/s
  figure is flagged as remembered. The total is 95 of 100 hours.
