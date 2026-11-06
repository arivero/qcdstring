#!/usr/bin/env python3
"""Analysis and figures for the 1976 paper. Reads ../results/*, writes
../results/summary.json and ../figures/*.png, and prints every number
quoted in the text."""
import glob, json, math, os
import numpy as np
from scipy.optimize import least_squares
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(HERE, "..", "results")
FIG = os.path.join(HERE, "..", "figures")
C1, C2, C3 = "#2a78d6", "#eb6834", "#1baf7a"     # categorical slots 1-3 (validated)
INK, INK2, GRID, SURF = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
plt.rcParams.update({"figure.facecolor": SURF, "axes.facecolor": SURF, "savefig.facecolor": SURF,
                     "axes.edgecolor": INK2, "axes.labelcolor": INK, "xtick.color": INK2, "ytick.color": INK2,
                     "text.color": INK, "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.6,
                     "axes.spines.top": False, "axes.spines.right": False, "font.size": 10,
                     "lines.linewidth": 2, "legend.frameon": False})
CDC7600 = 3.3e6 * 3600 * 100   # 100 hours at 3.3 Mflop/s
summary = {}


# ---------------------------------------------------------------- Z2 potential
def load_z2(beta):
    files = sorted(glob.glob(os.path.join(RES, f"z2ml_b{beta:.3f}_s*.npz")))
    files = [f for f in files if "pilot" not in f]
    Cs, meta, flop = [], None, 0.0
    for f in files:
        d = np.load(f)
        Cs.append(d["C"].mean(axis=2))           # average the two separation directions
        flop += float(d["flop"])
        meta = {k: int(d[k]) for k in ("Nt", "L", "tau", "nsub", "between", "therm")}
    return Cs, meta, flop, len(files)


def blocks_from_chains(Cs, bsize):
    out = []
    for C in Cs:
        n = len(C) // bsize
        out.extend(C[: n * bsize].reshape(n, bsize, -1).mean(axis=1))
    return np.array(out)


def potential(Cmean, Nt):
    R = np.arange(1, len(Cmean) + 1)
    with np.errstate(invalid="ignore", divide="ignore"):
        V = -np.log(Cmean) / Nt
    q = np.exp(-math.pi * Nt / R)                       # free-string excited levels, d = 3
    corr = -sum(np.log(1 - q ** k) for k in range(1, 6)) / Nt
    return V + corr, corr                               # E_0 = V_meas + (1/Nt) sum_k -ln(1-q^k)


def fit(R, V, dV, model):
    if model == "free":
        f = lambda p, r: p[0] * r + p[1] - p[2] / r
        p0 = [0.05, 0.1, 0.13]
    elif model == "luscher":
        f = lambda p, r: p[0] * r + p[1] - (math.pi / 24) / r
        p0 = [0.05, 0.1]
    elif model == "ng":
        f = lambda p, r: np.sqrt(np.maximum(p[0] ** 2 * r ** 2 - math.pi * p[0] / 12, 1e-12)) + p[1]
        p0 = [0.05, 0.1]
    elif model == "nocasimir":
        f = lambda p, r: p[0] * r + p[1]
        p0 = [0.05, 0.1]
    r = least_squares(lambda p: (f(p, R) - V) / dV, p0)
    chi2 = float(np.sum(r.fun ** 2))
    return r.x, chi2, len(R) - len(p0), f


from scipy.stats import chi2 as chi2dist

MODELS = {
    "free":          (lambda p, r: p[0] * r + p[1] - p[2] / r, [0.05, 0.1, 0.13], ("sigma", "c", "b")),
    "luscher":       (lambda p, r: p[0] * r + p[1] - (math.pi / 24) / r, [0.05, 0.1], ("sigma", "c")),
    "zero":          (lambda p, r: p[0] * r + p[1], [0.05, 0.1], ("sigma", "c")),
    "endpoint":      (lambda p, r: p[0] * r + p[1] - (math.pi / 24) / r + p[2] / r ** 2, [0.05, 0.1, 0.0], ("sigma", "c", "d")),
    "free_endpoint": (lambda p, r: p[0] * r + p[1] - p[2] / r + p[3] / r ** 2, [0.05, 0.1, 0.13, 0.0], ("sigma", "c", "b", "d")),
    "ng":            (lambda p, r: np.sqrt(np.maximum(p[0] ** 2 * r ** 2 - math.pi * p[0] / 12, 0.0)) + p[1], [0.05, 0.15], ("sigma", "c")),
}


