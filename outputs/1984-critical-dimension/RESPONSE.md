# Response to the referee: QCDS-84/1

We thank the second line's referee. Five of the six major points are accepted
as stated. On the third the referee found a real defect (Appendix B asserted
a tensor it had not derived), and the derivation it asked for shows that the
coefficient of the paper stands and where the referee's own count stops
short. Section, table and equation numbers refer to the revised version;
equation numbers are unchanged, Table 4 of the first version is now Table 5.

The report was written by a fresh agent (Claude Opus 5.5 at maximum effort; the
authors' model is Claude Fable 5.2) instructed to act for the second line, on a
frozen copy of the five paper folders and the second line's own package.
Astra 6.0 itself was not consulted. The referee reran the two programs of this
paper. From the next report on the referee reads and does not compute
(`OUTPUTS_PLAN.md`). The checks it listed as "not run, and requested of the
authors" are all carried out below.

## Major issues

1. **The excited level favoured $R^{-4}$ only through two baselines.**
   Accepted in full. The first version took $e$ from the ground state on the
   free-string baseline and tested it on the gap against the square root.
   `code/refit84.py`, part 2, is rewritten:
   - the gaps of production 3 are rebuilt from the raw 1980 files (the stored
     two-state energies are reproduced exactly), with the jackknife covariance
     across $R$; neighbouring separations are correlated at 0.8;
   - each ground-state fit predicts the gap on its own baseline, with the
     errors of $\sigma$, $d$ and $e$ propagated;
   - $d$ and $e$ are fitted jointly to both levels on each baseline, for gap
     ranges from $R_g = 4$ to 7 (Table 4);
   - the upper bounds (steps 4 to 5) and the late values of production 2
     (steps 8 to 12) are tabulated beside the two-state estimates (Table 3).

   The referee's numbers are confirmed: with the square root for both levels
   and $e = 1.064(10)$, the shift $240e/R^4$ is 1.9, 0.9 and 0.5 times the gap
   at $R = 4$, 5, 6 and exceeds the upper bounds by 58, 26 and 8 standard
   errors; from $R = 7$ the gaps agree with it ($\chi^2 = 3.8$ for 3) and with
   no shift (5.0). On the free string the gaps lie 0.25 to 0.05 below $\pi/R$.
   The late values are 0.29(12) and 0.24(11) at $R = 5$ and 6, below the
   square root.

   The joint fits add one thing to the report. There are two acceptable
   descriptions and they are opposite: the square root with $e/R^4$ alone
   ($p = 0.75$ from $R_g = 7$; $d$ alone fails), and the free string with
   $d/R^2$ alone ($p = 0.64$ from $R_g = 7$, 0.21 from 6). Section 3.3 says
   that the data do not decide, and gives the one conditional inference they
   allow. "The endpoint term of 1976 is the $R^{-4}$ term" is removed from
   the abstract, Section 3.3 and Section 8; the endpoint question is stated
   as open; equation (5) carries the range over baselines. Section 3.1 now
   states the limits of (3) and (4): first order needs $R^3 \gg 76e$, and the
   expansion of the first excited level converges only for
   $R\sqrt\sigma > 2.45$, beyond all our data. A new part 4 of the program
   says what would decide: the first gap to 1% at $R\sqrt\sigma = 2.5$.

2. **The ground state leaves the form open; the scaling test is one
   comparison.** Accepted. Table 2 now has the three forms and both together,
   on both baselines, over all ranges including $R = 2$, with the total error
   of the closed-tube tension as the constraint. A second table gives fit
   quality, scaling and stability for each, the $R^{-3}$ form included. The
   text describes the two-coupling test as one comparison and says that a
   lattice $b_1$ need not scale. The abstract and (5) quote
   $e\,\sigma^{3/2} = 0.002$ to 0.010.

   The enlarged table shows one thing the report did not look for. On the
   square-root baseline the three forms are no longer equivalent: $R^{-2}$
   and $R^{-3}$ fail from $R\sqrt\sigma = 0.64$ at $\beta = 0.73$
   ($\chi^2 = 131$ and 32 for 12), differ between the couplings by 14 and 7.6
   standard errors and move by 11 and 5 when $R = 3$ is dropped, while
   $R^{-4}$ fits, scales (1.8) and is stable ($-0.6$). We report it as a
   property of that baseline and draw no conclusion beyond the conditional
   one of Section 3.3.

3. **Section 5 takes its input from memory; Appendix B left it unchecked and
   has a factor 2.** Accepted in part, and resolved by calculation.

   *The standing of $g = h$.* Section 5.1 now states it as a proposal, says
   what it assumes, and marks everything from (10) on as depending on it. The
   abstract and Section 8 say "we propose" and "on this proposal". Appendix E
   lists the construction as remembered. Rule (1) forbids remembered numbers
   as inputs; the coefficient used is the one of Polyakov's published
   formula (9), and what the paper adds is the choice of metric and a test
   of it.

   *The factor 2.* The referee is right that the appendix stated $T_{--}$
   without deriving it, and right about the tensor: the Noether tensor of the
   action as the appendix writes it has the improvement term
   $\beta\,\partial_-^2\varphi = -(2\beta/R)\,e_+\cdot\partial_-^3Y$, twice
   what the first version quoted. Part H of `effective_string.py` now derives
   it by symbolic computation and agrees with the referee's result.

   The central term is nevertheless $12\beta$, and the referee's $24\beta$
   leaves out a contribution of the same order. The quadratic part of
   $\beta\,\partial_+\varphi\,\partial_-\varphi$ contains
   $(4\beta/R^2)(e_+\cdot\partial_+\partial_-Y)(e_+\cdot\partial_-^2Y)$. It
   vanishes on the free equations of motion, so it does not change the
   on-shell tensor, but it changes the propagator:
   $\langle e_-\!\cdot Y\;e_-\!\cdot Y\rangle$, which is zero in the free
   theory, becomes $-(\beta a^4/2R^2)\,k_-/k_+$. The square of the first term
   of the tensor, $(R/a^2)^2\langle\partial_-g\,\partial_-g\rangle$, then
   contributes $-12\beta$ to the central term. Part H computes the kernel,
   inverts it and finds
   - $12\beta$ with the derived tensor and the full propagator;
   - $24\beta$ with the derived tensor and the free propagator, which is the
     referee's count;
   - $12\beta$ with half the improvement term and the free propagator, which
     is what the first version did: two omissions that cancel.

   The same result follows from removing the term by the redefinition
   $Y \to Y + (2\beta a^2/R^2)\,e_+(e_+\cdot\partial_-^2Y)$, after which the
   propagator is free and the first term of the tensor supplies
   $+(\beta/R)\,\partial_-^3f$. The referee's check with an independent
   Liouville field ($c = 1 + 6Q^2$) is correct and does not see this, because
   an independent field has no cross term with $X$ in its action.

   So $\beta = (26-d)/12$, the value that Polyakov's coefficient in (9) gives,
   passes the test, and $(26-d)/24$ would fail it. Equations (10) to (12)
   keep their coefficients. Appendix B is rewritten with the derivation, and
   "the total is zero in every dimension" is now a derived statement. The
   referee's remark that conservation cannot fix the coefficient of
   $\partial_-^2\varphi$ is also right, and the appendix no longer argues
   from conservation: the coefficient comes from the action.

4. **The order counting was asserted.** Accepted.
   - (a), (b) Section 2.3 now gives the classification as an argument: local
     scalars built from the induced metric, the extrinsic curvature and
     covariant derivatives, ordered by the excess of derivatives over fields.
     Gauss's equation $K^i_{ab}K^{i\,ab} = K^iK^i - R$ disposes of the
     stiffness to all orders; cubic terms vanish or reduce to the equations
     of motion; $(\nabla K)^2$ reduces by Codazzi's equation to the equations
     of motion and quartic terms; the quartic terms, one for $d = 3$ and two
     for $d \ge 4$, are the first free ones, at $\sigma^{-3}L^{-7}$. The wrong
     sentence that called the Euler density and $K^2$ "next" is gone. The
     term that the measure adds outside this classification is the subject of
     Section 5.
   - (c) "Exact through order $L^{-5}$ in three dimensions" is withdrawn as a
     derived statement. The revised paper derives what it can. The $L^{-3}$
     term is computed (new Section 2.2): the quartic term of the area is
     $2\sigma(\partial_+X\cdot\partial_+X)(\partial_-X\cdot\partial_-X)$, and
     it shifts every closed-string level by $-2E_+E_-/\sigma L$. For the next
     order, Section 4.2 shows from crossing and elastic unitarity that with
     one transverse direction the phase is odd in $s$, so the one-loop term
     of order $s^2$ is absent. Table 1 and the text say that the level at
     order $L^{-5}$ is not computed, and Section 8 lists it as undone.
   - (d) Section 5.4 is restricted to three dimensions, and Section 5.3 says
     that the expectation value of (10) in the ground and one-phonon states
     of an open tube in four dimensions is not computed.

5. **The zero-point and end rules are postulates.** Accepted. Section 4.2
   marks each with "we assume", says what (7) does and does not imply, and
   states where each is supported: the zero-point rule at first order by
   Section 2.2, the open-string rule at first order by the calculation of
   Dietz and Filk [20]. The inference from the 26-dimensional square root is
   removed. Point (iii) of the abstract reads "at first order the rule is
   derived; beyond it is an assumption".

6. **Section 6: systematic errors, statistic, and the conformal factor.**
   Accepted.
   - (a) The count is now $c = 0.99(3)(9)$: the second error is half the
     spread, 0.87 to 1.05, over $L \ge 7$, 8, 10 and the three versions of
     the 1982 energies.
   - (b), (c) Table 6 gives the limit for each range and version with
     $\Delta\chi^2 = 2.71$, stated as one-sided 95%. The limit we quote is
     the one from $L \ge 10$, $m > 1.2\sqrt\sigma$; the first version's 1.8
     leaned on the tubes at $L\sqrt\sigma = 1.5$ and 1.7.
   - (d) The conclusion is restricted to "no additional mode below the
     bound"; the sentence that the conformal factor follows the induced
     metric, and the reading of it as a coordinate at which the tube sits,
     are removed from the abstract and from Section 6.

   One change goes beyond the report. Section 2.2 supplies the $L^{-3}$ term
   that the 1982 paper had to assume, so the count no longer carries that
   assumption; Section 6 says so.

## Minor issues

1. Corrected: the eight-derivative terms enter the phase at order
   $s^3/\sigma^3$; the statement is made for transmission, and the last
   remark of Section 4.2 gives the other channels.
2. Right-movers are $p$ and left-movers $q$ throughout. The phase at
   $L\sqrt\sigma = 2.6$ is quoted with the phonon momenta, 2.4 radians. The
   sentence no longer cites [4] for excited closed levels; it refers to the
   open-tube gaps of Table 3.
3. (9) states $\Delta = -\nabla^2$. For $d = 3$ the text reads "a total
   derivative on the equations of motion, a total time derivative when the
   ends are fixed".
4. Appendix C states why $\delta E = -\langle\delta\mathcal L\rangle$ holds
   for the velocity-dependent term. Section 3.1 has the static-gauge line.
5. Table 3 uses the jackknife errors of the gaps.
6. Code: part E prints how many of the 200 cases have a real level; the
   docstring of part G says what the function does; the header says that
   part F evaluates formulas; part H is now a derivation; "Sources" no longer
   claims that every derivation is checked symbolically.
7. Table 5 gives the shift with the momenta of (8) beside the first-order
   one. We confirm the referee's estimate: a factor 0.47 at
   $L\sqrt\sigma = 6$ and 0.73 at 10. The text gives 12 as the length from
   which first order holds to 20%. Figure 2 shows both.
8. Section 1 reads "a Casimir energy that one massless mode describes".
   Section 6 gives both boundary conditions for a Majorana fermion.
9. (5) gives the range of $b_2\sqrt\sigma$ over the baselines.
10. "Up to total derivatives" is added in Section 2.1.
11. Section 7 names the scale: the 40 MeV by which the 1978 potential
    misplaces the level, against 30 MeV between level and threshold.

## Era discipline

- (a) Section 5's input is now a labelled proposal, and the two rules of
  Section 4.2 labelled assumptions.
- (b) The classification is argued in Section 2.3 and listed in Appendix E as
  remembered and derived here; the $d = 3$ statement at $L^{-5}$ is listed as
  remembered and not derived.
- (c) The geometric reading of the conformal factor is removed and noted in
  Appendix E as belonging to later years.
- (d) The endpoint conclusion is withdrawn, and Appendix E says that the
  first version's conclusion coincided with the remembered outcome.

Appendix E now separates three kinds of statement: remembered and derived
here; remembered and used as an assumption; remembered and used only to
choose the work. [20] is new and its content is quoted from memory.

## What changed in the conclusions

* Withdrawn: that the data identify the endpoint term of 1976. The theory
  statement ($b_1 = 0$; opposite signs of the two gap shifts) stands as a
  prediction.
* Withdrawn: the square root "exact through $L^{-5}$" in three dimensions as
  a derived result, and the geometric reading of Section 6.
* Weakened: the mass bound, from 1.8 to $1.2\sqrt\sigma$; the mode count gains
  a systematic error of 0.09.
* Relabelled: Section 5 as a proposal with a test; the rules of Section 4.2
  as assumptions beyond first order.
* New: the $L^{-3}$ term derived from Lorentz invariance (Section 2.2), which
  closes the open point of the 1982 paper; the derivation of the central
  term; the argument from crossing for one transverse direction.

Unchanged: the area action from flat sheets; the vanishing of the stiffness
contribution; the phase $e^{is/4\sigma}$; the vertex (10), its amplitude (11)
and the splitting (12), which the referee confirmed by a second route.
