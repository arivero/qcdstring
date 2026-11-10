#!/usr/bin/env python3
"""SU(2) lattice gauge theory in four dimensions at finite temperature
(1982 paper): Nt x L^3 lattices, heat bath as in the 1978 programs
(su2core.py), and the closed time-like line

    P(x) = (1/2) Tr prod_t U_0(t, x).

A link is a unit quaternion; U has shape (4 directions, 4 components,
Nt, L, L, L); direction 0 is time. Links of one direction are updated in
classes that share no plaquette: two classes when all extents are even,
three when Nt is odd (colours 0,1,...,2 along the odd axis, class = sum of
the colours of the three perpendicular coordinates mod 3).

    python3 su2ft.py --Nt 4 --L 8 --beta 2.30 --nsweep 10000 --seed 1

stores the time series of the lattice average of P, of |P| averaged over
sites, and of the plaquette, in ../results/su2ft_Nt<Nt>_L<L>_b<beta>_s<seed>.npz

Cost model as in 1978: 500 operations per link update, 28 per quaternion
product in the measurements."""
import argparse, os, sys, time
import numpy as np

FLOP_PER_LINK_UPDATE = 500
FLOP_PER_QMUL = 28
HERE = os.path.dirname(os.path.abspath(__file__))


def qmul(a, b):
    a0, a1, a2, a3 = a
    b0, b1, b2, b3 = b
    return np.stack([a0 * b0 - a1 * b1 - a2 * b2 - a3 * b3,
                     a0 * b1 + a1 * b0 - a2 * b3 + a3 * b2,
                     a0 * b2 + a2 * b0 - a3 * b1 + a1 * b3,
                     a0 * b3 + a3 * b0 - a1 * b2 + a2 * b1])


def qconj(a):
    return a * np.array([1.0, -1.0, -1.0, -1.0]).reshape((4,) + (1,) * (a.ndim - 1))


def shift(f, mu, s):
    return np.roll(f, -s, axis=mu + 1)


def axis_colours(n):
    c = np.arange(n) % 2
    if n % 2 == 1 and n > 1:
        c[-1] = 2
    return c


