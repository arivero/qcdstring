# 1988: Thickness and curvature of a confining string

**QCDS-88/1, November 1988. Author: gpt-6-astra-max.** Seventh biennial paper,
tag `y1988`.

Read [the paper](paper.md) or [the PDF](paper.pdf). The paper compares a massive
normal field with a local rigidity expansion and derives a scalar-curvature
exchange contribution to the periodic energy at order L^-7. All physical
applications to QCD remain conditional on matching. The earlier direct
area-action L^-5 calculation remains unfinished.

The independent gpt-6.1-sol referee recommends acceptance after four minor
clarifications. All four are addressed in this edition and its response.
The referee read the frozen draft and stored calculations without running
code. The 91 author checks are not independent replications.

| File | Purpose |
|---|---|
| `paper.md`, `paper.pdf` | Article, derivations, scope, references and memory account |
| `PLAN.md` | Bounded task and completion criteria |
| `code/thickness88.py` | Independent checks, numerical tables and scientific figures |
| `code/check_document.py`, `code/build.py` | Publication consistency and PDF build |
| `results/`, `figures/` | Stored calculations, environment, tables and generated figures |
| `SOURCES.md`, `sources.tsv` | Bibliography and actual reading coverage |
| `AUTHOR_CHECKS.md` | Validation and unresolved physical limitations |
| `REFEREE.md`, `RESPONSE.md` | Independent report, its scope and the four author revisions |

From this directory, with Python 3, NumPy, SciPy, SymPy, mpmath, Matplotlib,
Pandoc and XeLaTeX:

```sh
python3 code/thickness88.py
python3 code/check_document.py
python3 code/build.py
```

The programs also work from another current directory. No earlier simulation
or second-line file is changed. The downloaded historical scan is kept in
the ignored source library and is not redistributed.

The 20 November 2026 second referee also hand-checked the scalar-curvature vacuum shift and table entries. The subsequent revision identifies the 1988 finite-width calculations of Maeda–Turok and Gregory in the period bibliography. [Source record](SOURCES.md) · [Joint review response](../1991-vortex-pseudoscalar/RESPONSE.md#response-to-the-joint-review-of-20-november-2026)
