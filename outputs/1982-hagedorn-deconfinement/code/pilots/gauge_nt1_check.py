import sys, time, math
import numpy as np
sys.path.insert(0, __import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)), '..'))
from z2ft import Z2FT, wall_corr_plain, two_level_wall, class_masks
# class masks sanity: no two links of a class share a plaquette
for shape in [(5,8,6),(4,8,6),(3,6,6),(7,8,8),(2,6,6)]:
    m = class_masks(shape)
    for mu in range(3):
        tot = sum(x.astype(int) for x in m[mu])
        assert (tot==1).all()
        for cl in m[mu]:
            for nu in range(3):
                if nu==mu: continue
                assert not (cl & np.roll(cl,1,axis=nu)).any(), (shape,mu,nu)
print("class masks ok")
# timing
t0=time.time()
lat = Z2FT(1, 64, 64, 0.40, 1)
for _ in range(2000): lat.sweep()
G=[]
for i in range(20000):
    lat.sweep()
    G.append(wall_corr_plain(lat.polyakov(), 16))
G=np.array(G); print("time", time.time()-t0)
B=G.reshape(40,-1,17).mean(axis=1)
g=B.mean(axis=0)
m_exact = math.log(1/math.tanh(0.40)) - 0.8
def eff(g): return np.log(g[:-1]/g[1:])
e=eff(g); nb=len(B)
js=np.array([eff((g*nb-B[i])/(nb-1)) for i in range(nb)])
de=np.sqrt((nb-1)*js.var(axis=0))
print("exact", m_exact)
for x in range(12): print(x, e[x], de[x])
