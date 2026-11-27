# A massive fermion partner of the unit electric string

Contemporary calculation on the two-derivative Seiberg–Witten branch of QCDS-95/S1. Fix the minimal straight unit tube, constant dual gauge coupling and canonical fields in photon units. Take zero longitudinal momentum and the BPS limit before comparing small positive $w$. The scalar source is the physical radial shape excitation of §4. The proposed fermion source contains a neutral gaugino and a condensate-dressed hyperino on the same tube. The November Wilson-QCD construction provides graded fermionic correlators and an example of calibrating their insertions in one vacuum. Its baryon clause supplies neither this defect operator nor a supersymmetry generator. [Baryon and odd-field clauses](https://github.com/yang-mills-group/OpenAI-QCD-20261104/blob/53f81cafe5cb9cd18cd0d5b49b8364cce50a0fe7/proof/YM/Massive/Target/Physics.lean) · [Electric-string action and fermion conventions, §§4 and 11](paper.md)

## The preserved transformation and its pole

Write $h(\rho)$ for the real positive normalized radial eigenfunction of $-\Delta+f^2$ at $\nu^2$, $\nu=0.881744$ to the precision of the archived critical calculation. Use the undeformed profiles $f,a$ and $\phi=e^{i\theta}f/\sqrt2$. In the component bases of (28)–(31) set
$$
 V=(0,h),\qquad U=D^\dagger V/\nu=(b,e),\qquad
 b=-i e^{i\theta} h'/\nu,\quad e=e^{i\theta}fh/\nu .
$$
Then $DU=\nu V$ and both vectors have norm one, since $\int(|h'|^2+f^2h^2)=\nu^2\int h^2$ with plane area measure. The associated gauge-vector fluctuation is angular and the scalar fluctuation is aligned with $\phi$, so $U$ obeys background gauge and represents the physical shape. The mode is regular on the axis and decays at infinity below the bulk threshold. It is orthogonal to the translations in $\ker D$.

At linear order on this physical fluctuation $Y$, the preserved chiral variation has the two entries $(\partial_+Y,DY)$ up to normalization and spinor phase, $\partial_\pm=\partial_t\pm\partial_z$. The time and longitudinal parts are the electric field plus longitudinal field strength and the corresponding covariant time and longitudinal derivatives of the condensate. The transverse parts linearize the two BPS equations in (28). The background gauge term vanishes on $Y$. One can check the action of the linearized charge directly: map the fermion back to $Y$ by its $u$ component. On solutions of (31) this odd transformation squares to $\partial_+$ on $Y,u,v$, using $Du=\partial_+v$. The conjugate sector uses the opposite longitudinal sign. For $Y=Ue^{-i\nu t}$ the normalized fermion profile in (31) is $(-iU,V)/\sqrt2$ times the same time dependence. This construction uses the *physical* component fermion operator in (30). The established vortex fluctuation factorization supplies the radial eigenfunction. [BPS fluctuation operator](https://arxiv.org/abs/1509.06632) · [Component realization](paper.md#114-the-gapless-kernel-at-the-bps-point)

For the self-adjoint form $Q$ in §11.4 take the canonically smeared fermion in its $u$ slot along $U$. In $S_+$ this combines the neutral $\bar\chi_{+,1}$ with $\bar\phi\psi_{q,1}$ and the indicated radial weights. On the span of $(U,0),(0,V)$ the off-diagonal matrix elements of $Q$ are $\nu$. Its projected resolvent is $z/(z^2-\nu^2)$, while the shape Green function is $1/(z^2-\nu^2)$. The ratios of the positive-pole residues in the frequency variable are therefore fixed: $1/2$ for the fermion and $1/(2\nu)$ for the scalar. These are quadratic defect correlators in the specified source units.

## Linear soft splitting

Define complex coefficients $A_\pm,B_\pm$ by $u_\pm=U A_\pm$, $v_\pm=V B_\pm$ on the isolated massive subspace. At $w=0$, $\dot A=-\nu B$ and $\dot B=\nu A$. Vacuum-subtracted masses below refer to the classical transverse normal frequencies. Along the centered branch the first variations of $f,a$ vanish and $s=w s_1+O(w^3)$, $s_1=(1-a)/2$. In the basis $(q,\tilde q,\chi_+,\chi_-)$ the new mass entries are $M_{q\tilde q}=s$ and $M_{\chi_i\chi_j}=w/2$ for both signs $i,j$. With $\sigma_x$ exchanging sectors, projection of the linearized Weyl equations gives
$$
 \dot A=-\nu B+i w k\,\sigma_x A,\qquad
 \dot B=\nu A+i(w/2)\sigma_x B,\qquad
 k=\int (s_1|e|^2-|b|^2/2).
$$
For example $u_{+,1}=\bar\chi_{+,1}$ receives $-i(w/2)(\chi_{+,2}+\chi_{-,2})$. Its projection on $b$ gives $-i(w/2)\int|b|^2 A_-$, since $\int\bar b h=0$. The $q_1$ equation contributes $i\int s|e|^2 A_-$. For $v_{+,2}=-i\bar\chi_{+,2}$ the surviving term is $i(w/2)h B_-$, with the same expressions upon exchanging sectors. These formulas use the real-linear Weyl variables of (31), before the constant rephasing to the self-adjoint convention. Coupling to the complementary subspace affects eigenvalues at second order when the massive cluster is isolated.

The normalized radial dilation $h(\rho)\mapsto t h(t\rho)$ gives $\int |h'|^2=\tfrac12\int \rho(f^2)'h^2$. The BPS equation makes the right side $\int(1-a)f^2h^2$, hence $k=0$. In each $\sigma_x$ eigenspace the linear perturbation of the time generator has diagonal entries $0,\pm iw/2$. The positive-frequency and negative-frequency unperturbed eigenvectors have equal weights in $A,B$. The two positive masses and the comparison with the two even scalar poles are
$$
 \frac{m_{F,\pm}}{m_\gamma}=\nu\pm\frac w4+O(w^2),\qquad
 \frac{m_{T,\pm}}{m_\gamma}=\nu\pm\frac w2+O(w^2),\qquad
 \lim_{w\downarrow0}\frac{m_{F,+}-m_{F,-}}{m_{T,+}-m_{T,-}}=\tfrac12 .
$$
The ratio concerns the minimal constant-coupling action. At fixed $w>0$ the string breaks the surviving four supercharges. The four fermions generated by the broken transformations stay at zero, whereas these localized massive fermions can split. On a long winding string the massive fermion contributes an exponentially small spin-structure signal, in addition to the Goldstino $1/L$ term. The 1998 fivebrane continuation needs its own transverse normalization and a scale range where the other bulk modes decouple. [1986 spin-structure diagnostic](../1986-fermionic-flux-tube/paper.md) · [1998 supersymmetry and the colour string](../1998-colour-across-dualities/paper.md)

**Prospective test, 27 November 2026.** The two dimensionless linear slopes are $-1/4,+1/4$. Use a separately assembled fermion matrix from (30), varying all entries and retaining angular phases, and compare extrapolated slopes within 0.01 as the step and radial mesh decrease. The existing §11.5 operator-norm bound cannot resolve them. The next scheduled visit constructs the static-source operator dictionary in fundamental Wilson QCD. This pole test remains available for the following return.

## Component test of P33

The test was run after the registration had been pushed. Starting with the real and imaginary parts of the four complex amplitudes, lift each unit column to the original eight Weyl components. Form $i\,\overline{[M(w)-M(0)]}\,(i\sigma_2)\bar\psi$ using (30) at every angle and radial quadrature point, and add the covariant hopping change from $a_w-a_0$ with opposite charges on $q,\tilde q$. Solve the static equations for $f_w,a_w,s_w$ at each deformation. Project the component velocities back with the kinetic inner product. Add the critical rest generator and diagonalize the resulting real skew evolution. The mass calculation uses neither the virial substitution nor the reduced soft matrix of the prediction. The detected cluster is fixed by the critical eigenfunction.

| Outer radius | Radial spacing | Angular samples | First $w$ | Extrapolated low slope | Extrapolated high slope |
|---:|---:|---:|---:|---:|---:|
| 24 | 0.08 | 8 | 0.0100 | −0.25000893 | +0.25000890 |
| 28 | 0.04 | 12 | 0.0050 | −0.25000224 | +0.25000224 |
| 32 | 0.02 | 16 | 0.0025 | −0.25000056 | +0.25000056 |

For each mesh use $2s(w/2)-s(w)$ with $s(w)=[m_F(w)/m_\gamma-\nu_{\rm mesh}]/w$. Each reported slope occurs twice in the real-component calculation. Removing only the induced neutral core mass gives $-0.18258274,+0.18258274$ on the middle grid. This alteration fails the registered 0.01 tolerance. Retaining the complete mass profile passes it.

The finite-$w$ matrix here is a compression onto the isolated critical cluster. For a bounded perturbation $V_w=O(w)$ and a fixed positive separation from its complementary spectrum, Schur elimination adds two off-diagonal factors of $V_w$ and one bounded complementary resolvent. Its contribution to the finite-$w$ energies is $O(w^2)$ and disappears from the limiting first derivative. The test establishes the registered **linear slopes** in the stated two-derivative theory. Full finite-deformation line shapes, and a source matching those states to a scalar–fermion transition in fundamental Wilson QCD, remain open. [Registration](https://github.com/arivero/qcdstring/commit/f62c4544c2b89941c1a2da26468076a9b5e36622) · [Independent component assembly](code/partner_splitting.py) · [Wilson operator-check comparison](https://github.com/yang-mills-group/QCD/blob/9b2971888b9d525431bdb398ae2cb3ac33bf28e5/docs/assessment.md#independent-checks-of-the-finite-lattice-quark-operator)
