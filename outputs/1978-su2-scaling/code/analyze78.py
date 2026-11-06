#!/usr/bin/env python3
"""Analysis and figures for the 1978 paper. Reads ../results/*, prints
every number quoted, writes ../results/summary78.json and ../figures/*.png."""
import glob, json, math, os
import numpy as np
from scipy.optimize import least_squares
from scipy.special import iv
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(HERE, "..", "results")
FIG = os.path.join(HERE, "..", "figures")
C1, C2, C3 = "#2a78d6", "#eb6834", "#1baf7a"
INK, INK2, GRID, SURF = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
plt.rcParams.update({"figure.facecolor": SURF, "axes.facecolor": SURF, "savefig.facecolor": SURF,
                     "axes.edgecolor": INK2, "axes.labelcolor": INK, "xtick.color": INK2, "ytick.color": INK2,
                     "text.color": INK, "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.6,
                     "axes.spines.top": False, "axes.spines.right": False, "font.size": 10,
                     "lines.linewidth": 2, "legend.frameon": False})
CAP = 3.3e6 * 3600 * 100
VARIANTS = {}
N = 2
B0 = 11 * N / (48 * math.pi ** 2)
B1 = (34 / 3) * (N / (16 * math.pi ** 2)) ** 2
TSTAR = {1.5: 1, 1.6: 1, 1.7: 1, 1.8: 1,  # initial T for blocking; T* itself is chosen by the rule
         1.9: 1, 2.0: 2, 2.1: 2, 2.2: 2, 2.3: 3, 2.4: 3, 2.5: 4, 2.6: 4}
FITR = {2.2: (1, 4), 2.3: (1, 5), 2.4: (2, 5), 2.5: (2, 7), 2.6: (2, 7)}


def a_lambda(beta, loops=2):
    g2 = 4.0 / beta
    if loops == 1:
        return math.exp(-1 / (2 * B0 * g2))
    return (B0 * g2) ** (-B1 / (2 * B0 ** 2)) * math.exp(-1 / (2 * B0 * g2))


def strong(beta):
    u = iv(2, beta) / iv(1, beta)
    return u, -math.log(u) - 4 * u ** 4


def jack(blocks, fn):
    nb = len(blocks)
    tot = blocks.mean(axis=0)
    c = fn(tot)
    js = np.array([fn((tot * nb - blocks[i]) / (nb - 1)) for i in range(nb)])
    return c, np.sqrt((nb - 1) * np.nanvar(js, axis=0)), js


def creutz(W, R, T):
    num, den = W[R - 1, T - 1] * W[R - 2, T - 2], W[R - 1, T - 2] * W[R - 2, T - 1]
    return -math.log(num / den) if num > 0 and den > 0 else float("nan")


THERM_CUT = 0.25          # fraction of measurements discarded at beta >= 2.4 (Response, Major 3)


def load(pattern=r"su2_loops_b\d\.\d\d\.json"):
    import re
    runs = {}
    for f in sorted(glob.glob(os.path.join(RES, "su2_loops_b*.json"))):
        if not re.fullmatch(pattern, os.path.basename(f)):
            continue
        d = json.load(open(f))
        runs[round(d["beta"], 2)] = d
    return runs


