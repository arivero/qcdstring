"""Section 11.5: gauge-fixed bosonic Hessian of the unit string at w >= 0, by partial waves.

Photon units, F-term frame of Eq. (3): u1 = sqrt2 q / v, u2 = sqrt2 q~ / v, S = Z/(g v),
dimensionless connection A with D u1 = (grad - iA) u1, D u2 = (grad + iA) u2. The energy per
length divided by v^2 is the integral of
    eps = b^2 + |D u1|^2/2 + |D u2|^2/2 + |grad S|^2 + (|u1|^2-|u2|^2)^2/16
          + |u1 u2 - 1 + 2 w S|^2/4 + |S|^2 (|u1|^2+|u2|^2)/2 ,
which reduces to Eq. (6) on u1 = f e^{i theta}, u2 = f e^{-i theta}, S = s. The kinetic metric is
|dA/dt|^2 + |du1/dt|^2/2 + |du2/dt|^2/2 + |dS/dt|^2.

Fluctuations are written in the co-rotating frame, u1 = e^{i theta}(f + eta1),
u2 = e^{-i theta}(f + eta2), with eight real fields (Re/Im eta1, eta2, S; A_rho, A_theta),
each expanded as X_c(rho) cos(l theta) + X_s(rho) sin(l theta). The background-gauge term
kappa G^2, G = -div(dA) + (f/2)(Im eta1 - Im eta2), is added; gauge-orbit levels scale with
kappa and are identified by changing it. The radial quadratic forms are derived with sympy
and discretized with P1 elements (Gauss quadrature), Dirichlet data at the outer radius and
natural data at the axis.
"""
import json
from functools import lru_cache
from pathlib import Path
import sys

import numpy as np
import sympy as sp
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import eigsh
from scipy.special import roots_legendre

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT.parents[0] / "1992-scalar-doublet" / "code"))
from trace_spectrum import static_solution  # noqa: E402

NAMES = ["p1", "q1", "p2", "q2", "c", "d", "r", "t"]


