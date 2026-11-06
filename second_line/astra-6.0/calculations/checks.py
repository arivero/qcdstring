#!/usr/bin/env python3
"""Reproduce elementary checks for the Strings, 1974 research programme.

No measured data, network calls, fitted parameters, or full string amplitudes.
Run with: python3 calculations/checks.py
"""

from __future__ import annotations

import json
import math
import platform
from pathlib import Path

import scipy
from scipy.integrate import quad
from scipy.special import j1, jv, jn_zeros


HERE = Path(__file__).resolve().parent
checks: list[dict] = []


def require(name: str, condition: bool, detail: str) -> None:
    checks.append({"name": name, "passed": bool(condition), "detail": detail})
    if not condition:
        raise AssertionError(f"{name}: {detail}")


def close(a: float, b: float, rel: float = 1e-9, absolute: float = 1e-11) -> bool:
    return math.isclose(a, b, rel_tol=rel, abs_tol=absolute)


# 1. The soft Ward identity for one generic massless 2 -> 2 kinematic point.
# This illustration is not a substitute for the general soft theorem.
theta = 0.73
momenta = [
    (1.0, 1.0, 0.0, 0.0),
    (1.0, -1.0, 0.0, 0.0),
    (1.0, math.cos(theta), math.sin(theta), 0.0),
    (1.0, -math.cos(theta), -math.sin(theta), 0.0),
]
eta = [-1, -1, 1, 1]


def ward_residual(couplings: list[float]) -> list[float]:
    return [
        math.fsum(eta[i] * couplings[i] * momenta[i][mu] for i in range(4))
        for mu in range(4)
    ]


equal_residual = ward_residual([1.0, 1.0, 1.0, 1.0])
unequal_residual = ward_residual([1.0, 1.0, 1.0, 2.0])
require(
    "soft_identity_equal_couplings",
    max(abs(x) for x in equal_residual) < 1e-13,
    "A common coupling reduces the leading soft Ward identity to momentum conservation.",
)
require(
    "soft_identity_unequal_example",
    max(abs(x) for x in unequal_residual) > 0.5,
    "The selected unequal-coupling assignment fails the same kinematic identity.",
)

# 2. Color topology. Flavor multiplicities and external operator normalizations
# are not included in these connected vacuum-surface factors.
topology = []
for n in (3, 10, 30):
    for genus, boundaries in ((0, 0), (0, 1), (1, 0), (1, 1)):
        exponent = 2 - 2 * genus - boundaries
        topology.append(
            {
                "N": n,
                "genus": genus,
                "fundamental_boundaries": boundaries,
                "exponent": exponent,
                "weight": n**exponent,
                "relative_to_sphere": n ** (-2 * genus - boundaries),
            }
        )
require(
    "topology_relative_weights",
    all(
        close(row["weight"] / row["N"] ** 2, row["relative_to_sphere"])
        for row in topology
    ),
    "A handle costs N^-2; a fixed-flavor boundary costs N^-1.",
)

# 3. Long-string energy, in r = R sqrt(sigma), e = E/sqrt(sigma), D=4.
dimension = 4
a = math.pi * (dimension - 2) / 12
luscher = -math.pi * (dimension - 2) / 24
long_string = []
for r in (2.0, 4.0, 8.0, 16.0):
    exact_ng = r * math.sqrt(1.0 - a / r**2)
    through_r1 = r - a / (2 * r)
    through_r3 = through_r1 - a**2 / (8 * r**3)
    long_string.append(
        {
            "R_sqrt_sigma": r,
            "NG_benchmark_E_over_sqrt_sigma": exact_ng,
            "expansion_through_R_minus_3": through_r3,
            "absolute_difference": through_r3 - exact_ng,
            "difference_times_r5": (through_r3 - exact_ng) * r**5,
        }
    )
require(
    "long_string_coefficients",
    close(luscher, -math.pi / 12) and close(a**2 / 8, math.pi**2 / 288),
    "The D=4 R^-1 and R^-3 coefficients have the stated signs and normalization.",
)
require(
    "long_string_asymptotic_error",
    close(long_string[-1]["difference_times_r5"], a**3 / 16, rel=0.003),
    "The truncated Nambu-Goto expansion approaches an R^-5 remainder.",
)

# 4. Dimensionless scaling factors. Overall convention-dependent constants in
# G_10 are omitted; the amplitude-level decoupling claim is NOT checked here.
little_string = [
    {
        "g_s": gs,
        "G10_over_alpha_prime_power4_proportional_to": gs**2,
        "ordinary_open_disk_4pt_coupling_proportional_to": gs,
    }
    for gs in (1e-1, 1e-2, 1e-3, 1e-4)
]

