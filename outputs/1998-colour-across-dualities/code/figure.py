"""Map the fixed-charge homotopy and the free-end tension ratio."""
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import brentq

root = Path(__file__).resolve().parents[1]
data = json.loads((root / "results/membrane.json").read_text())
fig, (left, right) = plt.subplots(1, 2, figsize=(8.1, 3.6), layout="constrained")
x = np.linspace(-0.025, 0.28)
for shift in (0, -1):
    left.plot(x, 4*x+shift, color="#8a8a8a", ls="--", lw=1.2)
for b, color, label in [(0, "#ad510b", "Wrapped bulk cycle"), (0.5, "#666666", "Intermediate path"),
                         (1, "#183f65", "Fixed-circle strip")]:
    left.plot([0,b/4], [0,b-1], lw=2.2, color=color, label=label)
    left.scatter([b/4], [b-1], color=color, s=16)
left.set(xlim=(-0.028,0.28), ylim=(-1.08,0.17), xlabel=r"$\arg(v)/(2\pi)$",
         ylabel=r"Lift of $\arg(t)/(2\pi)$", title="One relative charge")
left.legend(loc="lower right", fontsize=8, frameon=False)
eta = np.linspace(0.0001,0.95,160)
angles = np.array([brentq(lambda d: d+e*np.sin(d)-np.pi/2,0,np.pi/2) for e in eta])
unit = np.sqrt(8*np.sin(angles/2)**2+2/eta*(angles-np.pi/2)**2)
right.axhline(np.sqrt(2), lw=1.3, ls="--", color="#777777", label="Equal-circle chord")
right.plot(eta,2*np.sqrt(2)/unit, color="#183f65", label="Free endpoints")
rows=data["distance_scan"]
right.scatter([r["eta"] for r in rows], [r["length_2_over_1"] for r in rows],
              s=24, facecolor="white", edgecolor="#183f65", zorder=3, label="Cartesian minima")
right.set(xlabel=r"$\eta=2a^2/(4R)^2$", ylabel=r"$\ell_2/\ell_1$", title="Four-color tension ratio")
right.legend(fontsize=8, loc="upper left", frameon=False)
for ax in (left, right):
    ax.spines[["top","right"]].set_visible(False)
fig.savefig(root/"figures/charge-and-tension.png",dpi=200)
