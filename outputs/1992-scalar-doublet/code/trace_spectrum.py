"""Masses and physical two-phonon source strengths of the scalar vortex doublet.

Use Python, NumPy and SciPy. All lengths are in inverse dual photon masses.
The radial background and all fluctuation matrices are assembled in this file.
"""
import json
from math import pi, sqrt

import numpy as np
from scipy.integrate import solve_bvp
from scipy.optimize import brentq
from scipy.sparse import bmat, block_diag, diags
from scipy.sparse.linalg import eigsh, spsolve
from scipy.special import roots_legendre


def static_solution(w, radius, detuning, winding):
    """Use logarithmic radius and regular-axis data for the charged and neutral fields."""
    cutoff = 1e-5
    t = np.linspace(np.log(cutoff), np.log(radius), 440)
    r = np.exp(t)
    seed = np.tanh(r / 2)
    f = seed**winding
    vf = winding * r * seed**(winding-1) * (1-seed**2) / 2
    a = winding * (1 - (1 + r) * np.exp(-r))
    va = winding * r**2 * np.exp(-r)
    initial = np.vstack((f, vf, a, va, w*(winding-a)/2, -w*va/2))

    def equations(t, y):
        f, vf, a, va, s, vs = y
        r2 = np.exp(2*t)
        residual = f*f - 1 + 2*w*s
        return np.vstack((vf, (winding-a)**2*f + r2*f*(s*s + residual/2),
                          va, 2*va-r2*f*f*(winding-a),
                          vs, r2*((f*f+detuning)*s + w*residual/2)))

    def boundaries(left, right):
        f, vf, a, va, s, vs = left
        return (vf-winding*f, va-2*a, vs-cutoff**2*((w*w+detuning)*s-w/2)/2,
                right[0]-1, right[2]-winding, right[4])

    sol = solve_bvp(equations, boundaries, t, initial, tol=3e-9, max_nodes=16000)
    if not sol.success:
        raise ArithmeticError(sol.message)
    return sol


class RadialElements:
    """Consistent weighted P1 mass and stiffness matrices with Gauss integration."""
    def __init__(self, radius, spacing):
        self.cells = round(radius / spacing)
        self.h = radius / self.cells
        roots, weights = roots_legendre(4)
        self.right = (1+roots)/2
        self.left = 1-self.right
        self.r = self.h*(np.arange(self.cells)[:, None]+self.right)
        self.measure = pi*self.h*self.r*weights
        self.mass = self.multiplication(1)
        gradient = self.measure.sum(axis=1) / self.h**2
        self.kinetic = diags((-gradient, np.r_[gradient,0]+np.r_[0,gradient],
                              -gradient), (-1,0,1), format="csr")

    def multiplication(self, potential):
        weighted = self.measure*potential
        diag = np.r_[np.sum(weighted*self.left**2, axis=1),0]
        diag += np.r_[0,np.sum(weighted*self.right**2, axis=1)]
        off = np.sum(weighted*self.left*self.right, axis=1)
        return diags((off,diag,off),(-1,0,1),format="csr")

    def load(self, density):
        weighted = self.measure * density
        return (np.r_[(weighted*self.left).sum(axis=1), 0]
                + np.r_[0, (weighted*self.right).sum(axis=1)])

    def integrate(self, function):
        return float(np.sum(self.measure*function))

    def interpolate(self, values):
        return values[:-1,None]*self.left + values[1:,None]*self.right

    def derivative(self, values):
        return np.diff(values)[:,None]/self.h


def normalized_modes(stiffness, mass, count):
    values, vectors = eigsh(stiffness, k=count, M=mass, sigma=0., which="LM",
                            v0=np.ones(stiffness.shape[0]), tol=2e-12)
    order = np.argsort(values)
    return values[order], vectors[:, order]


