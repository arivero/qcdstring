"""Fluctuation spectrum and finite-length energies of a string at the tip of
the compactified D4 background (QCDS-99/S1).

Python 3 with NumPy, SciPy and SymPy.  Writes results/tip-spectrum.json.

Parts
  A  geometry: Kaluza-Klein mass, mass of the cigar doublet in eleven- and
     ten-dimensional variables, sphere radius, sigma-model coupling, tension
  B  fermions: the membrane mass operator from the supercovariant derivative
     with explicit 32 x 32 gamma matrices, its projector and dispersion
  C  the mass sum rule
  D  Casimir sums for the wound string, both spin structures, and tables
  E  the O(5) sigma-model gap
  F  bulk scalar with Kaluza-Klein charge n: radial eigenvalues by shooting
  G  test of the shooting on the radial equation printed in the 1998 glueball paper
"""
import itertools
import json
import math
from pathlib import Path

import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
from scipy.special import gamma as Gamma
from scipy.special import k1

out = {}

# ----------------------------------------------------------------- A geometry
rho, r0, RA, U0, RD, ls, gs, N, lam = sp.symbols("rho r0 R_A U0 R_D l_s g_s N lambda", positive=True)

# eleven dimensions: ds^2 = (r/R_A)^2 (-dt^2 + dx^2 + dy^2 + f dtau^2) + R_A^2 dr^2/(r^2 f) + R_S^2 dOmega_4^2
# f = 1 - (r0/r)^6, R_A = 2 R_S.  Proper distance from the tip: r - r0 = 3 r0 rho^2 / (2 R_A^2) + ...
dr = 3 * r0 * rho**2 / (2 * RA**2)
r = r0 + dr
f11 = 1 - (r0 / r) ** 6
# check that d(rho) = R_A dr / (r sqrt f) to leading order
lhs = sp.series(RA * sp.diff(r, rho) / (r * sp.sqrt(f11)), rho, 0, 2).removeO()
out["A_proper_distance_check"] = sp.simplify(lhs - 1) == 0
gtautau = sp.series((r / RA) ** 2 * f11, rho, 0, 3).removeO()
MKK11 = sp.sqrt(sp.simplify(gtautau / rho**2))
out["A_MKK_11d"] = str(sp.simplify(MKK11))                       # 3 r0 / R_A^2
warp3 = sp.series((r / r0) ** 3, rho, 0, 3).removeO()           # membrane wrapped on y: three warped directions
c11 = sp.simplify((warp3 - 1) / rho**2)
m_cigar_11 = sp.simplify(sp.sqrt(2 * c11) * (r0 / RA))          # proper mass times sqrt(-g_tt)
out["A_cigar_mass_over_MKK_11d"] = str(sp.simplify(m_cigar_11 / MKK11))

# ten dimensions, string frame: ds^2 = (U/R)^{3/2}(-dt^2 + dx^2 + f dtau^2) + (R/U)^{3/2}(dU^2/f + U^2 dOmega_4^2)
dU = sp.Rational(3, 4) * rho**2 * sp.sqrt(U0) / RD ** sp.Rational(3, 2)
U = U0 + dU
f10 = 1 - (U0 / U) ** 3
lhs10 = sp.series((RD / U) ** sp.Rational(3, 4) * sp.diff(U, rho) / sp.sqrt(f10), rho, 0, 2).removeO()
out["A_proper_distance_check_10d"] = sp.simplify(lhs10 - 1) == 0
gtt10 = sp.series((U / RD) ** sp.Rational(3, 2) * f10, rho, 0, 3).removeO()
MKK10 = sp.sqrt(sp.simplify(gtt10 / rho**2))
out["A_MKK_10d"] = str(sp.simplify(MKK10))                       # 3 sqrt(U0) / (2 R^{3/2})
warp10 = sp.series((U / U0) ** sp.Rational(3, 2), rho, 0, 3).removeO()
c10 = sp.simplify((warp10 - 1) / rho**2)
m_cigar_10 = sp.simplify(sp.sqrt(2 * c10) * (U0 / RD) ** sp.Rational(3, 4))
out["A_cigar_mass_over_MKK_10d"] = str(sp.simplify(m_cigar_10 / MKK10))

# the same ratio for every Dp soliton: g_tt ~ U^((7-p)/2), f = 1 - (U0/U)^(7-p)
ratios = {}
for pp in (2, 3, 4, 5, 6):
    Uq = sp.symbols("U", positive=True)
    gtt = Uq ** sp.Rational(7 - pp, 2)
    ff = 1 - (U0 / Uq) ** (7 - pp)
    ratio = sp.simplify((2 * sp.diff(sp.log(gtt), Uq) / sp.diff(ff, Uq)).subs(Uq, U0))
    ratios[pp] = str(ratio)
