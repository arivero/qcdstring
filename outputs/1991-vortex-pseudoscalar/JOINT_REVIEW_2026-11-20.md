# Review: qcdstring (final version, 20 November 2026)

**Reviewers.** First review: Claude Opus 5.5, 19 November 2026. Second referee: Claude Fable 5.2 (xhigh), 20 November, read-only, hand derivation only. This final version merges both and was checked against the repository at the state below.

**Repository state this review matches.** `main` = `origin/main` = `246f436` (20 Nov 19:29), working tree clean. The science is unchanged since the reviewed commit `766b845` (18 Nov, "1991: Match the pseudoscalar pole on an Abelian Higgs vortex"). The three later commits only add the no-pull-request rule to `AGENTS.md` and one `.gitignore` line.

**Scope.** Commit `766b845`: the side paper QCDS-91/S1 in `outputs/1991-vortex-pseudoscalar/` and the 1990 amplitude note `outputs/1990-pseudoscalar-curvature/amplitudes.md`. The second referee also covered the 1986 paper, the 1988 paper (commit `ecca678`) and the 1990 note, which had no effective referee.

## Verdict

**No wrong result was found by either referee.** Every equation re-derived by hand holds in the 1991, 1990, 1988 and 1986 papers. One external number disagrees with the 1991 paper by a factor of 2 and is still unexplained (action 1). The other findings concern prior-work credit, novelty labelling and process.

Review status of the work: AI review only. The repository's own referee read the text and ran nothing (`outputs/1991-vortex-pseudoscalar/REFEREE.md:7`, "I performed no numerical or symbolic execution, builds, simulations, or file edits."). No human review exists.

## Open actions, ranked

Paths below are relative to `outputs/1991-vortex-pseudoscalar/` unless a full path is given. Nothing in this list has been applied in the repository.

### 1. A published coupling is twice the paper's value (medium-high, unresolved)

- arXiv:2603.05243 (March 2026) writes the curvature coupling at $\lambda=e^2$ as $\kappa=\pi\int(\rho^2f'\varphi+\rho\alpha'a)\,d\rho\approx-0.7646\pi$. The second referee reports this from the preprint. Neither referee has read its eq. (29) line by line.
- The same referee derived that formula independently and converted the paper's vertex into it: $|\kappa|=\mathcal I/m_*=\alpha/\mu=0.38230\pi$, exactly half.
- Three derivations in the paper and its stored finite-difference check support the paper's value. A normalisation difference in the preprint is the likely cause; nobody has confirmed it.
- **Action:** read eq. (29) of the preprint and settle the factor. Cite the preprint in the retrospective note (`paper.md:471`).

### 2. The flux-overlap integral has a precedent in ref. [4] (medium)

```
paper.md:469
We have no prior value for these matrix elements in the conventions of [1]
to use as an input or a check.
```