def corr_fit(R, V, cov, model, p0=None):
    """Fit with the full covariance: chi^2 = r^T cov^-1 r, via Cholesky whitening.
    Errors from (J^T cov^-1 J)^-1."""
    f, q0, names = MODELS[model]
    Lc = np.linalg.cholesky(cov)
    Li = np.linalg.inv(Lc)
    res = least_squares(lambda p: Li @ (f(p, R) - V), q0 if p0 is None else p0, xtol=1e-14, ftol=1e-14)
    J = res.jac
    pcov = np.linalg.inv(J.T @ J)
    chi2 = float(np.sum(res.fun ** 2))
    dof = len(R) - len(q0)
    return {"p": res.x.tolist(), "dp": np.sqrt(np.diag(pcov)).tolist(), "chi2": chi2, "dof": dof,
            "pvalue": float(chi2dist.sf(chi2, dof)) if dof > 0 else float("nan"), "names": names}


CORR_RANGES = {0.73: [(2, 8), (3, 8), (4, 8), (3, 9), (4, 9)], 0.70: [(2, 6), (3, 6), (2, 5)]}


def analyse_beta(beta, Rfit):
    Cs, meta, flop, nch = load_z2(beta)
    Nt = meta["Nt"]
    B = blocks_from_chains(Cs, 5)
    nb = len(B)
    Cm = B.mean(axis=0)
    V, corr = potential(Cm, Nt)
    jk = np.array([potential((Cm * nb - B[i]) / (nb - 1), Nt)[0] for i in range(nb)])
    dV = np.sqrt((nb - 1) * np.nanvar(jk, axis=0))
    rel = B.std(axis=0, ddof=1) / math.sqrt(nb) / np.abs(Cm)
    R = np.arange(1, len(Cm) + 1)
    res = {"beta": beta, "chains": nch, "outer_per_chain": len(Cs[0]), "blocks": nb, **meta,
           "R": R.tolist(), "V": V.tolist(), "dV": dV.tolist(), "C": Cm.tolist(), "C_relerr": rel.tolist(),
           "excited_level_correction": corr.tolist(), "flop": flop}
    fits = {}
    for (rmin, rmax) in Rfit:
        sel = (R >= rmin) & (R <= rmax)
        for model in ("free", "luscher", "ng", "nocasimir"):
            p, chi2, dof, f = fit(R[sel], V[sel], dV[sel], model)
            pj = np.array([fit(R[sel], jk[i][sel], dV[sel], model)[0] for i in range(nb)])
            dp = np.sqrt((nb - 1) * np.var(pj, axis=0))
            fits[f"{model}_{rmin}-{rmax}"] = {"p": p.tolist(), "dp": dp.tolist(), "chi2": chi2, "dof": dof}
    res["fits"] = fits
    # correlated fits (Response, Major 1-2); covariance of V from the jackknife
    cfits = {}
    for (rmin, rmax) in CORR_RANGES[beta]:
        sel = (R >= rmin) & (R <= rmax)
        J = jk[:, sel]
        cov = (nb - 1) / nb * ((J - J.mean(axis=0)).T @ (J - J.mean(axis=0)))
        for model in MODELS:
            if model == "ng":
                sig0 = fits[f"luscher_{Rfit[0][0]}-{Rfit[0][1]}"]["p"][0]
                if rmin * math.sqrt(sig0) <= 0.51 * 1.15:
                    continue
            if len(MODELS[model][1]) >= sel.sum():
                continue
            cfits[f"{model}_{rmin}-{rmax}"] = corr_fit(R[sel], V[sel], cov, model)
    res["corr_fits"] = cfits
    # correlation of neighbouring V(R)
    good = [i for i in range(1, min(8, jk.shape[1])) if np.all(np.isfinite(jk[:, i]))]
    cc = np.corrcoef(jk[:, good].T)
    res["neighbour_correlation"] = float(np.mean([cc[i, i + 1] for i in range(cc.shape[0] - 1)]))
    F = V[1:] - V[:-1]
    Fj = jk[:, 1:] - jk[:, :-1]
    res["F"] = F.tolist()
    res["dF"] = np.sqrt((nb - 1) * np.nanvar(Fj, axis=0)).tolist()
    # local effective b from three consecutive R: exact solution of V = s R + c - b/R
    beff = []
    for r0 in range(3, len(R) - 1):
        def bloc(v):
            A = np.array([[r, 1, -1 / r] for r in (r0 - 1, r0, r0 + 1)], dtype=float)
            return np.linalg.solve(A, v[r0 - 2: r0 + 1])[2]
        b0 = bloc(V)
        bj = np.array([bloc(jk[i]) for i in range(nb)])
        beff.append((r0, b0, math.sqrt((nb - 1) * np.nanvar(bj))))
    res["b_local"] = beff
    return res, jk


