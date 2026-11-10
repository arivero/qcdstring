import sys, time, numpy as np
sys.path.insert(0, __import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)), '..'))
from z2ft import Z2FT
Nt,Lx,Ly,hot,seed,n = int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5]),int(sys.argv[6])
beta=float(sys.argv[7]) if len(sys.argv)>7 else 0.73
lat=Z2FT(Nt,Lx,Ly,beta,seed,hot=bool(hot))
V=Nt*Lx*Ly
plq=[];pt=[];py=[];px=[]
for i in range(n):
    lat.sweep()
    plq.append(lat.plaquette_sum()/(3*V))
    pt.append(lat.U[0].prod(axis=0,dtype=np.int8).mean())
    px.append(lat.U[1].prod(axis=1,dtype=np.int8).mean())
    py.append(lat.U[2].prod(axis=2,dtype=np.int8).mean())
plq=np.array(plq);pt=np.array(pt);py=np.array(py);px=np.array(px)
def tau_int(x):
    x=x-x.mean(); n=len(x); v=x.var(); t=0.5
    for k in range(1,n//10):
        t+=(x[:-k]*x[k:]).mean()/v
        if k>6*t: break
    return t
nb=10
print("Nt %d L %dx%d %s n=%d"%(Nt,Lx,Ly,"hot" if hot else "cold",n))
print("  plaq blocks:"," ".join("%.4f"%x for x in plq.reshape(nb,-1).mean(axis=1)), " tau %.0f"%tau_int(plq[n//5:]), "mean(last 80%%) %.5f"%plq[n//5:].mean())
print("  pt^2 blocks:"," ".join("%.4f"%x for x in (pt**2).reshape(nb,-1).mean(axis=1)), " tau(pt) %.0f"%tau_int(pt[n//5:]))
print("  py^2 blocks:"," ".join("%.4f"%x for x in (py**2).reshape(nb,-1).mean(axis=1)), " tau(py) %.0f"%tau_int(py[n//5:]))
print("  px^2 blocks:"," ".join("%.4f"%x for x in (px**2).reshape(nb,-1).mean(axis=1)), " tau(px) %.0f"%tau_int(px[n//5:]))
