"""Classical unit electric string in constant-coupling, softly broken dual SQED.

Run with Python, NumPy and SciPy. Results are printed as JSON on stdout.
The 1991 radial solver supplies the matched exterior for the longitudinal mode.
"""

from pathlib import Path
import json
import sys
import numpy as np
from scipy.integrate import simpson, solve_bvp
from scipy.optimize import brentq
from scipy.sparse import bmat, csc_matrix, diags
from scipy.sparse.linalg import eigsh, spsolve
from scipy.special import kve

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "1991-vortex-pseudoscalar" / "code"))
from vortex import INNER, background, localized, radial_matrix


def relaxed_background(w, outer, critical):
    radius = np.linspace(INNER, outer, 550)
    f, df, a, da = critical.sol(radius)
    guess = np.vstack((f, df, a, da, w * (1 - a) / 2, -w * da / 2))

    def equations(r, fields):
        f, df, a, da, s, ds = fields
        residual = f**2 - 1 + 2 * w * s
        return np.vstack((
            df, -df / r + (1 - a)**2 * f / r**2 + f * (residual / 2 + s**2),
            da, da / r - f**2 * (1 - a),
            ds, -ds / r + (f**2 + w**2) * s - w * (1 - f**2) / 2,
        ))

    def boundaries(left, right):
        return np.array((left[0] - INNER * left[1], 2 * left[2] - INNER * left[3],
                         left[5] - INNER * (w**2 * left[4] - w / 2) / 2,
                         right[0] - 1, right[2] - 1, right[4]))

    sol = solve_bvp(equations, boundaries, radius, guess, tol=2e-9, max_nodes=14000)
    if not sol.success:
        raise RuntimeError(sol.message)
    return sol


def bulk_mass(w):
    return 1 / (np.sqrt(1 + w**2 / 4) + abs(w) / 2)


def observables(w, outer, critical):
    profile = relaxed_background(w, outer, critical)
    eigenvalue, state = localized(profile, outer)
    r = np.linspace(0, outer, round(outer * 400) + 1)
    f, df, a, da, s, ds = profile.sol(np.maximum(r, INNER))
    f[0], a[0], da[0], ds[0] = 0, 0, 0, 0
    angular = np.divide((1 - a) * f, r, out=df.copy(), where=r > 0)
    magnetic = np.divide(da, r, out=np.full_like(r, da[1] / r[1]), where=r > 0)
    potential = f**2 * s**2 + (f**2 - 1 + 2 * w * s)**2 / 4

    def integral(function):
        return simpson(function, x=r)

    tau = integral(r * (df**2 + angular**2 + magnetic**2 + ds**2 + potential))
    virial_error = integral(r * (magnetic**2 - potential))
    wave = state.sol(np.maximum(r, INNER))[0]
    kappa = np.sqrt(1 - eigenvalue)
    exterior = np.linspace(outer, outer + 40 / kappa, 4001)
    tail = wave[-1] * np.exp(-kappa * (exterior - outer)) * kve(0, kappa * exterior) / kve(0, kappa * outer)
    norm = integral(r * wave**2) + simpson(exterior * tail**2, x=exterior)
    u = wave / np.sqrt(2 * np.pi * norm)
    alpha = 2 * np.pi * integral(da * u)
    current = 4 * np.pi * integral(u * df * (1 - a) * f)
    nu = np.sqrt(eigenvalue)
    if abs(virial_error) > 1e-7 or abs(current / (alpha * eigenvalue) - 1) > 1e-7:
        raise ArithmeticError("Failed the virial or magnetic/current overlap check")
    if not (0 < nu < 1 and np.min(u) > 0 and abs(integral(da) - 1) < 1e-7):
        raise ArithmeticError("Expected a normalized unit vortex and a nodeless bound mode")
    return {
        "w": w, "outer": outer, "SW_mgamma_over_Lambda": 8 * np.sqrt(2) * w, "tau": tau, "nu_squared": eigenvalue,
        "nu": nu, "lightest_bulk_mass": bulk_mass(w), "alpha": alpha,
        "g_Qodd": alpha / nu, "pole_product": alpha / np.sqrt(np.pi * tau),
        "virial_error": virial_error, "current_relative_error": current / (alpha * eigenvalue) - 1,
        "neutral_center": s[0], "first_crossing_L_mgamma": 4 * np.pi / nu,
        "first_two_state_gap_over_g_modd": alpha * nu / (np.pi * tau * np.sqrt(4 * np.pi)),
        "partial_width_over_g2_modd": alpha**2 * eigenvalue / (8 * np.pi**2 * tau**2),
        "tau_derivative": integral(r * s * (f**2 - 1 + 2 * w * s)),
        "tau_work_identity_error": w * integral(r * s * (f**2 - 1 + 2 * w * s))
        + 2 * integral(r * (ds**2 + f**2 * s**2)),
    }


def background_response(outer, critical):
    """Derivative of (f,a) with respect to w squared at zero breaking."""
    r = np.linspace(INNER, outer, 550)

    def equations(radius, fields):
        f, _, a, _ = critical.sol(radius)
        neutral = (1 - a) / 2
        h, dh, k, dk = fields
        higgs_mass = (1 - a)**2 / radius**2 + (3 * f**2 - 1) / 2
        return np.vstack((
            dh, -dh / radius + higgs_mass * h - 2 * (1 - a) * f * k / radius**2
            + f * (neutral + neutral**2),
            dk, dk / radius + f**2 * k - 2 * f * (1 - a) * h,
        ))

    def boundaries(left, right):
        return np.array((left[0] - INNER * left[1], 2 * left[2] - INNER * left[3],
                         right[0], right[2]))

    sol = solve_bvp(equations, boundaries, r, np.zeros((4, r.size)), tol=2e-9, max_nodes=12000)
    if not sol.success:
        raise RuntimeError(sol.message)
    return sol


