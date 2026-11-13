#!/usr/bin/env python3
"""Author calculations for QCDS-86/1; no lattice simulation or data fitting.

Run from any directory. Produces the printout, JSON, tables and figures beside
this script. Fixed-mass determinants are checked against a momentum integral;
the Gross-Neveu saddle is checked against that integral's derivative and a
direct minimization. N denotes Dirac flavours, not colours. All Gross-Neveu
numbers use m_infinity = 1 and are per flavour at leading order in large N.
"""
from pathlib import Path
import json
import math

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq, minimize_scalar
from scipy.special import k0, k1, zeta, digamma

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
FIGURES = ROOT / "figures"
PI = math.pi
GAMMA = float(np.euler_gamma)
LC = PI * math.exp(-GAMMA)
LOG = []
CHECKS = []


def say(line=""):
    LOG.append(line)
    print(line)


def check(name, error, tolerance):
    passed = bool(abs(error) < tolerance)
    CHECKS.append(dict(name=name, error=float(error), tolerance=tolerance, passed=passed))
    if not passed:
        raise AssertionError(f"{name}: error {error:g} >= {tolerance:g}")


def casimir(m, length, sector="NS"):
    """One nonchiral Dirac fermion; subtract the infinite-line energy."""
    if m == 0:
        return (-PI / 6 if sector == "NS" else PI / 3) / length
    x = m * length
    n = np.arange(1, max(40, math.ceil(40 / x)) + 1, dtype=float)
    signs = (-1.0) ** n if sector == "NS" else np.ones_like(n)
    return float(2 * m / PI * np.sum(signs * k1(n * x) / n))


def casimir_integral(m, length, sector="NS"):
    """Independent momentum-integral representation, not a Bessel sum."""
    if sector == "NS":
        integrand = lambda k: math.log1p(math.exp(-length * math.hypot(k, m)))
    else:
        integrand = lambda k: math.log(-math.expm1(-length * math.hypot(k, m)))
    return -2 / PI * quad(integrand, 0, np.inf, epsabs=2e-11, epsrel=2e-11)[0]


def odd_difference(m, length):
    if m == 0:
        return PI / (2 * length)
    n = np.arange(1, max(40, math.ceil(40 / (m * length))) + 1, 2, dtype=float)
    return float(4 * m / PI * np.sum(k1(n * m * length) / n))


def vacuum(m):
    """Renormalized potential per Dirac flavour, m_infinity = 1."""
    return 0.0 if m == 0 else m * m / (4 * PI) * (2 * math.log(m) - 1)


def potential(m, length, sector="NS"):
    # Subtract V(1) so sigma in the paper is the infinite-line physical tension.
    return vacuum(m) - vacuum(1) + casimir(m, length, sector) / length


def gap(m, length, sector="NS"):
    """pi V_eff'(m)/m, evaluated through a rapidly convergent K0 sum."""
    n = np.arange(1, max(40, math.ceil(40 / (m * length))) + 1, dtype=float)
    signs = (-1.0) ** n if sector == "NS" else np.ones_like(n)
    return float(math.log(m) - 2 * np.sum(signs * k0(n * m * length)))


def saddle(length, sector="NS"):
    if sector == "NS":
        if length <= LC:
            return 0.0
        return brentq(lambda m: gap(m, length, sector), 2e-4, 1.01, xtol=2e-12)
    upper = max(2.0, 4 / length)
    return brentq(lambda m: gap(m, length, sector), 1, upper, xtol=2e-12)


def energy(m, length, sector="NS"):
    return length * potential(m, length, sector)


