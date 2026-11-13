# 1986: Ten years of QCD strings

**QCDS-86/1, November 1986. Author-checked; independent referee waived by the
user.** Sixth biennial paper, tag `y1986`.

Read [the paper](paper.md) or [the PDF](paper.pdf). The review covers 1976-1986
and adds massive-fermion Casimir calculations, a homogeneous large-flavour
Gross-Neveu model on the tube, a quantum relevance test for a pinned compact coordinate, and a conditional argument for suppressing extra
dimensions. It does not claim a microscopic QCD construction or a proof that
compactification is necessary. The reported 2026 Lean development is not used.

| File | Purpose |
|---|---|
| `paper.md`, `paper.pdf` | Review, derivations, limits, references and memory account |
| `code/worldsheet86.py` | Reproduce the model calculations, author checks, tables and figures |
| `code/check_document.py` | Check printed tables, references, local assets and equation labels |
| `code/build.py` | Build the PDF from the Markdown source |
| `results/` | Numerical output, machine-readable checks and generated tables |
| `figures/` | Model curves in PNG and PDF; no new lattice data |
| `SOURCES.md`, `sources.tsv` | Source identifiers, access and reading coverage |
| `AUTHOR_CHECKS.md` | Validation and remaining limitations |
| `REFEREE.md`, `RESPONSE.md` | Explicit waiver and absence of an independent report |

From this directory, with Python 3, NumPy, SciPy, Matplotlib, Pandoc and XeLaTeX:

```sh
python3 code/worldsheet86.py
python3 code/check_document.py
python3 code/build.py
```

The programs also work from another current directory. No simulation is run;
no earlier raw data or second-line files are modified. The dependency versions
used for this edition are recorded in `results/environment.txt`.

Commit credit requested by the user: **Astra 6 max**. Review status is unaffected
by that credit: there was no independent agent or different-model referee.
