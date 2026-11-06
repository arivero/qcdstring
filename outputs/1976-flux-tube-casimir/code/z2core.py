"""Z2 lattice gauge theory in three dimensions: update and measurement
routines shared by the 1976 programs (and reused in 1980).

Lattice: U[mu] is an int8 array of shape (Nt, L, L) holding +/-1.
Direction 0 is time (extent Nt), directions 1 and 2 are space (extent L).
U[mu][t, x, y] is the link leaving site (t, x, y) in direction mu.
Action S = -beta * sum over plaquettes of U_P.

Heat bath (Glauber 1963): each link is set to +1 with probability
1/(1 + exp(-2 beta h)), with h the sum of its four staples. Links of one
direction and one checkerboard class share no plaquette, so a whole
class is updated at once.

Two-level averaging of time-like line products (Section 3 of the paper):
the space-like links on every tau-th time slice are frozen; between
them the lattice falls into independent slabs, each slab is updated
n_sub times, and the slab averages of products of time-like links are
multiplied together. The estimator is unbiased; its variance falls
exponentially with the number of slabs. [MEMORY: Luscher and Weisz
2001. The algorithm needs nothing that a 1976 machine lacks.]
"""
import numpy as np

# Cost model (flop-equivalents on a CDC 7600, see ../README.md).
FLOP_PER_LINK_UPDATE = 20
FLOP_PER_MEAS_OP = 1


def cold_start(Nt, L):
    return np.ones((3, Nt, L, L), dtype=np.int8)


def checkerboard_masks(shape):
    """masks[mu][p]: links of direction mu whose perpendicular-coordinate
    sum has parity p. Two mu-links in the same class share no plaquette."""
    idx = np.indices(shape)
    masks = []
    for mu in range(3):
        perp = sum(idx[nu] for nu in range(3) if nu != mu) % 2
        masks.append([perp == 0, perp == 1])
    return masks


def staples(U, mu):
    """Sum of the 4 staples attached to every mu-link (values -4..4)."""
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


class Z2Lattice:
    def __init__(self, Nt, L, beta, seed, frozen_tau=None):
        self.Nt, self.L, self.beta = Nt, L, beta
        self.U = cold_start(Nt, L)
        self.rng = np.random.default_rng(seed)
        self.masks = checkerboard_masks((Nt, L, L))
        self.ptab = 1.0 / (1.0 + np.exp(-2.0 * beta * np.arange(-4, 5)))
        self.link_updates = 0
        self.meas_ops = 0
        self.nlinks = 3 * Nt * L * L
        # update masks with the space-like links of every tau-th slice frozen
        self.sub_masks = None
        if frozen_tau:
            t = np.arange(Nt)[:, None, None] * np.ones((1, L, L), dtype=int)
            boundary = (t % frozen_tau == 0)
            self.sub_masks = []
            for mu in range(3):
                pair = []
                for p in range(2):
                    m = self.masks[mu][p].copy()
                    if mu != 0:
                        m &= ~boundary
                    pair.append(m)
                self.sub_masks.append(pair)

    def sweep(self, frozen=False):
        masks = self.sub_masks if frozen else self.masks
        U = self.U
        for mu in range(3):
            for p in range(2):
                m = masks[mu][p]
                S = staples(U, mu)
                pp = self.ptab[S[m] + 4]
                U[mu][m] = np.where(self.rng.random(pp.shape) < pp, 1, -1).astype(np.int8)
                self.link_updates += int(m.sum())

    def plaquette(self):
        U = self.U
        tot, n = 0.0, 0
        for mu in range(3):
            for nu in range(mu + 1, 3):
                P = U[mu] * np.roll(U[nu], -1, axis=mu) * np.roll(U[mu], -1, axis=nu) * U[nu]
                tot += P.mean()
                n += 1
        return tot / n


def wilson_loops(U, Rmax, Tmax, planes=None):
    """W[R-1, T-1] averaged over all positions, all three planes and both
    orientations of the rectangle in each plane (R along mu, T along nu and
    the reverse). Returns float array of shape (Rmax, Tmax)."""
    if planes is None:
        planes = [(0, 1), (0, 2), (1, 2)]
    W = np.zeros((Rmax, Tmax))
    nmax = max(Rmax, Tmax)
    lines = []
    for mu in range(3):
        ls = [None]
        P = np.ones(U.shape[1:], dtype=np.int8)
        for n in range(1, nmax + 1):
            P = P * np.roll(U[mu], -(n - 1), axis=mu)
            ls.append(P.copy())
        lines.append(ls)
    count = 0
    for (a, b) in planes:
        for (mu, nu) in ((a, b), (b, a)):
            for R in range(1, Rmax + 1):
                LmR = lines[mu][R]
                for T in range(1, Tmax + 1):
                    LnT = lines[nu][T]
                    loop = LmR * np.roll(LnT, -R, axis=mu) * np.roll(LmR, -T, axis=nu) * LnT
                    W[R - 1, T - 1] += loop.mean()
            count += 1
    return W / count


