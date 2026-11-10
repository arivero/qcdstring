"""Z2 lattice gauge theory in three dimensions at finite temperature
(1982 paper): a periodic lattice of Nt x Lx x Ly sites with a short
time extent Nt = 1/T.

U[mu] is an int8 array of shape (Nt, Lx, Ly); mu = 0 is time.
Action S = -beta sum_P U_P; heat bath as in the 1976 programs (z2core.py).

Differences from z2core.py:
  * rectangular space and any Nt, including odd Nt. Links of one direction
    are updated in classes that share no plaquette. With even extents two
    classes suffice; an odd extent needs three (colours 0,1,0,1,...,2 along
    that axis, class = sum of the colours of the two perpendicular
    coordinates mod 3).
  * slabs of unequal thickness for the two-level average.
  * the closed time-like line ("Polyakov line") P(x,y) = prod_t U_0(t,x,y),
    its wall sums, and the wall-wall correlator
        G(dx) = (1/Lx Ly) sum_{x,y} sum_{dy} P(x,y) P(x+dx, y+dy),
    whose decay in dx is governed by the states of a closed flux tube of
    length Nt with zero transverse momentum.

Cost model as in 1976: 20 operations per link update, one per
multiply-add in the measurements.
"""
import numpy as np

FLOP_PER_LINK_UPDATE = 20


def axis_colours(n):
    c = np.arange(n) % 2
    if n % 2 == 1 and n > 1:
        c[-1] = 2
    return c


def class_masks(shape):
    """masks[mu]: list of boolean arrays, the update classes of the mu-links."""
    masks = []
    for mu in range(3):
        perp = [nu for nu in range(3) if nu != mu]
        odd = any(shape[nu] % 2 == 1 and shape[nu] > 1 for nu in perp)
        tot = np.zeros(shape, dtype=np.int64)
        for nu in perp:
            if shape[nu] == 1:
                continue          # a direction of extent 1 gives no neighbour
            c = axis_colours(shape[nu]) if odd else np.arange(shape[nu]) % 2
            sh = [1, 1, 1]
            sh[nu] = shape[nu]
            tot = tot + c.reshape(sh)
        k = 3 if odd else 2
        masks.append([(tot % k) == j for j in range(k)])
    return masks


def staples(U, mu):
    """Sum of the four staples of every mu-link."""
    S = np.zeros(U.shape[1:], dtype=np.int8)
    Umu = U[mu]
    for nu in range(3):
        if nu == mu:
            continue
        Unu = U[nu]
        Unu_xmu = np.roll(Unu, -1, axis=mu)
        S += Unu_xmu * np.roll(Umu, -1, axis=nu) * Unu
        S += np.roll(Unu_xmu, 1, axis=nu) * np.roll(Umu, 1, axis=nu) * np.roll(Unu, 1, axis=nu)
    return S


class Z2FT:
    def __init__(self, Nt, Lx, Ly, beta, seed, slabs=None, hot=False):
        self.Nt, self.Lx, self.Ly, self.beta = Nt, Lx, Ly, beta
        self.shape = (Nt, Lx, Ly)
        self.rng = np.random.default_rng(seed)
        if hot:
            self.U = self.rng.choice(np.array([-1, 1], dtype=np.int8), size=(3,) + self.shape)
        else:
            self.U = np.ones((3,) + self.shape, dtype=np.int8)
        self.masks = class_masks(self.shape)
        self.ptab = 1.0 / (1.0 + np.exp(-2.0 * beta * np.arange(-4, 5)))
        self.link_updates = 0
        self.meas_ops = 0
        self.slabs = None
        if slabs is not None:
            assert sum(slabs) == Nt
            self.slabs = list(slabs)
            self.bounds = np.concatenate([[0], np.cumsum(slabs)])[:-1]      # frozen slices
            frozen = np.zeros(self.shape, dtype=bool)
            frozen[self.bounds] = True
            self.sub_masks = []
            for mu in range(3):
                self.sub_masks.append([m & ~frozen if mu != 0 else m for m in self.masks[mu]])

    def sweep(self, frozen=False):
        masks = self.sub_masks if frozen else self.masks
        U = self.U
        for mu in range(3):
            for m in masks[mu]:
                S = staples(U, mu)
                pp = self.ptab[S[m] + 4]
                U[mu][m] = np.where(self.rng.random(pp.shape) < pp, 1, -1).astype(np.int8)
                self.link_updates += int(m.sum())

    def plaquette_sum(self):
        """Sum of U_P over all plaquettes (the energy conjugate to beta)."""
        U, tot = self.U, 0
        for mu in range(3):
            for nu in range(mu + 1, 3):
                P = U[mu] * np.roll(U[nu], -1, axis=mu) * np.roll(U[mu], -1, axis=nu) * U[nu]
                tot += int(P.sum(dtype=np.int64))
        return tot

    def polyakov(self):
        """P(x,y), +-1."""
        return self.U[0].prod(axis=0, dtype=np.int8)

    def slab_lines(self):
        """Product of the time-like links of each slab: (nslab, Lx, Ly) float."""
        out = []
        t0 = 0
        for tau in self.slabs:
            out.append(self.U[0][t0:t0 + tau].prod(axis=0, dtype=np.int8))
            t0 += tau
        return np.array(out, dtype=np.float64)


def wall_corr_plain(P, X):
    """G(dx), dx = 0..X, from one configuration of Polyakov lines P(x,y):
    correlator of the wall sums over y, averaged over x, normalized so that
    G(dx) = sum_dy <P(0,0) P(dx,dy)>."""
    w = P.sum(axis=1, dtype=np.float64)                 # wall sums, (Lx,)
    Ly = P.shape[1]
    return np.array([(w * np.roll(w, -dx)).mean() for dx in range(X + 1)]) / Ly


def two_level_wall(lat, n_sub, X):
    """One two-level estimate of G(dx), dx = 0..X. The slab averages of the
    products l_s(x,y) l_s(x+dx,y+dy) are accumulated for every position and
    every displacement, multiplied over the slabs, and only then summed over
    positions and dy. Unbiased for any n_sub."""
    ns, Lx, Ly = len(lat.slabs), lat.Lx, lat.Ly
    acc = np.zeros((ns, X + 1, Lx, Ly, Ly))             # slab, dx, x, y, dy
    idx = (np.arange(Ly)[:, None] + np.arange(Ly)[None, :]) % Ly      # idx[y, dy] = y + dy
    for _ in range(n_sub):
        lat.sweep(frozen=True)
        l = lat.slab_lines()
        for dx in range(X + 1):
            acc[:, dx] += l[:, :, :, None] * np.roll(l, -dx, axis=1)[:, :, idx]
        lat.meas_ops += ns * (X + 1) * Ly * Lx * Ly + lat.Nt * Lx * Ly
    est = (acc / n_sub).prod(axis=0)                    # (X+1, Lx, Ly, Ly)
    lat.meas_ops += ns * (X + 1) * Ly * Lx * Ly
    return est.sum(axis=3).mean(axis=(1, 2))            # sum over dy, mean over positions
