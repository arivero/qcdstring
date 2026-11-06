# Provenance of the second line

| Item | Value |
|---|---|
| Author | Astra 6.0, working independently on the same brief |
| Received | 6 November 2026, 19:22-19:24, as /tmp/Strings_1974.zip plus three loose Markdown files |
| Archive SHA-256 | `cac12797df3fbfb1996b2da7421644f9bcb4679cdd6010372aa4a4575747f9c0` |
| Archive contents | 35 files, version 0.3 of "Strings, 1974" |
| Loose files | SPIN2_AND_SUPERSYMMETRY.md, FLAVOUR_AND_SCALES.md, SUCCESS_CRITERIA.md; each is byte-identical to the archive member of the same name |
| Stored at | `second_line/astra-6.0/`, unmodified |

## Reproduction on this machine

Python 3.14.4 and SciPy 1.16.3 (the archive used Python 3.12.14 and SciPy 1.17.0).

| Script | Result |
|---|---|
| `calculations/checks.py` | 11 checks pass; RESULTS.md identical apart from the environment line |
| `calculations/flavour_checks.py` | 22 checks pass; FLAVOUR_RESULTS.md byte-identical |
| `calculations/spin_susy_checks.py` | m_tensor/M_KK = 1.5669021099; SPIN_SUSY_RESULTS.md byte-identical |

An independent check by a different method, `numerics/d4_tensor.py`, gives the same
first eigenvalue to 1e-10 and adds the next three tensor levels.

The copy in this repository keeps the shipped outputs. Running the scripts in place
regenerates them.
