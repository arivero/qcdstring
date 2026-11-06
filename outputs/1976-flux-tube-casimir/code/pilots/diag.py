import sys, time, numpy as np
sys.path.insert(0, __import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)), '..'))
from z2core import *
beta=0.73; Nt=24; L=24; tau=int(sys.argv[1]); nsub=int(sys.argv[2])
lat = Z2Lattice(Nt, L, beta, 5, frozen_tau=tau)
for i in range(800): lat.sweep()
nslab = Nt//tau
Rs = [2,4,6,8,10]
# accumulate in blocks to get error of slab averages
nb = 10
blocks = np.zeros((nb, nslab, L, L, len(Rs)))
t=time.time()
for b in range(nb):
    for s in range(nsub//nb):
        lat.sweep(frozen=True)
        Lk = slab_line_products(lat.U, tau).astype(float)
        for j,R in enumerate(Rs):
            blocks[b,:,:,:,j] += Lk*np.roll(Lk,-R,axis=1)
blocks /= (nsub//nb)
A = blocks.mean(0); dA = blocks.std(0, ddof=1)/np.sqrt(nb)
print('tau',tau,'nsub',nsub,'time',time.time()-t)
for j,R in enumerate(Rs):
    a = A[...,j]; d = dA[...,j]
    prod = a.prod(axis=0)
    print(f"R={R}: mean|A|={np.abs(a).mean():.3f} rms A={np.sqrt((a**2).mean()):.3f} mean err={d.mean():.3f} frac|A|<2err={np.mean(np.abs(a)<2*d):.2f}  prod mean={prod.mean():.2e} prod rms={np.sqrt((prod**2).mean()):.2e}  expect~{np.exp(-Nt*(0.13+0.045*(R-1))):.1e}")