def tau_int(x, wmax=40):
    """Integrated autocorrelation time (in measurements) with a self-consistent window."""
    x = np.asarray(x) - np.mean(x)
    v = np.mean(x * x)
    tau = 0.5
    for t in range(1, min(wmax, len(x) // 3)):
        c = np.mean(x[:-t] * x[t:]) / v
        tau += c
        if t >= 6 * tau:
            break
    return max(tau, 0.5)


def measurements(d):
    W = np.array(d["W"])
    if d["beta"] >= 2.4 and not d.get("hot_start", False) and "_L" not in d.get("tag", ""):
        W = W[int(THERM_CUT * len(W)):]
    return W


def make_blocks(W, beta):
    """Blocks of at least four autocorrelation times of the largest loop used."""
    Rm = W.shape[1]
    ts = TSTAR.get(beta, 1)
    series = W[:, min(Rm, FITR.get(beta, (1, Rm))[1]) - 1, min(ts, W.shape[2] - 1)]
    tau = tau_int(series)
    nb = int(max(5, min(20, len(W) // max(1, int(math.ceil(4 * tau))))))
    B = W[: len(W) // nb * nb].reshape(nb, -1, W.shape[1], W.shape[2]).mean(axis=1)
    return B, nb, tau


def potential_section(runs):
    out = {}
    print("SU(2), d = 4: Wilson loops")
    for beta, d in sorted(runs.items()):
        W = measurements(d)
        blocks, nb, tau = make_blocks(W, beta)
        Rm = d["Rmax"]
        row = {"beta": beta, "L": d["L"], "n_smear": d["n_smear"], "nmeas": d["nmeas"], "plaquette": float(np.mean(d["plaq"])),
               "n_used": len(W), "blocks": nb, "tau_int": tau}
        # Creutz ratios
        for R in range(2, Rm + 1):
            c, e, _ = jack(blocks, lambda w, R=R: creutz(w, R, R))
            row[f"chi{R}{R}"] = (c, float(e))
        # V(R, T) = ln W(R,T)/W(R,T+1)
        def VRT(w):
            with np.errstate(invalid="ignore", divide="ignore"):
                return np.log(w[:, :-1] / w[:, 1:])
        Vt, dVt, Vj = jack(blocks, VRT)
        row["V_RT"] = Vt.tolist(); row["dV_RT"] = dVt.tolist()
        ts = TSTAR[beta]
        if beta in FITR:
            rmin, rmax = FITR[beta]
            R = np.arange(1, Rm + 1)
            def fitT(v, dv, model):
                sel = (R >= rmin) & (R <= rmax) & np.isfinite(v) & np.isfinite(dv)
                if model == "cornell":
                    f = lambda p: (p[0] + p[1] * R[sel] - p[2] / R[sel] - v[sel]) / dv[sel]
                    p0 = [0.5, 0.1, 0.25]
                else:
                    f = lambda p: (p[0] + p[1] * R[sel] - (math.pi / 12) / R[sel] - v[sel]) / dv[sel]
                    p0 = [0.5, 0.1]
                r = least_squares(f, p0)
                return r.x, float(np.sum(r.fun ** 2)), int(sel.sum()) - len(p0)
            # sigma(T) for every T with its jackknife error; T* = first T at which
            # sigma(T) and sigma(T+1) agree within the error of the difference
            sigT = {}
            for T in range(1, Vt.shape[1] + 1):
                v, dv = Vt[:, T - 1], dVt[:, T - 1]
                if np.sum(np.isfinite(v[rmin - 1:rmax]) & (dv[rmin - 1:rmax] < 0.05)) < rmax - rmin + 1:
                    break
                p, _, _ = fitT(v, dv, "cornell")
                pj = np.array([fitT(Vj[i][:, T - 1], dv, "cornell")[0][1] for i in range(nb)])
                sigT[T] = (p[1], pj)
            ts = None
            for T in sorted(sigT):
                if T + 1 in sigT:
                    diff = sigT[T][0] - sigT[T + 1][0]
                    dj = sigT[T][1] - sigT[T + 1][1]
                    ddiff = math.sqrt((nb - 1) * np.var(dj))
                    if abs(diff) < ddiff:
                        ts = T
                        break
            if ts is None:
                ts = max(sigT) - 1
            row["sigma_vs_T"] = {int(T): (float(v[0]), float(math.sqrt((nb - 1) * np.var(v[1])))) for T, v in sigT.items()}
        V, dV = Vt[:, ts - 1], dVt[:, ts - 1]
        row["Tstar"] = ts
        row["V"] = V.tolist(); row["dV"] = dV.tolist()
        u, sc = strong(beta)
        row["strong_coupling"] = sc
        if beta in FITR:
            sel = (R >= rmin) & (R <= rmax) & np.isfinite(V)
            for model in ("cornell", "luscher"):
                p, chi2, dof = fitT(V, dV, model)
                pj = np.array([fitT(Vj[i][:, ts - 1], dV, model)[0] for i in range(nb)])
                dp = np.sqrt((nb - 1) * np.var(pj, axis=0))
                row[f"fit_{model}"] = {"range": [rmin, rmax], "p": p.tolist(), "dp": dp.tolist(), "chi2": chi2, "dof": dof}
            row["sigma_Tplus1"] = float(sigT[ts + 1][0]) if ts + 1 in sigT else float("nan")
            s, ds = row["fit_cornell"]["p"][1], row["fit_cornell"]["dp"][1]
            # systematic: largest shift of sigma at any later T measured to within twice the error at T*
            shifts = [abs(v[0] - s) for T, v in row["sigma_vs_T"].items() if T > ts and v[1] < 2 * ds]
            row["dsigma_syst"] = max(shifts) if shifts else 0.0
        else:
            # strong coupling region: tension from the largest reliable Creutz ratio
            best = None
            for R in range(Rm, 1, -1):
                c, e = row[f"chi{R}{R}"]
                if np.isfinite(c) and e < 0.05 * abs(c):
                    best = (R, c, e); break
            s, ds = best[1], best[2]
            row["sigma_from"] = f"chi({best[0]},{best[0]})"
        row["sigma"] = float(s); row["dsigma"] = float(ds)
        row.setdefault("dsigma_syst", 0.0)
        dtot = math.hypot(ds, row["dsigma_syst"])
        aL2, aL1 = a_lambda(beta, 2), a_lambda(beta, 1)
        row["aLambda2"] = aL2
        row["sqrt_sigma_over_Lambda"] = math.sqrt(s) / aL2
        row["d_sqrt_sigma_over_Lambda"] = 0.5 * ds / math.sqrt(s) / aL2
        row["d_sqrt_sigma_over_Lambda_tot"] = 0.5 * dtot / math.sqrt(s) / aL2
        row["sqrt_sigma_over_Lambda_1loop"] = math.sqrt(s) / aL1
        out[f"{beta:.2f}"] = row
        chis = "  ".join(f"chi{R}{R} {row[f'chi{R}{R}'][0]:.4f}({row[f'chi{R}{R}'][1]:.4f})" for R in range(2, Rm + 1))
        print(f"  beta {beta:.2f} L {d['L']:2d} smear {d['n_smear']:2d} meas {d['nmeas']}: plaquette {row['plaquette']:.5f}  {chis}  strong coupling {sc:.4f}")
        print("     V(R) at T* = %d: " % ts + ", ".join(f"{v:.4f}({e:.4f})" for v, e in zip(V, dV)))
        print("     V(R) at T*+1:   " + ", ".join(f"{v:.4f}({e:.4f})" for v, e in zip(Vt[:, min(ts, Vt.shape[1]-1)], dVt[:, min(ts, Vt.shape[1]-1)])))
        for model in ("cornell", "luscher"):
            if f"fit_{model}" in row:
                fr = row[f"fit_{model}"]
                print(f"     fit {model:8s} R {fr['range']}: " + ", ".join(f"{n} {p:.4f}({e:.4f})" for n, p, e in zip(("V0", "sigma", "e"), fr["p"], fr["dp"])) + f"; chi2 {fr['chi2']:.1f}/{fr['dof']}")
        if "sigma_Tplus1" in row:
            print(f"     sigma from T*+1: {row['sigma_Tplus1']:.4f}")
        if "sigma_vs_T" in row:
            print("     sigma(T): " + ", ".join(f"T{T}: {v[0]:.4f}({v[1]:.4f})" for T, v in row["sigma_vs_T"].items()) + f"  -> T* = {row['Tstar']}")
        print(f"     sigma a^2 = {s:.4f}({ds:.4f})(syst {row['dsigma_syst']:.4f}); a Lambda_L (2-loop) = {aL2:.3e}; sqrt(sigma)/Lambda_L = {row['sqrt_sigma_over_Lambda']:.1f}({row['d_sqrt_sigma_over_Lambda']:.1f} stat, {row['d_sqrt_sigma_over_Lambda_tot']:.1f} total); 1-loop {row['sqrt_sigma_over_Lambda_1loop']:.1f}")
    return out


def scaling_variants(runs, pot):
    """Response, Major 1-2 and 5: the tension and the 1/R coefficient at
    beta = 2.4-2.6 under the analysis choices a reader could make."""
    from scipy.stats import chi2 as chi2dist
    out = {}
    print("\nVariants at beta = 2.4-2.6 (errors: jackknife over blocks of >= 4 autocorrelation times)")
    for beta in (2.4, 2.5, 2.6):
        d = runs[beta]
        W = measurements(d)
        B, nb, tau = make_blocks(W, beta)
        R = np.arange(1, W.shape[1] + 1)
        def VRT(w):
            with np.errstate(invalid="ignore", divide="ignore"):
                return np.log(w[:, :-1] / w[:, 1:])
        tot = B.mean(axis=0)
        Vt = VRT(tot)
        Vj = np.array([VRT((tot * nb - B[i]) / (nb - 1)) for i in range(nb)])
        dVt = np.sqrt((nb - 1) * np.nanvar(Vj, axis=0))
        # 20-block covariance for an indicative correlated chi^2
        B20 = W[: len(W) // 20 * 20].reshape(20, -1, W.shape[1], W.shape[2]).mean(axis=1)
        t20 = B20.mean(axis=0)
        V20 = np.array([VRT((t20 * 20 - B20[i]) / 19) for i in range(20)])
        ts = pot[f"{beta:.2f}"]["Tstar"]
        rmin, rmax = FITR[beta]
        def fit(T, lo, hi, efix=None, samples=False):
            sel = (R >= lo) & (R <= hi)
            v, dv = Vt[:, T - 1], dVt[:, T - 1]
            if efix is None:
                f = lambda p, vv: (p[0] + p[1] * R[sel] - p[2] / R[sel] - vv[sel]) / dv[sel]
                p0 = [0.5, 0.05, 0.25]
            else:
                f = lambda p, vv: (p[0] + p[1] * R[sel] - efix / R[sel] - vv[sel]) / dv[sel]
                p0 = [0.5, 0.05]
            p = least_squares(lambda q: f(q, v), p0).x
            pj = np.array([least_squares(lambda q: f(q, Vj[i][:, T - 1]), p).x for i in range(nb)])
            dp = np.sqrt((nb - 1) * np.var(pj, axis=0))
            # correlated chi^2 with the 20-block covariance
            J = V20[:, sel, T - 1]
            cov = 19 / 20 * ((J - J.mean(0)).T @ (J - J.mean(0)))
            m = p[0] + p[1] * R[sel] - (p[2] if efix is None else efix) / R[sel]
            r_ = m - v[sel]
            try:
                chi2c = float(r_ @ np.linalg.solve(cov, r_))
            except np.linalg.LinAlgError:
                chi2c = float("nan")
            dof = int(sel.sum()) - len(p0)
            return {"T": T, "R": [int(lo), int(hi)], "p": p.tolist(), "dp": dp.tolist(), "chi2_corr": chi2c, "dof": dof,
                    "p_corr": float(chi2dist.sf(chi2c, dof)) if dof > 0 and np.isfinite(chi2c) else float("nan")}
        A = fit(ts, rmin, rmax)
        errA = A["dp"][1]
        Tlate = ts
        for T in range(ts + 1, Vt.shape[1] + 1):
            ok = np.all(np.isfinite(Vt[rmin - 1:rmax, T - 1]))
            if not ok:
                break
            try:
                f_ = fit(T, rmin, rmax)
            except Exception:
                break
            if f_["dp"][1] < 2 * errA:
                Tlate = T
        Bv = fit(ts, rmin, rmax, efix=math.pi / 12)
        Cv = fit(Tlate, rmin, rmax)
        sq = math.sqrt(A["p"][1])
        lo2 = max(2, int(math.ceil(0.4 / sq))); hi2 = min(W.shape[1], int(math.floor(1.4 / sq)))
        Dv = fit(ts, lo2, hi2) if hi2 - lo2 >= 3 else None
        aL = a_lambda(beta)
        res = {"tau_int": tau, "blocks": nb, "n_used": len(W), "Tstar": ts, "Tlate": Tlate}
        print(f"  beta {beta}: {len(W)} measurements used, tau_int {tau:.1f}, {nb} blocks; T* = {ts}, latest usable T = {Tlate}")
        for name, v in (("A  e free, T*", A), ("B  e = pi/12, T*", Bv), ("C  e free, latest T", Cv), ("D  e free, R sqrt(sigma) 0.4-1.4", Dv)):
            if v is None:
                continue
            sig, dsig = v["p"][1], v["dp"][1]
            ratio = math.sqrt(sig) / aL; dratio = 0.5 * dsig / math.sqrt(sig) / aL
            v["ratio"] = ratio; v["dratio"] = dratio
            e_ = f"e {v['p'][2]:.3f}({v['dp'][2]:.3f})" if len(v["p"]) == 3 else "e = pi/12   "
            print(f"     {name:34s} T={v['T']} R={v['R'][0]}-{v['R'][1]}: sigma {sig:.4f}({dsig:.4f})  sqrt(sigma)/Lambda_L {ratio:.1f}({dratio:.1f})  {e_}  corr chi2 {v['chi2_corr']:.1f}/{v['dof']}")
            res[name.split()[0]] = v
        out[f"{beta:.2f}"] = res
    # scaling leverage: one-loop and two-loop ratios over 2.4-2.6
    print("  one-loop / two-loop ratio (variant A):", ", ".join(f"{b}: {math.sqrt(out[b]['A']['p'][1]) / a_lambda(float(b), 1):.0f} / {out[b]['A']['ratio']:.1f}" for b in out))
    return out


def fv_section(main):
    """Response, Major 4: smaller boxes and a hot start, same analysis as the main runs."""
    out = {}
    print("\nFinite volume and start (variant A fits where the box allows):")
    for tag in ("_L8", "_L12hot"):
        p = glob.glob(os.path.join(RES, f"su2_loops_b*{tag}.json"))
        if not p:
            continue
        d = json.load(open(p[0])); d["tag"] = tag
        beta = round(d["beta"], 2)
        W = np.array(d["W"])
        nb = 10
        B = W[: len(W) // nb * nb].reshape(nb, -1, W.shape[1], W.shape[2]).mean(axis=1)
        Wm = W.mean(axis=0)
        def VRT(w):
            with np.errstate(invalid="ignore", divide="ignore"):
                return np.log(w[:, :-1] / w[:, 1:])
        Vt = VRT(B.mean(axis=0)); Vj = np.array([VRT((B.mean(axis=0) * nb - B[i]) / (nb - 1)) for i in range(nb)])
        dVt = np.sqrt((nb - 1) * np.nanvar(Vj, axis=0))
        Wm_main = measurements(main[beta]).mean(axis=0)
        Vmain = VRT(Wm_main)
        rows = []
        for T in (2, 3):
            line = []
            for Rr in range(2, W.shape[1] + 1):
                if np.isfinite(Vt[Rr - 1, T - 1]):
                    line.append(f"R{Rr}: {Vt[Rr-1, T-1]:.4f}({dVt[Rr-1, T-1]:.4f}) vs {Vmain[Rr-1, T-1]:.4f}")
            print(f"   beta {beta} L {d['L']}{' hot' if d.get('hot_start') else ''}, T = {T}: " + "; ".join(line))
        # tension from R = 2..Rmax at T = 2 and 3, compared with the main run over the same R
        for T in (2, 3):
            Rr = np.arange(2, W.shape[1] + 1)
            def sfit(v, dv):
                ok = np.isfinite(v) & np.isfinite(dv)
                r = least_squares(lambda q: (q[0] + q[1] * Rr[ok] - q[2] / Rr[ok] - v[ok]) / dv[ok], [0.5, 0.05, 0.25])
                return r.x[1]
            sv = sfit(Vt[1:, T - 1], dVt[1:, T - 1])
            sj = np.array([sfit(Vj[i][1:, T - 1], dVt[1:, T - 1]) for i in range(nb)])
            ds = math.sqrt((nb - 1) * np.var(sj))
            sm = sfit(Vmain[1:W.shape[1], T - 1], dVt[1:, T - 1])
            print(f"     tension from R = 2-{W.shape[1]} at T = {T}: {sv:.4f}({ds:.4f}) here, {sm:.4f} in the main run over the same R")
            rows.append({"T": T, "sigma": sv, "dsigma": ds, "sigma_main_sameR": sm})
        out[f"{beta:.2f}{tag}"] = {"L": d["L"], "hot": d.get("hot_start", False), "rows": rows, "flop": d["flop"],
                                    "plaquette": float(np.mean(d["plaq"])), "plaquette_main": float(np.mean(main[beta]["plaq"]))}
        print(f"     plaquette {np.mean(d['plaq']):.5f} here, {np.mean(main[beta]['plaq']):.5f} main")
    return out


def figures(pot, cyc, heat):
    # figure 1: sigma a^2 against beta, strong coupling and asymptotic freedom
    fig, ax = plt.subplots(figsize=(6, 4.2))
    b = np.array(sorted(float(k) for k in pot))
    s = np.array([pot[f"{x:.2f}"]["sigma"] for x in b]); ds = np.array([pot[f"{x:.2f}"]["dsigma"] for x in b])
    ax.errorbar(b, s, ds, fmt="o", color=C1, ms=6, capsize=2, lw=1.2, mec=SURF, mew=1, label=r"$\sigma a^2$, this work")
    bb = np.linspace(1.45, 2.3, 100)
    ax.plot(bb, [strong(x)[1] for x in bb], color=INK2, ls="--", lw=1.5, label=r"$-\ln u - 4u^4$")
    ref = pot["2.50"]["sqrt_sigma_over_Lambda"] if "2.50" in pot else None
    if ref:
        bb2 = np.linspace(2.1, 2.75, 100)
        ax.plot(bb2, [(ref * a_lambda(x)) ** 2 for x in bb2], color=INK2, ls=":", lw=1.5,
                label=r"two-loop scaling through $\beta = 2.5$")
    ax.set_yscale("log")
    ax.set_xlabel(r"$\beta = 4/g^2$")
    ax.set_ylabel(r"$\sigma a^2$")
    ax.set_title("SU(2): string tension in lattice units", fontsize=10, loc="left")
    ax.legend(loc="lower left")
    fig.tight_layout(); fig.savefig(os.path.join(FIG, "fig1_su2_sigma.png"), dpi=150); plt.close(fig)
    # figure 2: sqrt(sigma)/Lambda_L, with the analysis variants at beta >= 2.4
    fig, ax = plt.subplots(figsize=(6, 4.2))
    sel = (b >= 2.1) & (b <= 2.31)
    r2 = np.array([pot[f"{x:.2f}"]["sqrt_sigma_over_Lambda"] for x in b])
    dr2 = np.array([pot[f"{x:.2f}"]["d_sqrt_sigma_over_Lambda"] for x in b])
    ax.errorbar(b[sel], r2[sel], dr2[sel], fmt="o", color=C1, ms=6, capsize=2, lw=1.2, mec=SURF, mew=1, label="A: $e$ free, $T^*$")
    if VARIANTS:
        for key, mk, col, lab, dx in (("A", "o", C1, None, 0.0), ("B", "s", C2, r"B: $e = \pi/12$", -0.012),
                                      ("C", "D", C3, "C: latest $T$", 0.012), ("D", "^", INK2, r"D: $R\sqrt{\sigma}$ = 0.4-1.4", 0.024)):
            xs, ys, es = [], [], []
            for bb_, v in VARIANTS.items():
                if key in v and v[key]:
                    xs.append(float(bb_) + dx); ys.append(v[key]["ratio"]); es.append(v[key]["dratio"])
            ax.errorbar(xs, ys, es, fmt=mk, color=col, ms=6, capsize=2, lw=1.2, mec=(SURF if key == "A" else col),
                        mew=(1 if key == "A" else 1.5), mfc=(col if key == "A" else SURF), label=lab)
    ax.set_xlabel(r"$\beta$")
    ax.set_ylabel(r"$\sqrt{\sigma}/\Lambda_L$ (two loops)")
    ax.set_ylim(0, 80)
    ax.set_title("Asymptotic scaling test", fontsize=10, loc="left")
    ax.legend(loc="lower left", fontsize=9)
    fig.tight_layout(); fig.savefig(os.path.join(FIG, "fig2_su2_scaling.png"), dpi=150); plt.close(fig)
    # figure 3: plaquette cycle and specific heat
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    ax = axes[0]
    if cyc:
        for dirn, col, mk in (("up", C1, "^"), ("down", C2, "v")):
            rows = [r for r in cyc["rows"] if r["direction"] == dirn]
            ax.errorbar([r["beta"] for r in rows], [r["plaquette"] for r in rows], [r["err"] for r in rows],
                        fmt=mk + "-", color=col, ms=6, lw=1.2, mec=SURF, mew=1, label=f"{'increasing' if dirn=='up' else 'decreasing'} $\\beta$")
        bb = np.linspace(1.4, 2.1, 50)
        uu = iv(2, bb) / iv(1, bb)
        ax.plot(bb, uu + 4 * uu ** 5, color=INK2, ls="--", lw=1.5, label=r"$u + 4u^5$")
        bb = np.linspace(2.3, 3.1, 50)
        ax.plot(bb, 1 - 3 / (4 * bb), color=INK2, ls=":", lw=1.5, label=r"$1 - 3/4\beta$")
        ax.set_xlabel(r"$\beta$"); ax.set_ylabel(r"$\langle \mathrm{Tr}\,U_P/2\rangle$")
        ax.set_title(r"SU(2), $8^4$: a thermal cycle", fontsize=10, loc="left")
        ax.legend(loc="upper left")
    ax = axes[1]
    if heat:
        bh = [r["beta"] for r in heat["runs"]]
        C, dC = [], []
        for r in heat["runs"]:
            p = np.array(r["plaq"])
            nb = 20
            blk = p[: len(p) // nb * nb].reshape(nb, -1)
            c = 6 * 8 ** 4 * p.var()
            js = []
            for i in range(nb):
                q = np.delete(blk, i, axis=0).ravel()
                js.append(6 * 8 ** 4 * q.var())
            C.append(c); dC.append(math.sqrt((nb - 1) * np.var(js)))
        ax.errorbar(bh, C, dC, fmt="o-", color=C1, ms=6, capsize=2, lw=1.2, mec=SURF, mew=1)
        ax.set_xlabel(r"$\beta$"); ax.set_ylabel(r"$6V(\langle P^2\rangle - \langle P\rangle^2)$")
        ax.set_title(r"Plaquette fluctuations, $8^4$", fontsize=10, loc="left")
        heat["C"] = C; heat["dC"] = dC
    fig.tight_layout(); fig.savefig(os.path.join(FIG, "fig3_su2_phase.png"), dpi=150); plt.close(fig)


def main():
    runs = load()
    pot = potential_section(runs)
    var = scaling_variants(runs, pot)
    VARIANTS.update(var)
    fvr = fv_section(runs)
    p = os.path.join(RES, "su2_cycle.json"); cyc = json.load(open(p)) if os.path.exists(p) else None
    p = os.path.join(RES, "su2_heat.json"); heat = json.load(open(p)) if os.path.exists(p) else None
    figures(pot, cyc, heat)
    if cyc:
        print("\nThermal cycle, 8^4 (up / down):")
        ups = {r["beta"]: r for r in cyc["rows"] if r["direction"] == "up"}
        dns = {r["beta"]: r for r in cyc["rows"] if r["direction"] == "down"}
        for bta in sorted(ups):
            print(f"   beta {bta:.1f}: {ups[bta]['plaquette']:.4f}({ups[bta]['err']:.4f})  {dns[bta]['plaquette']:.4f}({dns[bta]['err']:.4f})  diff {(ups[bta]['plaquette']-dns[bta]['plaquette'])/math.hypot(ups[bta]['err'], dns[bta]['err']):+.1f} sigma")
    if heat:
        print("\nSpecific heat 6V var(P), 8^4:")
        for r, c, dc in zip(heat["runs"], heat["C"], heat["dC"]):
            print(f"   beta {r['beta']:.1f}: {c:.3f}({dc:.3f})  plaquette {np.mean(r['plaq']):.5f}")
    # budget
    rows = [(f"Wilson loops, beta = {b}", runs[b]["flop"]) for b in sorted(runs)]
    if cyc: rows.append(("thermal cycle", cyc["flop"]))
    if heat: rows.append(("plaquette fluctuations", sum(r["flop"] for r in heat["runs"])))
    for k, v in fvr.items():
        rows.append((f"referee check {k}", v["flop"]))
    rows.append(("program checks (checks78.py)", 1.0e9))
    io = 0.10 * sum(runs[b]["flop"] for b in runs if runs[b]["L"] == 16)
    rows.append(("disk traffic of the 16^4 runs (10%)", io))
    tot = sum(f for _, f in rows)
    print("\nBudget (CDC 7600, 100 h at 3.3 Mflop/s = %.2e):" % CAP)
    for n, f in rows:
        print(f"   {n:28s} {f:.2e} ({100*f/CAP:5.1f} %)")
    print(f"   {'total':28s} {tot:.2e} ({100*tot/CAP:5.1f} %) = {tot/3.3e6/3600:.0f} h")
    json.dump({"potential": pot, "variants": var, "finite_volume": fvr, "budget": {"rows": rows, "total": tot, "cap": CAP}},
              open(os.path.join(RES, "summary78.json"), "w"), indent=1, default=float)


if __name__ == "__main__":
    main()
