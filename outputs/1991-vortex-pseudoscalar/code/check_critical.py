"""Critical vortex check using a BPS background and a finite Dirichlet disk."""
import numpy as np
from scipy.integrate import solve_bvp
from scipy.linalg import eigh_tridiagonal


def bps_background(outer):
    """Solve for q = log(f/r), regular at the axis, with f(outer) = 1."""
    inner = 1e-5
    r = np.linspace(inner, outer, 801)

    def equations(r, state):
        q, dq = state
        return np.vstack((dq, (r**2 * np.exp(2*q) - 1) / 2 - dq/r))

    def boundary(left, right):
        return np.array([left[1] + inner/4, right[0] + np.log(outer)])

    initial = np.vstack((-np.log1p(r**2)/2, -r/(1+r**2)))
    solution = solve_bvp(equations, boundary, r, initial, tol=2e-10, max_nodes=12000)
    if not solution.success:
        raise RuntimeError(solution.message)
    return solution


def disk_observables(background, outer, cells):
    h = outer / cells
    r = h * (np.arange(cells) + 0.5)
    q, dq = background.sol(r)
    f = r * np.exp(q)
    df = np.exp(q) * (1 + r*dq)
    da = r * (1 - f**2) / 2

    # Face fluxes at j*h, zero flux at the axis, odd ghost at the Dirichlet face.
    faces = h * np.arange(cells + 1)
    diagonal = (faces[:-1] + faces[1:]) / (r*h*h) + f**2
    diagonal[-1] += outer / (r[-1]*h*h)
    off_diagonal = -faces[1:-1] / (np.sqrt(r[:-1]*r[1:]) * h*h)
    values, modes = eigh_tridiagonal(diagonal, off_diagonal, select='i',
                                     select_range=(0, 0), tol=1e-11)
    mu = np.sqrt(values[0])
    u = np.sign(modes[0, 0]) * modes[:, 0] / np.sqrt(2*np.pi*r*h)
    ghosted = np.r_[u[0], u, -u[-1]]
    du = (ghosted[2:] - ghosted[:-2]) / (2*h)

    scalar_shape = f*u/mu
    vector_shape = -du/mu
    norm = 2*np.pi*h * np.sum(r * (scalar_shape**2 + vector_shape**2))
    direct_over_pi = h * np.sum(r**2 * df * scalar_shape + r * da * vector_shape)
    flux_over_pi = 2*h * np.sum(da*u) / mu
    return values[0], norm, direct_over_pi, flux_over_pi


if __name__ == '__main__':
    outer = 30.0
    solution = bps_background(outer)
    print("cells    mu^2           shape norm     |kappa|/pi     flux/pi")
    for cells in (5000, 10000, 20000):
        mu2, norm, direct, flux = disk_observables(solution, outer, cells)
        print(f"{cells:5d}    {mu2:.10f}   {norm:.10f}   {direct:.10f}   {flux:.10f}")
    if not (abs(norm - 1) < 2e-6 and abs(direct - flux) < 2e-6
            and round(mu2, 6) == 0.777473 and round(direct, 4) == 0.3823):
        raise ArithmeticError("The finest disk does not reproduce the quoted critical data")
