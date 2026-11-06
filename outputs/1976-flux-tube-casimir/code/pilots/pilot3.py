import sys, time, numpy as np
sys.path.insert(0, __import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)), '..'))
from z2core import *
beta = float(sys.argv[1]); tau = int(sys.argv[2]); nsub = int(sys.argv[3]); nout = int(sys.argv[4]); Nt = int(sys.argv[5])
lat = Z2Lattice(Nt, 32, beta, 17, frozen_tau=tau)
for i in range(800): lat.sweep()
C = []
t = time.time()
for i in range(nout):
    for j in range(5): lat.sweep()
    C.append(multilevel_polyakov(lat, tau, nsub, 10, multihit=False).mean(axis=1))
C = np.array(C)
m = C.mean(0); s = C.std(0, ddof=1)/np.sqrt(len(C))
print(f"beta {beta} Nt {Nt} tau {tau} nsub {nsub} nout {nout} time {time.time()-t:.0f}s")
for R in range(10):
    print(f"  R={R+1:2d} C={m[R]: .3e} rel.err={s[R]/abs(m[R]):.3f} V={-np.log(abs(m[R]))/Nt:.4f} dV={s[R]/abs(m[R])/Nt:.4f}")
