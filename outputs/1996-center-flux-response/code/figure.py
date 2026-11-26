"""Plot the two candidate costs against the numerically screened center sector."""
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

root = Path(__file__).resolve().parents[1]
data = json.loads((root / "results/flux-response.json").read_text())
samples = data["su4_source_scan"]
crossing = data["screening_crossing"]
t = np.linspace(-1/6, 1/8, 450)
middle = np.sqrt(2) * (1 + 2*t) / (1 + 4*t)
fig, ax = plt.subplots(figsize=(7.1, 3.8), layout="constrained")
ax.axhline(2, color="#686868", ls="--", lw=1.6, label="Two separated units")
ax.plot(t, middle, color="#ad510b", ls=":", lw=2.3, label="Middle vortex")
ax.plot(t, np.minimum(2, middle), color="#173960", lw=2.0, label="Lowest center-two cost")
ax.scatter([s["t"] for s in samples], [s["screened_ratio"] for s in samples],
           s=29, facecolor="white", edgecolor="#173960", zorder=5,
           label="Period and graph calculation")
ax.axvline(crossing, color="#777777", lw=0.9, ls=":")
ax.annotate(r"$t_*$", (crossing, 1.13), xytext=(4, 0), textcoords="offset points")
ax.set(xlim=(-0.171, 0.13), ylim=(1.10, 2.92),
       xlabel=r"Quartic source $t=\nu\Lambda^2/\mu$",
       ylabel="Tension / unit tension")
ax.spines[["top","right"]].set_visible(False)
ax.legend(frameon=False, loc="upper right", fontsize=9)
fig.savefig(root / "figures/flux-binding.png", dpi=200)
