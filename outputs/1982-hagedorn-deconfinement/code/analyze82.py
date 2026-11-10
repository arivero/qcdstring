#!/usr/bin/env python3
"""Analysis and figures for the 1982 paper. Prints every number quoted;
writes ../results/summary82.json and ../figures/*.png.

    python3 analyze82.py > ../results/analysis82.txt"""
import glob, json, math, os, sys
import numpy as np
from scipy.optimize import least_squares, brentq
from scipy.stats import chi2 as chi2dist
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from tube82 import (RES, beta_of_K, K_of_beta, load_path, free_energy, tube_energy, interp_at, ng_closed,
                    sigma_from_E, F_of_E, E_of_F, Series, crossing, tau_int, binned_error)
from ising_twist import kaufman_lnZ

FIG = os.path.join(HERE, "..", "figures")
C1, C2, C3, C4 = "#2a78d6", "#eb6834", "#1baf7a", "#8e5bd0"
INK, INK2, GRID, SURF = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
plt.rcParams.update({"figure.facecolor": SURF, "axes.facecolor": SURF, "savefig.facecolor": SURF,
                     "axes.edgecolor": INK2, "axes.labelcolor": INK, "xtick.color": INK2, "ytick.color": INK2,
                     "text.color": INK, "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.6,
                     "axes.spines.top": False, "axes.spines.right": False, "font.size": 10,
                     "lines.linewidth": 2, "legend.frameon": False})
CRAY = 12e6 * 3600 * 100          # 100 hours of a Cray-1 at 12 Mflop/s
TH3 = math.sqrt(3 / math.pi)      # T_H / sqrt(sigma), d = 3
TH4 = math.sqrt(3 / (2 * math.pi))
SUMMARY = {}

# geometry -> stretches (joined in K)
PATHS = {
    "16": ["q16", "q16x", "q16r"], "12": ["q12", "q12x", "q12r"], "10": ["g10"],
    "8a": ["q8a", "q8ax"], "8b": ["q8b", "q8bx"], "8c": ["q8c"], "8d": ["q8d"],
    "7": ["g7"], "6": ["g6"], "5": ["g5"], "4": ["g4"], "3": ["g3"],
}
BETAS = (0.73, 0.70)


def fmt(v, e, nd=4):
    return f"{v:.{nd}f}({e * 10 ** nd:.0f})"


def available(names):
    return all(os.path.exists(os.path.join(RES, f"path_{n}.npz")) for n in names)


# ------------------------------------------------------------------------------------------- 0
def check_2d():
    print("0. Exact check in two dimensions (Nt = 1, 24 x 12): thermodynamic integration against Kaufman")
    p = load_path([n for n in ("c2d", "c2dr") if available([n])])
    F, cov, _ = free_energy(p)
    Fp = free_energy(p, corrected=False)[0]
    a0 = kaufman_lnZ(p["Lx"], p["Ly"], p["K"][0])
    f0 = a0["pp"] - a0["pa"]
    print("   K      F (Monte Carlo)    F (trapezoid only)   exact      pull    kink mass from F   exact 2K + ln tanh K")
    rows = []
    for i, K in enumerate(p["K"]):
        a = kaufman_lnZ(p["Lx"], p["Ly"], K)
        ex = a["pp"] - a["pa"] - f0
        if i == 0 or i % 2:
            continue
        g0 = 2 * K + math.log(math.tanh(K))
        e = E_of_F(F[i] + f0, p["Lx"], p["Ly"])
        pull = (F[i] - ex) / math.sqrt(cov[i, i])
        rows.append(dict(K=float(K), F=float(F[i]), dF=float(math.sqrt(cov[i, i])), exact=float(ex), pull=float(pull)))
        print(f"   {K:.2f}   {F[i]:8.4f}({math.sqrt(cov[i,i]):.4f})   {Fp[i]:8.4f}            {ex:8.4f}   {pull:+.2f}    "
              f"{e:.4f}             {g0 if g0 > 0 else float('nan'):.4f}")
    print(f"   {p['flop']:.2e} operations")
    print("   formula Z_A/Z_P = (1/2) sum_k exp(-eps_k Lx) against the exact ratio (no Monte Carlo):")
    print("   K     Lx  Ly   exact F    formula    E from exact F   exact mass   mass x Ly")
    for (K, Lx, Ly) in ((0.50, 24, 12), (0.50, 24, 24), (0.50, 24, 48), (0.60, 24, 12), (0.48, 64, 32), (0.46, 64, 64)):
        a = kaufman_lnZ(Lx, Ly, K)
        Fex = a["pp"] - a["pa"]
        g0 = 2 * K + math.log(math.tanh(K))
        print(f"   {K:.2f}  {Lx:3d} {Ly:3d}  {Fex:8.5f}   {F_of_E(g0, Lx, Ly):8.5f}   {E_of_F(Fex, Lx, Ly):.5f}          {g0:.5f}      {g0 * Ly:.1f}")
    print("   error of the mass recovered through (4), two dimensions, against mass x Ly and the aspect ratio Lx/Ly (Ly = 16):")
    print("   mass x Ly    Lx/Ly = 1      1.5      2        3        4")
    asp = {}
    for target in (2.5, 3.0, 3.5, 4.0, 5.0, 6.0):
        Kt = brentq(lambda K: (2 * K + math.log(math.tanh(K))) * 16 - target, 0.4407, 2.0)
        g0 = 2 * Kt + math.log(math.tanh(Kt))
        errs = []
        for ratio in (1, 1.5, 2, 3, 4):
            Lx = int(round(16 * ratio))
            a = kaufman_lnZ(Lx, 16, Kt)
            errs.append(E_of_F(a["pp"] - a["pa"], Lx, 16) / g0 - 1)
        asp[target] = errs
        print(f"   {target:4.1f}         " + "   ".join(f"{100 * e:+6.2f}%" for e in errs))
    SUMMARY["check_2d"] = rows
    SUMMARY["check_2d_aspect"] = {str(k): [float(x) for x in v] for k, v in asp.items()}
    return p["flop"]


# ------------------------------------------------------------------------------------------- 1
def load_all():
    P, T = {}, {}
    for n, names in PATHS.items():
        if available(names):
            P[n] = load_path(names)
            T[n] = tube_energy(P[n])
    return P, T


def tube_tables(P, T):
    print("\n1. Closed flux tube: free energies and tube energies")
    print("   geometry (Nt x Lx x Ly), couplings, operations; largest ratio of binned to unbinned error; end correction at the last coupling")
    for n in P:
        p, t = P[n], T[n]
        ratio = float(np.max(p["e"] / p["e_naive"]))
        print(f"   {n:>3s}: {p['Nt']:2d} x {p['Lx']} x {p['Ly']}   K = {p['K'][0]:.4f} .. {p['K'][-1]:.4f} ({len(p['K'])} couplings)   "
              f"{p['flop']:.3e}   {ratio:.2f}   {t['F'][-1] - t['F_plain'][-1]:+.4f}")
    out = {}
    for beta in BETAS:
        Kt = float(K_of_beta(beta))
        print(f"\n   beta = {beta} (K = {Kt:.5f})")
        print("   geom   L    F              E0 (lattice dispersion)   E0 (continuum)   F/Lx      E0 x Ly   E0 x Lx")
        rows = {}
        for n in P:
            p, t = P[n], T[n]
            if not (p["K"][0] <= Kt <= p["K"][-1]):
                continue
            F, dF = interp_at(t["K"], t["F"], t["covF"], Kt)
            E, dE = interp_at(t["K"], t["E"], t["covE"], Kt)
            Ec, _ = interp_at(t["K"], t["E_cont"], t["covE"], Kt)
            rows[n] = dict(L=p["Nt"], Lx=p["Lx"], Ly=p["Ly"], F=F, dF=dF, E=E, dE=dE, E_cont=Ec)
            print(f"   {n:>3s}   {p['Nt']:2d}   {F:8.4f}({dF:.4f})   {fmt(E, dE)}                {Ec:.4f}           {F / p['Lx']:.4f}    {E * p['Ly']:5.1f}     {E * p['Lx']:5.1f}")
        out[beta] = rows
        print("   end correction to F at this coupling, and its effect on E0: " + "; ".join(
            f"{n}: {float(np.interp(Kt, T[n]['K'], T[n]['F'] - T[n]['F_plain'])):+.4f} ({abs(float(np.interp(Kt, T[n]['K'], T[n]['F'] - T[n]['F_plain']))) / P[n]['Lx']:.1e})"
            for n in rows))
    print("\n   largest end correction along each path: " + "; ".join(f"{n}: {float(np.max(np.abs(T[n]['F'] - T[n]['F_plain']))):.3f}" for n in P))
    print("   F accumulated between K = 0.15 and 0.20 (it measures how far from zero F is at the start): " + "; ".join(
        f"{n} (Ly = {P[n]['Ly']}): {float(np.interp(0.20, T[n]['K'], T[n]['F'])):+.3f}({float(np.interp(0.20, T[n]['K'], T[n]['dF'])):.3f})" for n in P))
    # F at the first coupling, from an exponential fit A exp(B K) to the integrand on K = 0.15 .. 0.20: F(0.15) = f(0.15)/B
    est = []
    for n in P:
        p = P[n]
        sel = p["K"] <= 0.2001
        K, f, e = p["K"][sel], p["dS"][sel], p["e"][sel]
        try:
            r = least_squares(lambda q: (q[0] * np.exp(q[1] * (K - 0.15)) - f) / e, [max(f[0], 0.01), 40.0], xtol=1e-12, ftol=1e-12)
            c = np.linalg.inv(r.jac.T @ r.jac)
            F0 = r.x[0] / r.x[1]
            dF0 = abs(F0) * math.sqrt(c[0, 0] / r.x[0] ** 2 + c[1, 1] / r.x[1] ** 2 - 2 * c[0, 1] / (r.x[0] * r.x[1]))
            est.append(f"{n} (Ly = {p['Ly']}): {F0:+.4f}({dF0:.4f})")
        except Exception:
            est.append(f"{n}: no fit")
    print("   F at K = 0.15 from an exponential fit to the integrand on K = 0.15 .. 0.20: " + "; ".join(est))
    # 8c (outside the window) against the lattices inside it
    r73 = out[0.73]
    if all(k in r73 for k in ("8a", "8b", "8c", "8d")):
        m, e, _, _, _ = combine_L8(r73)
        d = r73["8c"]["E"] / m - 1
        dd = math.hypot(r73["8c"]["dE"], e) / m
        print(f"   beta = 0.73: the 24 x 8 lattice (outside the window) against the mean of the three inside: {100 * d:+.1f}({100 * dd:.1f})%")
        SUMMARY["Ly8_excess"] = (float(d), float(dd))
    return out


