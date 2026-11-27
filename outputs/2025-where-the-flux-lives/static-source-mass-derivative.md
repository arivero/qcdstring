# A renormalized light–strange mass derivative of the static spectrum

November 2026 working note accompanying §10.4 of the December 2025 article. At a fixed physical separation $R>0$, choose a common mass-independent scheme at $\mu_0$. Hold the renormalized gauge reference, geometry and $\bar m=(2m_\ell+m_s)/3$ fixed, and vary
$$
 (m_u,m_d,m_s)=(m_\ell+\lambda,m_\ell+\lambda,m_s-2\lambda).
$$
Here $\lambda$ has mass dimension one. Use the same masses for sea and valence quarks, the same static representation and link action for the pair and both one-meson references, and $\hbar=c=1$. The target is $\partial_\lambda[E_0(R)-E_{+\ell}-E_{-\ell}]$ at zero source. The signs on the one-meson energies specify the static source and antisource. The article's odd scalar source multiplies this directional derivative by $c\bar m$.

## Insert the scalar before blocking the static lines

Let $i,j$ run over the straight string, isoscalar pair of static-light mesons, and pair of static-strange mesons. At fixed lattice spacing $a$, box and Euclidean time $T$ let $X_{ij}(T)$ be the full source-to-sink insertion after contracting the two static lines. Write $C_{ij}(T)=\langle X_{ij}(T)\rangle$ in the normalized gauge–light-fermion theory. A dot means a derivative along the tuned mass path at fixed physical coordinates. At finite regulator, wherever the path is differentiable and the partition function is nonzero,
$$
 \dot C_{ij}(T)=
 \langle\dot X_{ij}(T)\rangle-
 \big[\langle X_{ij}(T)\dot S_{\rm lat}\rangle
             -C_{ij}(T)\langle\dot S_{\rm lat}\rangle\big].
$$
This is the quotient rule for the finite integral. The mass insertion is the tuned action derivative, including any variation of the bare coupling, Wilson mass subtraction and improvement coefficients required by the fixed reference. In renormalized bulk units it represents the integrated $\bar uu+\bar dd-2\bar ss$ with its subtractions. The explicit derivative of $X_{ij}$ keeps any varying interpolator, line prescription and matching coefficients.