out["A_cigar_mass_over_MKK_Dp_family"] = ratios

# tension, sphere radius and sigma-model coupling in terms of lambda = 2 pi g_s N l_s M_KK, R_D^3 = pi g_s N l_s^3
M = sp.symbols("M_KK", positive=True)
RD3 = sp.pi * gs * N * ls**3
U0_sol = sp.Rational(4, 9) * M**2 * RD3                         # from M_KK = 3 sqrt(U0)/(2 R_D^{3/2})
gsN = lam / (2 * sp.pi * ls * M)
sigma = sp.simplify((1 / (2 * sp.pi * ls**2)) * (U0_sol / RD3 ** sp.Rational(1, 3)) ** sp.Rational(3, 2))
sigma = sp.simplify(sigma.subs(gs, gsN / N))
out["A_sigma_over_MKK2"] = str(sp.simplify(sigma / M**2))        # 2 lambda / (27 pi)
RS2 = sp.simplify((sp.sqrt(RD3) * sp.sqrt(U0_sol)).subs(gs, gsN / N))
out["A_sphere_radius2_over_ls2"] = str(sp.simplify(RS2 / ls**2))  # lambda / 3
out["A_inverse_coupling"] = str(sp.simplify(RS2 / (2 * sp.pi * ls**2)))  # lambda / (6 pi)
# string coupling at the tip: e^phi = g_s (U0/R)^{3/4}, times N / lambda^{3/2}
ephi = sp.simplify((gs * (U0_sol / RD3 ** sp.Rational(1, 3)) ** sp.Rational(3, 4)).subs(gs, gsN / N))
out["A_string_coupling_tip_times_N_over_lambda32"] = str(sp.simplify(ephi * N / lam ** sp.Rational(3, 2)))

# ----------------------------------------------------------------- B fermions
s1 = np.array([[0, 1], [1, 0]], dtype=complex)
s2 = np.array([[0, -1j], [1j, 0]])
s3 = np.array([[1, 0], [0, -1]], dtype=complex)
I2 = np.eye(2, dtype=complex)


def kron(*ms):
    a = np.eye(1, dtype=complex)
    for m in ms:
        a = np.kron(a, m)
    return a


sp_g = []                                    # ten Hermitian gamma matrices, 32 x 32
for k in range(5):
    pre, post = [s3] * k, [I2] * (4 - k)
    sp_g.append(kron(*pre, s1, *post))
    sp_g.append(kron(*pre, s2, *post))
chir = np.eye(32, dtype=complex)
for g in sp_g:
    chir = chir @ g
chir = chir / np.sqrt((chir @ chir)[0, 0])   # squares to one, anticommutes with the ten
G = [1j * chir] + sp_g                       # G[0]^2 = -1; indices 0..10
eta = np.diag([-1.0] + [1.0] * 10)
I32 = np.eye(32, dtype=complex)
clifford_ok = all(
    np.allclose(G[a] @ G[b] + G[b] @ G[a], 2 * eta[a, b] * I32) for a in range(11) for b in range(11))
out["B_clifford_ok"] = bool(clifford_ok)

# index use: 0 t, 1 x (string), 2 y (wrapped circle), 3 4 flat transverse, 5 6 cigar, 7 8 9 10 sphere
SPH = (7, 8, 9, 10)
fval = 1.0                                   # F_{7 8 9 10} = f in an orthonormal frame


def F4(a, b, c, d):
    idx = (a, b, c, d)
    if sorted(idx) != list(SPH):
        return 0.0
    perm = [SPH.index(i) for i in idx]
    sign = 1
    for i in range(4):
        for j in range(i + 1, 4):
            if perm[i] > perm[j]:
                sign = -sign
    return sign * fval


def anti(*idx):
    """Antisymmetrized product of upper-index gammas in an orthonormal frame."""
    if len(set(idx)) < len(idx):
        return np.zeros((32, 32), dtype=complex)
    m = I32
    for i in idx:
        m = m @ G[i]
    return m


def lower(a):
    return eta[a, a] * G[a]


def K(M_):
    """(1/288)(Gamma_M^{NPQR} - 8 delta_M^N Gamma^{PQR}) F_{NPQR}, lower index M."""
    tot = np.zeros((32, 32), dtype=complex)
    for n, p, q, r_ in itertools.permutations(SPH, 4):
        Fv = F4(n, p, q, r_)
        if M_ not in (n, p, q, r_):
            tot += lower(M_) @ anti(n, p, q, r_) * Fv       # Gamma_M^{NPQR} with M distinct
        if M_ == n:
            tot -= 8 * anti(p, q, r_) * Fv
    return tot / 288


