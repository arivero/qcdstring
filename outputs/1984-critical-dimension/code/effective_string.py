#!/usr/bin/env python3
"""Symbolic and numerical work behind the derivations in the 1984 paper.
Writes ../results/effective_string.txt. Runs in seconds (sympy, numpy).
Parts A-E, G, H and I check a derivation; part F evaluates formulas (11), (12).

A. The area action in static gauge to fourth order, and the flat-sheet argument.
   The quartic term is 2 sigma (d+X.d+X)(d-X.d-X); first-order level shifts.
B. The stiffness term is a total derivative plus equations of motion.
C. Scalar curvature of the induced metric to second order in the displacement.
D. Four-phonon amplitude of the area action: a pure phase, 2 delta = s/4 sigma.
E. Phonons on a string whose length depends on its state: the square roots.
F. Polyakov's anomaly on the induced metric: the six-derivative vertex, its
   amplitude, its absence for one transverse direction, the level shifts.
G. End terms: regulated mode sums and the shifts of ground state and phonons.
H. Central term of the long string in conformal gauge, derived from the action
   (9) on the induced metric: Noether tensor, propagator, and their sum 12 beta.
I. Casimir energy of a massive scalar on a circle.
"""
import itertools, math, os
import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
out = []
def say(s=""):
    out.append(s); print(s)

# ---------------------------------------------------------------------------------------- A
say("A. Area action in static gauge")
a, b, eps = sp.symbols("a b epsilon", positive=True)
# X^1 = a t, X^2 = b x (a string tilted in one transverse direction and moving in another):
# induced metric diag(-(1 - a^2), 1 + b^2); area density sqrt((1 - a^2)(1 + b^2))
area = sp.sqrt((1 - eps**2 * a**2) * (1 + eps**2 * b**2))
ser = sp.series(area, eps, 0, 6).removeO()
c2, c3 = sp.symbols("c2 c3")
trM = -a**2 + b**2                       # d_a X . d^a X
trM2 = a**4 + b**4                       # (d_a X . d_b X)(d^a X . d^b X)
# L = -sigma [1 + trM/2] + c2 trM^2 + c3 trM2  must equal  -sigma * area  on every flat sheet
quartic_needed = -sp.expand(ser.coeff(eps, 4))          # in units of sigma
sol = sp.solve(sp.Poly(sp.expand(c2 * trM**2 + c3 * trM2 - quartic_needed), a, b).coeffs(), [c2, c3], dict=True)
say(f"   area density on the flat sheet X1 = a t, X2 = b x: {sp.expand(ser)}")
say(f"   quartic coefficients fixed by flat sheets: c2/sigma = {sol[0][c2]}, c3/sigma = {sol[0][c3]}")
# one transverse direction: trM2 = trM^2, only c2 + c3 enters
say(f"   with one transverse direction only c2 + c3 = {sol[0][c2] + sol[0][c3]} sigma enters")
# the quartic term in light-cone derivatives d+- = (d_t +- d_x)/2, two transverse fields with arbitrary gradients
x1t, x1x, x2t, x2x, sgm = sp.symbols("x1t x1x x2t x2x sigma")
utt, utx, uxx = x1t**2 + x2t**2, x1t * x1x + x2t * x2x, x1x**2 + x2x**2
tr1 = -utt + uxx                          # d_a X . d^a X
tr2 = utt**2 - 2 * utx**2 + uxx**2        # (d_a X . d_b X)(d^a X . d^b X)
upp = ((x1t + x1x) / 2) ** 2 + ((x2t + x2x) / 2) ** 2
umm = ((x1t - x1x) / 2) ** 2 + ((x2t - x2x) / 2) ** 2
L4 = -sgm / 8 * tr1**2 + sgm / 4 * tr2
say(f"   quartic term minus 2 sigma (d+X.d+X)(d-X.d-X): {sp.expand(L4 - 2 * sgm * upp * umm)}")
say(f"   free energy density (sigma/2)(Xdot^2 + X'^2) minus sigma [(d+X)^2 + (d-X)^2]: {sp.expand(sgm / 2 * (utt + uxx) - sgm * (upp + umm))}")
say("   so L_4 = (2/sigma) eps_+ eps_-, the product of the energy densities of the two directions of motion, and a state of a closed")
say("   string with energies E_+ and E_- in the two directions is shifted at first order by -2 E_+ E_- / (sigma L)")
Ep, Em, Lc_, zz = sp.symbols("E_p E_m L zeta", positive=True)
root = sp.sqrt(sgm**2 * Lc_**2 + 2 * sgm * Lc_ * zz * (Ep + Em) + zz**2 * (Ep - Em) ** 2)
ser2 = sp.series(root, zz, 0, 3).removeO()
say(f"   square root (2) with E_+- = 2 pi (N - (d-2)/24)/L, second order in the phonon energies, minus [-2 E_+ E_-/(sigma L)]: "
    f"{sp.simplify(ser2.coeff(zz, 2).subs(sgm, sp.Symbol('sigma', positive=True)) + 2 * Ep * Em / (sp.Symbol('sigma', positive=True) * Lc_))}")