def slab_line_products(U, tau):
    """Product of the tau time-like links of each slab at every (x, y):
    shape (Nt//tau, L, L)."""
    Nt, L = U.shape[1], U.shape[2]
    return U[0].reshape(Nt // tau, tau, L, L).prod(axis=1, dtype=np.int8)


def multilevel_polyakov(lat, tau, n_sub, Rmax, multihit=False):
    """One outer measurement of C(R) = <P(0) P(R)> by two-level averaging.
    With multihit=True each time-like link in a slab product is replaced,
    for R >= 2, by its conditional mean tanh(beta h) given its staples
    (the four links of a slab two-line product share no plaquette when
    R >= 2). [MEMORY: Parisi, Petronzio and Rapuano 1983.]
    Returns array (Rmax, 2): direction of separation x or y."""
    Nt, L = lat.Nt, lat.L
    nslab = Nt // tau
    acc = np.zeros((nslab, L, L, Rmax, 2))
    ttab = np.tanh(lat.beta * np.arange(-4, 5))
    for _ in range(n_sub):
        lat.sweep(frozen=True)
        Lk = slab_line_products(lat.U, tau).astype(np.float64)
        if multihit:
            T0 = ttab[staples(lat.U, 0) + 4]
            Lm = T0.reshape(nslab, tau, L, L).prod(axis=1)
            lat.meas_ops += 12 * Nt * L * L
        else:
            Lm = Lk
        acc[:, :, :, 0, 0] += Lk * np.roll(Lk, -1, axis=1)
        acc[:, :, :, 0, 1] += Lk * np.roll(Lk, -1, axis=2)
        for R in range(2, Rmax + 1):
            acc[:, :, :, R - 1, 0] += Lm * np.roll(Lm, -R, axis=1)
            acc[:, :, :, R - 1, 1] += Lm * np.roll(Lm, -R, axis=2)
        lat.meas_ops += 4 * Rmax * nslab * L * L + Nt * L * L
    A = acc / n_sub
    est = A.prod(axis=0)  # (L, L, Rmax, 2)
    lat.meas_ops += nslab * L * L * Rmax * 2
    return est.mean(axis=(0, 1))


def naive_polyakov(lat, Rmax):
    """Direct estimate of C(R) from one configuration (for validation)."""
    P = lat.U[0].prod(axis=0, dtype=np.int8).astype(np.float64)
    out = np.zeros((Rmax, 2))
    for R in range(1, Rmax + 1):
        out[R - 1, 0] = (P * np.roll(P, -R, axis=0)).mean()
        out[R - 1, 1] = (P * np.roll(P, -R, axis=1)).mean()
    return out


def wilson_loops_improved(U, beta, Rmax, Tmax):
    """As wilson_loops, but for R >= 2 every link on the two T-sides is
    replaced by its conditional mean tanh(beta h) given its staples. The
    links so replaced share no plaquette with one another. Valid at all
    couplings; it pays at strong coupling, where tanh(beta h) is far from 1."""
    ttab = np.tanh(beta * np.arange(-4, 5))
    imp = [ttab[staples(U, nu) + 4] for nu in range(3)]
    W = np.zeros((Rmax, Tmax))
    nmax = max(Rmax, Tmax)
    def lines(V, mu, n):
        out, P = [None], np.ones(V.shape)
        for k in range(1, n + 1):
            P = P * np.roll(V, -(k - 1), axis=mu)
            out.append(P.copy())
        return out
    raw = [lines(U[mu].astype(np.float64), mu, nmax) for mu in range(3)]
    mh = [lines(imp[mu], mu, Tmax) for mu in range(3)]
    count = 0
    for mu in range(3):
        for nu in range(3):
            if nu == mu:
                continue
            for R in range(1, Rmax + 1):
                S = raw[mu][R]
                Tl = raw[nu] if R == 1 else mh[nu]
                for T in range(1, Tmax + 1):
                    loop = S * np.roll(Tl[T], -R, axis=mu) * np.roll(S, -T, axis=nu) * Tl[T]
                    W[R - 1, T - 1] += loop.mean()
            count += 1
    return W / count
