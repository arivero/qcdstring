"""Independent one-link SU(3) moment and spectator-factorization controls."""
from itertools import product
import json
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[1]

def colour_integrals():
    # The three-dimensional Weyl matrices have exactly the Haar (1,1)
    # moment. Including the SU(3) centre kills nonzero triality.
    omega = np.exp(2j*np.pi/3)
    X = np.roll(np.eye(3,dtype=complex),1,axis=0)
    Z = np.diag([1,omega,omega**2])
    matrices = [omega**r*np.linalg.matrix_power(X,p)@np.linalg.matrix_power(Z,q)
                for p,q,r in product(range(3),repeat=3)]
    moments = sum(np.einsum("ij,kl->ijkl",u,u.conj()) for u in matrices)/27
    target = np.einsum("ik,jl->ijkl",np.eye(3),np.eye(3))/3
    deleted = sum(u*u.trace().conjugate() for u in matrices)/27
    absent = sum(u*u.trace() for u in matrices)/27
    chars = np.array([[u.trace(),u.trace().conjugate()] for u in matrices])
    gram = chars.conj().T@chars/27
    err = max(np.max(abs(moments-target)),np.max(abs(deleted-np.eye(3)/3)),
              np.max(abs(absent)),np.max(abs(gram-np.eye(2))))
    assert err<1.e-13
    return float(err)

def isolated_link(t, mass_pair, cost, directions, spectator, complete):
    # Additive energies of decoupled spectators cancel in the final contrast.
    gap = mass_pair+cost
    amps = t if complete or not spectator else t/3
    h = np.diag([0.]+[gap]*directions)
    h[0,1:] = -amps
    h[1:,0] = -amps
    vals,vecs = np.linalg.eigh(h)
    return float(vals[0]),float(sum(vecs[1:,0]**2))

def main():
    report = {"haar_first_moment_error":colour_integrals(),"spectator_controls":[]}
    for directions in (1,2):
        for complete in (False,True):
            vac = np.array(isolated_link(.45,6.5,1.,directions,False,complete))
            pair = np.array(isolated_link(.45,6.5,1.,directions,True,complete))
            single = pair.copy()
            delta = pair-2*single+vac
            if complete:
                assert max(abs(delta))<1.e-14
            report["spectator_controls"].append(dict(orientations=directions,
                complete_product_contraction=complete,raw_vacuum=vac.tolist(),
                raw_screened_pair=pair.tolist(),subtracted_energy=float(delta[0]),
                subtracted_midpoint=float(delta[1])))
    (ROOT/"results"/"strip-local.json").write_text(json.dumps(report,indent=2)+"\n")

if __name__=="__main__":
    main()
