"""Project the neutral imaginary and longitudinal odd modes of the monopole string.

Python/SciPy. Photon mass units. The two-level kinetic mixing is a sensitivity
calculation for the displayed Wilsonian term, with all other corrections held fixed.
"""
import json
from math import exp, log, pi, sqrt
from pathlib import Path
import sys

import numpy as np
from scipy.sparse import bmat, block_diag
from scipy.sparse.linalg import spsolve

OUTPUTS = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(OUTPUTS / "1992-scalar-doublet" / "code"))
from trace_spectrum import RadialElements, normalized_modes, static_solution


def odd_block(w, radius, step):
    mesh = RadialElements(radius, step)
    solution = static_solution(w, radius, detuning=0, winding=1)
    r = mesh.r
    f, _, a, va, s, _ = solution.sol(np.log(r.ravel())).reshape(6, *r.shape)
    b = va / r**2
    j = slice(1, -1)
    neutral = slice(0, -1)
    mj, mn = mesh.mass[j, j], mesh.mass[neutral, neutral]
    vector = (mesh.kinetic + mesh.multiplication(f**2))[neutral, neutral]
    odd_values, odd_vectors = normalized_modes(vector, mn, 1)
    lambda_b = float(odd_values[0])
    vector_wave = odd_vectors[:, 0]
    charged = (mesh.kinetic + mesh.multiplication(
        (1-a)**2 / r**2 + (1+f**2)/2 - w*s + s**2))[j,j]
    cross = mesh.multiplication(f)[j,neutral]
    full = bmat(((charged, w*cross),
                 (w*cross.T, vector + w**2 * mn)), format="csc")
    mass = block_diag((mj,mn), format="csc")
    neutral_values, neutral_vectors = normalized_modes(full, mass, 1)
    lambda_n = float(neutral_values[0])
    neutral_wave = neutral_vectors[mj.shape[0]:,0]
    u = mesh.interpolate(np.r_[vector_wave,0])
    v = mesh.interpolate(np.r_[neutral_wave,0])
    row = dict(w=w, radius=radius, step=mesh.h, lambda_b=lambda_b, lambda_n=lambda_n,
               neutral_norm=float(neutral_wave @ mn @ neutral_wave),
               magnetic_overlap=abs(mesh.integrate(b*u*v)))
    if w==0:
        rhs = cross @ vector_wave
        susceptibility = float(rhs @ spsolve(charged-lambda_b*mj, rhs))
        row["relative_mass_squared_w2"] = 1 - susceptibility
        row["complement_response"] = susceptibility
    else:
        row["relative_mass_squared_w2"] = (lambda_n - lambda_b) / w**2
    return row


def kinetic_projection(lambda_b, lambda_n, h):
    # Stable evaluation of the squared-mass half-difference as h and the
    # diagonal detuning both tend to zero.
    middle = (lambda_b + lambda_n + h*h) / 2
    difference = np.hypot(lambda_b - lambda_n, abs(h)*sqrt(2*(lambda_b+lambda_n)+h*h))
    upper = middle + difference / 2
    lower = lambda_b * lambda_n / upper
    lower_weight = (lambda_n-lambda_b-h*h+difference)/(2*difference)
    upper_weight = (lambda_b-lambda_n+h*h+difference)/(2*difference)
    return dict(lower_mass=sqrt(lower), upper_mass=sqrt(upper),
                lower_vector_weight=lower_weight, upper_vector_weight=upper_weight)


def main():
    critical = [odd_block(0, 32, h) for h in (0.04, 0.02, 0.01, 0.005)]
    rows = [odd_block(w,32,0.01) for w in (0.001,0.005,0.01,0.025,0.05,0.1)]
    exterior = odd_block(0.01,40,0.01)
    if abs(exterior["relative_mass_squared_w2"] - rows[2]["relative_mass_squared_w2"]) > 4e-6:
        raise ArithmeticError("The neutral bound level depends on the exterior truncation")
    if abs(rows[0]["relative_mass_squared_w2"] - critical[2]["relative_mass_squared_w2"]) > 2e-4:
        raise ArithmeticError("Finite deformation disagrees with the complementary resolvent")
    for row in rows:
        w = row["w"]
        row["lightest_bulk_mass"] = sqrt(1+w*w/4)-w/2
        m_over_lambda = 8*sqrt(2)*w
        row["m_gamma_over_Lambda"] = m_over_lambda
        if m_over_lambda < 0.1:
            # Only an example of the isolated analytic term. Choose the finite
            # matching constant equal to one in ell=log(Lambda/m_gamma).
            ell = log(1/m_over_lambda)
            h = 3*w*row["magnetic_overlap"]/ell
            projection = kinetic_projection(row["lambda_b"],row["lambda_n"],h)
            if min(projection["lower_vector_weight"], projection["upper_vector_weight"]) < 0:
                raise ArithmeticError("Lost positive vector projection")
            if abs(projection["lower_vector_weight"]+projection["upper_vector_weight"]-1)>1e-12:
                raise ArithmeticError("Lost total vector weight")
            row["one_term_projection"] = dict(ell=ell, h_over_mgamma=h, **projection)

    old = json.loads((OUTPUTS/"1994-monopole-string/results/spectrum.json").read_text())
    tensions = {r["w"]:r["tau"] for r in old["backgrounds"]}
    consistency = []
    for row in old["even_levels"]:
        w=row["w"]
        if w:
            low,high=map(sqrt,row["nu_squared"])
            consistency.append(dict(w=w, gap_squared_over_tension_loss=(high-low)**2/(tensions[0]-tensions[w])))
    widths=[]
    for ell in (10,20,40,80):
        g=2*pi/sqrt(ell)
        w=exp(-ell)/(8*sqrt(2))
        bright_width=0.0110427*g*g*sqrt(critical[-1]["lambda_b"])
        widths.append(dict(ell=ell,w=w,g=g, gap_over_bright_partial_width=w/bright_width))
    print(json.dumps(dict(critical=critical, radial=rows, exterior_check=exterior,
                          tension_gap_check=consistency, leading_log_examples=widths),
                     indent=2,allow_nan=False))


if __name__ == "__main__":
    main()
