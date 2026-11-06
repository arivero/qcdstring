# 1978: The SU(2) string tension between strong coupling and asymptotic freedom

Slot 1978 of `OUTPUTS_PLAN.md` (idea 004, with the hadron checks of 009). Tag `y1978`.

| File | Contents |
|---|---|
| `paper.md` | The paper (preprint QCDS-78/1, November 1978) |
| `REFEREE.md` | Cold referee report for the second line |
| `RESPONSE.md` | Reply to the referee and the changes made |
| `code/` | Every program behind a number in the paper |
| `results/` | Raw outputs (JSON), `analysis78.txt` (printout of `code/analyze78.py`), `checks78.txt` |
| `figures/` | The three figures |

## Reproduce

Python 3 with numpy, scipy and matplotlib. Times are for a 16-core machine of 2026.

    python3 code/checks78.py              # exact checks of the programs, about a minute
    python3 code/su2_runs.py loops        # Wilson loops at twelve couplings, 12 processes, about 15 minutes
    python3 code/su2_runs.py cycle        # thermal cycle on 8^4, about 10 minutes
    python3 code/su2_runs.py heat         # plaquette fluctuations, 7 processes, a few minutes
    python3 code/su2_runs.py fv           # referee checks: 8^4 at 2.4, 12^4 hot start at 2.5, a few minutes
    python3 code/bottomonium78.py         # Section 7, reads the 1976 potentials, seconds
    python3 code/analyze78.py             # tables, fits, figures, budget

`code/su2core.py` holds the SU(2) heat bath, one-link averages, smearing and
Wilson loops. `code/bottomonium78.py` imports the radial solver of
`../1976-flux-tube-casimir/code/charmonium76.py` and reads its results.

## Budget

95 of 100 CDC 7600 hours, referee checks and disk traffic included (Appendix A of the paper).
