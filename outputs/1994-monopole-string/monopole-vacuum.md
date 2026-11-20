# An electric string near the monopole vacuum of pure SU(2)

**1994 working calculation.** Take four-dimensional pure $\mathcal N=2$ $SU(2)$ gauge theory with superpotential deformation $\mu\,\mathrm{Tr}\,\Phi^2$. In a monopole vacuum with $0<|\mu|\ll|\Lambda|$, a pair of heavy external fundamental electric sources requires a unit vortex of the dual photon. We obtain its positive leading tension from the same vacuum that determines its width. This fixes the string on which we can look for a polarized excitation.

## Fixing the vacuum and the flux

Write $u=\langle\mathrm{Tr}\,\Phi^2\rangle$ and choose the monopole point $u=\Lambda^2$. In the dual patch the light fields include the dual vector multiplet with scalar $a_D$ and a monopole hypermultiplet $(q,\tilde q)$ of dual charges $+1,-1$. The low-energy superpotential is
$$
 W=\sqrt2\,a_D q\tilde q+\mu u(a_D).
$$
The equations for a supersymmetric condensed vacuum give $a_D=0$, $q\tilde q=-\mu u'(0)/\sqrt2$ and $|q|=|\tilde q|$. Define $v^2=|q|^2+|\tilde q|^2=\sqrt2|\mu u'(0)|$. We use one of the two vacua and choose field phases on a CP-invariant slice. [Seiberg and Witten, §§5.6 and 6.2](https://arxiv.org/pdf/hep-th/9407087)

The period integral fixes the first two Taylor coefficients. Let $d=(u-\Lambda^2)/\Lambda^2$. Substitute $x=1+dt$ into the dimensionless dual period (6.23), choosing the cycle sign for which $a_D\sim i\Lambda d/2$. Then
$$
 a_D=\frac{i\Lambda d}{\pi}\int_0^1
   \sqrt{\frac{1-t}{t}}(1+dt/2)^{-1/2}\,dt
 =\frac{i\Lambda d}{2}\big[1-d/16+O(d^2)\big].
$$
The first two moments of the weight are $\pi/2$ and $\pi/8$. Inverting gives $u=\Lambda^2-2i\Lambda a_D-a_D^2/4+O(a_D^3/\Lambda)$. Thus $v^2=2\sqrt2|\mu\Lambda|$. If the quadratic superpotential is written $\mu_D a_D^2/2$, the mass parameter before canonical normalization is $\mu_D=\mu u''(0)=-\mu/2$. Below we use its magnitude after rephasing.

The fundamental electric weight is half a root. In semiclassical units its charge is $g_{\rm el}/2$, and the primitive smooth monopole has flux $4\pi/g_{\rm el}$. Their Dirac pairing is one. The pairing is integral and survives continuation to the dual patch. An external fundamental Wilson line is consequently a unit magnetic source for the dual connection $A$. Take $Dq=(\partial-iA)q$ and Maxwell term $-F^2/(4g^2)$ with $g$ the dual coupling. The condensate winds once and $\int F=2\pi$ on a transverse plane. This identifies the dual magnetic vortex as a tube of original electric flux. The microscopic adjoint fields have even electric weight and cannot screen an isolated fundamental probe. Only winding parity is an exact microscopic centre charge. No dynamical fundamental quarks are present. [Electric weight convention and monopole condensation](https://arxiv.org/pdf/hep-th/9407087)

## The controlled local action

Keep the two-derivative, constant-coupling Wilsonian dual QED with the monopoles explicit. In canonically chosen phases its bosonic scalar potential through the quadratic superpotential is
$$
 V=\frac{g^2}{2}(|q|^2-|\tilde q|^2)^2
   +g^2\left|\sqrt2(q\tilde q-v^2/2)+\mu_D a_D\right|^2
   +2|a_D|^2(|q|^2+|\tilde q|^2).
$$
The scalar kinetic terms have coefficients $1,1,1/g^2$ for $q,\tilde q,a_D$. Define the dual photon mass $m_\gamma=\sqrt2 g v$, the dimensionless deformation $w=g^2|\mu_D|/m_\gamma$ and the radial coordinate $\rho=m_\gamma r$. The two chiral masses in the bulk, each doubly degenerate in real components, are
$$
 \frac{m_\pm}{m_\gamma}=\sqrt{1+w^2/4}\ \pm w/2.
$$
For example, on the real D-flat slice the squared mass matrix in photon units has diagonal $(1,1+w^2)$ and off-diagonal $w$. The conjugate chiral pair gives the same eigenvalues. One other real scalar has mass $m_\gamma$ and the gauge phase is eaten. Thus the lowest one-particle bulk threshold drops *linearly* in $w$, even though the change in tension begins at second order. Taking $w$ small at fixed $m_\gamma$ is convenient in effective-theory units. Along the microscopic trajectory $m_\gamma/|\Lambda|$ and $w$ both vanish as $g\sqrt{|\mu/\Lambda|}$, and $g$ runs logarithmically. The Wilsonian coupling is evaluated at the light mass scale. Inserting the singular, monopole-integrated-out Coulomb-branch metric at $a_D=0$ would count the light monopole loop twice.

With $\mu_D$ real, the action is invariant under $(q,\tilde q,a_D)\mapsto(\tilde q^*,q^*,a_D^*)$ at fixed $A$. Its fixed fields allow the unit-string ansatz
$$
 q=H/\sqrt2,\qquad\tilde q=H^*/\sqrt2,\qquad
 H=v f(\rho)e^{i\theta},\quad A=a(\rho)\,d\theta,\quad a_D=gv s(\rho).
$$
The dimensionless tension is
$$
 \frac{\sigma}{2\pi v^2}=\tau=
 \int_0^\infty\rho\,d\rho\left[
 f'^2+\frac{(1-a)^2 f^2}{\rho^2}+\frac{a'^2}{\rho^2}
 +s'^2+f^2s^2+\frac{(f^2-1+2ws)^2}{4}\right].
$$
Regularity gives $f(0)=a(0)=s'(0)=0$ and $(f,a,s)\to(1,1,0)$ at infinity. At $w=0$, $s=0$ and the Bogomolny equations are $f'_0=(1-a_0)f_0/\rho$, $a'_0/\rho=(1-f_0^2)/2$. Their boundary term gives $\tau=1$. For a long fundamental string the static potential therefore has $V(R)/R\to\sigma$, with $\sigma_{\rm leading}=2\pi v^2=4\sqrt2\pi|\mu\Lambda|$ and $R\gg m_-^{-1},m_\gamma^{-1}$. Additive probe self-energies do not affect this limit. A charge under the *dual* potential is screened. The distinction between those two probes fixes the electric-confinement interpretation.

## First change in the tension

The equations and boundary conditions are invariant under $(w,s)\mapsto(-w,-s)$. On the branch continuous from the centered radial Bogomolny solution, $f,a$ change at order $w^2$ and $s=w s_1+O(w^3)$. The regular radial Hessian at $w=0$ has no translation or gauge zero mode in this gauge and sector. In particular, a zero of the linearized Bogomolny squares with $\delta f=f_0 h$ would satisfy $(-\Delta_\rho+f_0^2)h=0$, with regular axis and decaying exterior. Its integrated energy forces $h=0$. The neutral block is the same strictly positive scalar operator. Both radial blocks have massive exterior, giving the local continuation used in the expansion.

Write $L_f=-\partial_\rho^2-\rho^{-1}\partial_\rho+f^2$. The neutral equation is $(L_f+w^2)s=w(1-f^2)/2$. The gauge equation $a''-a'/\rho=-f^2(1-a)$ implies $L_f(1-a)=2a'/\rho$. At the critical point this solves the first-order neutral response exactly:
$$
 s_1=\frac{1-a_0}{2}.
$$
At a stationary unperturbed background, the first variations from $f-f_0$ and $a-a_0$ do not contribute to the coefficient of $w^2$ in the tension. Minimizing the remaining quadratic form in $s_1$ gives
$$
 \tau=1-w^2\int_0^\infty\rho\,d\rho\,s_1\frac{1-f_0^2}{2}
     +O(w^4)
 =1-\frac{w^2}{2}\int_0^\infty (1-a_0)a'_0\,d\rho+O(w^4)
 =1-\frac{w^2}{4}+O(w^4).
$$
Holding the neutral scalar fixed at zero misses this correction. Its sign also follows variationally by allowing the neutral field to relax on the Bogomolny core. The expansion concerns the local classical action above. Quantum and higher-derivative corrections to microscopic string observables have their own power counting.

There is also an on-shell response at finite $w$. At fixed $v,g$ stationarity permits differentiation in the explicit coefficient alone. Multiply the neutral equation by $s$, integrate by parts, and insert it in the derivative of the tension. For $w>0$ this gives
$$
 w\,\frac{d\tau}{dw}=-2\int_0^\infty\rho\,d\rho\,[(s')^2+f^2s^2]<0 .
$$
The strict inequality holds on a nontrivial relaxed branch since the source $w(1-f^2)/2$ is nonzero in the core. At $w=0.10$ the nonlinear solution gives $\tau=0.997508$ and $d\tau/dw=-0.0496894$. Along a microscopic trajectory the prefactor $2\pi v^2$ also varies. [Profiles and numerical check](results/spectrum.json)

## Retrospective source comparison

Vainshtein and Yung derive the dual mass splitting and the type-I behavior, and give the neutral-field equation in (67). Their arXiv v2 Eq. (3) has the period expansion used here. The coefficient of $a_D^2$ in $\mu u$ is $-\mu/4$; with the explicit factor $1/2$ in their Eq. (9), Eq. (10) as printed differs by a factor of two in $\mu_D$. Defining $w$ by the second derivative of the superpotential fixes the conversion. Hou also finds a downward tension correction. The coefficient above follows from the exact radial boundary term in our stated normalization. [Vainshtein and Yung, Eqs. (3)–(12), (59)–(67)](https://arxiv.org/pdf/hep-th/0012250v2) · [Hou, Eqs. (14)–(22)](https://arxiv.org/pdf/hep-th/0005119v2)
