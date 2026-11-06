#!/usr/bin/env python3
"""Analysis and figures for the 1980 paper. Prints every number quoted;
writes ../results/summary80.json and ../figures/*.png."""
import glob, json, math, os
import numpy as np
from scipy.optimize import least_squares, brentq
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(HERE, "..", "results")
FIG = os.path.join(HERE, "..", "figures")
R76 = os.path.join(HERE, "..", "..", "1976-flux-tube-casimir", "results")
C1, C2, C3 = "#2a78d6", "#eb6834", "#1baf7a"
INK, INK2, GRID, SURF = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
plt.rcParams.update({"figure.facecolor": SURF, "axes.facecolor": SURF, "savefig.facecolor": SURF,
                     "axes.edgecolor": INK2, "axes.labelcolor": INK, "xtick.color": INK2, "ytick.color": INK2,
                     "text.color": INK, "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.6,
                     "axes.spines.top": False, "axes.spines.right": False, "font.size": 10,
                     "lines.linewidth": 2, "legend.frameon": False})
CRAY = 12e6 * 3600 * 100          # 100 hours of a Cray-1 at 12 Mflop/s
CHANNELS = ("pp", "mp", "mm", "pm")
LEVEL = {"pp": 0, "mp": 1, "mm": 2, "pm": 3}


def ng_level(n, R, sigma, c=0.0, d=3):
    x = sigma ** 2 * R ** 2 + 2 * math.pi * sigma * (n - (d - 2) / 24)
    return (math.sqrt(x) if x > 0 else float("nan")) + c


def load(beta):
    files = sorted(f for f in glob.glob(os.path.join(RES, f"z2x_b{beta:.3f}_s*.npz")) if "test" not in f)
    data = {c: [] for c in CHANNELS}
    poly, flop, meta = [], 0.0, None
    for f in files:
        d = np.load(f)
        for c in CHANNELS:
            data[c].append(d[f"C_{c}"])
        poly.append(d["poly"])
        flop += float(d["flop"])
        meta = {k: (d[k].tolist() if d[k].ndim else d[k].item()) for k in ("Nt", "L", "tau", "nsub", "nsmear", "Tlist")}
    return data, poly, flop, meta, len(files)


def blocks(chains, bsize=5):
    out = []
    for C in chains:
        n = len(C) // bsize
        out.extend(C[: n * bsize].reshape((n, bsize) + C.shape[1:]).mean(axis=1))
    return np.array(out)


def jk(B, fn):
    nb = len(B)
    tot = B.mean(axis=0)
    c = fn(tot)
    js = np.array([fn((tot * nb - B[i]) / (nb - 1)) for i in range(nb)])
    return c, np.sqrt((nb - 1) * np.nanvar(js, axis=0)), js


def analyse(beta, Rfit):
    data, poly, flop, meta, nch = load(beta)
    Tl = meta["Tlist"]
    tau = meta["tau"]
    B = {c: blocks(data[c]) for c in CHANNELS}
    nb = len(B["pp"])
    res = {"beta": beta, "chains": nch, "blocks": nb, **meta, "flop": flop}
    # effective energies between consecutive T
    E, dE, Ej = {}, {}, {}
    for c in CHANNELS:
        def eff(C):
            with np.errstate(invalid="ignore", divide="ignore"):
                return np.log(C[:-1] / C[1:]) / tau            # (nT-1, Rmax)
        E[c], dE[c], Ej[c] = jk(B[c], eff)
        res[f"Eeff_{c}"] = E[c].tolist(); res[f"dEeff_{c}"] = dE[c].tolist()
    Rmax = E["pp"].shape[1]
    R = np.arange(1, Rmax + 1)
    # ground state: last effective energy with error below 0.01
    def pick(c, maxerr):
        idx = np.full(Rmax, -1)
        for r in range(Rmax):
            for i in range(E[c].shape[0] - 1, -1, -1):
                if np.isfinite(E[c][i, r]) and dE[c][i, r] < maxerr:
                    idx[r] = i
                    break
        return idx
    res["pick"] = {}
    out = {}
    for c, maxerr in (("pp", 0.01), ("mp", 0.05), ("mm", 0.08), ("pm", 0.08)):
        idx = pick(c, maxerr)
        val = np.array([E[c][i, r] if i >= 0 else np.nan for r, i in enumerate(idx)])
        err = np.array([dE[c][i, r] if i >= 0 else np.nan for r, i in enumerate(idx)])
        js = np.array([[Ej[c][k][i, r] if i >= 0 else np.nan for r, i in enumerate(idx)] for k in range(nb)])
        out[c] = (val, err, js, idx)
        res["pick"][c] = {"E": val.tolist(), "dE": err.tolist(), "T_from": [int(Tl[i]) if i >= 0 else None for i in idx]}
    # ground-state fits
    V, dV, Vj, _ = out["pp"]
    fits = {}
    for (rmin, rmax) in Rfit:
        sel = (R >= rmin) & (R <= rmax) & np.isfinite(V)
        def f3(v):
            r = least_squares(lambda p: (p[0] * R[sel] + p[1] - p[2] / R[sel] - v[sel]) / dV[sel], [0.05, 0.1, 0.13])
            return r.x
        def f2(v):
            r = least_squares(lambda p: (p[0] * R[sel] + p[1] - (math.pi / 24) / R[sel] - v[sel]) / dV[sel], [0.05, 0.1])
            return r.x
        def fng(v):
            def resid(p):
                m = np.array([ng_level(0, x, p[0], p[1]) for x in R[sel]])
                return np.where(np.isfinite(m), (m - v[sel]) / dV[sel], 1e3)
            p0 = f2(v)
            r = least_squares(resid, [p0[0], p0[1] + 0.02])
            return r.x
        for name, f in (("free", f3), ("luscher", f2), ("ng", fng)):
            p = f(V)
            pj = np.array([f(Vj[k]) for k in range(nb)])
            dp = np.sqrt((nb - 1) * np.nanvar(pj, axis=0))
            if name == "free":
                resid = (p[0] * R[sel] + p[1] - p[2] / R[sel] - V[sel]) / dV[sel]
            elif name == "luscher":
                resid = (p[0] * R[sel] + p[1] - (math.pi / 24) / R[sel] - V[sel]) / dV[sel]
            else:
                resid = (np.array([ng_level(0, x, p[0], p[1]) for x in R[sel]]) - V[sel]) / dV[sel]
            fits[f"{name}_{rmin}-{rmax}"] = {"p": p.tolist(), "dp": dp.tolist(), "chi2": float(np.sum(resid ** 2)), "dof": int(sel.sum() - len(p))}
    res["fits"] = fits
    # local b from three consecutive R
    bl = []
    for r0 in range(3, Rmax):
        def bloc(v):
            A = np.array([[r, 1, -1 / r] for r in (r0 - 1, r0, r0 + 1)], dtype=float)
            return np.linalg.solve(A, v[r0 - 2: r0 + 1])[2]
        if np.all(np.isfinite(V[r0 - 2: r0 + 1])):
            b0 = bloc(V)
            bj = np.array([bloc(Vj[k]) for k in range(nb)])
            bl.append((r0, float(b0), float(math.sqrt((nb - 1) * np.nanvar(bj)))))
    res["b_local"] = bl
    # gaps relative to the ground state, with correlated jackknife
    gaps = {}
    for c in ("mp", "mm", "pm"):
        val, err, js, idx = out[c]
        g = val - V
        gj = js - Vj
        dg = np.sqrt((nb - 1) * np.nanvar(gj, axis=0))
        gaps[c] = {"gap": g.tolist(), "dgap": dg.tolist()}
    res["gaps"] = gaps
    # Polyakov-loop correlator over the full time extent, for comparison with 1976
    P = blocks(poly)
    def vpoly(C):
        with np.errstate(invalid="ignore", divide="ignore"):
            return -np.log(C) / meta["Nt"]
    vp, dvp, _ = jk(P, vpoly)
    res["V_poly"] = vp.tolist(); res["dV_poly"] = dvp.tolist()
    return res


