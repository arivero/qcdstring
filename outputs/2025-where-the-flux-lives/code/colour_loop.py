"""Short-distance response of the metric-colour insertion at separated endpoints."""
import json
import math
from pathlib import Path

import numpy as np
from scipy.integrate import quad

ROOT = Path(__file__).resolve().parents[1]


def parameter_integral(z):
    def integrand(x):
        weight = x*(1-x)
        y = z/math.sqrt(weight)
        return 6*weight*(1+y)*math.exp(-y)
    return quad(integrand, 0, 1, epsrel=2e-12, epsabs=2e-17, limit=200)[0]


def spectral_integral(z):
    def integrand(t):
        return math.exp(-t)*(t+2*z*z/t)*math.sqrt(max(0., 1-(2*z/t)**2))
    return quad(integrand, 2*z, np.inf, epsrel=2e-12, epsabs=2e-17, limit=200)[0]


def finite_pole(z, heavy):
    """One exact heavy propagator with P(0)=0, relative to its massless soft result."""
    def integrand(t):
        rho = (1+2*(z/t)**2)*math.sqrt(max(0., 1-(2*z/t)**2))
        if abs(t-heavy) < 1e-7:
            quotient = (heavy/2-1)*math.exp(-heavy)
        else:
            quotient = (t*t*math.exp(-t)-heavy**2*math.exp(-heavy))/(heavy**2-t*t)
        return rho*heavy**2*quotient/t
    # The apparent singularity at t=heavy is removable in the combined transform.
    near = quad(integrand, 2*z, heavy, epsabs=2e-14, epsrel=2e-12)[0]
    far = quad(integrand, heavy, np.inf, epsabs=2e-14, epsrel=2e-12)[0]
    return near+far


def check_insertion(q2, c_vector, masses2):
    # Canonical massless metric field followed by the two diagonal massive fields.
    e0 = np.array([1., 0., 0.])
    light = np.array([1., c_vector, c_vector])
    poles = np.diag(np.r_[q2, q2+np.array(masses2)])
    cross = q2 * np.array([[0., 1., 1.], [1., 0., 0.], [1., 0., 0.]])

    def bubble_factor(h):
        return (q2 * (e0 @ np.linalg.solve(poles+h*cross, light)))**2
    dh = 3e-6
    measured = (bubble_factor(dh)-bubble_factor(-dh))/(2*dh)
    exact = -2*c_vector*q2*sum(1/(q2+m) for m in masses2)
    assert abs(measured-exact) < 3e-10
    return dict(q2=q2, finite_difference=float(measured), analytic=exact)


def main():
    modes = json.loads((ROOT/"results"/"harmonics.json").read_text())["neck"]["shooting"]
    c = modes["odd"]["plus"]
    samples = []
    for z in (0, .1, .5, 1., 2., 5., 10.):
        first, second = parameter_integral(z), spectral_integral(z)
        assert abs(first/second-1) < 4e-10
        samples.append(dict(mass_times_separation=z, parameter=first, spectral=second))
    assert abs(samples[0]["parameter"]-1) < 1e-13
    assert all(row["parameter"] > nxt["parameter"] for row,nxt in zip(samples,samples[1:]))
    # Units for these finite-q normalization checks are arbitrary.
    signs = [check_insertion(q2, -c/2, (2., 18.)) for q2 in (.03, .4, 2.)]
    finite = []
    for z in (.5, 1., 2.):
        soft = parameter_integral(z)
        ratios = []
        for first_mass in (20., 40., 80.):
            # M2/M1=3. Normalize each propagator by its own term in K.
            exact = (finite_pole(z, first_mass)+finite_pole(z, 3*first_mass)/9)/(1+1/9)
            ratios.append(exact/soft)
            finite.append(dict(mR=z, M1R=first_mass, M2R=3*first_mass,
                               finite_over_soft=ratios[-1]))
        assert all(abs(a-1)>abs(b-1) for a,b in zip(ratios, ratios[1:]))
        assert abs(ratios[-1]-1)<.006
    result = dict(mass_function=samples, inverse_kernel_checks=signs, finite_poles=finite,
                  coefficient_of_K_alpha_s_squared_over_R_cubed=2*(4/3)*.5*c/(3*math.pi))
    (ROOT/"results"/"colour-loop.json").write_text(json.dumps(result,indent=2)+"\n")


if __name__ == "__main__":
    main()