def combine_L8(rows):
    """Weighted mean of the four Nt = 8 geometries at one coupling, with chi^2."""
    names = [n for n in ("8a", "8b", "8c", "8d") if n in rows and np.isfinite(rows[n]["E"])
             and rows[n]["E"] * rows[n]["Lx"] >= 4 and rows[n]["E"] * rows[n]["Ly"] >= 3]      # the window of Section 3.2
    v = np.array([rows[n]["E"] for n in names]); e = np.array([rows[n]["dE"] for n in names])
    w = 1 / e ** 2
    m = (w * v).sum() / w.sum()
    return m, 1 / math.sqrt(w.sum()), float(((v - m) ** 2 * w).sum()), len(names) - 1, names



# ------------------------------------------------------------------------------------------- 2
def points_at(tab, beta, Lmin=0):
    """Independent tube energies at one coupling: one per length, Nt = 8 combined."""
    rows = tab[beta]
    pts = {}
    for n, r in rows.items():
        if n.startswith("8") or not np.isfinite(r["E"]):
            continue
        if r["E"] * r["Lx"] < 4 or r["E"] * r["Ly"] < 3:
            continue                                   # outside the window of Section 3.2
        pts[r["L"]] = (r["E"], r["dE"])
    if any(n.startswith("8") for n in rows):
        m, e, _, _, _ = combine_L8(rows)
        pts[8] = (m, e)
    L = np.array(sorted(k for k in pts if k >= Lmin), dtype=float)
    return L, np.array([pts[int(l)][0] for l in L]), np.array([pts[int(l)][1] for l in L])


MODELS = {
    "square root, c free": (lambda p, L: np.sqrt(np.maximum(p[0] ** 2 * L ** 2 - math.pi * p[0] * p[1] / 3, 1e-12)), [0.05, 1.0], ("sigma", "c")),
    "square root, c = 1":  (lambda p, L: np.sqrt(np.maximum(p[0] ** 2 * L ** 2 - math.pi * p[0] / 3, 1e-12)), [0.05], ("sigma",)),
    "sigma L - gamma/L":   (lambda p, L: p[0] * L - p[1] / L, [0.05, 0.5], ("sigma", "gamma")),
    "sigma L - pi/6L":     (lambda p, L: p[0] * L - math.pi / (6 * L), [0.05], ("sigma",)),
    "sigma L - gamma/L - kappa/L^3": (lambda p, L: p[0] * L - p[1] / L - p[2] / L ** 3, [0.05, 0.5, 1.0], ("sigma", "gamma", "kappa")),
    "sigma L - pi/6L - kappa/L^3":   (lambda p, L: p[0] * L - math.pi / (6 * L) - p[1] / L ** 3, [0.05, 1.0], ("sigma", "kappa")),
    "sigma L - kappa/L^3 (c = 0)":           (lambda p, L: p[0] * L - p[1] / L ** 3, [0.05, 1.0], ("sigma", "kappa")),
    "sigma L - pi/3L - kappa/L^3 (c = 2)":   (lambda p, L: p[0] * L - math.pi / (3 * L) - p[1] / L ** 3, [0.05, 1.0], ("sigma", "kappa")),
    "sigma L":             (lambda p, L: p[0] * L, [0.05], ("sigma",)),
    "sigma L + const":     (lambda p, L: p[0] * L + p[1], [0.05, 0.0], ("sigma", "const")),
}


def fit(L, E, dE, model):
    f, p0, names = MODELS[model]
    r = least_squares(lambda p: (f(p, L) - E) / dE, p0, xtol=1e-14, ftol=1e-14)
    cov = np.linalg.inv(r.jac.T @ r.jac)
    c2, dof = float(np.sum(r.fun ** 2)), len(L) - len(p0)
    return dict(p=r.x.tolist(), dp=np.sqrt(np.diag(cov)).tolist(), chi2=c2, dof=dof,
                pvalue=float(chi2dist.sf(c2, dof)) if dof > 0 else float("nan"), names=names)


def casimir_section(tab):
    print("\n2. The Casimir energy of the closed tube: fits of E0(L) at fixed coupling")
    out = {}
    for beta in BETAS:
        print(f"\n   beta = {beta}")
        L, E, dE = points_at(tab, beta)
        print("   L:  " + "  ".join(f"{int(l):7d}" for l in L))
        print("   E0: " + "  ".join(fmt(e, de) for e, de in zip(E, dE)))
        res = {}
        for Lmin in (5, 6, 7, 8, 10):
            sel = L >= Lmin
            if sel.sum() < 3:
                continue
            for m in MODELS:
                if sel.sum() <= len(MODELS[m][1]):
                    continue
                r = fit(L[sel], E[sel], dE[sel], m)
                res[(Lmin, m)] = r
                par = ", ".join(f"{n} = {p:.5f}({e:.5f})" if n == "sigma" else f"{n} = {p:.3f}({e:.3f})" for n, p, e in zip(r["names"], r["p"], r["dp"]))
                extra = ""
                if m == "sigma L - gamma/L - kappa/L^3":
                    extra = f"   c = 6 gamma/pi = {6 * r['p'][1] / math.pi:.2f}({6 * r['dp'][1] / math.pi:.2f})"
                if "kappa" in r["names"] and "(c = " not in m:
                    extra += f"   [square root: kappa = pi^2/72 sigma = {math.pi ** 2 / (72 * r['p'][0]):.2f}]"
                if "(c = 0)" in m:
                    extra = f"   kappa sigma = {r['p'][1] * r['p'][0]:.2f}({r['dp'][1] * r['p'][0]:.2f})"
                if m == "sigma L - gamma/L":
                    extra = f"   c = 6 gamma/pi = {6 * r['p'][1] / math.pi:.2f}({6 * r['dp'][1] / math.pi:.2f})"
                print(f"   L >= {Lmin:2d} ({int(sel.sum())} lengths)  {m:36s} {par:58s} chi2 {r['chi2']:7.1f}/{r['dof']}  p {r['pvalue']:.3f}{extra}")
        out[beta] = {f"{k[0]}|{k[1]}": v for k, v in res.items()}
        # variant: tubes whose E0 Ly lies between 3 and 5 lowered by 1% (the size of the transverse-size effect, Section 3.2)
        Ely = {}
        for nme, r_ in tab[beta].items():
            if np.isfinite(r_["E"]):
                Ely.setdefault(r_["L"], []).append(r_["E"] * r_["Ly"])
        Ev = np.array([e * (0.99 if min(Ely[int(l)]) < 5 else 1.0) for l, e in zip(L, E)])
        for Lmin in (7, 8):
            sel = L >= Lmin
            if sel.sum() >= 3:
                r = fit(L[sel], Ev[sel], dE[sel], "square root, c free")
                r1 = fit(L[sel], Ev[sel], dE[sel], "sigma L - gamma/L")
                print(f"   variant, L >= {Lmin}, tubes with E0 Ly < 5 lowered by 1%: c = {r['p'][1]:.3f}({r['dp'][1]:.3f}), sigma = {r['p'][0]:.5f}; gamma = {r1['p'][1]:.3f}({r1['dp'][1]:.3f})")
                out[beta][f"variant|{Lmin}"] = dict(c=r["p"][1], dc=r["dp"][1], sigma=r["p"][0], gamma=r1["p"][1], dgamma=r1["dp"][1])
        # reference tension: the square root with c = 1 from L >= 8
        ref = res[(8, "square root, c = 1")]
        s, ds = ref["p"][0], ref["dp"][0]
        print(f"   tension used below: sigma = {s:.5f}({ds:.5f}) (square root, L >= 8), sqrt(sigma) = {math.sqrt(s):.4f}; "
              f"Hagedorn length L_H = {1 / (TH3 * math.sqrt(s)):.2f}")
        print("   L   L sqrt(sigma)   E0            square root   E0/sqrt-1      sigma L - pi/6L   sigma L")
        Lall, Eall, dEall = points_at(tab, beta)
        rows = tab[beta]
        for n in ("5", "4", "3"):                      # show also the points outside the window, marked
            if n in rows and int(n) not in Lall and np.isfinite(rows[n]["E"]):
                Lall = np.append(Lall, int(n)); Eall = np.append(Eall, rows[n]["E"]); dEall = np.append(dEall, rows[n]["dE"])
        o = np.argsort(Lall)
        o_all = o
        for l, e, de in zip(Lall[o], Eall[o], dEall[o]):
            ng = ng_closed(s, l)
            flag = "" if (str(int(l)) not in rows or (rows[str(int(l))]["E"] * rows[str(int(l))]["Lx"] >= 4 and rows[str(int(l))]["E"] * rows[str(int(l))]["Ly"] >= 3)) else "  (outside the window)"
            print(f"   {int(l):2d}   {l * math.sqrt(s):5.2f}          {fmt(e, de)}    {ng:.4f}        {(e / ng - 1) * 100 if np.isfinite(ng) else float('nan'):+6.1f}%        {s * l - math.pi / (6 * l):.4f}            {s * l:.4f}{flag}")
        out[beta]["sigma_ref"] = (s, ds)
        # variant: continuum dispersion law in the momentum sum of (4)
        Lc, Ec, dEc = [], [], []
        w8 = []
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
        Lc, Ec, dEc = np.array(Lc, dtype=float)[o], np.array(Ec)[o], np.array(dEc)[o]
        for Lmin in (7, 8):
            sel = Lc >= Lmin
            r = fit(Lc[sel], Ec[sel], dEc[sel], "square root, c free")
            r1 = fit(Lc[sel], Ec[sel], dEc[sel], "sigma L - gamma/L")
            r2 = fit(Lc[sel], Ec[sel], dEc[sel], "square root, c = 1")
            print(f"   variant, L >= {Lmin}, continuum dispersion in (4): c = {r['p'][1]:.3f}({r['dp'][1]:.3f}), gamma = {r1['p'][1]:.3f}({r1['dp'][1]:.3f}); "
                  f"square root with c = 1: sigma = {r2['p'][0]:.5f}({r2['dp'][0]:.5f}), chi2 {r2['chi2']:.1f}/{r2['dof']}")
            out[beta][f"continuum|{Lmin}"] = dict(c=r["p"][1], dc=r["dp"][1], gamma=r1["p"][1], sigma=r2["p"][0], chi2=r2["chi2"])
        # spread of the tension over the forms that fit from L >= 8, and the dispersion law
        sv = {m: res[(8, m)]["p"][0] for m in ("square root, c free", "square root, c = 1", "sigma L - gamma/L", "sigma L - pi/6L")}
        sv["continuum dispersion, c = 1"] = out[beta]["continuum|8"]["sigma"]
        spread = (max(sv.values()) - min(sv.values())) / 2
        out[beta]["sigma_variants"] = sv
        out[beta]["sigma_ref_tot"] = (s, math.hypot(ds, spread))
        print("   tension under the forms that fit from L >= 8: " + ", ".join(f"{k}: {v:.5f}" for k, v in sv.items()))
        print(f"   tension with the spread of these forms as a systematic error: {s:.5f}({ds:.5f})({spread:.5f}), total {math.hypot(ds, spread):.5f}")
        stot = math.hypot(ds, spread)
        for l, e, de in zip(Lall[o_all], Eall[o_all], dEall[o_all]):
            ng = ng_closed(s, l)
            if np.isfinite(ng) and l * math.sqrt(s) < 1.45 and str(int(l)) in rows and rows[str(int(l))]["E"] * rows[str(int(l))]["Ly"] >= 3 and rows[str(int(l))]["E"] * rows[str(int(l))]["Lx"] >= 4:
                dng = (2 * s * l * l - math.pi / 3) / (2 * ng) * stot
                print(f"   L = {int(l)} (L sqrt(sigma) = {l * math.sqrt(s):.2f}, a sqrt(sigma) = {math.sqrt(s):.2f}) against the square root: "
                      f"{100 * (e / ng - 1):+.1f}({100 * de / ng:.1f})({100 * e / ng * dng / ng:.1f} from the tension)%, total {100 * math.hypot(de / ng, e / ng * dng / ng):.1f}")
                out[beta][f"excess|{int(l)}"] = (float(e / ng - 1), float(math.hypot(de / ng, e / ng * dng / ng)))
        cs = {f"square root, L >= {Lm}": (res[(Lm, 'square root, c free')]['p'][1], res[(Lm, 'square root, c free')]['dp'][1]) for Lm in (7, 8, 10)}
        for Lm in (7, 8):
            cs[f"window variant, L >= {Lm}"] = (out[beta][f"variant|{Lm}"]["c"], out[beta][f"variant|{Lm}"]["dc"])
            cs[f"continuum dispersion, L >= {Lm}"] = (out[beta][f"continuum|{Lm}"]["c"], out[beta][f"continuum|{Lm}"]["dc"])
        vals = [v[0] for v in cs.values()]
        print(f"   c with the L^-3 term of the square root, over ranges and variants: {min(vals):.2f} to {max(vals):.2f}; "
              f"with the L^-3 term free: " + ", ".join(f"L >= {Lm}: {6 * res[(Lm, 'sigma L - gamma/L - kappa/L^3')]['p'][1] / math.pi:.2f}({6 * res[(Lm, 'sigma L - gamma/L - kappa/L^3')]['dp'][1] / math.pi:.2f})"
                                                       for Lm in (6, 7, 8) if (Lm, 'sigma L - gamma/L - kappa/L^3') in res))
        out[beta]["c_variants"] = {k: (float(v[0]), float(v[1])) for k, v in cs.items()}
    SUMMARY["casimir"] = {str(b): {k: v for k, v in o.items()} for b, o in out.items()}
    return out