# ---------------------------------------------------------------------------------------- B
say()
say("B. Stiffness term")
t, x = sp.symbols("t x")
X = sp.Function("X")(t, x)
d = {0: lambda f: sp.diff(f, t), 1: lambda f: sp.diff(f, x)}
ddX2 = sum(d[i](d[j](X))**2 for i in (0, 1) for j in (0, 1))          # (d_a d_b X)^2, Euclidean
boxX = sum(d[i](d[i](X)) for i in (0, 1))
J = [sum(d[j](X) * d[i](d[j](X)) for j in (0, 1)) - d[i](X) * boxX for i in (0, 1)]
ident = sp.simplify(ddX2 - boxX**2 - sum(d[i](J[i]) for i in (0, 1)))
say(f"   (d_a d_b X)^2 - (d^2 X)^2 - d_a[d_b X d_a d_b X - d_a X d^2 X] = {ident}")

# ---------------------------------------------------------------------------------------- C
say()
say("C. Curvature of the induced metric h_ab = delta_ab + d_a X d_b X to second order")
e = sp.symbols("e")
Xs = e * X
h = sp.Matrix(2, 2, lambda i, j: (1 if i == j else 0) + d[i](Xs) * d[j](Xs))
hinv = h.inv()
co = [t, x]
Gam = [[[sum(hinv[k, l] * (sp.diff(h[l, i], co[j]) + sp.diff(h[l, j], co[i]) - sp.diff(h[i, j], co[l])) for l in (0, 1)) / 2
         for j in (0, 1)] for i in (0, 1)] for k in (0, 1)]
def riem(k, l, i, j):      # R^k_{l i j}
    r = sp.diff(Gam[k][l][j], co[i]) - sp.diff(Gam[k][l][i], co[j])
    r += sum(Gam[k][i][m] * Gam[m][l][j] - Gam[k][j][m] * Gam[m][l][i] for m in (0, 1))
    return r
Ric = sp.Matrix(2, 2, lambda l, j: sum(riem(k, l, k, j) for k in (0, 1)))
Rs = sum(hinv[i, j] * Ric[i, j] for i in (0, 1) for j in (0, 1))
R2 = sp.simplify(sp.series(sp.simplify(Rs), e, 0, 3).removeO().coeff(e, 2))
say(f"   R at second order minus [(d^2 X)^2 - (d_a d_b X)^2] = {sp.simplify(R2 - (boxX**2 - ddX2))}")
A_ = sum(d[i](X)**2 for i in (0, 1))
onshell = sp.simplify(sum(d[i](d[i](A_)) for i in (0, 1)) - 2 * ddX2 - 2 * sum(d[i](X) * d[i](boxX) for i in (0, 1)))
say(f"   d^2(d_c X d_c X) - 2 (d_a d_b X)^2 - 2 d_c X d_c d^2 X = {onshell}   (so R = -(1/2) d^2 A on shell)")

