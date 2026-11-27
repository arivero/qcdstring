"""Verify the printed tables, quoted values, equation tags and local links of QCDS-99/S1
against results/tip-spectrum.json.  Python 3 standard library."""
import json
import math
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
paper = (root / "paper.md").read_text()
d = json.loads((root / "results/tip-spectrum.json").read_text())


def rows(heading):
    block = next(part for part in paper.split(heading, 1)[1].split("\n\n") if part.startswith("|"))
    return [[c.strip() for c in line.strip("|").split("|")] for line in block.splitlines()[2:]]


def close(cell, value, tol):
    return abs(float(cell) - value) <= tol


checks = 0
# equation tags
tags = [int(t) for t in re.findall(r"\\tag\{(\d+)\}", paper)]
assert tags == list(range(1, len(tags) + 1)), tags
checks += 1

# Table 1: sphere gap
for cells, row in zip(rows("**Table 1.**"), d["E_gap_table"], strict=True):
    assert close(cells[0], row["lambda"], 0.006)
    assert close(cells[1], row["g2"], 0.00006)
    assert close(cells[2], row["gap_over_mu"], 5.1e-5 * max(1, row["gap_over_mu"] / 0.01) if row["gap_over_mu"] > 0.01 else 5.1e-7 if row["gap_over_mu"] < 0.001 else 5.1e-6)
    checks += 1

# Table 2: Casimir terms in units of M_KK
for cells, row in zip(rows("**Table 2.**"), d["D_table_units_MKK"][1:5], strict=True):
    assert float(cells[0]) == row["MKK_L_over_2pi"]
    for c, key in zip(cells[1:], ("luscher_two_bosons", "cigar_pair", "fermions_R", "fermions_NS", "R_minus_NS")):
        assert close(c, row[key], 5.1e-6), (c, key, row[key])
    checks += 1

# Table 3: string units at lambda_*
for cells, row in zip(rows("**Table 3.**"), d["D_table_lambda_star"], strict=True):
    assert float(cells[0]) == row["L_sqrt_sigma"]
    for c, key in zip(cells[1:], ("luscher_two", "luscher_six", "cigar_pair", "fermions_R", "R_minus_NS")):
        assert close(c, row[key], 5.1e-5), (c, key, row[key])
    checks += 1

# Table 4: bulk levels
levels = [(0, d["F_neutral_M2"][0]), (0, d["F_neutral_M2"][1]), (1, d["F_charge1_M2"][0]),
          (1, d["F_charge1_M2"][1]), (2, d["F_charge2_M2"][0])]
for cells, (n, m2), dg in zip(rows("**Table 4.**"), levels, d["F_level_diagnostics"], strict=True):
    assert int(cells[0]) == n and close(cells[1], m2, 5.1e-5) and close(cells[2], math.sqrt(m2) / 3, 5.1e-5)
    assert dg["n"] == n and abs(dg["M2"] - m2) < 1e-9 and dg["success"] and dg["above_bound_9n2"]
    assert int(cells[3]) == dg["nodes"]
    mant, expo = re.fullmatch(r"\$(\d)\\times10\^\{(-\d+)\}\$", cells[4]).groups()
    assert abs(math.log10(float(mant) * 10 ** int(expo)) - math.log10(dg["sensitivity"])) < 0.5
    checks += 1

# Table 6: three-length estimator
for cells, row in zip(rows("**Table 6.**"), d["D_three_length"], strict=True):
    assert close(cells[0], row["lambda"], 0.006)
    assert [float(x) for x in cells[1].split(",")] == row["L_sqrt_sigma"]
    assert close(cells[3], row["MKK_L_min"], 0.006) and close(cells[4], row["mS_L_max"], 6e-5 if row["mS_L_max"] < 1 else 0.006)
    assert close(cells[5], row["a_hat_R_over_pi"], 5.1e-5) and close(cells[6], row["a_hat_NS_over_pi"], 5.1e-5)
    assert row["NS_dominant"]
    checks += 1

# Table 5: string units
for cells, row in zip(rows("**Table 5.**"), d["E_window"], strict=True):
    assert close(cells[0], row["lambda"], 0.006)
    assert close(cells[1], row["MKK_over_sqrt_sigma"], 5.1e-5) and close(cells[2], row["fermion_over_sqrt_sigma"], 5.1e-5)
    assert abs(float(cells[3]) / row["mS_over_sqrt_sigma_mu_MKK"] - 1) < 2e-3
    assert abs(float(cells[4]) / row["inverse_mS_times_sqrt_sigma"] - 1) < 2e-3
    assert close(cells[5], row["lowest_tensor_glueball_over_sqrt_sigma"], 5.1e-5)
    assert close(cells[6], row["charged_tensor_over_sqrt_sigma"], 5.1e-5)
    assert close(cells[7], row["inverse_coupling"], 5.1e-5)
    checks += 1

