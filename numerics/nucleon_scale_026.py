#!/usr/bin/env python3
"""Idea 026 / issue #2: the 313 MeV nucleon scale against an independent tension.

Three parts, in the order fixed before the nucleon benchmark is looked at.

1. Tension. sigma = 1/(2 pi alpha') from a joint fit of the rho and omega
   leading natural-parity trajectories (J = 1..4, common slope, separate
   intercepts, ordinary least squares on M^2 with the error scaled by the
   residual scatter). Variants: each trajectory alone, rho5 added, and the
   static-potential tensions of QCDS-78/1 and of the 1975 Cornell fit.
2. Baryons with the nucleon held out. The leading N trajectory is fitted
   through N(1680) 5/2+ and N(2220) 9/2+ only, with the meson tension, an
   intercept a_B and an end mass m (quark-diquark rotating string, one
   massless end, one end of mass m that also carries the junction rest
   energy). The nucleon at J = 1/2 is then predicted. The same procedure
   predicts Delta(1232) and Lambda(1116) from their own higher members, as
   a control of the low-spin extrapolation.
3. Weak side. The benchmark H_EW = alpha(0) sqrt(M_Z^2 - M_W^2), its ratio
   to H_N = (m_p + m_n)/6, the shared-tension covariance of R_N and R_EW,
   and the deformation controls: the two-wall family and the 2/9 threshold
   derivative of ordinary QCD.

Inputs: data/trajectories_pdg.tsv (PDG database, editions 1996 and 2025);
electroweak and lepton inputs below with their sources. Pure Python.
Run: python3 numerics/nucleon_scale_026.py > numerics/nucleon_scale_026.txt
"""
import csv
import math
import os
import random

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data", "trajectories_pdg.tsv")
NMC = 4000
SEED = 26

# Electroweak and lepton inputs (GeV unless stated).
# Present: M_W, M_Z from the pdgLive evaluations archived in arivero/pdghist
# commit 60b4139, data/2026/electroweak.yaml; lepton pole masses and alpha(0)
# as in arivero/dualsm papers/paper-2-meson-mass-sum-rules/FIVE-FLAVOUR-MATCHING.md.
# Period: PDG 1996 edition values from the PDG database (pdghist data/1996/summary.yaml),
# alpha(0) from CODATA 1986.
EW = {
    "2025": dict(MW=(80.3625, 0.0077), MZ=(91.1879, 0.0020), ainv=137.035999,
                 lep=(0.00051099895, 0.1056583755, 1.77693), dtau=0.00009,
                 label="present (W, Z: PDG 2026 pdgLive; hadrons: PDG 2025 database)"),
    "1996": dict(MW=(80.3327, 0.1499), MZ=(91.187, 0.007), ainv=137.0359895,
                 lep=(0.00051099907, 0.105658389, 1.77700), dtau=0.00029,
                 label="period (PDG 1996 edition)"),
}
GF = 1.1663788e-5  # GeV^-2, for v = (sqrt2 G_F)^(-1/2) in the two-wall family only


def load(edition):
    with open(DATA, newline="") as f:
        rows = [r for r in csv.DictReader(f, delimiter="\t") if r["edition"] == edition]
    for r in rows:
        r["J"] = float(r["J"])
        r["m"] = float(r["mass_MeV"]) / 1000.0
        r["dm"] = 0.5 * (float(r["err_plus"]) + float(r["err_minus"])) / 1000.0
    return rows


def pick(rows, traj, roles):
    return [r for r in rows if r["trajectory"] == traj and r["role"] in roles]


# ---------------------------------------------------------------- linear algebra
def solve(A, b):
    n = len(b)
    M = [row[:] + [b[i]] for i, row in enumerate(A)]
    for i in range(n):
        p = max(range(i, n), key=lambda k: abs(M[k][i]))
        M[i], M[p] = M[p], M[i]
        for k in range(n):
            if k != i:
                f = M[k][i] / M[i][i]
                for j in range(i, n + 1):
                    M[k][j] -= f * M[i][j]
    return [M[i][n] / M[i][i] for i in range(n)]


def inverse(A):
    n = len(A)
    cols = [solve(A, [1.0 if i == j else 0.0 for i in range(n)]) for j in range(n)]
    return [[cols[j][i] for j in range(n)] for i in range(n)]


