#!/usr/bin/env python3
"""Section 5: one tension. The levels of the narrow states of 1974-76 in
V(r) = -kappa/r + sigma r, with no additive constant, M = 2 m_c + E.

(a) sigma, kappa and m_c fitted to three levels: psi(3.098), psi'(3.684)
    and the spin-weighted centre of the three chi states (3.413, 3.508,
    3.553, with J = 0, 1, 2 assumed). The fitted sigma is compared with
    the Regge value 1/(2 pi alpha'), alpha' = 0.865 GeV^-2.
(b) sigma fixed at the Regge value, kappa and m_c fitted to psi and psi'.
    The 1P centre, 1D, 2P and 3S levels are then predictions.
Radial equation by finite differences (scipy eigh_tridiagonal).
Writes ../results/charmonium76.json."""
import json, math, os
import numpy as np
from scipy.linalg import eigh_tridiagonal
from scipy.optimize import least_squares, brentq

HBARC = 0.19733
ALPHAP = 0.865                      # GeV^-2, pooled Regge slope (numerics/regge_fit.py)
SIGMA_REGGE = 1 / (2 * math.pi * ALPHAP)
DATA = {"1S": 3.098, "2S": 3.684}
CHI = [(3.413, 0), (3.508, 1), (3.553, 2)]
DATA["1P"] = sum(m * (2 * J + 1) for m, J in CHI) / sum(2 * J + 1 for _, J in CHI)


def levels(kappa, sigma, mc, l, n, N=6000, rmax=24.0):
    h = rmax / (N + 1)
    r = h * np.arange(1, N + 1)
    mu = mc / 2
    diag = 1 / (mu * h * h) - kappa / r + sigma * r + l * (l + 1) / (2 * mu * r * r)
    off = -np.ones(N - 1) / (2 * mu * h * h)
    return eigh_tridiagonal(diag, off, select="i", select_range=(0, n - 1), eigvals_only=True)


def s_wave_with_origin(kappa, sigma, mc, n, N=6000, rmax=24.0):
    """S-wave energies and |R_nS(0)|^2 (GeV^3) from the finite-difference eigenvectors."""
    h = rmax / (N + 1)
    r = h * np.arange(1, N + 1)
    mu = mc / 2
    diag = 1 / (mu * h * h) - kappa / r + sigma * r
    off = -np.ones(N - 1) / (2 * mu * h * h)
    E, vec = eigh_tridiagonal(diag, off, select="i", select_range=(0, n - 1))
    R0sq = vec[0, :] ** 2 / h ** 3            # u_1 = v_1/sqrt(h), R(0) = u_1/r_1
    return E, R0sq


def hyperfine_triplet_shift(kappa, mc, R0sq):
    """First-order shift of the spin triplet above the spin average for
    vector exchange with Coulomb strength kappa: kappa |R(0)|^2 / (6 m^2)."""
    return kappa * R0sq / (6 * mc * mc)


def spectrum(kappa, sigma, mc):
    s = levels(kappa, sigma, mc, 0, 3)
    p = levels(kappa, sigma, mc, 1, 2)
    d = levels(kappa, sigma, mc, 2, 1)
    E = {"1S": s[0], "2S": s[1], "3S": s[2], "1P": p[0], "2P": p[1], "1D": d[0]}
    return {k: 2 * mc + v for k, v in E.items()}


