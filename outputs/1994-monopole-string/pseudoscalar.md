# The pseudoscalar on a string carrying fundamental electric flux

At leading semiclassical order, the unit string in the weakly broken monopole vacuum supports a normalizable odd excitation. It has a nonzero matrix element to two transverse phonons. For sufficiently small breaking its mass lies below the lightest bulk particle, including the additional chiral multiplets of the dual theory. These are statements about a string between external fundamental electric probes in pure $\mathcal N=2$ $SU(2)$ deformed to $\mathcal N=1$. The calculation uses the two-derivative, constant-coupling action and the vacuum, profiles, and parameter $w$ defined in [the monopole-vacuum calculation](monopole-vacuum.md).

## A physical polarization in the full bosonic field equations

Let $A^c=A/g$ be the canonically normalized dual photon. Perturb the static string by $\delta A^c_a=\psi(r)b_a(t,z)$, $a=0,3$, with $\partial_a b^a=0$ and all other variations zero. The linear sources for the phases of $q,\tilde q$ and for the transverse connection are proportional to $\partial_a b^a$. The static fields have zero sheet derivatives; the neutral scalar carries no gauge charge. At rest this is a time-dependent $A^c_z$ with $\delta A^c_0=0$ and the Gauss equation satisfied. Thus even for a nonconstant neutral background no imposed scalar truncation is needed in the **fluctuation** equation. With $\int d^2x\,\psi^2=1$, put $\psi=m_\gamma u(\rho)$ and $m_{\rm odd}=m_\gamma\nu$. The radial and sheet equations are
$$
 L_f u=\nu^2 u,\qquad 2\pi\int_0^\infty\rho u^2d\rho=1,
 \qquad (\Box_{1,1}-m_{\rm odd}^2)b_a=0.
$$
The restoring mass density is $2g^2(|q|^2+|\tilde q|^2)=m_\gamma^2 f^2$. The gauge-invariant electric field $\delta F^c_{03}$ is nonzero. The defect insertion $\int d^2x\, F^c_{12}\delta F^c_{03}$ is even under reversal of the dual charge convention. Equivalently it is the linearized transverse integral of $F^c\wedge F^c$ up to an orientation and a constant. It is odd under longitudinal reflection and under the transverse reflection combined with flux reversal that preserves the unit vortex. Its scalar under transverse rotations therefore has the pseudoscalar two-phonon channel. A particular microscopic local operator would require its own matching coefficient. The electric Wilson line fixes the flux sector without that choice.

## Binding, threshold and residue

For a radial minimizer of the stated energy one can choose $0\le f\le1$ and $s\ge0$ for $w\ge0$. Replacing $f$ with $\min(|f|,1)$ and $s$ with its positive part decreases or preserves the gradients and angular cost. If $f^2>1$ and $s<0$ both replacements set the potential to zero. In the other three sign regions the change decreases or preserves $f^2s^2$ and $(f^2-1+2ws)^2$ separately. The regular vortex has $f(0)=0$. Since $f\to1$, the bottom of the vector bulk continuum in these units is 1. A trial wave equal to one on a fixed core disk, falling linearly in $\log\rho$ out to radius $R$, costs only $2\pi/\log(R/R_{\rm core})$ in gradient energy and gains a fixed positive amount from $1-f^2$ in the core. Therefore $0<\nu^2<1$. Strict positivity follows from the positive quadratic form and the location of the essential spectrum. The ground state is simple, radial and has one sign.

The same radial proof applies on the positive minimizing branch at other $w$ in this effective action. Below *all* bulk one-particle thresholds is a stronger test. At $w=0$ the computed radial eigenvalue is $\nu_0^2=0.77747281$ and $m_-/m_\gamma=1$. The finite gap, continuity of the centered profiles and isolated-eigenvalue perturbation then put $m_{\rm odd}<m_-$ on an open interval at small $w$. In particular the scalar bulk threshold moves at order $w$, while $f$ and hence $\nu^2$ are even in signed $w$. This proof gives no cutoff in the microscopic ratio $|\mu|/\Lambda$ for arbitrary breaking.