def laplacian(r, h):
    """Axis flux is zero; the outer face is Dirichlet. The cell norm includes r."""
    diagonal = np.full_like(r, 2 / h**2)
    diagonal[-1] += (r[-1] + h / 2) / (r[-1] * h**2)
    off = -(r[:-1] + h / 2) / (h**2 * np.sqrt(r[:-1] * r[1:]))
    return diags((off, diagonal, off), (-1, 0, 1), format="csc")


def critical_slopes(outer, step, critical, response):
    """Solve the reduced resolvent with the normalized wave derivative orthogonal to the wave."""
    eigenvalue, r, u = radial_matrix(critical, outer, step)
    h = r[1] - r[0]
    f, _, a, da = critical.sol(r)
    f2, _, _, da2 = response.sol(r)
    cell_norm = np.sqrt(2 * np.pi * r * h)
    q = cell_norm * u
    potential_slope = 2 * f * f2
    lambda2 = q @ (potential_slope * q)
    matrix = laplacian(r, h) + diags(f**2 - eigenvalue)
    column = csc_matrix(q[:, None])
    bordered = bmat(((matrix, column), (column.T, None)), format="csc")
    rhs = np.r_[-(potential_slope - lambda2) * q, 0.]
    dq = spsolve(bordered, rhs)[:-1]
    if abs(q @ dq) > 1e-8:
        raise ArithmeticError("Inconsistent normalization derivative")
    alpha0 = 2 * np.pi * h * np.sum(da * u)
    alpha2 = 2 * np.pi * h * np.sum(da2 * u + da * dq / cell_norm)
    nu = np.sqrt(eigenvalue)
    return {
        "outer": outer, "spacing": h, "nu_squared_w2": lambda2,
        "nu_w2": lambda2 / (2 * nu), "alpha_w2": alpha2,
        "g_Qodd_w2": alpha2 / nu - alpha0 * lambda2 / (2 * nu**3),
        "product_w2": (alpha2 + alpha0 / 8) / np.sqrt(np.pi),
        "even_mass_squared_linear_split": q @ (f**2 * (2 - a) * q) / nu,
    }


def even_levels(w, outer, step, critical):
    """Two coupled radial shape/neutral levels in the real D-flat scalar sector."""
    profile = relaxed_background(w, outer, critical)
    cells = round(outer / step)
    h = outer / cells
    r = (np.arange(cells) + 0.5) * h
    f, _, a, _, s, _ = profile.sol(r)
    kin = laplacian(r, h)
    higgs = kin + diags((1 - a)**2 / r**2 + (3 * f**2 - 1 + 2 * w * s) / 2 + s**2)
    azimuthal = kin + diags(1 / r**2 + f**2)
    neutral = kin + diags(f**2 + w**2)
    mixing_a = diags(-2 * (1 - a) * f / r)
    mixing_s = diags(f * (w + 2 * s))
    matrix = bmat(((higgs, mixing_a, mixing_s), (mixing_a, azimuthal, None),
                   (mixing_s, None, neutral)), format="csc")
    levels = eigsh(matrix, k=2, sigma=0.77, which="LM", return_eigenvectors=False,
                   v0=np.ones(3 * cells), tol=2e-11)
    return {"w": w, "spacing": h, "nu_squared": sorted(levels.tolist())}


def main():
    outer = 36.0
    critical = background(1, outer)
    response = background_response(outer, critical)
    rows = {w: observables(w, outer, critical) for w in (0, 0.001, 0.01, 0.025, 0.05, 0.1, 0.2, 0.3)}
    slopes = [critical_slopes(outer, h, critical, response) for h in (0.04, 0.02, 0.01)]
    even = [even_levels(w, outer, 0.01, critical) for w in (0, 0.01, 0.025, 0.05)]
    outer_check = observables(0.1, 28., background(1, 28.))
    if abs(outer_check["pole_product"] - rows[0.1]["pole_product"]) > 5e-8:
        raise ArithmeticError("Exterior interval affects the quoted pole product")
    if abs((rows[0.01]["tau"] - rows[0]["tau"]) / 0.01**2 + 0.25) > 1e-4:
        raise ArithmeticError("Tension disagrees with the boundary term")
    for key, slope_key in (("nu_squared", "nu_squared_w2"), ("pole_product", "product_w2")):
        finite_slope = (rows[0.01][key] - rows[0][key]) / 0.01**2
        if abs(finite_slope - slopes[-1][slope_key]) > 2e-4:
            raise ArithmeticError(f"Nonlinear solve disagrees with the linear response for {key}")
    split = (even[1]["nu_squared"][1] - even[1]["nu_squared"][0]) / (2 * even[1]["w"])
    if abs(split - slopes[-1]["even_mass_squared_linear_split"]) > 5e-4:
        raise ArithmeticError("Even Hessian disagrees with degenerate perturbation theory")
    if max(abs(row["tau_work_identity_error"]) for row in rows.values()) > 1e-7:
        raise ArithmeticError("Neutral equation and tension derivative disagree")
    if abs(slopes[-1]["even_mass_squared_linear_split"] - rows[0]["nu"]) > 1e-5:
        raise ArithmeticError("Radial matrix element disagrees with the critical virial identity")

    def threshold_difference(w):
        return observables(w, outer, critical)["nu"] - bulk_mass(w)

    crossing = brentq(threshold_difference, 0.2, 0.3, xtol=2e-8)
    print(json.dumps({"bulk_threshold_equality_w": crossing, "backgrounds": list(rows.values()), "linear_response": slopes, "even_levels": even,
                      "exterior_check": outer_check}, indent=2, allow_nan=False))


if __name__ == "__main__":
    main()