Equivalently, after integrating out the light fermions there is a sea covariance with $\sum_f\operatorname{Tr}(D_f^{-1}\dot D_f)-\dot S_g$ and the derivative of the contracted insertion. Each varying valence propagator contributes $-D_f^{-1}\dot D_fD_f^{-1}$. This expression applies where the inverses exist. The Grassmann quotient formula also covers determinant zeros in individual configurations. Both descriptions count the same contractions once. To block at finite cutoff, transport the whole numerator with **both** static lines and the mass insertion and transport the denominator through the same steps. Linearity of normalized integration then preserves each source coefficient. The release proves this finite-transfer identity on its own six-flavour regulator. Its continuum theorem is for calibrated local fields. The $2+1$-flavour extended-line estimates below require additional work. [Normalized transfer, November manuscript §97.4](https://github.com/yang-mills-group/OpenAI-informal-20261115/blob/6ca21d98b4022263fd7f2a3de5b5913b8495ee02/continuum-yang-mills-theory.pdf) · [Formal target and limit order](https://github.com/yang-mills-group/OpenAI-QCD-20261104/blob/53f81cafe5cb9cd18cd0d5b49b8364cce50a0fe7/proof/YM/Massive/Target/Statement.lean)

## An estimator with two matched one-meson subtractions

Take $T>T_0>0$. Remove linearly dependent source combinations and assume $C(T_0)>0$. For the simple largest generalized eigenvalue solve $C(T)v=\rho C(T_0)v$ with $v^\dagger C(T_0)v=1$. Differentiating and contracting with $v^\dagger$ cancels the eigenvector derivatives and gives
$$
 \partial_\lambda\log\rho
 =v^\dagger[\dot C(T)-\rho\,\dot C(T_0)]v/\rho .
$$
In a degenerate eigenspace the first variations are the eigenvalues of the corresponding derivative pencil on that space. Write $b_\pm(T)=C_{\pm\ell}(T)/C_{\pm\ell}(T_0)$ for the two isolated one-meson correlator ratios. The finite-time estimator is
$$
 -\frac{1}{T-T_0}\,\partial_\lambda\log
       \frac{\rho(T,T_0;R)}{b_+(T)b_-(T)} .
$$
A common invertible, time-independent endpoint renormalization sends both matrices to the same congruence and preserves their generalized eigenvalues, also when the basis depends differentiably on the mass. A multiplicative single-meson endpoint factor cancels within $b_\pm$. The static line identity terms multiply $\rho$ by $\exp[-(T-T_0)(\delta m_++\delta m_-)]$. The two $b$'s contain the identical factors, one apiece, so the static self-energy derivatives cancel exactly. Other endpoint contact contributions that change overlaps need a finite matched normalization or a sublinear large-$T$ derivative. Mixing of the scalar with any state-dependent line insertion allowed by the regulator requires a separately matched vertex. All coincident insertions retain the prescribed contact terms. [Euclidean Feynman–Hellmann derivation](https://arxiv.org/abs/1612.06963)

## Required continuum estimate

At fixed physical $R,T,T_0$ and box, a sufficient estimate is joint convergence of the matched matrices and their first $\lambda$ derivatives, locally uniformly in a neighbourhood of zero. Require this also for both one-meson correlators, with nonzero denominators, a nonsingular reference Gram matrix, and an isolated principal eigenvalue at the comparison point. Then the finite formula passes to the cutoff limit. Take the large-volume vacuum limit for the same observables at fixed times, keeping the separation from the temporal boundary large. Only then project by $T\to\infty$.

For example, write the resulting double ratio as
$$
 A(\lambda)\exp[-(T-T_0)\mathcal E(\lambda)](1+r_T(\lambda)),
 \qquad \mathcal E=E_0(R)-E_{+\ell}-E_{-\ell}.
$$
One sufficient large-time estimate on a fixed mass neighbourhood is $A>0$ with bounded logarithmic derivative, differentiable $\mathcal E$, and
$$
 |r_T|+\mu_0|\partial_\lambda r_T|
       \le C(1+\mu_0 T)e^{-\Delta(T-T_0)},\qquad \Delta>0 .
$$
The estimator then tends to $\mathcal E'(0)$. A continuum threshold can require a weaker, sublinear logarithmic-derivative bound in place of isolated-state exponential control. Ward-normalized scalar insertions reaching a line, and a mass neighbourhood with this control for the *resolved* static sector, are the missing estimates. Subtraction of the vacuum and the line identities alone leaves these estimates open. [Current and density normalization audit](https://github.com/yang-mills-group/QCD/blob/9b2971888b9d525431bdb398ae2cb3ac33bf28e5/docs/mass-current-normalization.md)

## A flavour-symmetric check

At $m_u=m_d=m_s$, take a flavour-singlet static pair with an isolated singlet level at the chosen $R$. A string interpolator and the flavour trace of the three two-meson interpolators can resolve this channel. With a flavour-covariant subtraction, the linear energy shift vanishes because a singlet diagonal expectation of the traceless scalar is zero. For each sign the one-meson flavour triplet has diagonal energy derivatives $(k_\pm,k_\pm,-2k_\pm)$. Indeed, permutation symmetry constrains the linear map from diagonal mass shifts to the three energies to act by a scalar on traceless shifts. Equivalently a singlet part is proportional to the mass trace and drops out. It follows that, at this symmetric point,
$$
 \partial_\lambda(E_{\bf1}(R)-E_{+\ell}-E_{-\ell})
  =\tfrac13\,\partial_\lambda
       (E_{+s}+E_{-s}-E_{+\ell}-E_{-\ell}).
$$
The identity also holds if a common mass-dependent energy per static line is added throughout. It applies to the ground-level target when that level is the isolated singlet. An exactly degenerate singlet and octet require diagonalizing the octet perturbation in the combined space. This fixes a threshold-subtracted slope relation without assigning a string fraction to the state.

The published ensemble mass coordinates in §10.4 range from $u=0.23849$ to $0.70132$. The symmetric-point check concerns the local derivative at $u=1$. The reported numbers at 1.33 fm are finite chords along a bare-trace trajectory at one lattice spacing. The local continuum derivative and this one-third test remain unmeasured by those data. [P31 and the original mass scan](paper.md#104-a-scalar-response-on-the-measured-levels-across-breaking) · [Three-ensemble study](https://arxiv.org/abs/2403.00754v2)
