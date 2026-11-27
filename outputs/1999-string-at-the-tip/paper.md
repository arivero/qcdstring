# What does the string at the tip carry?

**QCDS-99/S1 · October 1999 · Odd-year supplement to QCDS-98/1 of the counterfactual QCD string programme · Historical cutoff 31 October 1999**

## Abstract

The compactified D4 construction of 1998 holds the confining string at the tip of a cigar, where the circle with antiperiodic fermions shrinks. QCDS-98/1 noted that this tube need not carry the Goldstinos of a supersymmetric string and left its light spectrum open. Here we derive the quadratic spectrum of the string at the tip in the classical supergravity regime, fermions included, and follow what it implies for a long tube. The two cigar coordinates form a doublet of mass $M_{\rm KK}$ with one unit of Kaluza–Klein charge; the equality of this mass with $M_{\rm KK}$ holds for the whole family of D$p$ solitons. The eight fermions that survive $\kappa$-fixing obtain a common mass $M_{\rm KK}/2$ from the four-form flux and carry half a unit of charge. The masses obey $\sum_Bm^2=\sum_Fm^2$, which removes the logarithmic divergence of the one-loop vacuum energy of the transverse fields and places the cigar doublet exactly at the two-fermion threshold. The symmetries of the straight string forbid the direct two-fermion channel, because at fixed Kaluza–Klein charge the $\kappa$-projection ties the flat transverse spin to the chirality on the sphere. The four coordinates on the internal sphere are massless at tree level and form an $O(5)$ sigma model with $1/g^2=\lambda/6\pi$. Its dynamically generated gap is $C\times1.6048\,\mu(\lambda/9)^{1/3}e^{-\lambda/9}$, with $\mu$ near $M_{\rm KK}$, a threshold constant $C$ of order one that we do not compute, and the assumption that the matching introduces no $\log\lambda$. Where the geometry is trustworthy the tube therefore carries six light transverse bosons up to lengths of order $(\lambda/9)^{-1/3}e^{\lambda/9}/M_{\rm KK}$, and its Casimir coefficient there is six, three times the value for the two translations. The energy difference between periodic and antiperiodic fermions on a wound string is $(8M_{\rm KK}/\pi)\sum_{w\,{\rm odd}}K_1(wM_{\rm KK}L/2)/w$. At quadratic order on the common $\tau$-cigar branch this realizes the massive spin-structure diagnostic P21 of 1986 with four Dirac fermions of mass $M_{\rm KK}/2$. The antiperiodic sector is the dominant saddle only for $L>2\pi/M_{\rm KK}$. In the bulk, every normalizable charge-$n$ state of the transverse-traceless polarization lies above $|n|M_{\rm KK}$, and the lowest charge-one state is at $2.1775\,M_{\rm KK}$. The string clauses of P32, registered before the checks, are reached at quadratic order. Its bulk clause is narrowed to the computed tower, and the lightest charge-one scalar across the coupled bulk sectors remains to be computed. The route from this background to a pure four-dimensional polarized spectrum is narrowed: in its controlled regime the D4 tube has the wrong number of light fields.

## 1. The question left open in 1998

The preceding biennial article followed a color source through the 1995 duality web and the 1997 fivebrane construction. Its §8 compared a second construction available in the same year. Color D4-branes on a spatial circle with antiperiodic fermions have a strong-coupling description in which that circle closes smoothly at a tip. A long Wilson surface falls to the tip, where a fundamental string has finite redshifted tension, Eq. (22) of QCDS-98/1. The four supercharges that a supersymmetric color string breaks are absent from this vacuum from the start, so the tube need not carry Goldstinos. The article stopped there: "Neither classical limit supplies a derived polarized spectrum of ordinary, nonsupersymmetric pure Yang–Mills at the confinement scale." [1,2]

A long string is measured through its excitations. Its ground-state energy at length $L$ contains $\sigma L$, a constant, and a Casimir term $-\pi c/(6L)$ for a closed string wound once around a spatial circle, where $c$ counts the light transverse fields. Its first excited levels test the masses and charges of those fields. Both are fixed by the quadratic action of the string around its classical position. For the string at the tip that action has three parts. The two flat transverse directions give the translations. The two directions of the cigar, the radial coordinate and the shrinking circle, meet the warp factor at its minimum. The four directions of the internal four-sphere feel no potential, because the sphere has constant size and the string sits at an arbitrary point of it. The fermions see the four-form flux that threads the sphere.

The bosonic part was examined in January 1999. Expanding the Nambu–Goto action at the horizon, the calculation in [5] found that two transverse fields acquire a mass and six stay massless. In the four-dimensional case its mass parameter is $4\pi^2T^2$ in units where the shrinking circle has length $1/T$, which is $M_{\rm KK}^2$ in our units. That calculation left the fermions open. Treating them as in flat space, it concluded tentatively that the net Lüscher term would have the wrong sign. It stressed that the Ramond–Ramond background could change the answer. [5]

The question matters for the thesis of this programme, that the string of the dual resonance model is the chromoelectric flux tube. The effective-string results of 1976–1984 assume that a long tube carries only its two translations at low energy, which fixes the Casimir term and the leading corrections to the spectrum. The 1986 article studied fermions on the tube and their dependence on the spin structure of a circle. The 1988 article studied massive normal fields and how they mix with the translations. Each required a microscopic origin for the fields it postulated. The D4 construction supplies one in which every field of the tube is calculable, so it tests which of those postulates a confining string in a controlled background satisfies. [1]

This article computes the fermions and finishes the spectrum. Section 2 fixes the background and units. Sections 3 and 4 derive the bosonic and fermionic masses and charges. Section 5 records a sum rule and a threshold coincidence that follow from them. Section 6 treats the sphere coordinates as an asymptotically free sigma model, the point at which the tube departs most from a tube with only two translations. Section 7 computes the energy of a wound string in both spin structures. Section 8 asks whether the charged excitation of the string can decay into the bulk. Section 9 converts everything to string units, and §10 states what is reached and what remains.

What varies here is the 't Hooft coupling $\lambda$ at fixed $M_{\rm KK}$, the length $L$ of a wound string and the spin structure of the circle it winds. What stays fixed is the classical background, the position of the string at the tip and the one-loop treatment of its transverse fields. The observables are the masses and Kaluza–Klein charges of the transverse fields, the Casimir coefficient of the wound string and its difference between spin structures.