@lru_cache(maxsize=None)
def radial_forms(ell):
    rho, th, e, w, kap = sp.symbols("rho theta e w kappa", real=True)
    f, fp, a, ap, s, sp_ = sp.symbols("f fp a ap s sp", real=True)
    parts = ["c"] if ell == 0 else ["c", "s"]
    Cs, Sn = sp.symbols("Cs Sn", real=True)  # cos(l theta), sin(l theta)
    val, der, fields = {}, {}, {}
    for n in NAMES:
        X = 0
        Xr = 0
        Xt = 0
        for part in parts:
            v_ = sp.Symbol(f"{n}_{part}", real=True)
            dv = sp.Symbol(f"{n}_{part}_d", real=True)
            val[(n, part)], der[(n, part)] = v_, dv
            if ell == 0:
                trig, dtrig = sp.Integer(1), sp.Integer(0)
            else:
                trig = Cs if part == "c" else Sn
                dtrig = -ell * Sn if part == "c" else ell * Cs
            X += v_ * trig
            Xr += dv * trig
            Xt += v_ * dtrig
        fields[n] = (e * X, e * Xr, e * Xt)  # value, d/drho, d/dtheta
    I = sp.I
    p1, q1, p2, q2, c, d, r, t = (fields[n] for n in NAMES)
    eta1 = (p1[0] + I * q1[0], p1[1] + I * q1[1], p1[2] + I * q1[2])
    eta2 = (p2[0] + I * q2[0], p2[1] + I * q2[1], p2[2] + I * q2[2])
    U1, U1r, U1t = f + eta1[0], fp + eta1[1], eta1[2]
    U2, U2r, U2t = f + eta2[0], fp + eta2[1], eta2[2]
    Sx = s + c[0] + I * d[0]
    Sxr = sp_ + c[1] + I * d[1]
    Sxt = c[2] + I * d[2]
    Ar, At, Atr, Art = r[0], t[0], t[1], r[2]
    D1r = U1r - I * Ar * U1
    D1t = (I * U1 + U1t) / rho - I * (a / rho + At) * U1
    D2r = U2r + I * Ar * U2
    D2t = (-I * U2 + U2t) / rho + I * (a / rho + At) * U2
    b = (ap + At + rho * Atr - Art) / rho
    ab2 = lambda z: sp.expand(z * sp.conjugate(z))  # noqa: E731
    eps = (b**2 + (ab2(D1r) + ab2(D1t)) / 2 + (ab2(D2r) + ab2(D2t)) / 2 + ab2(Sxr) + ab2(Sxt) / rho**2
           + (ab2(U1) - ab2(U2)) ** 2 / 16 + ab2(U1 * U2 - 1 + 2 * w * Sx) / 4
           + ab2(Sx) * (ab2(U1) + ab2(U2)) / 2)
    div = (r[0] + rho * r[1] + t[2]) / rho
    G = -div + (f / 2) * (q1[0] - q2[0])
    E2 = sp.expand(eps).coeff(e, 2) + kap * sp.expand(G**2).coeff(e, 2)
    metric = sp.expand(r[0]**2 + t[0]**2 + (p1[0]**2 + q1[0]**2 + p2[0]**2 + q2[0]**2) / 2
                       + c[0]**2 + d[0]**2).coeff(e, 2)

    def theta_average(expr):
        """Integral over theta: for l >= 1, <Cs^2> = <Sn^2> = 1/2, odd powers and Cs Sn average to 0."""
        expr = sp.expand(expr)
        if ell == 0:
            return 2 * sp.pi * expr
        poly = sp.Poly(expr, Cs, Sn)
        total = 0
        for (i_, j_), coeff in poly.terms():
            if (i_, j_) == (0, 0):
                total += coeff
            elif (i_, j_) in ((2, 0), (0, 2)):
                total += coeff / 2
            elif i_ + j_ > 2:
                raise ValueError("quadratic form expected")
        return 2 * sp.pi * total

    E2r = sp.expand(theta_average(E2) * rho)
    Mr = sp.expand(theta_average(metric) * rho)
    keys = [(n, part) for part in parts for n in NAMES]
    xs = [val[k] for k in keys]
    dxs = [der[k] for k in keys]
    n = len(keys)
    K = [[sp.diff(E2r, dxs[i], dxs[j]) / 2 for j in range(n)] for i in range(n)]
    C = [[sp.diff(E2r, dxs[i], xs[j]) / 2 for j in range(n)] for i in range(n)]
    P = [[sp.diff(E2r, xs[i], xs[j]) / 2 for j in range(n)] for i in range(n)]
    Mm = [[sp.diff(Mr, xs[i], xs[j]) / 2 for j in range(n)] for i in range(n)]
    args = (rho, f, fp, a, ap, s, sp_, w, kap)
    lam = lambda mat: sp.lambdify(args, [list(row) for row in mat], "numpy")  # noqa: E731
    return n, lam(K), lam(C), lam(P), lam(Mm)


def background(w, radius):
    sol = static_solution(w, radius, 0.0, 1)

    def at(r):
        y = sol.sol(np.log(r))
        f, vf, a, va, s, vs = y
        return f, vf / r, a, va / r, s, vs / r
    return at


def evaluate(fun, n, args):
    """Evaluate a lambdified n x n matrix on arrays of quadrature points -> (Q, n, n)."""
    raw = fun(*args)
    Q = np.size(args[0])
    out = np.empty((Q, n, n))
    for i_ in range(n):
        for j_ in range(n):
            out[:, i_, j_] = np.broadcast_to(np.asarray(raw[i_][j_], float), (Q,))
    return out


def assemble(ell, w, bg, radius, h, kappa):
    n, K, C, P, M = radial_forms(ell)
    cells = round(radius / h)
    h = radius / cells
    gx, gw = roots_legendre(4)
    r0 = np.arange(cells) * h
    rq = (r0[:, None] + h * (1 + gx[None, :]) / 2).ravel()          # (cells*4,)
    wq = np.tile(gw * h / 2, cells)
    f, fp, a, ap, s, sp_ = bg(rq)
    args = (rq, f, fp, a, ap, s, sp_, w + 0 * rq, kappa + 0 * rq)
    Kq, Cq, Pq, Mq = (evaluate(F, n, args) for F in (K, C, P, M))
    N = np.stack([1 - (1 + gx) / 2, (1 + gx) / 2])                   # (2, 4)
    N = np.tile(N, (1, cells))                                       # (2, Q)
    dN = np.array([-1 / h, 1 / h])
    nodes = cells + 1
    rows, cols, kv, mv = [], [], [], []
    elem = np.repeat(np.arange(cells), 4)
    for A_ in range(2):
        for B_ in range(2):
            bk = (Kq * (dN[A_] * dN[B_]) + Cq * (dN[A_] * N[B_])[:, None, None]
                  + np.transpose(Cq, (0, 2, 1)) * (N[A_] * dN[B_])[:, None, None]
                  + Pq * (N[A_] * N[B_])[:, None, None]) * wq[:, None, None]
            bm = Mq * (N[A_] * N[B_] * wq)[:, None, None]
            ia = (elem + A_)[:, None, None] * n + np.arange(n)[None, :, None]
            ib = (elem + B_)[:, None, None] * n + np.arange(n)[None, None, :]
            ia, ib = np.broadcast_arrays(ia, ib)
            rows.append(ia.ravel()); cols.append(ib.ravel())
            kv.append(bk.ravel()); mv.append(bm.ravel())
    rows, cols = np.concatenate(rows), np.concatenate(cols)
    Kg = coo_matrix((np.concatenate(kv), (rows, cols)), shape=(nodes * n, nodes * n)).tocsr()
    Mg = coo_matrix((np.concatenate(mv), (rows, cols)), shape=(nodes * n, nodes * n)).tocsr()
    keep = np.arange((nodes - 1) * n)  # Dirichlet at the outer radius
    return Kg[keep][:, keep], Mg[keep][:, keep]