Put $B_D=F^c_{12}$, $\mathcal I=\int B_D\psi\,d^2x$ and $\alpha=g\mathcal I/m_\gamma=2\pi\int a' u\,d\rho$. The static Maxwell equation gives $((a'/\rho)')=-f^2(1-a)/\rho$. The regular positive unit solution has $0\le a\le1$, with $a'/\rho>0$, so $\mathcal I$ is strictly positive for a positive ground state. Translate **all** the static fields with the center. The pullback of the transverse magnetic two-form supplies $-\mathcal I(\partial^a b^b-\partial^b b^a)\epsilon_{ij}\partial_aX^i\partial_bX^j/2$. The neutral kinetic term contributes to the translation norm, with no term linear in $b_a$. On the fixed slice the two charged kinetic terms sum to $|D H|^2$. A boost fixes the translation norm to the actual string tension $\sigma$, including the neutral adjustment. The on-shell matching to the normal curvature of the sheet then gives
$$
 |Q_{\rm odd}|=\frac{\mathcal I}{m_{\rm odd}},\qquad
 \mathcal C(w)=\frac{|Q_{\rm odd}|m_{\rm odd}}{\sqrt\sigma}
              =\frac{\alpha(w)}{\sqrt{\pi\tau(w)}} .
$$
In particular, two oppositely moving phonons of perpendicular polarization excite the state with ordered amplitude $|V_{12}|=\mathcal I m_{\rm odd}^3/(2\sigma)$; exchanging the polarizations reverses its sign. The trace has zero direct residue from this state. No coupling was fitted to a string spectrum. At the Bogomolny limit $m_{\rm odd}/\sqrt\sigma=0.497471g$, $g|Q_{\rm odd}|=1.20101$ and $\mathcal C(0)=0.597469$. These use the radial solution already obtained in [QCDS-91/S1, Eqs. (15)–(25)](../1991-vortex-pseudoscalar/paper.md); the charge dictionary and the additional bulk-threshold test are essential to their present interpretation.

The isolated eigenvalue is a transverse bound state of the classical linearized equations. Two massless string translations are available in the interacting theory. Their partial width at weak dual coupling follows from the same residue, $\Gamma_{12}/m_{\rm odd}=|Q_{\rm odd}|^2m_{\rm odd}^4/(8\sigma^2)$, which is $0.01104g^2$ at criticality. Extra decay channels, including fermionic string excitations, are separate. At small breaking and weak coupling this gives a polarized resonance rather than a claim of an eternally stable massive particle.

## The first correction to the odd pole

Set $x=w^2$, $f=f_0+x f_2+O(x^2)$ and $a=a_0+x a_2+O(x^2)$. Fix photon mass units. Differentiating the two static equations with respect to $x$ gives an inhomogeneous radial problem with regular axis and decaying outer boundary,
$$
\begin{aligned}
 f_2''+f_2'/\rho &=
 \left[(1-a_0)^2/\rho^2+(3f_0^2-1)/2\right]f_2
 -2(1-a_0)f_0 a_2/\rho^2 + f_0(s_1+s_1^2),\\
 a_2''-a_2'/\rho &=f_0^2 a_2-2(1-a_0)f_0 f_2,
 \qquad s_1=(1-a_0)/2 .
\end{aligned}
$$
Let $\langle h,k\rangle=2\pi\int\rho h k\,d\rho$. With the positive eigenfunction normalized at every $w$, write $u=u_0+x u_2+O(x^2)$ and $\nu^2=\nu_0^2+x\lambda_2+O(x^2)$. The eigenvalue derivative and reduced resolvent are
$$
 \lambda_2=\langle u_0,2f_0 f_2 u_0\rangle,\qquad
 (L_{f_0}-\nu_0^2)u_2=(\lambda_2-2f_0 f_2)u_0,
 \qquad \langle u_0,u_2\rangle=0 .
$$
Both the flux profile and the wave change. The derivative of the magnetic overlap is $\alpha_2=2\pi\int(a'_2u_0+a'_0u_2)d\rho$, and the tension contributes $+\alpha_0/8$ to the numerator of the derivative of $\mathcal C$. The numerical result in the constant-coupling dual action is
$$
 \nu=0.8817442-0.15343\,w^2+O(w^4),\qquad
 g|Q_{\rm odd}|=1.201013+0.0882\,w^2+O(w^4),\qquad
 \mathcal C=0.5974688+0.0146\,w^2+O(w^4).