# ------------------------------------------------------------------------------------------- 3
def sigma_curve(T):
    """Zero-temperature tension against K from the Nt = 16 path (square root, c = 1), with errors."""
    t = T["16"]
    K = t["K"]
    ok = np.isfinite(t["E"]) & (t["E"] * 12 >= 5) & (t["E"] * 24 >= 5)
    sig = np.array([sigma_from_E(e, 16) if o else np.nan for e, o in zip(t["E"], ok)])
    # d sigma / d E for the error
    ds = np.array([(sigma_from_E(e + 1e-5, 16) - sigma_from_E(e - 1e-5, 16)) / 2e-5 * de if o else np.nan
                   for e, de, o in zip(t["E"], t["dE"], ok)])
    return K, sig, ds


def sigma_at(T, Kt):
    K, sig, ds = sigma_curve(T)
    ok = np.isfinite(sig)
    return float(np.interp(Kt, K[ok], sig[ok])), float(np.interp(Kt, K[ok], ds[ok]))


def scaling_section(P, T):
    print("\n3. Scaling curve: E0/sqrt(sigma) against L sqrt(sigma), with sigma(K) from the Nt = 16 tube")
    K16, sig, dsig = sigma_curve(T)
    print("   K        beta      sigma (Nt = 16)   sigma (Nt = 12)")
    for Kt in (0.2325, 0.2350, 0.23655, 0.2400, 0.2450, 0.25179, 0.2600, 0.2700, 0.2761, 0.2850):
        s, ds = sigma_at(T, Kt)
        e12, de12 = interp_at(T["12"]["K"], T["12"]["E"], T["12"]["covE"], Kt)
        s12 = sigma_from_E(e12, 12)
        print(f"   {Kt:.5f}  {beta_of_K(Kt):.4f}    {s:.5f}({ds:.5f})    {s12:.5f}({de12 / 12:.5f})")
    curve = {}
    print("   points inside the window (E0 Lx >= 4, E0 Ly >= 3); x = L sqrt(sigma), y = E0/sqrt(sigma), ratio to the square root")
    for n in ("3", "4", "5", "6", "7", "8a", "10", "12"):
        if n not in T:
            continue
        p, t = P[n], T[n]
        xs, ys, dys, rs, Ks = [], [], [], [], []
        for i, Kt in enumerate(t["K"]):
            e, de = t["E"][i], t["dE"][i]
            if not np.isfinite(e) or e * p["Lx"] < 4 or e * p["Ly"] < 3 or Kt < K16[np.isfinite(sig)][0]:
                continue
            if Kt > K16[-1]:
                continue
            s, ds = sigma_at(T, Kt)
            x, y = p["Nt"] * math.sqrt(s), e / math.sqrt(s)
            ng = ng_closed(1.0, x)
            xs.append(x); ys.append(y); dys.append(math.hypot(de / math.sqrt(s), 0.5 * y * ds / s)); rs.append(y / ng if np.isfinite(ng) else np.nan); Ks.append(Kt)
        curve[n] = dict(x=xs, y=ys, dy=dys, ratio=rs, K=Ks, Nt=p["Nt"])
        line = "  ".join(f"({x:.2f}, {y:.3f}({dy * 1e3:.0f}), {r:.3f})" for x, y, dy, r in list(zip(xs, ys, dys, rs))[:: max(1, len(xs) // 6)])
        print(f"   Nt = {p['Nt']:2d}: {line}")
    SUMMARY["scaling_curve"] = {n: {k: (v if not isinstance(v, list) else [float(a) for a in v]) for k, v in c.items()} for n, c in curve.items()}
    # ratio to the square root at fixed x = L sqrt(sigma), interpolated along each path
    def ratio_at(n, x):
        c = curve[n]
        xs, rs, ys, dys = np.array(c["x"]), np.array(c["ratio"]), np.array(c["y"]), np.array(c["dy"])
        if len(xs) < 2 or not (xs[0] <= x <= xs[-1]):
            return None
        r = float(np.interp(x, xs, rs))
        rel = float(np.interp(x, xs, dys / ys))
        return r, r * rel
    names = [n for n in ("3", "4", "5", "6", "7", "8a", "10") if n in curve]
    print("   Table 7: ratio of the tube energy to the square root at fixed L sqrt(sigma), by tube length in lattice units")
    print("   L sqrt(sigma)  " + "  ".join(f"L = {curve[n]['Nt']:<2d}     " for n in names))
    t7 = {}
    for x in (1.05, 1.12, 1.20, 1.32, 1.40, 1.50, 1.60, 1.80):
        row = {n: ratio_at(n, x) for n in names}
        t7[x] = {n: v for n, v in row.items() if v}
        print(f"   {x:4.2f}           " + "  ".join(f"{row[n][0]:.3f}({1e3 * row[n][1]:2.0f})" if row[n] else "    -     " for n in names))
    print("   Extrapolation at fixed L sqrt(sigma): r_inf + a/L^2 (and r_inf + a/L^4), tube lengths used, chi2/dof")
    ext = {}
    for x in (1.35, 1.40, 1.45, 1.50, 1.55, 1.60, 1.70):
        pts = [(curve[n]["Nt"],) + ratio_at(n, x) for n in names if ratio_at(n, x)]
        if len(pts) < 3:
            continue
        Lv = np.array([p_[0] for p_ in pts], dtype=float); rv = np.array([p_[1] for p_ in pts]); ev = np.array([p_[2] for p_ in pts])
        row = {}
        for power in (2, 4):
            A = np.vstack([np.ones_like(Lv), Lv ** -power]).T
            W = np.diag(1 / ev ** 2)
            cov = np.linalg.inv(A.T @ W @ A)
            p_ = cov @ A.T @ W @ rv
            c2 = float(((A @ p_ - rv) ** 2 / ev ** 2).sum())
            row[power] = (float(p_[0]), float(math.sqrt(cov[0, 0])), c2, len(Lv) - 2)
        ext[x] = row
        print(f"   {x:4.2f}   1/L^2: {row[2][0]:.3f}({1e3 * row[2][1]:.0f}), chi2 {row[2][2]:.1f}/{row[2][3]};   1/L^4: {row[4][0]:.3f}({1e3 * row[4][1]:.0f}), chi2 {row[4][2]:.1f}/{row[4][3]};"
              f"   L = {', '.join(str(int(l)) for l in Lv)}")
    print("   (every tube length is one integration path, and all share sigma(K) from the tube of length 16: the points of one length move together)")
    SUMMARY["table7"] = {str(k): {n: [float(a) for a in v] for n, v in r.items()} for k, r in t7.items()}
    SUMMARY["continuum_ratio"] = {str(k): {str(pw): [float(a) for a in v] for pw, v in r.items()} for k, r in ext.items()}
    # the Nt = 6 tube at beta = 0.73 against the square root
    return curve


# ------------------------------------------------------------------------------------------- 4
FILMS = {1: 0.4407, 2: 0.2761, 3: 0.2459, 4: 0.2361}


def film_section(T):
    print("\n4. Critical couplings of the Ising film (dual of the deconfinement coupling)")
    out = {}
    for Nt, K0 in FILMS.items():
        files = sorted(glob.glob(os.path.join(RES, f"film_Nt{Nt}_L*_K{K0:.4f}.npz")), key=lambda f: int(f.split("_L")[1].split("_")[0]))
        if not files:
            continue
        ser, flop = {}, 0.0
        hw = 0.006 if Nt == 1 else 0.003
        for f in files:
            d = np.load(f)
            L = int(d["L"])
            ser[L] = Series(d["M"] / (Nt * L * L), d["S"], K0, hw)
            flop += float(d["flop"])
            print(f"   Nt = {Nt}, L = {L:2d}: {d['M'].shape[0]} chains of {d['M'].shape[1]} sweeps, tau(m^2) = {ser[L].tau:5.0f}, "
                  f"{ser[L].nb} blocks of {ser[L].blen}, cumulant at K = {K0}: {ser[L].cumulant(K0):.4f}; "
                  f"reweighting range {hw} = {ser[L].sigS * hw:.1f} standard deviations of S")
        Ls = sorted(ser)
        cr = {}
        for a in Ls:
            for b in Ls:
                if a < b:
                    g, dg, u, lost = crossing(ser[a], ser[b])
                    cr[(a, b)] = (g, dg, u)
                    print(f"      crossing of L = {a:2d} and {b:2d}: K = {g:.5f}({dg:.5f}), cumulant {u:.3f}" + (f"   [{100 * lost:.0f}% of the resamplings cross outside the range]" if lost else ""))
        Lmax = Ls[-1]
        best = cr[(Ls[-2], Lmax)]
        others = [cr[(a, Lmax)][0] for a in Ls[:-1]]
        syst = max(abs(o - best[0]) for o in others)
        Kc, dKc = best[0], math.hypot(best[1], syst)
        row = dict(Kc=Kc, dKc_stat=best[1], dKc_syst=syst, dKc=dKc, cumulant=best[2], flop=flop)
        # slope of the cumulant at Kc against L: exponent 1/nu
        sl, dsl = [], []
        for L in Ls:
            def slope(sel=None, L=L):
                U = ser[L].curves(sel)[0]
                h = 0.0006 if Nt > 1 else 0.0012
                return (np.interp(Kc + h, ser[L].g, U) - np.interp(Kc - h, ser[L].g, U)) / (2 * h)
            sl.append(slope()); dsl.append(float(ser[L].boot(slope)))
        sl, dsl = np.array(sl), np.array(dsl)
        r = least_squares(lambda p: (p[0] + p[1] * np.log(Ls) - np.log(sl)) / (dsl / sl), [0.0, 1.0])
        cov = np.linalg.inv(r.jac.T @ r.jac)
        row.update(slopes=sl.tolist(), dslopes=dsl.tolist(), inv_nu=float(r.x[1]), d_inv_nu=float(math.sqrt(cov[1, 1])),
                   chi2_nu=float(np.sum(r.fun ** 2)), dof_nu=len(Ls) - 2)
        if Nt == 1:
            exact = 0.5 * math.log(1 + math.sqrt(2))
            print(f"   Nt = 1 (two-dimensional Ising model): K_c = {Kc:.5f}({best[1]:.5f})({syst:.5f}); exact {exact:.5f}; "
                  f"1/nu = {row['inv_nu']:.2f}({row['d_inv_nu']:.2f}); cumulant at the crossing {best[2]:.3f}")
        else:
            bc = float(beta_of_K(Kc))
            dbc = abs(float(beta_of_K(Kc + dKc)) - bc)
            s, ds = sigma_at(T, Kc)
            sp, _ = sigma_at(T, Kc + dKc)
            dstot = math.hypot(ds, abs(sp - s))
            tc = 1 / (Nt * math.sqrt(s))
            dtc = 0.5 * tc * dstot / s
            row.update(beta_c=bc, dbeta_c=dbc, sigma=s, dsigma=dstot, Tc=tc, dTc=dtc)
            print(f"   Nt = {Nt}: K_c = {Kc:.5f}({best[1]:.5f})({syst:.5f}), beta_c = {bc:.4f}({dbc:.4f}); sigma(K_c) = {s:.4f}({dstot:.4f}); "
                  f"T_c/sqrt(sigma) = {tc:.3f}({dtc:.3f}); T_c/T_H = {tc / TH3:.3f}; 1/nu = {row['inv_nu']:.2f}({row['d_inv_nu']:.2f}) "
                  f"[chi2 {row['chi2_nu']:.1f}/{row['dof_nu']}]; cumulant at the crossing {best[2]:.3f}")
        out[Nt] = row
    if all(n in out for n in (2, 3, 4)):
        x = np.array([1 / n ** 2 for n in (2, 3, 4)]); y = np.array([out[n]["Tc"] for n in (2, 3, 4)]); e = np.array([out[n]["dTc"] for n in (2, 3, 4)])
        A = np.vstack([np.ones(3), x]).T
        W = np.diag(1 / e ** 2)
        cov = np.linalg.inv(A.T @ W @ A)
        p = cov @ A.T @ W @ y
        c2 = float(((A @ p - y) ** 2 / e ** 2).sum())
        # two-point extrapolation from Nt = 3, 4
        a34 = (y[2] * x[1] - y[1] * x[2]) / (x[1] - x[2])
        da34 = math.hypot(e[2] * x[1], e[1] * x[2]) / abs(x[1] - x[2])
        print(f"   T_c/sqrt(sigma) linear in 1/Nt^2: Nt = 2,3,4: {p[0]:.3f}({math.sqrt(cov[0,0]):.3f}), chi2 {c2:.1f}/1; "
              f"Nt = 3,4 only: {a34:.3f}({da34:.3f}).  String value sqrt(3/pi) = {TH3:.4f}")
        print(f"   in units of T_H: Nt = 2, 3, 4: " + ", ".join(f"{out[n]['Tc'] / TH3:.3f}({out[n]['dTc'] / TH3:.3f}) [{(out[n]['Tc'] - TH3) / out[n]['dTc']:.1f} standard errors above 1]" for n in (2, 3, 4))
              + f"; extrapolated {p[0] / TH3:.3f}({math.sqrt(cov[0,0]) / TH3:.3f})")
        out["extrap"] = dict(all=(float(p[0]), float(math.sqrt(cov[0, 0])), c2), two=(float(a34), float(da34)))
    SUMMARY["films"] = {str(k): v for k, v in out.items()}
    return out


def critical_tube(P, T, films):
    """E0(K) of the Nt = 3 and 4 tubes inside the window: how it vanishes."""
    print("\n5. How the tube energy vanishes: E0 against the coupling for Nt = 3 and 4")
    out = {}
    for n in ("4", "3"):
        if n not in T or int(n) not in films:
            continue
        p, t = P[n], T[n]
        Nt = int(n)
        Kc, dKc = films[Nt]["Kc"], films[Nt]["dKc"]
        ok = np.isfinite(t["E"]) & (t["E"] * p["Lx"] >= 4) & (t["E"] * p["Ly"] >= 3)
        Kall, Eall = t["K"][ok], t["E"][ok]
        covall = t["covE"][np.ix_(ok, ok)]
        res = {}
        for rmax in (0.12, 0.08):                      # reduced coupling (K - K_c)/K_c up to rmax
            sel = (Kall - Kc) / Kc <= rmax
            K, E, cov = Kall[sel], Eall[sel], covall[np.ix_(sel, sel)]
            Li = np.linalg.inv(np.linalg.cholesky(cov + 1e-14 * np.eye(len(K))))
            def run(model, p0):
                r = least_squares(lambda q: Li @ (model(q, K) - E), p0, xtol=1e-14, ftol=1e-14)
                c = np.linalg.inv(r.jac.T @ r.jac)
                return r.x, np.sqrt(np.diag(c)), float(np.sum(r.fun ** 2))
            dof = len(K) - 2
            q, dq, c2 = run(lambda q, K: q[0] * (K - q[1]), [15.0, Kc])
            q2, dq2, c22 = run(lambda q, K: q[0] * np.maximum(K - Kc, 1e-9) ** q[1], [15.0, 1.0])
            qlo = run(lambda q, K: q[0] * np.maximum(K - (Kc - dKc), 1e-9) ** q[1], [15.0, 1.0])[0]
            qhi = run(lambda q, K: q[0] * np.maximum(K - (Kc + dKc), 1e-9) ** q[1], [15.0, 1.0])[0]
            q3, dq3, c23 = run(lambda q, K: q[0] * np.sqrt(np.maximum(K - q[1], 1e-12)), [1.0, Kc - 0.002])
            q4, dq4, c24 = run(lambda q, K: q[0] * np.maximum(K - q[1], 1e-9) ** q[2], [15.0, Kc, 1.0])
            r = dict(n=len(K), K_first=float(K[0]), K_last=float(K[-1]), E_first=float(E[0]), E_last=float(E[-1]),
                     line=dict(a=q[0], Kc=q[1], dKc=dq[1], chi2=c2, dof=dof, p=float(chi2dist.sf(c2, dof))),
                     power=dict(a=q2[0], nu=q2[1], dnu=dq2[1], dnu_Kc=abs(qhi[1] - qlo[1]) / 2, chi2=c22, dof=dof, p=float(chi2dist.sf(c22, dof))),
                     sqrt=dict(a=q3[0], K0=q3[1], chi2=c23, dof=dof),
                     free=dict(a=q4[0], Kc=q4[1], dKc=dq4[1], nu=q4[2], dnu=dq4[2], chi2=c24, dof=dof - 1, p=float(chi2dist.sf(c24, dof - 1))))
            res[rmax] = r
            print(f"   Nt = {n}, reduced coupling up to {rmax}: {len(K)} couplings, K = {K[0]:.4f} .. {K[-1]:.4f}, E0 = {E[0]:.3f} .. {E[-1]:.3f}")
            print(f"      straight line a (K - K0):        K0 = {q[1]:.5f}({dq[1]:.5f})  [cumulants: {Kc:.5f}({dKc:.5f})], a = {q[0]:.2f}, chi2 {c2:.1f}/{dof} (p {r['line']['p']:.3f})")
            print(f"      power a (K - K_c)^nu, K_c fixed: nu = {q2[1]:.3f}({dq2[1]:.3f})({r['power']['dnu_Kc']:.3f} from K_c), chi2 {c22:.1f}/{dof} (p {r['power']['p']:.3f})")
            print(f"      power with K_c free:             nu = {q4[2]:.3f}({dq4[2]:.3f}), K_c = {q4[1]:.5f}({dq4[1]:.5f}), chi2 {c24:.1f}/{dof - 1} (p {r['free']['p']:.3f})")
            print(f"      square root a (K - K0)^1/2:      K0 = {q3[1]:.5f}, chi2 {c23:.1f}/{dof}")
        # spread of the exponent over fit choices
        allnu = []
        print("      exponent under other choices (range; K_c fixed or free; with a factor 1 + b (K - K_c)):")
        for rmax in (0.06, 0.08, 0.12, 0.16, 0.20):
            sel = (Kall - Kc) / Kc <= rmax
            if sel.sum() < 4:
                continue
            K, E, cov = Kall[sel], Eall[sel], covall[np.ix_(sel, sel)]
            Li = np.linalg.inv(np.linalg.cholesky(cov + 1e-14 * np.eye(len(K))))
            def run(model, p0):
                r = least_squares(lambda q: Li @ (model(q, K) - E), p0, xtol=1e-14, ftol=1e-14)
                c = np.linalg.inv(r.jac.T @ r.jac)
                return r.x, np.sqrt(np.abs(np.diag(c))), float(np.sum(r.fun ** 2))
            row = []
            qa, da, ca = run(lambda q, K: q[0] * np.maximum(K - Kc, 1e-9) ** q[1], [15.0, 1.0])
            row.append(("K_c fixed", qa[1], da[1], ca, len(K) - 2))
            qb, db, cb = run(lambda q, K: q[0] * np.maximum(K - q[1], 1e-9) ** q[2], [15.0, Kc, 1.0])
            row.append(("K_c free", qb[2], db[2], cb, len(K) - 3))
            if len(K) >= 5:
                qc, dc_, cc = run(lambda q, K: q[0] * np.maximum(K - Kc, 1e-9) ** q[1] * (1 + q[2] * (K - Kc)), [15.0, 1.0, 0.0])
                row.append(("K_c fixed, factor", qc[1], dc_[1], cc, len(K) - 3))
            for lab, v, e, c2_, dof_ in row:
                allnu.append((v, e))
            print(f"      r <= {rmax:.2f} ({len(K)} points): " + ";  ".join(f"{lab}: {v:.3f}({e:.3f}) [{c2_:.1f}/{dof_}]" for lab, v, e, c2_, dof_ in row))
        vs = np.array([a[0] for a in allnu])
        print(f"      exponent over all these choices: {vs.min():.2f} to {vs.max():.2f}")
        # The points nearest K_c have E0 Ly close to 3, where formula (4) reads the energy too high.  Estimate of the
        # effect on the exponent: lower every point by the error (4) has in two dimensions at the same E0 Ly and the
        # same lattice shape, and fit again.
        def err4(target):
            Kt = brentq(lambda K: (2 * K + math.log(math.tanh(K))) * p["Ly"] - target, 0.4407, 2.0)
            g0 = 2 * Kt + math.log(math.tanh(Kt))
            a = kaufman_lnZ(p["Lx"], p["Ly"], Kt)
            return E_of_F(a["pp"] - a["pa"], p["Lx"], p["Ly"]) / g0 - 1
        shift = np.array([err4(min(float(e * p["Ly"]), 12.0)) for e in Eall])
        Ecor = Eall / (1 + shift)
        print(f"      two-dimensional error of (4) at the E0 Ly of each point ({p['Lx']} x {p['Ly']}): "
              + "  ".join(f"{e * p['Ly']:.1f}: {100 * s:+.2f}%" for e, s in list(zip(Eall, shift))[:5]) + "  ...")
        cor = {}
        for rmax in (0.08, 0.12):
            sel = (Kall - Kc) / Kc <= rmax
            K, E, cov = Kall[sel], Ecor[sel], covall[np.ix_(sel, sel)]
            Li = np.linalg.inv(np.linalg.cholesky(cov + 1e-14 * np.eye(len(K))))
            ra = least_squares(lambda q: Li @ (q[0] * np.maximum(K - Kc, 1e-9) ** q[1] - E), [15.0, 1.0], xtol=1e-14, ftol=1e-14)
            rb = least_squares(lambda q: Li @ (q[0] * np.maximum(K - q[1], 1e-9) ** q[2] - E), [15.0, Kc, 1.0], xtol=1e-14, ftol=1e-14)
            cor[rmax] = (float(ra.x[1]), float(rb.x[2]))
            print(f"      with every point lowered by that error, r <= {rmax:.2f}: nu = {ra.x[1]:.3f} (K_c fixed), {rb.x[2]:.3f} (K_c free)")
        xi = 1 / (Eall * Nt)
        loc = np.diff(np.log(Eall)) / np.diff(np.log(Kall - Kc))
        print("      local exponent d ln E0 / d ln(K - K_c) between neighbouring couplings, against xi/Nt = 1/(E0 Nt):")
        print("      " + "  ".join(f"{0.5 * (xi[i] + xi[i + 1]):.2f}: {loc[i]:.2f}" for i in range(min(len(loc), 10))))
        nu_spread = (float(vs.min()), float(vs.max()))
        xi_range = (float(xi.max()), float(xi[(Kall - Kc) / Kc <= 0.12].min()))
        # T_c from the zero of the straight line (wider range)
        K0, dK0 = res[0.12]["line"]["Kc"], res[0.12]["line"]["dKc"]
        s0, ds0 = sigma_at(T, K0)
        sp, _ = sigma_at(T, K0 + dK0)
        dst = math.hypot(ds0, abs(sp - s0))
        tc = 1 / (Nt * math.sqrt(s0))
        print(f"      zero of the straight line as critical coupling: beta = {float(beta_of_K(K0)):.4f}, sigma = {s0:.4f}({dst:.4f}), "
              f"T_c/sqrt(sigma) = {tc:.3f}({0.5 * tc * dst / s0:.3f})  [cumulants: {films[Nt]['Tc']:.3f}({films[Nt]['dTc']:.3f})]")
        out[n] = dict(K=Kall.tolist(), E=Eall.tolist(), dE=np.sqrt(np.diag(covall)).tolist(), Tc_line=tc, dTc_line=0.5 * tc * dst / s0,
                      nu_spread=nu_spread, xi_over_Nt=xi_range, nu_window_corrected={str(k): v for k, v in cor.items()},
                      line=res[0.12]["line"], **{f"range_{k}": v for k, v in res.items()})
    SUMMARY["critical_tube"] = out
    return out


# ------------------------------------------------------------------------------------------- 6
NC = 2
B0 = 11 * NC / (48 * math.pi ** 2)
B1 = (34 / 3) * (NC / (16 * math.pi ** 2)) ** 2


def a_lambda(beta):
    """Two-loop lattice scale, as in the 1978 paper."""
    g2 = 4.0 / beta
    return (B0 * g2) ** (-B1 / (2 * B0 ** 2)) * math.exp(-1 / (2 * B0 * g2))


def su2_curves(sers, grid, sels=None):
    """Cumulant, <P^2> and <|P|> of one lattice on a grid of beta: each run reweighted
    within its half-width, runs combined with weights that fall linearly to zero at
    the edge of each run's range."""
    num, den = np.zeros((3, len(grid))), np.zeros(len(grid))
    for k, sr in enumerate(sers):
        c = sr.curves(None if sels is None else sels[k])
        hw = sr.g[-1] - sr.g0
        w = np.clip(1 - np.abs(grid - sr.g0) / hw, 0, None)
        for j in range(3):
            num[j] += w * np.interp(grid, sr.g, c[j])
        den += w
    return num / np.where(den > 0, den, np.nan)


def su2_section():
    print("\n6. SU(2) in four dimensions: the deconfinement coupling from the closed time-like line")
    out, flop = {}, 0.0
    HW = 0.014
    for Nt in (2, 3, 4):
        lat = {}
        for L in (8, 12):
            files = sorted(glob.glob(os.path.join(RES, f"su2ft_Nt{Nt}_L{L}_b*_s1.npz")))
            if not files:
                continue
            sers = []
            for f in files:
                d = np.load(f)
                V = Nt * L ** 3
                sr = Series(d["pol"], 6 * V * d["plq"], float(d["beta"]), HW)
                sers.append(sr)
                flop += float(d["flop"])
                print(f"   Nt = {Nt}, L = {L:2d}, beta = {float(d['beta']):.2f}: {len(d['pol'])} sweeps, tau(P^2) = {sr.tau:4.0f}, {sr.nb} blocks, "
                      f"<|P|> = {np.abs(d['pol']).mean():.4f}, cumulant {sr.cumulant(sr.g0):.3f}, plaquette {d['plq'].mean():.5f}, "
                      f"spread of the conjugate sum x half-width = {sr.sigS * HW:.2f}")
            lat[L] = sers
        if len(lat) < 2:
            continue
        lo = max(min(sr.g0 for sr in lat[L]) for L in lat) - 0.004
        hi = min(max(sr.g0 for sr in lat[L]) for L in lat) + 0.004
        grid = np.linspace(lo, hi, 241)
        def cross(sels=None):
            ua = su2_curves(lat[8], grid, None if sels is None else sels[8])[0]
            ub = su2_curves(lat[12], grid, None if sels is None else sels[12])[0]
            d = ua - ub
            idx = np.where(np.sign(d[:-1]) * np.sign(d[1:]) < 0)[0]
            if len(idx) == 0:
                return np.nan, np.nan
            i = idx[np.argmin(np.abs(idx - len(grid) / 2))]
            g = grid[i] - d[i] * (grid[i + 1] - grid[i]) / (d[i + 1] - d[i])
            return g, float(np.interp(g, grid, ua))
        bc, uc = cross()
        rng = np.random.default_rng(4 + Nt)
        bs = []
        for _ in range(300):
            sels = {L: [rng.integers(0, sr.nb, sr.nb) for sr in lat[L]] for L in lat}
            bs.append(cross(sels)[0])
        bs = np.array(bs)
        dbc = float(np.nanstd(bs))
        # susceptibility peak of the larger lattice as a second estimate
        c12 = su2_curves(lat[12], grid)
        chi = Nt * 0 + 12 ** 3 * (c12[1] - c12[2] ** 2)
        bpeak = float(grid[np.nanargmax(chi)])
        aL = a_lambda(bc)
        row = dict(beta_c=float(bc), dbeta_c=dbc, cumulant=float(uc), beta_chi_peak=bpeak, aLambda=aL,
                   Tc_over_Lambda=1 / (Nt * aL), dTc_over_Lambda=abs(1 / (Nt * a_lambda(bc + dbc)) - 1 / (Nt * aL)),
                   frac_no_crossing=float(np.mean(~np.isfinite(bs))))
        print(f"   Nt = {Nt}: cumulants of L = 8 and 12 cross at beta_c = {bc:.4f}({dbc:.4f}), cumulant {uc:.3f}; "
              f"peak of V(<P^2> - <|P|>^2) on L = 12 at beta = {bpeak:.3f}; "
              f"T_c/Lambda_L = {row['Tc_over_Lambda']:.1f}({row['dTc_over_Lambda']:.1f})")
        # other ways of joining the three runs of a lattice
        def cross_with(curves_fn):
            d = curves_fn(8) - curves_fn(12)
            idx = np.where(np.sign(d[:-1]) * np.sign(d[1:]) < 0)[0]
            if len(idx) == 0:
                return float("nan")
            i = idx[np.argmin(np.abs(idx - len(grid) / 2))]
            return float(grid[i] - d[i] * (grid[i + 1] - grid[i]) / (d[i + 1] - d[i]))
        def nearest(L):
            g0s = np.array([sr.g0 for sr in lat[L]])
            out_ = np.empty(len(grid))
            for j, g in enumerate(grid):
                sr = lat[L][int(np.argmin(np.abs(g0s - g)))]
                out_[j] = np.interp(g, sr.g, sr.curves()[0])
            return out_
        def narrow(L, hw=0.010):
            num, den = np.zeros(len(grid)), np.zeros(len(grid))
            for sr in lat[L]:
                w = np.clip(1 - np.abs(grid - sr.g0) / hw, 0, None)
                num += w * np.interp(grid, sr.g, sr.curves()[0]); den += w
            return num / np.where(den > 0, den, np.nan)
        alt = [cross_with(nearest), cross_with(narrow)]
        join = max(abs(a_ - bc) for a_ in alt if np.isfinite(a_)) if any(np.isfinite(a_) for a_ in alt) else 0.0
        row.update(beta_c_nearest=alt[0], beta_c_narrow=alt[1], dbeta_c_join=float(join), dbeta_c_tot=float(math.hypot(dbc, join)))
        print(f"      other ways of joining the runs: nearest run {alt[0]:.4f}, weights within 0.010 {alt[1]:.4f}; "
              f"beta_c = {bc:.4f}({dbc:.4f})({join:.4f}), total {math.hypot(dbc, join):.4f}; "
              f"T_c/Lambda_L = {1 / (Nt * a_lambda(bc)):.1f}({abs(1 / (Nt * a_lambda(bc + math.hypot(dbc, join))) - 1 / (Nt * a_lambda(bc))):.1f})")
        row["curves"] = {str(L): [float(x) for x in su2_curves(lat[L], grid)[0][::20]] for L in lat}
        row["grid"] = [float(x) for x in grid[::20]]
        out[Nt] = row
    SUMMARY["su2"] = {str(k): v for k, v in out.items()}
    return out, flop


def su2_tension(su2):
    """T_c in units of the zero-temperature tension, under several ways of extracting the
    tension from Wilson loops. New runs at beta = 1.88 and 2.17; the 1978 runs at 2.2 and 2.3."""
    import io, contextlib
    sys.path.insert(0, os.path.join(HERE, "..", "..", "1978-su2-scaling", "code"))
    import analyze78 as a78
    a78.TSTAR.update({1.88: 1, 2.17: 1})
    a78.FITR.update({2.17: (1, 4)})
    R78 = os.path.join(HERE, "..", "..", "1978-su2-scaling", "results")
    runs, flop = {}, 0.0
    for b in (1.88, 2.17):
        d = json.load(open(os.path.join(RES, f"su2_loops_b{b:.2f}.json")))
        runs[b] = d
        flop += d["flop"]
    old_runs = {b: json.load(open(os.path.join(R78, f"su2_loops_b{b:.2f}.json"))) for b in (2.2, 2.3)}
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        pot = a78.potential_section(runs)
    print("\n7. SU(2): zero-temperature tension at the deconfinement couplings")
    print("   (a) the 1978 procedure on the new runs:")
    for line in buf.getvalue().splitlines()[1:]:
        print("      " + line.strip())
    old = json.load(open(os.path.join(R78, "summary78.json")))["potential"]

    # (b) one fit rule at every coupling: V0 + sigma R - e/R on V(R,T) = ln W(R,T)/W(R,T+1)
    def cornell(d, beta, rmin, rmax, T):
        W = a78.measurements(d)
        blocks, nb, tau = a78.make_blocks(W, beta)
        R = np.arange(1, W.shape[1] + 1)
        def VT(w):
            with np.errstate(invalid="ignore", divide="ignore"):
                return np.log(w[:, T - 1] / w[:, T])
        v, dv, vj = a78.jack(blocks, VT)
        sel = (R >= rmin) & (R <= rmax) & np.isfinite(v) & np.isfinite(dv)
        if sel.sum() < 3:
            return float("nan"), float("nan")
        def f(vv):
            r = least_squares(lambda p: (p[0] + p[1] * R[sel] - p[2] / R[sel] - vv[sel]) / dv[sel], [0.5, 0.1, 0.25])
            return r.x[1]
        c = f(v)
        js = np.array([f(vj[i]) for i in range(nb)])
        return float(c), float(math.sqrt((nb - 1) * np.nanvar(js)))
    def chi(d, beta, n):
        W = a78.measurements(d)
        blocks, nb, tau = a78.make_blocks(W, beta)
        c, e, _ = a78.jack(blocks, lambda w: a78.creutz(w, n, n))
        return float(c), float(e)
    data = {1.88: runs[1.88], 2.17: runs[2.17], 2.2: old_runs[2.2], 2.3: old_runs[2.3]}
    a78.TSTAR.setdefault(2.2, 2); a78.TSTAR.setdefault(2.3, 3)
    rmaxs = {1.88: 4, 2.17: 5, 2.2: 5, 2.3: 6}
    est = {b: {} for b in data}
    for b, d in data.items():
        est[b]["chi(2,2)"] = chi(d, b, 2)
        est[b]["chi(3,3)"] = chi(d, b, 3)
        for T in (1, 2):
            est[b][f"R 1-{rmaxs[b] - 1}, T = {T}"] = cornell(d, b, 1, rmaxs[b] - 1, T)
            est[b][f"R 2-{rmaxs[b]}, T = {T}"] = cornell(d, b, 2, rmaxs[b], T)
    est[1.88]["as in the text"] = (pot["1.88"]["sigma"], pot["1.88"]["dsigma"])
    est[2.17]["as in the text"] = (pot["2.17"]["sigma"], pot["2.17"]["dsigma"])
    est[2.2]["as in the text"] = (old["2.20"]["sigma"], old["2.20"]["dsigma"])
    est[2.3]["as in the text"] = (old["2.30"]["sigma"], old["2.30"]["dsigma"])
    print("   (b) tension under different estimators (lattice units):")
    for b in data:
        print(f"      beta = {b}: " + ";  ".join(f"{k}: {v[0]:.4f}({v[1]:.4f})" for k, v in est[b].items() if np.isfinite(v[0]) and v[1] < 0.3 * abs(v[0])))
    # T_c/sqrt(sigma) per variant
    slope2 = math.log(old["1.90"]["sigma"] / old["1.80"]["sigma"]) / 0.1
    def tc(Nt, sig):
        return 1 / (Nt * math.sqrt(sig))
    variants = {
        "as in the text":   {2: est[1.88]["as in the text"], 3: (est[2.17]["as in the text"], est[2.2]["as in the text"]), 4: (est[2.2]["as in the text"], est[2.3]["as in the text"])},
        "fits from R = 2, T = 1": {2: est[1.88]["R 2-4, T = 1"], 3: (est[2.17]["R 2-5, T = 1"], est[2.2]["R 2-5, T = 1"]), 4: (est[2.2]["R 2-5, T = 1"], est[2.3]["R 2-6, T = 1"])},
        "fits from R = 2, T = 2": {2: est[1.88]["R 2-4, T = 2"], 3: (est[2.17]["R 2-5, T = 2"], est[2.2]["R 2-5, T = 2"]), 4: (est[2.2]["R 2-5, T = 2"], est[2.3]["R 2-6, T = 2"])},
        "fits from R = 1, T = 1": {2: est[1.88]["R 1-3, T = 1"], 3: (est[2.17]["R 1-4, T = 1"], est[2.2]["R 1-4, T = 1"]), 4: (est[2.2]["R 1-4, T = 1"], est[2.3]["R 1-5, T = 1"])},
        "chi(3,3)":         {2: est[1.88]["chi(3,3)"], 3: (est[2.17]["chi(3,3)"], est[2.2]["chi(3,3)"]), 4: (est[2.2]["chi(3,3)"], est[2.3]["chi(3,3)"])},
    }
    out = {}
    print("   (c) T_c/sqrt(sigma) and T_c/T_H under each estimator (statistical errors; beta_c with its total error):")
    print("      estimator                  Nt = 2                  Nt = 3                  Nt = 4")
    table = {}
    for name, v in variants.items():
        row = {}
        # Nt = 2
        s2, d2 = v[2]
        bc, dbc = su2[2]["beta_c"], su2[2]["dbeta_c_tot"]
        if np.isfinite(s2) and d2 < 0.3 * s2:
            sc = s2 * math.exp(slope2 * (bc - 1.88))
            row[2] = (tc(2, sc), 0.5 * tc(2, sc) * math.hypot(d2 / s2, slope2 * dbc))
        # Nt = 3: from 2.17 with the slope to 2.2 of the same estimator
        (sa, da), (sb, db) = v[3]
        bc, dbc = su2[3]["beta_c"], su2[3]["dbeta_c_tot"]
        if np.isfinite(sa) and np.isfinite(sb) and da < 0.3 * sa:
            sl = math.log(sb / sa) / 0.03
            sc = sa * math.exp(sl * (bc - 2.17))
            row[3] = (tc(3, sc), 0.5 * tc(3, sc) * math.hypot(da / sa, sl * dbc))
        # Nt = 4: log-linear between 2.2 and 2.3
        (sa, da), (sb, db) = v[4]
        bc, dbc = su2[4]["beta_c"], su2[4]["dbeta_c_tot"]
        if np.isfinite(sa) and np.isfinite(sb) and db < 0.3 * sb:
            sl = math.log(sb / sa) / 0.1
            sc = sb * math.exp(sl * (bc - 2.3))
            row[4] = (tc(4, sc), 0.5 * tc(4, sc) * math.hypot(db / sb, sl * dbc))
        table[name] = row
        print(f"      {name:24s} " + "   ".join((f"{row[n][0]:.3f}({row[n][1]:.3f}) [{row[n][0] / TH4:.3f}]" if n in row else "        -            ") for n in (2, 3, 4)))
    print("      ranges below: estimators with a statistical error under 5%; chi(3,3) is left out at Nt = 3 and 4, where the 1978 paper")
    print("      found it 15% above the fitted tension")
    for Nt in (2, 3, 4):
        keep = [k for k in table if Nt in table[k] and table[k][Nt][1] < 0.05 * table[k][Nt][0] and not (k == "chi(3,3)" and Nt > 2)]
        vals = [table[k][Nt][0] for k in keep]
        central = table["as in the text"][Nt]
        out[Nt] = dict(Tc=central[0], dTc=central[1], lo=min(vals), hi=max(vals), Tc_over_TH=central[0] / TH4,
                       lo_TH=min(vals) / TH4, hi_TH=max(vals) / TH4, beta_c=su2[Nt]["beta_c"])
        print(f"      Nt = {Nt}: T_c/sqrt(sigma) between {min(vals):.3f} and {max(vals):.3f}, T_c/T_H between {min(vals) / TH4:.2f} and {max(vals) / TH4:.2f}")
    # extrapolations in 1/Nt^2 from Nt = 3, 4 under each estimator
    print("      straight line in 1/Nt^2 through Nt = 3 and 4, T_c/T_H at 1/Nt^2 = 0: " + "; ".join(
        f"{k}: {((table[k][4][0] * (1 / 9) - table[k][3][0] * (1 / 16)) / (1 / 9 - 1 / 16)) / TH4:.2f}" for k in table if 3 in table[k] and 4 in table[k]))
    print(f"   String value in d = 4: sqrt(3/2pi) = {TH4:.4f}")
    SUMMARY["su2_tension"] = {str(k): v for k, v in out.items()}
    SUMMARY["su2_tension_table"] = {k: {str(n): [float(x) for x in v] for n, v in r.items()} for k, r in table.items()}
    SUMMARY["su2_sigma_estimators"] = {str(b): {k: [float(x) for x in v] for k, v in e.items()} for b, e in est.items()}
    return out, flop


# ------------------------------------------------------------------------------------------- 8
def open_tube_section(cas):
    """The 1976 and 1980 potentials between static sources, refitted with the tension
    fixed by the closed tube (a Gaussian constraint on sigma)."""
    import io, contextlib
    sys.path.insert(0, os.path.join(HERE, "..", "..", "1980-excited-flux-tube", "code"))
    import analyze80 as a80
    print("\n8. The open tube of 1976 and 1980 with the tension of the closed tube")
    out = {}
    models = {
        "b free":            (lambda p, R: p[0] * R + p[1] - p[2] / R, [0.05, 0.15, 0.1], ("sigma", "c", "b")),
        "b = pi/24":         (lambda p, R: p[0] * R + p[1] - (math.pi / 24) / R, [0.05, 0.15], ("sigma", "c")),
        "pi/24 + d/R^2":     (lambda p, R: p[0] * R + p[1] - (math.pi / 24) / R + p[2] / R ** 2, [0.05, 0.15, 0.0], ("sigma", "c", "d")),
        "b and d free":      (lambda p, R: p[0] * R + p[1] - p[2] / R + p[3] / R ** 2, [0.05, 0.15, 0.13, 0.0], ("sigma", "c", "b", "d")),
        "b = 0":             (lambda p, R: p[0] * R + p[1], [0.05, 0.15], ("sigma", "c")),
    }
    for beta, ranges in ((0.73, [(2, 9), (3, 9), (4, 9), (5, 9)]), (0.70, [(2, 6), (3, 6)])):
        s0, ds0 = cas[beta]["sigma_ref_tot"]
        with contextlib.redirect_stdout(io.StringIO()):
            gs = a80.ground_state_corr(None, beta, ranges)
            V76, J76, nb76 = a80.data76(beta)
        E80, J80, nb80 = np.array(gs["E0"]), gs["_J"], gs["_nb"]
        print(f"\n   beta = {beta}: closed-tube tension {s0:.5f}({ds0:.5f}) as a constraint (statistical error and spread over the closed-tube forms)")
        res = {}
        for (rmin, rmax) in ranges:
            R = np.arange(rmin, rmax + 1)
            i76 = [r - 1 for r in R if r - 1 < len(V76) and np.all(np.isfinite(J76[:, r - 1]))]
            i80 = [r - 1 for r in R if r - 1 < len(E80) and np.all(np.isfinite(J80[:, r - 1]))]
            def cov(J, idx, nb):
                X = J[:, idx]
                return (nb - 1) / nb * ((X - X.mean(0)).T @ (X - X.mean(0)))
            n1, n2 = len(i76), len(i80)
            C = np.zeros((n1 + n2, n1 + n2))
            C[:n1, :n1] = cov(J76, i76, nb76)
            C[n1:, n1:] = cov(J80, i80, nb80)
            Rall = np.array([i + 1 for i in i76] + [i + 1 for i in i80], dtype=float)
            Vall = np.concatenate([V76[i76], E80[i80]])
            Li = np.linalg.inv(np.linalg.cholesky(C))
            for m, (f, p0, names) in models.items():
                if len(p0) >= len(Rall):
                    continue
                for constrained in (False, True):
                    def resid(p):
                        r = Li @ (f(p, Rall) - Vall)
                        return np.append(r, (p[0] - s0) / ds0) if constrained else r
                    r = least_squares(resid, p0, xtol=1e-14, ftol=1e-14)
                    pc = np.linalg.inv(r.jac.T @ r.jac)
                    c2 = float(np.sum(r.fun ** 2))
                    dof = len(Rall) + int(constrained) - len(p0)
                    res[(rmin, rmax, m, constrained)] = dict(p=r.x.tolist(), dp=np.sqrt(np.diag(pc)).tolist(), chi2=c2, dof=dof,
                                                             pvalue=float(chi2dist.sf(c2, dof)), names=names)
            for m in models:
                a, b = res.get((rmin, rmax, m, False)), res.get((rmin, rmax, m, True))
                if a is None:
                    continue
                def show(r):
                    par = ", ".join(f"{n} {p:.4f}({e:.4f})" for n, p, e in zip(r["names"], r["p"], r["dp"]) if n != "c")
                    return f"{par}; chi2 {r['chi2']:.1f}/{r['dof']} (p {r['pvalue']:.3f})"
                print(f"   R = {rmin}-{rmax}  {m:14s} free: {show(a):70s} | constrained: {show(b)}")
        out[beta] = {f"{k[0]}-{k[1]}|{k[2]}|{'constrained' if k[3] else 'free'}": v for k, v in res.items()}
        # the 1/R coefficient fitted alone under each closed-tube tension (statistical error of that tension only)
        rmin = 4 if beta == 0.73 else 3
        R = np.arange(rmin, ranges[0][1] + 1)
        i76 = [r - 1 for r in R if r - 1 < len(V76) and np.all(np.isfinite(J76[:, r - 1]))]
        i80 = [r - 1 for r in R if r - 1 < len(E80) and np.all(np.isfinite(J80[:, r - 1]))]
        cv = lambda J, idx, nb: (nb - 1) / nb * ((J[:, idx] - J[:, idx].mean(0)).T @ (J[:, idx] - J[:, idx].mean(0)))
        n1, n2 = len(i76), len(i80)
        C = np.zeros((n1 + n2, n1 + n2)); C[:n1, :n1] = cv(J76, i76, nb76); C[n1:, n1:] = cv(J80, i80, nb80)
        Rall = np.array([i + 1 for i in i76] + [i + 1 for i in i80], dtype=float)
        Vall = np.concatenate([V76[i76], E80[i80]])
        Li = np.linalg.inv(np.linalg.cholesky(C))
        dstat = cas[beta]["sigma_ref"][1]
        line = []
        for name, sv in cas[beta]["sigma_variants"].items():
            r = least_squares(lambda p: np.append(Li @ (p[0] * Rall + p[1] - p[2] / Rall - Vall), (p[0] - sv) / dstat), [sv, 0.15, 0.1], xtol=1e-14, ftol=1e-14)
            db = math.sqrt(np.linalg.inv(r.jac.T @ r.jac)[2, 2])
            line.append((name, sv, r.x[2], db, (math.pi / 24 - r.x[2]) / db))
        print(f"   R >= {rmin}, b alone, under each closed-tube tension: " + "; ".join(f"{sv:.5f}: b = {b_:.4f}({db:.4f}), {pl:.1f} s.e. below pi/24" for _, sv, b_, db, pl in line))
        out[beta]["b_by_tension"] = [(n_, float(sv), float(b_), float(db), float(pl)) for n_, sv, b_, db, pl in line]
        bb = res[(rmin, ranges[0][1], "b free", True)]
        print(f"   R >= {rmin}, b alone with the total tension error: b = {bb['p'][2]:.4f}({bb['dp'][2]:.4f}), {(math.pi / 24 - bb['p'][2]) / bb['dp'][2]:.1f} standard errors below pi/24 = {math.pi / 24:.4f}")
    SUMMARY["open_tube"] = {str(k): v for k, v in out.items()}
    return out


# ------------------------------------------------------------------------------------------- 9
PILOT_SCRATCH = [   # runs without stored output; operations from the cost model (code/pilots/README.md)
    ("gauge theory, Nt = 1 against the exact Ising mass (pilots/gauge_nt1_check.py)", 5.5e9),
    ("same-chain test of the two-level wall estimator (pilots/samechain82.py)", 3.8e9),
    ("smearing levels 0-8 for the closed line (pilots/smear_test.py)", 3.4e10),
    ("slow modes: 30,000-sweep histories of eight lattices (pilots/slow_modes.py)", 1.375e11),
]


def budget(flop, P, films):
    print("\n9. Computing budget (100 hours of a Cray-1 at 12 Mflop/s = %.3e operations)" % CRAY)
    rows = []
    rows.append(("Two-dimensional check of the integration (two runs)", sum(np.load(os.path.join(RES, f"path_{n}.npz"))["flop"] for n in ("c2d", "c2dr") if os.path.exists(os.path.join(RES, f"path_{n}.npz")))))
    groups = [("Tubes of length 16 and 12 (three stretches each)", ("16", "12")), ("Tube of length 10", ("10",)),
              ("Tube of length 8, four lattices", ("8a", "8b", "8c", "8d")), ("Tubes of length 7 and 6", ("7", "6")),
              ("Tubes of length 5, 4 and 3", ("5", "4", "3"))]
    for label, names in groups:
        rows.append((label, sum(P[n]["flop"] for n in names if n in P)))
    rows.append(("Ising films, Nt = 2, 3, 4 (cumulants)", sum(films[n]["flop"] for n in (2, 3, 4) if n in films)))
    if 1 in films:
        rows.append(("Two-dimensional check of the cumulant crossing (Nt = 1)", films[1]["flop"]))
    rows.append(("SU(2) at finite temperature, 18 runs", flop.get("su2 finite temperature", 0.0)))
    rows.append(("SU(2) Wilson loops at beta = 1.88 and 2.17", flop.get("su2 zero temperature", 0.0)))
    pil = os.path.join(RES, "pilots")
    g = sum(float(np.load(f)["flop"]) for f in glob.glob(os.path.join(pil, "z2[tw]_*.npz")))
    rows.append(("Gauge-theory wall correlators (17 runs; the direct check of Section 3.4)", g))
    rows.append(("First pilot of the integration method (path_p8)", float(np.load(os.path.join(pil, "path_p8.npz"))["flop"])))
    for label, f in PILOT_SCRATCH:
        rows.append(("Pilot: " + label, f))
    extra = sorted(glob.glob(os.path.join(RES, "extra_*.json")))
    for f in extra:
        d = json.load(open(f))
        rows.append((d["label"], d["flop"]))
    tot = sum(r[1] for r in rows)
    for label, f in rows:
        print(f"   {label:86s} {f:.3e}   {100 * f / CRAY:5.1f}%")
    print(f"   {'Total':86s} {tot:.3e}   {100 * tot / CRAY:5.1f}%  ({tot / CRAY * 100:.0f} hours)")
    direct = g + sum(f for l, f in PILOT_SCRATCH)
    print(f"   of which the direct gauge-theory method (wall correlators and its four pilots): {direct:.3e}, {100 * direct / CRAY:.2f}%")
    SUMMARY["budget"] = dict(rows=[(l, float(f)) for l, f in rows], total=float(tot), cap=CRAY, direct=float(direct))
    return tot


# ------------------------------------------------------------------------------------------- figures
def figures(tab, cas, curve, films, crit, P, T, su2t):
    os.makedirs(FIG, exist_ok=True)
    # ---- Figure 1: the closed tube against its length
    fig, ax = plt.subplots(1, 2, figsize=(11.5, 4.6))
    xx = np.linspace(0.75, 3.7, 400)
    ng = np.array([ng_closed(1.0, x) for x in xx])
    a = ax[0]
    a.plot(xx, xx, color=INK2, lw=1.2, ls=":")
    a.plot(xx, xx - math.pi / (6 * xx), color=INK2, lw=1.2, ls="--")
    a.plot(xx, ng, color=INK, lw=1.6)
    a.annotate(r"$\sigma L$", (2.42, 2.62), color=INK2, fontsize=9, ha="right")
    a.annotate(r"$\sigma L-\pi/6L$ (dashed)", (1.02, 0.62), color=INK2, fontsize=9, ha="right", rotation=0)
    a.annotate("square root (1)", (1.62, 0.95), color=INK, fontsize=9, ha="left")
    for beta, col, mk in ((0.73, C1, "o"), (0.70, C2, "s")):
        L, E, dE = points_at(tab, beta)
        s0 = cas[beta]["sigma_ref"][0]
        a.errorbar(L * math.sqrt(s0), E / math.sqrt(s0), dE / math.sqrt(s0), fmt=mk, color=col, ms=5.5, mec=SURF, mew=0.8,
                   capsize=2, lw=1, label=rf"$\beta = {beta:.2f}$, $L = {int(L[0])}$ to {int(L[-1])}")
    for n, mk, mfc, ms in (("3", "v", C3, 5.5), ("4", "^", SURF, 7.5)):
        c = curve[n]
        sel = [i for i, x in enumerate(c["x"]) if x < 1.28]
        a.errorbar(np.array(c["x"])[sel], np.array(c["y"])[sel], np.array(c["dy"])[sel], fmt=mk, color=C3, ms=ms, mfc=mfc,
                   mec=C3 if mfc == SURF else SURF, mew=1.2 if mfc == SURF else 0.8, capsize=2, lw=1, label=rf"$L = {n}$, coupling varied")
    a.axvline(1 / TH3, color=INK2, lw=0.8)
    a.annotate("endpoint of the square root\n" + r"$L\sqrt{\sigma} = 1.023$", (1 / TH3 + 0.04, 3.45), color=INK2, fontsize=8.5, va="top")
    a.set_xlim(0.45, 3.7); a.set_ylim(0, 3.6)
    a.set_xlabel(r"length of the tube, $L\sqrt{\sigma}$"); a.set_ylabel(r"energy of the tube, $E_0/\sqrt{\sigma}$")
    a.legend(loc="lower right", fontsize=8.5)
    a.set_title("Closed flux tube, Z2 gauge theory in three dimensions", fontsize=10, loc="left")
    b = ax[1]
    xs = np.linspace(1.03, 5.4, 300)
    b.plot(xs, xs * (xs - np.array([ng_closed(1.0, x) for x in xs])), color=INK, lw=1.6)
    b.axhline(math.pi / 6, color=INK2, lw=1.2, ls="--")
    b.axhline(0, color=INK2, lw=1.2, ls=":")
    b.annotate(r"free string, $\pi/6$", (4.2, math.pi / 6 - 0.055), color=INK2, fontsize=9, ha="left")
    b.annotate("no massless mode", (5.38, 0.02), color=INK2, fontsize=9, ha="right")
    b.annotate("square root (1)", (1.5, 0.95), color=INK, fontsize=9)
    for beta, col, mk in ((0.73, C1, "o"), (0.70, C2, "s")):
        L, E, dE = points_at(tab, beta)
        s0 = cas[beta]["sigma_ref"][0]
        b.errorbar(L * math.sqrt(s0), L * (s0 * L - E), L * dE, fmt=mk, color=col, ms=5.5, mec=SURF, mew=0.8, capsize=2, lw=1,
                   label=rf"$\beta = {beta:.2f}$")
    b.set_xlim(0.9, 5.4); b.set_ylim(-0.1, 1.2)
    b.set_xlabel(r"$L\sqrt{\sigma}$"); b.set_ylabel(r"$L\,(\sigma L - E_0)$")
    b.legend(loc="upper right", fontsize=8.5)
    b.set_title("Casimir energy of the tube times its length", fontsize=10, loc="left")
    fig.tight_layout(); fig.savefig(os.path.join(FIG, "fig1_tube.png"), dpi=150); plt.close(fig)

    # ---- Figure 2: how the tube energy vanishes
    fig, ax = plt.subplots(1, 2, figsize=(11.5, 4.3), sharey=True)
    for a, n in zip(ax, ("4", "3")):
        p, t = P[n], T[n]
        Nt = p["Nt"]
        Kc, dKc = films[Nt]["Kc"], films[Nt]["dKc"]
        ok = np.isfinite(t["E"]) & (t["E"] * p["Lx"] >= 4) & (t["E"] * p["Ly"] >= 3) & (t["K"] <= Kc * 1.17)
        Kd, Ed, dEd = t["K"][ok], t["E"][ok], t["dE"][ok]
        Kk = np.linspace(Kc * 0.985, min(Kc * 1.17, 0.2849), 300)
        sg = np.array([sigma_at(T, k)[0] for k in Kk])
        ngc = np.array([ng_closed(sv, Nt) for sv in sg])
        a.axvspan(Kc - dKc, Kc + dKc, color=GRID, lw=0)
        a.plot(Kk, ngc, color=C2, lw=1.8, label="square root (1) with the measured tension")
        ln = crit[n]["line"]
        a.plot(Kk, np.clip(ln["a"] * (Kk - ln["Kc"]), 0, None), color=C1, lw=1.2, label="straight line through the data")
        a.errorbar(Kd, Ed, dEd, fmt="o", color=C1, ms=5, mec=SURF, mew=0.8, capsize=2, lw=1, label=rf"tube of length {Nt}")
        a.annotate("critical coupling\nfrom the cumulants", (Kc + dKc + 0.0006, 0.50), color=INK2, fontsize=8.5, va="top")
        a.set_xlabel(r"Ising coupling $K$   (gauge coupling $\beta$ falls to the right)")
        a.set_title(rf"$L = N_t = {Nt}$", fontsize=10, loc="left")
        a.set_ylim(0, 0.55)
        a.legend(loc="lower right", fontsize=8.5)
        sec = a.secondary_xaxis("top", functions=(lambda k: beta_of_K(np.clip(k, 1e-3, None)), lambda bb: K_of_beta(np.clip(bb, 1e-3, None))))
        sec.set_xlabel(r"$\beta$", fontsize=9)
    ax[0].set_ylabel(r"energy of the closed tube, $E_0$ (lattice units)")
    fig.tight_layout(); fig.savefig(os.path.join(FIG, "fig2_critical.png"), dpi=150); plt.close(fig)

    # ---- Figure 3: T_c in units of the string's Hagedorn temperature
    fig, a = plt.subplots(figsize=(6.6, 4.4))
    x = np.array([1 / n ** 2 for n in (2, 3, 4)])
    yz = np.array([films[n]["Tc"] / TH3 for n in (2, 3, 4)]); ez = np.array([films[n]["dTc"] / TH3 for n in (2, 3, 4)])
    ys = np.array([su2t[n]["Tc"] / TH4 for n in (2, 3, 4)])
    lo = np.array([su2t[n]["lo_TH"] for n in (2, 3, 4)]); hi = np.array([su2t[n]["hi_TH"] for n in (2, 3, 4)])
    a.axhline(1.0, color=INK, lw=1.2)
    a.annotate(r"$T_c = T_H$ of the string", (0.005, 1.010), color=INK, fontsize=9, ha="left")
    a.errorbar(x, yz, ez, fmt="o", color=C1, ms=6, mec=SURF, mew=0.8, capsize=2, lw=1, label="Z2, three dimensions")
    a.errorbar(x, ys, [ys - lo, hi - ys], fmt="s", color=C2, ms=6, mec=SURF, mew=0.8, capsize=2, lw=1,
               label="SU(2), four dimensions (bar: range over tension estimators)")
    for xi, n in zip(x, (2, 3, 4)):
        a.annotate(rf"$N_t = {n}$", (xi, 0.80), color=INK2, fontsize=8.5, ha="center")
    a.set_xlim(0, 0.27); a.set_ylim(0.78, 1.3)
    a.set_xlabel(r"$1/N_t^2$"); a.set_ylabel(r"$T_c/T_H$")
    a.legend(loc="upper right", fontsize=9)
    fig.tight_layout(); fig.savefig(os.path.join(FIG, "fig3_tc.png"), dpi=150); plt.close(fig)

if __name__ == "__main__":
    flop = {}
    flop["2d check"] = check_2d()
    P, T = load_all()
    tab = tube_tables(P, T)
    for beta in BETAS:
        if any(n in tab[beta] for n in ("8a", "8b", "8c", "8d")):
            m, e, c2, dof, names = combine_L8(tab[beta])
            print(f"\n   beta = {beta}: Nt = 8 from {names}: E0 = {fmt(m, e)}, chi2 = {c2:.1f}/{dof}")
    cas = casimir_section(tab)
    curve = scaling_section(P, T)
    films = film_section(T)
    crit = critical_tube(P, T, films)
    su2, flop['su2 finite temperature'] = su2_section()
    su2t, flop['su2 zero temperature'] = su2_tension(su2)
    opent = open_tube_section(cas)
    total = budget(flop, P, films)
    figures(tab, cas, curve, films, crit, P, T, su2t)
    json.dump(SUMMARY, open(os.path.join(RES, 'summary82.json'), 'w'), indent=1, default=lambda o: o.tolist() if hasattr(o, 'tolist') else str(o))
