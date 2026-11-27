"""Figure of QCDS-99/S1: light fields of the tip string in string units, and the
effective Casimir coefficient of the wound string.  Python 3, NumPy, SciPy, Matplotlib."""
import json
import math
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import gamma as Gamma
from scipy.special import k1

root = Path(__file__).resolve().parents[1]
data = json.loads((root / "results/tip-spectrum.json").read_text())
tensor = math.sqrt(data["G_minimal_operator_k2"][0]) / 3
charged = math.sqrt(data["F_charge1_M2"][0]) / 3
hn = (8 / math.e) ** (1 / 3) / Gamma(4 / 3)

lam = np.linspace(8.0, 120.0, 400)
mk = np.sqrt(27 * np.pi / (2 * lam))
ms = mk * hn * (lam / 9) ** (1 / 3) * np.exp(-lam / 9)

fig, (a, b) = plt.subplots(1, 2, figsize=(11.0, 4.3))
a.semilogy(lam, charged * mk, color="tab:purple", lw=1.4, label="charge-one tensor glueball")
a.semilogy(lam, tensor * mk, color="tab:green", lw=1.4, label="lowest tensor glueball")
a.semilogy(lam, mk, color="tab:blue", lw=2.0, label=r"cigar doublet $M_{\rm KK}$")
a.semilogy(lam, mk / 2, color="tab:orange", lw=2.0, label=r"fermions $M_{\rm KK}/2$")
a.semilogy(lam, ms, color="tab:red", lw=1.6, ls="--", label=r"sphere gap, $\mu=M_{\rm KK}$")
a.axhline(4 * math.pi / 3, color="0.35", lw=1.0, ls=":", label=r"two phonons, $L\sqrt{\sigma}=3$")
a.axvline(27 * math.pi / 2, color="0.6", lw=0.8)
a.text(27 * math.pi / 2 + 1.5, 6e-4, r"$M_{\rm KK}=\sqrt{\sigma}$", fontsize=8, color="0.3")
a.set_xlabel(r"'t Hooft coupling $\lambda$")
a.set_ylabel(r"energy / $\sqrt{\sigma}$")
a.set_ylim(1e-4, 20)
a.set_title("(a) infinite-length masses of the light fields", fontsize=10)
a.legend(fontsize=7.2, loc="lower left")


def c_eff(x, structure):
    """-6 L E / pi for the eight transverse bosons (sphere treated as massless)
    and eight fermions of mass M_KK/2, at x = M_KK L."""
    def bsum(z, sign=1):
        w = np.arange(1, 400)
        return np.sum(sign ** w * k1(w * z) / w)
    luscher = 6.0
    cigar = 2 * 6 * bsum(x) / math.pi**2 * x          # -6L/pi times 2 E_B(M_KK, L)
    sign = 1 if structure == "R" else -1
    ferm = -8 * 6 * (0.5 * x) * bsum(0.5 * x, sign) / math.pi**2
    return luscher + cigar + ferm


xs = np.linspace(0.05, 14.0, 300)
b.plot(xs, [c_eff(x, "R") for x in xs], color="tab:blue", lw=1.8, label="periodic fermions (R)")
ns = np.array([c_eff(x, "NS") for x in xs])
b.plot(xs, np.where(xs > 2 * math.pi, ns, np.nan), color="tab:orange", lw=1.8, label="antiperiodic (NS), dominant saddle")
b.plot(xs, np.where(xs <= 2 * math.pi, ns, np.nan), color="tab:orange", lw=1.0, ls=":", label="NS, subdominant saddle")
b.axhline(6, color="0.35", lw=0.9, ls="--")
b.axhline(2, color="tab:red", lw=0.9, ls="--")
b.text(8.0, 6.25, "six light bosons (sphere massless)", fontsize=8, color="0.3")
b.text(5.2, 2.25, r"infrared reference for $L\gg 1/m_S$: two translations", fontsize=8, color="tab:red")
b.axvline(2 * math.pi, color="0.6", lw=0.8)
b.set_xlabel(r"$M_{\rm KK}L$")
b.set_ylabel(r"$c_{\rm eff}=-6L\,(E_0-\sigma L)/\pi$")
b.set_ylim(-0.5, 12.5)
b.set_title("(b) Casimir coefficient of the wound string", fontsize=10)
b.legend(fontsize=7.2, loc="upper right")
fig.tight_layout()
fig.savefig(root / "figures/tip-string.png", dpi=170)
print("written figures/tip-string.png")
