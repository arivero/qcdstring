"""Radial calculation for QCDS-91/S1. All radii are in inverse vector masses."""
import json
from pathlib import Path

import numpy as np
from scipy.integrate import simpson, solve_bvp
from scipy.linalg import eigh_tridiagonal
from scipy.special import kve

ROOT = Path(__file__).resolve().parents[1]
INNER = 1e-4


def background(beta, outer):
    radius = np.linspace(INNER, outer, 450)
    f = np.tanh(radius / 2)
    a = 1 - (1 + radius) * np.exp(-radius)

    def equations(r, y):
        f, df, a, da = y
        return np.vstack((df, -df / r + (1 - a)**2 * f / r**2
                          - beta * (1 - f**2) * f / 2, da,
                          da / r - f**2 * (1 - a)))

    def boundary(left, right):
        return np.array([INNER * left[1] - left[0], INNER * left[3] - 2 * left[2],
                         right[0] - 1, right[2] - 1])

    sol = solve_bvp(equations, boundary, radius,
                    np.vstack((f, (1 - f**2) / 2, a, radius * np.exp(-radius))),
                    tol=2e-8, max_nodes=8000)
    if not sol.success:
        raise RuntimeError(sol.message)
    return sol


def radial_matrix(profile, outer, spacing):
    """Cell-centred flux stencil with zero axis flux and a Dirichlet outer face."""
    n = round(outer / spacing)
    h = outer / n
    r = (np.arange(n) + 0.5) * h
    diagonal = 2 / h**2 + profile.sol(r)[0]**2
    diagonal[-1] += outer / (r[-1] * h**2)
    off = -(r[:-1] + h / 2) / (h**2 * np.sqrt(r[:-1] * r[1:]))
    values, states = eigh_tridiagonal(diagonal, off, select='i', select_range=(0, 0))
    wave = states[:, 0] / np.sqrt(2 * np.pi * r * h)
    return values[0], r, np.sign(wave[0]) * wave


def localized(profile, outer):
    seed, cell, wave = radial_matrix(profile, outer, 0.10)
    r = np.linspace(INNER, outer, 600)
    initial = np.interp(r, cell, wave) / wave[0]

    def equations(r, y, log_k):
        eigenvalue = 1 - np.exp(2 * log_k[0])
        return np.vstack((y[1], (profile.sol(r)[0]**2 - eigenvalue) * y[0] - y[1] / r))

    def boundary(left, right, log_k):
        k = np.exp(log_k[0])
        slope = k * kve(1, k * outer) / kve(0, k * outer)
        return np.array([left[0] - 1, left[1] + (1 - k*k) * INNER * left[0] / 2,
                         right[1] + slope * right[0]])

    sol = solve_bvp(equations, boundary, r, np.vstack((initial, np.gradient(initial, r))),
                    p=[np.log(np.sqrt(1 - seed))], tol=1e-9, max_nodes=8000)
    if not sol.success:
        raise RuntimeError(sol.message)
    k = np.exp(sol.p[0])
    return 1 - k*k, sol


