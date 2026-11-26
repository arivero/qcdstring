"""Spin-structure corollary of QCDS-95/S1 (Section 11).

Units: photon mass m_gamma = 1, e = 1, v^2 = 1/2, phi = f exp(i theta)/sqrt(2),
A_theta = a/rho. The critical (BPS) profile is the one distributed with QCDS-91/S1.

Checks printed to results/spin-structure.json:
  1. first-order (Bogomolny) residuals of the profile, the tension T = 2 pi v^2,
     and the transverse norm of the translation/Goldstino profile, T/2;
  2. the complex deformation operator D on a Cartesian grid annihilates the
     covariant translation (B, eta) = (i F12/sqrt2, D_1 phi);
  3. the neutral block -Laplacian + f^2 of D D^dagger in angular momenta 0-4:
     its lowest eigenvalue (the gap nu_0^2) and the bound states below one;
  4. closed-circle Casimir coefficients from regulated oscillator sums, from
     the conformal weights, and from the massless limit of the 1986 massive
     Dirac difference;
  5. the three-length estimator and the L -> 2L ratio on model energies with
     specified massive winding terms and a specified L^-3 remainder.
"""
import json
from math import pi, sqrt
from pathlib import Path
import sys

import numpy as np
from scipy.integrate import simpson
from scipy.linalg import eigh_tridiagonal
from scipy.special import k1

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT.parents[0] / "1991-vortex-pseudoscalar" / "code"))
from vortex import background  # noqa: E402
sys.path.insert(0, str(ROOT.parents[0] / "1992-scalar-doublet" / "code"))
from trace_spectrum import static_solution  # noqa: E402

OUTER = 30.0


def profile_checks(sol):
    r = np.linspace(1e-3, OUTER, 60001)
    f, df, a, da = sol.sol(r)
    bog1 = np.max(np.abs(df - f * (1 - a) / r))
    bog2 = np.max(np.abs(da / r - (1 - f**2) / 2))
    F = da / r
    dphi2 = 0.5 * (df**2 + f**2 * (1 - a) ** 2 / r**2)
    tension = simpson(2 * pi * r * (F**2 + dphi2), x=r)
    norm_translation = simpson(2 * pi * r * (0.5 * F**2 + 0.5 * dphi2), x=r)
    return dict(bogomolny_residual_f=float(bog1), bogomolny_residual_a=float(bog2),
                tension=float(tension), tension_over_pi=float(tension / pi),
                translation_norm_squared=float(norm_translation),
                translation_norm_over_half_tension=float(norm_translation / (tension / 2)))


def kernel_check(sol, half=10.0, h=0.025):
    """Residual of D acting on the covariant translation along x_1."""
    x = np.arange(-half, half + h / 2, h)
    X, Y = np.meshgrid(x, x, indexing="ij")
    rho = np.hypot(X, Y) + 1e-12
    f, df, a, da = sol.sol(np.clip(rho.ravel(), 1e-4, OUTER))
    f, df, a, da = (u.reshape(rho.shape) for u in (f, df, a, da))
    phi = f * (X + 1j * Y) / rho / sqrt(2)
    A1, A2 = -a * Y / rho**2, a * X / rho**2
    F12 = da / rho

    def d1(u):
        return np.gradient(u, h, axis=0)

    def d2(u):
        return np.gradient(u, h, axis=1)

    D1 = lambda u: d1(u) - 1j * A1 * u  # noqa: E731
    D2 = lambda u: d2(u) - 1j * A2 * u  # noqa: E731
    B = 1j * F12 / sqrt(2)
    eta = D1(phi)
    Xres = -1j * sqrt(2) * phi * B + D1(eta) + 1j * D2(eta)
    Zres = -1j * (d1(B) - 1j * d2(B)) + sqrt(2) * np.conj(phi) * eta
    core = (rho > 0.5) & (rho < half - 1.0)
    scale = np.max(np.abs(eta[core]))
    return dict(grid_spacing=h, max_X_over_max_eta=float(np.max(np.abs(Xres[core])) / scale),
                max_Z_over_max_eta=float(np.max(np.abs(Zres[core])) / scale),
                note="central differences; residual is O(h^2) and excludes rho < 0.5")