# symbolic and matrix results
assert d["A_cigar_mass_over_MKK_11d"] == "1" and d["A_cigar_mass_over_MKK_10d"] == "1"
assert set(d["A_cigar_mass_over_MKK_Dp_family"].values()) == {"1"}
assert d["A_sigma_over_MKK2"] == "2*lambda/(27*pi)" and d["A_inverse_coupling"] == "lambda/(6*pi)"
assert d["A_string_coupling_tip_times_N_over_lambda32"] == "sqrt(3)/(9*pi)"
for key in ("B_clifford_ok", "B_mass_operator_is_f_over_4_Gamma4", "B_projector_matrix_squares_to_one",
            "B_mass_operator_commutes_with_projector", "B_sphere_commutator_is_multiple_of_Gamma78",
            "B_AdS_term_is_f_over_12", "B_J56_commutes_with_Gamma4"):
    assert d[key] is True, key
assert d["B_projector_rank"] == 16 and d["B_kernel_dimension_on_shell"] == 16
assert d["B_kernel_dimension_on_shell_projected"] == 8
assert d["B_sphere_commutator_coefficient"] == round(-1 / 18, 12)
assert d["B_fermion_mass_over_MKK"] == "1/2" and d["C_sum_rule_bosons_minus_fermions"] == 0
assert d["B_cigar_charges_on_kappa_fixed_space"] == [-0.5, 0.5]
assert set(d["B_joint_mass_sign_and_charge_multiplicities"].values()) == {4}
assert d["B_sphere_K_equals_sign_f_over_6_Gamma_m_Gamma4"] == -1
assert d["B_flatspin_times_chirality_fixed_at_each_cigar_charge"] == {"0.5": [-1.0], "-0.5": [1.0]}
assert d["C_invariant_two_fermion_bilinears_charge_one"] == 0
assert d["C_invariant_couplings_two_fermions_plus_sphere_quantum"] == 8
assert d["C_cigar_minus_two_fermion_threshold"] == 0
assert d["C_subspace_leakage_under_generators"] < 1e-10 and d["C_projector_commutes_with_unbroken_rotations"] is True
checks += 1

# quoted values
quoted = {
    "1.6048": d["E_exact_gap_over_Lambda_MSbar"],
    "2.1775": math.sqrt(d["F_charge1_M2"][0]) / 3,
    "1.1775": math.sqrt(d["F_charge1_M2"][0]) / 3 - 1,
    "37.170": d["G_printed_1998_operator_k2"][0],
    "81.354": d["G_printed_1998_operator_k2"][1],
    "138.473": d["G_printed_1998_operator_k2"][2],
    "1.4794": d["G_printed_1998_operator_mass_ratios"][1],
    "1.9301": d["G_printed_1998_operator_mass_ratios"][2],
    "8.50": d["G_lambda_for_0pp_3p5"],
    "4.34": d["G_lambda_for_2pp_4p9"],
    "1.0877": d["D_R_minus_NS_over_asymptotic"][0]["ratio"],
    "1.0596": d["D_R_minus_NS_over_asymptotic"][1]["ratio"],
    "1.0364": d["D_R_minus_NS_over_asymptotic"][2]["ratio"],
    "0.99968": d["D_R_minus_NS_small_L_times_L_over_2pi"],
    "0.99905": -d["D_limit_boson_times_6L_over_pi"],
    "0.9999976": -d["D_limit_fermion_NS_times_12L_over_pi"],
    "0.0447": d["B_smallest_singular_value_off_shell"],
    "42.41": d["E_lambda_where_MKK_equals_sqrt_sigma"],
    "2.2": math.sqrt(27 * math.pi / 18),
}
for text, value in quoted.items():
    assert text in paper, text
    digits = len(text.split(".")[1])
    assert abs(float(text) - value) <= 0.51 * 10 ** -digits, (text, value)
    checks += 1
assert abs(d["G_minimal_operator_k2"][0] - 22.0966) < 5e-5
assert "1.4783" in paper and "1.9317" in paper

# local links
for target in re.findall(r"\]\(([^)#]+)(?:#[^)]*)?\)", paper):
    if "://" in target:
        continue
    assert (root / target).exists(), target
    checks += 1
print(f"check_article: {checks} checks passed")