# ---------------------------------------------------------------------------------------- D, F: amplitudes
def minkowski(p, q):
    return -p[0] * q[0] + p[1] * q[1]


def amplitude(vertex, moms, flav):
    """Sum over the assignments of four external legs to the four fields of a quartic
    vertex. vertex(P, F) returns the product of derivative factors for fields 1..4 carrying
    momenta P (incoming) and flavours F, where fields (1,2) and (3,4) are flavour-contracted."""
    tot = 0
    for perm in itertools.permutations(range(4)):
        P = [moms[i] for i in perm]; F = [flav[i] for i in perm]
        if F[0] == F[1] and F[2] == F[3]:
            tot += vertex(P)
    return tot


def v_c2(P):      # (dX.dX)(dX.dX): each d -> i p; (i)^4 = 1
    return minkowski(P[0], P[1]) * minkowski(P[2], P[3])


def v_c3(P):      # (d_a X^m d_b X^m)(d^a X^n d^b X^n)
    return minkowski(P[0], P[2]) * minkowski(P[1], P[3])


def v_anom(P):    # d_a(dX.dX) d^a(dX.dX): [(-p1.p2)(-p3.p4)] [i(p1+p2)].[i(p3+p4)]
    s12 = (P[0][0] + P[1][0], P[0][1] + P[1][1]); s34 = (P[2][0] + P[3][0], P[2][1] + P[3][1])
    return -minkowski(P[0], P[1]) * minkowski(P[2], P[3]) * minkowski(s12, s34)


say()
say("D. Four-phonon amplitude of the area action (sigma = 1, canonical fields)")
p, q = sp.symbols("p q", positive=True)
p1, p2 = (p, p), (q, -q)                  # right-mover and left-mover, incoming
p3, p4 = (-p, -p), (-q, q)                # outgoing phonons written as incoming
s = -minkowski((p1[0] + p2[0], p1[1] + p2[1]), (p1[0] + p2[0], p1[1] + p2[1]))
say(f"   s = {sp.simplify(s)}")
ng = lambda fl: sp.simplify(amplitude(v_c2, [p1, p2, p3, p4], fl) * sp.Rational(-1, 8) + amplitude(v_c3, [p1, p2, p3, p4], fl) * sp.Rational(1, 4))
T_, A_n, R_ = ng([1, 2, 1, 2]), ng([1, 1, 2, 2]), ng([1, 2, 2, 1])
same = ng([1, 1, 1, 1])
say(f"   transmission (i j -> i j): M = {sp.factor(T_)} = s^2/2;   annihilation (i i -> k k): {A_n};   reflection (i j -> j i): {R_}")
say(f"   one flavour: M = {sp.factor(same)};   phase 2 delta = M/2s = {sp.simplify(T_ / (2 * s))} = s/4")

# ---------------------------------------------------------------------------------------- E
say()
say("E. Phonons on a string lengthened by the momentum of the opposite movers")
rng = np.random.default_rng(84)
worst_c, worst_o, n_c, n_o = 0.0, 0.0, 0, 0
for _ in range(200):
    sig, L = rng.uniform(0.5, 2), rng.uniform(2, 8)
    N, Nb, c = rng.integers(0, 6), rng.integers(0, 6), rng.integers(1, 25)
    al, ar = 2 * math.pi * (N - c / 24), 2 * math.pi * (Nb - c / 24)
    # P (L + Q/sig) = al, Q (L + P/sig) = ar  ->  solve
    # P - Q = (al - ar)/L ; P Q / sig + P L = al
    dPQ = (al - ar) / L
    # Q^2/sig + Q (L + dPQ/sig) + dPQ L - al = 0
    A, B, C = 1 / sig, L + dPQ / sig, dPQ * L - al
    disc = B * B - 4 * A * C
    if disc < 0:
        continue
    Q = (-B + math.sqrt(disc)) / (2 * A); Pm = Q + dPQ
    E = sig * L + Pm + Q
    E2 = sig**2 * L**2 + 4 * math.pi * sig * (N + Nb - c / 12) + (2 * math.pi * (N - Nb) / L) ** 2
    if E2 > 0 and E > 0:
        worst_c = max(worst_c, abs(E - math.sqrt(E2))); n_c += 1
    # open string: P (R + P/2 sig) = pi (N - c/24), E = sig R + P
    al = math.pi * (N - c / 24)
    disc = L * L + 2 * al / sig
    if disc >= 0:
        Po = sig * (-L + math.sqrt(disc))
        Eo2 = sig**2 * L**2 + 2 * math.pi * sig * (N - c / 24)
        worst_o = max(worst_o, abs(sig * L + Po - math.sqrt(Eo2))); n_o += 1