Arodź 1991 (ref. [4], scan p. 518) has $M^{12}=4\pi\sum W^0\int\rho\,\varphi_l(H'+H/\rho)$, which is $2b_0\mathcal I$ in the paper's conventions. The two-phonon element remains new.

**Action:** credit p. 518 of [4] for the overlap integral in this sentence.

### 3. The README overstates what is new and carries no novelty status (medium)

```
README.md:22-25
The 1991 side paper, **A trapped electric field on an Abelian Higgs
vortex** (QCDS-91/S1), derives the mass and polarized two-phonon residue
of a localized electric mode. At equal Higgs and vector masses a second
particle of even parity has the same mass and a different phonon channel.
```

What is known:

- The trapped longitudinal vector state: Arodź 1991 (ref. [4]) shows it exists and gives a square-well estimate of its energy (scan p. 516). A computed energy first appears in Arodź–Hadasz 1995.
- The even partner at critical coupling: the BPS-vortex shape mode, $\omega^2\simeq0.777\,m_V^2$. JHEP 05 (2016) 074 (Alonso-Izquierdo, García Fuertes, Mateos Guilarte) builds the same $(1/\omega)\mathcal D^\dagger$ partner, and later work quotes $\omega^2=0.777476$ against the paper's $0.7774728$ (confirmed by the second referee). Goodband–Hindmarsh, PRD 52 (1995) 4621, is cited here from memory and needs checking.

What is plausibly new: the pole match (19) to the 1990 convention, the equal projected strength of the even partner via $N'(0)=m_*\mathcal I$ in (28), the polarization table, the widths and the finite-volume test. The identification of the shape mode with the physical $A_0/A_z$ mode may also be the paper's own.

What has not been searched: the novelty of the odd-mode coupling (15)–(19). The 2026 thesis in the retrospective note was consulted only through its abstract. Agia, arXiv:1512.03404, which calls the scalar breather the lightest massive mode, is missing.

**Action:** rewrite the README sentence with a novelty status: mass known, overlap integral in [4], residue, sum rule and critical-partner strength new, coupling novelty "not searched", review AI-only.

### 4. The retrospective note omits the shape-mode literature (medium)

`paper.md:471` cites Arodź–Hadasz (1995) and a 2026 thesis. It omits the BPS shape-mode papers of action 3, which contain the critical degeneracy of §8 as a spectral fact. The note exists to separate period derivation from later priority.

**Action:** add those references and arXiv:2603.05243 to the note.

### 5. Process record (low)

```
OUTPUTS_PLAN.md:33-34
... Since 1982 the referee is
a different model from the author.
```

```
paper.md:3                **Codex · qcdstring programme**
REFEREE.md:55             **Signed:** Independent second-line referee, Codex — `vortex_referee`
```

- Author and referee both sign as "Codex", and the author model is not recorded. **Action:** record both model names.
- The 1991 folder has `results/radial.json` and no `results/environment.txt`. Tags stop at `y1988`. **Action:** add the environment record and tag the 1990 and 1991 outputs.
- The BPS residual is $1.1\times10^{-6}$ while the table prints eight digits. **Action:** print the digits the residual supports, or state the residual beside the table.

### 6. Text corrections (low)

- `TIMELINE.md:40`: "Arodź derives vector bound states on the Abelian Higgs vortex, following a flux-twist proposal in 1987." The second referee reports that the note added in proof of ref. [4] says its author learned of the 1987 work (Davis, `paper.md:477`) afterwards. **Action:** replace "following" with a neutral ordering.
- `paper.md:44`: "critical or Bogomolny coupling" has no reference. Candidates named by the second referee: Förster 1974, Gervais–Sakita 1975.
- The 1988 paper might cite Maeda–Turok and Gregory (1988). This suggestion is from memory and unverified.

### 7. Consequences the papers do not draw (low)

- At $\beta=1$ the even partner realises the 1988 scalar-curvature model with $|q|=|Q_{\rm pole}|$.
- The charge-free product $|Q_{\rm pole}|m_*/\sqrt\sigma=0.597469$ (`paper.md:414`) is never compared with the registered P04 value, $Q\approx0.37$ at mass $1.85\sqrt\sigma$, a product of about $0.68$ (`ideas/013-a-pseudoscalar-on-the-worldsheet.md:12-13`).

### 8. Notes without a required action

- `PREDICTIONS.md:250-262`: the 1990 and 1991 entries say "at tree level" and "P04 remains open". The wording is accurate. A tag "AI review only" would complete it.
- `AGENTS.md:25-26` requires 15,000 tokens per manuscript from 1990 on. The 1991 paper has 17,479. This is the user's rule. The first review found the scope caveats of §1, §4 and §11 repetitive; the second referee found that they make different points.
- Style count by the second referee: about 21 negation-contrast phrases in the 1988 paper and about 54 in the 1986 paper. The 1991 paper is nearly free of them.

## Resolved

- The untracked `outputs/paper-lengths.png` is now ignored (`.gitignore`, commit `246f436`). The file stays on disk, untracked.

## What was verified

By hand, in the 1991 paper (first review; the second referee re-derived these and agrees):

| Item | Location (`paper.md`) | Result |
|---|---|---|
| Vacuum masses $m_V^2=2e^2v^2$, $m_H^2=2\lambda v^2$ | 37-41 | correct |
| Tension $\sigma=2\pi v^2\tau$, BPS value $\pi m_V^2/e^2$ | 56-81 | correct |
| Radial equations (5) and $dB/dr=-2ev^2wf^2/r$ | 64-71, 218 | correct |
| Current identity $HB=4eK$ | 218-222 | correct |
| Pole match $\lvert Q_{\rm pole}\rvert=\mathcal I/m_*$ from (15) | 236-248 | correct |
| Two-body phase space $1/m_*^2$ and $\Gamma_{12}=g_*^2/(2m_*^3)$ | 421-428 | correct |
| Even-partner widths $\Gamma_{11}+\Gamma_{22}=\Gamma_{12}$ | 433 | correct |
| Finite-volume element (31), golden-rule limit, density $L/4\pi$ | 441-453 | correct |
| Numbers in (29): $0.497471e$, $0.00270524e^6$, $\Gamma/m_*=0.0110427e^2$, splitting $0.08385e$ | 410-449 | reproduce from the table |
| Critical partner $DD^\dagger(0,u)=(0,\mu^2u)$ | 330-340 | correct |
| $\mu=0.8173>m_H/m_V=0.7071$ at $\beta=1/2$ | 155 | correct |

Also by hand:

- 1990 channel algebra in `outputs/1990-pseudoscalar-curvature/amplitudes.md`: trace $-D_u$, antisymmetric $2D_s+D_u$, spin two $+D_u$.
- Second referee, 1991 paper: equations (12), (14), (20), (23)–(25), (27) and (28). For (28) it used a route independent of the paper's and got $N'(0)=\mu\alpha=m_*\mathcal I$.
- Second referee, 1986 and 1988 papers: $V''_{NS}(0)$, $7\zeta(3)L^2/(32\pi^3)$, $\Delta E=-32\pi^6b/(225L^7)$ and the table rows. `OUTPUTS_PLAN.md:79` marks the 1986 paper "author-checked and unrefereed by explicit user waiver".
- Parity bookkeeping (§3, eq. (10)), the use of $CP_\perp$ and the antisymmetric right–left state are consistent. The on-shell argument of §5.1 is standard and correctly restricted to three points. `paper.md:431` calls (30) a partial width, which is accurate, since a Higgs-plus-phonon channel may be open at $\beta=1/2$.

Numerically, before the user's instruction to stop running programs: `code/vortex.py` rerun on a scratch copy gave a byte-identical `results/radial.json`, and a separate finite-difference solver ($N=20000$, $R=30$) gave $\mu^2=0.77747276$ against the stored $0.77747281$.

## Limits of this review

- The factor 2 of action 1 is unresolved.
- Priority was checked by a few searches. The odd-mode coupling has not been searched.
- Goodband–Hindmarsh, Förster, Gervais–Sakita, Maeda–Turok and Gregory are cited from memory.
- Commit `146e3a8` (17 Nov, "Plans: reconnect the effective-string work to the superstring programme") was not reviewed. It edits `AGENTS.md` and `LONG_MARCH.md` only.
