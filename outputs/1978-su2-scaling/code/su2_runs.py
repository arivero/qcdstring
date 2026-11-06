#!/usr/bin/env python3
"""Monte Carlo runs for the 1978 paper (SU(2), d = 4).

    python3 su2_runs.py cycle      # thermal cycle of the plaquette, 8^4
    python3 su2_runs.py heat       # plaquette fluctuations (specific heat), 8^4
    python3 su2_runs.py loops      # Wilson loops at nine couplings, in parallel
Outputs in ../results/."""
import json, os, sys, time
from multiprocessing import Pool
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from su2core import SU2Lattice, FLOP_PER_LINK_UPDATE

RES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")

# beta, L, smearing steps, Rmax = Tmax, thermalization, measurements, sweeps between
PLAN = [
    (1.5, 8, 0, 3, 200, 200, 4),
    (1.6, 8, 0, 3, 200, 200, 4),
    (1.7, 8, 0, 4, 200, 200, 4),
    (1.8, 8, 0, 4, 200, 200, 4),
    (1.9, 8, 2, 4, 200, 200, 4),
    (2.0, 8, 2, 4, 200, 200, 4),
    (2.1, 8, 2, 4, 200, 200, 4),
    (2.2, 10, 4, 5, 200, 150, 5),
    (2.3, 12, 6, 6, 200, 120, 8),
    (2.4, 12, 10, 6, 200, 120, 8),
    (2.5, 16, 15, 8, 200, 100, 8),
    (2.6, 16, 20, 8, 200, 80, 8),
]


def flop(lat):
    return lat.link_updates * FLOP_PER_LINK_UPDATE + lat.ops


def loops_one(args):
    beta, L, nsm, rmax, therm, nmeas, every = args[:7]
    hot = len(args) > 7 and args[7]
    tag = args[8] if len(args) > 8 else ""
    t0 = time.time()
    lat = SU2Lattice(L, beta, int(1000 * beta) + L + (500 if hot else 0), hot=hot)
    for _ in range(therm):
        lat.sweep()
    W, P = [], []
    for i in range(nmeas):
        for _ in range(every):
            lat.sweep()
        P.append(lat.plaquette())
        W.append(lat.wilson_loops(rmax, rmax, nsm))
    out = {"beta": beta, "L": L, "n_smear": nsm, "Rmax": rmax, "therm": therm, "nmeas": nmeas, "every": every,
           "W": np.array(W).tolist(), "plaq": P, "link_updates": lat.link_updates, "flop": flop(lat),
           "seconds": time.time() - t0}
    out["hot_start"] = bool(hot)
    json.dump(out, open(os.path.join(RES, f"su2_loops_b{beta:.2f}{tag}.json"), "w"))
    print(f"beta {beta}: L = {L}, plaquette {np.mean(P):.5f}, {out['flop']:.2e} flop, {out['seconds']:.0f} s", flush=True)
    return beta


def loops(only=None):
    plan = [p for p in PLAN if only is None or p[0] in only]
    order = sorted(plan, key=lambda p: -p[1])      # big lattices first
    with Pool(len(plan)) as pool:
        pool.map(loops_one, order)


# Referee checks (Response, Major 3-4): smaller boxes and a hot start
FV_PLAN = [
    (2.4, 8, 10, 4, 200, 120, 8, False, "_L8"),
    (2.5, 12, 15, 6, 200, 100, 8, True, "_L12hot"),
]


def fv():
    with Pool(len(FV_PLAN)) as pool:
        pool.map(loops_one, FV_PLAN)


def cycle():
    betas = [round(1.5 + 0.1 * i, 2) for i in range(16)]
    path = betas + betas[::-1]
    lat = SU2Lattice(8, betas[0], 7, hot=True)
    for _ in range(100):
        lat.sweep()
    rows = []
    for leg, b in enumerate(path):
        lat.beta = b
        for _ in range(100):
            lat.sweep()
        pl = []
        for _ in range(100):
            lat.sweep()
            pl.append(lat.plaquette())
        pl = np.array(pl)
        rows.append({"beta": b, "direction": "up" if leg < len(betas) else "down", "plaquette": float(pl.mean()),
                     "err": float(pl.reshape(10, -1).mean(axis=1).std(ddof=1) / np.sqrt(10))})
        print(rows[-1], flush=True)
    json.dump({"L": 8, "rows": rows, "flop": flop(lat), "link_updates": lat.link_updates},
              open(os.path.join(RES, "su2_cycle.json"), "w"), indent=1)


def heat_one(beta):
    lat = SU2Lattice(8, beta, int(100 * beta) + 77)
    for _ in range(200):
        lat.sweep()
    pl = []
    for _ in range(1000):
        lat.sweep()
        pl.append(lat.plaquette())
    return {"beta": beta, "plaq": pl, "flop": flop(lat), "link_updates": lat.link_updates}


def heat():
    betas = [1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5]
    with Pool(len(betas)) as pool:
        res = pool.map(heat_one, betas)
    json.dump({"L": 8, "runs": res}, open(os.path.join(RES, "su2_heat.json"), "w"))
    for r in res:
        p = np.array(r["plaq"])
        print(r["beta"], p.mean(), 6 * 8 ** 4 * p.var(), flush=True)


if __name__ == "__main__":
    if sys.argv[1] == "loops" and len(sys.argv) > 2:
        loops([float(b) for b in sys.argv[2:]])     # e.g. python3 su2_runs.py loops 1.5 1.6 1.7
    else:
        {"loops": loops, "cycle": cycle, "heat": heat, "fv": fv}[sys.argv[1]]()