def calculation(beta, outer, draw=False):
    profile = background(beta, outer)
    eigenvalue, state = localized(profile, outer)
    # Include the regular axis and extend the matched Bessel tail for the norm.
    r = np.linspace(0, outer, round(outer * 400) + 1)
    f, df, a, da = profile.sol(np.maximum(r, INNER))
    f[0], a[0], da[0] = 0, 0, 0
    mag = np.divide(da, r, out=np.full_like(r, da[1] / r[1]), where=r > 0)
    w, dw = state.sol(np.maximum(r, INNER))
    dw[0] = 0
    k = np.sqrt(1 - eigenvalue)
    tail_r = np.linspace(outer, outer + 40 / k, 4001)
    tail = w[-1] * np.exp(-k * (tail_r - outer)) * kve(0, k * tail_r) / kve(0, k * outer)

    def integral(y):
        return simpson(y, x=r)

    norm = np.sqrt(2 * np.pi * (integral(r * w*w) + simpson(tail_r * tail**2, x=tail_r)))
    u, du, tail_u = w / norm, dw / norm, tail / norm
    mu = np.sqrt(eigenvalue)
    alpha = 2 * np.pi * integral(da * u)  # e I/m_V
    # 4e int psi Im[(D1 Phi)* D2 Phi] = m_*^2 I, in vector mass units.
    current = 4 * np.pi * integral(u * df * (1 - a) * f)
    angular = np.divide((1 - a) * f, r, out=np.full_like(r, df[0]), where=r > 0)
    tau = integral(r * (df**2 + angular**2 + mag**2 + beta * (1 - f**2)**2 / 4))
    rayleigh_bulk = integral(r * (du**2 + f**2 * u*u)) * 2 * np.pi
    # Exterior integration by parts for a solution of the constant-potential equation.
    tail_norm = 2 * np.pi * simpson(tail_r * tail_u**2, x=tail_r)
    rayleigh = rayleigh_bulk + eigenvalue * tail_norm - 2 * np.pi * outer * u[-1] * du[-1]
    potential_moment = integral(r * (1 - f*f) * u)
    wave_moment = integral(r * u) + simpson(tail_r * tail_u, x=tail_r)
    flux = integral(da)
    # Scaling of the classical stationary energy at fixed flux interchanges these terms.
    magnetic = integral(r * mag**2)
    potential = integral(r * beta * (1 - f*f)**2 / 4)
    matrix = {}
    for h in (0.10, 0.05, 0.025):
        lam, cells, uu = radial_matrix(profile, outer, h)
        dalpha = profile.sol(cells)[3]
        matrix[str(h)] = [float(lam), float(2 * np.pi * h * np.sum(dalpha * uu) / np.sqrt(lam))]
    Qe = alpha / mu
    mass_scale = mu / np.sqrt(np.pi * tau)
    result = dict(beta=beta, outer=outer, mu2=eigenvalue, mu=mu, kappa=k,
                  alpha=alpha, eQ=Qe, tau=tau, m_over_e_sqrt_sigma=mass_scale,
                  residue_over_e6_sigma2=Qe**2 * mass_scale**8 / 2,
                  product=Qe * mass_scale, width_over_e2_mass=Qe**2 * mass_scale**4 / 8,
                  first_splitting_over_e_mass=Qe * mass_scale**2 / np.sqrt(4*np.pi),
                  source_weight=alpha**2 / (2*np.pi*magnetic),
                  u0=u[0], flux=flux, magnetic=magnetic, potential=potential,
                  current_over_mu2alpha=current / (eigenvalue * alpha),
                  integrated_equation=potential_moment / (k*k * wave_moment),
                  rayleigh=rayleigh, tail_norm=tail_norm, positive=bool(np.all(u > 0)),
                  matrix_dirichlet=matrix)
    if beta == 1:
        result['bps_first'] = float(np.max(np.abs(df - angular)))
        field_residual = np.abs(mag - (1 - f*f) / 2)
        result['bps_second'] = float(np.max(field_residual))
        result['bps_second_off_axis'] = float(np.max(field_residual[1:]))
        # Canonical BPS partner in Eq. (16) of the curvature comparison.
        # The azimuthal potential perturbation is r times the vector profile.
        scalar_shape = f * u / mu
        vector_shape = -du / mu
        tail_du = -k * kve(1, k * tail_r) / kve(0, k * tail_r) * tail_u
        norm_inside = integral(r * (scalar_shape**2 + vector_shape**2))
        norm_outside = simpson(tail_r * (tail_u**2 + tail_du**2), x=tail_r) / eigenvalue
        shape_norm = 2 * np.pi * (norm_inside + norm_outside)
        scalar_term = np.pi * integral(r**2 * df * scalar_shape)
        vector_term = np.pi * integral(r * da * vector_shape)
        journal_kappa = -(scalar_term + vector_term)
        result['curvature_eq27'] = dict(shape_norm=shape_norm, scalar_term=scalar_term,
                                        vector_term=vector_term, journal_kappa=journal_kappa)
        if abs(shape_norm - 1) > 3e-6 or abs(journal_kappa + Qe) > 3e-6:
            raise ArithmeticError("Canonical shape norm or curvature/flux comparison failed")

        # Change the static profiles along the normalized even partner at e=m_V=1.
        def translational_norm(delta):
            shifted_f = f + delta * f * u / mu
            shifted_df = df + delta * (df * u + f * du) / mu
            shifted_a = a - delta * r * du / mu
            shifted_mag = mag - delta * (f**2 - eigenvalue) * u / mu
            shifted_ang = np.divide((1 - shifted_a) * shifted_f, r,
                                    out=shifted_df.copy(), where=r > 0)
            return 2 * np.pi * integral(r * (shifted_mag**2
                                        + (shifted_df**2 + shifted_ang**2) / 2))
        delta = 1e-4
        slope = (translational_norm(delta) - translational_norm(-delta)) / (2 * delta)
        result['even_norm_derivative'] = slope
        result['even_over_odd_vertex'] = slope / (mu * alpha)
        if (abs(result['even_over_odd_vertex'] - 1) > 3e-6 or abs(tau - 1) > 2e-6
                or max(result['bps_first'], result['bps_second']) > 3e-6):
            raise ArithmeticError("Critical profile or scalar-partner check failed")
    if draw:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fig, (ax, bx) = plt.subplots(1, 2, figsize=(8.2, 3.1), constrained_layout=True)
        ax.plot(r, f**2, label=r"$f^2$ (potential)")
        ax.plot(r, u / u[0], label=r"$u/u(0)$ (state)")
        ax.axhline(eigenvalue, ls="--", color="0.35", label=r"$m_*^2/m_V^2$")
        ax.set(xlim=(0, 10), ylim=(0, 1.08), xlabel=r"$m_V r$")
        ax.legend(fontsize=8)
        bx.plot(r, 2 * np.pi * r * u**2, label="norm density")
        bx.plot(r, 2 * np.pi * da * u / alpha, label="flux overlap density")
        bx.set(xlim=(0, 10), ylim=(0, None), xlabel=r"$m_V r$", ylabel="per unit scaled radius")
        bx.legend(fontsize=8)
        fig.savefig(ROOT / 'figures/profiles.png', dpi=175)
        plt.close(fig)
    if not (0 < eigenvalue < 1 and result['positive'] and abs(tau) > 0
            and abs(flux - 1) < 2e-6 and abs(current / (eigenvalue * alpha) - 1) < 2e-6
            and abs(rayleigh - eigenvalue) < 2e-6 and abs(magnetic - potential) < 2e-6
            and abs(result['integrated_equation'] - 1) < 2e-6):
        raise ArithmeticError(result)
    return result


if __name__ == '__main__':
    rows = [calculation(beta, 36, draw=(beta == 1)) for beta in (0.5, 1, 2)]
    rows += [calculation(1, outer) for outer in (18, 26)]
    (ROOT / 'results/radial.json').write_text(json.dumps(rows, indent=2) + '\n')
    for row in rows:
        print(*(f'{row[key]:.9g}' for key in ('beta', 'outer', 'mu2', 'mu', 'alpha', 'eQ',
                                                'tau', 'product', 'residue_over_e6_sigma2')))