class SU2FT:
    def __init__(self, Nt, L, beta, seed, hot=False):
        self.Nt, self.L, self.beta = Nt, L, beta
        self.shape = (Nt, L, L, L)
        self.V = Nt * L ** 3
        self.rng = np.random.default_rng(seed)
        shp = (4, 4) + self.shape
        if hot:
            U = self.rng.normal(size=shp)
            U /= np.linalg.norm(U, axis=1, keepdims=True)
        else:
            U = np.zeros(shp)
            U[:, 0] = 1.0
        self.U = U
        self.masks = []
        for mu in range(4):
            perp = [nu for nu in range(4) if nu != mu]
            odd = any(self.shape[nu] % 2 == 1 for nu in perp)
            tot = np.zeros(self.shape, dtype=np.int64)
            for nu in perp:
                c = axis_colours(self.shape[nu]) if odd else np.arange(self.shape[nu]) % 2
                sh = [1, 1, 1, 1]
                sh[nu] = self.shape[nu]
                tot = tot + c.reshape(sh)
            k = 3 if odd else 2
            self.masks.append([(tot % k) == j for j in range(k)])
        self.link_updates = 0
        self.ops = 0.0

    def staple_sum(self, mu):
        U = self.U
        V = np.zeros_like(U[mu])
        for nu in range(4):
            if nu == mu:
                continue
            a = shift(U[nu], mu, 1)
            V += qmul(qmul(a, qconj(shift(U[mu], nu, 1))), qconj(U[nu]))
            b = shift(a, nu, -1)
            V += qmul(qmul(qconj(b), qconj(shift(U[mu], nu, -1))), shift(U[nu], nu, -1))
        return V

    def _draw_a0(self, alpha):
        n = alpha.size
        a0 = np.empty(n)
        todo = np.arange(n)
        while todo.size:
            al = alpha[todo]
            r1, r2, r3, r4 = (1.0 - self.rng.random((4, todo.size)))
            lam2 = -(np.log(r1) + np.cos(2 * np.pi * r2) ** 2 * np.log(r3)) / (2 * al)
            ok = r4 * r4 <= 1 - lam2
            a0[todo[ok]] = 1 - 2 * lam2[ok]
            todo = todo[~ok]
        return a0

    def sweep(self):
        for mu in range(4):
            for m in self.masks[mu]:
                V = self.staple_sum(mu)[:, m]
                k = np.sqrt((V * V).sum(axis=0))
                a0 = self._draw_a0(self.beta * k)
                cth = 2 * self.rng.random(a0.size) - 1
                phi = 2 * np.pi * self.rng.random(a0.size)
                s = np.sqrt(np.maximum(1 - a0 * a0, 0.0))
                sth = np.sqrt(1 - cth * cth)
                a = np.stack([a0, s * sth * np.cos(phi), s * sth * np.sin(phi), s * cth])
                Unew = qmul(a, qconj(V) / k)
                Unew /= np.linalg.norm(Unew, axis=0, keepdims=True)
                self.U[mu][:, m] = Unew
                self.link_updates += int(m.sum())

    def plaquette(self):
        U, tot = self.U, 0.0
        for mu in range(4):
            for nu in range(mu + 1, 4):
                P = qmul(qmul(U[mu], shift(U[nu], mu, 1)), qconj(qmul(U[nu], shift(U[mu], nu, 1))))
                tot += P[0].mean()
        self.ops += 6 * 3 * FLOP_PER_QMUL * self.V
        return tot / 6

    def polyakov(self):
        """P(x) = Tr/2 of the product of the time-like links: array (L, L, L)."""
        U0 = self.U[0]
        P = U0[:, 0]
        for t in range(1, self.Nt):
            P = qmul(P, U0[:, t])
        self.ops += (self.Nt - 1) * FLOP_PER_QMUL * self.L ** 3
        return P[0]

    def flop(self):
        return self.link_updates * FLOP_PER_LINK_UPDATE + self.ops


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--Nt", type=int, required=True)
    ap.add_argument("--L", type=int, required=True)
    ap.add_argument("--beta", type=float, required=True)
    ap.add_argument("--nsweep", type=int, default=5000)
    ap.add_argument("--therm", type=int, default=500)
    ap.add_argument("--hot", action="store_true")
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--tag", default="")
    ap.add_argument("--outdir", default=os.path.join(HERE, "..", "results"))
    a = ap.parse_args()
    t0 = time.time()
    lat = SU2FT(a.Nt, a.L, a.beta, 823000 + 100 * a.Nt + a.seed, hot=a.hot)
    for _ in range(a.therm):
        lat.sweep()
    pol, apol, plq = [], [], []
    for i in range(a.nsweep):
        lat.sweep()
        P = lat.polyakov()
        pol.append(float(P.mean())); apol.append(float(np.abs(P).mean()))
        plq.append(float(lat.plaquette()))
    name = f"su2ft_Nt{a.Nt}_L{a.L}_b{a.beta:.4f}_s{a.seed}{a.tag}.npz"
    np.savez(os.path.join(a.outdir, name), pol=np.array(pol), apol=np.array(apol), plq=np.array(plq), beta=a.beta,
             Nt=a.Nt, L=a.L, nsweep=a.nsweep, therm=a.therm, hot=a.hot, link_updates=lat.link_updates,
             flop=lat.flop(), seconds=time.time() - t0)
    print(f"wrote {name}: plaq {np.mean(plq):.5f} <|P|> {np.mean(np.abs(pol)):.4f} {lat.flop():.3e} flop, {time.time()-t0:.0f} s", flush=True)


if __name__ == "__main__":
    main()
