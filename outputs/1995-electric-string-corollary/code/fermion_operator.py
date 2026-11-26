"""Section 11.4: the transverse fermion operator of the unit string, checked symbolically.

Conventions (stated in Section 11.4): left-handed Weyl spinors with lower indices,
sigma-bar^mu D_mu = d_t - sigma.D, equations of motion
    i sigma-bar.D psi_i = -conj(M_ij) eps conj(psi_j),   eps = i sigma_2,
from L = -i psi^dag sigma-bar.D psi - (1/2)(M_ij psi_i psi_j + c.c.).
Photon units: e = 1, v^2 = 1/2, phi = H = f e^{i theta}/sqrt2.

Checks written to results/fermion-operator.json:
  1. the vacuum mass matrix of (psi_q, psi_qt, psi_A, lambda) has four equal
     singular values m_gamma, for any phase of the superpotential coupling;
  2. with chi_pm = (psi_A +- lambda)/sqrt2 (phase-adjusted) the matrix splits into
     the sectors (psi_q, chi_+) and (psi_qt, chi_-), at any point of the vortex;
  3. the component equations of each sector are, identically and without using the
     Bogomolny equations, the 2d Dirac system (d_t -+ d_3) u = -D^dag v,
     (d_t +- d_3) v = D u with the bosonic deformation operator D of Eq. (28).
"""
import json
from pathlib import Path

import numpy as np
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
t, x, y, z = sp.symbols("t x y z", real=True)
I = sp.I


def cfield(name):
    return sp.Function(name + "r", real=True)(t, x, y, z) + I * sp.Function(name + "i", real=True)(t, x, y, z)


def mass_matrix_checks():
    out = {}
    rng = np.random.default_rng(1995)
    for alpha in (0.0, 0.7, np.pi):
        worst_vac, worst_split = 0.0, 0.0
        for _ in range(50):
            theta = rng.uniform(0, 2 * np.pi)
            f = rng.uniform(0, 1.2)
            H = f * np.exp(1j * theta) / np.sqrt(2)          # phi = H, |H| -> 1/sqrt2
            q, qt = H / np.sqrt(2), np.conj(H) / np.sqrt(2)   # q = H/sqrt2, qt = conj(H)/sqrt2
            g = 1.0                                           # absorbed in photon units
            c = np.sqrt(2) * g * np.exp(1j * alpha)
            # rows/cols: psi_q, psi_qt, psi_A, lambda  (charges +1, -1, 0, 0)
            M = np.array([[0, 0, c * qt, np.sqrt(2) * np.conj(q)],
                          [0, 0, c * q, -np.sqrt(2) * np.conj(qt)],
                          [c * qt, c * q, 0, 0],
                          [np.sqrt(2) * np.conj(q), -np.sqrt(2) * np.conj(qt), 0, 0]])
            if abs(f - 1) < 1e-12 or True:
                sv = np.linalg.svd(M / 1.0, compute_uv=False)
                worst_vac = max(worst_vac, np.max(np.abs(sv - f)))   # all four equal f (= 1 in vacuum)
            U = np.eye(4, dtype=complex)
            U[2:, 2:] = np.array([[np.exp(-1j * alpha), np.exp(-1j * alpha)], [1, -1]]) / np.sqrt(2)
            Mr = U.T @ M @ U   # psi -> U psi' keeps -(1/2) psi^T M psi form
            # sector split: (psi_q, chi_+) and (psi_qt, chi_-) only
            mask = np.ones((4, 4), bool)
            for i, j in [(0, 2), (2, 0), (1, 3), (3, 1)]:
                mask[i, j] = False
            worst_split = max(worst_split, np.max(np.abs(Mr[mask])))
        out[f"alpha={alpha:.3f}"] = dict(max_singular_value_minus_f=float(worst_vac),
                                         max_cross_sector_entry=float(worst_split))
    return out


