#!/usr/bin/env python3
"""Chew-Frautschi fits to the 1974 tables.

For each trajectory, fit m^2 = c + d J by weighted least squares (errors
on m^2 from the mass errors), report alpha' = 1/d and alpha(0) = -c/d,
pool the slopes of the firm natural-parity trajectories, and derive the
string tension and the quantities that follow from it (ideas 001, 009,
016). Pure Python.
"""
import csv
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data", "regge_1974.tsv")
HBARC = 0.19733  # GeV fm


def load():
    with open(DATA, newline="") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    for r in rows:
        for k in ("J", "L", "mass", "dmass", "width"):
            r[k] = float(r[k])
        r["pool"] = r["pool"] == "1"
    return rows


def wls(xs, ys, dys):
    """Weighted least squares y = c + d x. Returns c, d, dc, dd."""
    w = [1.0 / dy**2 for dy in dys]
    S = sum(w); Sx = sum(wi * x for wi, x in zip(w, xs)); Sy = sum(wi * y for wi, y in zip(w, ys))
    Sxx = sum(wi * x * x for wi, x in zip(w, xs)); Sxy = sum(wi * x * y for wi, x, y in zip(w, xs, ys))
    Delta = S * Sxx - Sx**2
    d = (S * Sxy - Sx * Sy) / Delta
    c = (Sxx * Sy - Sx * Sxy) / Delta
    return c, d, math.sqrt(Sxx / Delta), math.sqrt(S / Delta)


def fit_trajectory(points):
    xs = [p["J"] for p in points]
    ys = [p["mass"] ** 2 for p in points]
    dys = [max(2 * p["mass"] * p["dmass"], 1e-4) for p in points]
    c, d, dc, dd = wls(xs, ys, dys)
    ap = 1.0 / d
    dap = dd / d**2
    a0 = -c / d
    da0 = math.sqrt((dc / d) ** 2 + (c * dd / d**2) ** 2)
    return ap, dap, a0, da0


def main():
    rows = load()
    trajs = []
    for t in dict.fromkeys(r["trajectory"] for r in rows):
        firm = [r for r in rows if r["trajectory"] == t and r["status"] == "firm"]
        allp = [r for r in rows if r["trajectory"] == t]
        trajs.append((t, firm, allp))

    print("Chew-Frautschi fits, m^2 = c + d J   (alpha' = 1/d, alpha(0) = -c/d)\n")
    print(f"{'trajectory':10s} {'pts':>3s} {'alpha\' [GeV^-2]':>18s} {'alpha(0)':>16s}   {'with tentative states':>24s}")
    pooled = []
    for t, firm, allp in trajs:
        if len(firm) < 2:
            continue
        ap, dap, a0, da0 = fit_trajectory(firm)
        extra = ""
        if len(allp) > len(firm):
            ap2, dap2, a0b, da0b = fit_trajectory(allp)
            extra = f"{ap2:6.3f} +/- {dap2:5.3f}, a0 = {a0b:5.2f}"
        print(f"{t:10s} {len(firm):3d} {ap:9.3f} +/- {dap:5.3f} {a0:9.3f} +/- {da0:5.3f}   {extra:>24s}")
        if all(p["pool"] for p in firm):
            pooled.append((ap, dap, t))

    # Pooled slope: inverse-variance weighted mean, plus the plain scatter.
    w = [1 / dap**2 for ap, dap, _ in pooled]
    ap_bar = sum(wi * ap for wi, (ap, _, _) in zip(w, pooled)) / sum(w)
    dap_bar = 1 / math.sqrt(sum(w))
    scatter = math.sqrt(sum((ap - ap_bar) ** 2 for ap, _, _ in pooled) / (len(pooled) - 1))
    print(f"\nPooled slope over {len(pooled)} trajectories ({', '.join(t for *_, t in pooled)}):")
    print(f"  alpha' = {ap_bar:.3f} +/- {dap_bar:.3f} (statistical)  scatter between trajectories = {scatter:.3f} GeV^-2")
    spread = max(ap for ap, _, _ in pooled) / min(ap for ap, _, _ in pooled)
    print(f"  max/min slope ratio = {spread:.2f}   (P06 asks for equality within 10-20 percent)")

    sigma = 1 / (2 * math.pi * ap_bar)
    rs = math.sqrt(sigma)
    print("\nDerived from the pooled slope (idea 009):")
    print(f"  sigma = 1/(2 pi alpha') = {sigma:.4f} GeV^2 = {sigma / HBARC:.3f} GeV/fm;  sqrt(sigma) = {rs * 1000:.0f} MeV")
    print(f"  Hagedorn temperature, d = 4: T_H = sqrt(3 sigma/(2 pi)) = {math.sqrt(3 * sigma / (2 * math.pi)) * 1000:.0f} MeV"
          f"   (Hagedorn 1965 from the spectrum: ~160 MeV; pure-gauge T_c from memory: ~0.64 sqrt(sigma) = {0.64 * rs * 1000:.0f} MeV)")
    print(f"  Hagedorn temperature, d = 3: T_H = sqrt(3 sigma/pi)     = {math.sqrt(3 * sigma / math.pi) * 1000:.0f} MeV (same sigma; for lattice comparisons only)")
    print(f"  Luscher term at R = 1 fm, d = 4: -pi/(12 R) = {-math.pi / 12 * HBARC * 1000:.1f} MeV")
    rc = math.sqrt(math.pi * 2 / (12 * sigma))
    print(f"  short-string limit R_c = sqrt(pi (d-2)/(12 sigma)) = {rc:.2f} GeV^-1 = {rc * HBARC:.2f} fm")
    print(f"  Cornell comparison (memory, 1975): sigma = 1/a^2 with a = 2.34 GeV^-1 gives {1 / 2.34**2:.4f} GeV^2")

    print("\nMeson-baryon pairing (idea 016): baryon with orbital L against mesons with orbital L+1")
    mes = [r for r in rows if r["sector"] == "meson"]
    for b in [r for r in rows if r["sector"] == "baryon"]:
        partners = [m for m in mes if m["L"] == b["L"] + 1]
        if not partners:
            continue
        print(f"  {b['name_1974']:20s} L={int(b['L'])} m={b['mass']:.3f}")
        for m in sorted(partners, key=lambda m: abs(m["mass"] - b["mass"])):
            flag = "" if m["status"] == "firm" else " (tentative)"
            print(f"      {m['name_1974']:12s} L={int(m['L'])} m={m['mass']:.3f}   dm = {1000 * (m['mass'] - b['mass']):+5.0f} MeV{flag}")


if __name__ == "__main__":
    main()