WV = (0, 1, 2)
Mop = sum(G[a] @ K(a) for a in WV)           # Gamma^alpha K_alpha
G4 = anti(*SPH)
out["B_mass_operator_is_f_over_4_Gamma4"] = bool(np.allclose(Mop, fval / 4 * G4))
ev = np.linalg.eigvals(Mop)
out["B_mass_operator_eigenvalues"] = sorted({round(float(x.real), 12) for x in ev})
GM2 = anti(0, 1, 2)
out["B_projector_matrix_squares_to_one"] = bool(np.allclose(GM2 @ GM2, I32))
out["B_mass_operator_commutes_with_projector"] = bool(np.allclose(Mop @ GM2, GM2 @ Mop))
P = (I32 - GM2) / 2
out["B_projector_rank"] = int(round(np.trace(P).real))
# dispersion: (i k_a Gamma^a + m Gamma_4) has a kernel exactly on omega^2 = k^2 + m^2
m_f = fval / 4
kx = 0.37
om = math.sqrt(kx**2 + m_f**2)
Dk = -1j * om * G[0] + 1j * kx * G[1] + Mop
sv = np.linalg.svd(Dk, compute_uv=False)
out["B_kernel_dimension_on_shell"] = int(np.sum(sv < 1e-10))
svP = np.linalg.svd(Dk @ P, compute_uv=False)
out["B_kernel_dimension_on_shell_projected"] = int(np.sum(svP < 1e-10)) - (32 - out["B_projector_rank"])
Dk_off = -1j * (om * 1.1) * G[0] + 1j * kx * G[1] + Mop
out["B_smallest_singular_value_off_shell"] = float(np.linalg.svd(Dk_off, compute_uv=False).min())
# normalization check on the sphere: [K_7, K_8] = (f^2/18) Gamma^{78} up to sign, i.e. R_S = 3/f
comm = K(7) @ K(8) - K(8) @ K(7)
ratio = comm @ np.linalg.inv(anti(7, 8))
out["B_sphere_commutator_coefficient"] = round(float(ratio[0, 0].real), 12)
out["B_sphere_commutator_is_multiple_of_Gamma78"] = bool(np.allclose(ratio, ratio[0, 0] * I32))
out["B_expected_abs_coefficient_f2_over_18"] = fval**2 / 18
# on AdS directions K_mu = (f/12) Gamma_mu Gamma_4, the Killing value for R_A = 6/f
out["B_AdS_term_is_f_over_12"] = bool(np.allclose(K(3), fval / 12 * lower(3) @ G4))
# fermion mass in field-theory units: (r0/R_A) f/4 with f = 3/R_S = 6/R_A  ->  3 r0/(2 R_A^2) = M_KK/2
m_fermion = sp.simplify((r0 / RA) * sp.Rational(1, 4) * 6 / RA)
out["B_fermion_mass_over_MKK"] = str(sp.simplify(m_fermion / MKK11))

# cigar rotation generator (1/2) Gamma^{56} on the kappa-fixed subspace: charges +-1/2, four of each per mass sign
basis = np.linalg.svd(P)[0][:, :16]
J56 = basis.conj().T @ (0.5 * anti(5, 6)) @ basis
M4 = basis.conj().T @ G4 @ basis
evj = np.linalg.eigvals(J56)
out["B_cigar_charges_on_kappa_fixed_space"] = sorted({round(float(x.imag), 12) for x in evj})
joint = np.linalg.eigvals(J56 + 10 * M4)          # commuting operators: joint eigenvalues
counts = {}
for x in joint:
    key = (round(float((x.real) / 10), 6), round(float(x.imag), 6))
    counts[str(key)] = counts.get(str(key), 0) + 1
out["B_joint_mass_sign_and_charge_multiplicities"] = counts
out["B_J56_commutes_with_Gamma4"] = bool(np.allclose(anti(5, 6) @ G4, G4 @ anti(5, 6)))

# sphere component of the flux operator: K_m = s (f/6) Gamma_m Gamma_(4), record the sign s
k7 = K(7)
sgn = [sv for sv in (1, -1) if np.allclose(k7, sv * fval / 6 * lower(7) @ G4)]
out["B_sphere_K_equals_sign_f_over_6_Gamma_m_Gamma4"] = sgn[0] if sgn else None