say(f"   closed string, {n_c} of 200 random (sigma, L, N, Nbar, c) with a real level: largest |E - square root (2)| = {worst_c:.1e}")
say(f"   open string,  {n_o} of 200 random (sigma, R, N, c) with a real level:       largest |E - square root of [3]| = {worst_o:.1e}")
Ps, Qs, Ls, sg, al_, ar_ = sp.symbols("P Q L sigma alpha alphabar", positive=True)
Esq = sp.expand((sg * Ls + Ps + Qs) ** 2)
rel = sp.simplify(Esq - (sg**2 * Ls**2 + 2 * sg * (Ps * (Ls + Qs / sg) + Qs * (Ls + Ps / sg)) + (Ps - Qs) ** 2))
say(f"   identity (sigma L + P + Q)^2 = sigma^2 L^2 + 2 sigma [P(L + Q/sigma) + Q(L + P/sigma)] + (P - Q)^2: remainder {rel}")

# ---------------------------------------------------------------------------------------- F
say()
say("F. Polyakov's anomaly on the induced metric (evaluation of (11) and (12))")
kap = sp.symbols("kappa")
an = lambda fl: sp.factor(amplitude(v_anom, [p1, p2, p3, p4], fl))
say("   vertex kappa [d_a (dX.dX)]^2 in the Euclidean action, kappa = (26 - d)/(384 pi sigma^2); L_Minkowski = -kappa d_a A d^a A")
say(f"   sum over assignments of d_a A d^a A: annihilation {an([1, 1, 2, 2])} = -2 s^3;  transmission {an([1, 2, 1, 2])};  reflection {an([1, 2, 2, 1])} = +2 s^3")
say(f"   one flavour: {an([1, 1, 1, 1])}   (the vertex is trivial for one transverse direction)")
say("   amplitude M = +2 kappa s^3 [delta_ij delta_kl - delta_il delta_jk] = (26 - d) s^3/(192 pi sigma^2) [ ... ]")
for dd in (3, 4, 5, 26):
    n = dd - 2
    Mm = np.zeros((n * n, n * n))
    for i, j, kk, l in itertools.product(range(n), repeat=4):
        Mm[i * n + j, kk * n + l] = (i == j) * (kk == l) - (i == l) * (j == kk)
    ev = np.round(np.linalg.eigvalsh(Mm), 10)
    vals, counts = np.unique(ev, return_counts=True)
    say(f"   d = {dd}: eigenvalues of [delta_ij delta_kl - delta_il delta_jk] on the (i, j) states: " + ", ".join(f"{v:+.0f} (x{c_})" for v, c_ in zip(vals, counts)))
coef = sp.Rational(4, 3) * sp.pi**3
say(f"   level shift of N = Nbar = 1 at momenta 2 pi/L: Delta E = -(26 - d) lambda s^2/(192 pi sigma^2 L), s = 16 pi^2/L^2  ->  -(26 - d) lambda ({coef}) /(sigma^2 L^5), 4 pi^3/3 = {float(coef):.3f}")
say("   d = 4 (lambda = +1 scalar, +1 pseudoscalar, -1 for the two spin-2 states), units sqrt(sigma) = 1:")
say("   L sqrt(sigma)   square root (2), N = Nbar = 1   shift of scalar and pseudoscalar   relative   tree phase s/4   anomaly phase")
for Lv in (4, 5, 6, 8, 10, 12):
    Eng = math.sqrt(Lv**2 + 4 * math.pi * (2 - 2 / 12))
    sh = -22 * float(coef) / Lv**5
    sv = 16 * math.pi**2 / Lv**2
    say(f"   {Lv:5.1f}           {Eng:7.3f}                          {sh:+8.4f}                        {sh / Eng * 100:+6.2f}%    {sv / 4:6.3f}          {22 * sv**2 / (384 * math.pi):6.3f}")