def neutral_block(sol, ell, outer=40.0, spacing=0.02):
    """Cell-centred -u'' - u'/r + (ell^2/r^2 + f^2) u with Dirichlet outer face."""
    n = round(outer / spacing)
    h = outer / n
    r = (np.arange(n) + 0.5) * h
    diag = 2 / h**2 + sol.sol(np.minimum(r, OUTER))[0] ** 2 + ell**2 / r**2
    diag[-1] += outer / (r[-1] * h**2)
    off = -(r[:-1] + h / 2) / (h**2 * np.sqrt(r[:-1] * r[1:]))
    vals = eigh_tridiagonal(diag, off, select="i", select_range=(0, 3), eigvals_only=True)
    return vals


def casimir_checks():
    out = {}
    # regulated oscillator sums at L = 1: S(eps) = sum_n k_n exp(-eps k_n), k_n = 2 pi (n + s)
    for s, name in [(0.0, "periodic"), (0.5, "antiperiodic")]:
        finite = []
        for eps in (2e-3, 1e-3, 5e-4):
            n = np.arange(0 if s else 1, int(60 / eps / (2 * pi)) + 2)
            k = 2 * pi * (n + s)
            S = np.sum(k * np.exp(-eps * k))
            finite.append(S - 1 / (2 * pi * eps**2))  # subtract the area divergence
        out[f"chiral_sum_finite_part_{name}"] = finite  # -> 2 pi zeta(-1, s')
    zeta_p = -1 / 12
    zeta_a = 1 / 24
    boson = 2 * 0.5 * 2 * pi * zeta_p               # real boson, both movers, +1/2 sum |k|
    maj_R = -2 * 0.5 * 2 * pi * zeta_p              # nonchiral Majorana, periodic
    maj_NS = -2 * 0.5 * 2 * pi * zeta_a             # nonchiral Majorana, antiperiodic
    out.update(boson_coefficient_over_pi=boson / pi, majorana_R_over_pi=maj_R / pi,
               majorana_NS_over_pi=maj_NS / pi,
               difference_two_majoranas_over_pi=2 * (maj_R - maj_NS) / pi)
    # conformal weights: c = 3 (two bosons, two Majoranas), R ground weights h = hbar = 1/8
    c = 3.0
    E_NS = 2 * pi * (0 - c / 12)
    E_R = 2 * pi * (2 * (1 / 8) - c / 12)
    out.update(cft_E_R_times_L_over_pi=E_R / pi, cft_E_NS_times_L_over_pi=E_NS / pi)
    # massless limit of the 1986 massive Dirac difference (4m/pi) sum_{odd w} K1(w m L)/w
    lim = {}
    for mL in (1e-1, 1e-2, 1e-3):
        w = np.arange(1, 4_000_001, 2, dtype=float)
        D = 4 * mL / pi * np.sum(k1(w * mL) / w)   # at L = 1
        lim[str(mL)] = float(2 / pi * D)
    out["massive_dirac_difference_times_2L_over_pi"] = lim
    return out


def casimir_massive(m, L, kind):
    w = np.arange(1, 400, dtype=float)
    terms = k1(w * m * L) / w
    if kind == "boson":
        return -m / pi * np.sum(terms)
    if kind == "majorana_R":
        return m / pi * np.sum(terms)
    if kind == "majorana_NS":
        return m / pi * np.sum((-1) ** w * terms)
    raise ValueError(kind)


def model_energy(L, spin, nb0, nf0, sigma, massive):
    """sigma L + c0 + massless Casimir + L^-3 square-root remainder + massive winding."""
    a = (pi / 6) * (nf0 - nb0) if spin == "R" else -(pi / 6) * nb0 - (pi / 12) * nf0
    E = sigma * L + 0.37 + a / L - a**2 / (2 * sigma * L**3)
    for m, nb, nf in massive:
        E += nb * casimir_massive(m, L, "boson")
        E += nf * casimir_massive(m, L, "majorana_R" if spin == "R" else "majorana_NS")
    return E, a