def gevp_section(beta, E0, dE0):
    """Second production: 2x2 correlation matrices per channel. Lowest
    generalized eigenvalue of C(T) v = lambda C(T0) v gives the effective
    energy -ln(lambda)/(T - T0)."""
    from scipy.linalg import eigh
    files = sorted(glob.glob(os.path.join(RES, f"z2g_b{beta:.3f}_s*.npz")))
    if not files:
        return None
    data = {c: [] for c in ("pp", "mp", "mm")}
    flop = 0.0
    for f in files:
        d = np.load(f)
        for c in data:
            data[c].append(d[f"C_{c}"])
        flop += float(d["flop"])
        Tl = d["Tlist"].tolist(); tau = int(d["tau"])
    out = {"flop": flop, "chains": len(files), "Tlist": Tl}
    for c in data:
        B = blocks(data[c])                      # (nb, nT, Rmax, 2, 2)
        nb = len(B)
        Rmax = B.shape[2]
        def gev(C, T0i, Ti):
            res = np.full(Rmax, np.nan)
            for r in range(Rmax):
                A = 0.5 * (C[Ti, r] + C[Ti, r].T)
                M = 0.5 * (C[T0i, r] + C[T0i, r].T)
                try:
                    w = eigh(A, M, eigvals_only=True)
                except Exception:
                    continue
                lam = w.max()
                if lam > 0:
                    res[r] = -math.log(lam) / ((Ti - T0i) * tau)
            return res
        for (T0i, Ti) in ((0, 1), (1, 2), (2, 3)):
            if Ti >= len(Tl):
                continue
            e, de, ej = jk(B, lambda C: gev(C, T0i, Ti))
            out[f"{c}_{Tl[T0i]}-{Tl[Ti]}"] = {"E": e.tolist(), "dE": de.tolist()}
    # gaps from the (4,8) solution against E0 of the first production
    for c in ("mp", "mm"):
        k = f"{c}_4-8"
        if k in out:
            e = np.array(out[k]["E"]); de = np.array(out[k]["dE"])
            n = min(len(e), len(E0))
            out[f"gap_{c}"] = {"gap": (e[:n] - E0[:n]).tolist(), "dgap": np.hypot(de[:n], dE0[:n]).tolist()}
    return out

from scipy.stats import chi2 as chi2dist

CMODELS = {
    "free":          (lambda p, r: p[0] * r + p[1] - p[2] / r, [0.05, 0.1, 0.13], ("sigma", "c", "b")),
    "luscher":       (lambda p, r: p[0] * r + p[1] - (math.pi / 24) / r, [0.05, 0.1], ("sigma", "c")),
    "zero":          (lambda p, r: p[0] * r + p[1], [0.05, 0.1], ("sigma", "c")),
    "endpoint":      (lambda p, r: p[0] * r + p[1] - (math.pi / 24) / r + p[2] / r ** 2, [0.05, 0.1, 0.0], ("sigma", "c", "d")),
    "free_endpoint": (lambda p, r: p[0] * r + p[1] - p[2] / r + p[3] / r ** 2, [0.05, 0.1, 0.13, 0.0], ("sigma", "c", "b", "d")),
    "ng":            (lambda p, r: np.sqrt(np.maximum(p[0] ** 2 * r ** 2 - math.pi * p[0] / 12, 0.0)) + p[1], [0.05, 0.15], ("sigma", "c")),
}


