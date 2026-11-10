# 1984: The critical dimension as a statement about the effective string

Slot 1984 of `OUTPUTS_PLAN.md` (ideas 002, 011, 012; also 001). Tag `y1984`.

| File | Contents |
|---|---|
| `paper.md` | The paper (preprint QCDS-84/1, November 1984) |
| `REFEREE.md` | Cold referee report for the second line |
| `RESPONSE.md` | Reply to the referee and the changes made |
| `code/effective_string.py` | Symbolic and numerical work behind the derivations: checks of Sections 2-4 and Appendices B, C; evaluation of (11), (12) (sympy, numpy) |
| `code/refit84.py` | Refits of the stored data of the 1976, 1980 and 1982 papers; figures |
| `results/` | `effective_string.txt`, `refit84.txt`, `summary84.json` |
| `figures/` | The two figures |

## Reproduce

Python 3 with numpy, scipy, sympy and matplotlib.

    python3 code/effective_string.py     # Sections 2, 4, 5 and Appendices A-C; seconds
    python3 code/refit84.py              # Sections 3 and 6; reads ../1976-*, ../1980-*, ../1982-*; about a minute

## Computing

No new simulation (Appendix D of the paper). From this paper on the programme's
papers rest on derivations and on data already taken.
