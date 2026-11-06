import sys, time, numpy as np
sys.path.insert(0, __import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)), '..'))
from z2core import *
beta, Nt, L, Rmax = 0.70, 6, 12, 4
lat = Z2Lattice(Nt, L, beta, 7, frozen_tau=2)
for i in range(500): lat.sweep()
print('plaq', lat.plaquette())
nv = []
t = time.time()
for i in range(40000):
    lat.sweep()
    nv.append(naive_polyakov(lat, Rmax).mean(axis=1))
nv = np.array(nv)
print('naive time', time.time()-t)
ml = []
t = time.time()
for i in range(800):
    for j in range(4): lat.sweep()
    ml.append(multilevel_polyakov(lat, 2, 50, Rmax).mean(axis=1))
ml = np.array(ml)
print('ml time', time.time()-t)
def blk(a, nb=20):
    a = a[:len(a)//nb*nb].reshape(nb, -1, a.shape[1]).mean(axis=1)
    return a.mean(0), a.std(0, ddof=1)/np.sqrt(nb)
m1, e1 = blk(nv); m2, e2 = blk(ml)
for R in range(Rmax):
    print(R+1, f"naive {m1[R]:.5f}+-{e1[R]:.5f}   multilevel {m2[R]:.5f}+-{e2[R]:.5f}")