# the same level with the phase of (11) added to the quantization rule (8), momenta dressed by the lengthening
say("   with dressed momenta: P (L + P) = 2 pi (1 - 1/12) - lambda 22 s^2/(384 pi), s = 4 p^2, p = 2 pi/(L + P), E = L + 2 P  (units sqrt(sigma) = 1)")
say("   L sqrt(sigma)   first-order shift (12)   shift with dressed momenta, lambda = +1 and -1   ratio to (12)")
from scipy.optimize import brentq as _brentq
for Lv in (5, 6, 8, 10, 12):
    def level(lam):
        fP = lambda P: P * (Lv + P) - 2 * math.pi * (1 - 1 / 12) + lam * 22 * (4 * (2 * math.pi / (Lv + P)) ** 2) ** 2 / (384 * math.pi)
        return Lv + 2 * _brentq(fP, 0.0, 10.0)
    e0_, ep_, em_ = level(0), level(+1), level(-1)
    sh = 22 * float(coef) / Lv**5
    say(f"   {Lv:5.1f}           -+{sh:.4f}                 {ep_ - e0_:+.4f}, {em_ - e0_:+.4f}                              {(e0_ - ep_) / sh:.2f}, {(em_ - e0_) / sh:.2f}")

# ---------------------------------------------------------------------------------------- G
say()
say("G. End terms")
def regulated(power, R=1.0):
    """finite part of sum_n n^power exp(-eps n): the sum minus its divergent part power!/eps^(power+1), at eps = 0.005"""
    vals = []
    for ep in (0.02, 0.01, 0.005):
        n = np.arange(1, int(60 / ep))
        ssum = np.sum(n.astype(float) ** power * np.exp(-ep * n))
        div = math.factorial(power) / ep ** (power + 1)
        vals.append(ssum - div)
    return vals[-1]
say(f"   finite part of sum n   = {regulated(1):+.6f}   (zeta(-1) = -1/12 = {-1/12:+.6f})")
say(f"   finite part of sum n^3 = {regulated(3):+.6f}   (zeta(-3) = 1/120 = {1/120:+.6f})")
say("   boundary Lagrangian b1 (d_x X)^2 at both ends:      ground state +b1 pi (d-2)/(6 sigma R^2) = d1/R^2;  phonon of mode k: -24 k d1/R^2 per transverse direction")
say("   boundary Lagrangian b2 (d_t d_x X)^2 at both ends:  ground state -b2 pi^3 (d-2)/(60 sigma R^4) = e/R^4; phonon of mode k: +240 k^3 e/R^4 per transverse direction")
say("   (ratios: -[4 k pi]/[pi/6] = -24 k and [4 k^3 pi^3]/[pi^3/60] = 240 k^3)")

# ---------------------------------------------------------------------------------------- H
say()
say("H. Central term of the long string in conformal gauge, from the action (9) on the induced metric")
# X = R (e+ u + e- v) + Y, with u, v the light-cone coordinates, e+^2 = e-^2 = 0, e+.e- = -1/2.
# Only the components f = e+.Y and g = e-.Y enter at this order: Y = -2 (g e+ + f e-) + transverse.
u, v, Rr, aa, bet, epsl = sp.symbols("u v R a beta epsilon", positive=True)
f = sp.Function("f")(u, v); g = sp.Function("g")(u, v)
def dot_pm(F1, G1, F2, G2):
    """(F1 e+ + G1 e-) . (F2 e+ + G2 e-) = -(F1 G2 + G1 F2)/2"""
    return -(F1 * G2 + G1 * F2) / 2
