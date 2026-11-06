#!/usr/bin/env python3
"""Conditional flavour/scale calculations; no particle masses are fitted.

The original checks.py remains independent. Run this script from any directory.
All numerical inputs below are synthetic, except the explicitly rounded,
historically accessible weak/pion scales used for an order-of-magnitude control.
"""
from __future__ import annotations

import json
import math
from fractions import Fraction
from pathlib import Path

import numpy as np
from scipy.integrate import solve_ivp

HERE = Path(__file__).resolve().parent
checks = []


def require(name, condition, scope):
    checks.append(dict(name=name, passed=bool(condition), scope=scope))
    if not condition:
        raise AssertionError(name)


def b(nf):
    return 11 - Fraction(2, 3) * nf


# One Higgs doublet, one nonzero quark Yukawa, SU(3), electroweak couplings
# neglected. All 2*Ng quarks are active; no other colored particles.
a = Fraction(9, 2)
generations = []
for ng in range(1, 10):
    beta = b(2 * ng)
    rstar = (8 - beta) / a
    generations.append(dict(Ng=ng, b3=str(beta), rstar=str(rstar),
                            color_AF=beta > 0, positive_ratio=rstar > 0,
                            both=beta > 0 and rstar > 0))
allowed = [row['Ng'] for row in generations if row['both']]
require('conditional_generation_interval', allowed == list(range(3, 9)),
        'A property of the specified one-loop truncation, not a generation theorem.')
require('three_family_fixed_ratio', (8 - b(6)) / a == Fraction(2, 9),
        'The ratio fixed point differs from the beta_y=0 nullcline r=16/9.')

# Independent differential-equation check of the analytic fixed-ratio flow.
flow = []
for ng in (3, 4, 8):
    beta = float(b(2 * ng))
    c = 8 - beta
    rs = c / float(a)
    g2_uv, g2_ir = 0.25, 1.0
    dt = 8 * math.pi**2 / beta * (1 / g2_ir - 1 / g2_uv)
    for r_uv in (0.05, 0.5, 2.0):
        def rhs(t, z):
            g2, y2 = z
            return [-beta * g2**2 / (8 * math.pi**2),
                    y2 * (float(a) * y2 - 8 * g2) / (8 * math.pi**2)]
        sol = solve_ivp(rhs, (0, dt), (g2_uv, r_uv * g2_uv),
                        rtol=2e-11, atol=1e-13)
        r_num = sol.y[1, -1] / sol.y[0, -1]
        r_exact = rs / (1 - (1 - rs / r_uv) * (g2_ir / g2_uv)**(-c / beta))
        require(f'RG_flow_Ng{ng}_r{r_uv}', sol.success and
                math.isclose(sol.y[0, -1], g2_ir, rel_tol=1e-9) and
                math.isclose(r_num, r_exact, rel_tol=2e-9) and
                abs(r_num-rs) < abs(r_uv-rs),
                'Numerical coupled beta functions agree with the analytic solution and IR attraction.')
        flow.append(dict(Ng=ng, r_uv=r_uv, r_ir=r_num, rstar=rs,
                         g2_uv=g2_uv, g2_ir=g2_ir, log_mu_ratio=dt))

# Rank-one hierarchy: singular values, not matrix entries or eigenvalues.
rng = np.random.default_rng(1974)
rank_examples = []
for n in (2, 3, 4):
    u = rng.normal(size=n); u /= np.linalg.norm(u)
    v = rng.normal(size=n); v /= np.linalg.norm(v)
    y0 = np.outer(u, v)
    delta = rng.normal(size=(n, n)); delta /= np.linalg.norm(delta, 2)
    eps = 0.001
    sv = np.linalg.svd(y0 + eps * delta, compute_uv=False)
    zleft = np.diag(np.linspace(0.7, 2, n))
    zright = np.diag(np.linspace(0.8, 3, n))
    normalized_rank = np.linalg.matrix_rank(zleft @ y0 @ zright, tol=1e-12)
    require(f'rank_hierarchy_n{n}', sv[1] <= eps + 1e-12 and
            abs(sv[0] - 1) <= eps + 1e-12 and normalized_rank == 1,
            'Weyl singular-value bound and rank preservation under invertible normalization.')
    rank_examples.append(dict(matrix_size=n, epsilon=eps, singular_values=sv.tolist()))

