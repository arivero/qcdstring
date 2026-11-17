#!/usr/bin/env python3
"""Reproduce QCDS-88/1: quadratic spectra, determinants and curvature exchange.

No lattice simulation or fit. Numerical work checks the displayed derivations.
All paths are relative to this file, not the invoking working directory.
"""
import json
import platform
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import mpmath as mp
import numpy as np
import scipy
from scipy.integrate import quad
from scipy.linalg import eigh
from scipy.special import k1
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
FIGURES = ROOT / "figures"
CHECKS = []


def close(name, actual, expected, atol=1e-11, rtol=1e-10):
    actual, expected = np.asarray(actual), np.asarray(expected)
    error = float(np.max(np.abs(actual - expected)))
    tolerance = float(atol + rtol * np.max(np.abs(expected)))
    CHECKS.append(dict(name=name, error=error, tolerance=tolerance,
                       passed=bool(error <= tolerance)))


def condition(name, passed):
    CHECKS.append(dict(name=name, passed=bool(passed)))


def symbolic(name, expression):
    condition(name, sp.simplify(expression) == 0)


def periodic_energy(x):
    """L E_C for a single scalar with x = M L, extensive term removed."""
    if x == 0:
        return -np.pi / 6
    if x < 0:
        raise ValueError("M L must be nonnegative")
    windings = np.arange(1, max(2, int(np.ceil(45 / x))) + 1)
    return float(-x / np.pi * np.sum(k1(windings * x) / windings))


def integral_energy(x):
    """Independent momentum-log representation of L E_C."""
    val, error = quad(lambda u: np.log(-np.expm1(-np.hypot(u, x))),
                      0, np.inf, epsabs=2e-12, epsrel=2e-12)
    return val / np.pi, error / np.pi


def interval_energy(x):
    """R E_DD after subtracting bulk and isolated endpoint energies."""
    val, error = quad(lambda u: np.log(-np.expm1(-2*np.hypot(u, x))),
                      0, np.inf, epsabs=2e-12, epsrel=2e-12)
    return val / (2*np.pi), error / (2*np.pi)


def spectra():
    rows = []
    for g in (0.0, 0.3, 0.6, 0.9):
        m = 1.0
        a = np.sqrt(1-g*g)
        M = m/a
        B = np.array([[1., -g], [-g, 1.]])
        V = np.diag([0., m*m])
        masses2, vectors = eigh(V, B)
        close(f"generalized masses g={g}", masses2, [0., M*M])
        close(f"source residues g={g}", vectors[0]**2, [1., g*g/(1-g*g)])
        T = np.array([[1., g/a], [0., 1/a]])
        close(f"canonical kinetic matrix g={g}", T.T @ B @ T, np.eye(2))
        close(f"canonical mass matrix g={g}", T.T @ V @ T, np.diag([0., M*M]))
        condition(f"positive kinetic eigenvalues g={g}", np.linalg.eigvalsh(B).min() > 0)
        for z in (0.03, 0.4, 2., 10.):
            Q = z*B+V
            effective = z-g*g*z*z/(z+m*m)
            close(f"integrated determinant g={g} z={z}",
                  np.linalg.det(Q), (z+m*m)*effective)
            close(f"displacement spectral form g={g} z={z}",
                  np.linalg.inv(Q)[0, 0], 1/z+(g*g/(1-g*g))/(z+M*M))
        rows.append(dict(g=g, M_over_m=M, residue=g*g/(1-g*g),
                         spurious_p_over_m=None if g == 0 else 1/g))
    # A positive Euclidean p^4 kernel is not sufficient for reflection positivity.
    # This matrix is C(t_i+t_j) at a fixed nonzero spatial momentum.
    times = np.array([0.2, 1.0])
    sums = times[:, None] + times[None, :]
    k, alpha = 1., 1.
    omega = np.sqrt(k*k+1/alpha)
    reflection = np.exp(-k*sums)/(2*k)-np.exp(-omega*sums)/(2*omega)
    eigs = np.linalg.eigvalsh(reflection)
    condition("positive-stiffness reflection counterexample", eigs[0] < -1e-5)
    return rows, eigs.tolist()