def calculate(w, radius, spacing, detuning=0.0, winding=1):
    sol = static_solution(w, radius, detuning, winding)
    mesh = RadialElements(radius, spacing)
    r = mesh.r
    f, vf, a, va, s, vs = sol.sol(np.log(r.ravel())).reshape(6,*r.shape)
    df, da, ds = vf/r, va/r, vs/r
    b = da/r
    angular = (winding-a)*f/r
    remainder = f*f-1+2*w*s
    potential = (f*f+detuning)*s*s + remainder**2/4
    tau = mesh.integrate(df*df + angular**2 + b*b + ds*ds + potential)/(2*pi)
    virial = mesh.integrate(b*b-potential)/(2*pi)
    # The neutral profile has natural axis data. The two vector-like radial
    # coefficients vanish at the axis. All three trial spaces vanish at R.
    vanishing = slice(1,-1)
    natural = slice(0,-1)
    spaces = [vanishing,vanishing,natural]
    scalar_mass = mesh.mass[natural,natural]
    odd_matrix = (mesh.kinetic+mesh.multiplication(f*f))[natural,natural]
    odd_values, odd_vectors = normalized_modes(odd_matrix,scalar_mass,1)
    odd_lambda = float(odd_values[0])
    u = mesh.interpolate(np.r_[odd_vectors[:,0],0])
    alpha = abs(mesh.integrate(b*u))

    h_block = mesh.kinetic + mesh.multiplication((winding-a)**2/r**2+(3*f*f-1)/2+w*s+s*s)
    c_block = mesh.kinetic + mesh.multiplication(1/r**2+f*f)
    n_block = mesh.kinetic + mesh.multiplication(f*f+w*w+detuning)
    hc = mesh.multiplication(-2*f*(winding-a)/r)[vanishing,vanishing]
    hn = mesh.multiplication(f*(w+2*s))[vanishing,natural]
    stiff = bmat(((h_block[vanishing,vanishing],hc,hn),
                  (hc.T,c_block[vanishing,vanishing],None),
                  (hn.T,None,n_block[natural,natural])), format="csc")
    metric = block_diag([mesh.mass[sp,sp] for sp in spaces],format="csc")
    values, vectors = normalized_modes(stiff,metric,2)
    levels=[]
    for value, mode in zip(values,vectors.T):
        components=np.zeros((3,mesh.cells+1))
        for component,space,coefficients in zip(components,spaces,np.split(mode, [mesh.cells - 1, 2 * (mesh.cells - 1)])):
            component[space]=coefficients
        h,c,n = [mesh.interpolate(q) for q in components]
        dh,dc,dn = [mesh.derivative(q) for q in components]
        delta_b = dc+c/r
        # Off-shell derivative of the translation norm, and independently
        # its stationary reduction to the variation of magnetic minus potential energy.
        direct = mesh.integrate(4*b*delta_b + 2*df*dh + 2*angular*((winding-a)*h/r-f*c) + 2*ds*dn)
        stationary = mesh.integrate(2*f*f*(winding-a)*c/r
                                    -f*(remainder+2*s*s)*h
                                    -(2*(f*f+detuning)*s+w*remainder)*n)
        # Differentiate the static dilation identity in a normal-mode direction.
        dilation = value * mesh.integrate(vf*h + da*c + vs*n)
        if abs(direct-stationary)>3e-6:
            raise ArithmeticError("The two evaluations of the translation source disagree")
        levels.append(dict(mass=sqrt(value),mass_squared=float(value),
                           trace_over_odd=(stationary*value/(2*alpha*odd_lambda**1.5))**2,
                           neutral_fraction=mesh.integrate(n*n),
                           norm_derivative=abs(stationary), source_disagreement=abs(direct-stationary),
                           dilation_disagreement=abs(dilation-stationary)))
    lower, upper = levels
    total = lower["trace_over_odd"] + upper["trace_over_odd"]
    lower_share = lower["trace_over_odd"] / total
    zero = lower_share * upper["mass_squared"] + (1 - lower_share) * lower["mass_squared"]
    driven_zero = None
    if w != 0:
        load = np.concatenate((mesh.load(-f*(remainder+2*s*s))[vanishing],
                               mesh.load(2*f*f*(winding-a)/r)[vanishing],
                               mesh.load(-(2*(f*f+detuning)*s+w*remainder))[natural]))

        def driven_response(z):
            return load @ spsolve(z*metric-stiff, load)

        gap = upper["mass_squared"] - lower["mass_squared"]
        inside = 1e-7 * gap
        driven_zero = brentq(driven_response, lower["mass_squared"]+inside,
                             upper["mass_squared"]-inside, xtol=2e-12)
    flux = mesh.integrate(b) / (2 * pi)
    if abs(flux - winding) > 1e-7 or abs(virial) > 1e-7:
        raise ArithmeticError("Static solution failed its flux or scale-variation test")
    return dict(w=w, winding=winding, detuning=detuning, radius=radius, spacing=mesh.h, tau=tau,
                odd_mass=sqrt(odd_lambda), flux=flux, virial_error=virial, levels=levels,
                trace_sum_over_odd=total, lower_share=lower_share, pole_pair_zero=zero, driven_zero=driven_zero)


