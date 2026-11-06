#!/usr/bin/env python3
"""Witten D4 tensor benchmark and free-worldsheet finite-size controls.

No experimental inputs. The D4 model has unwanted KK states and is not a
controlled pure-QCD limit. Supersymmetry breaking is a chosen spin structure.
"""
from __future__ import annotations

import json
import math
from fractions import Fraction
from pathlib import Path

import numpy as np
from scipy.integrate import quad, solve_ivp
from scipy.optimize import brentq

HERE = Path(__file__).resolve().parent


def solutions(lam, eps=1e-6):
    # z=UKK/U, H=z^3 F. UV normalizable branch from a Frobenius series.
    c = [1.]
    for k in range(7):
        previous = (k+1)**2*c[k-2] if k >= 2 else 0.
        c.append((previous-lam*c[k])/((k+1)*(k+4)))
    f = sum(v*eps**i for i, v in enumerate(c))
    fp = sum(i*v*eps**(i-1) for i, v in enumerate(c) if i)
    uv = solve_ivp(
        lambda z, y: [y[1], (-(4-7*z**3)*y[1]-(lam-9*z*z)*y[0])/(z*(1-z**3))],
        (eps, .5), (f, fp), rtol=1e-10, atol=1e-12, dense_output=True)
    # IR regular branch: H=1-lam*delta/3+lam*(lam-3)*delta^2/36+...
    b = lam*(lam-3)/36
    ir = solve_ivp(
        lambda z, y: [y[1], ((2+z**3)*y[1]-lam*y[0])/(z*(1-z**3))],
        (1-eps, .5), (1-lam*eps/3+b*eps**2, lam/3-2*b*eps),
        rtol=1e-10, atol=1e-12, dense_output=True)
    if not (uv.success and ir.success):
        raise RuntimeError('Radial integration failed')
    return uv, ir


def normalizable(uv, z):
    f, fp = uv.sol(z)
    return z**3*f, 3*z*z*f+z**3*fp


def residual(lam, eps):
    uv, ir = solutions(lam, eps)
    h, hp = normalizable(uv, .5)
    k, kp = ir.sol(.5)
    return float(h*kp-hp*k)


roots = []
for eps in (1e-4, 1e-5, 1e-6):
    lam = brentq(lambda x: residual(x, eps), 4., 8., xtol=1e-10)
    roots.append(dict(endpoint_cutoff=eps, radial_eigenvalue=lam,
                      mass_over_MKK=2*math.sqrt(lam)/3,
                      matching_residual=residual(lam, eps)))
assert max(r['radial_eigenvalue'] for r in roots)-min(r['radial_eigenvalue'] for r in roots) < 1e-7

eps = 1e-6
lam = roots[-1]['radial_eigenvalue']
uv, ir = solutions(lam, eps)
scale = normalizable(uv, .5)[0]/ir.sol(.5)[0]


def mode(z):
    return normalizable(uv, z) if z <= .5 else scale*ir.sol(z)


def integrate(func):
    return sum(quad(func, lo, hi, epsabs=1e-12, epsrel=1e-9)[0]
               for lo, hi in ((eps, .5), (.5, 1-eps)))


norm = integrate(lambda z: z**(-3)*mode(z)[0]**2)
gradient = integrate(lambda z: (z**(-2)-z)*mode(z)[1]**2)
# The missing interval adjacent to the regular tip contributes O(eps) to norm.
# Add its leading integral, using H(1)=scale; numerator is O(eps^2).
norm += scale**2*eps
gradient += (lam*scale/3)**2*1.5*eps**2
rayleigh = gradient/norm
assert math.isclose(rayleigh, lam, rel_tol=2e-7)
assert all(mode(float(z))[0] > 0 for z in np.linspace(eps, 1-eps, 1001))

# Open physical transverse EFT, not a covariant critical string partition sum.
# No GSO or fermion-parity projection has been applied to these sectors.
# E_Cas = (pi/R)*coefficient. Each scalar contributes -1/24.
# Each real Majorana: NS -1/48; R +1/24, including ground conformal weight.
casimir = [
    dict(sector='two transverse bosons', coefficient=str(-Fraction(2,24))),
    dict(sector='two bosons + two NS Majoranas', coefficient=str(-Fraction(2,24)-Fraction(2,48))),
    dict(sector='two bosons + two R Majoranas', coefficient=str(-Fraction(2,24)+Fraction(2,24))),
]

result = dict(
    scope='Known smooth confining background; no claim of pure QCD or observed mass prediction.',
    tensor=dict(roots=roots, norm=norm, rayleigh_eigenvalue=rayleigh,
                nodeless_on_sample=True, literature_comparison_4lambda=4*lam),
    supersymmetry=dict(fermion_circle_momentum='(n+1/2)*MKK',
                      boson_circle_momentum='n*MKK',
                      note='Kinematic frequencies; not physical interacting particle masses.'),
    tension=dict(sigma_over_MKK2_per_lambda4=2/(27*math.pi),
                 note='lambda4=g4^2*N; convention g4^2=2*pi*gs*ls*MKK.'),
    worldsheet_casimir=casimir)
(HERE/'spin_susy_results.json').write_text(json.dumps(result, indent=2)+'\n')
lines = ['# Tensor and supersymmetry benchmark', '',
         'The first tensor root is stable under three endpoint cutoffs; the independent Rayleigh quotient agrees; the sampled mode is nodeless.', '',
         '| Endpoint cutoff | Radial eigenvalue | m_tensor / M_KK |', '|---:|---:|---:|']
for r in roots:
    lines.append(f"| {r['endpoint_cutoff']:.0e} | {r['radial_eigenvalue']:.10f} | {r['mass_over_MKK']:.10f} |")
lines += ['', f'Rayleigh eigenvalue: {rayleigh:.10f}.',
          f'In the Brower–Mathur–Tan convention the squared eigenvalue is 4 times ours: {4*lam:.6f}, agreeing with their rounded 22.097.', '',
          'Regularity at the smooth tip and UV normalizability eliminate the zero mode analytically. No hard wall or fitted tensor mass is used.', '',
          'The fermion spin structure on the contractible spatial circle is antiperiodic. Circle frequencies are (n+1/2) M_KK; bosonic frequencies are n M_KK. These are not a calculation of strongly interacting superpartner pole masses.', '',
          'The same metric gives sigma = [2 lambda4/(27 pi)] M_KK^2. The tensor and unwanted KK scales have no parametric separation in the classical-gravity regime.', '',
          '## Free worldsheet discriminator', '',
          'Open interval of length R; two massless transverse scalars. Extra Majoranas, if present, are physical modes. Sector ground energies before projections:', '',
          '| Content | Coefficient of pi/R |', '|---|---:|']
for row in casimir:
    lines.append(f"| {row['sector']} | {row['coefficient']} |")
lines += ['', 'Boundary conditions, projections and masses change this answer. These are analytic free-field controls, not claims about the physical QCD flux-tube spectrum.', '',
          'Derivations: notes/SPIN2_AND_SUPERSYMMETRY.md. Run spin_susy_checks.py to reproduce the numerical calculation.', '']
(HERE/'SPIN_SUSY_RESULTS.md').write_text('\n'.join(lines))
print(f'Tensor m/MKK={roots[-1]["mass_over_MKK"]:.10f}; Rayleigh agreement={abs(rayleigh-lam):.3e}; endpoint stability and nodelessness verified.')