The results were registered as prediction P32 before any of the checks reported below was run. [Registration](https://github.com/arivero/qcdstring/commit/4557fb2) · [Calculation and printout](README.md)

## 2. Background, units and the range of control

In the string frame the compactified D4 background is
$$
 ds^2=\Big({U\over R}\Big)^{3/2}\big(\eta_{\mu\nu}dx^\mu dx^\nu+f(U)\,d\tau^2\big)
       +\Big({R\over U}\Big)^{3/2}\Big({dU^2\over f(U)}+U^2d\Omega_4^2\Big),
 \qquad f(U)=1-{U_0^3\over U^3},
 \tag{1}
$$
with dilaton $e^\phi=g_s(U/R)^{3/4}$, $N$ units of four-form flux on the sphere and $R^3=\pi g_sN\ell_s^3$. The four-dimensional coordinates are $x^\mu$, and $\tau$ is the circle on which the fermions are antiperiodic. Regularity at $U=U_0$ fixes the period of $\tau$ to $2\pi/M_{\rm KK}$ with
$$
 M_{\rm KK}={3\over2}{U_0^{1/2}\over R^{3/2}},\qquad
 \lambda=2\pi g_sN\ell_sM_{\rm KK},
 \tag{2}
$$
in the conventions of QCDS-98/1. The string tension at the tip, whose square root $\sqrt\sigma$ serves as the unit of energy in §§7–9, is
$$
 \sigma={1\over2\pi\ell_s^2}\Big({U_0\over R}\Big)^{3/2}
       ={2\lambda\over27\pi}\,M_{\rm KK}^2 .
 \tag{3}
$$
[2,1]

The eleven-dimensional form of the same background is useful for the fermions. Lifting on the M-theory circle $y$ gives the product of the seven-dimensional anti-de Sitter soliton with a round four-sphere,
$$
 ds_{11}^2=\Big({r\over R_A}\Big)^2\big(\eta_{\mu\nu}dx^\mu dx^\nu+dy^2+h(r)\,d\tau^2\big)
           +{R_A^2\,dr^2\over r^2h(r)}+R_S^2\,d\Omega_4^2,\qquad h(r)=1-{r_0^6\over r^6},
 \tag{4}
$$
with $R_A=2R_S$ and a four-form $F_4=f\,{\rm vol}(S^4)$ of constant frame value $f=3/R_S=6/R_A$. The two radial coordinates are related by $U\propto r^2$. In these variables $M_{\rm KK}=3r_0/R_A^2$. The relation $f=3/R_S=6/R_A$ is the Freund–Rubin condition. We check it below through the Killing-spinor equations, because the fermion mass depends on it. [2,8,6]

Near the tip let $\rho$ be the proper distance from $U=U_0$. Expanding (1),
$$
 U-U_0={3\over4}{U_0^{1/2}\over R^{3/2}}\,\rho^2+O(\rho^4),\qquad
 ds^2_{(\rho,\tau)}=d\rho^2+M_{\rm KK}^2\rho^2d\tau^2+O(\rho^4).
 \tag{5}
$$
The angle $\theta=M_{\rm KK}\tau$ has period $2\pi$, and the cigar near its tip is a flat plane in polar coordinates. A rotation of this plane by an angle $\alpha$ is the translation $\tau\to\tau+\alpha/M_{\rm KK}$. Its generator is the Kaluza–Klein momentum. A state of momentum $nM_{\rm KK}$ around $\tau$ has charge $n$ under the rotation.

The classical description requires small curvature in string units at the tip and small string coupling in the region used. The radius squared of the four-sphere at the tip is
$$
 R_{\rm tip}^2=R^{3/2}U_0^{1/2}={\lambda\over3}\,\ell_s^2 ,
 \tag{6}
$$
so weak curvature needs $\lambda\gg3$. The string coupling at the tip follows from the dilaton and (2),
$$
 e^{\phi(U_0)}={\lambda^{3/2}\over3\sqrt3\,\pi N},
$$
so string loops are suppressed when $N\gg\lambda^{3/2}$. At larger radius the dilaton grows, and the eleven-dimensional form (4) takes over; the string at the tip sits where the coupling is smallest. In this regime
$$
 {M_{\rm KK}\over\sqrt\sigma}=\sqrt{27\pi\over2\lambda},
 \tag{7}
$$
which equals one at $\lambda_*=27\pi/2\simeq42.41$ and falls below one at larger coupling. Where the geometry is reliable, the Kaluza–Klein scale lies at or below $\sqrt\sigma$. The 1998 article and the programme's tensor benchmark make the same point for the glueballs; the benchmark is a programme file of the second line, `numerics/d4_tensor.py`, written at machine date November 2026. Here we ask what it means for the string itself. [1]

## 3. The bosons of the string at the tip

Fix static gauge with worldsheet coordinates $(t,x^1)$ and let the string sit at $U=U_0$ at a point of the sphere. To quadratic order the Nambu–Goto action separates into three sets of transverse fields.

**Translations.** The two flat directions $x^2,x^3$ enter through the induced metric with the warp factor at the tip. With $Y_a=x^a$ the Lagrangian density is $-\tfrac12\sigma\,\partial Y_a\cdot\partial Y_a$, two massless fields as for any long string.

**The cigar doublet.** Let $X_c=(X^5,X^6)$ be Cartesian coordinates on the cigar plane in proper units, so that $|X_c|=\rho$. The string's energy per unit length at displacement $\rho$ is the local tension
$$
 \sigma(\rho)={1\over2\pi\ell_s^2}\Big({U(\rho)\over R}\Big)^{3/2}
            =\sigma+{1\over2\pi\ell_s^2}\,{1\over2}M_{\rm KK}^2\rho^2+O(\rho^4),
 \tag{8}
$$
where the second form uses (5). The kinetic term of $X_c$ has coefficient $1/2\pi\ell_s^2$ because the metric component along $\rho$ is one and the two-dimensional conformal factor cancels from $\sqrt{-h}\,h^{ab}$. The quadratic Lagrangian density is therefore
$$
 \mathcal L_c=-{1\over2\pi\ell_s^2}\Big[{1\over2}\partial X_c\cdot\partial X_c+{1\over2}M_{\rm KK}^2\,X_c\cdot X_c\Big],
 \tag{9}
$$
and the doublet has mass exactly $M_{\rm KK}$. In the eleven-dimensional form the membrane wraps $t$, $x^1$ and $y$, its energy density scales as $(r/R_A)^3$, and the same expansion gives the same mass. The program checks both forms symbolically.

The equality of the two masses is a property of the whole family of D$p$ solitons. For a soliton with $g_{tt}\propto U^{(7-p)/2}$ and $f=1-(U_0/U)^{7-p}$ the ratio of the doublet mass to the Kaluza–Klein mass at the tip is
$$
 {m_c^2\over M_{\rm KK}^2}={2\,\partial_U\log g_{tt}\over\partial_Uf}\bigg|_{U_0}
   ={2\cdot{7-p\over2U_0}\over{7-p\over U_0}}=1 ,
 \tag{10}
$$
for $p=2,\dots,6$. The same identity explains the value $4b^2$ found in [5] for the D3-based three-dimensional model. Its origin is that the warp factor along the string and the size of the shrinking circle derive from one harmonic function.

The doublet carries Kaluza–Klein charge. The combinations $X_c^\pm=X^5\pm iX^6$ rotate by $e^{\pm i\alpha}$ under the rotation of the cigar plane, which is the translation of $\tau$ by $\alpha/M_{\rm KK}$. One quantum of $X_c^\pm$ therefore carries momentum $\pm M_{\rm KK}$ around the shrinking circle, charge $\pm1$. The charge is conserved because $\tau$ is an isometry of (1).

**The sphere.** The string sits at an arbitrary point $n\in S^4$, $n\cdot n=1$. The background is invariant under $SO(5)$, so the position is a modulus of the classical solution, and the four tangent fluctuations are massless at tree level. Their Lagrangian density is
$$
 \mathcal L_S=-{1\over2g^2}\,\partial n\cdot\partial n,\qquad
 {1\over g^2}={R_{\rm tip}^2\over2\pi\ell_s^2}={\lambda\over6\pi}={9\over4}{\sigma\over M_{\rm KK}^2},
 \tag{11}
$$
again with the conformal factor cancelled. The coupling of the sphere fields is small where the geometry is reliable. The last form shows that $1/g^2$ is the ratio of the string scale to the Kaluza–Klein scale, and §6 shows that this ratio controls how long the sphere fields stay light.

The cigar doublet is a microscopic example of the massive normal field of P23, registered in 1988 for a displacement $y$ coupled to a normal field $\phi$ by the derivative mixing $-g_{\rm mix}\,\partial\phi\cdot\partial y$. For the straight string at the tip the background metric is block diagonal and the cigar fields do not mix with the translations at quadratic order, so $g_{\rm mix}=0$, the pole sits at $M=m/\sqrt{1-g_{\rm mix}^2}=M_{\rm KK}$, and its residue in the displacement correlator vanishes. Any mixing would enter at higher order in the fields, through curvature of the worldsheet.

In total the eight transverse bosons consist of two massless translations, a doublet of mass $M_{\rm KK}$ and charge $\pm1$, and four sphere fields massless at tree level. This agrees with the count of two massive and six massless fields in [5].

## 4. The fermions: masses from the four-form flux

The type IIA string at the tip lifts to a membrane wrapped on $y$ at $r=r_0$. The quadratic fermionic action of the supermembrane in a bosonic background is
$$
 S_F\propto\int d^3\xi\,\sqrt{-h}\;\bar\theta\,(1-\Gamma_{M2})\,\Gamma^\alpha D_\alpha\theta ,\qquad
 D_M=\nabla_M+K_M,\qquad
 K_M={1\over288}\big(\Gamma_M{}^{NPQR}-8\,\delta_M^N\,\Gamma^{PQR}\big)F_{NPQR},
 \tag{12}
$$
where $\theta$ is an eleven-dimensional Majorana spinor, $\Gamma^\alpha$ are the pulled-back gamma matrices, $\Gamma_{M2}$ is the worldvolume chirality and $D_M$ is the supercovariant derivative of eleven-dimensional supergravity. Here $\Gamma_M{}^{NPQR}$ is the antisymmetrized product of five gamma matrices with unit weight, nonzero only for five distinct indices. Sign conventions for $K_M$ differ between references, and we fix its normalization physically. With $F_4=f\,{\rm vol}(S^4)$ the contraction in (12) gives, up to the orientation of the flux,
$$
 K_\mu={f\over12}\,\Gamma_\mu\Gamma_{(4)},\qquad \Gamma_{(4)}=\Gamma^{\hat7\hat8\hat9\hat{10}},
 \tag{13}
$$
off the sphere, and $K_m=-(f/6)\Gamma_m\Gamma_{(4)}$ on it. The operator $D_M$ must annihilate the Killing spinors of the product of seven-dimensional anti-de Sitter space with the four-sphere. The flux is covariantly constant, so the integrability conditions $[D_M,D_N]\epsilon=0$ reduce to $\tfrac14R_{MNAB}\Gamma^{AB}+[K_M,K_N]=0$. Off the sphere $\Gamma_{(4)}$ commutes with $\Gamma_\mu$, and on it $\Gamma_{(4)}$ anticommutes with $\Gamma_m$, so
$$
 [K_\mu,K_\nu]=2\Big({f\over12}\Big)^2\Gamma_{\mu\nu}={\Gamma_{\mu\nu}\over2R_A^2},\qquad
 [K_m,K_n]=-2\Big({f\over6}\Big)^2\Gamma_{mn}=-{\Gamma_{mn}\over2R_S^2},
$$
which give $R_A=6/f$ and $R_S=3/f$. Appendix A verifies both statements with explicit $32\times32$ matrices. The normalization of the mass term below follows from the two radii alone. [6,7,8]

At the tip the spin connection along the worldvolume vanishes. Its components $\omega_\alpha{}^{\hat\alpha\hat\rho}$ are proportional to $\partial_\rho(r/R_A)$, and $r(\rho)$ is stationary at $\rho=0$. The worldvolume directions $t$, $x^1$, $y$ are all directions of the anti-de Sitter factor, so (13) applies to each, and
$$
 \Gamma^\alpha D_\alpha=\Gamma^\alpha\partial_\alpha+\sum_{\alpha=t,x,y}\Gamma^\alpha K_\alpha
   =\Gamma^\alpha\partial_\alpha+{f\over4}\,\Gamma_{(4)} .
 \tag{14}
$$
The matrix $\Gamma_{(4)}$ squares to one and commutes with $\Gamma^t$, $\Gamma^x$, $\Gamma^y$ and with $\Gamma_{M2}=\Gamma^{\hat t\hat x\hat y}$, since it shares no index with them. We fix $\kappa$-symmetry by $\Gamma_{M2}\theta=-\theta$. Off shell this leaves sixteen real components in the sector independent of $y$, which form eight two-component Majorana fields. On shell each field carries one polarization, eight in all. Multiplying (14) by its opposite-mass partner $\Gamma^\beta\partial_\beta-(f/4)\Gamma_{(4)}$ gives $\eta^{\alpha\beta}\partial_\alpha\partial_\beta-(f/4)^2$, because $\Gamma_{(4)}$ commutes with the worldvolume gamma matrices and squares to one. This is the Klein–Gordon operator with mass $f/4$ in proper units. Energies conjugate to the four-dimensional time are smaller by the warp factor $r_0/R_A$ at the tip, so
$$
 m_F={r_0\over R_A}\,{f\over4}={3\over2}{r_0\over R_A^2}={M_{\rm KK}\over2}.
 \tag{15}
$$
All eight fermions have this mass; the two eigenvalues $\pm f/4$ of the mass operator give masses of either sign, four fields of each. Table 7 counts the corresponding joint eigenspaces on the complexified sixteen-dimensional space.

The fermions carry half-integral charge. The rotation of the cigar plane acts on spinors by $\exp(\tfrac\alpha2\Gamma^{\hat5\hat6})$. The generator $\tfrac12\Gamma^{\hat5\hat6}$ commutes with $\Gamma_{(4)}$ and with $\Gamma_{M2}$. On the sixteen-dimensional $\kappa$-fixed space its eigenvalues are $\pm\tfrac i2$, four states of each charge for each sign of the mass:
$$
 q_F=\pm\tfrac12,\qquad m_F={M_{\rm KK}\over2}.
 \tag{16}
$$
The half-integral charge is the antiperiodicity of fermions around $\tau$ seen from the tip. A full rotation of the cigar plane is one circuit of the shrinking circle, and a spinor changes sign under it. The smooth geometry carries the spin structure that extends over the disc, which is the boundary condition that breaks supersymmetry in the five-dimensional theory.

The same mass can be read in ten dimensions. The reduction $ds_{11}^2=e^{-2\phi/3}ds_{10}^2+e^{4\phi/3}dy^2$ rescales orthonormal frames on the ten-dimensional directions by $e^{-\phi/3}$. The four-form with all legs on the sphere is the same form in both descriptions, so its frame values obey $f=e^{4\phi/3}F^{(10)}_{\hat7\hat8\hat9\hat{10}}$, and proper masses obey $m^{(10)}=e^{-\phi/3}m^{(11)}$. The string-frame mass operator is therefore
$$
 m^{(10)}={1\over4}\,e^{\phi}F^{(10)}_{\hat7\hat8\hat9\hat{10}}\,\Gamma_{(4)} ,
$$
the Ramond–Ramond term of the Green–Schwarz covariant derivative with coefficient $1/4$ after the sum over the two worldsheet directions. Energies conjugate to the four-dimensional time follow from the string-frame redshift $(U_0/R)^{3/4}$ at the tip. Since $r_0/R_A=e^{-\phi/3}(U_0/R)^{3/4}$ there, the product $(U_0/R)^{3/4}m^{(10)}$ equals (15). The dilaton gradient and the spin connection, which enter the ten-dimensional derivative separately, vanish at the tip because $U(\rho)$ is stationary there. The frame value of the flux is the same at every point of the sphere, and $SO(5)$ relates the points. All eight fermions therefore have one mass, wherever the string sits on the sphere.

These are the fermions that [5] left open. They are massive, and the gap comes from the Ramond–Ramond flux that [5] pointed to.

## 5. A sum rule and a threshold

The masses of the sixteen transverse fields satisfy
$$
 \sum_{\rm bosons}m^2-\sum_{\rm fermions}m^2=2M_{\rm KK}^2-8\Big({M_{\rm KK}\over2}\Big)^2=0 .
 \tag{17}
$$
The one-loop vacuum energy density of free fields in two dimensions has a logarithmic ultraviolet divergence proportional to $\sum_Bm^2-\sum_Fm^2$. Equation (17) states that the string tension receives no logarithmically divergent renormalization from its transverse fields at one loop. This is the behavior expected of a string in a background that solves the supergravity equations. The two mass terms come from different parts of the background, the warp factor for the bosons and the flux for the fermions. The sum rule therefore tests their relative normalization independently of any numerics.

With two massive bosons and eight fermions of a common mass, (17) fixes the ratio of the masses:
$$
 m_c=2m_F,\qquad q_c=q_F+q_F=1 .
 \tag{18}
$$
The cigar quantum sits exactly at the threshold for two fermions, and the Kaluza–Klein charges match. The other conserved quantum numbers of the straight string decide whether the two can mix. They are the rotation of the two flat transverse directions, $\mathrm{Spin}(2)_{\rm flat}$, generated by $\tfrac12\Gamma^{\hat3\hat4}$, and the rotations of the tangent space of the sphere at the string's point, $\mathrm{Spin}(4)=SU(2)\times SU(2)$, whose chirality is $\Gamma_{(4)}$. The cigar boson is a singlet of both. On the $\kappa$-fixed space $\Gamma^{\hat0\hat1\hat2}\theta=-\theta$, and the eleven-dimensional volume element $\Gamma^{\hat0}\cdots\Gamma^{\hat{10}}$ is proportional to the identity, so the product $\Gamma^{\hat3\hat4}\Gamma^{\hat5\hat6}\Gamma_{(4)}$ takes a fixed value there. At fixed cigar charge the flat spin $s_{\rm flat}$ therefore determines the sphere chirality:
$$
 q_F=+\tfrac12:\ (s_{\rm flat},\Gamma_{(4)})=(+\tfrac12,-1)\ \text{or}\ (-\tfrac12,+1);\qquad
 q_F=-\tfrac12:\ (+\tfrac12,+1)\ \text{or}\ (-\tfrac12,-1),
$$
four states of each kind on the complexified projected space. Two fermions with the charge of the cigar quantum both have $q_F=+\tfrac12$. A flat-spin singlet needs opposite flat spins, and then the two have opposite sphere chiralities. Their product transforms as $(2,1)\otimes(1,2)=(2,2)$ of $\mathrm{Spin}(4)$ and contains no singlet. With equal flat spins the pair carries flat spin $\pm1$. The program confirms that the space of couplings of a charge-one fermion pair invariant under $\mathrm{Spin}(2)_{\rm flat}\times\mathrm{Spin}(4)$ has dimension zero. These rotations leave the straight embedding fixed, and the embedding-dependent projector $\Gamma_{M2}$ transforms by conjugation under them, so the argument applies to the full pulled-back, $\kappa$-projected action, including the terms from the variation of the projector. No local coupling of one cigar field to two fermions without sphere fields is invariant, and the direct channel from the cigar quantum to two fermions is forbidden around the straight tip.

The representation $(2,2)$ is the tangent vector of the sphere, the representation of one sphere quantum. With one sphere quantum added, the program finds an eight-dimensional space of ordered internal tensors, the candidate couplings before fermionic exchange, worldsheet covariance and on-shell projection are imposed, so the three-body channel is allowed by the internal symmetries. At tree level its threshold lies at $2m_F$ plus the energy of the sphere quantum, which is at least $M_{\rm KK}$. With the tree-level fermion masses and the matched sphere gap of §6, the lightest three-body state with the quantum numbers of the cigar quantum is estimated to lie at $M_{\rm KK}+m_S$. The interacting threshold, the matrix element and the radiative shifts of $m_c-2m_F$ and of the sphere sector remain open, and they decide whether the charge-one cigar level is stable. On a wound string of finite length the comparison also depends on the spin structure. Antiperiodic fermions carry half-integral momenta, so the two-fermion threshold in the NS sector rises to $2(m_F^2+\pi^2/L^2)^{1/2}$, whereas periodic fermions have zero modes at $m_F$.

## 6. The four sphere coordinates as an $O(5)$ sigma model

Below the scale $M_{\rm KK}$ the cigar doublet and the fermions decouple. The transverse theory consists of the two free translations and the $O(5)$ sigma model (11), with its coupling matched at a scale $\mu$ of order $M_{\rm KK}$. The fermions transform under the $SO(4)$ that fixes the string's point on the sphere, through the chirality $\Gamma_{(4)}$, and they couple to the sphere fields above $\mu$. Maps from the plane to $S^4$ admit no topological term, because the second homotopy group and the second and third cohomology groups of $S^4$ vanish.

The $O(N)$ sigma model in two dimensions is asymptotically free [9]. With the normalization (11) and $t=g^2$, the two-loop beta function in the minimal subtraction scheme is $\mu\,dt/d\mu=-(N-2)t^2/2\pi-(N-2)t^3/4\pi^2+O(t^4)$. The corresponding scale parameter, in the same $\overline{\rm MS}$ convention as (20), is
$$
 \Lambda=\mu\Big({2\pi\over(N-2)g^2}\Big)^{1/(N-2)}e^{-2\pi/((N-2)g^2)}
        =\mu\Big({\lambda\over9}\Big)^{1/3}e^{-\lambda/9}\quad(N=5),
 \tag{19}
$$
where the second form inserts $1/g^2=\lambda/6\pi$. The exact mass gap of the model is known [10]:
$$
 m_S={(8/e)^{1/(N-2)}\over\Gamma(1+1/(N-2))}\,\Lambda_{\overline{\rm MS}}
    =1.6048\,\Lambda_{\overline{\rm MS}}\quad(N=5).
 \tag{20}
$$
Combining the two,
$$
 m_S=C\times1.6048\,\mu\Big({\lambda\over9}\Big)^{1/3}e^{-\lambda/9},
 \tag{21}
$$
where $C$ collects the one-loop threshold matching between the full transverse theory at $\mu$ and the sigma model. A one-loop shift $1/g^2(\mu)=\lambda/6\pi+\delta$ by a pure number $\delta$ gives $C=e^{-2\pi\delta/3}(1+O(g^2))$, a constant of order one that we have not computed. A different choice of $\mu$ within a factor of order one is absorbed in the same constant. We assume that $\delta$ contains no $\log\lambda$. The assumption would follow if the full transverse theory above $M_{\rm KK}$ did not run the sphere coupling, through a cancellation between the bosonic running and the fermions coupled through the flux, of the kind that conformal invariance of a string in a background solving the supergravity equations suggests. We have not shown that the cancellation extends to the finite threshold. A shift $(k/2\pi)\log\lambda$ would multiply (21) by $\lambda^{-k/3}$. The massive particles of the model form a five-plet of $SO(5)$. In two dimensions there is no spontaneous breaking of the continuous symmetry, so the tree-level moduli are lifted and no Goldstone bosons remain [11].

**Table 1.** Gap of the sphere fields in units of the matching scale, from (21) with $C=1$, as a matching example.

| $\lambda$ | $g^2=6\pi/\lambda$ | $m_S/\mu$ |
|---|---|---|
| 9 | 2.0944 | 0.5904 |
| 18 | 1.0472 | 0.2736 |
| 27 | 0.6981 | 0.1152 |
| 42.41 | 0.4444 | 0.02417 |
| 54 | 0.3491 | 0.007228 |
| 80 | 0.2356 | 0.0004585 |

The gap is exponentially small where the geometry is trustworthy. Between the scales $m_S$ and $M_{\rm KK}$ the sphere fields are weakly coupled and behave as four massless bosons, with corrections of order $g^2(1/L)$ at length $L$. The tube then carries six light transverse bosons, the two translations and the four sphere fields. Only at lengths beyond $1/m_S$ does it reduce to the two translations. The plateau of six requires $m_FL\gg1$, $m_SL\ll1$ and a small running coupling $g^2(1/L)$, and the closed-string expansion needs $L\sqrt\sigma\gg1$ as well. The upper end of the window is $1/m_S=(\lambda/9)^{-1/3}e^{\lambda/9}/(1.6048\,C\mu)$. With $\mu=M_{\rm KK}$ and $C=1$ it is $1/m_S=3.03/\sqrt\sigma$ at $\lambda=20$, $41.4/\sqrt\sigma$ at $\lambda_*$ and about $3000/\sqrt\sigma$ at $\lambda=80$.

The programme's 1986 and 1988 articles asked whether a flux tube carries fields beyond its translations, fermions in the first case and massive normal fields in the second. Here the extra fields have a definite origin. They are the position of the string on a compact space of constant size, whose isometry is a flavor symmetry of the dual five-dimensional theory. Their mass is generated dynamically on the worldsheet, by the mechanism that gaps the two-dimensional $O(N)$ models. Nothing in the background lifts them classically.

## 7. The wound string in two spin structures

Compactify a spatial direction of the four-dimensional theory on a circle of length $L$ and wind the string once around it. The fermions of the five-dimensional theory may be periodic (R) or antiperiodic (NS) around this circle. The fermions on the string inherit the choice, because they are spacetime spinors carried around the circle. The transverse fields of §§3–4 then contribute one-loop Casimir energies. For a real boson of mass $m$ on a circle of length $L$,
$$
 E_B(m,L)=-{m\over\pi}\sum_{w\ge1}{K_1(wmL)\over w},
 \tag{22}
$$
and for a two-dimensional Majorana fermion
$$
 E_F^{\rm R}(m,L)=+{m\over\pi}\sum_{w\ge1}{K_1(wmL)\over w},\qquad
 E_F^{\rm NS}(m,L)={m\over\pi}\sum_{w\ge1}(-1)^w{K_1(wmL)\over w}.
 \tag{23}
$$
Appendix B recalls the derivation. The massless limits are $-\pi/6L$, $+\pi/6L$ and $-\pi/12L$. In the window of §6, where the sphere fields are light, the ground-state energy of the wound string is
$$
 E_0^\alpha(L)-\sigma L=6\,E_B(0,L)+2\,E_B(M_{\rm KK},L)+8\,E_F^\alpha(M_{\rm KK}/2,L)+\cdots ,\qquad \alpha={\rm R},{\rm NS},
 \tag{24}
$$
up to a constant from the counterterms and terms of higher order in the interactions. Each energy is measured from the zero-flux vacuum of the same spin structure, subtracted separately in each sector as in QCDS-95/S1. Beyond $1/m_S$ the coefficient 6 becomes 2 and the sphere contributes exponentially small terms.

The difference between the spin structures comes from the fermions alone:
$$
 E_0^{\rm R}-E_0^{\rm NS}={8M_{\rm KK}\over\pi}\sum_{w\ {\rm odd}}{K_1(wM_{\rm KK}L/2)\over w}
   \;\longrightarrow\;
   \begin{cases}2\pi/L, & M_{\rm KK}L\ll1,\\[2pt] 8\sqrt{M_{\rm KK}/\pi L}\;e^{-M_{\rm KK}L/2}, & M_{\rm KK}L\gg1.\end{cases}
 \tag{25}
$$
The ratio of the sum to its asymptotic form is 1.0877, 1.0596 and 1.0364 at $M_{\rm KK}L=8$, 12 and 20.

The antiperiodic sector has a competing saddle. With antiperiodic fermions on both circles, the background (1) competes with the solution in which the circle of length $L$ shrinks and $\tau$ stays finite. The two are exchanged by interchanging the circles. The Euclidean action of the solution in which a circle of length $\beta$ shrinks is $-c\,N^3V\beta^{-5}$. Here $V$ is the volume of the remaining five directions of the fivebrane worldvolume, including the length of the other circle. This is the free energy of near-extremal fivebranes, whose entropy grows as $N^3T^5$ [12]. With $V_3$ the volume of Euclidean time and the two transverse directions, the action of (1) is $-cN^3V_3(2\pi R_{11})\,L\,\beta_\tau^{-5}$, and the exchanged solution has $-cN^3V_3(2\pi R_{11})\,\beta_\tau L^{-5}$. Comparing the two gives
$$
 \text{(1) dominates in the NS sector}\iff L>\beta_\tau={2\pi\over M_{\rm KK}} .
 \tag{26}
$$
Below that length the dominant solution lets the wound string slip off the tip of the other cigar, and the antiperiodic energy in (24) describes a subdominant saddle. Periodic fermions forbid the circle of length $L$ from shrinking smoothly, so the periodic sector has (1) at every length.

**Table 2.** Contributions to the ground-state energy of the wound string in units of $M_{\rm KK}$, at $M_{\rm KK}L=2\pi k$. The row $k=1$ lies at the tie of the two NS saddles, $L=2\pi/M_{\rm KK}$.

| $k$ | two translations | cigar doublet | fermions, R | fermions, NS | R − NS |
|---|---|---|---|---|---|
| 1 | -0.16667 | -0.00063 | 0.04382 | -0.04257 | 0.08639 |
| 1.5 | -0.11111 | -0.00002 | 0.00712 | -0.00708 | 0.01420 |
| 2 | -0.08333 | -0.00000 | 0.00126 | -0.00126 | 0.00251 |
| 3 | -0.05556 | -0.00000 | 0.00004 | -0.00004 | 0.00009 |

**Table 3.** The same in units of $\sqrt\sigma$ at $\lambda_*=27\pi/2$, where $M_{\rm KK}=\sqrt\sigma$. The antiperiodic sector is the dominant saddle only in the last two rows. In the first three the R − NS entry compares with the competing NS saddle and is formal.

| $L\sqrt\sigma$ | two translations | six light bosons | cigar doublet | fermions, R | R − NS |
|---|---|---|---|---|---|
| 3 | -0.3491 | -1.0472 | -0.0260 | 0.3823 | 0.7125 |
| 4 | -0.2618 | -0.7854 | -0.0080 | 0.1867 | 0.3573 |
| 6 | -0.1745 | -0.5236 | -0.0009 | 0.0520 | 0.1023 |
| 8 | -0.1309 | -0.3927 | -0.0001 | 0.0160 | 0.0318 |
| 10 | -0.1047 | -0.3142 | -0.0000 | 0.0052 | 0.0103 |

![Figure 1. (a) Infinite-length masses of the light fields of the string at the tip in units of $\sqrt\sigma$ as functions of $\lambda$. The sphere gap uses (21) with $\mu=M_{\rm KK}$ and $C=1$ as a matching example. The dotted line is the two-phonon reference level of a closed tube of length $3/\sqrt\sigma$. (b) Effective Casimir coefficient $c_{\rm eff}=-6L(E_0-\sigma L)/\pi$ of the wound string from the one-loop determinants of (24). $E_0$ is measured from the zero-flux vacuum of the same spin structure, and the four sphere coordinates are kept massless throughout. The periodic sector rises from the cancellation of bosons and fermions at short length to six. The antiperiodic sector falls from twelve to six and is the dominant saddle to the right of $M_{\rm KK}L=2\pi$. The line at two is the infrared reference for $L\gg1/m_S$; the crossover to it is a separate statement about the interacting sphere theory.](figures/tip-string.png)

**The massive diagnostic P21.** In 1986 the programme registered a conditional statement for a fixed-mass nonchiral Dirac field shared by periodic and antiperiodic closed-tube sectors. The vacuum-energy difference would be $(4m/\pi)\sum_{w\,{\rm odd}}K_1(wmL)/w$, and "a microscopic realization of both sectors is required". The eight Majorana fermions of (16) are four nonchiral Dirac fields of mass $M_{\rm KK}/2$. Equation (25) is four times the P21 formula at $m=M_{\rm KK}/2$, including the large-length form $\sqrt{8m/\pi L}\,e^{-mL}$ per Dirac field. The periodic sector exists at every length and the antiperiodic one as the dominant saddle for $L>2\pi/M_{\rm KK}$. The realization holds at quadratic order on the common $\tau$-cigar branch. QCDS-95/S1 realized the massless limit of P21 with four Goldstinos on the electric string of the weakly broken $N=2$ theory. The D4 tube realizes the massive case. [1]

**The three-length test.** The ledger defines a test that extracts the coefficient $a_\alpha$ of $1/L$ in each sector, cancelling the tension and a constant. For $b$ massless periodic bosons and $f$ massless nonchiral Majoranas, $a_{\rm R}=\pi(f-b)/6$ and $a_{\rm NS}=-\pi b/6-\pi f/12$. In the window the D4 tube has $f=0$, since all fermions are massive, and $b=6$, so $a_{\rm R}=a_{\rm NS}=-\pi$. Beyond $1/m_S$, $b=2$ and $a_{\rm R}=a_{\rm NS}=-\pi/3$. The estimator of the ledger is $\widehat a_\alpha(L)=(4L/3)[2E_\alpha(L)-3E_\alpha(2L)+E_\alpha(4L)]$, which cancels the tension and a constant exactly and returns $a_\alpha$ up to corrections from the massive fields. The program evaluates it from the determinants of (24):

**Table 6.** Three-length estimator from the one-loop determinants, with energies measured from the zero-flux vacuum of each spin structure. The sphere gap uses $\mu=M_{\rm KK}$, $C=1$.

| $\lambda$ | $L\sqrt\sigma$ | sphere sector | $\min M_{\rm KK}L$ | $\max m_SL$ | $\widehat a_{\rm R}/\pi$ | $\widehat a_{\rm NS}/\pi$ |
|---|---|---|---|---|---|---|
| 80 | 10, 20, 40 | four free bosons | 7.28 | 0.0134 | -0.8553 | -1.1447 |
| 80 | 20, 40, 80 | four free bosons | 14.56 | 0.0267 | -0.9947 | -1.0053 |
| 42.41 | 8, 16, 32 | four free bosons | 8.00 | 0.7734 | -0.8941 | -1.1059 |
| 20 | 30, 60, 120 | five-plet of mass $m_S$ | 43.69 | 39.66 | -0.3336 | -0.3336 |

All four triplets lie above the saddle crossing, so both sectors are dominant. At $\lambda=80$ the longer triplet sits on the plateau of six, and in the shorter one the fermions shift the two estimators by equal and opposite amounts: their mean stays at $-\pi$ and their difference is the exponential spin signal. At $\lambda_*$ the longest length reaches $m_SL=0.77$, where the free-sphere approximation is marginal. At $\lambda=20$ the sphere sector is gapped over the whole triplet; it is represented by the five-plet of the $O(5)$ model at leading exponential order, and both estimators return $-\pi/3$. The free-sphere rows neglect corrections of relative order $g^2(1/L)$. The electric string of QCDS-95/S1 reads $(b,f)=(2,2)$ and has a power-law spin difference $\pi/2L$. The D4 tube has no power-law spin difference, and its spin difference decays at the rate $M_{\rm KK}/2$. Finite-length spectroscopy in two spin structures thus distinguishes a vacuum without supersymmetry from a supersymmetric vacuum whose string breaks it. QCDS-98/1 §8 left this distinction to be measured.

## 8. Charged bulk states and the stability of the cigar quantum

The lowest charge-one cigar excitation of the string has energy $M_{\rm KK}$ above the ground state in the quadratic, zero-longitudinal-momentum result on the tip branch; single fermions carry half a unit of charge at $M_{\rm KK}/2$. At infinite length it sits at the bottom of the two-fermion continuum of §5, into which symmetry forbids it to decay directly; on a circle the two-fermion states form discrete R and NS levels. Kaluza–Klein charge is conserved. The excitation could still decay by emitting a charged closed-string state into the bulk if such a state existed below $M_{\rm KK}$. We test one bulk sector that can be solved exactly.

The transverse-traceless metric fluctuation with both indices along the flat directions, such as $h_{x^2x^3}$ independent of $x^2$ and $x^3$, obeys the minimally coupled massless scalar equation in the eleven-dimensional background (4). In four-dimensional terms it is a component of a spin-two glueball, and Constable and Myers argue that a scalar mode identified with the dilaton is degenerate with it [4]. The background has $\tau$ as an isometry, so the fluctuation can carry momentum $nM_{\rm KK}$ around $\tau$ without spoiling this property. Writing it as $\phi(r)e^{-iMt+inM_{\rm KK}\tau}$, the radial equation is
$$
 \big((r^7-r)\,\phi'\big)'+r^3\Big(M^2-{9n^2r^6\over r^6-1}\Big)\phi=0,
 \tag{27}
$$
in units $r_0=R_A=1$, where $M_{\rm KK}=3$. The regular solution behaves as $(r-1)^{|n|/2}$ at the tip and the normalizable one as $r^{-6}$ at large $r$. We solve (27) by shooting from both ends and matching at an intermediate radius.

**Table 4.** Lowest eigenvalues of (27) in units with $M_{\rm KK}^2=9$. The node count is that of the matched eigenfunction; the last column is the largest change of $M^2$ under three joint choices of the matching radius and of the inner and outer end points.

| charge $n$ | $M^2$ | $M/M_{\rm KK}$ | nodes | change of $M^2$ |
|---|---|---|---|---|
| 0 | 22.0966 | 1.5669 | 0 | $4\times10^{-6}$ |
| 0 | 55.5833 | 2.4851 | 1 | $2\times10^{-5}$ |
| 1 | 42.6733 | 2.1775 | 0 | $3\times10^{-9}$ |
| 1 | 83.1305 | 3.0392 | 1 | $3\times10^{-8}$ |
| 2 | 78.8994 | 2.9608 | 0 | $7\times10^{-11}$ |

Multiplying (27) by $\phi$ and integrating gives
$$
 (M^2-9n^2)\int_1^\infty r^3\phi^2\,dr=\int_1^\infty(r^7-r)\,\phi'^2\,dr+9n^2\int_1^\infty{r^3\phi^2\over r^6-1}\,dr ,
$$
with no boundary terms for the regular and normalizable solutions. Both terms on the right are nonnegative, and the derivative term is positive for any nonzero normalizable mode, so every such mode of (27) has $M>|n|M_{\rm KK}$; for $n=0$ the statement is $M>0$. The bound holds for every level of this operator, and the numerical levels respect it.

Two checks validate the method. The neutral level $1.5669\,M_{\rm KK}$ equals the programme's tensor benchmark of the second line, rechecked by `numerics/d4_tensor.py`. The substitution $x=r^2$ turns (27) at $n=0$ into the benchmark's equation $-[(x^4-x)H']'=\kappa xH$ with $\kappa={9\over4}(M/M_{\rm KK})^2$. The same shooting code applied to the equation printed as (3.3) in the 1998 glueball calculation [3], $(\lambda^7-\lambda)f''+(10\lambda^6-4)f'+\lambda^3k^2f=0$, gives $k^2=37.170$, 81.354 and 138.473. Their mass ratios 1.4794 and 1.9301 agree with the published ratios $2.38/1.61=1.4783$ and $3.11/1.61=1.9317$ to the two-decimal rounding of that table. The printed equation follows from the neutral case of (27) by multiplying both the radial kinetic coefficient and the weight by $r^3$ before expanding the derivative and dividing by $r^3$, which turns $7r^6-1$ into $10r^6-4$. With the coordinate $\rho\propto r^2$ of [3] the factor $r^3$ is $\rho^{3/2}$, proportional to $e^{2\phi}$: the printed equation uses the string-frame measure without the weight $e^{-2\phi}$. For the three-dimensional model Constable and Myers show that the dilaton and the transverse gravitons obey the same equation; for QCD$_4$ they find the two spectra degenerate at least in the WKB approximation. We use (27), which follows from the eleven-dimensional metric alone, and use the printed equation only to test the numerical method. [3,4]

In this sector the lowest charge-one state lies at $2.1775\,M_{\rm KK}$, which is $1.1775\,M_{\rm KK}$ above the cigar quantum, the bulk threshold separation. A charged excitation of the string at energy $M_{\rm KK}$ therefore cannot decay by emitting a charged glueball of this polarization, and kinematics forbids any channel that ends with the string in its ground state and a charged bulk state of this kind. Other bulk fields with charge, such as modes of the metric along $\tau$ or of the three-form, satisfy different radial equations, and we have not solved them. Within the computed sector, the tube's charged level is limited only by the threshold question of §5.

In four-dimensional terms the charge is the momentum around the compact fifth direction of the parent theory. The low-energy theory, pure Yang–Mills, has no such quantum number. A level of the tube that carries it is a direct signal of the fifth direction. At quadratic order and zero longitudinal momentum it lies at $M_{\rm KK}$ above the ground state on the tip branch, independent of $L$ at this order, whereas the levels of the translations approach the ground state as $4\pi/L$. A finite-length spectrum that resolves a length-independent level at $M_{\rm KK}$, at the edge of the two-fermion continuum, identifies the construction even where the Casimir term alone would leave room for doubt.

## 9. The tube in string units

**Table 5.** Infinite-length masses of the light fields of the tip string in units of $\sqrt\sigma$. The sphere gap uses $\mu=M_{\rm KK}$ and $C=1$ as a matching example.

| $\lambda$ | $M_{\rm KK}$ | $M_{\rm KK}/2$ | $m_S$ | $1/m_S$ in $1/\sqrt\sigma$ | tensor glueball | charged tensor glueball | $1/g^2$ |
|---|---|---|---|---|---|---|---|
| 20 | 1.4562 | 0.7281 | 0.3305 | 3.03 | 2.2818 | 3.1709 | 1.0610 |
| 42.41 | 1.0000 | 0.5000 | 0.0242 | 41.37 | 1.5669 | 2.1775 | 2.2500 |
| 80 | 0.7281 | 0.3641 | 0.000334 | 2995.66 | 1.1409 | 1.5855 | 4.2441 |

For orientation, the lowest free two-phonon reference level of a closed tube of length $L$ without longitudinal momentum consists of two phonons with opposite momenta and costs $4\pi/L$, which is $4.19\sqrt\sigma$ at $L\sqrt\sigma=3$. For every coupling in the table the infinite-length masses of the cigar doublet, of the two-fermion threshold and of the tensor glueball lie below this reference value. This compares masses with a reference level. The ordering of the actual levels at finite length requires the finite-length spectrum, which we do not compute. At infinite length the sphere sector has the gap $m_S$.

The ground-state energy of the long tube takes the form
$$
 E_0(L)=\sigma L-{\pi\,c_{\rm eff}(L)\over6L}+\cdots ,\qquad
 c_{\rm eff}\simeq\begin{cases}6, & 1/M_{\rm KK}\ll L\ll 1/m_S,\\ 2, & L\gg1/m_S,\end{cases}
 \tag{28}
$$
with energies measured from the zero-flux vacuum of each spin structure and the crossover at $L\sim1/m_S$ governed by the finite-volume behavior of the $O(5)$ model. The sign of the Casimir term is attractive in both regimes. The massive fermions decouple at long distance, and the light bosons determine the sign. The concern in [5] that the net term might be repulsive is thereby answered at quadratic order: the net term is attractive. Its magnitude in the window is three times the universal value derived in [13] for a long string whose only light fields are its translations.

The coupling relation (11), $1/g^2=(9/4)\sigma/M_{\rm KK}^2$, explains why the window is long where the calculation is reliable. The sphere fields are stiff when $\sigma$ exceeds $M_{\rm KK}^2$, and their gap carries the factor $e^{-(3/2)\pi\sigma/M_{\rm KK}^2}$, since $\lambda/9=(3/2)\pi\sigma/M_{\rm KK}^2$ by (7). The equality $M_{\rm KK}=\sqrt\sigma$ leaves the window open, as Table 5 shows at $\lambda_*$. The hierarchy between $m_S$ and $M_{\rm KK}$ is lost when $1/g^2$ falls to order one, near $\lambda\simeq9$, where $M_{\rm KK}\simeq2.2\sqrt\sigma$ and the classical geometry is no longer reliable, so the window cannot be followed further in this calculation. The extra fields are therefore features of the compactification in the regime where it is computed.

For an open string between static sources the same fields contribute, but the effective boundary conditions of the tip fields at the ends depend on the segments of the string that rise from the tip to the sources, which we have not matched. If all transverse bosons obey Dirichlet conditions there, each light boson contributes $-\pi/24R$ and the potential carries $-\pi c_{\rm eff}/24R$. If in addition the leading massive boundary effect is a round trip of each massive field between the ends, with a consistent reflection condition for the fermions and no lighter boundary exchange, the fermions and the cigar doublet contribute terms that decay as $e^{-M_{\rm KK}R}$ and $e^{-2M_{\rm KK}R}$ up to powers. We give both as conditional examples. The programme's own measurements bear on it only in part. The closed tube of the three-dimensional $Z_2$ theory carries $c=0.99(3)(9)$ massless modes, one per transverse direction, and its data exclude a second boson or a Majorana field [1]. The $SU(2)$ potentials of 1978 give a total $1/R$ coefficient between 0.24 and 0.33 at $R\sqrt\sigma\simeq0.4$–1.3, which includes one-gluon exchange. A fixed Casimir value $\pi/12$ was acceptable at $\beta=2.5$ only, and the Casimir share of the fitted term was left unresolved (QCDS-78/1 §6) [1]. The conditional open-string value for six light bosons, $\pi/4=0.785$, exceeds that total, but at separations below the window of (28). These are period comparisons for pure gauge theories with their own dimensions and fit assumptions, and the D4 construction approaches pure gauge theory only at small $\lambda$.

A tube with only two light transverse fields at the lengths of interest requires $M_{\rm KK}\gg\sqrt\sigma$ and $m_S\gg\sqrt\sigma$ together. By (7) and (21) both need $\lambda$ small, where the classical background fails. The registered glueball predictions of P08 point the same way, as separate extrapolations for the identified polarizations. If the scalar of the degenerate minimal tower is identified with the $0^{++}$ of P08, placing it at $3.5\sqrt\sigma$ needs $\lambda\simeq8.50$. Placing the tensor at $4.9\sqrt\sigma$ needs $\lambda\simeq4.34$, the value recorded in the programme's long march. Whether that scalar is the lightest scalar of the construction is not established here, and the pseudoscalar target is untested. At such couplings $g^2=6\pi/\lambda$ exceeds two and Table 1 gives $m_S$ of order $\mu$. The controlled hierarchy behind the window of six light bosons is lost there, at couplings where the derivation no longer holds. [1]

## 10. Disposition and the next calculations

**The string clauses of P32 are reached at quadratic order, and its bulk clause is narrowed.** Each string clause was derived analytically and checked numerically after the registration; the bulk clause was checked for one tower. The doublet mass $M_{\rm KK}$ and its charge $\pm1$ follow from (8)–(10), checked symbolically in both the ten- and eleven-dimensional forms. The fermion mass $M_{\rm KK}/2$ and charge $\pm\tfrac12$ follow from (12)–(16), checked with explicit Clifford matrices including both Killing-spinor normalizations, the $\kappa$-projector and the on-shell kernel. The sum rule is (17). The sphere coupling $1/g^2=\lambda/6\pi$ is (11), and the gap (21) is proportional to $M_{\rm KK}(\lambda/9)^{1/3}e^{-\lambda/9}$ under the matching assumption of §6, that the threshold shift contains no $\log\lambda$, with the constant $C$ of order one left uncomputed. The spin difference (25) holds at quadratic order on the common $\tau$-cigar branch. The registered bulk clause concerns the lightest bulk scalar of unit charge. Every normalizable charge-one state of the transverse-traceless tower lies above $M_{\rm KK}$, analytically, and its lowest level is at $2.1775\,M_{\rm KK}$. The coupled scalar sectors of the metric along $\tau$ and of the three-form remain to be solved. This clause is therefore narrowed to the computed tower, and the lightest charge-one scalar across the coupled sectors is the open computation.

**The route to a pure four-dimensional spectrum is narrowed.** In its controlled regime the D4 tube carries six light transverse bosons up to lengths of order $(\lambda/9)^{-1/3}e^{\lambda/9}/M_{\rm KK}$, a charged doublet at $M_{\rm KK}$ at the two-fermion threshold, and eight fermions at $M_{\rm KK}/2$, all with masses at or below $\sqrt\sigma$. It reproduces the Casimir term of a tube with two translations only beyond $1/m_S$. The 1998 target of a controlled pure four-dimensional polarized spectrum therefore remains open, and this background reaches it, if at all, only through an extrapolation to small $\lambda$ that the classical geometry cannot follow. The construction keeps a positive role: it is a controlled example of a confining string whose internal fields, their masses, charges and spin-structure dependence, are all calculable, and the finite-length tests of §7 discriminate it from the supersymmetric strings of QCDS-95/S1 and QCDS-98/1.

**The decisive next calculations** are the following.

1. *The charge-one level.* The radiative shifts of $m_c-2m_F$ and of the sphere sector, and the amplitude of the three-body channel with one sphere quantum that symmetry allows. They decide whether the charge-one cigar level is stable. They are the first place where the tube's charged spectrum depends on interactions.
2. *The threshold constant $C$.* The one-loop shift $\delta$ of the inverse sphere coupling at $\mu\sim M_{\rm KK}$, including a check that it contains no $\log\lambda$. It fixes the length at which $c_{\rm eff}$ falls from six to two. It requires the couplings of the sphere fields to the cigar doublet and to the fermions.
3. *Other charged bulk sectors.* The radial problems for the metric components along $\tau$ and for the three-form with momentum around $\tau$. They complete the stability statement of §8.
4. *A background that lifts the internal fields.* A confining geometry in which the internal space at the string's location has no isometry, or in which the string's position on it meets a classical potential. Such a background would give the sphere fields a mass without the exponential suppression of (21). The programme's next biennial slot can test the confining backgrounds that become available then against this requirement.

## Appendix A. The membrane mass operator with explicit matrices

The program `code/tip_spectrum.py` builds ten Hermitian $32\times32$ gamma matrices as tensor products of Pauli matrices, $\Gamma^{2k-1}=\sigma_3^{\otimes(k-1)}\otimes\sigma_1\otimes1^{\otimes(5-k)}$ and $\Gamma^{2k}=\sigma_3^{\otimes(k-1)}\otimes\sigma_2\otimes1^{\otimes(5-k)}$ for $k=1,\dots,5$, together with $\Gamma^0=\Gamma^1\cdots\Gamma^{10}$. This product is anti-Hermitian, anticommutes with the other ten and squares to $-1$; the code obtains it as $i$ times the product rescaled to square to one. Indices $0,1,2$ are the worldvolume directions $t$, $x^1$, $y$; indices 3 and 4 the flat transverse directions; 5 and 6 the cigar plane; 7 to 10 the tangent space of the sphere. The four-form has the single frame component $F_{\hat7\hat8\hat9\hat{10}}=f$. The checks, all passed at machine precision, are listed in Table 7.

**Table 7.** Explicit-matrix checks of the fermion mass operator, with $f=1$.

| Check | Result |
|---|---|
| Clifford algebra $\{\Gamma^A,\Gamma^B\}=2\eta^{AB}$ | satisfied |
| $K_\mu=(f/12)\Gamma_\mu\Gamma_{(4)}$ on a flat transverse direction | satisfied |
| $K_m=-(f/6)\Gamma_m\Gamma_{(4)}$ on a sphere direction | satisfied |
| $[K_{\hat7},K_{\hat8}]$ proportional to $\Gamma^{\hat7\hat8}$, coefficient | $-1/18$ |
| $\Gamma^\alpha K_\alpha$ summed over $t$, $x^1$, $y$ | $(f/4)\Gamma_{(4)}$, eigenvalues $\pm1/4$ |
| $\Gamma_{M2}^2$ and rank of $(1-\Gamma_{M2})/2$ | $1$ and $16$ |
| mass operator commutes with $\Gamma_{M2}$ | satisfied |
| kernel of the Dirac operator on shell, full and $\kappa$-fixed | 16 and 8 |
| smallest singular value 10 per cent off shell | 0.0447 |
| charges of $\tfrac12\Gamma^{\hat5\hat6}$ on the complexified $\kappa$-fixed space | $\pm\tfrac12$, four of each per sign of the mass |
| $2s_{\rm flat}\Gamma_{(4)}$ at cigar charge $+\tfrac12$ and $-\tfrac12$ | $-1$ and $+1$ |
| invariant charge-one couplings of two fermions | 0 |
| the same with one sphere quantum | 8 |

The coefficient $-1/18$ fixes $R_S=3/f$ through the integrability condition of $D_m\epsilon=0$ on a round sphere. The anti-de Sitter component fixes $R_A=6/f$ through the corresponding Killing equation. With both radii fixed, the mass in (14) is determined. The vector generators of $\mathrm{Spin}(4)$ used in the coupling count are computed from the adjoint action of $\tfrac12\Gamma^{ab}$ on the sphere gamma matrices, which fixes their sign relative to the spinor generators. The on-shell kernel has dimension 16 for the full operator. Restricted to the $\kappa$-fixed space it has dimension 8, the eight physical fermions with one on-shell degree of freedom each. The same program checks the bosonic statements of §§2–3 symbolically, including the proper-distance expansion (5), the tension (3), the sphere radius (6) and the identity (10) for $p=2,\dots,6$.

## Appendix B. Casimir sums

For a real scalar of mass $m$ on a circle of length $L$ the zero-point energy is $\tfrac12\sum_k\omega_k$ with $\omega_k=\sqrt{(2\pi k/L)^2+m^2}$. After subtraction of the term proportional to $L$, which renormalizes the tension, Poisson resummation gives (22). Explicitly,
$$
 {1\over2}\sum_{k\in\mathbb Z}\sqrt{\Big({2\pi k\over L}\Big)^2+m^2}
 ={L\over2}\int{dp\over2\pi}\sqrt{p^2+m^2}-{m\over\pi}\sum_{w\ge1}{K_1(wmL)\over w},
$$
where the integral is the divergent energy density of the infinite string and is absorbed into $\sigma$. The sum over $w$ is finite for every $m>0$. The term with winding $w$ is the contribution of a path that encircles the circle $w$ times, weighted by the propagator of a massive field over the distance $wL$. For a fermion the closed path picks up the sign of the spin structure at each circuit. Periodic fermions give the opposite sign of the boson at every $w$, and antiperiodic fermions an extra factor $(-1)^w$, as in (23). The massless limits follow from $K_1(z)\simeq1/z$ and $\sum_w1/w^2=\pi^2/6$, $\sum_w(-1)^w/w^2=-\pi^2/12$. The same sums appear in QCDS-86/1 §§5.1–5.4, where the massive Dirac difference first entered the programme. [1]

The program evaluates the sums directly to $wmL\simeq60$ and checks the massless limits. At $mL=10^{-3}$ it gives $-0.99905$, $+0.99905$ and $-0.9999976$ in units of $\pi/6L$, $\pi/6L$ and $\pi/12L$, respectively. The difference (25) times $L/2\pi$ is $0.99968$ at $M_{\rm KK}L=10^{-3}$. With the sphere fields counted as massless, the periodic total times $L$ vanishes as $L\to0$, the cancellation of eight bosons against eight periodic fermions at short distance.

## Appendix C. Memory and historical evidence

**Remembered and re-derived.** The compactified D4 background, its Kaluza–Klein mass and its tension were published in 1998, and QCDS-98/1 already used them. The two massive cigar fields were found in January 1999. Asymptotic freedom of the $O(N)$ models dates from 1975 and their exact gap from 1990. The entropy law of near-extremal fivebranes dates from 1996. The supermembrane action in a supergravity background dates from 1987, and its superspace form to second order in fermions from 1998. Equations (1)–(11), (19)–(20) and (26) reconstruct these inputs in the form used here. This article assigns itself no discovery of them.

**Remembered and used to choose the calculation.** The memory that the fermions on confining strings in these backgrounds turn out massive, and that the later lattice spectra of closed flux tubes follow the free Nambu–Goto string closely, led us to treat the fermion masses and the light window as the decisive questions. No later number enters as an input. The comparisons in Appendix D are made after the fact and use actual publication dates.

**Derived within this programme.** We know no published counterpart, as of the historical date, for the following statements. For these the derivation here is the only support, and the referee is asked to press hardest on them. They are the fermion mass $M_{\rm KK}/2$ and charge from the four-form flux in this background; the sum rule as a check, the threshold coincidence (18) it enforces and the selection rule that forbids the direct two-fermion channel; the identity (10) for the family of solitons; the application of the $O(5)$ gap to the string at the tip and the resulting window of six light bosons; the saddle condition (26) for the wound string; the realization of P21; and the bound $M>|n|M_{\rm KK}$ with the charged tensor levels of Table 4.

## Appendix D. Retrospective comparison with later publications

This appendix was written at publication, on 27 November 2026, with actual publication dates. The 1999 derivation uses only the sources listed under References available by October 1999.

- **November 1999, the D3-based model.** Kinar, Schreiber, Sonnenschein and Weiss computed fermionic fluctuations of confining strings. For the three-dimensional model built from D3-branes on a circle they found all eight fermions massive, with half the mass of the massive boson, and a net Lüscher term that is attractive. They treated one cigar mode as massless for an open Wilson loop whose flat segment sits slightly away from the tip, where the rotation of the cigar plane is spontaneously broken. For the wound closed string of §7 the string sits at the tip by symmetry, and both cigar fields have mass $M_{\rm KK}$. That result is the D3 analogue of §4. [L1]
- **March 2000.** Brower, Mathur and Tan tabulated the glueball spectrum of the M-theory form of the D4 background in units with $M_{\rm KK}^2=9$. Their tensor multiplet begins at $22.097$ and $55.584$, the two neutral levels of Table 4. The tabulated spectrum also contains a lighter neutral scalar from the metric along $\tau$ at $7.308$, that is $0.901\,M_{\rm KK}$; its charged partners belong to the open sector of §10. [L2]
- **September 2004, the D4 model.** Bigazzi, Cotrone, Martucci and Pando Zayas computed the one-loop correction to the Wilson loop in the D4 model. In their units $M_{\rm KK}={3\over2}m_0$ they found six massless bosons, two bosons with $m^2={9\over4}m_0^2=M_{\rm KK}^2$ and eight fermions with $m^2={9\over16}m_0^2=M_{\rm KK}^2/4$. They used the vanishing of $\sum_B\omega^2-\sum_F\omega^2$ as a check, as in (17), and found a finite one-loop shift of the tension. In the passages read they keep the six massless fields free in the one-loop energy, and the sphere gap of §6 does not appear. [L3]
- **July 2010.** Athenodorou, Bringoltz and Teper measured about twenty states of closed flux tubes in $SU(N)$ gauge theories in 3+1 dimensions, up to lengths near $6/\sqrt\sigma$. They found most low-lying states well described by the free Nambu–Goto string, whose ground state carries the Casimir term of two transverse fields. The tube of §9 shows $c_{\rm eff}=6$ only where $m_FL\gg1$, $m_SL\ll1$, $g^2(1/L)$ is small and $L\sqrt\sigma\gg1$. At the lattice lengths, up to $6/\sqrt\sigma$, these conditions hold at best marginally near $\lambda_*$, where $m_FL\le3$, and the comparison is qualitative. The comparison is consistent with the conclusion of §10 that the controlled D4 tube differs from the pure-gauge tube. [L4]
- Aharony and Karzbrun discussed the effective action of confining strings, with holographic backgrounds as examples (abstract read only). [L5]

The bosonic masses, the fermion masses and the sum rule of §§3–5 agree with the later record: the mass relation for the D3-based model appeared in November 1999 and the full D4 spectrum in 2004. Within this counterfactual chronology the D4 fermion spectrum appears a few weeks before the first related publication. In the actual record no priority belongs to this programme. We have not found the sphere gap or the selection rule of §5 applied to this string in the passages read, and literature priority for them is unestablished.

## References available by October 1999

1. QCD string programme: *Where does the color go when a string is lifted?* (QCDS-98/1), §8 and Eq. (22); *What the vortex doublet predicts on a Seiberg–Witten electric string* (QCDS-95/S1), §11; the 1986 article (QCDS-86/1), §§5.1–5.4; the 1988 article (QCDS-88/1) on massive normal fields; the 1984 refits (QCDS-84/1), Eq. (13), $c=0.99(3)(9)$ for the three-dimensional $Z_2$ tube; and the 1978 $SU(2)$ fits (QCDS-78/1), §6. Predictions P08, P21, P23 and P32 are in the ledger. The caveat on the IIA chart and the coupling needed for the tensor glueball are in the long march. The tensor benchmark is in the second line's T05 and in `numerics/d4_tensor.py`. [1998 paper](../1998-colour-across-dualities/paper.md) · [1995 corollary](../1995-electric-string-corollary/paper.md) · [1988 paper](../1988-thickness-curvature/paper.md) · [1986 paper](../1986-fermionic-flux-tube/paper.md) · [1984 paper](../1984-critical-dimension/paper.md) · [1978 paper](../1978-su2-scaling/paper.md) · [Ledger](../../PREDICTIONS.md) · [Long march](../../LONG_MARCH.md) · [Tensor benchmark](../../numerics/d4_tensor.py)
2. E. Witten, *Anti-de Sitter space, thermal phase transition, and confinement in gauge theories* (1998), §4. The compactified D4 and M5 constructions. [Paper](https://arxiv.org/abs/hep-th/9803131)
3. C. Csáki, H. Ooguri, Y. Oz and J. Terning, *Glueball mass spectrum from supergravity* (1998 preprint, 1999 publication), §3, Eqs. (3.1)–(3.5) and Table 5. [Paper](https://arxiv.org/abs/hep-th/9806021)
4. N. R. Constable and R. C. Myers, *Spin-two glueballs, positive energy theorems and the AdS/CFT correspondence* (August 1999 preprint). The minimally coupled equation for the transverse-traceless metric fluctuation and its degeneracy with the dilaton. [Paper](https://arxiv.org/abs/hep-th/9908175)
5. J. Greensite and P. Olesen, *Worldsheet fluctuations and the heavy quark potential in the AdS/CFT approach* (January 1999 preprint), §§4–5 and 7; and *Remarks on the heavy quark potential in the supergravity approach* (1998). [1999 paper](https://arxiv.org/abs/hep-th/9901057) · [1998 paper](https://arxiv.org/abs/hep-th/9806235)
6. E. Bergshoeff, E. Sezgin and P. K. Townsend, *Supermembranes and eleven-dimensional supergravity*, Phys. Lett. B 189 (1987) 75. The membrane action in a supergravity background.
7. B. de Wit, K. Peeters and J. Plefka, *Superspace geometry for supermembrane backgrounds*, Nucl. Phys. B 532 (1998) 99. The supermembrane action to second order in the fermionic coordinates in an unrestricted background. [Paper](https://arxiv.org/abs/hep-th/9803209)
8. P. G. O. Freund and M. A. Rubin, *Dynamics of dimensional reduction*, Phys. Lett. B 97 (1980) 233. The product of anti-de Sitter space with a sphere threaded by four-form flux.
9. A. M. Polyakov, *Interaction of Goldstone particles in two dimensions. Applications to ferromagnets and massive Yang–Mills fields*, Phys. Lett. B 59 (1975) 79. Asymptotic freedom of the two-dimensional $O(N)$ models.
10. P. Hasenfratz and F. Niedermayer, *The exact mass gap of the O(N) sigma model for arbitrary* $N\ge3$ *in* $d=2$, Phys. Lett. B 245 (1990) 529; P. Hasenfratz, M. Maggiore and F. Niedermayer, Phys. Lett. B 245 (1990) 522. [DOI](https://doi.org/10.1016/0370-2693(90)90686-Z)
11. S. Coleman, *There are no Goldstone bosons in two dimensions*, Commun. Math. Phys. 31 (1973) 259; N. D. Mermin and H. Wagner, Phys. Rev. Lett. 17 (1966) 1133. [Coleman](https://doi.org/10.1007/BF01646487) · [Mermin–Wagner](https://doi.org/10.1103/PhysRevLett.17.1133)
12. I. R. Klebanov and A. A. Tseytlin, *Entropy of near-extremal black p-branes* (1996), Eq. (3.16) for fivebranes. [Paper](https://arxiv.org/abs/hep-th/9604089)
13. M. Lüscher, *Symmetry breaking aspects of the roughening transition in gauge theories*, Nucl. Phys. B 180 (1981) 317. The universal Casimir term of a long string.
14. G. T. Horowitz and R. C. Myers, *The AdS/CFT correspondence and a new positive energy conjecture for general relativity* (1998). The anti-de Sitter soliton as the candidate minimum-energy solution with supersymmetry-breaking boundary conditions. [Paper](https://arxiv.org/abs/hep-th/9808079)

## Later publications cited in Appendix D

- [L1] Y. Kinar, E. Schreiber, J. Sonnenschein and N. Weiss, *Quantum fluctuations of Wilson loops from string models* (November 1999 preprint), §§12–13. [Paper](https://arxiv.org/abs/hep-th/9911123)
- [L2] R. C. Brower, S. D. Mathur and C.-I Tan, *Glueball spectrum for QCD from AdS supergravity duality* (2000), Tables 1–2. [Paper](https://arxiv.org/abs/hep-th/0003115)
- [L3] F. Bigazzi, A. L. Cotrone, L. Martucci and L. A. Pando Zayas, *Wilson loop, Regge trajectory and hadron masses in a Yang–Mills theory from semiclassical strings* (2004), §3. [Paper](https://arxiv.org/abs/hep-th/0409205)
- [L4] A. Athenodorou, B. Bringoltz and M. Teper, *Closed flux tubes and their string description in D=3+1 SU(N) gauge theories* (2010), abstract. [Paper](https://arxiv.org/abs/1007.4720)
- [L5] O. Aharony and E. Karzbrun, *On the effective action of confining strings* (2009), abstract. [Paper](https://arxiv.org/abs/0903.1927)