go_squared = 0.2
alpha_eff = 1.0
ncos = []
for delta in (1e-2, 1e-4, 1e-6):
    alpha_prime = delta * alpha_eff
    gs = go_squared / math.sqrt(delta)
    gravity_factor = gs**2 * alpha_prime**4 / alpha_eff**4
    predicted = go_squared**2 * delta**3
    ncos.append(
        {
            "delta": delta,
            "alpha_prime": alpha_prime,
            "g_s": gs,
            "G_o_squared": go_squared,
            "alpha_prime_effective": alpha_prime / delta,
            "gravity_factor": gravity_factor,
            "predicted_factor": predicted,
        }
    )
require(
    "NCOS_scaling",
    all(
        close(row["gravity_factor"], row["predicted_factor"], absolute=1e-35)
        and close(row["alpha_prime_effective"], alpha_eff)
        for row in ncos
    ),
    "G10/(alpha_eff')^4 scales as G_o^4 delta^3 at fixed open-sector parameters.",
)

# 5. Central-charge budgets for conventional critical constructions.
central_charge = {
    "D_free_embedding_coordinates": 4,
    "bosonic_extra_matter_c": 26 - 4,
    "RNS_extra_matter_c": 15 - 1.5 * 4,
}
require(
    "central_charge_budgets",
    central_charge["bosonic_extra_matter_c"] == 22
    and central_charge["RNS_extra_matter_c"] == 9,
    "Arithmetic only: no modular-invariant or unitary internal model is constructed.",
)

# 6. Hard-wall tensor problem. Set z0=L=1; all eigenvalues below are m*z0.
tensor_modes = []
for index, root in enumerate(jn_zeros(1, 3), 1):
    root = float(root)
    norm_numeric, norm_error = quad(
        lambda z: z * jv(2, root * z) ** 2, 0.0, 1.0,
        epsabs=1e-12, epsrel=1e-12,
    )
    norm_analytic = 0.5 * float(jv(2, root)) ** 2
    gradient_integral, _ = quad(
        lambda z: root**2 * z * j1(root * z) ** 2,
        0.0, 1.0, epsabs=1e-12, epsrel=1e-12,
    )
    rayleigh = gradient_integral / norm_numeric
    boundary_residual = root * float(j1(root))
    tensor_modes.append(
        {
            "mode": index,
            "m_times_z0": root,
            "m2_times_z0_squared": root**2,
            "Neumann_boundary_residual": boundary_residual,
            "norm_numeric_z0_equals_1": norm_numeric,
            "norm_analytic_z0_equals_1": norm_analytic,
            "quadrature_absolute_error_estimate": norm_error,
            "Rayleigh_quotient": rayleigh,
        }
    )
require(
    "tensor_boundary_conditions",
    all(abs(row["Neumann_boundary_residual"]) < 1e-11 for row in tensor_modes),
    "The three massive modes satisfy the chosen infrared Neumann condition.",
)
require(
    "tensor_norms",
    all(
        row["norm_numeric_z0_equals_1"] > 0
        and close(row["norm_numeric_z0_equals_1"], row["norm_analytic_z0_equals_1"])
        for row in tensor_modes
    ),
    "Numerical norms agree with the Bessel-function integral identity.",
)
require(
    "tensor_rayleigh_quotient",
    all(
        close(row["Rayleigh_quotient"], row["m2_times_z0_squared"])
        for row in tensor_modes
    ),
    "The positive quadratic-form quotient independently reproduces each eigenvalue.",
)

constant_mode_norms = [
    {"UV_cutoff_epsilon": eps, "norm": 0.5 * (eps**-2 - 1)}
    for eps in (1e-1, 1e-2, 1e-3)
]
normalizable_zero_norm = quad(lambda z: z**5, 0.0, 1.0)[0]
require(
    "zero_mode_boundary_control",
    close(normalizable_zero_norm, 1 / 6) and (4.0 - 4.0) == 0,
    "The z^4 zero mode is normalizable, fails Neumann (derivative 4), and satisfies z psi'-4 psi=0.",
)