def main():
    out = {"data": DATA, "sigma_regge": SIGMA_REGGE}
    # solver check only: the 1974 shooting code (numerics/charmonium.py) with its
    # default inputs (kappa = 0.52 of Eichten et al. 1975, alpha' = 0.88, 1S at 3.097)
    sig88 = 1 / (2 * math.pi * 0.88)
    mc = brentq(lambda m: spectrum(0.52, sig88, m)["1S"] - 3.097, 1.0, 2.5)
    chk = spectrum(0.52, sig88, mc)
    print(f"check (1974 inputs): m_c = {mc:.3f}, 2S = {chk['2S']:.3f}, 1P = {chk['1P']:.3f}  [1974 shooting: 1.368, 3.712, 3.528]")
    out["check_1974"] = {"mc": mc, **chk}

    # (a) three-parameter fit
    def res3(p):
        k, s, m = p
        M = spectrum(k, s, m)
        return [M["1S"] - DATA["1S"], M["2S"] - DATA["2S"], M["1P"] - DATA["1P"]]
    fa = least_squares(res3, [0.5, 0.18, 1.4], bounds=([0.05, 0.02, 0.8], [1.5, 0.6, 2.5]), xtol=1e-12, ftol=1e-12)
    k, s, m = fa.x
    Ma = spectrum(k, s, m)
    # sensitivity of sigma to the chi centre: +/- 10 MeV
    sens = []
    for dm in (-0.010, 0.010):
        def r3(p, dm=dm):
            kk, ss, mm = p
            M = spectrum(kk, ss, mm)
            return [M["1S"] - DATA["1S"], M["2S"] - DATA["2S"], M["1P"] - (DATA["1P"] + dm)]
        sens.append(least_squares(r3, fa.x, xtol=1e-12, ftol=1e-12).x[1])
    print(f"(a) fit to 1S, 2S, 1P centre {DATA['1P']:.4f}: kappa = {k:.3f}, sigma = {s:.4f} GeV^2, m_c = {m:.3f} GeV")
    print(f"    sigma(charmonium)/sigma(Regge) = {s/SIGMA_REGGE:.3f};  1P centre moved by -/+10 MeV gives sigma = {sens[0]:.4f}, {sens[1]:.4f}")
    out["fit_a"] = {"kappa": k, "sigma": s, "mc": m, "levels": Ma, "sigma_ratio": s / SIGMA_REGGE,
                    "sigma_if_1P_minus10": sens[0], "sigma_if_1P_plus10": sens[1]}

    # (a') the S-wave data are spin triplets; with the potential's own first-order
    # spin-spin term the spin averages lie lower by kappa |R(0)|^2/(6 m^2), times f
    out["fit_a_hyperfine"] = {}
    for frac in (0.5, 1.0):
        def res3h(p, frac=frac):
            k, s_, m = p
            M = spectrum(k, s_, m)
            _, R0 = s_wave_with_origin(k, s_, m, 2)
            sh = frac * hyperfine_triplet_shift(k, m, R0)
            return [M["1S"] + sh[0] - DATA["1S"], M["2S"] + sh[1] - DATA["2S"], M["1P"] - DATA["1P"]]
        fh = least_squares(res3h, fa.x, bounds=([0.05, 0.02, 0.8], [1.5, 0.6, 2.5]), xtol=1e-12, ftol=1e-12)
        kh, sh_, mh = fh.x
        _, R0 = s_wave_with_origin(kh, sh_, mh, 2)
        shifts = frac * hyperfine_triplet_shift(kh, mh, R0)
        Mh = spectrum(kh, sh_, mh)
        print(f"(a') with {frac:.1f} x first-order spin-spin: kappa = {kh:.3f}, sigma = {sh_:.4f} ({sh_/SIGMA_REGGE:.2f} of Regge), m_c = {mh:.3f};"
              f" triplet shifts {1000*shifts[0]:.0f}, {1000*shifts[1]:.0f} MeV; 1D = {Mh['1D']:.3f}")
        out["fit_a_hyperfine"][str(frac)] = {"kappa": kh, "sigma": sh_, "mc": mh, "shift_1S": shifts[0], "shift_2S": shifts[1],
                                              "sigma_ratio": sh_ / SIGMA_REGGE, "levels": Mh}
    _, R0a = s_wave_with_origin(k, s, m, 2)
    sha = hyperfine_triplet_shift(k, m, R0a)
    print(f"    at the fit (a) parameters the first-order triplet shifts are {1000*sha[0]:.0f} and {1000*sha[1]:.0f} MeV")
    out["fit_a"]["first_order_triplet_shifts"] = sha.tolist()

    # (b) Regge sigma, two-parameter fit
    def res2(p):
        kk, mm = p
        M = spectrum(kk, SIGMA_REGGE, mm)
        return [M["1S"] - DATA["1S"], M["2S"] - DATA["2S"]]
    fb = least_squares(res2, [0.5, 1.4], bounds=([0.05, 0.8], [1.5, 2.5]), xtol=1e-12, ftol=1e-12)
    kb, mb = fb.x
    Mb = spectrum(kb, SIGMA_REGGE, mb)
    print(f"(b) sigma = {SIGMA_REGGE:.4f} (Regge): kappa = {kb:.3f}, m_c = {mb:.3f}")
    for key in ("1S", "2S", "1P", "1D", "2P", "3S"):
        print(f"    {key}: {Mb[key]:.3f} GeV" + (f"   (data {DATA[key]:.3f})" if key in DATA else ""))
    out["fit_b"] = {"kappa": kb, "mc": mb, "levels": Mb}
    out["open_charm_threshold"] = 2 * 1.865
    json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results", "charmonium76.json"), "w"), indent=1)


if __name__ == "__main__":
    main()
