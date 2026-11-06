# Pilot runs (1976)

The runs used to choose the method and parameters of Section 3.3, kept
because they cost machine time and because two of their findings are quoted
in the paper. Logs are in `../../results/pilots/`. The scripts are kept as run
(they import `../z2core.py`); some were run with an earlier default of the
one-link option.

| Script | Purpose | Log | Charged operations (cost model of Appendix A) |
|---|---|---|---|
| `validate_ml.py` | first comparison of direct and two-level estimates (two settings) | (not kept) | $6.1\times10^{9}$ |
| (first `z2_validate.py`) | direct and two-level estimates on separate stretches of one chain, $N_t = 6$ | (superseded by the same-chain test) | $1.33\times10^{10}$ |
| `z2_multilevel.py --tag _pilot` | $N_t = 32$, $L = 32$, slabs of 2: signal lost beyond $R = 4$-5 | (not kept) | $1.04\times10^{10}$ |
| `pilot2.py` | $N_t = 24$, slabs of 2, with and without the one-link average | `pilot2_*.log` | $2.28\times10^{10}$ |
| `diag.py` | slab averages for slabs of 2, 4, 6 on one frozen configuration | `diag*.log` | $1.44\times10^{10}$ |
| `pilot3.py` | $N_t = 16$ and 12, slabs of 2 and 4, 200 sub-updates | `p3_*.log` | $3.75\times10^{10}$ |
| `pilot3.py` | 1000 and 3000 sub-updates | `p4_*.log` | $3.78\times10^{10}$ |
| `samechain.py` | same-chain comparison, the method of the final `z2_validate.py` | `sc_*.log` | $2.08\times10^{10}$ |
| **Total** | | | $1.63\times10^{11}$ (13.7% of the cap) |