def z2_section():
    out = {}
    plans = {0.73: [(2, 8), (3, 8), (2, 7), (3, 9)], 0.70: [(2, 6), (2, 5), (3, 6)]}
    figdata = {}
    for beta, rf in plans.items():
        r, jk = analyse_beta(beta, rf)
        out[f"{beta:.2f}"] = r
        figdata[beta] = r
        print(f"\nZ2, beta = {beta}: {r['chains']} chains x {r['outer_per_chain']} outer, Nt = {r['Nt']}, L = {r['L']}, slabs of {r['tau']}, {r['nsub']} sub-updates")
        for i, R in enumerate(r["R"]):
            print(f"   R = {R:2d}: V = {r['V'][i]:.5f} +/- {r['dV'][i]:.5f}   (rel. error of C {r['C_relerr'][i]:.3f}; excited-level corr {r['excited_level_correction'][i]:.1e})")
        for k, v in r["fits"].items():
            names = {"free": ("sigma", "c", "b"), "luscher": ("sigma", "c"), "ng": ("sigma", "c"), "nocasimir": ("sigma", "c")}[k.split("_")[0]]
            s = ", ".join(f"{n} = {p:.4f}({dp:.4f})" for n, p, dp in zip(names, v["p"], v["dp"]))
            print(f"   fit {k:16s}: {s};  chi2/dof = {v['chi2']:.1f}/{v['dof']}")
        print("   local b from three consecutive R:", ", ".join(f"R={a}: {b:.3f}({c:.3f})" for a, b, c in r["b_local"]))
        print(f"   mean correlation of neighbouring V(R): {r['neighbour_correlation']:.3f}")
        for k, v in r["corr_fits"].items():
            s_ = ", ".join(f"{n} = {p:.4f}({dp:.4f})" for n, p, dp in zip(v["names"], v["p"], v["dp"]))
            print(f"   correlated {k:20s}: {s_};  chi2/dof = {v['chi2']:.1f}/{v['dof']}  p = {v['pvalue']:.3f}")
    return out, figdata