def lowest(ell, w, bg, radius, h, kappa, k=8):
    Kg, Mg = assemble(ell, w, bg, radius, h, kappa)
    vals = eigsh(Kg, k=k, M=Mg, sigma=-0.25, which="LM", return_eigenvectors=False,
                 ncv=max(60, 4 * k), maxiter=20000, v0=np.ones(Kg.shape[0]))
    return np.sort(vals)


def physical_levels(ell, w, bg, radius, h, k=8, tol=2e-4):
    """Levels independent of the gauge parameter (kappa = 1 and 2)."""
    v1 = lowest(ell, w, bg, radius, h, 1.0, k)
    v2 = lowest(ell, w, bg, radius, h, 2.0, k)
    return [float(x) for x in v1 if np.min(np.abs(v2 - x)) < tol], [float(x) for x in v1]


def bulk_threshold(w):
    """Lowest bulk squared mass: (h, Re S) mixing in the vacuum, [[1, w], [w, 1 + w^2]]."""
    return (np.sqrt(1 + w * w / 4) - w / 2) ** 2


def summarize(levels_by_l, w):
    """Remove the two translation levels (l = 1) and return the lowest remaining level."""
    rest = []
    for l, vals in levels_by_l.items():
        vals = sorted(vals)
        if l == "1":
            vals = vals[2:]
        rest += vals
    return min(rest)


def main():
    radius, h = 25.0, 0.05
    out = {"validation": {}, "scan": [], "high_l": {}, "budget": {}}
    for w in (0.001, 0.01):
        bg = background(w, radius)
        out["validation"][str(w)] = {"l0_masses": [float(np.sqrt(x)) for x in physical_levels(0, w, bg, radius, h)[0][:6]]}
    ws = [round(0.02 * k, 3) for k in range(0, 22)]  # 0 ... 0.42
    for w in ws:
        bg = background(w, radius)
        row = {"w": w, "bulk_threshold": float(bulk_threshold(w))}
        ells = range(0, 9) if w in (0.0, 0.1, 0.2, 0.3, 0.38, 0.42) else range(0, 3)
        lev = {}
        for l in ells:
            lev[str(l)] = physical_levels(l, w, bg, radius, h)[0][:4]
        row["levels"] = lev
        row["translations"] = lev["1"][:2]
        row["lowest_nontranslation"] = float(summarize(lev, w))
        out["scan"].append(row)
        print(json.dumps(row), flush=True)
    for w in (0.0, 0.388):
        bg = background(w, radius)
        out["high_l"][str(w)] = {str(l): physical_levels(l, w, bg, radius, h, k=4)[0][:2] for l in (12, 16)}
    w = 0.388
    for label, (R, hh) in {"R25_h0.05": (25.0, 0.05), "R25_h0.025": (25.0, 0.025),
                           "R35_h0.05": (35.0, 0.05)}.items():
        bg = background(w, R)
        lev = {str(l): physical_levels(l, w, bg, R, hh)[0][:4] for l in (0, 1, 2)}
        out["budget"][label] = dict(levels=lev, lowest_nontranslation=float(summarize(lev, w)))
    (ROOT / "results" / "boson-hessian.json").write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps({k: out[k] for k in ("validation", "high_l", "budget")}, indent=1))


if __name__ == "__main__":
    main()
