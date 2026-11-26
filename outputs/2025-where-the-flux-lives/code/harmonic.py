"""Signed axial-mode matching on the polar metric, with independent FE and shooting checks."""
from pathlib import Path
import json
import math

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
from scipy import sparse
from scipy.sparse.linalg import eigsh

ROOT = Path(__file__).resolve().parents[1]

def background(b, end, method):
    eps = np.exp(-b)
    def rhs(t, state):
        v, vprime = state
        shape = np.exp(-v-eps*np.expm1(-v))
        return [vprime, -2*shape*np.expm1(-b-v)]
    sol = solve_ivp(rhs, [0,end],[0,0],method=method,rtol=2.e-12,atol=2.e-14,
                    max_step=.16,dense_output=True)
    if not sol.success:
        raise RuntimeError(sol.message)
    def fields(t):
        v = sol.sol(np.asarray(t).ravel())[0].reshape(np.shape(t))
        return 2*np.exp(-v-eps*np.expm1(-v)), eps*np.exp(-v)
    return fields

def rule(end, step):
    n = round(end/step)
    assert abs(end/n-step)<1.e-10
    g,w = np.polynomial.legendre.leggauss(5)
    u = (1+g)/2
    return (np.arange(n)[:,None]+u)*step, w*step/2, np.column_stack((1-u,u))

def moments(t,weight,f2,p,values,odd):
    mu = f2*weight
    mu = mu/np.sum(mu)
    phi = values/np.sqrt(np.sum(mu*values**2))
    # Choose the sign near the largest positive-t endpoint for the first odd
    # eigenfunction, and at the equator for the first excited even one.
    sign_reference = phi[-1,-1] if odd else phi[0,0]
    phi = phi*np.sign(sign_reference)
    parity = -1 if odd else 1
    right = np.exp(p/2)
    root_density = right*np.sqrt(p)
    pos = root_density*np.exp(t)
    neg = root_density*np.exp(-t)
    den = np.sum(mu*(pos+neg))
    return dict(area_mean=float((1+parity)*np.sum(mu*phi)/2),
                right=float((1+parity)*np.sum(mu*right*phi)/(2*np.sum(mu*right))),
                plus=float(np.sum(mu*(pos+parity*neg)*phi)/den),
                minus=float(np.sum(mu*(neg+parity*pos)*phi)/den))

def finite_elements(b, end, step):
    fields = background(b,end,"RK45")
    t,w,basis = rule(end,step)
    f2,p = fields(t)
    n = len(t)
    elems = np.column_stack((np.arange(n),np.arange(1,n+1)))
    rows = np.broadcast_to(elems[:,:,None],(n,2,2)).ravel()
    cols = np.broadcast_to(elems[:,None,:],(n,2,2)).ravel()
    def matrix(local):
        return sparse.coo_matrix((local.ravel(),(rows,cols)),shape=(n+1,n+1)).tocsr()
    mass = matrix(np.einsum("iq,qa,qb->iab",w*f2,basis,basis))
    stiff = matrix(np.broadcast_to(np.array([[1.,-1.],[-1.,1.]])/step,(n,2,2)))
    out={}
    for odd in (True,False):
        start = int(odd)
        # A shift below zero keeps the Neumann constant mode regular.
        e,vs = eigsh(stiff[start:,start:], M=mass[start:,start:], k=2,
                     sigma=-.025,tol=2.e-12,v0=np.linspace(1.,2.,n+1-start))
        idx = np.argsort(e)[0 if odd else 1]
        nodes = np.r_[0.,vs[:,idx]] if odd else vs[:,idx]
        values = nodes[elems] @ basis.T
        info = moments(t,w,f2,p,values,odd)
        info["lambda"] = float(e[idx])
        out["odd" if odd else "even"] = info
    return out

def shooting(b, end):
    fields = background(b,end,"DOP853")
    t,w,_ = rule(end,.10)
    f2,p = fields(t)
    out = {}
    for odd in (True,False):
        def solve(lam,dense=False):
            def ode(x,y):
                return [y[1],-lam*float(fields(x)[0])*y[0]]
            sol = solve_ivp(ode,[0,end],[0,1] if odd else [1,0],
                            method="DOP853",rtol=1.e-11,atol=2.e-13,
                            max_step=.35,dense_output=dense)
            if not sol.success:
                raise RuntimeError(sol.message)
            return sol
        def mismatch(lam):
            return solve(lam).y[1,-1]
        low,high=.001,.003
        while mismatch(low)*mismatch(high)>0:
            low,high=high,1.65*high
            if high>25:
                raise ValueError("First eigenvalue was not bracketed")
        lam=brentq(mismatch,low,high,xtol=8.e-14)
        values=solve(lam,True).sol(t.ravel())[0].reshape(t.shape)
        nodes=int(np.count_nonzero(np.diff(np.sign(values.ravel()))))
        assert nodes==(0 if odd else 1)
        info=moments(t,w,f2,p,values,odd)
        info.update({"lambda":lam,"interior_half_nodes":nodes})
        out["odd" if odd else "even"]=info
    return out

def main():
    members={}
    for name,b in [("neck",.001),("near_round",19.)]:
        shoot=shooting(b,25.)
        coarse=finite_elements(b,25.,.04)
        fine=finite_elements(b,25.,.01)
        tail=finite_elements(b,32.,.02)
        for parity in ("odd","even"):
            a,z=shoot[parity],fine[parity]
            assert abs(a["lambda"]/z["lambda"]-1)<5.e-4
            assert max(abs(a[k]-z[k]) for k in ("right","plus","minus"))<3.e-4
            assert abs(z["lambda"]/tail[parity]["lambda"]-1)<2.e-4
            assert abs(a["area_mean"])<1.e-9
        assert shoot["odd"]["plus"]>0 and abs(shoot["odd"]["right"])<1.e-12
        if name=="near_round":
            assert abs(shoot["odd"]["plus"]-1/math.sqrt(3))<1.e-6
            assert abs(shoot["odd"]["lambda"]-1)<1.e-6
        members[name]=dict(b=b,shooting=shoot,fem_step_004=coarse,
                           fem_step_001=fine,fem_cap_32_step_002=tail)
    (ROOT/"results"/"harmonics.json").write_text(json.dumps(members,indent=2)+"\n")

if __name__=="__main__":
    main()