def ols(X, y):
    """Ordinary least squares; covariance scaled by the residual variance."""
    n, p = len(X), len(X[0])
    XtX = [[sum(X[k][i] * X[k][j] for k in range(n)) for j in range(p)] for i in range(p)]
    Xty = [sum(X[k][i] * y[k] for k in range(n)) for i in range(p)]
    beta = solve(XtX, Xty)
    res = [y[k] - sum(X[k][i] * beta[i] for i in range(p)) for k in range(n)]
    dof = n - p
    s2 = sum(r * r for r in res) / dof if dof > 0 else float("nan")
    cov = [[c * s2 for c in row] for row in inverse(XtX)]
    return beta, cov, res, dof


def tension_fit(groups):
    """M^2 = (J - a_g) / alpha' with a common slope. Returns alpha', its error, intercepts."""
    X, y = [], []
    for g, pts in enumerate(groups):
        for r in pts:
            row = [r["J"]] + [1.0 if h == g else 0.0 for h in range(len(groups))]
            X.append(row)
            y.append(r["m"] ** 2)
    beta, cov, res, dof = ols(X, y)
    d, dd = beta[0], math.sqrt(cov[0][0])
    ap = 1.0 / d
    intercepts = [-c / d for c in beta[1:]]
    return ap, dd / d**2, intercepts, max(abs(x) for x in res), dof


# ---------------------------------------------------------------- rotating string
def j_classical(E, sigma, m):
    """Classical angular momentum of a straight rotating string with one massless
    end and one end of mass m (GeV), total energy E. Returns None if E <= m."""
    if m <= 0:
        return E * E / (2 * math.pi * sigma)
    if E <= m:
        return None

    def ej(v):
        g = 1.0 / math.sqrt(1 - v * v)
        w = sigma * (1 - v * v) / (m * v)  # end force balance: sigma sqrt(1-v^2) = gamma m v omega
        e = g * m + (sigma / w) * (math.asin(v) + math.pi / 2)
        j = g * m * v * v / w + sigma / (2 * w * w) * (math.pi / 2 + math.asin(v) - v * math.sqrt(1 - v * v))
        return e, j

    lo, hi = 1e-12, 1 - 1e-15
    for _ in range(70):
        mid = 0.5 * (lo + hi)
        if ej(mid)[0] < E:
            lo = mid
        else:
            hi = mid
    return ej(0.5 * (lo + hi))[1]


def mass_at(J, a, sigma, m):
    """Mass on the trajectory J = a + J_cl(M)."""
    target = J - a
    if target <= 0:
        return float("nan")
    if m <= 0:
        return math.sqrt(2 * math.pi * sigma * target)
    lo, hi = m * (1 + 1e-12), 20.0
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        jc = j_classical(mid, sigma, m)
        if jc is None or jc < target:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def intercept(points, sigma, m):
    """Weighted intercept from held-out states; chi^2 of their agreement."""
    vals, ws = [], []
    for r in points:
        a = r["J"] - j_classical(r["m"], sigma, m)
        eps = 1e-4
        da = abs(j_classical(r["m"] + eps, sigma, m) - j_classical(r["m"] - eps, sigma, m)) / (2 * eps) * r["dm"]
        vals.append(a)
        ws.append(1 / da**2)
    abar = sum(w * a for w, a in zip(ws, vals)) / sum(ws)
    chi2 = sum(w * (a - abar) ** 2 for w, a in zip(ws, vals))
    return abar, 1 / math.sqrt(sum(ws)), chi2, vals


def predict(points, Jt, sigma, m):
    a, da, chi2, vals = intercept(points, sigma, m)
    return mass_at(Jt, a, sigma, m), a, da, chi2


