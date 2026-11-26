"""Independent distance and induced-area checks in a fixed flat MQCD probe."""
import json
from math import cos, pi, sin, sqrt
from itertools import product

import numpy as np
from scipy.optimize import brentq, minimize
from numpy.polynomial.legendre import leggauss


def point(u, theta, sheet, n, radius, a):
    # Two Cartesian complex planes and the lift of the flat log(t) cylinder.
    v = a * np.exp(u + 1j*theta)
    w = a * np.exp(-u - 1j*theta)
    return np.array([v.real, v.imag, w.real, w.imag, n*radius*u,
                     radius*(n*theta - 2*pi*sheet)])


def endpoints(parameters, sector, n, radius, a, phase=0):
    u1, u2, delta = parameters
    return (point(u1, phase-delta/2, 0, n, radius, a),
            point(u2, phase+delta/2, sector, n, radius, a))


def distance_check(n, k, radius, a):
    q = 2*pi*k/n
    eta = 2*(a/(n*radius))**2
    delta = brentq(lambda d: d + eta*sin(d) - q, q-eta-0.1, q+eta+0.1)
    def squared(params):
        first, last = endpoints(params, k, n, radius, a)
        diff = last - first
        return float(diff @ diff) / (n*radius)**2
    starts = ((0.23, -0.12, 0.7*q), (-0.2, 0.14, q+0.3))
    solves = [minimize(squared, s, method="Powell", bounds=((-1.5,1.5),(-1.5,1.5),(-3*np.pi,3*np.pi)),
                       options={"xtol": 1e-10, "ftol": 1e-12, "maxiter": 8000}) for s in starts]
    if not all(sol.success for sol in solves):
        raise RuntimeError(f"Endpoint minimization failed at {eta}, {k}: {[s.message for s in solves]}")
    opt = min(solves, key=lambda sol: sol.fun)
    ell = sqrt(opt.fun)*n*radius
    expected = sqrt(8*a*a*sin(delta/2)**2 + (n*radius*(delta-q))**2)
    assert abs(ell/expected - 1) < 1e-10
    assert max(abs(opt.x[0]), abs(opt.x[1]), abs(opt.x[2]-delta)) < 2e-6
    return delta, ell, float(max(s.fun for s in solves)-opt.fun)


def tilt_check(params, k, n, radius, a, slope):
    first, last = endpoints(params, k, n, radius, a)
    tangent = last-first
    ell = np.linalg.norm(tangent)
    phase_step = 1e-5
    low = endpoints(params, k, n, radius, a, -phase_step)
    high = endpoints(params, k, n, radius, a, phase_step)
    nodes, weights = leggauss(12)
    area_difference = 0.
    for node, weight in zip(nodes, weights, strict=True):
        u = (node+1)/2
        generator = ((1-u)*(high[0]-low[0]) + u*(high[1]-low[1]))/(2*phase_step)
        det_shift = slope**2 * (generator @ generator - (generator @ tangent / ell)**2)
        # sqrt(1+x)-1 evaluated without nearly equal subtractions.
        area_difference += weight/2 * ell * det_shift / (1+sqrt(1+det_shift))
    return 2*area_difference / slope**2 / (2*pi)**2


def tension_ratio(eta):
    n, r = 4, 1.
    a = n*r*sqrt(eta/2)
    d1, l1, _ = distance_check(n, 1, r, a)
    _, l2, _ = distance_check(n, 2, r, a)
    return {"eta": eta, "delta_1": round(d1, 9), "length_1_over_a": round(l1/a, 9),
            "length_2_over_1": round(l2/l1, 9),
            "linear_coefficient": round((l2/l1/sqrt(2)-1)/eta, 8)}


def duality_check():
    tau = 0.37 + 1.41j
    def tension(q, tau):
        return abs(q[0]-tau*q[1])/sqrt(tau.imag)
    matrices = [((0,-1),(1,0)), ((1,1),(0,1)), ((2,1),(1,1))]
    worst = 0.
    for matrix in matrices:
        m=np.array(matrix, dtype=int)
        (aa,b),(c,d)=matrix
        dual_tau=(aa*tau+b)/(c*tau+d)
        for p,q in product(range(-3,4),repeat=2):
            x=np.array([p,q]); y=m@x
            worst=max(worst, abs(tension(x,tau)-tension(y,dual_tau)))
            # If original color is p modulo four, carry its covector along.
            assert int(np.array([d,-b])@y) % 4 == p % 4
    return worst


def evaluate():
    scan = [tension_ratio(eta) for eta in (0.005,0.02,0.03125,0.10,0.25,0.50,0.90)]
    n, radius, a = 4, 40., 20.
    delta, ell, spread = distance_check(n, 1, radius, a)
    sigma = ell/(2*pi)**2
    stiffness = sigma*((n*radius)**2
                       + 2*a*a*(cos(delta/2)**2+sin(delta/2)**2/3))
    tilts = []
    for dimensionless_slope in (0.08,0.04,0.02,0.01,0.005):
        measured = tilt_check((0,0,delta),1,n,radius,a,dimensionless_slope/(n*radius))
        tilts.append({"slope_times_NR": dimensionless_slope, "stiffness": round(measured,6),
                      "relative_error": round(measured/stiffness-1,10)})
    assert abs(tilts[-1]["relative_error"]) < 1e-5
    return {
        "distance_scan": scan, "example": {
            "N": n, "R_over_lp": radius, "a_over_lp": a, "delta": round(delta,9),
            "length_over_lp": round(ell,9), "sigma_lp2": round(sigma,9),
            "K_phi": round(stiffness,7), "K_phi_over_N2": round(stiffness/n**2,7),
            "sigma_R2": round(sigma*radius**2,7),
            "rotor_gap_over_sqrt_sigma_at_Lsqrt_sigma_1000": 1/(2000*stiffness),
            "unit_vortex_dimension_gaussian": round(pi*stiffness,6),
            "tilt_checks":tilts, "endpoint_start_spread":float(spread)},
        "iib": {"charge_pairs":49, "matrices":3, "max_tension_difference":duality_check()}
    }


if __name__ == "__main__":
    print(json.dumps(evaluate(), indent=2, allow_nan=False))
