"""Plot the conditional two-mode projection using the measured radial inputs."""
from pathlib import Path
import json

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from odd_cluster import kinetic_projection

root = Path(__file__).resolve().parents[1]
data = json.loads((root / "results/odd-cluster.json").read_text())
rows = data["radial"]
figure, (left, right) = plt.subplots(1, 2, figsize=(8.3,3.1), layout="constrained")
left.plot([r["w"] for r in rows], [r["relative_mass_squared_w2"] for r in rows],
          "o-", color="#245f87", label="Full radial block")
left.axhline(data["critical"][-1]["relative_mass_squared_w2"], ls="--",
             lw=1, color="#373737", label="Critical resolvent")
left.set(xscale="log",xlabel="Soft breaking $w$",
         ylabel=r"$(\lambda_n-\lambda_b)/w^2$")
left.legend(frameon=False, fontsize=8)
row = rows[0]
b,n = row["lambda_b"],row["lambda_n"]
scale = abs(b-n)/np.sqrt((b+n)/2)
x=np.geomspace(.01,1000,350)
fractions = [kinetic_projection(b,n,scale*t)["lower_vector_weight"] for t in x]
right.plot(x,fractions,color="#a94427")
p=row["one_term_projection"]
right.plot(p["h_over_mgamma"]/scale,p["lower_vector_weight"],"o",color="#16374d",
           label="One-term example")
right.set(xscale="log",xlabel=r"$|h|\sqrt{(m_b^2+m_n^2)/2}/|m_b^2-m_n^2|$",
          ylabel="Vector weight in lower pole",ylim=(-.02,.55))
right.legend(frameon=False,fontsize=8)
for ax in (left,right):
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
figure.savefig(root / "figures/odd-cluster.png",dpi=200,bbox_inches="tight")