# A positive flux-charge budget gives a bound on a linear chiral index.
# Pure linear algebra: this is NOT an actual compactification.
q = np.diag([2., 8.]); ell = np.array([1., 2.]); budget = 12.
continuous_bound = math.sqrt(2 * budget * (ell @ np.linalg.solve(q, ell)))
points = [(i, j) for i in range(-4, 5) for j in range(-2, 3)
          if 2*i*i + 8*j*j <= 2*budget]
integer_max = max(abs(i+2*j) for i, j in points)
require('flux_index_bound', integer_max == 4 and integer_max <= continuous_bound,
        'Exhaustive integer enumeration within a positive quadratic budget agrees with Cauchy-Schwarz.')
degeneration = [dict(eta=eta, max_abs_index=math.floor(math.sqrt(2) / eta))
                for eta in (1., .1, .01)]
require('nonuniform_flux_bound', [x['max_abs_index'] for x in degeneration] == [1, 14, 141],
        'Q=diag(eta^2,1), L=1, index=n1: a degenerating metric can remove a uniform bound.')

# Threshold matching: continuity of one-loop alpha_s at mu=m_h.
# Synthetic units, Lambda_6 fixed. Ordered heavy masses remain above Lambda_3.
def match_one(lambda_hi, nf_hi, mass):
    return math.exp((float(b(nf_hi))*math.log(lambda_hi) +
                     (float(b(nf_hi-1))-float(b(nf_hi)))*math.log(mass)) /
                    float(b(nf_hi-1)))


lambda6 = 0.01
heavy = [10., 2., 0.5]  # t, b, c in arbitrary common units
lambda_low = lambda6
for nf, mass in zip((6, 5, 4), heavy):
    next_lambda = match_one(lambda_low, nf, mass)
    require(f'threshold_continuity_{nf}_to_{nf-1}',
            math.isclose(float(b(nf))*math.log(mass/lambda_low),
                         float(b(nf-1))*math.log(mass/next_lambda), rel_tol=1e-12),
            'Inverse couplings match continuously at the selected threshold.')
    lambda_low = next_lambda
lambda3_exact = lambda6**(7/9) * math.prod(heavy)**(2/27)
require('three_threshold_formula', math.isclose(lambda_low, lambda3_exact, rel_tol=1e-12),
        'Sequential matching reproduces Lambda3=Lambda6^(7/9)*(mt*mb*mc)^(2/27).')


def low_scale(masses):
    value = lambda6
    for nf, mass in zip((6, 5, 4), masses):
        value = match_one(value, nf, mass)
    return value


h = 1e-4
top_slope = (math.log(low_scale([heavy[0]*math.exp(h), *heavy[1:]])) -
             math.log(low_scale([heavy[0]*math.exp(-h), *heavy[1:]]))) / (2*h)
all_slope = (math.log(low_scale([m*math.exp(h) for m in heavy])) -
             math.log(low_scale([m*math.exp(-h) for m in heavy]))) / (2*h)
require('threshold_sensitivities', math.isclose(top_slope, 2/27, rel_tol=1e-8) and
        math.isclose(all_slope, 2/9, rel_tol=1e-8),
        'Fixed high-scale coupling and reference scale; threshold ordering unchanged.')

# The no-threshold transmutation example is deliberately separate from matching.
# alpha_s(M)=0.12 is a synthetic input, not a measured value or a prediction.
alpha = 0.12
ratio = math.exp(2*math.pi/(7*alpha))
sensitivity = 2*math.pi/(7*alpha)
scale_examples = [dict(alpha_s=al, M_over_Lambda6=math.exp(2*math.pi/(7*al)))
                  for al in (.10, .12, .15)]

# Rounded historically available weak and pion scales, for dimensional control.
weak_v, pion_f = 246., .093
required_doublets = (weak_v/pion_f)**2
qcd_only_max_v = math.sqrt(8)*pion_f
require('ordinary_QCD_control', required_doublets > 1e6 and qcd_only_max_v < 0.3,
        'Equal QCD-sized decay constants assumed; extra strong sectors are not covered.')