def corr_fit(R, V, cov, model):
    f, q0, names = CMODELS[model]
    Li = np.linalg.inv(np.linalg.cholesky(cov))
    res = least_squares(lambda p: Li @ (f(p, R) - V), q0, xtol=1e-14, ftol=1e-14)
    pcov = np.linalg.inv(res.jac.T @ res.jac)
    chi2 = float(np.sum(res.fun ** 2)); dof = len(R) - len(q0)
    return {"p": res.x.tolist(), "dp": np.sqrt(np.diag(pcov)).tolist(), "chi2": chi2, "dof": dof,
            "pvalue": float(chi2dist.sf(chi2, dof)) if dof > 0 else float("nan"), "names": names}


def ground_state_corr(r, beta, ranges):
    """Correlated fits to E0 from the single-operator effective energy between
    T = 8 and 12, with the jackknife covariance."""
    data, poly, flop, meta, nch = load(beta)
    B = blocks(data["pp"])
    nb = len(B)
    tau = meta["tau"]
    def e812(C):
        with np.errstate(invalid="ignore", divide="ignore"):
            return np.log(C[1] / C[2]) / tau
    E0, dE0, J = jk(B, e812)
    R = np.arange(1, len(E0) + 1)
    out = {"E0": E0.tolist(), "dE0": dE0.tolist(), "fits": {}}
    for (rmin, rmax) in ranges:
        sel = (R >= rmin) & (R <= rmax)
        Js = J[:, sel]
        cov = (nb - 1) / nb * ((Js - Js.mean(axis=0)).T @ (Js - Js.mean(axis=0)))
        for m in CMODELS:
            if len(CMODELS[m][1]) >= sel.sum():
                continue
            if m == "ng" and rmin < 3:
                continue
            out["fits"][f"{m}_{rmin}-{rmax}"] = corr_fit(R[sel], E0[sel], cov, m)
    good = [i for i in range(1, len(E0)) if np.all(np.isfinite(J[:, i]))]
    cc = np.corrcoef(J[:, good].T)
    out["neighbour_correlation"] = float(np.mean([cc[i, i + 1] for i in range(len(good) - 1)]))
    out["_J"] = J
    out["_nb"] = nb
    return out