def main():
    rows=[calculate(w,32,0.01) for w in (0,0.001,0.0025,0.005,0.01,0.025,0.05,-0.01)]
    refinement=[calculate(w,32,h) for w in (0.001,0.01) for h in (0.04,0.02,0.005)]
    exterior=[calculate(0.01,r,0.01) for r in (24,40)]
    controls=[calculate(w,32,0.01,detuning=0.08) for w in (0,0.001,0.01)]
    critical_mass = rows[0]["odd_mass"]
    joint = [calculate(w, 32, 0.01, detuning=2*critical_mass*w*ratio)
             for w in (0.0025, 0.01) for ratio in (0.5, 1, 2)]
    positive, reflected = rows[4], rows[-1]
    for sign in (0, 1):
        for key in ("mass", "trace_over_odd"):
            if abs(positive["levels"][sign][key] - reflected["levels"][sign][key]) > 1e-8:
                raise ArithmeticError("The signed-deformation symmetry failed")
    resolved = refinement[2]
    lower, upper = resolved["levels"]
    slope = (upper["mass"] - lower["mass"]) / (2 * resolved["w"])
    if abs(slope - 0.5) > 2e-4 or abs(resolved["lower_share"] - 0.5) > 0.003:
        raise ArithmeticError("The refined two-mode limit failed")
    if controls[1]["lower_share"] < 0.99:
        raise ArithmeticError("A detuned neutral scalar has unexpectedly large trace weight")
    for row in joint:
        ratio = row["detuning"] / (2*critical_mass*row["w"])
        predicted_share = (1 + ratio / sqrt(1 + ratio**2)) / 2
        if abs(predicted_share-row["lower_share"]) > 0.025:
            raise ArithmeticError("Joint detuning disagrees with the two-level projection")
    multiple = [calculate(w, 32, 0.0125, winding=k) for k in (2, 3) for w in (0, 0.01)]
    for critical, split in zip(multiple[::2], multiple[1::2]):
        low, high = split["levels"]
        if abs((high["mass"] - low["mass"])/split["w"] - 1) > 0.002:
            raise ArithmeticError("Non-unit radial branch failed the splitting law")
        tension_slope = (split["tau"] - critical["tau"]) / split["w"]**2
        if abs(tension_slope + split["winding"]**2/4) > 0.002:
            raise ArithmeticError("Non-unit radial branch failed the tension response")
    print(json.dumps(dict(rows=rows, refinement=refinement, exterior=exterior,
                          detuned_control=controls, joint_scaling=joint, multiple_winding=multiple), indent=2, allow_nan=False))


if __name__=="__main__":
    main()