result = dict(scope='Conditional EFT and algebraic controls, not a string vacuum or mass prediction.',
              checks=checks, generations=generations, RG_flow=flow, rank_examples=rank_examples,
              flux_toy=dict(Q=q.tolist(), ell=ell.tolist(), L=budget,
                            continuous_bound=continuous_bound, integer_max=integer_max,
                            degeneration=degeneration),
              thresholds=dict(lambda6=lambda6, masses=heavy, lambda3=lambda_low,
                              dlogLambda3_dlogmt=top_slope, dlogLambda3_dlogv=all_slope,
                              top_mass_factor10_changes_Lambda3_by=10**(2/27)),
              transmutation=dict(examples=scale_examples, sensitivity_at_alpha012=sensitivity),
              QCD_chiral_control=dict(v_GeV=weak_v, fpi_GeV=pion_f,
                                     required_equal_doublets=required_doublets,
                                     max_v_GeV_for_eight_equal_doublets=qcd_only_max_v))
(HERE/'flavour_results.json').write_text(json.dumps(result, indent=2)+'\n')

lines = ['# Flavour and scale calculations', '',
         f'{len(checks)} checks passed. No future particle mass or observed generation count was fitted.', '',
         'These calculations test stated effective theories and algebraic toys. They do not construct a string vacuum.', '',
         '## Generation-dependent gauge–Yukawa flow', '',
         'One Higgs doublet; one nonzero quark Yukawa; electroweak couplings neglected; all 2Ng quarks active.', '',
         '| Ng | b3 | Fixed ratio y²/g3² | Color AF and positive ratio? |',
         '|---:|---:|---:|---|']
for row in generations:
    lines.append(f"| {row['Ng']} | {row['b3']} | {row['rstar']} | {'yes' if row['both'] else 'no'} |")
lines += ['', 'The allowed integers are 3–8 in this truncation. Three is the smallest, not the unique solution.', '',
          '### Finite running at Ng=3', '',
          'Synthetic g3² grows from 0.25 to 1. The fixed ratio is 2/9. Attraction is incomplete.', '',
          '| UV ratio | IR ratio |', '|---:|---:|']
for row in flow:
    if row['Ng'] == 3:
        lines.append(f"| {row['r_uv']:.4f} | {row['r_ir']:.6f} |")
lines += ['', '## One large Yukawa', '',
          'For a normalized rank-one matrix plus a perturbation of operator norm 0.001:', '',
          '| Matrix size | Singular values, decreasing |', '|---:|---|']
for row in rank_examples:
    lines.append(f"| {row['matrix_size']} | {', '.join(f'{x:.8g}' for x in row['singular_values'])} |")
lines += ['', 'The mechanism works with two, three or four families; it does not choose their number.', '',
          '## Flux budget toy', '',
          f'For Q=diag(2,8), L=12 and index n1+2n2, the continuous bound is {continuous_bound:.6f}; integer enumeration gives maximum 4.',
          'For Q=diag(eta²,1), L=1 and index n1, eta=1, 0.1, 0.01 permits maximum |index|=1, 14, 141. A bound need not remain uniform in a limit.', '',
          '## QCD thresholds', '',
          f'Synthetic Lambda6={lambda6}; heavy masses={heavy}; Lambda3={lambda_low:.9f}.',
          f'd ln Lambda3 / d ln mt = {top_slope:.9f} = 2/27 at fixed high-scale coupling.',
          f'd ln Lambda3 / d ln v = {all_slope:.9f} = 2/9 when all three heavy thresholds scale with v at fixed Yukawas.',
          f'A factor ten change of mt changes Lambda3 by {10**(2/27):.6f}. This does not lock the scales.', '',
          '## Transmutation sensitivity', '',
          'Six-flavour, one-loop running without threshold matching; alpha_s is a chosen input.', '',
          '| alpha_s(M) | M/Lambda6 |', '|---:|---:|']
for row in scale_examples:
    lines.append(f"| {row['alpha_s']:.2f} | {row['M_over_Lambda6']:.6f} |")
lines += ['', f'At alpha_s=0.12 the logarithmic sensitivity to alpha_s is {sensitivity:.6f}.', '',
          '## Ordinary-QCD weak-scale control', '',
          f'Using rounded v=246 GeV and fpi=0.093 GeV gives {required_doublets:.0f} equal QCD-sized doublets to supply v.',
          f'Even eight such doublets give only {qcd_only_max_v:.6f} GeV. The equal-decay-constant assumption is an illustration, not a prediction for many-flavour QCD.', '',
          'The derivations, assumptions and proposed string tests are in notes/FLAVOUR_AND_SCALES.md and SUCCESS_CRITERIA.md.', '']
(HERE/'FLAVOUR_RESULTS.md').write_text('\n'.join(lines))
print(f'PASS: {len(checks)} flavour/scale checks; conditional Ng interval={allowed}; flux toy maximum={integer_max}')
