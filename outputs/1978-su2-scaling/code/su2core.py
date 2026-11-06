"""SU(2) lattice gauge theory in four dimensions: heat bath, one-link
averages, spatial smearing and Wilson loops (1978 paper).

A link is a unit quaternion a = (a0, a1, a2, a3) <-> U = a0 + i a.sigma.
Arrays have shape (4, L, L, L, L) per direction; U has shape
(4 directions, 4 components, L, L, L, L). Wilson action
S = beta sum_P (1 - Tr U_P / 2), beta = 4/g^2.

Heat bath: given the staple sum V (a quaternion of norm k), the link is
U = a V^dagger/k with a0 drawn from sqrt(1-a0^2) exp(beta k a0)
(Kennedy-Pendleton rejection [MEMORY: 1985]; Creutz's 1980 algorithm
samples the same density) and the other components uniform on a sphere.
"""
import math
import numpy as np
from scipy.special import ive

# Cost model, flop-equivalents (see ../README.md and the paper's Appendix A)
FLOP_PER_LINK_UPDATE = 500     # 6 staples x 2 products x 28, sum, draw, product, normalization
FLOP_PER_QMUL = 28             # one quaternion product
FLOP_ONE_LINK_AVERAGE = 400    # staples + Bessel ratio


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
    """f(x + s mu) for a field with the quaternion index first."""
    return np.roll(f, -s, axis=mu + 1)


class SU2Lattice:
    def __init__(self, L, beta, seed, hot=False):
        self.L, self.beta = L, beta
        self.rng = np.random.default_rng(seed)
        shape = (4, 4) + (L,) * 4
        if hot:
            U = self.rng.normal(size=shape)
            U /= np.linalg.norm(U, axis=1, keepdims=True)
        else:
            U = np.zeros(shape)
            U[:, 0] = 1.0
        self.U = U
        idx = np.indices((L,) * 4)
        self.masks = []
        for mu in range(4):
            perp = sum(idx[nu] for nu in range(4) if nu != mu) % 2
            self.masks.append([perp == 0, perp == 1])
        self.link_updates = 0
        self.ops = 0.0      # measurement operations, flop-equivalents

    def staple_sum(self, mu):
        """V with Tr(U_mu(x) V) summing the six plaquettes containing U_mu(x)."""
        U = self.U
        V = np.zeros_like(U[mu])
        for nu in range(4):
            if nu == mu:
                continue
            a = shift(U[nu], mu, 1)                       # U_nu(x+mu)
            V += qmul(qmul(a, qconj(shift(U[mu], nu, 1))), qconj(U[nu]))
            b = shift(a, nu, -1)                          # U_nu(x+mu-nu)
            V += qmul(qmul(qconj(b), qconj(shift(U[mu], nu, -1))), shift(U[nu], nu, -1))
        return V

    def _draw_a0(self, alpha):
        """a0 with density sqrt(1-a0^2) exp(alpha a0), vectorized rejection."""
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
            for p in range(2):
                m = self.masks[mu][p]
                V = self.staple_sum(mu)[:, m]
                k = np.sqrt((V * V).sum(axis=0))
                a0 = self._draw_a0(self.beta * k)
                # uniform direction for (a1, a2, a3)
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
        self.ops += 6 * 3 * FLOP_PER_QMUL * self.L ** 4
        return tot / 6

    def one_link_average(self, mu):
        """Conditional mean of every mu-link given its staples:
        <U> = [I_2(beta k)/I_1(beta k)] V^dagger / k  [MEMORY: Parisi, Petronzio, Rapuano 1983]."""
        V = self.staple_sum(mu)
        k = np.sqrt((V * V).sum(axis=0))
        x = self.beta * k
        self.ops += FLOP_ONE_LINK_AVERAGE * self.L ** 4
        return (ive(2, x) / ive(1, x) / k) * qconj(V)

    def smeared_spatial(self, t_dir, n_iter, c=0.5):
        """Smearing of the links orthogonal to t_dir within each time slice:
        U_i <- normalize(U_i + c * sum of the 4 spatial staples)
        [MEMORY: Albanese et al. (APE) 1987]."""
        sp = [d for d in range(4) if d != t_dir]
        S = {i: self.U[i].copy() for i in sp}
        for _ in range(n_iter):
            new = {}
            for i in sp:
                acc = S[i].copy()
                for j in sp:
                    if j == i:
                        continue
                    # x -> x+j -> x+j+i -> x+i
                    acc += c * qmul(qmul(S[j], shift(S[i], j, 1)), qconj(shift(S[j], i, 1)))
                    # x -> x-j -> x-j+i -> x+i
                    bj = shift(S[j], j, -1)
                    acc += c * qmul(qmul(qconj(bj), shift(S[i], j, -1)), shift(bj, i, 1))
                new[i] = acc / np.linalg.norm(acc, axis=0, keepdims=True)
            S = new
            self.ops += 3 * 4 * 2 * FLOP_PER_QMUL * self.L ** 4
        return S

    def wilson_loops(self, Rmax, Tmax, n_smear, t_dir=0, improved=True):
        """W[R-1, T-1]: time along t_dir, spatial sides from smeared links,
        time-like sides from one-link averages when R >= 2. Averaged over
        all positions and the three spatial directions."""
        L4 = self.L ** 4
        S = self.smeared_spatial(t_dir, n_smear) if n_smear > 0 else {i: self.U[i] for i in range(4) if i != t_dir}
        Ut_raw = self.U[t_dir]
        Ut_avg = self.one_link_average(t_dir) if improved else Ut_raw
        def lines(F, d, n):
            out, P = [None], None
            for k in range(1, n + 1):
                f = shift(F, d, k - 1)
                P = f.copy() if P is None else qmul(P, f)
                out.append(P)
            self.ops += n * FLOP_PER_QMUL * L4
            return out
        Tr = lines(Ut_raw, t_dir, Tmax)
        Ta = lines(Ut_avg, t_dir, Tmax)
        W = np.zeros((Rmax, Tmax))
        for i in S:
            Sl = lines(S[i], i, Rmax)
            for R in range(1, Rmax + 1):
                T_ = Tr if R == 1 else Ta
                for T in range(1, Tmax + 1):
                    P1 = qmul(Sl[R], shift(T_[T], i, R))           # x -> x+R -> up T
                    P2 = qmul(T_[T], shift(Sl[R], t_dir, T))       # x -> up T -> x+R
                    W[R - 1, T - 1] += (P1 * P2).sum(axis=0).mean()
                self.ops += Tmax * (2 * FLOP_PER_QMUL + 8) * L4
        return W / len(S)