# joint quantum numbers on the kappa-fixed space: cigar charge, flat transverse spin, sphere chirality
J34 = basis.conj().T @ (0.5 * anti(3, 4)) @ basis
Hj = 1j * (1.0 * J56 + 0.37 * J34) + 0.11 * M4          # Hermitian combination of commuting operators
w_, V_ = np.linalg.eigh(Hj)
triples = {}
for k in range(16):
    v = V_[:, k]
    q56 = round(float(np.imag(v.conj() @ J56 @ v)), 6)
    q34 = round(float(np.imag(v.conj() @ J34 @ v)), 6)
    ch = round(float(np.real(v.conj() @ M4 @ v)), 6)
    triples[str((q56, q34, ch))] = triples.get(str((q56, q34, ch)), 0) + 1
out["B_joint_charge_flatspin_chirality"] = triples
corr = {}
for key in triples:
    q56, q34, ch = eval(key)
    corr.setdefault(q56, set()).add(round(q34 * ch * 2, 6))
out["B_flatspin_times_chirality_fixed_at_each_cigar_charge"] = {str(k): sorted(v) for k, v in corr.items()}

# invariant bilinears on the charge +1/2 subspace under Spin(2)_flat x Spin(4)_sphere
Pplus = None
evq, Vq = np.linalg.eig(J56)
idx = [k for k in range(16) if abs(evq[k].imag - 0.5) < 1e-8]
Vp, _ = np.linalg.qr(Vq[:, idx])                     # orthonormal basis of the q56 = +1/2 subspace (8 dim)
def restrict(op16):
    return Vp.conj().T @ op16 @ Vp
full_gens = [J34] + [basis.conj().T @ (0.5 * anti(a, b)) @ basis for a, b in itertools.combinations((7, 8, 9, 10), 2)]
gens_V = [restrict(g16) for g16 in full_gens]
proj_out = np.eye(16) - Vp @ Vp.conj().T
leak = max(float(np.abs(proj_out @ g16 @ Vp).max()) for g16 in full_gens)   # unrestricted generators map the subspace into itself
out["C_subspace_leakage_under_generators"] = leak
assert leak < 1e-10
# the membrane projector commutes with the unbroken rotations (it transforms by conjugation)
out["C_projector_commutes_with_unbroken_rotations"] = bool(all(np.allclose(anti(0, 1, 2) @ (0.5 * anti(a, b)), (0.5 * anti(a, b)) @ anti(0, 1, 2))
    for a, b in [(3, 4), (5, 6)] + list(itertools.combinations((7, 8, 9, 10), 2))))
dV = Vp.shape[1]
rows_ = []
for X in gens_V:                                      # X^T B + B X = 0 for bilinear forms B on the subspace
    rows_.append(np.kron(X.T, np.eye(dV)) + np.kron(np.eye(dV), X.T))
A_ = np.vstack(rows_)
sv_ = np.linalg.svd(A_, compute_uv=False)
out["C_invariant_two_fermion_bilinears_charge_one"] = int(np.sum(sv_ < 1e-9))
# the same with one tangent sphere quantum (vector of SO(4), flat spin zero)
def so4_vector(a, b):
    """Adjoint action of (1/2) Gamma^{ab} on the sphere gammas: [X, Gamma^d] = sum_c m[c, d] Gamma^c."""
    X = 0.5 * anti(a, b)
    m = np.zeros((4, 4))
    for jd, dd in enumerate((7, 8, 9, 10)):
        comm = X @ G[dd] - G[dd] @ X
        for jc, cc in enumerate((7, 8, 9, 10)):
            m[jc, jd] = np.real(np.trace(G[cc] @ comm)) / 32
    return m
gens_W = [np.zeros((4, 4))] + [so4_vector(a, b) for a, b in itertools.combinations((7, 8, 9, 10), 2)]
out["C_vector_generator_78_matrix"] = so4_vector(7, 8).round(12).tolist()
rows_ = []
for X, Y in zip(gens_V, gens_W):
    rows_.append(np.kron(np.kron(X.T, np.eye(dV)), np.eye(4)) + np.kron(np.kron(np.eye(dV), X.T), np.eye(4))
                 + np.kron(np.kron(np.eye(dV), np.eye(dV)), Y.T))
A_ = np.vstack(rows_)
sv_ = np.linalg.svd(A_, compute_uv=False)
out["C_invariant_couplings_two_fermions_plus_sphere_quantum"] = int(np.sum(sv_ < 1e-9))

# ----------------------------------------------------------------- C sum rule
out["C_sum_rule_bosons_minus_fermions"] = 2 * 1.0**2 - 8 * 0.5**2
out["C_cigar_minus_two_fermion_threshold"] = 1.0 - 2 * 0.5

