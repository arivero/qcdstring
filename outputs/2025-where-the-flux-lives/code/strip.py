"""Gauge-invariant strong-electric SU(3) strip, revision of QCDS-25/S1.

Diagonalize the specified variational space of monotone fundamental lines
and all their cuts. Units set the cheaper horizontal fundamental cost to 1.
"""
from functools import lru_cache
from itertools import product
import json
from pathlib import Path

import numpy as np
from scipy import sparse
from scipy.optimize import brentq
from scipy.sparse.linalg import eigsh

ROOT = Path(__file__).resolve().parents[1]
MAIN_T = 0.45
MASS_PAIR = 6.5
RUNG = 1.25

def full_paths(length, left, right):
    """Each vertex number is 2*x+row. A directed edge is a pair of vertices."""
    for start in (range(2) if left is None else (left,)):
        for end in (range(2) if right is None else (right,)):
            for rows in product(range(2), repeat=length):
                previous = start
                path = []
                for x, row in enumerate(rows):
                    if row != previous:
                        path.append((2*x+previous, 2*x+row))
                    path.append((2*x+row, 2*(x+1)+row))
                    previous = row
                if end != previous:
                    path.append((2*length+previous, 2*length+end))
                yield tuple(path)

@lru_cache(maxsize=None)
def basis(length, left, right):
    networks = set()
    for path in full_paths(length, left, right):
        subsets = [()]
        for edge in path:
            subsets += [s+(edge,) for s in subsets]
        networks.update(subsets)
    states = sorted(networks, key=lambda s: (len(s),s))
    lookup = {s:i for i,s in enumerate(states)}
    size = len(states)
    occupations = np.zeros((size,5))
    midpoint = np.zeros((size,2))
    end_rungs = np.zeros(size)
    central = {(length-1)//2,length//2}
    bra, ket, amplitudes = [], [], []
    vacuum = left is None and right is None

    for i, edges in enumerate(states):
        segments = sum(j==0 or edges[j-1][1]!=edge[0] for j,edge in enumerate(edges))
        matched_left = bool(edges and left is not None and edges[0][0]==left)
        matched_right = bool(edges and right is not None and edges[-1][1]==2*length+right)
        light = (left is not None)+(right is not None)+2*(segments-matched_left-matched_right)
        occupations[i,3] = light/2
        occupations[i,4] = float(not edges)
        for j, (u,v) in enumerate(edges):
            x, row = divmod(u,2)
            if v//2 == x:
                occupations[i,2] += 1
                if x in (0,length):
                    end_rungs[i] += .5
            else:
                occupations[i,row] += 1
                if x in central:
                    midpoint[i,row] += 1/len(central)
            k = lookup[edges[:j]+edges[j+1:]]
            amp = 1. if vacuum and len(edges)==1 else 1/3
            bra.extend((i,k))
            ket.extend((k,i))
            amplitudes.extend((-amp,-amp))
    hopping = sparse.csr_matrix((amplitudes,(bra,ket)),shape=(size,size))
    return occupations, midpoint, end_rungs, hopping

def levels(length, left, right, costs, mass_pair=MASS_PAIR, t=MAIN_T, field=0., count=2):
    occ, mid, rungs, hops = basis(length,left,right)
    diagonal = occ[:,:4] @ np.array([*costs,RUNG,mass_pair]) + field*mid[:,0]
    matrix = sparse.diags(diagonal,format="csr") + t*hops
    start = np.random.default_rng(915).normal(size=len(diagonal))
    energies, vectors = eigsh(matrix,k=count,which="SA",tol=2.e-13,ncv=32,v0=start)
    order = np.argsort(energies)
    energies, vectors = energies[order], vectors[:,order]
    assert np.max(np.linalg.norm(matrix@vectors-vectors*energies,axis=0)) < 3.e-10
    weights = (vectors*vectors).T
    return dict(size=len(diagonal), energy=energies, mid=weights@mid,
                rung=weights@rungs, mass_slope=weights@occ[:,3],
                empty_weight=weights@occ[:,4])

def compare(length, row, costs=(1.,2.), mass_pair=MASS_PAIR, t=MAIN_T, field=0.):
    args = (costs,mass_pair,t,field)
    pair = levels(length,row,row,*args)
    vac = levels(length,None,None,*args,count=1)
    single_l = levels(length,row,None,*args,count=1)
    single_r = levels(length,None,row,*args,count=1)
    def reference(key):
        return single_l[key][0]+single_r[key][0]-vac[key][0]
    return dict(length=length, source="AB"[row], costs=costs,
                dimensions=[s["size"] for s in [pair,single_l,single_r,vac]],
                spectrum=pair["energy"], energy_minus_mesons=pair["energy"]-reference("energy"),
                raw_mid=pair["mid"], left_mid=single_l["mid"][0], right_mid=single_r["mid"][0],
                vacuum_mid=vac["mid"][0], sub_mid=pair["mid"]-reference("mid"),
                raw_end_rung=pair["rung"], sub_end_rung=pair["rung"]-reference("rung"),
                light_pairs=pair["mass_slope"], empty_network=pair["empty_weight"])

def path_coefficient(costs):
    """Sum all orders of building the unique minimal string from zero flux."""
    n = len(costs)
    M = sum(costs)
    weights = {0:1.}
    for mask in range(1,2**n):
        selected = [(mask>>i)&1 for i in range(n)]
        previous = sum(weights[mask^(1<<i)] for i in range(n) if selected[i])
        if all(selected):
            return previous
        gaps = sum(s==0 and (i==0 or selected[i-1]) for i,s in enumerate(selected))
        excess = sum(c*s for c,s in zip(costs,selected))+M*(gaps-1)
        assert excess > 0
        weights[mask] = previous/excess

def tuned(t, coefficient):
    def solve(mass):
        return levels(4,1,1,(1.,2.),mass,t)
    def derivative(mass):
        return np.diff(solve(mass)["mass_slope"])[0]
    mass = brentq(derivative, MASS_PAIR-.35,MASS_PAIR+.35,xtol=2.e-14,rtol=2.e-15)
    E = solve(mass)["energy"]
    gap = E[1]-E[0]
    leading = 2*coefficient*(t/3)**6
    scan = np.unique(np.r_[np.linspace(MASS_PAIR-.35,MASS_PAIR+.35,15),mass-gap,mass,mass+gap])
    scan_gaps = np.array([np.diff(solve(q)["energy"])[0] for q in scan])
    index = np.flatnonzero(scan==mass)[0]
    assert np.all(np.diff(scan_gaps[:index+1])<0) and np.all(np.diff(scan_gaps[index:])>0)
    local = [np.diff(solve(mass+k*gap)["energy"])[0] for k in (-1,1)]
    curvature = (sum(local)-2*gap)/gap**2
    assert curvature>0
    return dict(t=t,mass_pair=mass,gap=gap,leading=leading,ratio=gap/leading,
                mid=solve(mass)["mid"], mass_slopes=solve(mass)["mass_slope"],
                adjacent_gap_ratios=np.array(local)/gap,curvature=curvature,
                mass_scan=scan,scanned_gaps=scan_gaps)

def native(obj):
    if isinstance(obj, np.ndarray):
        return obj.tolist()
    if isinstance(obj, np.generic):
        return obj.item()
    raise TypeError(str(type(obj)))

def main():
    rows = [compare(length,source) for length in (3,4,5) for source in (0,1)]
    control = [compare(3,source,(1.,1.)) for source in (0,1)]
    reflected = compare(3,0,(2.,1.))
    reflect_error = np.max(abs(reflected["sub_mid"][:,::-1]-rows[1]["sub_mid"]))
    dh = 1.e-4
    fd = []
    for dist, row_idx in [(3,1),(5,5)]:
        plus = compare(dist,1,field=dh)
        minus = compare(dist,1,field=-dh)
        derivative = (plus["energy_minus_mesons"]-minus["energy_minus_mesons"])/(2*dh)
        fd.append(dict(length=dist, derivative=derivative,
                       max_error=np.max(abs(derivative-rows[row_idx]["sub_mid"][:,0]))))
    coef = path_coefficient([RUNG,1.,1.,1.,1.,RUNG])
    curves = [tuned(t,coef) for t in (MAIN_T,.30,.225)]
    m0,gap = curves[0]["mass_pair"],curves[0]["gap"]
    offsets = []
    for shift in (-5.,-1.,0.,1.,5.):
        h = compare(4,1,mass_pair=m0+shift*gap)
        offsets.append(dict(gaps=shift,sub_mid=h["sub_mid"],spectrum=h["spectrum"]))
    assert reflect_error < 1.e-8
    assert max(v["max_error"] for v in fd)<1.e-6
    out = dict(t=MAIN_T,rung_cost=RUNG,pair_mass=MASS_PAIR,rows=rows,uniform=control,
               reflected_max_error=reflect_error, finite_difference=fd,
               paths_coefficient=coef,tuning=curves,detunings=offsets)
    (ROOT/"results"/"strip.json").write_text(json.dumps(out,default=native,indent=2)+"\n")
    figure(rows,offsets)

def figure(rows,offsets):
    from matplotlib import pyplot as plt
    fig,(a,b)=plt.subplots(1,2,figsize=(9.3,3.8),layout="constrained")
    for source, shape in (("A","o"),("B","s")):
        points=[row for row in rows if row["source"]==source]
        for level,color in ((0,"#155b79"),(1,"#9b4c26")):
            a.plot([p["length"] for p in points],[p["sub_mid"][level,0] for p in points],
                   marker=shape,ls="-" if source=="B" else ":",color=color,
                   label=f"sources {source}, level {level}")
    a.set(title="Fixed screening mass",xlabel="source separation (bonds)",
          ylabel="subtracted midpoint flux on A",xticks=[3,4,5])
    a.legend(frameon=False,fontsize=8)
    for i,color in [(0,"#155b79"),(1,"#9b4c26")]:
        b.plot([x["gaps"] for x in offsets],[x["sub_mid"][i,0] for x in offsets],
               "o-",color=color,label=f"level {i}")
    b.set(title="Displaced sources, four bonds",xlabel=r"$(2m-2m_*)/\Delta_{\min}$",
          ylabel="subtracted midpoint flux on A")
    b.legend(frameon=False,fontsize=8)
    fig.savefig(ROOT/"results"/"strip.png",dpi=180)
    plt.close(fig)

if __name__=="__main__":
    main()
