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
  folder also holds our response and the changes it caused.
* **Evidence.** Remembered numbers choose the work and sit in the ledger
  as predictions. A paper closes a ledger entry only by computing it.
* **Only the next slots are fixed.** 1976 to 1984 are drafted in the
  table below; later slots are rewritten as results and historical
  discoveries arrive.

| Year | Working title | Ideas | Status |
|---|---|---|---|
| 1976 | The Casimir energy of a flux tube, and an area law on the computer (Z2 in 3d, U(1) in 4d) | 001, 004, 009 | done: `outputs/1976-flux-tube-casimir/`, tag `y1976` |
| 1978 | SU(2) string tension and asymptotic scaling | 004 | done: `outputs/1978-su2-scaling/`, tag `y1978` |
| 1980 | Excited flux-tube levels, the square-root spectrum, roughening; longer strings to separate the Casimir coefficient from an endpoint term | 001, 011 | |
| 1982 | Hagedorn versus deconfinement: Polyakov loops and T_c below T_H | 005, 009 | |
| 1984 | The critical dimension as a statement about the effective string | 002, 012 | |
