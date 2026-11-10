# Pilot runs (1982)

The runs that chose the method of Section 3, kept because they cost machine
time and because their findings are quoted in Sections 3.1 and 3.4. The
scripts are kept as run and import the programs of `../`. Stored outputs are
in `../../results/pilots/`.

| Script | Purpose | Output | Charged operations (cost model of Appendix C) |
|---|---|---|---|
| `gauge_nt1_check.py` | gauge theory with one time slice: wall correlator of the lines against the exact mass of the two-dimensional Ising model | `gauge_nt1_check.log`: effective masses 0.169(5) and 0.167(5) at steps 2 and 3, against 0.1677 | $5.5\times10^{9}$ |
| `samechain82.py` | two-level and plain wall estimators on the same Markov chain, three small lattices | `samechain82.log`: differences with errors five to twelve times smaller than either estimate's | $3.8\times10^{9}$ |
| `smear_test.py` | smearing levels 0, 1, 2, 4, 8 for the closed line at $N_t = 8$, 12, 16 | printed: one or two steps raise the overlap, eight lose the signal | $3.4\times10^{10}$ |
| `slow_modes.py` | long histories of plaquette and lines on eight lattice-and-start combinations (list below) | printed, not stored: slow wandering of the plaquette at $N_t = 8$ | $1.375\times10^{11}$ |
| `../ising_path.py --name p8` | first test of the integration method, tube of length 8, 4000 sweeps per coupling | `path_p8.npz` | $1.8\times10^{10}$ |
| **Total** | | | $1.99\times10^{11}$ (4.6% of the cap) |

The seventeen gauge-theory wall-correlator runs (`../run_gauge_check.sh`,
`z2w_*.npz` and `z2t_*.npz` here) are charged separately in Table 12 of the
paper, $1.40\times10^{11}$ operations.

The operations of the first four scripts were not counted by the programs;
they are computed from the sweeps and lattice sizes with 20 operations per
link update and the measurement charges of Appendix C.

The eight runs of `slow_modes.py`, all at $\beta = 0.73$ ($N_t \times L_x \times L_y$):
$8\times64\times12$, $8\times48\times16$ and $8\times32\times32$, each from a hot and from a
cold start, 30,000 sweeps; $16\times32\times32$ from a cold start, 20,000 sweeps;
$12\times48\times16$ from a hot start, 30,000 sweeps.

Of these charges, the direct gauge-theory method (the wall correlators and
the first four scripts) is $3.21\times10^{11}$, 7.4% of the cap; `path_p8` is a
pilot of the dual-model method.