def mc_predict(points, Jt, ap, dap, m, rng, n=NMC):
    """Monte Carlo over the slope (residual-scaled error) and the held-out masses.
    Samples whose trajectory does not reach Jt (possible for m > 0) are dropped."""
    out = []
    for _ in range(n):
        aps = rng.gauss(ap, dap)
        s = 1 / (2 * math.pi * aps)
        pts = [dict(J=r["J"], m=rng.gauss(r["m"], r["dm"]), dm=r["dm"]) for r in points]
        M, a, _, _ = predict(pts, Jt, s, m)
        if not math.isnan(M):
            out.append((M, M / (3 * math.sqrt(s)) if Jt == 0.5 else M / math.sqrt(s)))
    out.sort()
    q = lambda arr, f: arr[int(f * (len(arr) - 1))]
    Ms = sorted(x[0] for x in out)
    Rs = sorted(x[1] for x in out)
    return (q(Ms, 0.5), q(Ms, 0.16), q(Ms, 0.84)), (q(Rs, 0.5), q(Rs, 0.16), q(Rs, 0.84))


def two_point_solve(points, sigma):
    """Intercept and end mass through two held-out states exactly (zero dof)."""
    (r1, r2) = points
    f = lambda m: (r1["J"] - j_classical(r1["m"], sigma, m)) - (r2["J"] - j_classical(r2["m"], sigma, m))
    grid = [i * 0.005 for i in range(0, 200)]
    vals = [(m, f(m)) for m in grid if r1["m"] > m]
    for (m0, f0), (m1, f1) in zip(vals, vals[1:]):
        if f0 == 0 or f0 * f1 < 0:
            lo, hi = m0, m1
            for _ in range(100):
                mid = 0.5 * (lo + hi)
                if f(lo) * f(mid) <= 0:
                    hi = mid
                else:
                    lo = mid
            m = 0.5 * (lo + hi)
            return m, r1["J"] - j_classical(r1["m"], sigma, m)
    return None, None


# ---------------------------------------------------------------- main
def section(t):
    print("\n" + t + "\n" + "-" * len(t))


