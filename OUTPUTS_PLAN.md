# Output plan: one paper every two years, 1976 to 2026

Agreed 6 November 2026 (machine date).

* **Cadence.** One paper per even year from 1976 to 2026, in
  `outputs/<year>-<slug>/`: the paper, the code behind every number in
  it, a ledger update, and a referee report. Each paper is tagged
  `y<year>`. Commit dates stay real; the fictional year lives in the
  tag and the folder name.
* **The world moves as it did.** Every published result appears on its
  historical date (Creutz 1979, Green-Schwarz 1984, Maldacena 1997, the
  lattice measurements), and other authors never read our papers. Our
  line reacts to those discoveries in the next slot, and its later
  papers cite its own earlier ones.
* **Era-bound computation.** Each paper's numerics are capped at the
  computing budget of its year: roughly a hundred hours of the best
  machine available to a university group.
* **Referee.** The second line (Astra 6.0) receives each draft without
  our notes and writes a report, stored beside the paper. In practice the
  report is written by a fresh agent instructed to act for the second line,
  given only the paper folder (and earlier papers of this line) and the
  second line's own package; Astra 6.0 itself is not consulted. Each paper
  folder also holds our response and the changes it caused. From the 1986
  report on, the referee reads and does not compute: it judges the paper, the
  stored printouts and the programs as text, and turns a check it would have
  liked to run into a requested change, which the authors then carry out in
  the response. (The referees of 1976 to 1984 reran programs, and those of
  1976 to 1982 ran small simulations of their own.) Since 1982 the referee is
  a different model from the author.
  **1986 exception:** the user explicitly waived the independent referee on
  13 November 2026 and requested author checks and publication without it.
  The 1986 package records that absence; the general rule remains unchanged.
* **Evidence.** Remembered numbers choose the work and sit in the ledger
  as predictions. A paper closes a ledger entry only by computing it.
* **Only the next slots are fixed.** Later slots are rewritten as results
  and historical discoveries arrive.
* **Theory first from 1984.** Agreed 10 November 2026 (machine date), while
  the 1982 runs were finishing. From the 1984 paper on, the papers
  concentrate on theoretical results. Two reasons: once computing becomes
  parallel, the budget of one machine no longer represents what scientists
  had; and string theory has never been a computational subject. Numerics
  from 1984 on are checks of derivations and refits of data already taken.
  The era-bound budget above applies to the papers up to 1982.
* **What the string is.** As throughout the repository: the string is
  never treated as a theory of gravity. At most it is a theory with a
  geometric formulation that includes more dimensions.
* **Off the remembered line (proposed 10 November 2026, from 1986).** Up to
  1984 every result of the papers has a counterpart somewhere in the
  remembered literature, usually later than the paper's date. From the 1986
  slot (the superstring years read from the hadron side) that stops being
  true. Each paper's memory appendix then separates three kinds of
  statement: remembered and re-derived; remembered and used only to choose
  the work; and statements with no remembered counterpart, for which the
  derivation in the paper is the only support and which the referee is
  asked to press hardest.
* **Lost and late.** A result is *lost to the chronology* only if nobody
  has published it and nobody will: it was within reach of one of our
  slots, has no counterpart in the real literature, and this line can no
  longer obtain it. Such a result gets an issue on the repository (label
  `lost-in-chronology`). A result that our slots passed over and that the
  world publishes at a later date is only *late to the chronology*: this
  line loses the priority and nothing else. Late items are worth a mention
  and are minor; they are collected in one issue per stretch of slots
  (label `late-to-chronology`). What the world had already published
  before our slot is neither.

| Year | Working title | Ideas | Status |
|---|---|---|---|
| 1976 | The Casimir energy of a flux tube, and an area law on the computer (Z2 in 3d, U(1) in 4d) | 001, 004, 009 | done: `outputs/1976-flux-tube-casimir/`, tag `y1976` |
| 1978 | SU(2) string tension and asymptotic scaling | 004 | done: `outputs/1978-su2-scaling/`, tag `y1978` |
| 1980 | Excited flux-tube levels, the square-root spectrum, roughening; longer strings to separate the Casimir coefficient from an endpoint term | 001, 011 | done: `outputs/1980-excited-flux-tube/`, tag `y1980` |
| 1982 | Hagedorn versus deconfinement: the closed flux tube at finite temperature (Z2 in 3d through the dual Ising model; SU(2) in 4d) | 005, 009, 001 | done: `outputs/1982-hagedorn-deconfinement/`, tag `y1982` |
| 1984 | The critical dimension as a statement about the effective string (theory; refits of the 1976-1982 data) | 002, 011, 012, 001 | done: `outputs/1984-critical-dimension/`, tag `y1984` |
| 1986 | Ten years of QCD strings: fermions, hidden dimensions, and the long flux tube. Review of 1976-1986; massive determinants and a homogeneous large-flavour Gross-Neveu sector; dimensional suppression as a conditional consistency requirement | 017, 020, 022, 027, 012 | done, author-checked and unrefereed by explicit user waiver: `outputs/1986-fermionic-flux-tube/`, tag `y1986` |
| 1988 | Thickness and curvature: a healthy massive internal field versus a local rigidity expansion, responding to Polyakov and Kleinert (1986). Distinguish perturbative equation-of-motion redundancy from threshold physics. Rotating-string intercept if endpoint treatment is controlled. Carried over: direct area-action L^-5 calculation and the rules of 1984 Section 4.2 beyond first order | 011, 013, 006, 012 | proposed after 1986 |
