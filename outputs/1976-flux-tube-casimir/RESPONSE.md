# Response to the referee: QCDS-76/1

We thank the second line's referee. The report is right on every major
point. We revised the paper as follows; section and table numbers refer to the
revised version.

The referee's report was written by a fresh agent instructed to act for the
second line. It saw only this folder and the second line's own package,
`second_line/astra-6.0/`, and none of the first line's notes. Astra 6.0 itself
was not consulted.

## Major issues

1. **Correlated fits.** Accepted. All fits in Section 3.4 now use the full
   jackknife covariance (`code/analyze.py`, function `corr_fit`), and Table 6
   lists $b$ against the starting separation. We reproduce the referee's
   numbers: $b = 0.0701(13)$, $\chi^2 = 13.1/4$ for $R = 2$-8, and $0.085(5)$,
   $0.103(17)$ from $R = 3$ and 4. The phrase "7$\sigma$ below $\pi/24$" is
   gone. The abstract and Section 6 now say what the correlated fits support:
   a $1/R$ term of Casimir sign is required at both couplings; its fitted
   coefficient depends on the starting separation; $\pi/24$ is acceptable from
   $R\sqrt\sigma \approx 0.9$.

2. **Endpoint operators.** Accepted. Section 2.1 now names the endpoint term
   $b_1(\partial_x X)^2$ at the two ends and its $R^{-2}$ contribution, and
   says that we know no 1976 argument forbidding it. (One of us remembers a
   later argument from the nonlinearly realized symmetry of the string; as a
   remembered result it carries no weight here, and Appendix B now notes that
   Section 2.1 restates Lüscher 1981 without the ends.) Table 6 adds the fit
   $\pi/24 + d/R^2$, with $d\sqrt\sigma = 0.0111(2)$ and $0.0094(16)$. The paper
   now presents the two readings as equally good and says the data cannot
   separate them.

3. **The local coefficient.** Accepted. The local coefficient now starts at
   $R = 3$, so $V(1)$ never enters; the $R = 5$ value, 0.067(30), is in the
   text; the sentence on "agreement to about 20%" between couplings is
   replaced by a statement that the shortest separations differ by several
   standard errors, which we attribute to the lattice. "Toward the free-string
   value" is removed from Section 6. We note in Section 3.4 that $R = 9$
   ($R\sqrt\sigma = 1.99$) is measured to 3%, too coarse to separate the two
   readings.

4. **Nambu-Goto rows.** Accepted. The square root is now fitted only from
   $R = 3$ at $\beta = 0.73$ ($R\sqrt\sigma = 0.66$) and from $R = 3$ at
   $\beta = 0.70$; no clamping occurs. It fails at $\beta = 0.73$ and fits at
   $\beta = 0.70$ ($\chi^2 = 1.0/2$), as the referee found.

5. **Charmonium.** Accepted. Section 5 now states the model error before the
   fit: the potential's own first-order spin-spin term puts the triplets 47
   and 30 MeV above the spin averages at the parameters of fit (a). Two new
   fits subtract half or all of that shift, recomputed self-consistently
   (`code/charmonium76.py`), and give $\sigma = 0.144$ and $0.146\
   \mathrm{GeV}^2$. The claim is now "0.78-0.86 of the Regge tension". Our
   self-consistent full-shift fit raises $\kappa$ to 0.82 and gives 0.79 of
   Regge, between the referee's two fixed-shift values (0.82, 0.77). The
   $^3D_1$ level is recorded without an error bar, with the note that both
   lines remember its outcome, so it carries no weight.

## Minor issues

1. Table 4's settings ($n_{\rm sub} = 20$, $N_t \le 8$) are stated, and the
   error ratio is corrected to 3.4-11. A direct cross-check at the production
   parameters was run (`code/z2_direct_check.py`, $4\times10^4$ sweeps): $R =
   1$-4 agree with the two-level values within 0.1-1.0 standard errors.
2. The test behind "gains little" is now quoted: mean $|\tanh\beta h| = 0.934$
   at $\beta = 0.73$, $h = 0$ on 4.3% of time-like links, and the pilot with
   and without the one-link average (`results/pilots/pilot2_*.log`).
3. U(1): runs of 2500 sweeps at $\beta = 1.00$ from a hot and a cold start
   (`u1_4d.py two_starts`) converge to the same plaquette, 0.585, with a single
   peak; the autocorrelation time is 12-17 sweeps. The cycle's difference at
   $\beta = 1.00$ came from runs that were too short. The paper now
   establishes the jump and leaves the order open. The starts of the $10^4$
   runs are stated in the caption of Table 7. The Coulomb formula now reads
   $2\alpha/R(R-1)$; the ratio 6:2:1 is unchanged.
4. $\alpha'$ is cited to our 1974 Regge fit [24]. The pilot runs are now in
   `code/pilots/` and `results/pilots/`, with their cost (13.7% of the cap) in
   Table 9.
5. The $\chi$ masses are given as measured to a few MeV, with the $\pm10$ MeV
   allowance on their centre for the spin assignment; $K_c$ is cited to the
   series analyses [25]; the square root (2) is displayed in Section 2.3; the
   abstract gives the total hours (now 98) and drops "beyond $\beta \approx
   0.45$".

## Era discipline

* "Creutz ratio" is replaced by "the ratio $\chi(R,T)$" in the text, the
  figures and the programs.
* The closed form (2) is flagged as remembered (Arvis 1983) and used only as
  a fitting form.
* The universality argument is flagged as a restatement of Lüscher 1981.
* The von Mises sampler is flagged as remembered (Best and Fisher 1979), with
  the referee's estimate of what a 1976 sampler would cost.
* The solver check in `charmonium76.py` now says what it is: a comparison with
  the 1974 shooting code at that code's default inputs, where $\kappa = 0.52$
  is the published value of Eichten et al. 1975 and 3.097 GeV the 1974 mass.
  It checks the solver and is no evidence for anything.
* Appendix B now lists the three conclusions that lean toward remembered
  outcomes: $b \to \pi/24$, the order of the U(1) transition, and the D-wave
  level.

## Budget

With the checks and the pilot runs the programme uses 98.3 of 100 hours.
Appendix A now says the charges are floors, that a 10% underestimate would
overrun the cap by about 8 hours, and that the U(1) loops are where a 1976
group would have saved. The memory footprint fits the 512K-word large core
memory.