hmn_global = (8 / math.e) ** (1 / 3) / Gamma(1 + 1 / 3)

# ----------------------------------------------------------------- D Casimir sums


def bessel_sum(x, sign=+1, odd_only=False):
    """sum over w >= 1 of sign^w K_1(w x)/w (optionally odd w only)."""
    tot, w = 0.0, 1
    while True:
        term = k1(w * x) / w
        if w * x > 60:
            break
        if not (odd_only and w % 2 == 0):
            tot += (sign**w) * term
        w += 1
    return tot


def e_boson(m, L):                 # one real periodic scalar, energy on a circle of length L
    return -math.pi / (6 * L) if m == 0 else -(m / math.pi) * bessel_sum(m * L)


def e_fermion(m, L, structure):    # one two-dimensional Majorana fermion
    return (m / math.pi) * bessel_sum(m * L, sign=+1 if structure == "R" else -1)


# massless limits
x = 1e-3
out["D_limit_boson_times_6L_over_pi"] = e_boson(x, 1.0) * 6 / math.pi
out["D_limit_fermion_R_times_6L_over_pi"] = e_fermion(x, 1.0, "R") * 6 / math.pi
out["D_limit_fermion_NS_times_12L_over_pi"] = e_fermion(x, 1.0, "NS") * 12 / math.pi


def shift(xl, structure, sphere="heavy"):
    """Ground-energy shift of the wound string in units of M_KK, at x = M_KK L.
    sphere: 'heavy' leaves the four sphere coordinates out (L far above the sigma-model length);
            'free' counts them as four massless bosons (L far below it)."""
    L = xl
    e = 2 * e_boson(0, L) + 2 * e_boson(1.0, L) + 8 * e_fermion(0.5, L, structure)
    if sphere == "free":
        e += 4 * e_boson(0, L)
    return e


def r_minus_ns(xl):
    return (8 / math.pi) * bessel_sum(xl / 2, odd_only=True)


rows = []
for mult in (0.5, 1.0, 1.5, 2.0, 3.0, 4.0):
    xl = 2 * math.pi * mult
    rows.append({
        "MKK_L_over_2pi": mult,
        "luscher_two_bosons": 2 * e_boson(0, xl),
        "cigar_pair": 2 * e_boson(1.0, xl),
        "fermions_R": 8 * e_fermion(0.5, xl, "R"),
        "fermions_NS": 8 * e_fermion(0.5, xl, "NS"),
        "total_R_heavy_sphere": shift(xl, "R"),
        "total_NS_heavy_sphere": shift(xl, "NS"),
        "total_R_free_sphere": shift(xl, "R", "free"),
        "R_minus_NS": r_minus_ns(xl),
    })
    assert abs(rows[-1]["fermions_R"] - rows[-1]["fermions_NS"] - rows[-1]["R_minus_NS"]) < 1e-12
out["D_table_units_MKK"] = rows
for xl in (8.0, 12.0, 20.0):
    asym = 8 * math.sqrt(1.0 / (math.pi * xl)) * math.exp(-xl / 2)
    out.setdefault("D_R_minus_NS_over_asymptotic", []).append({"MKK_L": xl, "ratio": r_minus_ns(xl) / asym})
out["D_NS_saddle_condition"] = "M_KK L > 2 pi"
star = 27 * math.pi / 2
tab = []
for Ls in (3.0, 4.0, 6.0, 8.0, 10.0):
    xl = Ls                                    # M_KK = sqrt(sigma) at lambda = 27 pi / 2
    row = {"L_sqrt_sigma": Ls, "luscher_two": 2 * e_boson(0, xl), "luscher_six": 6 * e_boson(0, xl),
           "cigar_pair": 2 * e_boson(1.0, xl), "fermions_R": 8 * e_fermion(0.5, xl, "R"),
           "R_minus_NS": r_minus_ns(xl), "NS_saddle": xl > 2 * math.pi}
    tab.append(row)
out["D_table_lambda_star"] = tab


def casimir_total(Lv, mk, structure, sphere, msph=None):
    """Casimir part of the wound-string energy (zero-flux vacuum of the same spin structure subtracted):
    two translations, cigar pair (mass mk), eight fermions (mass mk/2) and the sphere sector
    ('free': four massless bosons; 'gapped': the O(5) five-plet of mass msph at leading exponential order)."""
    e = 2 * e_boson(0, Lv) + 2 * e_boson(mk, Lv) + 8 * e_fermion(mk / 2, Lv, structure)
    if sphere == "free":
        e += 4 * e_boson(0, Lv)
    else:
        e += 5 * e_boson(msph, Lv)
    return e