cp, cm = Rr * u - 2 * epsl * g, Rr * v - 2 * epsl * f                 # coefficients of e+ and e- in X
h_pm = dot_pm(sp.diff(cp, u), sp.diff(cm, u), sp.diff(cp, v), sp.diff(cm, v))       # d+X . d-X
phi = sp.log(-2 * h_pm)
phi1 = sp.series(phi, epsl, 0, 2).removeO().coeff(epsl, 1)
say(f"   phi = ln(-2 d+X.d-X) at first order: {sp.simplify(phi1)}   [= -(2/R)(e+.d-Y + e-.d+Y)]")
Lag = h_pm / aa**2 + bet * sp.diff(phi, u) * sp.diff(phi, v)          # S = (1/4 pi) int du dv Lag
L2 = sp.expand(sp.series(sp.expand(Lag), epsl, 0, 3).removeO().coeff(epsl, 2))
L2 = sp.expand(sp.simplify(L2))
say(f"   quadratic Lagrangian: {L2}")
# kernel K(k): fields A exp(i theta) + B exp(-i theta), theta = k+ u + k- v; the constant part of L2 is B^T K A
kp, km = sp.symbols("k_p k_m", positive=True)
Af, Ag, Bf, Bg = sp.symbols("A_f A_g B_f B_g")
th = kp * u + km * v
subsd = {f: Af * sp.exp(sp.I * th) + Bf * sp.exp(-sp.I * th), g: Ag * sp.exp(sp.I * th) + Bg * sp.exp(-sp.I * th)}
L2k = sp.expand(L2.subs(subsd).doit())
const = sp.expand(sum(term for term in L2k.as_ordered_terms() if not term.has(u) and not term.has(v)))
K = sp.Matrix(2, 2, lambda i, j: sp.factor(const.coeff([Bf, Bg][i]).coeff([Af, Ag][j])))
say(f"   kernel in the basis (f, g): K_ff = {K[0, 0]},  K_fg = {K[0, 1]},  K_gg = {K[1, 1]}")
# Noether tensor. Under delta X = eps(u, v) d-X the zeroth-order variation is delta f = -eps R/2, delta g = 0, so
# delta S = (1/4 pi) int E_f (-eps R/2) with E_f the Euler-Lagrange expression of f; E_f = d+ W, and with
# delta S = -(1/2 pi) int d+eps T_-- this gives T_-- = -(R/4) W at first order in the fields.
from sympy.calculus.euler import euler_equations
Ef = [eq.lhs for eq in euler_equations(L2, [f, g], [u, v])][0]
plane = {f: Af * sp.exp(sp.I * th), g: Ag * sp.exp(sp.I * th)}
Efk = sp.expand(sp.simplify(Ef.subs(plane).doit() / sp.exp(sp.I * th)))
Wk = sp.expand(Efk / (sp.I * kp))
Tk = sp.expand(-Rr / 4 * Wk)                                           # T_--(k) = t_f A_f + t_g A_g
t_f, t_g = sp.factor(Tk.coeff(Af)), sp.factor(Tk.coeff(Ag))
say(f"   Noether tensor at first order, in momentum space: T = ({t_g}) g + ({t_f}) f")
say("   on shell (k_p = 0 for a function of v): T = -(R/a^2) d-g - (2 beta/R) d-^3 f; the second term is beta d-^2 phi")
def central(tf, tg, Kmat, order=1):
    Kinv = Kmat.inv()
    tm = lambda t: t.subs({kp: -kp, km: -km}, simultaneous=True)
    C = sum([tf, tg][i] * tm([tf, tg][j]) * Kinv[i, j] for i in (0, 1) for j in (0, 1))
    C = sp.series(sp.simplify(C), bet, 0, order + 1).removeO()
    return sp.simplify(sp.expand(C).coeff(bet, 1)), sp.simplify(sp.expand(C).coeff(bet, 0))
