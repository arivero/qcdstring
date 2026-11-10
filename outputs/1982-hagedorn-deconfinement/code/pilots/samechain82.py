# same-chain comparison of two-level and plain estimators on a small lattice
import sys, numpy as np
sys.path.insert(0, __import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)), '..'))
from z2ft import Z2FT, wall_corr_plain, two_level_wall
import z2ft
def both(lat, n_sub, X):
    ns, Lx, Ly = len(lat.slabs), lat.Lx, lat.Ly
    acc = np.zeros((ns, X + 1, Lx, Ly, Ly)); idx = (np.arange(Ly)[:, None] + np.arange(Ly)[None, :]) % Ly
    pl = np.zeros(X+1)
    for _ in range(n_sub):
        lat.sweep(frozen=True)
        l = lat.slab_lines()
        for dx in range(X + 1):
            acc[:, dx] += l[:, :, :, None] * np.roll(l, -dx, axis=1)[:, :, idx]
        pl += wall_corr_plain(lat.polyakov(), X)
    return (acc / n_sub).prod(axis=0).sum(axis=3).mean(axis=(1, 2)), pl/n_sub
for (Nt, slabs) in ((4,[2,2]),(6,[3,3]),(5,[3,2])):
    lat = Z2FT(Nt, 12, 8, 0.70, 7, slabs=slabs)
    for _ in range(500): lat.sweep()
    A=[];B=[]
    for i in range(3000):
        lat.sweep(); lat.sweep()
        a,b = both(lat, 10, 4); A.append(a); B.append(b)
    A=np.array(A);B=np.array(B); D=A-B
    n=len(A)
    print("Nt",Nt,slabs)
    for x in range(5):
        print("  dx=%d plain %.5f(%.5f) two-level %.5f(%.5f) diff %.5f(%.5f) pull %.2f"%(x,B[:,x].mean(),B[:,x].std()/np.sqrt(n),A[:,x].mean(),A[:,x].std()/np.sqrt(n),D[:,x].mean(),D[:,x].std()/np.sqrt(n),D[:,x].mean()/(D[:,x].std()/np.sqrt(n))))
