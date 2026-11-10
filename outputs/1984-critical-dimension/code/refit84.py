#!/usr/bin/env python3
"""Refits of the programme's existing data for the 1984 paper. No new
simulation. Writes ../results/refit84.txt, ../results/summary84.json and the
figures.

1. The open tube of 1976 and 1980 (ground state) with the closed-tube tension
   of 1982 (total error) as a constraint: end terms R^-2, R^-3, R^-4 and
   R^-2 with R^-4, on two baselines (free string; square root), all ranges.
2. The first excited level of 1980 with ONE baseline for both levels: the
   production-3 gaps rebuilt from the raw files with their jackknife
   covariance, the shifts -24 d/R^2 and +240 e/R^4 predicted by the ground
   state on the same baseline, joint fits of (d, e) to both levels, and the
   later-time values of production 2.
3. The closed tube of 1982: number of massless modes and bound on one more
   scalar, under the ranges and systematic variants of the 1982 paper.
"""
import contextlib, io, json, math, os, sys
import numpy as np
from scipy.optimize import least_squares, brentq
from scipy.special import k1
from scipy.stats import chi2 as chi2dist
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "..")
RES = os.path.join(HERE, "..", "results")
FIG = os.path.join(HERE, "..", "figures")
sys.path.insert(0, os.path.join(OUT, "1980-excited-flux-tube", "code"))
sys.path.insert(0, os.path.join(OUT, "1982-hagedorn-deconfinement", "code"))
C1, C2, C3 = "#2a78d6", "#eb6834", "#1baf7a"
INK, INK2, GRID, SURF = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
plt.rcParams.update({"figure.facecolor": SURF, "axes.facecolor": SURF, "savefig.facecolor": SURF,
                     "axes.edgecolor": INK2, "axes.labelcolor": INK, "xtick.color": INK2, "ytick.color": INK2,
                     "text.color": INK, "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.6,
                     "axes.spines.top": False, "axes.spines.right": False, "font.size": 10,
                     "lines.linewidth": 2, "legend.frameon": False})
lines, SUM = [], {}
def say(s=""):
    lines.append(s); print(s)

S82 = json.load(open(os.path.join(OUT, "1982-hagedorn-deconfinement", "results", "summary82.json")))
S80 = json.load(open(os.path.join(OUT, "1980-excited-flux-tube", "results", "summary80.json")))
PI24 = math.pi / 24


def ng_open(sig, R, n=0):
    x = sig**2 * R**2 + 2 * math.pi * sig * (n - 1 / 24)
    return np.sqrt(np.maximum(x, 1e-12))


SQ3 = lambda s, R: -math.pi**2 / (1152 * s * R**3)          # R^-3 term of the square root, d = 3
MODELS = {
    # name: (function of (parameters after sigma, R, sigma), number of parameters after sigma, baseline)
    "free string":                 (lambda p, R, s: s * R + p[0] - PI24 / R, 1, "free"),
    "+ d/R^2":                     (lambda p, R, s: s * R + p[0] - PI24 / R + p[1] / R**2, 2, "free"),
    "+ f/R^3":                     (lambda p, R, s: s * R + p[0] - PI24 / R + p[1] / R**3, 2, "free"),
    "+ e/R^4":                     (lambda p, R, s: s * R + p[0] - PI24 / R + p[1] / R**4, 2, "free"),
    "+ d/R^2 + e/R^4":             (lambda p, R, s: s * R + p[0] - PI24 / R + p[1] / R**2 + p[2] / R**4, 3, "free"),
    "+ area R^-3 + e/R^4":         (lambda p, R, s: s * R + p[0] - PI24 / R + SQ3(s, R) + p[1] / R**4, 2, "R^-3"),
    "square root":                 (lambda p, R, s: ng_open(s, R) + p[0], 1, "sqrt"),
    "square root + d/R^2":         (lambda p, R, s: ng_open(s, R) + p[0] + p[1] / R**2, 2, "sqrt"),
    "square root + f/R^3":         (lambda p, R, s: ng_open(s, R) + p[0] + p[1] / R**3, 2, "sqrt"),
    "square root + e/R^4":         (lambda p, R, s: ng_open(s, R) + p[0] + p[1] / R**4, 2, "sqrt"),
    "square root + d/R^2 + e/R^4": (lambda p, R, s: ng_open(s, R) + p[0] + p[1] / R**2 + p[2] / R**4, 3, "sqrt"),
}
POWER = {"+ d/R^2": 0.5, "+ f/R^3": 1.0, "+ e/R^4": 1.5, "+ area R^-3 + e/R^4": 1.5,
         "square root + d/R^2": 0.5, "square root + f/R^3": 1.0, "square root + e/R^4": 1.5}


def sigma82(beta):
    """Closed-tube tension of 1982 with its total error (statistical and spread over the closed-tube forms)."""
    s0, ds = S82["casimir"][str(beta)]["sigma_ref_tot"]
    return float(s0), float(ds)


