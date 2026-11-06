#!/usr/bin/env python3
"""Compact U(1) lattice gauge theory in four dimensions (Section 4).

Links U = exp(i theta) on an L^4 periodic lattice, Wilson action
S = -beta sum_P cos theta_P. Heat bath: given the staple sum K of a link,
theta is drawn from the von Mises density exp(beta |K| cos(theta + arg K)),
which numpy samples directly. Wilson loops use, for R >= 2, the
conditional mean of each link on the two T-sides, I_1(beta|K|)/I_0(beta|K|)
times K*/|K| [MEMORY: Parisi, Petronzio and Rapuano 1983].

    python3 u1_4d.py cycle            # thermal cycle on 8^4 (hysteresis)
    python3 u1_4d.py loops            # Wilson loops on 10^4 at nine couplings
Writes ../results/u1_cycle.json and ../results/u1_loops.json."""
import json, math, os, sys, time
import numpy as np
from scipy.special import i0e, i1e

FLOP_PER_LINK_UPDATE = 300   # 6 staples of 3 complex products, von Mises draw
FLOP_PER_MEAS_OP = 6         # one complex multiply-add

HERE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(HERE, "..", "results")


class U1Lattice:
    def __init__(self, L, beta, seed, hot=False):
        self.L, self.beta = L, beta
        self.rng = np.random.default_rng(seed)
        shape = (4,) + (L,) * 4
        th = self.rng.uniform(-math.pi, math.pi, shape) if hot else np.zeros(shape)
        self.U = np.exp(1j * th)
        idx = np.indices((L,) * 4)
        self.masks = []
        for mu in range(4):
            perp = sum(idx[nu] for nu in range(4) if nu != mu) % 2
            self.masks.append([perp == 0, perp == 1])
        self.link_updates = 0
        self.meas_ops = 0

    def staple(self, mu):
        U = self.U
        K = np.zeros(U.shape[1:], dtype=np.complex128)
        for nu in range(4):
            if nu == mu:
                continue
            Unu_xmu = np.roll(U[nu], -1, axis=mu)
            K += Unu_xmu * np.conj(np.roll(U[mu], -1, axis=nu)) * np.conj(U[nu])
            K += np.conj(np.roll(Unu_xmu, 1, axis=nu)) * np.conj(np.roll(U[mu], 1, axis=nu)) * np.roll(U[nu], 1, axis=nu)
        return K

    def sweep(self):
        for mu in range(4):
            for p in range(2):
                m = self.masks[mu][p]
                K = self.staple(mu)[m]
                kap = self.beta * np.abs(K)
                th = self.rng.vonmises(-np.angle(K), kap)
                self.U[mu][m] = np.exp(1j * th)
                self.link_updates += int(m.sum())

    def plaquette(self):
        U, tot = self.U, 0.0
        for mu in range(4):
            for nu in range(mu + 1, 4):
                P = U[mu] * np.roll(U[nu], -1, axis=mu) * np.conj(np.roll(U[mu], -1, axis=nu)) * np.conj(U[nu])
                tot += P.real.mean()
        return tot / 6

    def improved(self, nu):
        K = self.staple(nu)
        k = np.abs(K)
        x = self.beta * k
        return (i1e(x) / i0e(x)) * np.conj(K) / np.where(k > 0, k, 1.0)

    def wilson(self, Rmax, Tmax):
        """W[R-1,T-1] averaged over the 12 ordered planes and all positions."""
        U = self.U
        L4 = self.L ** 4
        W = np.zeros((Rmax, Tmax))
        imp = [self.improved(nu) for nu in range(4)]
        self.meas_ops += 4 * 6 * 3 * L4
        def lines(V, mu, nmax):
            out, P = [None], np.ones(V.shape, dtype=np.complex128)
            for n in range(1, nmax + 1):
                P = P * np.roll(V, -(n - 1), axis=mu)
                out.append(P.copy())
            return out
        raw = [lines(U[mu], mu, max(Rmax, Tmax)) for mu in range(4)]
        mh = [lines(imp[mu], mu, Tmax) for mu in range(4)]
        self.meas_ops += 8 * max(Rmax, Tmax) * L4
        n = 0
        for mu in range(4):
            for nu in range(4):
                if nu == mu:
                    continue
                for R in range(1, Rmax + 1):
                    S = raw[mu][R]
                    Tl = raw[nu] if R == 1 else mh[nu]
                    for T in range(1, Tmax + 1):
                        loop = S * np.roll(Tl[T], -R, axis=mu) * np.conj(np.roll(S, -T, axis=nu)) * np.conj(Tl[T])
                        W[R - 1, T - 1] += loop.real.mean()
                self.meas_ops += 5 * Rmax * Tmax * L4
                n += 1
        return W / n


