# Strings, 1974

## Starting position

We are at the end of 1974, carrying modern theoretical knowledge. Our working conviction is that strings describe quantum matter, especially strong interactions; identifying them with the gravity of our spacetime is not the purpose of the programme.

This is a research position, not a license to alter established calculations. Conventional critical closed strings have gravitational sectors. We will use that knowledge to identify precisely which assumptions must change when constructing a theory of strings without dynamical spacetime gravity.

The main physical question is:

> Can one interacting string description account for confinement, massive tensor states and hard constituent scattering, while containing no physical massless graviton in the spacetime whose experiments it describes?

Version 0.3 has five explanatory targets: an exceptionally heavy top, a derived limitation on generations, a quantitative relation between QCD and the Fermi scale, a physical explanation of the spin-two object, and an explanation of supersymmetry and its realization. Flavour, tensor interpretation and supersymmetry all enter the first research cycle. Read SUCCESS_CRITERIA.md for the meaning of a prediction in this counterfactual exercise.

There is also an independent existence question: can finite-tension, interacting string theories survive a limit that removes gravity? Modern little string theories and noncommutative open string theories supply benchmarks for this question. They are not automatically models of hadrons.

## Read first

| File | Purpose |
|---|---|
| [SUCCESS_CRITERIA.md](SUCCESS_CRITERIA.md) | The five explanatory targets and their prediction standards |
| [RESEARCH_PLAN.md](RESEARCH_PLAN.md) | Research priorities, twelve-week pilot and one-year decision points |
| [ASSUMPTIONS.md](ASSUMPTIONS.md) | Meaning of “not gravity,” historical rules and standards of evidence |
| [IDEA_REGISTER.md](IDEA_REGISTER.md) | Fourteen tests, dependencies and stopping conditions |
| [notes/SPIN2_AND_SUPERSYMMETRY.md](notes/SPIN2_AND_SUPERSYMMETRY.md) | Tensor origin, worldsheet/spacetime supercharges and a smooth confining benchmark |
| [calculations/SPIN_SUSY_RESULTS.md](calculations/SPIN_SUSY_RESULTS.md) | Reproduced D4 tensor eigenvalue, Rayleigh check and worldsheet finite-size controls |
| [notes/FLAVOUR_AND_SCALES.md](notes/FLAVOUR_AND_SCALES.md) | Rank-one Yukawas, conditional 3–8 family interval, flux bounds and threshold derivations |
| [calculations/FLAVOUR_RESULTS.md](calculations/FLAVOUR_RESULTS.md) | Twenty-two executed flavour and scale checks |
| [notes/TENSOR_TOY_MODEL.md](notes/TENSOR_TOY_MODEL.md) | Worked example: a bulk tensor equation with a gapped four-dimensional spectrum |
| [notes/DERIVATIONS.md](notes/DERIVATIONS.md) | Short calculations underlying the programme |
| [calculations/RESULTS.md](calculations/RESULTS.md) | Executed numerical and algebraic sanity checks |
| [REFERENCES.md](REFERENCES.md) | Sources separated into pre-1975 foundations and theoretical imports |
| [DECISION_LOG.md](DECISION_LOG.md) | Current decisions, unresolved questions and the next work session |

Each file in the ideas directory is an executable research brief: a question, calculation, deliverable, and condition for abandoning that route. “Executable” here means specific enough to work on; most calculations remain proposed.

## What has actually been done

The package contains a sourced plan and fourteen test briefs. The original Python script checks color-topology powers, elementary decoupling scalings, long-string energies, critical central-charge deficits, and a tensor Sturm–Liouville toy model. A second script executes twenty-two flavour and scale controls. A third reproduces the tensor mode in a smooth D4 confining background and checks it against a Rayleigh quotient and endpoint convergence. These are preparatory or benchmark calculations, not a completed physical string model or a solution of QCD.

The toy model has no normalizable massless tensor with the chosen boundary conditions. Its first massive eigenvalue is \(m_1z_0\simeq3.831706\). This shows why a tensor field in a higher-dimensional description does not by itself imply an observed four-dimensional graviton. The assumed geometry and infrared boundary still need a microscopic justification.

In the explicitly specified one-loop, one-Higgs, single-Yukawa truncation, simultaneous color asymptotic freedom and a positive nonzero fixed Yukawa/color ratio allow 3–8 generations. This makes three the smallest permitted integer under those conditions, not a derived unique family count. A separate algebraic toy shows how a finite index bound can fail to stay uniform in a limit. No numerical top mass or strong/weak ratio is predicted.

The new D4 benchmark eliminates the massless tensor through smooth-tip regularity and UV normalizability, giving m_tensor/M_KK=1.5669021. Its antiperiodic spatial circle breaks inherited spacetime supersymmetry. This supplies a common mechanism for the two features, while the unwanted KK states and the unexplained choice of microscopic background remain limitations.

## Reproduce

Use Python 3 and SciPy; the initial run used Python 3.12.14 and SciPy 1.17.0.

~~~bash
python3 -m pip install -r calculations/requirements.txt
python3 calculations/checks.py
python3 calculations/flavour_checks.py
python3 calculations/spin_susy_checks.py
~~~

The scripts write their respective RESULTS.md, FLAVOUR_RESULTS.md and SPIN_SUSY_RESULTS.md reports and JSON data beside themselves. They make no network requests. The tensor scripts use no experimental data; the flavour script uses synthetic inputs and explicitly rounded historical weak/pion scales for one dimensional control. None fits a future mass or generation count.

Prepared and revised 6 November 2026. Counterfactual research date: end of 1974. Version 0.3.