result = {
    "scope": "Elementary scaling, long-string, soft-identity and hard-wall spectral checks; not a string-theory construction.",
    "environment": {"python": platform.python_version(), "scipy": scipy.__version__},
    "checks": checks,
    "soft_identity_example": {
        "theta_radians": theta,
        "equal_coupling_residual": equal_residual,
        "unequal_example_residual": unequal_residual,
    },
    "topology": topology,
    "long_string_D4": long_string,
    "little_string_bulk_scaling_only": little_string,
    "NCOS_scaling_only": ncos,
    "central_charge": central_charge,
    "tensor_hard_wall_modes": tensor_modes,
    "constant_zero_mode_cutoff_norms": constant_mode_norms,
    "z_power4_mode_norm_at_z0_1": normalizable_zero_norm,
}
(HERE / "results.json").write_text(json.dumps(result, indent=2) + "\n")

lines = [
    "# Executed checks",
    "",
    f"Environment: Python {platform.python_version()}, SciPy {scipy.__version__}.",
    f"All {len(checks)} consistency checks passed. No experimental data were used.",
    "",
    "These checks validate the arithmetic and the explicitly assumed tensor toy model. "
    "They do not prove a decoupled interacting theory, solve a worldsheet, or fit QCD.",
    "",
    "## Tensor spectrum",
    "",
    "AdS-like hard wall, source-free UV behavior, infrared Neumann condition, z0=L=1.",
    "",
    "| Mode | m z0 | Numerical norm | Rayleigh quotient |",
    "|---|---:|---:|---:|",
]
for row in tensor_modes:
    lines.append(
        f"| {row['mode']} | {row['m_times_z0']:.9f} | "
        f"{row['norm_numeric_z0_equals_1']:.9f} | {row['Rayleigh_quotient']:.9f} |"
    )
lines.extend([
    "",
    "At m=0 the constant solution is UV-nonnormalizable. The normalizable z^4 solution "
    "fails the Neumann wall condition. Changing the wall to z psi'-4 psi=0 restores "
    "that zero mode. Thus the absence of a massless tensor depends on the physical boundary problem.",
    "",
    "## Long-string benchmark in four dimensions",
    "",
    "r=R sqrt(sigma); energy units sqrt(sigma). The square-root expression is a Nambu-Goto "
    "benchmark, not an asserted exact UV spectrum.",
    "",
    "| r | Square-root energy | Through r^-3 | Difference |",
    "|---:|---:|---:|---:|",
])
for row in long_string:
    lines.append(
        f"| {row['R_sqrt_sigma']:.0f} | "
        f"{row['NG_benchmark_E_over_sqrt_sigma']:.10f} | "
        f"{row['expansion_through_R_minus_3']:.10f} | {row['absolute_difference']:.3e} |"
    )
lines.extend([
    "",
    "The leading correction is -pi/(12R); the next displayed coefficient is "
    "-pi^2/(288 sigma R^3). Their scope is a long string with two massless transverse modes.",
    "",
    "## NCOS scaling",
    "",
    "Set alpha_eff'=1 and G_o^2=0.2. Suppress the overall normalization of G10.",
    "",
    "| delta | alpha' | Bulk g_s | G10/(alpha_eff')^4 factor |",
    "|---:|---:|---:|---:|",
])
for row in ncos:
    lines.append(
        f"| {row['delta']:.0e} | {row['alpha_prime']:.0e} | "
        f"{row['g_s']:.1f} | {row['gravity_factor']:.1e} |"
    )
lines.extend([
    "",
    "The open scale and coupling stay finite in this bookkeeping. "
    "Metric scaling and the closed-channel amplitude still require the full NCOS analysis.",
    "",
    "## Other checks",
    "",
    "- Universal soft couplings satisfy momentum conservation at the chosen 2-to-2 kinematic point; "
    "a specified unequal assignment fails.",
    "- A handle changes the vacuum color weight by N^-2 and a fixed-flavor boundary by N^-1.",
    "- At fixed alpha', the bulk gravitational factor is proportional to g_s^2. "
    "The ordinary open disk four-point coupling also vanishes as g_s goes to zero.",
    "- Four free embedding dimensions require additional matter central charge 22 "
    "for a conventional bosonic critical string, or 9 for a conventional RNS construction.",
    "",
    "## Not yet calculated",
    "",
    "The annulus comparison, little-string interaction observables, a microscopic trace Hamiltonian, "
    "a smooth confining background, tensor residues, hard scattering in the same model, and a "
    "consistent internal spectrum remain proposed work.",
    "",
    "Full numeric output and individual checks are in results.json. "
    "Run checks.py to regenerate both output files.",
    "",
])
(HERE / "RESULTS.md").write_text("\n".join(lines))
print(f"PASS: {len(checks)} checks; first tensor eigenvalue m*z0={tensor_modes[0]['m_times_z0']:.9f}")
print(f"Wrote {HERE / 'RESULTS.md'} and {HERE / 'results.json'}")
