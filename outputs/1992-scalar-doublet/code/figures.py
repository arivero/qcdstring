"""Draw the paper figures from the stored radial solutions."""
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / "results/trace-spectrum.json").read_text())
out = ROOT / "figures"
out.mkdir(exist_ok=True)
plt.rcParams.update({"font.size":10, "axes.spines.top":False, "axes.spines.right":False,
                     "savefig.bbox":"tight", "figure.dpi":150})
rows = [r for r in data["rows"] if r["w"]>0]
w = np.array([r["w"] for r in rows])
critical = data["rows"][0]["odd_mass"]
colors = ["#12618a","#a64228"]
fig, (ax,bx) = plt.subplots(1,2,figsize=(8.1,3.1),layout="constrained")
for i,(sign,label) in enumerate(((-1,"Lower scalar"),(1,"Upper scalar"))):
    ax.plot(w,[r["levels"][i]["mass"] for r in rows], "o", ms=4, color=colors[i],label=label)
    ax.plot([0,w[-1]],[critical,critical+sign*w[-1]/2], color=colors[i],lw=1,ls="--")
    bx.plot(w,[r["levels"][i]["trace_over_odd"] for r in rows], "o-", ms=4,color=colors[i])
ax.plot(w,[r["odd_mass"] for r in rows], color="#333333",label="Odd vector",lw=1.3)
ax.set(xlabel="Soft parameter $w$",ylabel=r"Mass / $m_\gamma$")
ax.legend(frameon=False,fontsize=8)
bx.plot(0,0.5,"o",ms=6,mfc="white",mec="#333333",clip_on=False)
bx.axhline(0.5,color="#666666",ls=":",lw=1)
bx.set(xlabel="Soft parameter $w$",ylabel="Trace residue / odd residue")
fig.savefig(out / "doublet.png",dpi=200)
plt.close(fig)

fig,ax=plt.subplots(figsize=(5.8,3.1),layout="constrained")
x=np.linspace(0,2.15,151)
ax.plot(x,(1+x/np.sqrt(1+x*x))/2,color="#222222",label="Two-level limit")
for w,marker,color in [(0.0025,"o",colors[0]),(0.01,"s",colors[1])]:
    sample=[r for r in data["joint_scaling"] if r["w"]==w]
    ax.plot([r["detuning"]/(2*critical*w) for r in sample],
            [r["lower_share"] for r in sample],marker,ms=5,color=color,label=f"$w={w}$")
ax.set(xlabel=r"Detuning $\delta/(2\nu_0 w)$",ylabel="Lower share of the trace doublet",ylim=(0.45,1.0))
ax.legend(frameon=False,fontsize=9)
fig.savefig(out / "detuning.png",dpi=200)
