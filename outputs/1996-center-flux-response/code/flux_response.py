"""Period, charge and screening checks for QCDS-96/1 (Lambda = 1)."""
import heapq
import json
from itertools import combinations
from math import pi, sqrt

import numpy as np
from numpy.polynomial import Polynomial


def characteristic(rank):
    x = Polynomial([0.0, 1.0])
    previous, current = Polynomial([2.0]), x
    for _ in range(2, rank + 1):
        previous, current = current, x * current - previous
    return current


def period_jacobian(rank, step, points=128, radius_fraction=0.32):
    """Integrate the original differential on both sides of each perturbation."""
    polynomial = characteristic(rank)
    q = polynomial.deriv() / rank
    nodes = np.sort(q.roots())[::-1]
    landmarks = np.r_[2.0, nodes, -2.0]
    jacobian = np.empty((rank - 1, rank - 1), dtype=complex)
    phases = np.exp(2j * pi * np.arange(points) / points)
    for row, center in enumerate(nodes):
        radius = radius_fraction * min(landmarks[row] - center, center - landmarks[row + 2])
        dz_over_i = radius * phases
        z = center + dz_over_i
        base_p = polynomial(z)
        base_dp = polynomial.deriv()(z)
        base_y = 1j * np.sqrt(2 - z) * np.sqrt(2 + z) * q(z)
        for col, degree in enumerate(range(rank - 2, -1, -1)):
            monomial = z ** degree
            derivative = degree * z ** (degree - 1) if degree else 0
            periods = []
            for shift in (step, -step):
                change = shift * monomial
                radicand = change * (2 * base_p + change) / base_y ** 2
                if np.max(np.abs(radicand)) >= 0.8:
                    raise ValueError("Contour too close to the moved branch points")
                y = base_y * np.sqrt(1 + radicand)
                periods.append(np.mean(z * (base_dp + shift * derivative) * dz_over_i / y))
            jacobian[row, col] = (periods[0] - periods[1]) / (2 * step)
    return jacobian


def period_check(rank, step, points=128, radius_fraction=0.32):
    jacobian = period_jacobian(rank, step, points, radius_fraction)
    du2 = np.zeros(rank - 1)
    du4 = np.zeros(rank - 1)
    du2[0] = -1
    du4[0], du4[2] = characteristic(rank).coef[rank - 2], -1
    g2 = np.linalg.solve(jacobian.T, du2)
    g4 = np.linalg.solve(jacobian.T, du4)
    angles = np.arange(1, rank) * pi / rank
    target = 2j * np.sin(angles)
    h = g4 / g2
    return {
        "N": rank, "step": step, "points": points, "radius_fraction": radius_fraction,
        "max_abs_du2_error": float(np.max(np.abs(g2 - target))),
        "max_abs_quartic_ratio_error": float(np.max(np.abs(h - (2 + 4 * np.cos(angles) ** 2)))),
        "max_abs_du2_real": float(np.max(np.abs(g2.real))),
        "max_abs_quartic_ratio_imag": float(np.max(np.abs(h.imag))),
        "du2_imaginary": g2.imag.tolist(),
        "du4_over_du2_real": h.real.tolist(),
    }


def center_minima(weights):
    """Shortest paths using positive vortex costs in either orientation."""
    rank = len(weights) + 1
    cost = [float("inf")] * rank
    cost[0] = 0.0
    queue = [(0.0, 0)]
    while queue:
        previous, sector = heapq.heappop(queue)
        if previous > cost[sector]:
            continue
        for index, weight in enumerate(weights, 1):
            for direction in (1, -1):
                neighbor = (sector + direction * index) % rank
                candidate = previous + weight
                if candidate < cost[neighbor]:
                    cost[neighbor] = candidate
                    heapq.heappush(queue, (candidate, neighbor))
    return cost


def wedge_weights(rank, order):
    colors = np.eye(rank, dtype=int)
    result = []
    for indices in combinations(range(rank), order):
        occupancy = np.sum(colors[list(indices)], axis=0)
        flux = occupancy[:-1] - occupancy[1:]
        result.append({"colors": [i + 1 for i in indices], "flux": flux.tolist()})
    return result


def evaluate():
    convergence = [period_check(4, h) for h in (0.01, 0.003, 0.001, 0.0003, 0.0001)]
    variants = [period_check(4, 0.0001, 64, 0.27), period_check(4, 0.0001, 256, 0.39)]
    rank_checks = [period_check(n, 0.00001) for n in (4, 5, 6, 8)]
    su4 = rank_checks[0]
    g2 = np.array(su4["du2_imaginary"])
    g4 = g2 * np.array(su4["du4_over_du2_real"])
    samples = []
    for t in (-1/6, -1/8, -0.11, -0.10, 0, 0.05, 1/8):
        weights = np.abs(g2 + t * g4)
        center = center_minima(weights)
        samples.append({
            "t": round(t, 9), "elementary_ratio": round(weights[1] / weights[0], 8),
            "screened_ratio": round(center[2] / center[1], 8),
            "two_minus_elementary": round(2 - weights[1] / weights[0], 8)
        })
    crossing = float((2 * g2[0] - g2[1]) / (g4[1] - 2 * g4[0]))
    slope = float(g4[1] / g2[1] - g4[0] / g2[0])
    ranks = []
    for n in (4, 5, 6, 8, 12):
        sines = np.sin(np.arange(1, n) * pi / n)
        ratios = np.array(center_minima(sines))[1:] / sines[0]
        ranks.append({"N": n, "quadratic_center_ratios": np.round(ratios, 7).tolist()})
        assert np.max(np.abs(ratios - sines / sines[0])) < 1e-12
    for row in rank_checks:
        assert row["max_abs_quartic_ratio_error"] < 2e-6
        assert row["max_abs_du2_error"] < 2e-6
    assert abs(crossing - (sqrt(2) - 2) / (8 - 2 * sqrt(2))) < 1e-8
    assert abs(slope + 2) < 1e-8
    for row in samples:
        t = row["t"]
        assert abs(row["screened_ratio"] - min(2, sqrt(2)*(1+2*t)/(1+4*t))) < 1e-7
    return {
        "period_convergence": convergence, "contour_variations": variants, "rank_checks": rank_checks,
        "su4_wedge_two": wedge_weights(4, 2), "su4_source_scan": samples,
        "screening_crossing": round(crossing, 9), "logarithmic_slope": round(slope, 9),
        "quadratic_graph": ranks
    }


if __name__ == "__main__":
    print(json.dumps(evaluate(), indent=2, allow_nan=False))