def three_length(Lv, mk, structure, sphere, msph=None):
    f_ = lambda x: casimir_total(x, mk, structure, sphere, msph)
    return (4 * Lv / 3) * (2 * f_(Lv) - 3 * f_(2 * Lv) + f_(4 * Lv))


tl = []
for lam_v, Ls, sphere in ((80.0, 10.0, "free"), (80.0, 20.0, "free"), (27 * math.pi / 2, 8.0, "free"), (20.0, 30.0, "gapped")):
    mk = math.sqrt(27 * math.pi / (2 * lam_v))                       # in units of sqrt(sigma)
    msph = mk * hmn_global * (lam_v / 9) ** (1 / 3) * math.exp(-lam_v / 9)
    row = {"lambda": lam_v, "L_sqrt_sigma": [Ls, 2 * Ls, 4 * Ls], "sphere": sphere,
           "MKK_L_min": mk * Ls, "mS_L_max": msph * 4 * Ls, "mS_L_min": msph * Ls,
           "NS_dominant": mk * Ls > 2 * math.pi}
    for st_ in ("R", "NS"):
        row["a_hat_" + st_ + "_over_pi"] = three_length(Ls, mk, st_, sphere, msph) / math.pi
    tl.append(row)
out["D_three_length"] = tl
out["D_uv_total_R_free_sphere_times_L"] = shift(1e-3, "R", "free") * 1e-3   # tends to zero: 8 bosons against 8 fermions
out["D_R_minus_NS_small_L_times_L_over_2pi"] = r_minus_ns(1e-3) * 1e-3 / (2 * math.pi)

# conversion to string units: M_KK / sqrt(sigma) = sqrt(27 pi / (2 lambda))
conv = []
for lam_v in (20.0, 27 * math.pi / 2, 80.0):
    mk = math.sqrt(27 * math.pi / (2 * lam_v))
    for Ls in (2.0, 3.0, 4.0, 6.0):
        xl = mk * Ls
        conv.append({"lambda": lam_v, "MKK_over_sqrt_sigma": mk, "L_sqrt_sigma": Ls, "MKK_L": xl,
                     "NS_allowed": xl > 2 * math.pi,
                     "shift_R_over_sqrt_sigma": mk * shift(xl, "R"),
                     "luscher_over_sqrt_sigma": mk * 2 * e_boson(0, xl),
                     "R_minus_NS_over_sqrt_sigma": mk * r_minus_ns(xl),
                     "fermion_gap_over_sqrt_sigma": mk / 2, "cigar_gap_over_sqrt_sigma": mk,
                     "two_phonon_over_sqrt_sigma": 4 * math.pi / Ls})
out["D_table_string_units"] = conv

# ----------------------------------------------------------------- E O(5) gap
Nn = 5
hmn = (8 / math.e) ** (1 / (Nn - 2)) / Gamma(1 + 1 / (Nn - 2))
out["E_exact_gap_over_Lambda_MSbar"] = hmn
gap = []
for lam_v in (9.0, 18.0, 27.0, 27 * math.pi / 2, 54.0, 80.0):
    g2 = 6 * math.pi / lam_v
    Lam_over_mu = (2 * math.pi / ((Nn - 2) * g2)) ** (1 / (Nn - 2)) * math.exp(-2 * math.pi / ((Nn - 2) * g2))
    gap.append({"lambda": lam_v, "g2": g2, "gap_over_mu": hmn * Lam_over_mu,
                "check_closed_form": hmn * (lam_v / 9) ** (1 / 3) * math.exp(-lam_v / 9)})
out["E_gap_table"] = gap
window = []
for lam_v in (20.0, 27 * math.pi / 2, 80.0):
    mk = math.sqrt(27 * math.pi / (2 * lam_v))
    ms = mk * hmn * (lam_v / 9) ** (1 / 3) * math.exp(-lam_v / 9)
    window.append({"lambda": lam_v, "MKK_over_sqrt_sigma": mk, "fermion_over_sqrt_sigma": mk / 2,
                   "mS_over_sqrt_sigma_mu_MKK": ms, "inverse_mS_times_sqrt_sigma": 1 / ms,
                   "lowest_tensor_glueball_over_sqrt_sigma": None, "inverse_coupling": lam_v / (6 * math.pi)})
out["E_window"] = window
out["E_lambda_where_MKK_equals_sqrt_sigma"] = 27 * math.pi / 2