def ground_data(beta, rmin, rmax, cache={}):
    """1976 and 1980 ground-state energies for R = rmin..rmax with their jackknife covariance (the two sets are independent)."""
    import analyze80 as a80
    if beta not in cache:
        with contextlib.redirect_stdout(io.StringIO()):
            gs = a80.ground_state_corr(None, beta, [(3, 6)])
            V76, J76, nb76 = a80.data76(beta)
        cache[beta] = (np.array(gs["E0"]), gs["_J"], gs["_nb"], V76, J76, nb76)
    E80, J80, nb80, V76, J76, nb76 = cache[beta]
    R = np.arange(rmin, rmax + 1)
    i76 = [r - 1 for r in R if r - 1 < len(V76) and np.all(np.isfinite(J76[:, r - 1]))]
    i80 = [r - 1 for r in R if r - 1 < len(E80) and np.all(np.isfinite(J80[:, r - 1]))]
    cov = lambda J, idx, nb: (nb - 1) / nb * ((J[:, idx] - J[:, idx].mean(0)).T @ (J[:, idx] - J[:, idx].mean(0)))
    n1, n2 = len(i76), len(i80)
    C = np.zeros((n1 + n2, n1 + n2))
    C[:n1, :n1] = cov(J76, i76, nb76); C[n1:, n1:] = cov(J80, i80, nb80)
    Rall = np.array([i + 1 for i in i76] + [i + 1 for i in i80], dtype=float)
    Vall = np.concatenate([V76[i76], E80[i80]])
    return Rall, Vall, C, n1


def open_tube():
    say("1. Open tube, ground state: 1976 and 1980 data with the closed-tube tension of 1982 (total error) as a constraint")
    say("   chi2/dof (p); coefficient; coefficient in units of the tension")
    out = {}
    for beta, ranges in ((0.73, [(2, 9), (3, 9), (4, 9), (5, 9)]), (0.70, [(2, 6), (3, 6)])):
        s0, ds0 = sigma82(beta)
        say(f"\n   beta = {beta}, sigma = {s0:.5f}({ds0:.5f}), sqrt(sigma) = {math.sqrt(s0):.4f}")
        res = {}
        for (rmin, rmax) in ranges:
            Rall, Vall, C, n1 = ground_data(beta, rmin, rmax)
            Li = np.linalg.inv(np.linalg.cholesky(C))
            for m, (f, npar, base) in MODELS.items():
                if base == "sqrt" and s0**2 * rmin**2 <= math.pi * s0 / 12:
                    continue
                p0 = [s0, 0.15] + [0.0] * (npar - 1)
                r = least_squares(lambda p: np.append(Li @ (f(p[1:], Rall, p[0]) - Vall), (p[0] - s0) / ds0), p0, xtol=1e-14, ftol=1e-14)
                cv = np.linalg.inv(r.jac.T @ r.jac)
                pc = np.sqrt(np.diag(cv))
                c2, dof = float(np.sum(r.fun**2)), len(Rall) + 1 - len(p0)
                row = dict(p=r.x.tolist(), dp=pc.tolist(), cov=cv.tolist(), chi2=c2, dof=dof, pvalue=float(chi2dist.sf(c2, dof)))
                res[(rmin, rmax, m)] = row
                txt = ""
                if npar == 2:
                    power = POWER[m]
                    txt = f"coefficient {r.x[2]:.4f}({pc[2]:.4f}); x sigma^{power} = {r.x[2] * s0**power:.5f}({pc[2] * s0**power:.5f})"
                if npar == 3:
                    txt = f"d {r.x[2]:.4f}({pc[2]:.4f}), e {r.x[3]:.3f}({pc[3]:.3f}), correlation {cv[2, 3] / (pc[2] * pc[3]):+.2f}"
                say(f"   R = {rmin}-{rmax}  {m:28s} {c2:8.1f}/{dof:2d} ({row['pvalue']:.3f})  {txt}")
            res[(rmin, rmax, "data")] = dict(R=Rall.tolist(), V=Vall.tolist(), dV=np.sqrt(np.diag(C)).tolist(), n76=n1)
        out[beta] = res
    # scaling of the coefficients between the couplings, matched ranges in R sqrt(sigma) (0.64-1.94)
    say("\n   scaling between the couplings at matched R sqrt(sigma) >= 0.64 (R >= 3 at 0.73, R >= 2 at 0.70):")
    for m, power in POWER.items():
        v = []
        for beta, key in ((0.73, (3, 9, m)), (0.70, (2, 6, m))):
            s0 = sigma82(beta)[0]
            r = out[beta][key]
            v.append((r["p"][2] * s0**power, r["dp"][2] * s0**power))
        pull = (v[0][0] - v[1][0]) / math.hypot(v[0][1], v[1][1])
        say(f"   {m:28s} coefficient x sigma^{power}: {v[0][0]:.5f}({v[0][1]:.5f}) and {v[1][0]:.5f}({v[1][1]:.5f}); difference {pull:+.1f} standard errors")
        SUM.setdefault("scaling", {})[m] = dict(b073=v[0], b070=v[1], pull=pull)
    say("   stability under the range at beta = 0.73 (R >= 3 against R >= 4):")
    for m in POWER:
        a, b = out[0.73][(3, 9, m)], out[0.73][(4, 9, m)]
        # the R >= 4 data are a subset: error of the difference ~ sqrt(db^2 - da^2)
        dd = math.sqrt(max(b["dp"][2] ** 2 - a["dp"][2] ** 2, 1e-30))
        say(f"   {m:28s} {a['p'][2]:.4f}({a['dp'][2]:.4f}) -> {b['p'][2]:.4f}({b['dp'][2]:.4f}); shift {(b['p'][2] - a['p'][2]) / dd:+.1f} standard errors of the difference")
        SUM.setdefault("stability", {})[m] = dict(r3=(a["p"][2], a["dp"][2]), r4=(b["p"][2], b["dp"][2]), pull=(b["p"][2] - a["p"][2]) / dd)
    es = {m: (SUM["scaling"][m]["b073"][0], SUM["scaling"][m]["b070"][0]) for m in ("+ e/R^4", "+ area R^-3 + e/R^4", "square root + e/R^4")}
    lo, hi = min(min(v) for v in es.values()), max(max(v) for v in es.values())
    say(f"   e sigma^1.5 over the three baselines that fit, both couplings: {lo:.4f} to {hi:.4f};  b2 sqrt(sigma) = -(60/pi^3) e sigma^1.5: {-60 / math.pi**3 * lo:.4f} to {-60 / math.pi**3 * hi:.4f}")
    SUM["e_range"] = (lo, hi)
    SUM["open"] = {str(b): {f"{k[0]}-{k[1]}|{k[2]}": v for k, v in o.items()} for b, o in out.items()}
    return out


