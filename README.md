# qcdstring

**Date of founding: 6 November 1974.**

Working premise of this repository: the relativistic string of the dual
resonance model is the chromoelectric flux tube of the strong
interactions. Its tension is set by the Regge slope, alpha' ~ 0.9 GeV^-2,
and that is the only scale the theory has ever been anchored to by data.
The proposal of Scherk, Schwarz and Yoneya (this year) to reinterpret the
massless spin-2 closed-string state as the graviton, by rescaling alpha'
by thirty-eight orders of magnitude, is treated here as a wrong turn.
The arguments for and against are laid out in `THESIS.md`.

The author of this repository has an unusual handicap: a complete memory
of how the subject develops over the next fifty years. That memory is a
resource, and it is used openly. Results that are "remembered" rather
than derived are labelled as such everywhere, and are treated as
conjectures until re-derived with the tools and data of 1974. A memory
of a result is a strong hint about *what* is true and a weak hint about
*why*; the research plan is built around closing that gap.

## Layout

| Path | Contents |
|---|---|
| `THESIS.md` | The position: the string is the hadronic flux tube. Arguments, counter-arguments, what would change my mind. |
| `RESEARCH_PLAN.md` | Phased plan, milestones, falsifiable predictions, resource needs. |
| `LONG_MARCH.md` | How the programme absorbs the five superstring theories and M-theory as charts on the confining vacuum; the admission that it is geometry, and the hadronic reading of that geometry. |
| `outputs/` | One paper every two years from 1976 (plan and rules in `OUTPUTS_PLAN.md`). Each folder holds the paper, every program behind its numbers, raw results, figures, a cold referee report for the second line and our response. Tagged `y1976`, `y1978`, ... |
| `second_line/` | The independent package of Astra 6.0 on the same premise, unmodified, with provenance and a memo on how it was integrated. |
| `TIMELINE.md` | What the memory says happens next (1974 to 2026), and where to intervene. |
| `PREDICTIONS.md` | Registered predictions with dates. The honesty ledger. |
| `OUTPUTS_PLAN.md` | The plan for one paper every two years, 1976 to 2026: the rules (the world moves as it did, era-bound computing, a cold referee) and the next slots. |
| `papers/` | Two manifests. `library-1974.tsv`: papers that exist now and should be on the shelf. `memory-future.tsv`: papers that do not exist yet; their results must be rederived. `fetch.py` resolves identifiers through INSPIRE and downloads what is freely available. |
| `ideas/` | One file per idea to test. Each has a claim, its 1974 status, what the memory says, a concrete test, and a status line. |
| `numerics/` | Small programs: Regge fits, the Nambu-Goto (Arvis) spectrum and Luscher term, a Z2 lattice gauge Monte Carlo (Metropolis 1953 exists; a lattice gauge theory now exists too, Wilson 1974). |
| `data/` | Hadron masses and spins from the 1974 Review of Particle Properties, in machine-readable form. |
| `journal/` | Dated lab notebook. |
| `people/` | Who to write to, visit, or recruit, and why. |
| `GLOSSARY.md` | Terms, with the 1974 name and the later name side by side. |

## Conventions

* Units: GeV, with hbar = c = 1. alpha' is the Regge slope; sigma = 1/(2 pi alpha') is the string tension.
* Remembered numbers are predictions, never inputs or evidence (see `second_line/README.md` for the mapping onto the second line's six status labels).
* Every claim is tagged with one of: `[1974]` derivable or checkable now; `[MEMORY]` remembered from the future, to be rederived; `[TEST]` a concrete check that can be run.
* Idea files are numbered and never renumbered. Status lines are one of `open`, `in progress`, `supported`, `refuted`, `superseded by NNN`.
* Papers are cited by the key in the manifests (e.g. `Wilson1974`).

## Quick start

    python3 numerics/regge_fit.py        # universal slope from 1974 hadron data
    python3 numerics/arvis_spectrum.py   # Nambu-Goto spectrum, Luscher term, Hagedorn temperature
    python3 numerics/z2_lattice.py       # area law in Z2 lattice gauge theory (small, slow, honest)
    python3 numerics/d4_tensor.py        # D4 tensor glueball levels, independent check of the second line
    python3 papers/fetch.py --dry-run    # see which papers can be fetched today