# ----------------------------------------------------------------- F bulk scalar with charge n
# ((x^7 - x) phi')' + x^3 (M2 - 9 n^2 x^6/(x^6 - 1)) phi = 0, units r0 = R_A = 1, M_KK = 3.


def frobenius_a1(M2, n):
    xs, a1 = sp.symbols("x a1")
    s = sp.Rational(abs(int(2 * n)), 4)
    t = sp.symbols("t", positive=True)
    phi = t**s * (1 + a1 * t)
    xx = 1 + t
    expr = sp.diff((xx**7 - xx) * sp.diff(phi, t), t) + xx**3 * (M2 - 9 * sp.Rational(int(2 * n), 2) ** 2 * xx**6 / (xx**6 - 1)) * phi
    lead = sp.series(sp.simplify(expr / t**s), t, 0, 1).removeO()
    return float(sp.solve(sp.Eq(lead, 0), a1)[0])


def mismatch(M2, n, xm=1.6, xmax=200.0, eps=1e-5):
    s = abs(n) / 2
    a1 = frobenius_a1(sp.Float(M2), n)

    def rhs(x, y):
        phi, p = y
        return [p / (x**7 - x), -x**3 * (M2 - 9 * n * n * x**6 / (x**6 - 1)) * phi]

    phi0 = eps**s * (1 + a1 * eps)
    dphi0 = s * eps ** (s - 1) * (1 + a1 * eps) + eps**s * a1 if s > 0 else a1
    x0 = 1 + eps
    left = solve_ivp(rhs, (x0, xm), [phi0, (x0**7 - x0) * dphi0], method="DOP853", rtol=1e-11, atol=1e-14)
    k2 = M2 - 9 * n * n
    phiR = xmax**-6 * (1 - k2 / (16 * xmax**2))
    dphiR = -6 * xmax**-7 * (1 - k2 / (16 * xmax**2)) + xmax**-6 * (k2 / (8 * xmax**3))
    right = solve_ivp(rhs, (xmax, xm), [phiR, (xmax**7 - xmax) * dphiR], method="DOP853", rtol=1e-11, atol=1e-30)
    if not (left.success and right.success):
        raise RuntimeError(f"radial integration failed at M2={M2}, n={n}")
    a, pa = left.y[0, -1], left.y[1, -1]
    b, pb = right.y[0, -1], right.y[1, -1]
    return (a * pb - pa * b) / math.sqrt((a * a + pa * pa) * (b * b + pb * pb))


def levels(n, lo, hi, count, step=0.5):
    found, m2 = [], lo
    prev = mismatch(m2, n)
    while m2 < hi and len(found) < count:
        nxt = m2 + step
        cur = mismatch(nxt, n)
        if prev * cur < 0:
            found.append(brentq(lambda z: mismatch(z, n), m2, nxt, xtol=1e-9))
        m2, prev = nxt, cur
    return found


def diagnose(M2, n, xm=1.6, xmax=200.0, eps=1e-5):
    """Solver success flags and node count of the matched eigenfunction on (1, xmax)."""
    s_ = abs(n) / 2
    a1 = frobenius_a1(sp.Float(M2), n)

    def rhs(x, y):
        phi, p = y
        return [p / (x**7 - x), -x**3 * (M2 - 9 * n * n * x**6 / (x**6 - 1)) * phi]

    phi0 = eps**s_ * (1 + a1 * eps)
    dphi0 = s_ * eps ** (s_ - 1) * (1 + a1 * eps) + eps**s_ * a1 if s_ > 0 else a1
    x0 = 1 + eps
    grid_l = np.linspace(x0, xm, 4000)
    left = solve_ivp(rhs, (x0, xm), [phi0, (x0**7 - x0) * dphi0], method="DOP853", rtol=1e-11, atol=1e-14, t_eval=grid_l)
    k2 = M2 - 9 * n * n
    phiR = xmax**-6 * (1 - k2 / (16 * xmax**2))
    dphiR = -6 * xmax**-7 * (1 - k2 / (16 * xmax**2)) + xmax**-6 * (k2 / (8 * xmax**3))
    grid_r = np.geomspace(xmax, xm, 4000)
    right = solve_ivp(rhs, (xmax, xm), [phiR, (xmax**7 - xmax) * dphiR], method="DOP853", rtol=1e-11, atol=1e-30, t_eval=grid_r)
    scale = left.y[0, -1] / right.y[0, -1]
    phi_all = np.concatenate([left.y[0], scale * right.y[0][::-1]])
    nodes = int(np.sum(np.sign(phi_all[1:]) != np.sign(phi_all[:-1])))
    return {"success": bool(left.success and right.success), "nodes": nodes}