def main():
    RESULTS.mkdir(exist_ok=True)
    FIGURES.mkdir(exist_ok=True)
    say("QCDS-86/1: author calculations (not an independent referee report)")
    say("A. Closed-string vacuum energies for one nonchiral Dirac fermion")
    say("x=mL     L E_NS       L E_R        L(E_R-E_NS)    c_eff_NS")
    fixed = []
    for x in [0, 0.25, 0.5, 1, 2, 3, 5, 8]:
        ens, er = casimir(x, 1), casimir(x, 1, "R")
        row = dict(x=x, L_E_NS=ens, L_E_R=er, L_difference=er-ens, c_eff_NS=-6*ens/PI)
        fixed.append(row)
        say(f"{x:5.2f}  {ens:12.8f} {er:12.8f} {er-ens:14.8f} {-6*ens/PI:12.8f}")
        for sector in ["NS", "R"]:
            check(f"integral vs sum x={x} {sector}", casimir(x, 1, sector)-casimir_integral(x, 1, sector), 2e-9)
        check(f"odd winding identity x={x}", er-ens-odd_difference(x, 1), 2e-12)

    # Independent small-mass and asymptotic checks, including the zero mode.
    for sector, expected in [("NS", -PI/6), ("R", PI/3)]:
        check(f"massless limit {sector}", casimir_integral(1e-7, 1, sector)-expected, 3e-7)
    for x in [3, 5, 8]:
        leading = 4*x/PI*k1(x)
        check(f"odd sum leading winding x={x}", (odd_difference(x, 1)-leading)/leading, 0.001)
    say("Scalar periodic contribution is -1/2 of the Dirac R contribution.")
    say("Thus one real scalar and one equal-mass Majorana in R cancel exactly at this order.")

    say()
    say("B. Homogeneous large-N Gross-Neveu saddle, m_infinity=1")
    say(f"m_infinity L_c = pi exp(-EulerGamma) = {LC:.10f}")
    say("L       m_NS/m_inf   m_R/m_inf    E_NS/N/m_inf  E_R/N/m_inf   fixed_NS")
    gn = []
    for length in [1, 1.5, LC, 1.8, 2, 2.5, 3, 5, 8]:
        mns, mr = saddle(length), saddle(length, "R")
        ens, er = energy(mns, length), energy(mr, length, "R")
        row = dict(L=length, m_NS=mns, m_R=mr, E_NS=ens, E_R=er,
                   E_fixed_NS=casimir(1, length), E_fixed_R=casimir(1, length, "R"))
        gn.append(row)
        say(f"{length:7.4f} {mns:12.8f} {mr:12.8f} {ens:14.8f} {er:14.8f} {casimir(1,length):12.8f}")
        for sector, mass in [("NS", mns), ("R", mr)]:
            if mass:
                check(f"gap residual L={length} {sector}", gap(mass,length,sector), 1e-9)
                h = 2e-5
                def independent_pot(v):
                    return vacuum(v)-vacuum(1)+casimir_integral(v,length,sector)/length
                deriv = (independent_pot(mass+h)-independent_pot(mass-h))/(2*h)
                check(f"integral stationary L={length} {sector}", deriv, 2e-8)
                minimum = minimize_scalar(independent_pot, bounds=(1e-6, max(3,2*mass)), method="bounded",
                                          options={"xatol":1e-10})
                check(f"independent minimizer L={length} {sector}", minimum.x-mass, 3e-6)
                check(f"nonzero saddle below zero L={length} {sector}", max(0,energy(mass,length,sector)-energy(0,length,sector)),1e-12)
            else:
                for trial in [.01,.1,.5,1,2]:
                    check(f"zero minimum L={length} trial={trial}", max(0,ens-energy(trial,length)), 1e-12)

    say()
    say("C. Critical curvature from a spatial momentum cutoff")
    # Cutoff Lambda=2*pi*M/L. Coupling fixed by the infinite-line gap in the
    # SAME spatial-cutoff scheme: 1/lambda=asinh(Lambda/m_inf)/pi.
    for length in [1,LC,3]:
        count = 100000
        cutoff = 2*PI*count/length
        bare_inv = math.asinh(cutoff)/PI
        mode_sum = (digamma(count+.5)-digamma(.5))/PI
        curvature = bare_inv-mode_sum
        exact = math.log(LC/length)/PI
        say(f"L={length:.8f}: cutoff V''(0)={curvature:.10f}, analytic={exact:.10f}")
        check(f"critical curvature L={length}", curvature-exact, 1e-9)
    near = LC * 1.0001
    predicted_m2 = 8*PI**2/(7*zeta(3,1)*near**2)*math.log(near/LC)
    check("critical quartic coefficient", saddle(near)**2/predicted_m2-1, 5e-4)
    say(f"Quartic coefficient at L_c: 7 zeta(3) L_c^2/(32 pi^3) = {7*zeta(3,1)*LC**2/(32*PI**3):.10f}")

    say()
    say("D. Determinant derivative and variational energy")
    for length in [1,2,5]:
        for mass in [.3,.7,1.2]:
            h=1e-5
            for sector in ["NS","R"]:
                derivative=(potential(mass+h,length,sector)-potential(mass-h,length,sector))/(2*h)
                check(f"V derivative m={mass} L={length} {sector}", derivative-mass/PI*gap(mass,length,sector),2e-9)
    for row in gn:
        for sector in ["NS","R"]:
            check(f"self-consistency lowers E L={row['L']} {sector}", max(0,row['E_'+sector]-row['E_fixed_'+sector]),1e-12)

    say()
    say("E. Group dimensions and critical central-charge bookkeeping")
    for n in [3,5,16]:
        mesons=n*n
        pairs=n*(n-1)//2
        adj=n*(2*n-1)
        check(f"SO(2n) to U(n), n={n}",mesons+2*pairs-adj,1e-12)
        say(f"SO({2*n}) adjoint: {adj} = {mesons} + {pairs} + {pairs}")
    say("RNS flat matter c=3D/2; reparametrization+superconformal ghosts c=-15; D=10.")
    say("Four free embedding supermultiplets have c=6; a critical internal sector must supply c=9.")
    say("Heterotic left internal deficit: 26-10=16; 32 real chiral fermions supply c=16.")
    say("These are critical gauge-fixed counts, not the physical cylinder Casimir count.")

    say()
    say("F. Dimensional matching and rotating-string checks")
    # The formal 4+epsilon flow does not establish a continuum theory in D>4.
    for nc in [2,3]:
        b=11*nc/(48*PI**2)
        for epsilon in [.01,.1]:
            gsq=epsilon/(2*b)
            check(f"epsilon fixed point Nc={nc} eps={epsilon}",epsilon/2-b*gsq,1e-12)
            check(f"epsilon UV eigenvalue Nc={nc} eps={epsilon}",epsilon/2-3*b*gsq+epsilon,1e-12)
        for g4 in [.4,.8]:
            scale=math.exp(-1/(2*b*g4*g4))
            mu=.8
            gmu2=1/(1/g4**2+2*b*math.log(mu))
            check(f"Lambda4 invariant Nc={nc} g={g4}",mu*math.exp(-1/(2*b*gmu2))/scale-1,1e-12)
    eint=2*quad(lambda theta:1,0,PI/2)[0]
    jint=2*quad(lambda theta:math.sin(theta)**2,0,PI/2)[0]
    check("rotating-string energy integral",eint-PI,1e-12)
    check("rotating-string angular momentum integral",jint-PI/2,1e-12)
    check("Regge slope from independent integrals",jint/eint**2-1/(2*PI),1e-12)
    say("Formal epsilon fixed point and UV slope checked; Lambda4 is invariant under one-loop running.")
    say("Rotating-string integrals give E=pi sigma/omega and J=pi sigma/(2 omega^2).")

    say()
    say("G. Compact-coordinate pinning: local Hessian and Gaussian scaling")
    for stiffness in [.02,.1,1,10]:
        shell_width=.03
        # Independent radial momentum integral in a two-dimensional shell.
        variance=quad(lambda k:1/(2*PI*stiffness*k),math.exp(-shell_width),1)[0]
        scaling_dimension=variance/(2*shell_width)
        check(f"vertex dimension kappa={stiffness}",scaling_dimension-1/(4*PI*stiffness),1e-12)
        # The Gaussian average of cos(theta_fast) fixes the linear flow of u.
        averaged=quad(lambda z:math.exp(-z*z/2)*math.cos(math.sqrt(variance)*z)/math.sqrt(2*PI),-10,10)[0]
        inferred_growth=2+math.log(averaged)/shell_width
        check(f"weak pinning flow kappa={stiffness}",inferred_growth-(2-scaling_dimension),1e-11)
        coupling=.07
        step=1e-4
        pinning_potential=lambda y:coupling*2*math.sin(y/(2*math.sqrt(stiffness)))**2
        hessian=(pinning_potential(step)+pinning_potential(-step)-2*pinning_potential(0))/step**2
        check(f"canonical pinning Hessian kappa={stiffness}",hessian/(coupling/stiffness)-1,1e-7)
    say(f"Weak pinning relevance threshold: kappa > 1/(8 pi) = {1/(8*PI):.10f}")
    say(f"For kappa=sigma r^2 this requires M_KK/sqrt(sigma) < sqrt(8 pi) = {math.sqrt(8*PI):.10f}.")
    say("This is a weak-deformation test, not a bound on all compactifications or an exact quantum mass.")

    # Figures are model calculations, never mock data.
    xs=np.linspace(.04,8,240)
    fig,ax=plt.subplots(figsize=(6.8,4.3))
    ax.plot(xs,[-6*casimir(x,1)/PI for x in xs],label="Dirac, antiperiodic")
    ax.plot(xs,[-6*casimir(x,1,"R")/PI for x in xs],label="Dirac, periodic")
    ax.axhline(0,color="black",lw=.5)
    ax.set(xlabel=r"$mL$",ylabel=r"$-6LE_{\rm C}/\pi$",title="Fixed-mass determinant: sector-dependent vacuum energy")
    ax.legend();fig.tight_layout();fig.savefig(FIGURES/"casimir86.pdf");fig.savefig(FIGURES/"casimir86.png",dpi=170);plt.close(fig)
    ls=np.r_[np.linspace(.8,LC-.002,70),np.linspace(LC+.002,6,180)]
    msns=np.array([saddle(v) for v in ls]);msr=np.array([saddle(v,"R") for v in ls])
    fig,axs=plt.subplots(1,2,figsize=(10,4.1))
    axs[0].plot(ls,msns,label="Antiperiodic saddle");axs[0].plot(ls,msr,label="Periodic saddle")
    axs[0].axvline(LC,color="gray",ls=":");axs[0].axhline(1,color="gray",ls="--",lw=.7)
    axs[0].set(xlabel=r"$m_\infty L$",ylabel=r"$s_*/m_\infty$",title="Homogeneous large-N saddle");axs[0].legend(fontsize=8)
    axs[1].plot(ls,[energy(m,v) for m,v in zip(msns,ls)],label="Self-consistent, NS")
    axs[1].plot(ls,[casimir(1,v) for v in ls],ls="--",label="Fixed mass, NS")
    axs[1].set(xlabel=r"$m_\infty L$",ylabel=r"$\Delta E/(N m_\infty)$",title="Vacuum energy above the matched tension");axs[1].legend(fontsize=8)
    fig.tight_layout();fig.savefig(FIGURES/"gap86.pdf");fig.savefig(FIGURES/"gap86.png",dpi=170);plt.close(fig)

    table=["| $mL$ | $LE_{\\rm NS}$ | $LE_{\\rm R}$ | $L(E_{\\rm R}-E_{\\rm NS})$ |", "|---:|---:|---:|---:|"]
    for r in fixed:table.append(f"| {r['x']:g} | {r['L_E_NS']:.6f} | {r['L_E_R']:.6f} | {r['L_difference']:.6f} |")
    (RESULTS/"fixed_mass_table.md").write_text("\n".join(table)+"\n")
    table=["| $m_\\infty L$ | $s_{\\rm NS}/m_\\infty$ | $s_{\\rm R}/m_\\infty$ | $\\Delta E_{\\rm NS}/(Nm_\\infty)$ | Fixed-mass NS |", "|---:|---:|---:|---:|---:|"]
    for r in gn:table.append(f"| {r['L']:.4f} | {r['m_NS']:.6f} | {r['m_R']:.6f} | {r['E_NS']:.6f} | {r['E_fixed_NS']:.6f} |")
    (RESULTS/"gap_table.md").write_text("\n".join(table)+"\n")
    say()
    say(f"PASS: {len(CHECKS)} author checks. No claim of an independent proof or referee review.")
    out=dict(critical_length=LC,fixed_mass=fixed,gross_neveu=gn,checks=CHECKS)
    (RESULTS/"worldsheet86.json").write_text(json.dumps(out,indent=2,allow_nan=False)+"\n")
    (RESULTS/"worldsheet86.txt").write_text("\n".join(LOG)+"\n")


if __name__ == "__main__":
    main()
