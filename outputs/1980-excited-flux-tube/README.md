# 1980: Excited flux tubes, the square root, and roughening

Slot 1980 of `OUTPUTS_PLAN.md` (ideas 001, 004, 011). Tag `y1980`.

| File | Contents |
|---|---|
| `paper.md` | The paper (preprint QCDS-80/1, November 1980) |
| `REFEREE.md` | Cold referee report for the second line |
| `RESPONSE.md` | Reply to the referee and the changes made |
| `code/` | Every program behind a number in the paper |
| `results/` | Raw outputs (NPZ, JSON), `analysis80.txt` (printout of `code/analyze80.py`), `checks80.txt` |
| `figures/` | The three figures |

## Reproduce

Python 3 with numpy, scipy and matplotlib. Times are for a 16-core machine of 2026.
The Z2 programs import the update routine of `../1976-flux-tube-casimir/code/z2core.py`.

    python3 code/checks80.py             # gauge covariance of all operators, seconds
    sh code/run_excited.sh               # first production, 32 processes, about 10 minutes
    sh code/run_gevp.sh                  # second production (two operators per channel), about 15 minutes
    python3 code/z2_excited_direct.py --beta 0.73 --nconf 1000 --Rmax 9 --seed 1   # third production, one of 8 chains (seeds 1-8), about 25 minutes each
    python3 code/bcsos_calibration.py    # Section 5 calibration, 24 runs, about 15 minutes
    sh code/smearing_tests.sh            # the three smearing tests of Appendix B
    python3 code/ising_interface.py      # Section 5, 36 runs, about 10 minutes
    python3 code/analyze80.py            # tables, fits, figures, budget

## Budget

99 of 100 Cray-1 hours (Appendix B of the paper). Runs beyond the budget are in `results/over_budget/` and enter no number.