def algebra():
    z, m, g, s, sig, q, L = sp.symbols("z m g s sigma q L", positive=True)
    Q = sp.Matrix([[z, -g*z], [-g*z, z+m*m]])
    symbolic("kernel determinant", Q.det()-z*((1-g*g)*z+m*m))
    symbolic("integrating out a field", Q.inv()[0, 0]-1/(z-g*g*z*z/(z+m*m)))
    # First-order reduction of the p^4 operator. y=(1+g^2 z/(2m^2)) chi.
    eps = sp.symbols("epsilon")
    reduced = (1+eps*g*g*z/(2*m*m))**2*(z-eps*g*g*z*z/(m*m))
    symbolic("first-order field redefinition", sp.diff(reduced, eps).subs(eps, 0))
    # Null external vectors independently give the intrinsic-curvature vertex.
    p, r = sp.symbols("p r", positive=True)
    eta = sp.diag(1, -1)
    p1, p2 = sp.Matrix([p, p]), sp.Matrix([r, -r])
    dot = (p1.T*eta*p2)[0]
    invariant = ((p1+p2).T*eta*(p1+p2))[0]
    vertex = -2*q*dot**2/sig
    symbolic("on-shell curvature vertex", vertex+q*invariant**2/(2*sig))
    exchange = q*q/(4*sig*sig)*(s**4/(m*m-s)+s**4/(m*m+s))
    theta = exchange/(2*s)
    b = q*q/(4*sig*sig*m*m)
    symbolic("crossed scalar exchange", theta-b*s**3/(1-s*s/m**4))
    symbolic("phase is odd", theta+theta.subs(s, -s))
    symbolic("low-energy phase coefficient", sp.limit(theta/s**3, s, 0)-b)
    # Direct on-shell Hessian contraction, followed by the vacuum contraction.
    f, h = sp.symbols("f h")
    H = sp.Matrix([[f+h, f-h], [f-h, f+h]])
    R2 = (sp.trace(eta*H)**2-sp.trace(eta*H*eta*H))/sig
    symbolic("intrinsic curvature on free waves", R2+8*f*h/sig)
    contraction = sp.pi**3/(30*L**4)
    energy = -q*q/(2*m*m)*64/(sig*sig)*L*contraction**2
    symbolic("direct vacuum shift versus scattering coefficient",
             energy+32*sp.pi**6*b/(225*L**7))
    # Derive the finite term of a regulated sum; no zeta value is an input.
    a = sp.symbols("a", positive=True)
    w = sp.exp(-a)
    sum_n3 = w*(1+4*w+w*w)/(1-w)**4
    symbolic("finite regulated chiral contraction", sp.limit(sum_n3-6/a**4, a, 0)-sp.Rational(1, 120))
    return str(sp.simplify(energy))


def finite_size():
    rows = []
    for x in (0.5, 1., 2., 4., 8.):
        bessel = periodic_energy(x)
        momentum, error = integral_energy(x)
        close(f"periodic Bessel versus momentum integral x={x}", bessel, momentum)
        condition(f"periodic quadrature error x={x}", error < 1e-10)
        interval, error_dd = interval_energy(x)
        close(f"DD versus periodic at double length x={x}", interval, periodic_energy(2*x)/4)
        condition(f"DD quadrature error x={x}", error_dd < 1e-10)
        rows.append(dict(x=x, L_E=bessel, c_eff=-6*bessel/np.pi,
                         R_E_DD=interval))
    momentum, _ = integral_energy(0.)
    close("massless periodic limit", momentum, -np.pi/6)
    interval, _ = interval_energy(0.)
    close("massless DD limit", interval, -np.pi/24)
    # Small-mass leading correction and large-mass asymptotics.
    x = .001
    close("small-mass leading linear term", periodic_energy(x), -np.pi/6+x/2,
          atol=2e-6, rtol=0)
    x = 25.
    asymptotic = -np.sqrt(x/(2*np.pi))*np.exp(-x)*(1+3/(8*x)-15/(128*x*x))
    close("large-mass asymptotics", periodic_energy(x), asymptotic, atol=0., rtol=1e-5)
    return rows


def regulated_sum():
    mp.mp.dps = 60
    rows = []
    for value in ("0.2", "0.1", "0.05", "0.025"):
        a = mp.mpf(value)
        w = mp.exp(-a)
        finite = w*(1+4*w+w*w)/(1-w)**4-6/a**4
        # Derived next term: 1/120 - a^2/504 + O(a^4).
        close(f"regulated mode sum a={value}", float(finite),
              float(mp.mpf(1)/120-a*a/504), atol=float(a**4/5000), rtol=0)
        rows.append(dict(a=float(a), subtracted_sum=float(finite),
                         limit=1/120))
    return rows


