#!/usr/bin/env python3
"""Section 7 of the 1978 paper: the four 1976 charmonium potentials applied
to the upsilon family, and a joint fit to both families.

(1) Each 1976 fit (a, b, a', a'') is used unchanged; only m_b is fitted, to the
    1S level at 9.46 GeV. For a' and a'' the upsilon levels are treated like
    the psi levels: the observed S states are spin triplets, lying
    f * kappa |R(0)|^2 / (6 m^2) above the spin averages (f = 0.5, 1).
(2) A joint fit of kappa, sigma, m_c and m_b to psi, psi', Upsilon, Upsilon'
    (spin averages, no spin-dependent terms); the chi_c centre is then a test.
(3) The open-bottom threshold from the charmed mesons, without and with the
    D* - D splitting (scaled by m_c/m_b).
Writes ../results/bottomonium78.json."""
import json, math, os, sys
from scipy.optimize import brentq, least_squares
HERE = os.path.dirname(os.path.abspath(__file__))
C76 = os.path.join(HERE, "..", "..", "1976-flux-tube-casimir")
sys.path.insert(0, os.path.join(C76, "code"))
from charmonium76 import spectrum, levels, s_wave_with_origin, hyperfine_triplet_shift   # the 1976 solver

M_D, M_DSTAR = 1.865, 2.008          # charmed mesons, 1976-77
DATA78 = {"1S": 9.46, "2S": 10.02, "3S": 10.40}
PSI = {"1S": 3.098, "2S": 3.684}
CHI_CENTRE = 3.522
PSI3770 = 3.772


def thresholds(mb, mc):
    naive = 2 * (mb + M_D - mc)
    mbar_d = (M_D + 3 * M_DSTAR) / 4
    split_b = (M_DSTAR - M_D) * mc / mb
    with_star = 2 * (mb + mbar_d - mc - 0.75 * split_b)
    return naive, with_star


def main():
    c76 = json.load(open(os.path.join(C76, "results", "charmonium76.json")))
    fits = {"a": c76["fit_a"], "b": dict(c76["fit_b"], sigma=c76["sigma_regge"]),
            "a'": dict(c76["fit_a_hyperfine"]["0.5"], frac=0.5), "a''": dict(c76["fit_a_hyperfine"]["1.0"], frac=1.0)}
    out = {"data_1978": DATA78, "fits": {}}
    print("(1) the 1976 potentials, m_b fitted to the 1S level")
    for tag, f in fits.items():
        kappa, sigma, mc = f["kappa"], f["sigma"], f["mc"]
        frac = f.get("frac", 0.0)
        def shift(mb):
            if frac == 0:
                return [0.0, 0.0]
            _, R0 = s_wave_with_origin(kappa, sigma, mb, 2)
            return (frac * hyperfine_triplet_shift(kappa, mb, R0)).tolist()
        mb = brentq(lambda m: spectrum(kappa, sigma, m)["1S"] + shift(m)[0] - DATA78["1S"], 3.5, 6.5)
        lv = spectrum(kappa, sigma, mb)
        sh = shift(mb)
        s4 = 2 * mb + levels(kappa, sigma, mb, 0, 4)[3]
        up2 = lv["2S"] + sh[1]
        thr = thresholds(mb, mc)
        out["fits"][tag] = {"kappa": kappa, "sigma": sigma, "mc": mc, "mb": mb, "levels": lv, "4S": s4,
                            "Upsilon2S": up2, "splitting": up2 - DATA78["1S"], "threshold_naive": thr[0], "threshold_Dstar": thr[1]}
        print(f"   ({tag:3s}) kappa {kappa:.3f} sigma {sigma:.4f}: m_b = {mb:.3f}; Upsilon' - Upsilon = {up2 - DATA78['1S']:.3f} (data 0.56);"
              f" 3S {lv['3S']:.3f}, 1P {lv['1P']:.3f}, 1D {lv['1D']:.3f}, 4S {s4:.3f}; threshold {thr[0]:.3f} / with D* {thr[1]:.3f}")

    print("(2) joint fit to psi, psi', Upsilon, Upsilon'")
    def res(p):
        k, s, mc, mb = p
        Mc, Mb = spectrum(k, s, mc), spectrum(k, s, mb)
        return [Mc["1S"] - PSI["1S"], Mc["2S"] - PSI["2S"], Mb["1S"] - DATA78["1S"], Mb["2S"] - DATA78["2S"]]
    r = least_squares(res, [0.5, 0.17, 1.4, 4.8], bounds=([0.05, 0.02, 0.8, 3.5], [1.5, 0.6, 2.5, 6.5]), xtol=1e-12, ftol=1e-12)
    k, s, mc, mb = r.x
    Mc, Mb = spectrum(k, s, mc), spectrum(k, s, mb)
    s4 = 2 * mb + levels(k, s, mb, 0, 4)[3]
    thr = thresholds(mb, mc)
    sigma_regge = c76["sigma_regge"]
    print(f"   kappa {k:.3f}, sigma {s:.4f} GeV^2 ({s / sigma_regge:.2f} of Regge), m_c {mc:.3f}, m_b {mb:.3f}")
    print(f"   chi_c centre {Mc['1P']:.3f} (data {CHI_CENTRE:.3f}); charmonium 1D {Mc['1D']:.3f}")
    print(f"   bottomonium: 3S {Mb['3S']:.3f}, 1P {Mb['1P']:.3f}, 1D {Mb['1D']:.3f}, 2P {Mb['2P']:.3f}, 4S {s4:.3f}; threshold {thr[0]:.3f} / with D* {thr[1]:.3f}")
    out["joint"] = {"kappa": k, "sigma": s, "sigma_ratio": s / sigma_regge, "mc": mc, "mb": mb, "charmonium": Mc,
                    "bottomonium": Mb, "4S": s4, "threshold_naive": thr[0], "threshold_Dstar": thr[1]}
    json.dump(out, open(os.path.join(HERE, "..", "results", "bottomonium78.json"), "w"), indent=1)


if __name__ == "__main__":
    main()
