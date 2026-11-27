"""Check P33 from the four Weyl fields, with critical modes of the existing solver."""
from functools import lru_cache
import importlib.util
from pathlib import Path
import numpy as np

source = Path(__file__).resolve().parents[2] / "1992-scalar-doublet/code/trace_spectrum.py"
spec = importlib.util.spec_from_file_location("trace_spectrum", source)
radial = importlib.util.module_from_spec(spec)
spec.loader.exec_module(radial)


@lru_cache(maxsize=None)
def profile(w, radius):
    return radial.static_solution(w, radius, 0.0, 1)


def weyl_matrix(phi, s, w):
    matrix = np.zeros((4, 4, *phi.shape), dtype=complex)
    matrix[0, 1] = matrix[1, 0] = s
    matrix[0, 2] = matrix[2, 0] = phi.conj()
    matrix[0, 3] = matrix[3, 0] = phi.conj()
    matrix[1, 2] = matrix[2, 1] = phi
    matrix[1, 3] = matrix[3, 1] = -phi
    matrix[2, 2] = w
    return matrix


def lift(amplitudes, b, e, h):
    ap, bp, am, bm = amplitudes
    psi = np.zeros((4, 2, *e.shape), dtype=complex)
    psi[0, 0] = e*ap
    psi[1, 1] = (e*am).conj()
    plus = np.broadcast_arrays((b*ap).conj(), -1j*h*bp.conjugate())
    minus = np.broadcast_arrays(1j*h*bm, b*am)
    psi[2] = (np.asarray(plus)+np.asarray(minus))/np.sqrt(2)
    psi[3] = (np.asarray(plus)-np.asarray(minus))/np.sqrt(2)
    return psi


def compression(w, radius, spacing, ntheta, *, omit_core=False):
    mesh = radial.RadialElements(radius, spacing)
    r = mesh.r.reshape(-1, 1)
    wgt = mesh.measure.reshape(-1, 1)/ntheta
    angle = np.exp(2j*np.pi*np.arange(ntheta)/ntheta)
    f0, _, a0, _, s0, _ = profile(0.0, radius).sol(np.log(r[:, 0]))[:, :, None]
    fw, _, aw, _, sw, _ = profile(w, radius).sol(np.log(r[:, 0]))[:, :, None]
    natural = slice(0, -1)
    op = mesh.kinetic + mesh.multiplication(f0.reshape(mesh.r.shape)**2)
    val, vec = radial.normalized_modes(op[natural, natural], mesh.mass[natural, natural], 1)
    nu = np.sqrt(val[0])
    nodes = np.r_[vec[:, 0], 0.]
    h = mesh.interpolate(nodes).reshape(-1, 1)
    hp = np.broadcast_to(mesh.derivative(nodes), mesh.r.shape).reshape(-1, 1)
    b = -1j*angle*hp/nu
    e = angle*f0*h/nu
    dm = (weyl_matrix(fw*angle/np.sqrt(2), 0*sw if omit_core else sw, w)
          - weyl_matrix(f0*angle/np.sqrt(2), s0, 0.0))
    delta_connection = (aw-a0)/r
    generator = np.empty((8, 8))
    for col in range(8):
        amp = np.zeros(4, dtype=complex)
        amp[col % 4] = 1 if col < 4 else 1j
        psi = lift(amp, b, e, h)
        eps_conjugate = np.stack((psi[:, 1].conj(), -psi[:, 0].conj()), axis=1)
        out = 1j*np.einsum("ijrt,jsrt->isrt", dm.conj(), eps_conjugate)
        for field, charge in [(0, 1), (1, -1)]:
            out[field, 0] -= charge*delta_connection*angle.conj()*psi[field, 1]
            out[field, 1] += charge*delta_connection*angle*psi[field, 0]
        plus, minus = (out[2]+out[3])/np.sqrt(2), (out[2]-out[3])/np.sqrt(2)
        projected = np.array([
            np.sum(wgt*(b.conj()*plus[0].conj()+e.conj()*out[0, 0])),
            np.sum(wgt*h*(-1j*plus[1].conj())),
            np.sum(wgt*(b.conj()*minus[1]+e.conj()*out[1, 1].conj())),
            np.sum(wgt*h*(-1j*minus[0]))])
        ap, bp, am, bm = amp
        projected += nu*np.array([-bp, ap, -bm, am])
        generator[:, col] = np.r_[projected.real, projected.imag]
    if np.linalg.norm(generator + generator.T, ord=np.inf) > 1e-10:
        raise ArithmeticError("The projected real Weyl evolution lost skew symmetry.")
    eigenvalues = np.linalg.eigvalsh(1j*generator)
    return (eigenvalues[4:]-nu)/w


def slopes(radius, spacing, ntheta, w, **kwargs):
    full = compression(w, radius, spacing, ntheta, **kwargs)
    half = compression(w/2, radius, spacing, ntheta, **kwargs)
    return 2*half-full


if __name__ == "__main__":
    target = np.array([-.25, -.25, .25, .25])
    for radius, h, nt, w in [(24, .08, 8, .01), (28, .04, 12, .005), (32, .02, 16, .0025)]:
        actual = slopes(radius, h, nt, w)
        print(f"R={radius} h={h:g} angles={nt} w={w:g}: {actual}")
        if np.max(abs(actual-target)) > .01:
            raise ArithmeticError("Registered P33 tolerance failed.")
    altered = slopes(28, .04, 12, .005, omit_core=True)
    print(f"control without the induced core mass: {altered}")
