import sys, time, numpy as np
sys.path.insert(0, __import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)), '..'))
from z2core import *
beta = float(sys.argv[1]); mh = sys.argv[2] == '1'; nsub = int(sys.argv[3])
lat = Z2Lattice(24, 24, beta, 5, frozen_tau=2)
for i in range(800): lat.sweep()
C = []
t = time.time()
for i in range(12):
    for j in range(5): lat.sweep()
    C.append(multilevel_polyakov(lat, 2, nsub, 12, multihit=mh).mean(axis=1))
C = np.array(C)
m = C.mean(0); s = C.std(0, ddof=1)/np.sqrt(len(C))
print(f"beta {beta} multihit {mh} nsub {nsub} time {time.time()-t:.0f}s")
for R in range(12):
    print(f"  R={R+1:2d} C={m[R]: .3e} rel.err={s[R]/abs(m[R]):.3f} V={-np.log(abs(m[R]))/24:.4f}")
