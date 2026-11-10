"""Three-dimensional Ising model on an Nt x Lx x Ly lattice, periodic in t
and x, periodic or antiperiodic in y (1982 paper).

Wegner's duality maps the Z2 gauge theory at coupling beta onto this model
at tanh(beta) = exp(-2K). A closed surface of the strong-coupling expansion
that wraps the (t, x) torus once is the world sheet of a flux tube of
length Nt that travels once around x; in the Ising model it is an interface
forced by the antiperiodic boundary. Hence

    Z_A / Z_P = sum over flux-tube states n of exp(-E_n(Nt) Lx)  (up to
                exponentially small terms),
    F(K) = -ln(Z_A/Z_P) = int_0^K [ <S>_P - <S>_A ] dK',

with S = sum over bonds of eps_b s_i s_j (eps_b = -1 on the seam bonds of
the antiperiodic lattice), because d ln Z / dK = <S>.

Heat bath in classes that share no bond: two classes when every extent is
even, three when one is odd (colours 0,1,0,1,...,2 along an odd axis,
class = sum of colours mod 3). A direction of extent 1 carries no bond.

Cost model as in 1980: 10 operations per spin update; 3 per site for each
measurement of S.
"""
import numpy as np

FLOP_PER_SPIN_UPDATE = 10
FLOP_PER_SITE_MEAS = 3


def axis_colours(n):
    c = np.arange(n) % 2
    if n % 2 == 1 and n > 1:
        c[-1] = 2
    return c


class IsingTwist:
    def __init__(self, Nt, Lx, Ly, K, seed, antiperiodic=False, hot=None):
        self.shape = (Nt, Lx, Ly)
        self.K = K
        self.rng = np.random.default_rng(seed)
        self.anti = antiperiodic
        self.V = Nt * Lx * Ly
        if hot is None:
            hot = K < 0.2217          # start disordered below the bulk critical coupling
        if hot:
            self.s = self.rng.choice(np.array([-1, 1], dtype=np.int8), size=self.shape)
        else:
            self.s = np.ones(self.shape, dtype=np.int8)
        self.axes = [ax for ax in range(3) if self.shape[ax] > 1]
        odd = any(self.shape[ax] % 2 == 1 for ax in self.axes)
        tot = np.zeros(self.shape, dtype=np.int64)
        for ax in self.axes:
            c = axis_colours(self.shape[ax]) if odd else np.arange(self.shape[ax]) % 2
            sh = [1, 1, 1]
            sh[ax] = self.shape[ax]
            tot = tot + c.reshape(sh)
        k = 3 if odd else 2
        self.masks = [(tot % k) == j for j in range(k)]
        self.nb_max = 2 * len(self.axes)
        self.set_K(K)
        self.spin_updates = 0
        self.meas_ops = 0

    def set_K(self, K):
        self.K = K
        self.ptab = 1.0 / (1.0 + np.exp(-2.0 * K * np.arange(-self.nb_max, self.nb_max + 1)))

    def _fwd(self, ax):
        """s(x + e_ax) with the seam sign when ax = y."""
        f = np.roll(self.s, -1, axis=ax)
        if ax == 2 and self.anti:
            f = f.copy()
            f[:, :, -1] *= -1
        return f

    def _bwd(self, ax):
        b = np.roll(self.s, 1, axis=ax)
        if ax == 2 and self.anti:
            b = b.copy()
            b[:, :, 0] *= -1
        return b

    def field(self):
        h = np.zeros(self.shape, dtype=np.int8)
        for ax in self.axes:
            h += self._fwd(ax)
            h += self._bwd(ax)
        return h

    def sweep(self):
        for m in self.masks:
            h = self.field()
            p = self.ptab[h[m] + self.nb_max]
            self.s[m] = np.where(self.rng.random(p.shape) < p, 1, -1).astype(np.int8)
        self.spin_updates += self.V

    def bond_sum(self):
        """S = sum_b eps_b s_i s_j."""
        tot = 0
        for ax in self.axes:
            tot += int((self.s * self._fwd(ax)).sum(dtype=np.int64))
        self.meas_ops += FLOP_PER_SITE_MEAS * self.V
        return tot

    def magnetization(self):
        return int(self.s.sum(dtype=np.int64))

    def flop(self):
        return self.spin_updates * FLOP_PER_SPIN_UPDATE + self.meas_ops


def run_point(Nt, Lx, Ly, K, anti, nsweep, therm, seed, hot=None, every=1):
    """Time series of S (and of M for the periodic lattice)."""
    lat = IsingTwist(Nt, Lx, Ly, K, seed, antiperiodic=anti, hot=hot)
    for _ in range(therm):
        lat.sweep()
    n = nsweep // every
    S = np.empty(n, dtype=np.int64)
    M = np.empty(n, dtype=np.int64)
    for i in range(n):
        for _ in range(every):
            lat.sweep()
        S[i] = lat.bond_sum()
        M[i] = lat.magnetization()
    return S, M, lat.flop()


# ---------------------------------------------------------------- exact two-dimensional results
def kaufman_lnZ(M, N, K):
    """ln of the four partition functions of the M x N Ising torus at coupling K
    (Kaufman 1949): boundary conditions (along M, along N) = pp, pa, ap, aa,
    where 'a' is antiperiodic. Checked against direct enumeration in checks82.py."""
    def gam(l):
        c = np.cosh(2 * K) / np.tanh(2 * K) - np.cos(np.pi * l / N)
        g = np.arccosh(c)
        if l == 0:
            g = 2 * K + np.log(np.tanh(K))          # signed
        return g
    odd = np.array([gam(2 * r + 1) for r in range(N)])
    even = np.array([gam(2 * r) for r in range(N)])
    ln1 = np.sum(np.log(2 * np.cosh(M * odd / 2)))
    ln2 = np.sum(np.log(2 * np.sinh(M * odd / 2)))
    ln3 = np.sum(np.log(2 * np.cosh(M * even / 2)))
    s4 = np.prod(np.sign(np.sinh(M * even / 2)))
    ln4 = np.sum(np.log(np.abs(2 * np.sinh(M * even / 2))))
    pref = 0.5 * M * N * np.log(2 * np.sinh(2 * K)) - np.log(2.0)
    ref = max(ln1, ln2, ln3, ln4)
    z = [np.exp(ln1 - ref), np.exp(ln2 - ref), np.exp(ln3 - ref), s4 * np.exp(ln4 - ref)]
    comb = {"pp": (1, 1, 1, 1), "ap": (1, 1, -1, -1), "pa": (1, -1, 1, -1), "aa": (-1, 1, 1, -1)}
    return {k: pref + ref + np.log(sum(c * zi for c, zi in zip(v, z))) for k, v in comb.items()}