def estimator_checks(nu0):
    sigma = pi  # BPS tension in photon units at unit coupling (illustration)
    massive = [(nu0, 4, 4), (1.0, 8, 8)]  # illustrative supersymmetric counts
    rows = []
    for label, nb in [("minimal", 2), ("extra neutral scalar", 3)]:
        for L in (10.0, 20.0, 40.0):
            est = {}
            for spin in ("R", "NS"):
                E = lambda x: model_energy(x, spin, nb, 2, sigma, massive)[0]  # noqa: E731
                est[spin] = 4 * L / 3 * (2 * E(L) - 3 * E(2 * L) + E(4 * L))
            dR = (model_energy(L, "R", nb, 2, sigma, massive)[0]
                  - model_energy(L, "NS", nb, 2, sigma, massive)[0])
            d2R = (model_energy(2 * L, "R", nb, 2, sigma, massive)[0]
                   - model_energy(2 * L, "NS", nb, 2, sigma, massive)[0])
            rows.append(dict(content=label, L=L, a_R_hat_over_pi=est["R"] / pi,
                             a_NS_hat_over_pi=est["NS"] / pi,
                             difference_times_2L_over_pi=dR * 2 * L / pi,
                             ratio_2L_to_L=d2R / dR,
                             massive_dirac_difference_at_nu0=float(
                                 2 * (casimir_massive(nu0, L, "majorana_R")
                                      - casimir_massive(nu0, L, "majorana_NS")))))
    return dict(sigma=sigma, massive_content="(mass, real bosons, Majoranas): "
                + str(massive), rows=rows)


NU0 = 0.8817442  # sqrt(0.7774728), QCDS-91/S1


def profile_response(w, radius, points):
    """sup|f_w - f_0|, sup|a_w - a_0|/rho, sup|s_w| on the deformed branch of Eq. (6)."""
    r = np.exp(np.linspace(np.log(1e-4), np.log(0.999 * radius), points))
    y0 = static_solution(0.0, radius, 0.0, 1).sol(np.log(r))
    yw = static_solution(w, radius, 0.0, 1).sol(np.log(r))
    df = float(np.max(np.abs(yw[0] - y0[0])))
    da = float(np.max(np.abs(yw[2] - y0[2]) / r))
    sm = float(np.max(np.abs(yw[4])))
    return df, da, sm


def perturbation_bound():
    """||V_w|| <= max(w, sup|s|) + sup|df| + sup|da|/rho, and the largest w with bound < nu0/2."""
    rows = []
    for w in (0.01, 0.05, 0.1, 0.2, 0.3, 0.35, 0.4):
        df, da, sm = profile_response(w, 25.0, 20001)
        rows.append(dict(w=w, sup_df=df, sup_da_over_rho=da, sup_s=sm,
                         bound=max(w, sm) + df + da))
    def excess(w, radius=25.0, points=20001):
        df, da, sm = profile_response(w, radius, points)
        return max(w, sm) + df + da - NU0 / 2
    lo, hi = 0.3, 0.45
    for _ in range(30):
        mid = 0.5 * (lo + hi)
        if excess(mid) < 0:
            lo = mid
        else:
            hi = mid
    w_star = lo
    # error budget: outer radius and sampling of the supremum at w_star
    budget = dict(radius_35=excess(w_star, 35.0) + NU0 / 2, points_40001=excess(w_star, 25.0, 40001) + NU0 / 2,
                  reference=excess(w_star) + NU0 / 2)
    gap_at = {str(r["w"]): NU0 - r["bound"] for r in rows}
    return dict(nu0=NU0, half_gap=NU0 / 2, rows=rows, w_star=w_star,
                bound_at_w_star_variants=budget, lower_bound_on_fermion_gap=gap_at)


def main():
    sol = background(1.0, OUTER)
    out = {"profile": profile_checks(sol), "kernel": kernel_check(sol)}
    spectra = {}
    for ell in range(5):
        vals = neutral_block(sol, ell)
        spectra[str(ell)] = dict(lowest=float(vals[0]), below_one=[float(v) for v in vals if v < 1])
    out["neutral_block"] = spectra
    # finite-box test: a continuum level moves to one as the box grows, a bound state stays below
    box = {}
    for ell in (1, 2):
        box[str(ell)] = {str(R): float(neutral_block(sol, ell, outer=R, spacing=0.04)[0] - 1)
                         for R in (40.0, 80.0, 160.0)}
    out["neutral_block_box_scaling_lowest_minus_one"] = box
    nu0 = sqrt(spectra["0"]["lowest"])
    out["gap"] = dict(nu0=nu0, contour_radius=nu0 / 2)
    out["casimir"] = casimir_checks()
    out["estimator"] = estimator_checks(nu0)
    out["deformation"] = perturbation_bound()
    (ROOT / "results" / "spin-structure.json").write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