def direct_section(beta, sigma_ref):
    """Third production: conventional loops, T = 0..7, a four-operator basis
    in the one-phonon channel. Generalized eigenvalues with T0 = 1 give
    effective energies at unit steps in T."""
    from scipy.linalg import eigh
    files = sorted(glob.glob(os.path.join(RES, f"z2d_b{beta:.3f}_s*.npz")))
    if not files:
        return None
    Cpp, Cmp, flop = [], [], 0.0
    for f in files:
        d = np.load(f)
        Cpp.append(d["Cpp"]); Cmp.append(d["Cmp"]); flop += float(d["flop"])
    # regroup blocks of 20 configurations into blocks of 100 within each chain
    def regroup(arrs, k=5):
        out = []
        for A in arrs:
            n = len(A) // k
            out.extend(A[: n * k].reshape((n, k) + A.shape[1:]).mean(axis=1))
        return np.array(out)
    Bpp, Bmp = regroup(Cpp), regroup(Cmp)
    nb = len(Bpp)
    Tn = Bpp.shape[1]
    Rmax = Bpp.shape[2]
    res = {"flop": flop, "blocks": nb, "configs": int(sum(len(c) for c in Cpp) * 20)}
    # overlaps of the four (-,+) operators at T = 0
    M = Bmp.mean(axis=0)
    corr = {}
    for R in range(4, Rmax + 1):
        c0 = 0.5 * (M[0, R - 1] + M[0, R - 1].T)
        dg = np.sqrt(np.diag(c0))
        corr[R] = (c0 / np.outer(dg, dg)).tolist()
    res["op_correlation_T0"] = corr
    def eff_single(C, ch, k):
        with np.errstate(invalid="ignore", divide="ignore"):
            return np.log(C[:-1, :, k, k] / C[1:, :, k, k])          # (Tn-1, Rmax)
    def eff_gevp(C, ops, T0=1):
        out = np.full((Tn - 1, Rmax), np.nan)
        for r in range(Rmax):
            if r + 1 < 2:
                continue
            idx = [o for o in ops if not (o == 3 and r + 1 < 4)]
            A0 = C[T0, r][np.ix_(idx, idx)]
            A0 = 0.5 * (A0 + A0.T)
            lam = []
            for T in range(Tn):
                A = C[T, r][np.ix_(idx, idx)]
                A = 0.5 * (A + A.T)
                try:
                    w = eigh(A, A0, eigvals_only=True)
                    lam.append(w.max())
                except Exception:
                    lam.append(np.nan)
            lam = np.array(lam)
            with np.errstate(invalid="ignore", divide="ignore"):
                out[:, r] = np.log(lam[:-1] / lam[1:])
        return out
    def jk_(fn, B):
        tot = B.mean(axis=0)
        c = fn(tot)
        js = np.array([fn((tot * nb - B[i]) / (nb - 1)) for i in range(nb)])
        return c, np.sqrt((nb - 1) * np.nanvar(js, axis=0)), js
    E0, dE0, J0 = jk_(lambda C: eff_single(C, "pp", 0), Bpp)
    E1s, dE1s, J1s = jk_(lambda C: eff_single(C, "mp", 0), Bmp)
    E1g, dE1g, J1g = jk_(lambda C: eff_gevp(C, [0, 1, 2, 3]), Bmp)
    res.update({"E0": E0.tolist(), "dE0": dE0.tolist(), "E1_single": E1s.tolist(), "dE1_single": dE1s.tolist(),
                "E1_gevp": E1g.tolist(), "dE1_gevp": dE1g.tolist()})
    # gaps with the same configurations: E1(T) - E0(T*) with E0 from its own plateau (T = 5 -> 6)
    t0 = min(5, Tn - 2)
    gap = E1g - E0[t0][None, :]
    gj = J1g - J0[:, t0][:, None, :]
    dgap = np.sqrt((nb - 1) * np.nanvar(gj, axis=0))
    res.update({"gap_gevp": gap.tolist(), "dgap_gevp": dgap.tolist(), "E0_T": t0})
    print(f"\n  conventional loops, beta = {beta}: {res['configs']} configurations, {nb} blocks of 100")
    print("   operator correlations at T = 0, R = 5: " + str(np.round(np.array(corr.get(5, [[np.nan]])), 3).tolist()))
    for r in range(1, Rmax):
        R = r + 1
        if R < 3:
            continue
        line0 = " ".join(f"{E0[T, r]:.3f}({dE0[T, r]:.3f})" for T in range(Tn - 1) if np.isfinite(E0[T, r]) and dE0[T, r] < 0.1)
        line1 = " ".join(f"{E1g[T, r]:.3f}({dE1g[T, r]:.3f})" for T in range(Tn - 1) if np.isfinite(E1g[T, r]) and dE1g[T, r] < 0.15)
        line1s = " ".join(f"{E1s[T, r]:.3f}({dE1s[T, r]:.3f})" for T in range(Tn - 1) if np.isfinite(E1s[T, r]) and dE1s[T, r] < 0.15)
        print(f"   R {R}: E0(T->T+1) {line0}")
        print(f"         E1 4-op GEVP  {line1}")
        print(f"         E1 one op     {line1s}")

    # two-state description of the generalized eigenvalue effective energies over T = 2..6
    def two_state(e, de, Ts):
        ok = np.isfinite(e) & np.isfinite(de)
        if ok.sum() < 4:
            return np.nan
        T_, e_, de_ = Ts[ok], e[ok], de[ok]
        try:
            r = least_squares(lambda p: (p[0] + p[1] * np.exp(-abs(p[2]) * T_) - e_) / de_,
                              [e_[-1], 0.5, 1.0], bounds=([0, -10, 0.05], [3, 10, 5]))
            return r.x[0]
        except Exception:
            return np.nan
    Ts = np.arange(2, min(7, Tn - 1))
    ts_fit, dts_fit = [], []
    J1 = J1g
    for r in range(Rmax):
        if r + 1 < 3:
            ts_fit.append(np.nan); dts_fit.append(np.nan); continue
        e = E1g[Ts, r]; de = dE1g[Ts, r]
        c = two_state(e, de, Ts)
        js = np.array([two_state(J1[i][Ts, r], de, Ts) for i in range(nb)])
        ts_fit.append(c); dts_fit.append(math.sqrt((nb - 1) * np.nanvar(js)))
    res["E1_two_state"] = ts_fit; res["dE1_two_state"] = dts_fit
    sig = sigma_ref
    print("   summary (E0 from T = 5->6; NG gap with sigma = %.4f):" % sig)
    for r in range(2, Rmax):
        R = r + 1
        e0 = E0[min(5, Tn - 2), r]
        ng = math.sqrt(sig ** 2 * R ** 2 + 2 * math.pi * sig * 23 / 24) - math.sqrt(max(sig ** 2 * R ** 2 - 2 * math.pi * sig / 24, 0.0))
        g45 = gap[4, r]; dg45 = dgap[4, r]
        g67 = gap[6, r] if Tn - 1 > 6 else np.nan; dg67 = dgap[6, r] if Tn - 1 > 6 else np.nan
        print(f"     R {R}: E0 {e0:.4f}; gap T4->5 {g45:.3f}({dg45:.3f}), T6->7 {g67:.3f}({dg67:.3f}); two-state E1 {ts_fit[r]:.3f}({dts_fit[r]:.3f}) -> gap {ts_fit[r]-e0:.3f}; NG {ng:.3f}; pi/R {math.pi/R:.3f}")
    return res


def data76(beta):
    """1976 potentials (closed time-like lines, Nt = 16) with jackknife samples,
    rebuilt from the 1976 raw files."""
    files = sorted(f for f in glob.glob(os.path.join(R76, f"z2ml_b{beta:.3f}_s*.npz")) if "pilot" not in f)
    blocks_ = []
    for f in files:
        d = np.load(f)
        C = d["C"].mean(axis=2)
        n = len(C) // 5
        blocks_.extend(C[: n * 5].reshape(n, 5, -1).mean(axis=1))
    B = np.array(blocks_)
    nb = len(B)
    Nt = 16
    R = np.arange(1, B.shape[1] + 1)
    corr = -sum(np.log(1 - np.exp(-math.pi * Nt / R) ** k) for k in range(1, 6)) / Nt
    def V(Cm):
        with np.errstate(invalid="ignore", divide="ignore"):
            return -np.log(Cm) / Nt + corr
    tot = B.mean(axis=0)
    return V(tot), np.array([V((tot * nb - B[i]) / (nb - 1)) for i in range(nb)]), nb


def joint_fits(beta, E0_80, J80, nb80, ranges):
    """Correlated fits to the 1976 and 1980 ground-state data together
    (independent data sets: block-diagonal covariance)."""
    V76, J76, nb76 = data76(beta)
    out = {}
    for (rmin, rmax) in ranges:
        R = np.arange(rmin, rmax + 1)
        i76 = [r - 1 for r in R if r - 1 < len(V76) and np.all(np.isfinite(J76[:, r - 1]))]
        i80 = [r - 1 for r in R if np.all(np.isfinite(J80[:, r - 1]))]
        def cov(J, idx, nb):
            X = J[:, idx]
            return (nb - 1) / nb * ((X - X.mean(0)).T @ (X - X.mean(0)))
        c76, c80 = cov(J76, i76, nb76), cov(J80, i80, nb80)
        Ct = np.zeros((len(i76) + len(i80),) * 2)
        Ct[: len(i76), : len(i76)] = c76
        Ct[len(i76):, len(i76):] = c80
        Rall = np.array([i + 1 for i in i76] + [i + 1 for i in i80], dtype=float)
        Vall = np.concatenate([V76[i76], E0_80[i80]])
        res = {}
        for m in ("free", "endpoint", "free_endpoint", "luscher", "zero"):
            if len(CMODELS[m][1]) >= len(Rall):
                continue
            res[m] = corr_fit(Rall, Vall, Ct, m)
        out[f"{rmin}-{rmax}"] = res
    return out


