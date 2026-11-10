#!/usr/bin/env python3
"""Exact check of kaufman_lnZ (ising_twist.py): the four partition functions of
small two-dimensional Ising tori, periodic or antiperiodic in each direction,
by direct enumeration of all spin configurations. Writes ../results/checks82.txt."""
import os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from ising_twist import kaufman_lnZ


def brute(M, N, K, aM, aN):
    n = M * N
    tot = 0.0
    for bits in range(1 << n):
        s = np.array([(bits >> i) & 1 for i in range(n)]).reshape(M, N) * 2 - 1
        e = 0
        for i in range(M):
            for j in range(N):
                sm = s[(i + 1) % M, j] * (-1 if (aM and i == M - 1) else 1)
                sn = s[i, (j + 1) % N] * (-1 if (aN and j == N - 1) else 1)
                e += s[i, j] * (sm + sn)
        tot += np.exp(K * e)
    return np.log(tot)


lines, worst = [], 0.0
for (M, N) in ((3, 4), (4, 3), (4, 4), (2, 5), (3, 3)):
    for K in (0.3, 0.4407, 0.6):
        kf = kaufman_lnZ(M, N, K)
        for key, (aM, aN) in (("pp", (0, 0)), ("ap", (1, 0)), ("pa", (0, 1)), ("aa", (1, 1))):
            worst = max(worst, abs(brute(M, N, K, aM, aN) - kf[key]))
lines.append(f"kaufman_lnZ against enumeration, five tori, three couplings, four boundary conditions: largest difference {worst:.1e}")
print("\n".join(lines))
open(os.path.join(HERE, "..", "results", "checks82.txt"), "w").write("\n".join(lines) + "\n")