def gaps80(beta=0.73):
    """First gap of the open tube from production 3 of 1980 (conventional loops, four operators), rebuilt from
    the raw files so that the jackknife covariance across R is available. Follows direct_section of analyze80.py."""
    import glob
    from scipy.linalg import eigh
    files = sorted(glob.glob(os.path.join(OUT, "1980-excited-flux-tube", "results", f"z2d_b{beta:.3f}_s*.npz")))
    Cpp, Cmp = [], []
    for f in files:
        d = np.load(f)
        Cpp.append(d["Cpp"]); Cmp.append(d["Cmp"])
    def regroup(arrs, k=5):
        out = []
        for A in arrs:
            n = len(A) // k
            out.extend(A[: n * k].reshape((n, k) + A.shape[1:]).mean(axis=1))
        return np.array(out)
    Bpp, Bmp = regroup(Cpp), regroup(Cmp)
    nb, Tn, Rmax = len(Bpp), Bpp.shape[1], Bpp.shape[2]
    def eff_single(C):
        with np.errstate(invalid="ignore", divide="ignore"):
            return np.log(C[:-1, :, 0, 0] / C[1:, :, 0, 0])
    def eff_gevp(C, ops=(0, 1, 2, 3), T0=1):
        out = np.full((Tn - 1, Rmax), np.nan)
        for r in range(1, Rmax):
            idx = [o for o in ops if not (o == 3 and r + 1 < 4)]
            A0 = C[T0, r][np.ix_(idx, idx)]; A0 = 0.5 * (A0 + A0.T)
            lam = []
            for T in range(Tn):
                A = C[T, r][np.ix_(idx, idx)]; A = 0.5 * (A + A.T)
                try:
                    lam.append(eigh(A, A0, eigvals_only=True).max())
                except Exception:
                    lam.append(np.nan)
            lam = np.array(lam)
            with np.errstate(invalid="ignore", divide="ignore"):
                out[:, r] = np.log(lam[:-1] / lam[1:])
        return out
    def jk_(fn, B):
        tot = B.mean(axis=0)
        return fn(tot), np.array([fn((tot * nb - B[i]) / (nb - 1)) for i in range(nb)])
    E0, J0 = jk_(eff_single, Bpp)
    E1, J1 = jk_(eff_gevp, Bmp)
    dE1 = np.sqrt((nb - 1) * np.nanvar(J1, axis=0))
    t0 = min(5, Tn - 2)
    def two_state(e, de, Ts):
        ok = np.isfinite(e) & np.isfinite(de)
        if ok.sum() < 4:
            return np.nan
        try:
            r = least_squares(lambda p: (p[0] + p[1] * np.exp(-abs(p[2]) * Ts[ok]) - e[ok]) / de[ok], [e[ok][-1], 0.5, 1.0],
                              bounds=([0, -10, 0.05], [3, 10, 5]))
            return r.x[0]
        except Exception:
            return np.nan
    Ts = np.arange(2, min(7, Tn - 1))
    ts = np.array([two_state(E1[Ts, r], dE1[Ts, r], Ts) if r + 1 >= 3 else np.nan for r in range(Rmax)])
    Jts = np.array([[two_state(J1[i][Ts, r], dE1[Ts, r], Ts) if r + 1 >= 3 else np.nan for r in range(Rmax)] for i in range(nb)])
    out = dict(nb=nb, R=np.arange(1, Rmax + 1, dtype=float),
               gap_ts=ts - E0[t0], J_ts=Jts - J0[:, t0], gap_ub=E1[4] - E0[t0], J_ub=J1[:, 4] - J0[:, t0],
               E1_ts=ts, E0=E0[t0])
    return out