def plots():
    plt.rcParams.update({"font.size": 10, "axes.spines.top": False,
                         "axes.spines.right": False, "savefig.dpi": 180})
    g = .6
    v = np.linspace(0, 4, 500)
    fig, ax = plt.subplots(figsize=(6.8, 4.0))
    ax.plot(v, 1-g*g*v/(1+v), label="Exact integrated kernel", color="#1b5678", lw=2)
    ax.plot(v, 1-g*g*v, label="Through $p^4$", color="#b64b32", ls="--")
    ax.plot(v, 1-g*g*v+g*g*v*v, label="Through $p^6$", color="#597d36", ls=":")
    ax.axvspan(0, 1, color="#dbe6eb", alpha=.45, label="Taylor convergence domain")
    ax.axhline(0, color="0.5", lw=.7)
    ax.set(xlabel="$p_E^2/m^2$", ylabel="$K_{\\rm eff}(p_E^2)/p_E^2$",
           ylim=(-.6, 2.8), xlim=(0, 4))
    ax.legend(frameon=False)
    fig.tight_layout()
    for ext in ("png", "pdf"):
        fig.savefig(FIGURES / f"kernel88.{ext}")
    plt.close(fig)
    xs = np.linspace(.08, 9, 250)
    values = np.array([periodic_energy(x) for x in xs])
    fig, ax = plt.subplots(figsize=(6.8, 4.0))
    ax.plot(xs, -6*values/np.pi, color="#1b5678", lw=2,
            label="One periodic massive scalar")
    leading = 6/np.pi*np.sqrt(xs/(2*np.pi))*np.exp(-xs)
    ax.plot(xs[xs >= 2], leading[xs >= 2], color="#b64b32", ls="--",
            label="Leading large-mass expression")
    ax.set(xlabel="$M L$", ylabel="$-6 L E_C/\\pi$", xlim=(0, 9), ylim=(0, 1.02))
    ax.legend(frameon=False)
    fig.tight_layout()
    for ext in ("png", "pdf"):
        fig.savefig(FIGURES / f"casimir88.{ext}")
    plt.close(fig)


def main():
    RESULTS.mkdir(exist_ok=True)
    FIGURES.mkdir(exist_ok=True)
    mass_rows, reflection = spectra()
    expression = algebra()
    energy_rows = finite_size()
    regulator_rows = regulated_sum()
    plots()
    result = dict(checks=CHECKS, normal_modes=mass_rows,
                  reflection_eigenvalues=reflection, finite_size=energy_rows,
                  regulator=regulator_rows, scalar_vacuum_shift=expression)
    (RESULTS / "thickness88.json").write_text(json.dumps(result, indent=2)+"\n")
    masses = ["| g | M/m | Massive residue in y | Spurious p_E/m |",
              "|---|---|---|---|"]
    for row in mass_rows:
        pole = "absent" if row["spurious_p_over_m"] is None else f"{row['spurious_p_over_m']:.6f}"
        masses.append(f"| {row['g']:.1f} | {row['M_over_m']:.6f} | {row['residue']:.6f} | {pole} |")
    finite = [r"| $ML$ | $LE_C$ | $-6LE_C/\pi$ | $R E_{DD}^{\rm int}$ |",
              "|---|---|---|---|"]
    for row in energy_rows:
        finite.append(f"| {row['x']:g} | {row['L_E']:.8f} | {row['c_eff']:.8f} | {row['R_E_DD']:.8f} |")
    regulator = ["| Regulator a | Subtracted sum | Limit |", "|---|---|---|"]
    for row in regulator_rows:
        regulator.append(f"| {row['a']:g} | {row['subtracted_sum']:.10f} | {row['limit']:.10f} |")
    for name, lines in (("masses", masses), ("casimir", finite), ("regulator", regulator)):
        (RESULTS / f"{name}_table.md").write_text("\n".join(lines)+"\n")
    failures = [r for r in CHECKS if not r["passed"]]
    report = [f"{len(CHECKS)-len(failures)}/{len(CHECKS)} author checks passed.",
              "Reflection matrix eigenvalues: "+str(reflection),
              "Coupling-dependent scalar vacuum shift: "+expression, ""]
    report += [("PASS " if r["passed"] else "FAIL ")+r["name"] for r in CHECKS]
    (RESULTS / "thickness88.txt").write_text("\n".join(report)+"\n")
    (RESULTS / "environment.txt").write_text(
        "Python "+platform.python_version()+"\n"+
        "\n".join(f"{mod.__name__} {mod.__version__}" for mod in
                  (np, scipy, sp, mp, matplotlib))+"\n")
    print("\n".join(report[:3]))
    if failures:
        raise SystemExit("Failed checks: "+", ".join(r["name"] for r in failures))


if __name__ == "__main__":
    main()
