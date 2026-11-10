#!/usr/bin/env python3
"""Zero-temperature string tension of SU(2) at the deconfinement couplings of
Nt = 2 and 3 (1982 paper, Section 5): Wilson loops with the 1978 programs
(../../1978-su2-scaling/code/su2core.py, su2_runs.py), at beta = 1.88 on 8^4
and beta = 2.17 on 10^4. For Nt = 4 the 1978 runs at beta = 2.2 and 2.3 are
used. Writes ../results/su2_loops_b<beta>.json; analyze82.py fits them with
the 1978 procedure."""
import os, sys
from multiprocessing import Pool
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "1978-su2-scaling", "code"))
import su2_runs

# beta, L, smearing steps, Rmax = Tmax, thermalization, measurements, sweeps between (as in the 1978 plan)
PLAN = [(1.88, 8, 2, 4, 200, 200, 4), (2.17, 10, 4, 5, 200, 150, 5)]


def one(p):
    su2_runs.RES = os.path.join(HERE, "..", "results")
    return su2_runs.loops_one(p)


if __name__ == "__main__":
    with Pool(len(PLAN)) as pool:
        pool.map(one, PLAN)