def jcov(J, idx, nb):
    A = J[:, idx] - J[:, idx].mean(0)
    return (nb - 1) / nb * (A.T @ A)


def excited(opn):
    say("\n2. The first excited level of the open tube (1980, beta = 0.73): one baseline for both levels")
    beta = 0.73
    s0, ds0 = sigma82(beta)
    g = gaps80(beta)
    z = S80["z2"]["0.73"]
    chk = float(np.nanmax(np.abs(g["E1_ts"] - np.array(z["direct"]["E1_two_state"]))))
    say(f"   production 3 rebuilt from the raw files; two-state energies against the stored 1980 values: largest difference {chk:.1e}")
    nb = g["nb"]
    idx = [i for i in range(len(g["R"])) if g["R"][i] >= 4]
    R = g["R"][idx]
    gts, gub = g["gap_ts"][idx], g["gap_ub"][idx]
    Cts, Cub = jcov(g["J_ts"], idx, nb), jcov(g["J_ub"], idx, nb)
    dts, dub = np.sqrt(np.diag(Cts)), np.sqrt(np.diag(Cub))
    cc = Cts / np.outer(dts, dts)
    say(f"   {nb} jackknife blocks; correlation of the two-state gaps at neighbouring R: " + ", ".join(f"{cc[i, i + 1]:+.2f}" for i in range(len(R) - 1)))
    # production 2 (two operators, time steps of four): the latest window, T = 8 -> 12, against E0 of production 1
    e812, de812 = np.array(z["gevp"]["mp_8-12"]["E"]), np.array(z["gevp"]["mp_8-12"]["dE"])
    e0p1, de0p1 = np.array(z["ground_corr"]["E0"]), np.array(z["ground_corr"]["dE0"])
    g812 = np.array([e812[int(r) - 1] - e0p1[int(r) - 1] for r in R]); dg812 = np.array([math.hypot(de812[int(r) - 1], de0p1[int(r) - 1]) for r in R])
    sq = ng_open(s0, R, 1) - ng_open(s0, R, 0)
    fr = math.pi / R
    say("   R   R sqrt(sigma)   two-state (T = 2-7)   upper bound (T = 4->5)   production 2, T = 8->12   square-root gap   free gap pi/R")
    for i, r in enumerate(R):
        say(f"   {int(r)}   {r * math.sqrt(s0):.2f}            {gts[i]:.3f}({dts[i]:.3f})          {gub[i]:.3f}({dub[i]:.3f})            {g812[i]:.3f}({dg812[i]:.3f})"
            f"              {sq[i]:.3f}             {fr[i]:.3f}")
    say("   two-state estimate minus the square-root gap: " + ", ".join(f"{v:+.3f}({e:.3f})" for v, e in zip(gts - sq, dts)))
    say("   two-state estimate minus pi/R:                " + ", ".join(f"{v:+.3f}({e:.3f})" for v, e in zip(gts - fr, dts)))
    say("   T = 8->12 minus the square-root gap:          " + ", ".join(f"{v:+.3f}({e:.3f})" for v, e in zip(g812 - sq, dg812)))

    # (a) what the ground state predicts for the gap, on the same baseline
    say("\n   (a) gap predicted by the ground-state fit on the SAME baseline: baseline gap - 24 d/R^2 + 240 e/R^4, with the errors of sigma, d, e")
    say("       chi2 against the two-state gaps with their jackknife covariance and the prediction's covariance; and prediction minus upper bound")
    def gap_model(base, sig, d, e, Rv):
        b0 = (ng_open(sig, Rv, 1) - ng_open(sig, Rv, 0)) if base == "sqrt" else math.pi / Rv
        return b0 - 24 * d / Rv**2 + 240 * e / Rv**4
    preds = {}
    for m, base, has in (("+ d/R^2", "free", "d"), ("+ e/R^4", "free", "e"), ("+ d/R^2 + e/R^4", "free", "de"),
                         ("square root + d/R^2", "sqrt", "d"), ("square root + e/R^4", "sqrt", "e"), ("square root + d/R^2 + e/R^4", "sqrt", "de")):
        for rmin in (3, 4):
            ft = opn[beta][(rmin, 9, m)]
            pv, cv = np.array(ft["p"]), np.array(ft["cov"])
            def unpack(q):
                d_ = q[2] if "d" in has else 0.0
                e_ = q[3] if has == "de" else (q[2] if has == "e" else 0.0)
                return q[0], d_, e_
            f0 = gap_model(base, *unpack(pv), R)
            Jm = np.zeros((len(R), len(pv)))
            for k in range(len(pv)):
                h = 1e-6 * max(abs(pv[k]), 1e-3)
                qp = pv.copy(); qp[k] += h; qm = pv.copy(); qm[k] -= h
                Jm[:, k] = (gap_model(base, *unpack(qp), R) - gap_model(base, *unpack(qm), R)) / (2 * h)
            Cp = Jm @ cv @ Jm.T
            dp_ = np.sqrt(np.diag(Cp))
            sig_, d_, e_ = unpack(pv)
            shift = -24 * d_ / R**2 + 240 * e_ / R**4
            txt = []
            for gmin in (4, 5, 6, 7):
                sel = R >= gmin
                Ct = (Cts + Cp)[np.ix_(sel, sel)]
                dv = (gts - f0)[sel]
                txt.append(f"R >= {gmin}: {float(dv @ np.linalg.solve(Ct, dv)):.1f}/{int(sel.sum())}")
            say(f"       {m:28s} ground state R >= {rmin} (chi2 {ft['chi2']:.1f}/{ft['dof']}):  " + ";  ".join(txt))
            say(f"           shift/gap at R = 4..9: " + ", ".join(f"{v:+.2f}" for v in shift / gts)
                + ";   (prediction - upper bound)/error: " + ", ".join(f"{(a_ - b_) / math.hypot(c_, d2):+.1f}" for a_, b_, c_, d2 in zip(f0, gub, dp_, dub)))
            preds[(m, rmin)] = dict(pred=f0.tolist(), dpred=dp_.tolist(), shift=shift.tolist(), d=d_, e=e_)
    for base, f0 in (("square root, no end term", sq), ("free string, no end term", fr)):
        txt = []
        for gmin in (4, 5, 6, 7):
            sel = R >= gmin
            dv = (gts - f0)[sel]
            txt.append(f"R >= {gmin}: {float(dv @ np.linalg.solve(Cts[np.ix_(sel, sel)], dv)):.1f}/{int(sel.sum())}")
        say(f"       {base:28s}                                   " + ";  ".join(txt))

    # (b) joint fits of both levels on one baseline
    say("\n   (b) joint fits to the ground state (1976 and 1980, R >= 3) and the two-state gaps (R >= R_g), tension constrained; chi2/dof (p)")
    Rall, Vall, C, n1 = ground_data(beta, 3, 9)
    Li0 = np.linalg.inv(np.linalg.cholesky(C))
    joint = {}
    for base in ("sqrt", "free"):
        for gmin in (4, 5, 6, 7):
            sel = R >= gmin
            Lg = np.linalg.inv(np.linalg.cholesky(Cts[np.ix_(sel, sel)]))
            for has in ("", "d", "e", "de"):
                def unpack(q):
                    d_ = q[2] if "d" in has else 0.0
                    e_ = q[3] if has == "de" else (q[2] if has == "e" else 0.0)
                    return d_, e_
                def resid(q):
                    d_, e_ = unpack(q)
                    b0 = ng_open(q[0], Rall) if base == "sqrt" else q[0] * Rall - PI24 / Rall
                    r0 = Li0 @ (b0 + q[1] + d_ / Rall**2 + e_ / Rall**4 - Vall)
                    r1 = Lg @ (gap_model(base, q[0], d_, e_, R[sel]) - gts[sel])
                    return np.concatenate([r0, r1, [(q[0] - s0) / ds0]])
                q0 = [s0, 0.15] + [0.0] * len(has)
                r = least_squares(resid, q0, xtol=1e-14, ftol=1e-14)
                cv = np.linalg.inv(r.jac.T @ r.jac); pc = np.sqrt(np.diag(cv))
                c2, dof = float(np.sum(r.fun**2)), len(r.fun) - len(q0)
                d_, e_ = unpack(r.x)
                par = ""
                if has == "d": par = f"d = {r.x[2]:+.4f}({pc[2]:.4f})"
                if has == "e": par = f"e = {r.x[2]:+.4f}({pc[2]:.4f})"
                if has == "de": par = f"d = {r.x[2]:+.4f}({pc[2]:.4f}), e = {r.x[3]:+.3f}({pc[3]:.3f})"
                # chi2 share of the gaps
                rr = resid(r.x)
                cg = float(np.sum(rr[len(Rall):-1] ** 2))
                say(f"       baseline {base:5s} R_g = {gmin}  end terms: {has or 'none':4s}  {c2:8.1f}/{dof:2d} ({chi2dist.sf(c2, dof):.3f})  of which gaps {cg:6.1f}/{int(sel.sum())}   {par}")
                joint[f"{base}|{gmin}|{has}"] = dict(chi2=c2, dof=dof, p=float(chi2dist.sf(c2, dof)), chi2_gaps=cg, x=r.x.tolist(), dx=pc.tolist())

    # (c) the later-time values of production 2 against each reading (diagonal errors)
    say("\n   (c) production 2, T = 8->12, R = 4-8 (diagonal chi2, 5 separations):")
    sel = (R >= 4) & (R <= 8)
    def c812(f0):
        return float(np.sum(((g812 - f0)[sel] / dg812[sel]) ** 2))
    say(f"       square root, no end term: {c812(sq):.1f};  free string: {c812(fr):.1f}")
    for (m, rmin), pr in preds.items():
        if rmin == 3:
            say(f"       {m:28s} (ground state R >= 3): {c812(np.array(pr['pred'])):.1f}")
    SUM["excited"] = dict(R=R.tolist(), gap_ts=gts.tolist(), dgap_ts=dts.tolist(), gap_ub=gub.tolist(), dgap_ub=dub.tolist(),
                          gap_812=g812.tolist(), dgap_812=dg812.tolist(), sqrt_gap=sq.tolist(), free_gap=fr.tolist(),
                          preds={f"{k[0]}|{k[1]}": v for k, v in preds.items()}, joint=joint, sigma=s0)
    return dict(R=R, gts=gts, dts=dts, gub=gub, dub=dub, g812=g812, dg812=dg812, sq=sq, fr=fr, preds=preds, s0=s0)


