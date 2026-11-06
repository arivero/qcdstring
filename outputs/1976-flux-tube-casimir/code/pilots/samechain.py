import sys, time, numpy as np
sys.path.insert(0, __import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)), '..'))
from z2core import *
tau = int(sys.argv[1]); seed = int(sys.argv[2])
beta, Nt, L, Rmax, nsub, nout = 0.70, 6, 12, 4, 20, 6000
lat = Z2Lattice(Nt, L, beta, seed, frozen_tau=tau)
for i in range(2000): lat.sweep()
nslab = Nt//tau
ML, NV = [], []
for o in range(nout):
    for j in range(2): lat.sweep()
    acc = np.zeros((nslab, L, L, Rmax, 2)); nv = np.zeros(Rmax)
    for s in range(nsub):
        lat.sweep(frozen=True)
        Lk = slab_line_products(lat.U, tau).astype(float)
        for R in range(1, Rmax+1):
            acc[..., R-1, 0] += Lk*np.roll(Lk, -R, axis=1)
            acc[..., R-1, 1] += Lk*np.roll(Lk, -R, axis=2)
        nv += naive_polyakov(lat, Rmax).mean(axis=1)
    ML.append((acc/nsub).prod(axis=0).mean(axis=(0,1)).mean(axis=1)); NV.append(nv/nsub)
ML, NV = np.array(ML), np.array(NV)
D = ML - NV
def be(a, nb=30):
    a = a[:len(a)//nb*nb].reshape(nb,-1,a.shape[1]).mean(1); return a.mean(0), a.std(0,ddof=1)/np.sqrt(nb)
m1,e1 = be(NV); m2,e2 = be(ML); d,ed = be(D)
print('tau', tau, 'seed', seed)
for R in range(Rmax):
    print(f" R={R+1} naive {m1[R]:.5f}({e1[R]:.5f}) ml {m2[R]:.5f}({e2[R]:.5f}) diff {d[R]:+.5f}({ed[R]:.5f}) pull {d[R]/ed[R]:+.2f}")