def z2_figure(figdata):
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    ax = axes[0]
    r = figdata[0.73]
    F = np.array(r["F"]); dF = np.array(r["dF"])
    Rm = np.arange(1, len(F) + 1)              # force between R and R+1
    ok = np.isfinite(F) & (dF < 0.02)
    ax.errorbar(Rm[ok] + 0.5, F[ok], dF[ok], fmt="o", color=C1, ms=6, capsize=2, lw=1.2, mec=SURF, mew=1,
                label=r"$V(R+1)-V(R)$, $\beta=0.73$")
    rr = np.arange(2, 10)
    cf = r["corr_fits"]
    s1, c1, d1 = cf["endpoint_2-8"]["p"]
    ax.plot(rr + 0.5, s1 + (math.pi / 24) / (rr * (rr + 1)) - d1 * (2 * rr + 1) / (rr * rr * (rr + 1) ** 2),
            color=INK2, lw=1.5, ls="--", label=r"$b = \pi/24$ and $d/R^2$, $R = 2$-8")
    s2, c2, b2 = cf["free_3-8"]["p"]
    ax.plot(rr + 0.5, s2 + b2 / (rr * (rr + 1)), color=C1, lw=1.5, label=fr"free $b = {b2:.3f}$, $R = 3$-8")
    s3, c3 = cf["zero_4-8"]["p"]
    ax.plot(rr + 0.5, s3 + 0 * rr, color=INK2, lw=1.5, ls=":", label=r"$b = 0$, $R = 4$-8")
    ax.set_xlabel("R + 1/2 (lattice units)")
    ax.set_ylabel("force (lattice units)")
    ax.set_title("Force between static sources (correlated fits)", fontsize=10, loc="left")
    ax.legend(loc="upper right", fontsize=9)
    ax = axes[1]
    for beta, col, mk, key in ((0.73, C1, "o", "free_3-8"), (0.70, C2, "s", "free_3-6")):
        rb = figdata[beta]
        sq = math.sqrt(rb["corr_fits"][key]["p"][0])
        bl = np.array(rb["b_local"])
        ok = bl[:, 2] < 0.1
        ax.errorbar(bl[ok, 0] * sq, bl[ok, 1], bl[ok, 2], fmt=mk, color=col, ms=6, capsize=2, lw=1.2, mec=SURF, mew=1,
                    label=fr"$\beta = {beta}$")
    ax.axhline(math.pi / 24, color=INK2, ls="--", lw=1.5)
    ax.text(0.62, math.pi / 24 + 0.006, r"$\pi/24$ (free string)", color=INK2)
    ax.set_ylim(0, 0.2)
    ax.set_xlabel(r"$R\sqrt{\sigma}$ (centre of the three points)")
    ax.set_ylabel(r"$b$ from $V$ at $R-1$, $R$, $R+1$")
    ax.set_title("Local coefficient of the 1/R term", fontsize=10, loc="left")
    ax.legend(loc="lower right")
    fig.tight_layout()
    fig.savefig(os.path.join(FIG, "fig2_z2_casimir.png"), dpi=150)
    plt.close(fig)


# ---------------------------------------------------------------- Z2 strong coupling
def strong_section():
    p = os.path.join(RES, "z2_strong.json")
    if not os.path.exists(p):
        return None
    d = json.load(open(p))
    fig, ax = plt.subplots(figsize=(5.5, 4))
    b = np.array([r["beta"] for r in d["rows"]])
    for key, col, mk, lab in (("chi22", C1, "o", r"$\chi(2,2)$"), ("chi33", C2, "s", r"$\chi(3,3)$")):
        y = np.array([r[key][0] for r in d["rows"]]); e = np.array([r[key][1] for r in d["rows"]])
        ok = np.isfinite(y) & np.isfinite(e) & (e < 0.2)
        ax.errorbar(b[ok] + (0.004 if key == "chi33" else 0), y[ok], e[ok], fmt=mk, color=col, ms=6, capsize=2, lw=1.2, mec=SURF, mew=1, label=lab)
    bb = np.linspace(0.22, 0.76, 300)
    u = np.tanh(bb)
    ax.plot(bb, -np.log(u), color=INK2, lw=1.5, ls=":", label=r"$-\ln u$")
    ax.plot(bb, -np.log(u) - 2 * u ** 4, color=INK2, lw=1.5, ls="--", label=r"$-\ln u - 2u^4$")
    for beta, col, mk in ((0.73, C1, "D"), (0.70, C2, "D")):
        pass
    ax.axvline(0.7613, color=INK2, lw=0.8)
    ax.text(0.755, 1.5, r"$\beta_c = 0.7613$", color=INK2, ha="right")
    ax.set_xlabel(r"$\beta$")
    ax.set_ylabel(r"$\chi(R,R)$ (lattice units)")
    ax.set_title("3d Z2: strong coupling and beyond", fontsize=10, loc="left")
    ax.legend(loc="lower left")
    ax.set_ylim(0, 1.6)
    fig.tight_layout()
    fig.savefig(os.path.join(FIG, "fig1_z2_strong.png"), dpi=150)
    plt.close(fig)
    print("\nZ2 strong coupling (L = %d):" % d["L"])
    for r in d["rows"]:
        print(f"   beta {r['beta']:.2f}: plaquette {r['plaquette']:.4f}  chi22 {r['chi22'][0]:.4f}({r['chi22'][1]:.4f})"
              f"  chi23 {r['chi23'][0]:.4f}({r['chi23'][1]:.4f})  chi33 {r['chi33'][0]:.4f}({r['chi33'][1]:.4f})"
              f"  -ln u {r['sc_lead']:.4f}  O(u^4) {r['sc_u4']:.4f}")
    return d