def ising_section():
    p = os.path.join(RES, "ising_interface.json")
    if not os.path.exists(p):
        return None
    runs = json.load(open(p))
    Ks = sorted({r["K"] for r in runs}); Ls = sorted({r["L"] for r in runs})
    tab = {}
    for r in runs:
        w = np.array(r["w2"])
        nbk = 10                      # blocks of 100-200 measurements, several autocorrelation times at L = 64
        b = w[: len(w) // nbk * nbk].reshape(nbk, -1).mean(axis=1)
        tab[(r["K"], r["L"])] = (w.mean(), b.std(ddof=1) / math.sqrt(nbk), b)
    out = {"rows": [], "Ls": Ls}
    print("\nIsing interface, Lz = 24: w^2(L)")
    for K in Ks:
        line = f"   K {K:.2f} (beta {math.atanh(math.exp(-2 * K)):.4f}): " + "  ".join(f"L{L}: {tab[(K, L)][0]:.4f}({tab[(K, L)][1]:.4f})" for L in Ls)
        # slope from L = 16, 32, 64
        Lf = [L for L in Ls if L >= 16]
        x = np.log(Lf); y = np.array([tab[(K, L)][0] for L in Lf]); e = np.array([tab[(K, L)][1] for L in Lf])
        A = np.vstack([np.ones_like(x), x]).T
        W = np.diag(1 / e ** 2)
        cov = np.linalg.inv(A.T @ W @ A)
        coef = cov @ A.T @ W @ y
        s, ds = coef[1], math.sqrt(cov[1, 1])
        # also the last pair 32 -> 64
        s2 = (tab[(K, 64)][0] - tab[(K, 32)][0]) / math.log(2)
        ds2 = math.hypot(tab[(K, 64)][1], tab[(K, 32)][1]) / math.log(2)
        out["rows"].append({"K": K, "beta": math.atanh(math.exp(-2 * K)), "w2": {L: tab[(K, L)][0] for L in Ls},
                            "dw2": {L: tab[(K, L)][1] for L in Ls}, "slope": s, "dslope": ds, "slope_32_64": s2, "dslope_32_64": ds2})
        print(line + f"   slope(16-64) {s:.4f}({ds:.4f})  slope(32-64) {s2:.4f}({ds2:.4f})")
    # crossing of the slope with 1/pi^2 by linear interpolation in K
    target = 1 / math.pi ** 2
    for key in ("slope", "slope_32_64"):
        ks = [r["K"] for r in out["rows"]]; ss = [r[key] for r in out["rows"]]
        cross = None
        for i in range(len(ks) - 1):
            if (ss[i] - target) * (ss[i + 1] - target) <= 0:
                cross = ks[i] + (target - ss[i]) * (ks[i + 1] - ks[i]) / (ss[i + 1] - ss[i])
                break
        out[f"K_R_{key}"] = cross
        if cross:
            print(f"   {key} crosses 1/pi^2 = {target:.4f} at K = {cross:.3f}, i.e. beta_R = {math.atanh(math.exp(-2 * cross)):.3f}")
    out["flop"] = sum(r["flop"] for r in runs)
    return out


def ng_gap(n, R, sigma, d=3):
    return math.sqrt(sigma ** 2 * R ** 2 + 2 * math.pi * sigma * (n - (d - 2) / 24)) - math.sqrt(max(sigma ** 2 * R ** 2 - 2 * math.pi * sigma * (d - 2) / 24, 0.0))


def bcsos_section(isg):
    """Response, Major 3: the slope criterion calibrated on the BCSOS model."""
    p = os.path.join(RES, "bcsos.json")
    if not os.path.exists(p) or not isg:
        return None
    d = json.load(open(p))
    KR = d["K_R"]
    Ls = [16, 32, 64]
    out = {"K_R_exact": KR}
    slopes = {}
    for K in sorted({r["K"] for r in d["runs"]}):
        seeds = sorted({r["seed"] for r in d["runs"] if r["K"] == K})
        per = {L: {r["seed"]: np.mean(r["w2"]) for r in d["runs"] if r["K"] == K and r["L"] == L} for L in Ls}
        def slope(excl=None):
            y = [np.mean([v for sd, v in per[L].items() if sd != excl]) for L in Ls]
            return np.polyfit(np.log(Ls), y, 1)[0]
        s0 = slope()
        js = [slope(sd) for sd in seeds]
        ds = math.sqrt((len(seeds) - 1) * np.var(js))
        slopes[K] = (s0, ds)
        out[f"slope_{K:.4f}"] = (s0, ds)
    s_KR = slopes[KR][0]
    ks = sorted(slopes)
    # BCSOS coupling where its slope crosses 1/pi^2 (linear between the two couplings)
    k1, k2 = ks[0], ks[-1]
    s1, s2 = slopes[k1][0], slopes[k2][0]
    target = 1 / math.pi ** 2
    k_cross = k1 + (target - s1) * (k2 - k1) / (s2 - s1)
    ratio = k_cross / KR
    # Ising: coupling where its slope equals the BCSOS slope at K_R
    rows = isg["rows"]
    Kmatch = None
    for a, b in zip(rows[:-1], rows[1:]):
        if (a["slope"] - s_KR) * (b["slope"] - s_KR) <= 0:
            Kmatch = a["K"] + (s_KR - a["slope"]) * (b["K"] - a["K"]) / (b["slope"] - a["slope"])
            break
    Kcross_ising = isg.get("K_R_slope")
    Kscaled = Kcross_ising / ratio if Kcross_ising else None
    beta_of = lambda K: math.atanh(math.exp(-2 * K))
    out.update({"bcsos_slope_at_KR": slopes[KR], "bcsos_crossing": k_cross, "ratio": ratio,
                "ising_K_matched": Kmatch, "ising_K_scaled": Kscaled,
                "beta_matched": beta_of(Kmatch) if Kmatch else None, "beta_scaled": beta_of(Kscaled) if Kscaled else None,
                "beta_cross": beta_of(Kcross_ising) if Kcross_ising else None})
    print("\nBCSOS calibration (heights in layer units):")
    for K in ks:
        print(f"   K = {K:.4f}: slope 16-64 = {slopes[K][0]:.4f}({slopes[K][1]:.4f})")
    print(f"   at the exact K_R the slope exceeds 1/pi^2 by {100 * (s_KR * math.pi ** 2 - 1):.0f}%; BCSOS crosses 1/pi^2 at K = {k_cross:.4f} = {ratio:.3f} K_R")
    print(f"   Ising: slope equals {s_KR:.4f} at K = {Kmatch:.4f} (beta {beta_of(Kmatch):.4f}); crossing {Kcross_ising:.4f} / {ratio:.3f} = {Kscaled:.4f} (beta {beta_of(Kscaled):.4f})")
    return out


def figures(res, isg):
    # figure 1: levels at beta = 0.73 (production 3) and the gap in units of pi/R
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.2))
    ax = axes[0]
    r = res["0.73"]; gs = r["ground_corr"]; dr = r["direct"]
    sig, c, dd = gs["fits"]["endpoint_2-9"]["p"]
    E0d = np.array(dr["E0"])[5]; dE0d = np.array(dr["dE0"])[5]
    R = np.arange(1, len(E0d) + 1)
    ok = R >= 2
    ax.errorbar(R[ok], E0d[ok], dE0d[ok], fmt="o", color=C1, ms=6, capsize=2, lw=1.2, mec=SURF, mew=1, label="ground state")
    E1t = np.array(dr["E1_two_state"]); dE1t = np.array(dr["dE1_two_state"])
    ok1 = (R >= 3) & np.isfinite(E1t)
    ax.errorbar(R[ok1], E1t[ok1], dE1t[ok1], fmt="s", color=C2, ms=6, capsize=2, lw=1.2, mec=SURF, mew=1, label="first excitation (two-state)")
    rr = np.linspace(2.6, 9.4, 200)
    e0f = sig * rr + c - (math.pi / 24) / rr + dd / rr ** 2
    ax.plot(rr, e0f, color=C1, lw=1.2)
    ax.plot(rr, e0f + np.array([ng_gap(1, x, sig) for x in rr]), color=C2, lw=1.5, label="+ square-root gap")
    ax.plot(rr, e0f + math.pi / rr, color=C2, lw=1.2, ls=":", label=r"+ $\pi/R$")
    ax.set_ylim(0, 1.6); ax.set_xlabel("R (lattice units)"); ax.set_ylabel("energy (lattice units)")
    ax.set_title(r"Z2, $\beta = 0.73$: two lowest levels", fontsize=10, loc="left")
    ax.legend(loc="upper right", fontsize=9)
    ax = axes[1]
    x = R * math.sqrt(sig)
    g = E1t - E0d
    dg = np.hypot(dE1t, dE0d)
    ok = (R >= 3) & np.isfinite(g)
    ax.errorbar(x[ok], (g * R / math.pi)[ok], (dg * R / math.pi)[ok], fmt="o", color=C1, ms=6, capsize=2, lw=1.2, mec=SURF, mew=1,
                label=r"$\beta = 0.73$, conventional loops")
    for beta, col, mk in ((0.73, C3, "D"), (0.70, C2, "s")):
        rb = res[f"{beta:.2f}"]
        sgm = rb["ground_corr"]["fits"]["endpoint_" + ("2-9" if beta == 0.73 else "2-6")]["p"][0]
        e = np.array(rb["gevp"]["mp_4-8"]["E"]); de = np.array(rb["gevp"]["mp_4-8"]["dE"])
        e0 = np.array(rb["ground_corr"]["E0"]); de0 = np.array(rb["ground_corr"]["dE0"])
        n = min(len(e), len(e0))
        Rr = np.arange(1, n + 1)
        gg = e[:n] - e0[:n]; dgg = np.hypot(de[:n], de0[:n])
        okk = (Rr >= 3) & np.isfinite(gg) & (dgg < 0.09)
        xx_ = Rr * math.sqrt(sgm)
        ax.errorbar(xx_[okk] + 0.02, (gg * Rr / math.pi)[okk], (dgg * Rr / math.pi)[okk], fmt=mk, color=col, ms=6, capsize=2, lw=1.2,
                    mec=col, mfc=SURF, mew=1.5, label=fr"$\beta = {beta}$, two-level, $T$ = 4-8")
    xx = np.linspace(0.55, 2.1, 200)
    ax.plot(xx, [ng_gap(1, v, 1.0) * v / math.pi for v in xx], color=INK2, lw=1.5, label="square root (1)")
    ax.axhline(1, color=INK2, lw=1.5, ls=":", label=r"$\pi/R$")
    ax.set_xlabel(r"$R\sqrt{\sigma}$"); ax.set_ylabel(r"$(E_1 - E_0)\,R/\pi$")
    ax.set_ylim(0, 1.3); ax.legend(loc="lower right", fontsize=8.5)
    ax.set_title("First excitation in units of the phonon spacing", fontsize=10, loc="left")
    fig.tight_layout(); fig.savefig(os.path.join(FIG, "fig1_levels.png"), dpi=150); plt.close(fig)
    # figure 2: local b against R sqrt(sigma), 1976 and 1980
    fig, ax = plt.subplots(figsize=(6, 4.2))
    s76 = os.path.join(R76, "summary.json")
    if os.path.exists(s76):
        d76 = json.load(open(s76))["z2"]
        for b76, key in (("0.73", "free_3-8"), ("0.70", "free_3-6")):
            rr76 = d76[b76]; sq = math.sqrt(rr76["corr_fits"][key]["p"][0])
            bl = np.array(rr76["b_local"]); ok = bl[:, 2] < 0.06
            ax.errorbar(bl[ok, 0] * sq, bl[ok, 1], bl[ok, 2], fmt="^", color=INK2, ms=5, capsize=2, lw=1, mec=SURF, mew=1,
                        label="1976, $N_t = 16$" if b76 == "0.73" else None)
    for beta, col, mk in ((0.73, C1, "o"), (0.70, C2, "s")):
        rb = res[f"{beta:.2f}"]
        sq = math.sqrt(rb["ground_corr"]["fits"]["endpoint_" + ("2-9" if beta == 0.73 else "2-6")]["p"][0])
        bl = np.array(rb["b_local"]); ok = bl[:, 2] < 0.06
        ax.errorbar(bl[ok, 0] * sq, bl[ok, 1], bl[ok, 2], fmt=mk, color=col, ms=6, capsize=2, lw=1.2, mec=SURF, mew=1,
                    label=fr"1980, $\beta = {beta}$")
    ax.axhline(math.pi / 24, color=INK2, ls="--", lw=1.5)
    ax.text(0.62, math.pi / 24 + 0.005, r"$\pi/24$", color=INK2)
    ax.set_xlabel(r"$R\sqrt{\sigma}$"); ax.set_ylabel(r"local coefficient of $1/R$")
    ax.set_ylim(0, 0.2); ax.legend(loc="lower right", fontsize=9)
    ax.set_title("The Casimir coefficient, 1976 and 1980 data", fontsize=10, loc="left")
    fig.tight_layout(); fig.savefig(os.path.join(FIG, "fig2_casimir.png"), dpi=150); plt.close(fig)
    # figure 3: Ising interface
    if isg:
        fig, axes = plt.subplots(1, 2, figsize=(10, 4))
        ax = axes[0]
        for K, col, mk in zip([0.30, 0.38, 0.42, 0.50], [C1, C2, C3, INK2], ["o", "s", "D", "^"]):
            rw = [x for x in isg["rows"] if abs(x["K"] - K) < 1e-9][0]
            Ls = isg["Ls"]
            ax.errorbar(np.log(Ls), [rw["w2"][L] for L in Ls], [rw["dw2"][L] for L in Ls], fmt=mk + "-", color=col, ms=5, lw=1.2,
                        capsize=2, mec=SURF, mew=1, label=f"K = {K:.2f} ($\\beta$ = {math.atanh(math.exp(-2 * K)):.3f})")
        ax.set_xlabel(r"$\ln L$"); ax.set_ylabel(r"$w^2$")
        ax.set_title("Interface width against box size", fontsize=10, loc="left"); ax.legend(loc="upper left", fontsize=9)
        ax = axes[1]
        K = [x["K"] for x in isg["rows"]]
        ax.errorbar(K, [x["slope"] for x in isg["rows"]], [x["dslope"] for x in isg["rows"]], fmt="o", color=C1, ms=6, capsize=2, lw=1.2,
                    mec=SURF, mew=1, label="slope, L = 16-64")
        ax.axhline(1 / math.pi ** 2, color=INK2, ls="--", lw=1.5)
        ax.text(0.47, 1 / math.pi ** 2 - 0.022, r"$1/\pi^2$ ($L \to \infty$)", color=INK2)
        if "bcsos" in isg:
            sk = isg["bcsos"]["bcsos_slope_at_KR"][0]
            ax.axhline(sk, color=C2, ls=":", lw=1.5)
            ax.text(0.47, sk + 0.008, "BCSOS at its exact $K_R$, L = 16-64", color=C2)
        ax.axhline(0, color=INK2, lw=0.8)
        ax.set_xlabel("Ising coupling K"); ax.set_ylabel(r"$dw^2/d\ln L$")
        ax.set_title("Rough and smooth", fontsize=10, loc="left"); ax.legend(loc="upper right")
        fig.tight_layout(); fig.savefig(os.path.join(FIG, "fig3_roughening.png"), dpi=150); plt.close(fig)