def sensitivity(M2, n):
    vals = []
    for xm_, xmax_, eps_ in ((1.6, 200.0, 1e-5), (2.0, 400.0, 1e-6), (1.3, 100.0, 1e-4)):
        f_ = lambda z: mismatch(z, n, xm=xm_, xmax=xmax_, eps=eps_)
        vals.append(brentq(f_, M2 - 0.3, M2 + 0.3, xtol=1e-10))
    return max(abs(v - M2) for v in vals)


neutral = levels(0, 1.0, 70.0, 3)
charged1 = levels(1, 9.5, 90.0, 2)
charged2 = levels(2, 36.5, 140.0, 1)
out["F_neutral_M2"] = neutral
out["F_charge1_M2"] = charged1
out["F_charge2_M2"] = charged2
out["F_neutral_m_over_MKK"] = [math.sqrt(v) / 3 for v in neutral]
out["F_charge1_m_over_MKK"] = [math.sqrt(v) / 3 for v in charged1]
out["F_charge2_m_over_MKK"] = [math.sqrt(v) / 3 for v in charged2]
out["F_bulk_threshold_separation_over_MKK"] = math.sqrt(charged1[0]) / 3 - 1
diag = []
for n_, m2 in ((0, neutral[0]), (0, neutral[1]), (1, charged1[0]), (1, charged1[1]), (2, charged2[0])):
    dd = diagnose(m2, n_)
    dd.update({"n": n_, "M2": m2, "sensitivity": sensitivity(m2, n_), "above_bound_9n2": m2 > 9 * n_ * n_})
    diag.append(dd)
out["F_level_diagnostics"] = diag



def mismatch_general(k2, a, b, xm=1.7, xmax=60.0, eps=1e-4):
    """Neutral radial operator (x^7 - x) f'' + (a x^6 - b) f' + x^3 k2 f = 0."""
    def rhs(x, y):
        return [y[1], -((a * x**6 - b) * y[1] + x**3 * k2 * y[0]) / (x**7 - x)]
    f1p = -k2 / (a - b)
    left = solve_ivp(rhs, (1 + eps, xm), [1 + f1p * eps, f1p], method="DOP853", rtol=1e-11, atol=1e-14)
    pw = a - 1
    right = solve_ivp(rhs, (xmax, xm), [xmax**-pw, -pw * xmax**(-pw - 1)], method="DOP853", rtol=1e-11, atol=1e-30)
    if not (left.success and right.success):
        raise RuntimeError(f"radial integration failed at k2={k2}, operator ({a}, {b})")
    fa, ga = left.y[:, -1]
    fb, gb = right.y[:, -1]
    return (fa * gb - ga * fb) / math.sqrt((fa * fa + ga * ga) * (fb * fb + gb * gb))


def levels_general(a, b, count=3, lo=0.5, hi=200.0, step=0.25):
    found, k = [], lo
    prev = mismatch_general(k, a, b)
    while k < hi and len(found) < count:
        cur = mismatch_general(k + step, a, b)
        if prev * cur < 0:
            found.append(brentq(lambda z: mismatch_general(z, a, b), k, k + step, xtol=1e-10))
        k, prev = k + step, cur
    return found


printed = levels_general(10, 4)
out["G_printed_1998_operator_k2"] = printed
out["G_printed_1998_operator_mass_ratios"] = [math.sqrt(v / printed[0]) for v in printed]
out["G_published_table5_ratios"] = [x / 1.61 for x in (1.61, 2.38, 3.11)]
minimal = levels_general(7, 1, count=4)
out["G_minimal_operator_k2"] = minimal
for row in out["E_window"]:
    row["lowest_tensor_glueball_over_sqrt_sigma"] = row["MKK_over_sqrt_sigma"] * math.sqrt(minimal[0]) / 3
    row["charged_tensor_over_sqrt_sigma"] = row["MKK_over_sqrt_sigma"] * math.sqrt(charged1[0]) / 3
# lambda at which the tensor glueball and its degenerate scalar would sit at the registered P08 values
for name, target in (("0pp_3p5", 3.5), ("2pp_4p9", 4.9)):
    mk = target / (math.sqrt(minimal[0]) / 3)
    out["G_lambda_for_" + name] = 27 * math.pi / (2 * mk * mk)

Path(__file__).resolve().parents[1].joinpath("results/tip-spectrum.json").write_text(json.dumps(out, indent=1))
print(json.dumps({k: v for k, v in out.items() if not k.startswith("D_table")}, indent=1))