def cycle():
    L, nth, nme = 8, 100, 100
    betas = [round(0.70 + 0.05 * i, 3) for i in range(13)]
    path = betas + betas[::-1]
    lat = U1Lattice(L, betas[0], 1976, hot=True)
    for _ in range(200):
        lat.sweep()
    rows = []
    t0 = time.time()
    for leg, b in enumerate(path):
        lat.beta = b
        for _ in range(nth):
            lat.sweep()
        pl = []
        for _ in range(nme):
            lat.sweep()
            pl.append(lat.plaquette())
        pl = np.array(pl)
        blk = pl.reshape(10, -1).mean(axis=1)
        rows.append({"beta": b, "direction": "up" if leg < len(betas) else "down",
                     "plaquette": float(pl.mean()), "err": float(blk.std(ddof=1) / math.sqrt(10))})
        print(f"{rows[-1]['direction']:4s} beta {b:.3f}  <cos theta_P> = {pl.mean():.4f} +/- {rows[-1]['err']:.4f}", flush=True)
    out = {"L": L, "therm_per_point": nth, "meas_per_point": nme, "rows": rows,
           "link_updates": lat.link_updates, "flop": lat.link_updates * FLOP_PER_LINK_UPDATE + 8 * lat.meas_ops,
           "seconds": time.time() - t0}
    json.dump(out, open(os.path.join(RES, "u1_cycle.json"), "w"), indent=1)


def two_starts():
    """Referee check (Minor 3): beta = 1.00 on 8^4 from a hot and a cold start,
    2500 sweeps each, plaquette after every sweep."""
    out = {}
    for start in ("hot", "cold"):
        lat = U1Lattice(8, 1.00, 4242, hot=(start == "hot"))
        pl = []
        for _ in range(2500):
            lat.sweep()
            pl.append(lat.plaquette())
        out[start] = {"plaq": pl, "flop": lat.link_updates * FLOP_PER_LINK_UPDATE + 8 * 6 * 3 * 6 * 4096 * 2500}
        p = np.array(pl[500:])
        print(f"{start} start: <cos theta_P> over sweeps 500-2500 = {p.mean():.4f}, min {p.min():.4f}, max {p.max():.4f}", flush=True)
    json.dump(out, open(os.path.join(RES, "u1_two_starts.json"), "w"))


def loops_one(b, L=10, therm=300, nmeas=400, every=2, Rmax=4, seed=0):
    lat = U1Lattice(L, b, 2000 + seed, hot=(b < 1.0))
    for _ in range(therm):
        lat.sweep()
    Ws, pl = [], []
    for _ in range(nmeas):
        for _ in range(every):
            lat.sweep()
        pl.append(lat.plaquette())
        Ws.append(lat.wilson(Rmax, Rmax))
    return {"beta": b, "L": L, "therm": therm, "nmeas": nmeas, "every": every,
            "W": np.array(Ws).tolist(), "plaq": pl, "link_updates": lat.link_updates,
            "flop": lat.link_updates * FLOP_PER_LINK_UPDATE + lat.meas_ops * FLOP_PER_MEAS_OP}


def loops():
    from multiprocessing import Pool
    betas = [0.60, 0.80, 0.90, 0.95, 1.00, 1.05, 1.10, 1.20, 1.40]
    with Pool(len(betas)) as pool:
        res = pool.map(loops_one, betas)
    json.dump(res, open(os.path.join(RES, "u1_loops.json"), "w"))
    for r in res:
        print(r["beta"], "plaq", np.mean(r["plaq"]), "flop %.2e" % r["flop"])


if __name__ == "__main__":
    {"cycle": cycle, "loops": loops, "two_starts": two_starts}[sys.argv[1]]()