# ---------------------------------------------------------------- U(1)
def u1_section():
    out = {}
    p = os.path.join(RES, "u1_cycle.json")
    cyc = json.load(open(p)) if os.path.exists(p) else None
    p = os.path.join(RES, "u1_loops.json")
    loops = json.load(open(p)) if os.path.exists(p) else None
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    if cyc:
        ax = axes[0]
        for dirn, col, mk in (("up", C1, "^"), ("down", C2, "v")):
            rows = [r for r in cyc["rows"] if r["direction"] == dirn]
            ax.errorbar([r["beta"] for r in rows], [r["plaquette"] for r in rows], [r["err"] for r in rows],
                        fmt=mk + "-", color=col, ms=7, lw=1.2, mec=SURF, mew=1, label=f"{'increasing' if dirn=='up' else 'decreasing'} $\\beta$")
        from scipy.special import i0, i1
        bb = np.linspace(0.65, 0.98, 100)
        uu = i1(bb) / i0(bb)
        ax.plot(bb, uu + 4 * uu ** 5, color=INK2, ls="--", lw=1.5, label=r"$u + 4u^5$, $u = I_1(\beta)/I_0(\beta)$")
        ax.set_xlabel(r"$\beta$"); ax.set_ylabel(r"$\langle\cos\theta_P\rangle$")
        ax.set_title(f"U(1), d = 4, {cyc['L']}$^4$: a thermal cycle", fontsize=10, loc="left")
        ax.legend(loc="upper left")
        out["cycle"] = cyc["rows"]
    if loops:
        ax = axes[1]
        rows = []
        for r in loops:
            W = np.array(r["W"])
            nb = 20
            blk = W[: len(W) // nb * nb].reshape(nb, -1, W.shape[1], W.shape[2]).mean(axis=1)
            Wm = W.mean(axis=0)
            def chi(W_, R, T):
                num, den = W_[R - 1, T - 1] * W_[R - 2, T - 2], W_[R - 1, T - 2] * W_[R - 2, T - 1]
                return -math.log(num / den) if num > 0 and den > 0 else float("nan")
            row = {"beta": r["beta"], "plaquette": float(np.mean(r["plaq"]))}
            for (R, T) in ((2, 2), (3, 3), (4, 4)):
                c = chi(Wm, R, T)
                jk = np.array([chi((Wm * nb - blk[i]) / (nb - 1), R, T) for i in range(nb)])
                row[f"chi{R}{T}"] = (c, float(math.sqrt((nb - 1) * np.var(jk))) if np.all(np.isfinite(jk)) else float("nan"))
            from scipy.special import i0, i1
            u = i1(r["beta"]) / i0(r["beta"])
            row["sc_u4"] = -math.log(u) - 4 * u ** 4
            rows.append(row)
        out["loops"] = rows
        b = np.array([r["beta"] for r in rows])
        for key, col, mk, lab in (("chi22", C1, "o", r"$\chi(2,2)$"), ("chi33", C2, "s", r"$\chi(3,3)$")):
            y = np.array([r[key][0] for r in rows]); e = np.array([r[key][1] for r in rows])
            ok = np.isfinite(y) & np.isfinite(e) & (e < 0.3)
            ax.errorbar(b[ok] + (0.006 if key == "chi33" else 0), y[ok], e[ok], fmt=mk, color=col, ms=6, capsize=2, lw=1.2, mec=SURF, mew=1, label=lab)
        from scipy.special import i0, i1
        bb = np.linspace(0.55, 1.0, 100)
        u = i1(bb) / i0(bb)
        ax.plot(bb, -np.log(u) - 4 * u ** 4, color=INK2, ls="--", lw=1.5, label=r"$-\ln u - 4u^4$")
        ax.axhline(0, color=INK2, lw=0.8)
        ax.set_xlabel(r"$\beta$"); ax.set_ylabel(r"$\chi(R,R)$")
        ax.set_title(f"U(1), d = 4, {loops[0]['L']}$^4$: the area law ends", fontsize=10, loc="left")
        ax.legend(loc="upper right")
        print(f"\nU(1) ratios chi(R,R), L = {loops[0]['L']}:")
        for r in rows:
            print(f"   beta {r['beta']:.2f}: plaquette {r['plaquette']:.4f}  chi22 {r['chi22'][0]:.4f}({r['chi22'][1]:.4f})  chi33 {r['chi33'][0]:.4f}({r['chi33'][1]:.4f})  chi44 {r['chi44'][0]:.4f}({r['chi44'][1]:.4f})  SC O(u^4) {r['sc_u4']:.4f}")
    fig.tight_layout()
    fig.savefig(os.path.join(FIG, "fig3_u1.png"), dpi=150)
    plt.close(fig)
    return out


def budget():
    rows = []
    def add(name, path, key="flop"):
        if not os.path.exists(path):
            return
        if path.endswith(".npz"):
            return
        d = json.load(open(path))
        if isinstance(d, list):
            f = sum(x["flop"] for x in d)
        elif "runs" in d:
            f = sum(x["flop"] for x in d["runs"])
        else:
            f = d["flop"]
        rows.append((name, f))
    add("Z2 estimator validation", os.path.join(RES, "z2_validate.json"))
    add("Z2 strong coupling", os.path.join(RES, "z2_strong.json"))
    for beta in (0.73, 0.70):
        _, _, f, _ = load_z2(beta)
        rows.append((f"Z2 two-level, beta = {beta}", f))
    add("U(1) thermal cycle", os.path.join(RES, "u1_cycle.json"))
    add("U(1) Wilson loops", os.path.join(RES, "u1_loops.json"))
    add("Z2 direct check at production parameters", os.path.join(RES, "z2_direct_check.json"))
    p2 = os.path.join(RES, "u1_two_starts.json")
    if os.path.exists(p2):
        d2 = json.load(open(p2))
        rows.append(("U(1) two starts at beta = 1.00", d2["hot"]["flop"] + d2["cold"]["flop"]))
    rows.append(("pilot runs (code/pilots/README.md)", 1.63e11))
    tot = sum(f for _, f in rows)
    print("\nComputing budget (flop-equivalents; CDC 7600, 100 h at 3.3 Mflop/s = %.2e):" % CDC7600)
    for n, f in rows:
        print(f"   {n:32s} {f:.2e}  ({100*f/CDC7600:5.1f} %)")
    print(f"   {'total':32s} {tot:.2e}  ({100*tot/CDC7600:5.1f} %)  = {tot/3.3e6/3600:.0f} CDC 7600 hours")
    return {"rows": rows, "total": tot, "cap": CDC7600}


def main():
    z2, figdata = z2_section()
    summary["z2"] = z2
    z2_figure(figdata)
    summary["z2_strong"] = strong_section()
    summary["u1"] = u1_section()
    summary["budget"] = budget()
    json.dump(summary, open(os.path.join(RES, "summary.json"), "w"), indent=1, default=float)


if __name__ == "__main__":
    main()
