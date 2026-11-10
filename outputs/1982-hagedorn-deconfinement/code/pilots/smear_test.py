import sys, time, numpy as np
sys.path.insert(0, __import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)), '..'))
from z2ft import Z2FT
def smear_ty(U0, Uy, n, c=0.5):
    """smear time-like and y links within each x = const plane; arrays (Nt, Lx, Ly), t axis 0, y axis 2"""
    a, b = U0.astype(float), Uy.astype(float)
    for _ in range(n):
        up_a = b * np.roll(a, -1, axis=2) * np.roll(b, -1, axis=0)
        dn_a = np.roll(b, 1, axis=2) * np.roll(a, 1, axis=2) * np.roll(np.roll(b, 1, axis=2), -1, axis=0)
        up_b = a * np.roll(b, -1, axis=0) * np.roll(a, -1, axis=2)
        dn_b = np.roll(a, 1, axis=0) * np.roll(b, 1, axis=0) * np.roll(np.roll(a, 1, axis=0), -1, axis=2)
        a, b = (a + c * (up_a + dn_a)) / (1 + 2 * c), (b + c * (up_b + dn_b)) / (1 + 2 * c)
    return a, b
def run(Nt, Lx, Ly, nmeas, levels=(0,1,2,4,8), X=8, beta=0.73, seed=5, c=0.5):
    lat = Z2FT(Nt, Lx, Ly, beta, seed)
    for _ in range(600): lat.sweep()
    nl=len(levels); C=np.zeros((nmeas, X+1, nl, nl))
    for i in range(nmeas):
        lat.sweep()
        a, b = lat.U[0], lat.U[2]
        W=[]; done=0
        a_, b_ = a.astype(float), b.astype(float)
        for n in levels:
            a_, b_ = smear_ty(a_, b_, n-done, c); done=n
            W.append(a_.prod(axis=0).sum(axis=1))     # wall sums (Lx,)
        W=np.array(W)
        for dx in range(X+1):
            C[i,dx] = (W[:,None,:]*np.roll(W,-dx,axis=1)[None,:,:]).mean(axis=2)/Ly
    return C, lat.link_updates*20
def report(C, levels, nb=30):
    n=len(C)//nb; B=C[:n*nb].reshape(nb,n,*C.shape[1:]).mean(axis=1); g=B.mean(axis=0)
    for k,lev in enumerate(levels):
        def eff(g): return np.log(g[:-1,k,k]/g[1:,k,k])
        e=eff(g); js=np.array([eff((g*nb-B[i])/(nb-1)) for i in range(nb)]); de=np.sqrt((nb-1)*js.var(axis=0))
        print("  smear %d: G(1)/G(0)=%.3f  "%(lev, g[1,k,k]/g[0,k,k]) + " ".join("%.4f(%.0f)"%(e[x],1e4*de[x]) for x in range(5)))
for (Nt,Lx,Ly,nm) in ((12,48,16,6000),(16,48,16,6000),(8,48,16,6000)):
    t0=time.time(); levels=(0,1,2,4,8)
    C,fl=run(Nt,Lx,Ly,nm,levels)
    print("Nt",Nt,Lx,Ly,"flop %.2e"%fl,"sec %.0f"%(time.time()-t0)); report(C,levels)
