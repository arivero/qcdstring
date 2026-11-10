"""Shared analysis routines of the 1982 paper: from the bond sums of the
periodic and antiperiodic Ising lattices to the energy of the closed flux
tube, with errors."""
import glob, math, os
import numpy as np
from scipy.optimize import brentq

HERE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(HERE, "..", "results")


def beta_of_K(K):
    """Gauge coupling dual to the Ising coupling K: tanh(beta) = exp(-2K)."""
    return np.arctanh(np.exp(-2 * np.asarray(K, dtype=float)))


def K_of_beta(beta):
    return -0.5 * np.log(np.tanh(beta))


def binned_error(b, min_bins=10):
    """Error of the mean of the block means b: the largest value found when the
    blocks are merged in pairs repeatedly, down to min_bins bins."""
    errs, nb, k = [], len(b), 1
    while nb // k >= min_bins:
        bb = b[: nb // k * k].reshape(-1, k).mean(axis=1)
        errs.append(bb.std(ddof=1) / math.sqrt(len(bb)))
        k *= 2
    return max(errs), errs[0]


def load_path(names):
    """Join the stretches of one geometry. Returns dict with K (sorted), dS = <S>_P - <S>_A,
    its error e, dvar = var_P - var_A, flop, and the raw block means."""
    rows, flop, meta = {}, 0.0, None
    for nm in names:
        d = np.load(os.path.join(RES, f"path_{nm}.npz"))
        geo = (int(d["Nt"]), int(d["Lx"]), int(d["Ly"]))
        assert meta in (None, geo), "stretches of different geometry"
        meta = geo
        flop += float(d["flop"])
        for i, K in enumerate(d["K"]):
            K = round(float(K), 6)
            sp, sa = d[f"SP_{i}"], d[f"SA_{i}"]
            ep, ep0 = binned_error(sp)
            ea, ea0 = binned_error(sa)
            row = dict(dS=sp.mean() - sa.mean(), e=math.hypot(ep, ea), e_naive=math.hypot(ep0, ea0),
                       dvar=float(d[f"varP_{i}"]) - float(d[f"varA_{i}"]), m2=d[f"m2_{i}"], m4=d[f"m4_{i}"],
                       nP=int(d[f"nP_{i}"]), nA=int(d[f"nA_{i}"]), runs=1)
            if K in rows:                      # a second, independent run at the same coupling
                o = rows[K]
                w1, w2 = 1 / o["e"] ** 2, 1 / row["e"] ** 2
                row = dict(dS=(w1 * o["dS"] + w2 * row["dS"]) / (w1 + w2), e=1 / math.sqrt(w1 + w2),
                           e_naive=1 / math.sqrt(1 / o["e_naive"] ** 2 + 1 / row["e_naive"] ** 2),
                           dvar=0.5 * (o["dvar"] + row["dvar"]), m2=np.concatenate([o["m2"], row["m2"]]),
                           m4=np.concatenate([o["m4"], row["m4"]]), nP=o["nP"] + row["nP"], nA=o["nA"] + row["nA"],
                           runs=o["runs"] + 1, pull=(o["dS"] - row["dS"]) / math.hypot(o["e"], row["e"]))
            rows[K] = row
    Ks = np.array(sorted(rows))
    out = {"Nt": meta[0], "Lx": meta[1], "Ly": meta[2], "K": Ks, "flop": flop, "rows": [rows[k] for k in Ks]}
    for key in ("dS", "e", "e_naive", "dvar"):
        out[key] = np.array([rows[k][key] for k in Ks])
    return out


def free_energy(p, corrected=True):
    """F(K_i) = int_{K_0}^{K_i} dS dK by the trapezoidal rule with the end
    correction -h^2/12 [f'(b) - f'(a)] on every interval (f' = var_P - var_A),
    and the matrix W with F = W @ dS, so that cov(F) = W diag(e^2) W^T."""
    K, dS = p["K"], p["dS"]
    n = len(K)
    W = np.zeros((n, n))
    for i in range(1, n):
        W[i] = W[i - 1]
        h = K[i] - K[i - 1]
        W[i, i - 1] += h / 2
        W[i, i] += h / 2
    F = W @ dS
    if corrected:
        h = np.diff(K)
        F[1:] -= np.cumsum(h ** 2 / 12 * np.diff(p["dvar"]))
    cov = W @ np.diag(p["e"] ** 2) @ W.T
    return F, cov, W


def F_of_E(E, Lx, Ly, lattice=True):
    """-ln(Z_A/Z_P) for a tube of energy E: Z_A/Z_P = (1/2) sum_k exp(-eps_k Lx)
    over the momenta p_k = pi k / Ly, k = 0 .. 2 Ly - 1 (Section 3.2)."""
    p = np.pi * np.arange(2 * Ly) / Ly
    if lattice:
        eps = np.arccosh(np.cosh(E) + 1 - np.cos(p))
    else:
        pp = np.minimum(p, 2 * np.pi - p)
        eps = np.sqrt(E * E + pp * pp)
    return E * Lx - math.log(0.5 * np.sum(np.exp(-Lx * (eps - E))))


def E_of_F(F, Lx, Ly, lattice=True):
    if not np.isfinite(F) or F_of_E(1e-7, Lx, Ly, lattice) >= F:
        return float("nan")
    return brentq(lambda E: F_of_E(E, Lx, Ly, lattice) - F, 1e-7, 8.0, xtol=1e-12)


def tube_energy(p):
    """E_0(K_i) with errors and covariance (linear propagation through E_of_F)."""
    F, cov, W = free_energy(p)
    Lx, Ly = p["Lx"], p["Ly"]
    E = np.array([E_of_F(f, Lx, Ly) for f in F])
    Ec = np.array([E_of_F(f, Lx, Ly, lattice=False) for f in F])
    dEdF = np.full(len(F), np.nan)
    for i, (f, e) in enumerate(zip(F, E)):
        if np.isfinite(e):
            h = 1e-4
            dEdF[i] = (E_of_F(f + h, Lx, Ly) - E_of_F(f - h, Lx, Ly)) / (2 * h)
    J = np.where(np.isfinite(dEdF), dEdF, 0.0)
    covE = (J[:, None] * cov) * J[None, :]
    return dict(K=p["K"], F=F, dF=np.sqrt(np.diag(cov)), E=E, dE=np.sqrt(np.diag(covE)), E_cont=Ec, covE=covE,
                covF=cov, F_plain=free_energy(p, corrected=False)[0])


def interp_at(K, x, cov, Kt):
    """Linear interpolation of x(K) at Kt and its error from the covariance."""
    i = int(np.searchsorted(K, Kt))
    if i == 0 or i >= len(K):
        if i < len(K) and abs(K[i] - Kt) < 1e-9:
            return x[i], math.sqrt(cov[i, i])
        return float("nan"), float("nan")
    if abs(K[i] - Kt) < 1e-9:
        return x[i], math.sqrt(cov[i, i])
    t = (Kt - K[i - 1]) / (K[i] - K[i - 1])
    v = (1 - t) * x[i - 1] + t * x[i]
    var = (1 - t) ** 2 * cov[i - 1, i - 1] + t ** 2 * cov[i, i] + 2 * t * (1 - t) * cov[i - 1, i]
    return v, math.sqrt(max(var, 0.0))


def ng_closed(sigma, L, c=1.0, N=0):
    """Ground level (N = Nbar = 0) of the wound closed string, Appendix A; c towers."""
    x = sigma ** 2 * L ** 2 + 4 * math.pi * sigma * (2 * N - c / 12)
    return math.sqrt(x) if x > 0 else float("nan")


def sigma_from_E(E, L, c=1.0):
    """Invert E^2 = sigma^2 L^2 - pi c sigma / 3."""
    return (math.pi * c / 3 + math.sqrt((math.pi * c / 3) ** 2 + 4 * L ** 2 * E ** 2)) / (2 * L ** 2)


# ---------------------------------------------------------------- cumulant crossings
def tau_int(x):
    """Integrated autocorrelation time with a self-consistent window (W >= 6 tau)."""
    x = np.asarray(x, dtype=float) - np.mean(x)
    n = len(x)
    v = np.mean(x * x)
    if v == 0 or n < 8:
        return 0.5
    f = np.fft.rfft(x, 2 * n)
    acf = np.fft.irfft(f * np.conj(f))[: n // 2] / (n - np.arange(n // 2)) / v
    tau = 0.5
    for t in range(1, n // 2):
        tau += acf[t]
        if t >= 6 * tau:
            break
    return max(tau, 0.5)


class Series:
    """Time series of an order parameter m and of the quantity S conjugate to the
    coupling, from several chains at coupling g0; reweighting to g uses
    exp((g - g0) S). Blocks of at least four autocorrelation times of m^2.
    The reweighted sums are tabulated per block on a grid of couplings, so that
    cumulants and their bootstrap errors cost nothing afterwards."""

    def __init__(self, m, S, g0, half_width, ngrid=61, min_blocks=8):
        m, S = np.atleast_2d(m).astype(float), np.atleast_2d(S).astype(float)
        self.g0 = g0
        self.tau = max(tau_int(c ** 2) for c in m)
        n = m.shape[1]
        blen = int(math.ceil(4 * self.tau))
        nb = max(1, n // blen)
        while m.shape[0] * nb < min_blocks and nb < n:
            nb += 1
        blen = n // nb
        mb = m[:, : nb * blen].reshape(-1, blen)
        Sb = S[:, : nb * blen].reshape(-1, blen)
        self.nb, self.blen, self.sigS = mb.shape[0], blen, float(Sb.std())
        self.g = np.linspace(g0 - half_width, g0 + half_width, ngrid)
        S0 = Sb.mean()
        self.T = np.empty((4, ngrid, self.nb))          # sums of w, w m^2, w m^4, w |m| per block
        for i, g in enumerate(self.g):
            w = np.exp((g - g0) * (Sb - S0))
            self.T[0, i] = w.sum(axis=1)
            self.T[1, i] = (w * mb ** 2).sum(axis=1)
            self.T[2, i] = (w * mb ** 4).sum(axis=1)
            self.T[3, i] = (w * np.abs(mb)).sum(axis=1)

    def curves(self, sel=None):
        """Cumulant, <m^2> and <|m|> on the grid, from all blocks or a resampling of them."""
        T = self.T if sel is None else self.T[:, :, sel]
        s = T.sum(axis=2)
        m2, m4, am = s[1] / s[0], s[2] / s[0], s[3] / s[0]
        return 1 - m4 / (3 * m2 * m2), m2, am

    def cumulant(self, g, sel=None):
        return float(np.interp(g, self.g, self.curves(sel)[0]))

    def boot(self, fn, nboot=200, seed=0):
        rng = np.random.default_rng(seed)
        vals = np.array([fn(rng.integers(0, self.nb, self.nb)) for _ in range(nboot)])
        return np.nanstd(vals, axis=0)


def _cross(ga, ua, gb, ub):
    """Crossing of two cumulant curves nearest the centre of their common range.
    Returns (coupling, found). When the curves do not cross inside the range the
    coupling returned is the end of the range at which they are closest."""
    g = np.linspace(max(ga[0], gb[0]), min(ga[-1], gb[-1]), 400)
    d = np.interp(g, ga, ua) - np.interp(g, gb, ub)
    idx = np.where(np.sign(d[:-1]) * np.sign(d[1:]) < 0)[0]
    if len(idx) == 0:
        return (g[0] if abs(d[0]) < abs(d[-1]) else g[-1]), False
    i = idx[np.argmin(np.abs(idx - len(g) / 2))]
    return g[i] - d[i] * (g[i + 1] - g[i]) / (d[i + 1] - d[i]), True


def crossing(sa, sb, nboot=400, seed=0):
    """Coupling at which the cumulants of two series cross, bootstrap error over
    blocks, the cumulant there, and the fraction of bootstrap samples without a
    crossing inside the reweighting range. Those samples are kept, at the end of
    the range where the curves are closest, so that the error is not truncated."""
    g, found = _cross(sa.g, sa.curves()[0], sb.g, sb.curves()[0])
    rng = np.random.default_rng(seed)
    gs, lost = [], 0
    for _ in range(nboot):
        ia, ib = rng.integers(0, sa.nb, sa.nb), rng.integers(0, sb.nb, sb.nb)
        gi, ok = _cross(sa.g, sa.curves(ia)[0], sb.g, sb.curves(ib)[0])
        gs.append(gi); lost += (not ok)
    err = float(np.std(gs))
    return (g if found else float("nan")), err, (sa.cumulant(g) if found else float("nan")), lost / nboot