def main():
    res = {}
    for beta, Rfit in ((0.73, [(3, 10), (4, 10), (3, 8)]), (0.70, [(3, 8), (3, 7), (2, 7)])):
        if not glob.glob(os.path.join(RES, f"z2x_b{beta:.3f}_s*.npz")):
            continue
        r = analyse(beta, Rfit)
        res[f"{beta:.2f}"] = r
        print(f"\nZ2, beta = {beta}: {r['chains']} chains, {r['blocks']} blocks of 5, Nt = {r['Nt']}, L = {r['L']}, slabs of {r['tau']}, {r['nsub']} sub-updates")
        for c in CHANNELS:
            pk = r["pick"][c]
            print(f"   {c}: " + ", ".join(f"R{i+1} {e:.4f}({d:.4f})[T{t}]" for i, (e, d, t) in enumerate(zip(pk["E"], pk["dE"], pk["T_from"])) if t))
        for k, v in r["fits"].items():
            names = ("sigma", "c", "b") if k.startswith("free") else ("sigma", "c")
            print(f"   fit {k:12s}: " + ", ".join(f"{n} {p:.4f}({e:.4f})" for n, p, e in zip(names, v["p"], v["dp"])) + f"; chi2 {v['chi2']:.1f}/{v['dof']}")
        print("   local b: " + ", ".join(f"R{a}: {b:.3f}({c:.3f})" for a, b, c in r["b_local"]))
        for c in ("mp", "mm", "pm"):
            g = r["gaps"][c]
            print(f"   gap {c}: " + ", ".join(f"R{i+1} {x:.4f}({y:.4f})" for i, (x, y) in enumerate(zip(g["gap"], g["dgap"])) if np.isfinite(x)))
        for c in ("mp", "mm", "pm"):
            Ee, dEe = np.array(r[f"Eeff_{c}"]), np.array(r[f"dEeff_{c}"])
            for i, T in enumerate(r["Tlist"][:-1]):
                print(f"   E_eff {c} T{T}->{r['Tlist'][i+1]}: " + ", ".join(f"R{j+1} {Ee[i,j]:.3f}({dEe[i,j]:.3f})" for j in range(Ee.shape[1]) if np.isfinite(Ee[i,j]) and dEe[i,j] < 0.3))
        print("   V from the Polyakov-line correlator over Nt: " + ", ".join(f"{x:.4f}({y:.4f})" for x, y in zip(r["V_poly"], r["dV_poly"]) if np.isfinite(x)))
        gs = ground_state_corr(r, beta, {0.73: [(2, 9), (3, 9), (4, 9), (5, 9)], 0.70: [(2, 6), (3, 6)]}[beta])
        J80, nb80 = gs.pop("_J"), gs.pop("_nb")
        r["ground_corr"] = gs
        jf = joint_fits(beta, np.array(gs["E0"]), J80, nb80, {0.73: [(2, 9), (3, 9), (4, 9)], 0.70: [(2, 6), (3, 6)]}[beta])
        r["joint_fits"] = jf
        for rng_, v in jf.items():
            for m, fv in v.items():
                print(f"   joint 1976+1980 R {rng_} {m:13s}: " + ", ".join(f"{n} {p:.4f}({e:.4f})" for n, p, e in zip(fv["names"], fv["p"], fv["dp"])) + f"; chi2 {fv['chi2']:.1f}/{fv['dof']} p {fv['pvalue']:.3f}")
        print(f"   ground state from T = 8-12: " + ", ".join(f"R{i+1} {x:.4f}({y:.4f})" for i, (x, y) in enumerate(zip(gs["E0"], gs["dE0"])) if np.isfinite(x) and y < 0.02))
        print(f"   neighbour correlation {gs['neighbour_correlation']:.3f}")
        for k, v in gs["fits"].items():
            print(f"   correlated {k:18s}: " + ", ".join(f"{n} {p:.4f}({e:.4f})" for n, p, e in zip(v["names"], v["p"], v["dp"])) + f"; chi2 {v['chi2']:.1f}/{v['dof']} p {v['pvalue']:.3f}")
        dsec = direct_section(beta, gs["fits"]["endpoint_" + ("2-9" if beta == 0.73 else "2-6")]["p"][0])
        if dsec:
            r["direct"] = dsec
        g = gevp_section(beta, np.array(gs["E0"]), np.array(gs["dE0"]))
        if g:
            r["gevp"] = g
            for k, v in g.items():
                if isinstance(v, dict) and "E" in v:
                    print(f"   GEVP {k:8s}: " + ", ".join(f"R{i+1} {x:.3f}({y:.3f})" for i, (x, y) in enumerate(zip(v["E"], v["dE"])) if np.isfinite(x) and y < 0.3))
                elif isinstance(v, dict) and "gap" in v:
                    print(f"   GEVP {k:8s}: " + ", ".join(f"R{i+1} {x:.3f}({y:.3f})" for i, (x, y) in enumerate(zip(v["gap"], v["dgap"])) if np.isfinite(x) and y < 0.3))
    isg = ising_section()
    bcal = bcsos_section(isg)
    if isg and bcal:
        isg["bcsos"] = bcal
    figures(res, isg)
    rows = [(f"Z2 excited levels, beta = {b}", res[b]["flop"]) for b in res]
    rows += [(f"Z2 two-operator runs, beta = {b}", res[b]["gevp"]["flop"]) for b in res if "gevp" in res[b]]
    rows += [(f"Z2 conventional loops, beta = {b}", res[b]["direct"]["flop"]) for b in res if "direct" in res[b]]
    if isg:
        rows.append(("Ising interface", isg["flop"]))
    st = sorted(glob.glob(os.path.join(RES, "z2x_b0.730_s98_smeartest*.npz")))
    if st:
        rows.append(("smearing tests (kept)", sum(float(np.load(f)["flop"]) for f in st)))
    for name, fn in (("BCSOS calibration", "bcsos.json"), ("BCSOS first run (widths stored in half units)", "bcsos_first_run_var_h_over_2.json")):
        pb = os.path.join(RES, fn)
        if os.path.exists(pb):
            rows.append((name, sum(r["flop"] for r in json.load(open(pb))["runs"])))
    tot = sum(f for _, f in rows)
    print("\nBudget (Cray-1, 100 h at 12 Mflop/s = %.2e):" % CRAY)
    for n, f in rows:
        print(f"   {n:30s} {f:.2e} ({100*f/CRAY:5.1f} %)")
    print(f"   {'total':30s} {tot:.2e} ({100*tot/CRAY:5.1f} %) = {tot/12e6/3600:.0f} h")
    json.dump({"z2": res, "ising": isg, "budget": {"rows": rows, "total": tot, "cap": CRAY}},
              open(os.path.join(RES, "summary80.json"), "w"), indent=1, default=float)


if __name__ == "__main__":
    main()
