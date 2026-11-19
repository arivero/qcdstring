# Project writing convention

When writing or revising scientific prose, avoid possessive attribution of
ideas, theories, models and calculations to individual people. Prefer neutral
wording such as "the theory", "the model", "the calculation in [reference]",
or "the construction of A and B". Collective first person is welcome:
"we find", "we see", "our model", "our calculation".

Keep proper citations and established names such as "Yang-Mills theory" and
"Gross-Neveu model". This is a prose convention, not a request to remove credit,
rename technical terms, or alter verbatim titles and quotations. Use neutral
constructions for other conceptual possessives when they read naturally.
Apply the rule to new and revised text; do not rewrite archived papers or the
unaltered second-line package solely for style.

This project-wide note records the user instruction of 13 November 2026.

# Planning a paper

Before choosing the scope of a new paper, read `LONG_MARCH.md`,
`RESEARCH_PLAN.md`, `OUTPUTS_PLAN.md` and `TIMELINE.md`. Consult `THESIS.md`,
`PREDICTIONS.md`, the latest paper and its response, and the relevant idea
files and second-line research plan to recover the scientific context.

Starting with the 1990 paper, each completed manuscript must meet the
15,000-token minimum defined in `OUTPUTS_PLAN.md`.

Reading the plans is required; following their proposed research agenda is
not. Their topics, priorities, sequencing and interpretations are revisable
guidance, not binding commitments or established scientific results. Choose
the next question from the current evidence, unresolved mechanisms and the
discoveries available at the paper's historical date. Explain a material
change of direction briefly and update the active plan when useful. Current
user instructions take precedence.

In particular, consider how a proposed effective-string calculation advances
the broader connection to superstrings, gauge dynamics and confinement
discussed in `LONG_MARCH.md`. A focused effective-theory paper can be justified;
the broader construction should remain visible when choosing successive
papers. This reminder does not prescribe the subject of the next paper.

Recorded at the user's request on 17 November 2026.

# Integration without pull requests

Integrate finished work directly on the repository's default branch as
set on GitHub (usually `main` or `master`; check with
`gh repo view --json defaultBranchRef`). Fast-forward when the history allows it, otherwise merge
locally, then push the default branch. Do not open pull requests. A side
branch is for work in progress only; merge it back as soon as the work
is complete and delete it afterwards. User instruction of 20 November 2026.