$$
The small positive last coefficient reflects a cancellation. The magnetic overlap drops as the vortex relaxes, while the smaller tension raises the ratio.

| $w$ | $\sigma/(2\pi v^2)$ | $m_{\rm odd}/m_\gamma$ | $m_-/m_\gamma$ | $g\lvert Q_{\rm odd}\rvert$ | $\mathcal C$ |
|---:|---:|---:|---:|---:|---:|
| 0 | 1 | 0.881744 | 1 | 1.201013 | 0.597469 |
| 0.025 | 0.999844 | 0.881648 | 0.987578 | 1.201068 | 0.597478 |
| 0.05 | 0.999375 | 0.881361 | 0.975312 | 1.201232 | 0.597505 |
| 0.10 | 0.997508 | 0.880212 | 0.951249 | 1.201884 | 0.597608 |
| 0.20 | 0.990124 | 0.875638 | 0.904988 | 1.204384 | 0.597957 |
| 0.30 | 0.978129 | 0.868104 | 0.861187 | 1.208196 | 0.598324 |

The rows solve the nonlinear three-profile background anew at each input. They independently test the expansion. The table also shows why using the photon threshold alone would be misleading. The odd mass equals the lightest scalar bulk mass near $w=0.27974$ in this action. The longitudinal vector channel still binds above this equality, since it is an invariant linear sector. Establishing an actual decay there requires a coupling, phase space, and the appropriate conserved quantum numbers. The larger values of $w$ are effective-theory controls. They do not define a new boundary of the microscopic Seiberg–Witten regime.

At $w=0.10$ the lightest bulk mass exceeds the odd mass by $0.07104\,m_\gamma$. On a periodically closed straight tube the first free counterpropagating phonon pair meets the odd mode at $L m_\gamma=4\pi/\nu=14.277$. The off-diagonal two-state matrix element follows from canonical external legs and the antisymmetric polarization. With only these levels in the crossing it gives $2|v_A|/m_{\rm odd}=0.08382g$. The two-phonon partial width is $\Gamma_{12}/m_{\rm odd}=0.01104g^2$. Extra degenerate states would require diagonalizing the full mixing matrix, in particular in a supersymmetric spin sector. [Finite-volume normalization, QCDS-91/S1, Eq. (31)](../1991-vortex-pseudoscalar/paper.md#102-a-test-on-a-periodic-tube)

The Python/SciPy calculation uses the earlier Bessel-tail solver for the odd state, nonlinear collocation for the relaxed background, and a separate cell-centered linear-response calculation with a normalization constraint. It checks unit flux, the magnetic/current identity, the scale virial identity, the on-shell tension derivative, and the effect of changing the outer radius from 36 to 28 at $w=0.10$. At mesh spacings $0.04,0.02,0.01$ the derivative of $\mathcal C$ with respect to $w^2$ is $0.0145364,0.0145661,0.0145735$. The nonlinear difference between $w=0$ and $0.01$ gives $0.01457$. These are mesh and range comparisons without rigorous numerical error bars. From the repository root run `OPENBLAS_NUM_THREADS=1 python3 outputs/1994-monopole-string/code/soft_vortex.py`. [Source](code/soft_vortex.py) · [Numerical results](results/spectrum.json)

## Microscopic scope

Along the small-$|\mu|/|\Lambda|$ trajectory, the Higgs and photon masses are parametrically below $|\Lambda|$ and the renormalized dual coupling is weak asymptotically. The leading bound-state separation from the bulk is finite in $m_\gamma$ units. Small corrections respecting the symmetries can shift or split a degenerate localized multiplet while preserving subthreshold spectral weight in the odd channel. The parity-resolved residue and its numerical corrections below refer to the specified classical dual action. Field dependence of the gauge kinetic function, including a possible coupling of a neutral fluctuation to $F^c\widetilde F^c$, higher-derivative operators, and loop corrections can modify the pole and its distribution among nearby states. No continuation of this unprotected mass or residue to large soft breaking or to pure Yang–Mills has been established.