def massive_casimir(m, L, nmax=60):
    """Casimir energy of one scalar of mass m on a circle of length L: -(m/pi) sum_n K1(n m L)/n."""
    n = np.arange(1, nmax + 1)
    return -(m / math.pi) * float(np.sum(k1(n * m * L) / n))


def modes():
    say("\n3. The closed tube of 1982: how many modes does it carry?")
    import analyze82 as a82
    with contextlib.redirect_stdout(io.StringIO()):
        P, T = a82.load_all()
        tab = a82.tube_tables(P, T)
    # the three versions of the 1982 energies: as measured; tubes with 3 <= E0 Ly < 5 lowered by 1%; continuum dispersion in (4)
    data = {"as measured": {}, "window (-1%)": {}, "continuum dispersion": {}}
    for beta in (0.73, 0.70):
        L, E, dE = a82.points_at(tab, beta)
        data["as measured"][beta] = (L, E, dE)
        Ely = {}
        for r_ in tab[beta].values():
            if np.isfinite(r_["E"]):
                Ely.setdefault(r_["L"], []).append(r_["E"] * r_["Ly"])
        data["window (-1%)"][beta] = (L, np.array([e * (0.99 if min(Ely[int(l)]) < 5 else 1.0) for l, e in zip(L, E)]), dE)
        Lc, Ec, dEc, w8 = [], [], [], []
        for nme, r_ in tab[beta].items():
            if not np.isfinite(r_["E"]) or r_["E"] * r_["Lx"] < 4 or r_["E"] * r_["Ly"] < 3:
                continue
            if nme.startswith("8"):
                w8.append((r_["E_cont"], r_["dE"]))
            else:
                Lc.append(r_["L"]); Ec.append(r_["E_cont"]); dEc.append(r_["dE"])
        if w8:
            ww = np.array([1 / e ** 2 for _, e in w8])
            Lc.append(8); Ec.append(float((ww * np.array([v for v, _ in w8])).sum() / ww.sum())); dEc.append(float(1 / math.sqrt(ww.sum())))
        o = np.argsort(Lc)
        data["continuum dispersion"][beta] = (np.array(Lc, dtype=float)[o], np.array(Ec)[o], np.array(dEc)[o])
    res = {}
    say("   (a) number of massless modes c (square root with c free; the L^-3 term is fixed by Section 2), by range and by version of the data")
    allc = []
    for var in data:
        for Lmin in (7, 8, 10):
            cs = []
            for beta in (0.73, 0.70):
                L, E, dE = data[var][beta]
                sel = L >= Lmin
                r = a82.fit(L[sel], E[sel], dE[sel], "square root, c free")
                cs.append((r["p"][1], r["dp"][1]))
            w = np.array([1 / c[1] ** 2 for c in cs]); cm = float(np.sum(w * np.array([c[0] for c in cs])) / w.sum()); dcm = float(1 / math.sqrt(w.sum()))
            say(f"       {var:22s} L >= {Lmin:2d}: c = {cs[0][0]:.3f}({cs[0][1]:.3f}) at beta = 0.73, {cs[1][0]:.3f}({cs[1][1]:.3f}) at 0.70; together {cm:.3f}({dcm:.3f})")
            res[f"c|{var}|{Lmin}"] = dict(c=cs, joint=(cm, dcm))
            allc.append(cm)
    c0, dc0 = res["c|as measured|8"]["joint"]
    say(f"       central value (as measured, L >= 8): {c0:.3f}({dc0:.3f}); over ranges and versions: {min(allc):.2f} to {max(allc):.2f}, half-spread {0.5 * (max(allc) - min(allc)):.3f}")
    SUM["c_final"] = dict(c=c0, stat=dc0, lo=min(allc), hi=max(allc))
    # (b) one additional scalar of mass m = mu sqrt(sigma) added to the square root with c = 1; tensions refitted
    say("   (b) one more scalar of mass m: its Casimir energy added to the square root, tensions refitted at each coupling.")
    say("       lower limit on m/sqrt(sigma): where chi2 exceeds its value without the scalar by 2.71 (one-sided 95%) and by 3.84")
    lims = []
    for var in data:
        for Lmin in (7, 8, 10):
            def chi2_of(mu):
                tot = 0.0
                for beta in (0.73, 0.70):
                    L, E, dE = data[var][beta]
                    sel = L >= Lmin
                    def resid(p):
                        sg = p[0]
                        base = np.sqrt(np.maximum(sg**2 * L[sel]**2 - math.pi * sg / 3, 1e-12))
                        extra = np.array([massive_casimir(mu * math.sqrt(sg), l) for l in L[sel]]) if np.isfinite(mu) else 0.0
                        return (base + extra - E[sel]) / dE[sel]
                    r = least_squares(resid, [sigma82(beta)[0]], xtol=1e-14, ftol=1e-14)
                    tot += float(np.sum(r.fun**2))
                return tot
            c_inf = chi2_of(float("inf"))
            ndof = sum(int((data[var][b][0] >= Lmin).sum()) for b in (0.73, 0.70)) - 2
            grid = np.linspace(0.2, 6.0, 59)
            vals = np.array([chi2_of(mu) for mu in grid])
            cmin = float(vals.min())
            out_ = []
            for dchi in (2.71, 3.84):
                f = lambda mu: chi2_of(mu) - c_inf - dchi
                lo = brentq(f, 0.2, 6.0) if f(0.2) * f(6.0) < 0 else float("nan")
                out_.append(lo)
            say(f"       {var:22s} L >= {Lmin:2d}: chi2 without the scalar {c_inf:5.1f}/{ndof}; lowest chi2 with it {cmin:5.1f} at m = {grid[int(vals.argmin())]:.1f};"
                f"  m > {out_[0]:.2f} (2.71), {out_[1]:.2f} (3.84)")
            res[f"m|{var}|{Lmin}"] = dict(chi2_inf=c_inf, dof=ndof, m271=out_[0], m384=out_[1], chi2_min=cmin)
            lims.append((var, Lmin, out_[0]))
    ok = [l[2] for l in lims if np.isfinite(l[2])]
    say(f"       limit (2.71) over ranges and versions: {min(ok):.2f} to {max(ok):.2f}; L >= 10 alone: " + ", ".join(f"{l[2]:.2f}" for l in lims if l[1] == 10))
    SUM["m_limits"] = dict(lo=min(ok), hi=max(ok))
    SUM["modes"] = res
    return data, res


