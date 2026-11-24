# Pseudoscalar exchange on a four-dimensional flux tube

The 1988 scalar couples to the intrinsic curvature of the sheet and can
couple two phonons of the same polarization. In four spacetime dimensions a
second curvature measures how the two normals rotate around an infinitesimal
loop on the sheet. If a massive pseudoscalar couples to this curvature, its
pole selects one of the four right-left phonon states.
[QCDS-88/1, §7](../1988-thickness-curvature/paper.md#7-a-curvature-coupling-that-scatters-physical-phonons)

## From normal curvature to the vertex

Expand about a straight tube of tension $\sigma$ in flat spacetime. Write
$h_{ab}$ for the induced metric, $\eta_{ab}=\mathrm{diag}(-1,1)$ for its
straight-sheet value, $\varepsilon^{01}=1/\sqrt{-h}$ and $\epsilon_{12}=+1$.
For an oriented orthonormal pair of normals $n_i$, the connection is
$A_a=n_1\cdot\partial_a n_2$. Differentiating
$n_i\cdot\partial_b X=0$ gives
$(\partial_a n_i)\cdot\partial_b X=-K^i_{ab}$.
The normal components of $\partial_a n_1$ and $\partial_b n_2$ are
orthogonal, so differentiating $A$ gives the Ricci equation

$$
F_{ab}=\partial_a A_b-\partial_b A_a
      =\epsilon_{ij}K^i_{ac}h^{cd}K^j_{bd}.
$$

A local rotation of the normal frame shifts $A$ by a gradient and preserves
$F$. On a closed oriented Euclidean sheet, $\int F/(2\pi)$ is the normal
Euler number. A constant coefficient of $F$ therefore drops out of local
scattering. A field $a(\xi)$ gives a bulk interaction since
$aF=d(aA)-da\wedge A$ locally. In three spacetime dimensions there is only
one normal and this curvature vanishes.
[Mazur and Nair, *Strings in QCD and θ vacua* (1987)](https://doi.org/10.1016/0550-3213(87)90030-7)

Take a canonical real field of mass $m>0$ and define the dimensionless
coupling $Q$ by

$$
S_a=\int d^2\xi\,\sqrt{-h}\left[
-\tfrac12(\nabla a)^2-\tfrac12m^2a^2
+Q\,a\,\varepsilon^{ab}F_{ab}\right].
$$

Exchanging $i,j$ in $K^i_{ac}h^{cd}K^j_{bd}$ transposes $a,b$. Contracting
with $\varepsilon^{ab}$ thus selects the part antisymmetric in $i,j$.
Reflecting the string direction at fixed transverse axes reverses the sign
of $\varepsilon^{ab}F_{ab}$. Reflecting one transverse axis also reverses
its sign, by $\epsilon_{ij}$. Proper transverse rotations preserve it.
Assigning $a$ spin zero and these two odd parities makes the interaction
even under each reflection.

With canonical displacements $y^i=\sqrt{\sigma}\,X^i_\perp$, the linear
curvature is $K^i_{ab}=\partial_a\partial_b y^i/\sqrt{\sigma}$.
Substituting both curvatures and assigning the two incoming phonons to them
in both orders gives the Feynman vertex $iV_{ij}(p,q)$, with

$$
V_{ij}(p,q)=\frac{2Q}{\sigma}\,\epsilon_{ij}
                (p\cdot q)(p\wedge q),\qquad
p\wedge q=\varepsilon^{ab}p_a q_b .
$$

At fixed momenta, exchanging $i,j$ changes the sign. Exchanging the two
complete phonon legs changes both $\epsilon_{ij}$ and $p\wedge q$ in sign,
as Bose symmetry requires. The vertex vanishes for parallel polarizations
or for two phonons moving in the same direction.

## Polarization amplitudes

Order each state as $e_{ij}=\lvert i_R,j_L\rangle$. For incoming momenta
$p^a=(E_R,E_R)$, $q^a=(E_L,-E_L)$, we have $s=-(p+q)^2=4E_RE_L$,
$p\cdot q=-s/2$ and $p\wedge q=s/2$. Thus
$V_{ij}^{RL}=-Q s^2\epsilon_{ij}/(2\sigma)$. Use
$S=\mathbf 1+i\mathcal M/(2s)+\cdots$ and quote the tree pole coefficient
$R=\lim_{s\to m^2}(m^2-s)\mathcal M$. The Laurent residue in $s$ is $-R$.

The $t=0$ pairing joins phonons moving in the same direction. The $s$ and
$u=-s$ pairings each join a right mover to a left mover. Ordering each
vertex right mover first gives the pseudoscalar exchange amplitude

$$
\mathcal M_{ij\to kl}
=D_s\,\epsilon_{ij}\epsilon_{kl}+D_u\,\epsilon_{il}\epsilon_{kj},
\qquad
D_s=\frac{Q^2s^4}{4\sigma^2(m^2-s)},\quad
D_u=\frac{Q^2s^4}{4\sigma^2(m^2+s)} .
$$

On a polarization tensor $B$, the two index contractions give $B-B^T$ and
$B-\mathbf 1\,\mathrm{tr}\,B$, respectively. The following normalized
channels diagonalize both terms.

| Transverse channel | Normalized state | Tree exchange $\mathcal M$ | Pole coefficient $R$ |
|---|---|---|---|
| Trace scalar | $(e_{11}+e_{22})/\sqrt{2}$ | $-D_u$ | $0$ |
| Antisymmetric pseudoscalar | $(e_{12}-e_{21})/\sqrt{2}$ | $2D_s+D_u$ | $Q^2m^8/(2\sigma^2)$ |
| Symmetric traceless, spin two | $(e_{11}-e_{22})/\sqrt{2}$, $(e_{12}+e_{21})/\sqrt{2}$ | $+D_u$ for each | $0$ for each |

The pole factorizes as
$R_{ij\to kl}=Q^2m^8\epsilon_{ij}\epsilon_{kl}/(4\sigma^2)$.
Thus $R_{12\to12}=-R_{12\to21}=Q^2m^8/(4\sigma^2)$.
The transition $11\to22$ has zero pole residue and a finite crossed term
$-D_u$. For $11\to11$ the entire tree exchange vanishes.

For $s\ll m^2$ the exchange starts at order $s^4$. The four-phonon anomaly
term proposed in 1984 is polynomial in $s$ at order $s^3$ and contributes
zero residue at $m^2$. [QCDS-84/1, Eq. (11)](../1984-critical-dimension/paper.md#52-a-four-phonon-vertex-without-free-parameter)

The zero residue in each symmetric channel is a selection rule for this
pseudoscalar. Establishing such a mode on a gauge-theory tube requires
matching. Its pole position determines $m$ and its antisymmetric residue
determines $\lvert Q\rvert$ at tree level. Symmetry also permits $Q=0$.
For nonzero $Q$, decay to two phonons gives the resonance a width beyond
this tree approximation.

**Review provenance, 20 November 2026.** The joint AI review checked the three reduced channel amplitudes and the distinction between a finite crossed term and a direct-channel residue. This is the 1990 working note in the series. [Joint report](../1991-vortex-pseudoscalar/JOINT_REVIEW_2026-11-20.md) · [Response](../1991-vortex-pseudoscalar/RESPONSE.md#response-to-the-joint-review-of-20-november-2026)