def run(edition, rng):
    rows = load(edition)
    ew = EW[edition]
    print("\n" + "=" * 78 + f"\nEdition {edition}: {ew['label']}\n" + "=" * 78)

    # 1. tension
    section("1. Tension from meson trajectories (nucleon not used)")
    rho, om = pick(rows, "rho", {"tension"}), pick(rows, "omega", {"tension"})
    rho5 = pick(rows, "rho", {"tension", "variant"})
    fits = {}
    for name, groups in [("rho+omega, J=1-4 (primary)", [rho, om]), ("rho only", [rho]),
                         ("omega only", [om]), ("rho incl. rho5 + omega", [rho5, om])]:
        ap, dap, ics, rmax, dof = tension_fit(groups)
        s = 1 / (2 * math.pi * ap)
        fits[name] = (ap, dap)
        print(f"  {name:28s} alpha' = {ap:.4f} +/- {dap:.4f} GeV^-2  sqrt(sigma) = {1000 * math.sqrt(s):6.1f}"
              f" +/- {1000 * 0.5 * math.sqrt(s) * dap / ap:4.1f} MeV  intercepts {', '.join(f'{x:.3f}' for x in ics)}"
              f"  max |res| = {rmax:.3f} GeV^2 (dof {dof})")
    ap, dap = fits["rho+omega, J=1-4 (primary)"]
    sigma = 1 / (2 * math.pi * ap)
    rs = math.sqrt(sigma)
    drs = 0.5 * rs * dap / ap
    statics = [("static potential, QCDS-78/1 joint fit", 0.168), ("static potential, Cornell 1975 (memory)", 0.183)]
    for name, s in statics:
        print(f"  {name:40s} sigma = {s:.3f} GeV^2, sqrt(sigma) = {1000 * math.sqrt(s):.1f} MeV")

    # 2. baryons, nucleon held out
    section("2. Baryon trajectories with the low-spin member held out")
    N = pick(rows, "N", {"heldout"})
    Nv = pick(rows, "N", {"heldout", "variant"})
    D = pick(rows, "Delta", {"heldout"})
    L = pick(rows, "Lambda", {"heldout"})
    mN_obs = sum(r["m"] for r in pick(rows, "N", {"benchmark"})) / 2
    mD_obs = pick(rows, "Delta", {"control"})[0]["m"]
    mL_obs = pick(rows, "Lambda", {"control"})[0]["m"]
    print(f"  held-out N states: {', '.join(r['state'] for r in N)};  benchmark (m_p+m_n)/2 = {1000 * mN_obs:.4f} MeV")
    print("  primary tension; end mass m carries the diquark and junction rest energy\n")
    print(f"  {'m [GeV]':>7s} | {'a_N':>7s} {'chi2':>5s} {'M_N pred':>9s} {'R_N pred':>8s} {'pred/obs':>8s} |"
          f" {'Delta(1232) pred/obs':>20s} | {'Lambda pred/obs':>15s}")
    for m in [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6]:
        MN, aN, daN, chiN = predict(N, 0.5, sigma, m)
        MD, aD, _, _ = predict(D, 1.5, sigma, m)
        ML, aL, _, _ = predict(L, 0.5, sigma, m)
        print(f"  {m:7.2f} | {aN:7.3f} {chiN:5.2f} {1000 * MN:9.1f} {MN / (3 * rs):8.4f} {MN / mN_obs:8.4f} |"
              f" {1000 * MD:8.1f} {MD / mD_obs:11.4f} | {1000 * ML:6.1f} {ML / mL_obs:8.4f}")

    section("2a. Uncertainty (Monte Carlo over slope and held-out masses), median and 68% interval")
    for m in [0.0, 0.3]:
        (Mq, Rq) = mc_predict(N, 0.5, ap, dap, m, rng)
        print(f"  m = {m:.1f} GeV: M_N = {1000 * Mq[0]:.0f} ({1000 * Mq[1]:.0f}-{1000 * Mq[2]:.0f}) MeV,"
              f"  R_N = M_N/(3 sqrt(sigma)) = {Rq[0]:.3f} ({Rq[1]:.3f}-{Rq[2]:.3f})")
    if len(Nv) > len(N):
        MN, aN, _, chiN = predict(Nv, 0.5, sigma, 0.0)
        print(f"  variant with {Nv[-1]['state']} (error assumed): m = 0: a_N = {aN:.3f}, chi2 = {chiN:.2f},"
              f" M_N = {1000 * MN:.0f} MeV, R_N = {MN / (3 * rs):.3f}")
    for name, (apv, _) in fits.items():
        sv = 1 / (2 * math.pi * apv)
        MN, aN, _, _ = predict(N, 0.5, sv, 0.0)
        print(f"  tension variant {name}: m = 0: a_N = {aN:.3f}, M_N = {1000 * MN:.0f} MeV,"
              f" R_N = {MN / (3 * math.sqrt(sv)):.3f}, pred/obs = {MN / mN_obs:.3f}")
    for name, s in statics:
        MN, aN, _, _ = predict(N, 0.5, s, 0.0)
        print(f"  {name}: m = 0: a_N = {aN:.3f}, M_N = {1000 * MN:.0f} MeV, R_N = {MN / (3 * math.sqrt(s)):.3f},"
              f" pred/obs = {MN / mN_obs:.3f}")
    # free slope from the two held-out states
    (r1, r2) = N
    apN = (r2["J"] - r1["J"]) / (r2["m"] ** 2 - r1["m"] ** 2)
    aNf = r1["J"] - apN * r1["m"] ** 2
    MNf = math.sqrt((0.5 - aNf) / apN)
    print(f"  free slope through the two held-out N states: alpha'_N = {apN:.3f} GeV^-2, a_N = {aNf:.3f},"
          f" M_N = {1000 * MNf:.0f} MeV (pred/obs {MNf / mN_obs:.3f})")
    m2, a2 = two_point_solve(N, sigma)
    if m2 is not None:
        MN2 = mass_at(0.5, a2, sigma, m2)
        print(f"  intercept and end mass both through the two N states (zero dof): m = {m2:.3f} GeV, a_N = {a2:.3f},"
              f" M_N = {1000 * MN2:.0f} MeV (pred/obs {MN2 / mN_obs:.3f})")
    else:
        print("  intercept and end mass both through the two N states: no solution with 0 <= m < 1 GeV")

    section("2b. Inverse checks (the benchmark inserted by hand)")
    a_needed = 0.5 - (3 * 0.728) ** 2 / (2 * math.pi)
    print(f"  R_N = 0.728 at J = 1/2 on a massless-end line selects a_B = 1/2 - (3 R_N)^2/(2 pi) = {a_needed:.3f}")
    a_obs = 0.5 - mN_obs**2 * ap
    print(f"  the observed nucleon on the primary slope selects a_B = {a_obs:.3f};"
          f" the held-out fit gives a_N = {intercept(N, sigma, 0.0)[0]:.3f} +/- {intercept(N, sigma, 0.0)[1]:.3f}")

    # 3. weak side
    section("3. Electroweak benchmark, shared tension, held-out lepton sum")
    (MW, dMW), (MZ, dMZ) = ew["MW"], ew["MZ"]
    B2 = MZ**2 - MW**2
    B = math.sqrt(B2)
    dB_rel = 0.5 * math.sqrt((2 * MW * dMW) ** 2 + (2 * MZ * dMZ) ** 2) / B2
    HEW = B / ew["ainv"]
    HN = mN_obs / 3
    Hl = sum(ew["lep"]) / 6
    RN, REW = HN / rs, HEW / rs
    t = 0.5 * dap / ap  # fractional error of sqrt(sigma)
    print(f"  H_N  = (m_p+m_n)/6           = {1000 * HN:.4f} MeV")
    print(f"  H_EW = alpha(0) sqrt(MZ^2-MW^2) = {1000 * HEW:.4f} +/- {1000 * HEW * dB_rel:.4f} MeV  (fractional {dB_rel:.6f})")
    print(f"  H_EW/H_N = {HEW / HN:.6f} +/- {HEW / HN * dB_rel:.6f};  R_N/R_EW = {HN / HEW:.6f} +/- {HN / HEW * dB_rel:.6f}")
    print(f"  with the primary tension, sqrt(sigma) = {1000 * rs:.1f} +/- {1000 * drs:.1f} MeV (fractional {t:.4f}):")
    print(f"    R_N  = {RN:.4f} +/- {RN * t:.4f}")
    print(f"    R_EW = {REW:.4f} +/- {REW * math.hypot(t, dB_rel):.4f}")
    cov = RN * REW * t * t
    corr = cov / (RN * t * REW * math.hypot(t, dB_rel))
    print(f"    cov(R_N, R_EW) = {cov:.3e}, correlation {corr:.5f}; the quotient carries none of it")
    print(f"  held out, not used above: H_l = (m_e+m_mu+m_tau)/6 = {1000 * Hl:.4f} MeV, R_l = {Hl / rs:.4f},"
          f" H_l/H_EW = {Hl / HEW:.6f}")

    if edition == "2025":
        section("3a. Deformation controls on the weak side (tension held fixed)")
        v = (math.sqrt(2) * GF) ** -0.5
        gp = 2 * B / v
        print(f"  tree-level on-shell: sqrt(MZ^2-MW^2) = g' v/2 with v = (sqrt2 G_F)^(-1/2) = {v:.4f} GeV, so g' = {gp:.4f}")
        print(f"  R_EW = [alpha(0) g'/2] (v/sqrt(sigma)) = {1 / ew['ainv'] * gp / 2:.6f} x {v / rs:.1f}")
        print("  two-wall family: sqrt(sigma) ~ M e^(-k y1), v ~ M e^(-k y2): d ln R_EW / d(k (y2 - y1)) = -1;")
        print("    any R_EW is reached by moving one wall; the string data must fix k (y2 - y1), g' at the wall")
        print("    and the running of the photon coupling to the Thomson limit.")
        print("  threshold control (second line, FLAVOUR_AND_SCALES.md section 4): at fixed Lambda_6,")
        print("    d ln Lambda_3 / d ln v = 2/9; with sqrt(sigma) ~ Lambda_3 and alpha(0), g' fixed,")
        print("    d ln R_EW / d ln v = 7/9, d ln R_N / d ln v = 0, d ln(R_N/R_EW) / d ln v = -7/9.")
        print(f"    holding R_N/R_EW to its measured fractional error {dB_rel:.6f} needs v/Lambda_6 fixed to"
              f" {dB_rel * 9 / 7:.6f}: ordinary QCD supplies no such relation.")


def main():
    rng = random.Random(SEED)
    print(__doc__.split("\n\n")[0])
    for ed in ("2025", "1996"):
        run(ed, rng)


if __name__ == "__main__":
    main()