def forecast():
    """What a future measurement of the first gap would need in order to tell the two end terms apart."""
    say("\n4. What would decide between the end terms: shifts of the first gap at long distance, in units of sqrt(sigma)")
    say("    R sqrt(sigma)   square-root gap   +240 e/R^4 for e sigma^1.5 = 0.0019, 0.0104   -24 d/R^2 for d sigma^0.5 = 0.0096")
    rows = []
    for x in (2.0, 2.5, 3.0, 4.0):
        g = math.sqrt(x * x + 2 * math.pi * 23 / 24) - math.sqrt(x * x - math.pi / 12)
        a1, a2, b_ = 240 * 0.0019 / x**4, 240 * 0.0104 / x**4, -24 * 0.0096 / x**2
        say(f"    {x:.1f}             {g:.3f}             {a1:+.4f} ({100 * a1 / g:.1f}%), {a2:+.4f} ({100 * a2 / g:.1f}%)                 {b_:+.4f} ({100 * b_ / g:.1f}%)")
        rows.append((x, g, a1, a2, b_))
    say(f"    the expansion of the first excited level in 1/sigma R^2 converges for R sqrt(sigma) > {math.sqrt(2 * math.pi * 23 / 24):.2f}; of the ground state, for R sqrt(sigma) > {math.sqrt(math.pi / 12):.2f}")
    SUM["forecast"] = rows