full1, full0 = central(t_f, t_g, K)
say(f"   <T(k) T(-k)> with this tensor and the propagator of the full quadratic action: order beta^0: {full0};  order beta: {sp.factor(full1)}")
nonlocal_full = sp.simplify(sp.limit(full1 * kp / km**3, kp, 0))
say(f"   its non-local part (the coefficient of k_m^3/k_p): {nonlocal_full} beta")
# the same with the free propagator only (what a count that ignores the quadratic terms of (9) gives)
K0 = K.subs(bet, 0)
free1, free0 = central(t_f.subs(kp, 0), t_g.subs(kp, 0), K0)
nonlocal_free = sp.simplify(sp.limit(free1 * kp / km**3, kp, 0))
say(f"   with the free propagator instead: coefficient {nonlocal_free} beta")
# calibration: a canonical field chi, Lagrangian d+chi d-chi, T = q d-^2 chi adds 12 q^2 to the central term
Kchi = 2 * kp * km
qq = sp.symbols("q")
cal = sp.simplify((-qq * km**2) * (-qq * km**2) / Kchi * kp / km**3)
say(f"   calibration: for a canonical field with improvement q d-^2 chi the same coefficient is {cal}, and that is a central term 12 q^2;")
say(f"   so the coefficient x 24 is the central term: {sp.simplify(24 * nonlocal_full)} beta from (9) on the induced metric"
    f"  ({sp.simplify(24 * nonlocal_free)} beta if the propagator correction is left out)")
half1, _ = central(t_f.subs(kp, 0) / 2, t_g.subs(kp, 0), K0)
say(f"   with half the improvement term and the free propagator (the first version of Appendix B): {sp.simplify(24 * sp.limit(half1 * kp / km**3, kp, 0))} beta, by two omissions that cancel")
# the redefinition g -> g + (beta a^2/R^2) k_m^2 f (in momentum space) removes the term of the action that changes <g g>
Jm = sp.Matrix([[1, 0], [bet * aa**2 / Rr**2 * km**2, 1]])            # (f, g) = Jm (f', g')
Kp = sp.simplify(Jm.T * K * Jm)
say(f"   after the redefinition g = g' - (beta a^2/R^2) d-^2 f': K_ff to first order in beta = {sp.simplify(sp.series(Kp[0, 0], bet, 0, 2).removeO())},"
    f" and the tensor becomes -(R/a^2) d-g' + (beta/R) d-^3 f' - (2 beta/R) d-^3 f' = -(R/a^2) d-g' - (beta/R) d-^3 f'")
say("   total: d + 12 beta - 26 = 0 for beta = (26 - d)/12, which is the coefficient of (9): (beta/4 pi) int du dv d+phi d-phi = (26 - d)/(48 pi) int (1/2)(d phi)^2")
# ---------------------------------------------------------------------------------------- I
say()
say("I. Casimir energy of a massive scalar on a circle (Section 6): -(m/pi) sum_n K1(n m L)/n against the regulated mode sum")
from scipy.special import k1
def bessel_form(m, L, nmax=4000):
    n = np.arange(1, nmax + 1)
    return -(m / math.pi) * float(np.sum(k1(n * m * L) / n))
def mode_sum(m, L, ep):
    n = np.arange(-200000, 200001); kq = 2 * math.pi * n / L; w = np.sqrt(kq * kq + m * m)
    kk = np.linspace(kq[0] - math.pi / L, kq[-1] + math.pi / L, 8000001); ww = np.sqrt(kk * kk + m * m)
    return 0.5 * np.sum(w * np.exp(-ep * w)) - 0.5 * np.trapezoid(ww * np.exp(-ep * ww), kk) * L / (2 * math.pi)
for m_, L_ in ((1.0, 2.0), (2.0, 1.5)):
    say(f"   m = {m_}, L = {L_}: Bessel form {bessel_form(m_, L_):.6f}; mode sum with cutoff 0.02, 0.01: {mode_sum(m_, L_, 0.02):.6f}, {mode_sum(m_, L_, 0.01):.6f}")
say(f"   m -> 0: {bessel_form(1e-3, 1.0, 200000):.5f} against -pi/6 = {-math.pi / 6:.5f}")
open(os.path.join(HERE, "..", "results", "effective_string.txt"), "w").write("\n".join(out) + "\n")
