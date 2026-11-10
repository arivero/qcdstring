# 1982: Hagedorn versus deconfinement: the closed flux tube at finite temperature

Slot 1982 of `OUTPUTS_PLAN.md` (ideas 005, 009; also 001). Tag `y1982`.

| File | Contents |
|---|---|
| `paper.md` | The paper (preprint QCDS-82/1, November 1982) |
| `REFEREE.md` | Cold referee report for the second line |
| `RESPONSE.md` | Reply to the referee and the changes made |
| `code/` | Every program behind a number in the paper |
| `results/` | Raw outputs (NPZ, JSON), `analysis82.txt` (printout of `code/analyze82.py`), `hagedorn.txt`, `gauge_check.txt`, `checks82.txt`, `pilots/` |
| `figures/` | The three figures |

## Reproduce

Python 3 with numpy, scipy and matplotlib. Times are for a 16-core machine of 2026.
The SU(2) Wilson loops use `../1978-su2-scaling/code/`; Section 6 reads the raw data of
`../1976-flux-tube-casimir/` and `../1980-excited-flux-tube/` through `../1980-excited-flux-tube/code/analyze80.py`.

    python3 code/hagedorn.py             # Section 2: level density, T_H, open and closed channels; seconds
    sh code/run_paths.sh                 # Sections 3-4: integration paths of the dual Ising model, about 30 minutes
    sh code/run_films.sh                 # Section 4.3: Ising films for the critical couplings, about 3 minutes
    sh code/run_su2.sh                   # Section 5: SU(2) at finite temperature, 18 processes, about 15 minutes
    python3 code/su2_tension82.py        # Section 5: SU(2) Wilson loops at beta = 1.88 and 2.17, 2 minutes
    sh code/run_gauge_check.sh           # Sections 3.1, 3.4: gauge-theory wall correlators, 2 minutes
    python3 code/analyze82.py > results/analysis82.txt   # tables, fits, figures, budget
    python3 code/checks82.py > results/checks82.txt      # Kaufman's formula against exact enumeration

`code/tube82.py` holds the analysis routines (integration with covariance, formula (4), cumulant crossings);
`code/ising_twist.py` the Ising lattice with an antiperiodic plane and Kaufman's exact two-dimensional formula;
`code/z2ft.py` the gauge theory at finite temperature. Random seeds are fixed.

## Budget

88 of 100 Cray-1 hours, pilots included (Appendix C of the paper; `code/pilots/README.md`).