def figures(opn, exc, data):
    os.makedirs(FIG, exist_ok=True)
    fig, ax = plt.subplots(1, 2, figsize=(11.5, 4.6))
    a = ax[0]
    xs = np.linspace(0.6, 1.5, 200)
    for beta, col, mk, key in ((0.73, C1, "o", (3, 9)), (0.70, C2, "s", (2, 6))):
        s0 = sigma82(beta)[0]
        rs = math.sqrt(s0)
        fit = opn[beta][key + ("square root + e/R^4",)]
        dat = opn[beta][key + ("data",)]
        R, V, dV = np.array(dat["R"]), np.array(dat["V"]), np.array(dat["dV"])
        rem = (V - (ng_open(fit["p"][0], R) + fit["p"][1])) / rs
        keep = R * rs < 1.5
        a.errorbar((R * rs)[keep], rem[keep], (dV / rs)[keep], fmt=mk, color=col, ms=5, mec=SURF, mew=0.8, capsize=2, lw=1, label=rf"$\beta = {beta:.2f}$ (1976 and 1980)")
    e_s = np.mean([SUM["scaling"]["square root + e/R^4"][k][0] for k in ("b073", "b070")])
    a.plot(xs, e_s / xs**4, color=INK, lw=1.6)
    a.annotate(rf"$e/R^4$, $e\,\sigma^{{3/2}} = {e_s:.4f}$", (0.80, 0.036), color=INK, fontsize=9)
    a.axhline(0, color=INK2, lw=1.0, ls=":")
    a.set_xlim(0.58, 1.5); a.set_ylim(-0.01, 0.075)
    a.set_xlabel(r"$R\sqrt{\sigma}$"); a.set_ylabel(r"$[E_0 - \mu - \sqrt{\sigma^2R^2 - \pi\sigma/12}\,]/\sqrt{\sigma}$")
    a.set_title("Open tube, ground state: what the square root leaves", fontsize=10, loc="left")
    a.legend(loc="upper right", fontsize=8.5)
    b = ax[1]
    R, s0 = exc["R"], exc["s0"]
    rs = math.sqrt(s0)
    b.errorbar(R * rs - 0.012, (exc["gts"] - exc["sq"]) / rs, exc["dts"] / rs, fmt="o", color=C1, ms=5.5, mec=SURF, mew=0.8, capsize=2, lw=1,
               label="two-state estimate (production 3)")
    sel = R <= 8
    b.errorbar((R * rs + 0.012)[sel], ((exc["g812"] - exc["sq"]) / rs)[sel], (exc["dg812"] / rs)[sel], fmt="s", color=C2, ms=5, mec=SURF, mew=0.8, capsize=2, lw=1,
               label="T = 8 to 12 (production 2)")
    rr = np.linspace(3.6, 9.4, 200)
    e_sq = exc["preds"][("square root + e/R^4", 3)]["e"]
    d_sq = exc["preds"][("square root + d/R^2", 4)]["d"]
    b.plot(rr * rs, 240 * e_sq / rr**4 / rs, color=INK, lw=1.6)
    b.plot(rr * rs, -24 * d_sq / rr**2 / rs, color=INK2, lw=1.4, ls="--")
    b.axhline(0, color=INK2, lw=1.0, ls=":")
    b.annotate(r"$+240\,e/R^4$, $e$ from the ground state", (1.36, 0.92), color=INK, fontsize=9)
    b.annotate(r"$-24\,d/R^2$, $d$ from the ground state ($R \geq 4$)", (0.82, -1.45), color=INK2, fontsize=9)
    b.set_xlim(0.78, 2.05); b.set_ylim(-1.6, 1.6)
    b.set_xlabel(r"$R\sqrt{\sigma}$"); b.set_ylabel(r"(first gap $-$ square-root gap)$/\sqrt{\sigma}$")
    b.set_title("First gap minus the square-root gap, and the first-order end shifts", fontsize=10, loc="left")
    b.legend(loc="upper right", fontsize=8.5)
    fig.tight_layout(); fig.savefig(os.path.join(FIG, "fig1_ends.png"), dpi=150); plt.close(fig)

    # Figure 2: the level N = Nbar = 1 of the closed tube in four dimensions
    fig, a = plt.subplots(figsize=(6.8, 4.5))
    Ls = np.linspace(4.5, 12, 300)
    ng = np.sqrt(Ls**2 + 4 * math.pi * (2 - 2 / 12))
    g0 = np.sqrt(Ls**2 - 4 * math.pi * 2 / 12)
    sh = 22 * (4 * math.pi**3 / 3) / Ls**5
    free = 4 * math.pi / Ls
    def level(Lv, lam):       # rule (8) with the phase of (11) added, momenta dressed (Table 5)
        fP = lambda P: P * (Lv + P) - 2 * math.pi * (1 - 1 / 12) + lam * 22 * (4 * (2 * math.pi / (Lv + P)) ** 2) ** 2 / (384 * math.pi)
        return Lv + 2 * brentq(fP, 0.0, 10.0)
    dn = np.array([level(l, +1) for l in Ls]); up = np.array([level(l, -1) for l in Ls])
    a.plot(Ls, (ng - g0) / free, color=INK, lw=1.6, label="square root (2): four degenerate states")
    a.plot(Ls, (dn - g0) / free, color=C1, lw=2.0, label="scalar and pseudoscalar")
    a.plot(Ls, (up - g0) / free, color=C2, lw=2.0, label="spin 2 (two states)")
    a.plot(Ls, (ng - sh - g0) / free, color=C1, lw=0.9, ls="--")
    a.plot(Ls, (ng + sh - g0) / free, color=C2, lw=0.9, ls="--")
    a.annotate("first order (12), dashed", (5.0, 0.36), color=INK2, fontsize=9)
    a.axhline(1.0, color=INK2, lw=1.0, ls=":")
    a.annotate("free phonons", (11.9, 1.01), color=INK2, fontsize=9, ha="right")
    a.set_xlim(4.5, 12); a.set_ylim(0.3, 1.1)
    a.set_xlabel(r"length of the closed tube, $L\sqrt{\sigma}$")
    a.set_ylabel(r"$(E_{1,1} - E_0)\,/\,(4\pi/L)$")
    a.set_title("Four dimensions: the anomaly term splits the two-phonon level", fontsize=10, loc="left")
    a.legend(loc="lower right", fontsize=8.5)
    fig.tight_layout(); fig.savefig(os.path.join(FIG, "fig2_split.png"), dpi=150); plt.close(fig)


if __name__ == "__main__":
    opn = open_tube()
    exc = excited(opn)
    data, mres = modes()
    forecast()
    figures(opn, exc, data)
    open(os.path.join(RES, "refit84.txt"), "w").write("\n".join(lines) + "\n")
    json.dump(SUM, open(os.path.join(RES, "summary84.json"), "w"), indent=1, default=lambda o: o.tolist() if hasattr(o, "tolist") else float(o))
