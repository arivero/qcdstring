# 1976: The Casimir energy of a flux tube, and an area law on the computer

Slot 1976 of `OUTPUTS_PLAN.md` (ideas 001, 004, 009). Tag `y1976`.

| File | Contents |
|---|---|
| `paper.md` | The paper (preprint QCDS-76/1, November 1976) |
| `REFEREE.md` | Cold referee report for the second line |
| `RESPONSE.md` | Reply to the referee and the changes made |
| `code/` | Every program behind a number in the paper |
| `results/` | Raw outputs (JSON, NPZ) and `analysis.txt`, the printout of `code/analyze.py` |
| `figures/` | The three figures |

## Reproduce

Python 3 with numpy, scipy and matplotlib. Times are for a 16-core machine of 2026.

    python3 code/casimir.py              # Section 2, seconds
    python3 code/z2_strong.py            # Section 3.2, 8 processes, about 2 minutes
    python3 code/z2_validate.py          # Section 3.3 validation, about 5 minutes
    sh code/run_z2_production.sh         # Section 3.4, 24 processes, about 5 minutes
    python3 code/u1_4d.py cycle          # Section 4, under a minute
    python3 code/u1_4d.py loops          # Section 4, 9 processes, a few minutes
    python3 code/charmonium76.py         # Section 5, seconds
    python3 code/z2_direct_check.py      # referee check, 4 processes, about 5 minutes
    python3 code/u1_4d.py two_starts     # referee check, a few minutes
    python3 code/analyze.py              # tables, fits, figures, budget

`code/z2core.py` holds the Z2 update and the two-level estimator; the 1980
paper reuses it. Random seeds are fixed, so reruns reproduce the numbers up to
floating-point summation order.

## Budget

98 of 100 CDC 7600 hours with the referee checks and the pilot runs
(Appendix A of the paper; pilot scripts in `code/pilots/`).