def component_identity(sector):
    """Sector 1: psi_q (charge +1), chi_+, conj(m) = sqrt2 phi.
    Sector 2: psi_qt (charge -1), chi_-, conj(m) = sqrt2 conj(phi); conjugated variables."""
    A1 = sp.Function("A1", real=True)(x, y)
    A2 = sp.Function("A2", real=True)(x, y)
    phi = sp.Function("Pr", real=True)(x, y) + I * sp.Function("Pi", real=True)(x, y)
    psi = [cfield("p1"), cfield("p2")]
    chi = [cfield("c1"), cfield("c2")]
    cj = sp.conjugate

    def Dj(u, j, charge):
        A = (A1, A2)[j]
        return sp.diff(u, (x, y)[j]) - I * charge * A * u

    def sigma_dot_D(s, charge):
        d1 = [Dj(s[0], 0, charge), Dj(s[1], 0, charge)]
        d2 = [Dj(s[0], 1, charge), Dj(s[1], 1, charge)]
        d3 = [sp.diff(s[0], z), sp.diff(s[1], z)]
        return [d1[1] - I * d2[1] + d3[0], d1[0] + I * d2[0] - d3[1]]

    def eps_conj(s):
        return [cj(s[1]), -cj(s[0])]

    charge = 1 if sector == 1 else -1
    mbar = sp.sqrt(2) * phi if sector == 1 else sp.sqrt(2) * cj(phi)
    sdp, sdc = sigma_dot_D(psi, charge), sigma_dot_D(chi, 0)
    ec, ep = eps_conj(chi), eps_conj(psi)
    R_psi = [I * (sp.diff(psi[k], t) - sdp[k]) + mbar * ec[k] for k in range(2)]
    R_chi = [I * (sp.diff(chi[k], t) - sdc[k]) + mbar * ep[k] for k in range(2)]

    def dz(u):
        return (sp.diff(u, x) - I * sp.diff(u, y)) / 2

    def dzb(u):
        return (sp.diff(u, x) + I * sp.diff(u, y)) / 2

    Az, Azb = (A1 - I * A2) / 2, (A1 + I * A2) / 2
    Dz = lambda u: dz(u) - I * Az * u     # noqa: E731
    Dzb = lambda u: dzb(u) - I * Azb * u  # noqa: E731
    if sector == 1:
        B, eta = cj(chi[0]), psi[0]
        vX, vZ = psi[1], -I * cj(chi[1])
    else:
        B, eta = chi[1], cj(psi[1])
        vX, vZ = cj(psi[0]), -I * chi[0]
    Du = [-I * sp.sqrt(2) * phi * B + 2 * Dzb(eta), -2 * I * dz(B) + sp.sqrt(2) * cj(phi) * eta]
    Ddv = [I * sp.sqrt(2) * cj(phi) * vX - 2 * I * dzb(vZ), -2 * Dz(vX) + sp.sqrt(2) * phi * vZ]
    plus = lambda u: sp.diff(u, t) + sp.diff(u, z)   # noqa: E731
    minus = lambda u: sp.diff(u, t) - sp.diff(u, z)  # noqa: E731
    pv, pu = (plus, minus) if sector == 1 else (minus, plus)
    sv, su = ("+", "-") if sector == 1 else ("-", "+")
    targets = {
        f"(dt{sv}d3)v_X - (Du)_X": pv(vX) - Du[0],
        f"(dt{sv}d3)v_Z - (Du)_Z": pv(vZ) - Du[1],
        f"(dt{su}d3)u_B + (D^dag v)_B": pu(B) + Ddv[0],
        f"(dt{su}d3)u_eta + (D^dag v)_eta": pu(eta) + Ddv[1],
    }
    residuals = {"R_psi1": R_psi[0], "R_psi2": R_psi[1], "R_chi1": R_chi[0], "R_chi2": R_chi[1]}
    result = {}
    for label, expr in targets.items():
        found = None
        for rname, R in residuals.items():
            for conj in (False, True):
                base = cj(R) if conj else R
                for c in (1, -1, I, -I):
                    diff = sp.expand(expr - c * base)
                    # all component functions are real: conj(Derivative(real)) = Derivative(real)
                    diff = diff.replace(lambda e: isinstance(e, sp.conjugate) and isinstance(e.args[0], sp.Derivative),
                                        lambda e: e.args[0])
                    if sp.simplify(sp.expand(diff)) == 0:
                        found = f"{c} * {'conj(' + rname + ')' if conj else rname}"
                        break
                if found:
                    break
            if found:
                break
        result[label] = found
    return result


def main():
    out = {"mass_matrix": mass_matrix_checks(),
           "sector_1_identity": component_identity(1),
           "sector_2_identity": component_identity(2)}
    out["relabelling"] = {
        "sector_1": "u = (conj chi_+1, psi_q1), v = (psi_q2, -i conj chi_+2); left-moving kernel",
        "sector_2": "u = (chi_-2, conj psi_qt2), v = (conj psi_qt1, -i chi_-1); right-moving kernel",
        "chi_pm": "(exp(i alpha) psi_A +- lambda)/sqrt2 for superpotential phase alpha; alpha = 0 here",
        "components": "1, 2 are the sigma_3 = +1, -1 components of the lower-index Weyl spinor"}
    (ROOT / "results" / "fermion-operator.json").write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))
    assert all(v is not None for k in ("sector_1_identity", "sector_2_identity") for v in out[k].values())


if __name__ == "__main__":
    main()
