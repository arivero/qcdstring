# Working calculations

These derivations fix conventions and make the proposed tests concrete. They are standard benchmarks or elementary deductions, not claims of a new string theory. Source keys resolve in REFERENCES.md.

## Soft tensor coupling

Let all external \(p_i\) be future-directed momenta, with \(\eta_i=+1\) for outgoing and \(-1\) for incoming states. Under the standard soft-factorization assumptions,

\[
\mathcal M_{n+1}(q,\epsilon)\simeq
\left[\sum_i \eta_i g_i
\frac{p_i^\mu p_i^\nu\epsilon_{\mu\nu}}{p_i\cdot q}\right]
\mathcal M_n.
\]

With \(\delta\epsilon_{\mu\nu}=q_\mu\xi_\nu+q_\nu\xi_\mu\), the variation is proportional to
\(2\xi_\nu\sum_i\eta_i g_i p_i^\nu\). Requiring decoupling of the spurious polarization gives the identity used in T01. For generic connected scattering processes, a common \(g_i\) reduces it to momentum conservation [H3].

This establishes the leading universal coupling within the assumptions. It does not, by itself, prove a complete nonlinear gravitational theory, nor force a massless tensor into every string construction. The standard closed-string zero-slope gravitational limits provide separate historical results [H4, H5].

## Large-N topology

Use a matrix normalization with an overall \(N\) in the action at fixed 't Hooft coupling. A ribbon diagram contributes a power \(N^{F-E+V}\). For a connected orientable surface with \(b\) fundamental boundaries,

\[
F-E+V=\chi=2-2h-b.
\]

Hence a handle suppresses a vacuum contribution by \(N^{-2}\), and a fixed-flavor quark boundary by \(N^{-1}\). This is compatible with a closed-string coupling proportional to \(1/N\), but does not determine a worldsheet action [H1].

## The long open-string energy

A massless transverse displacement with fixed endpoints has frequencies \(\omega_n=\pi n/R\). The finite, subtracted Casimir term is

\[
\frac12\sum_{n=1}^\infty\omega_n
\ \longrightarrow\ -\frac{\pi}{24R}.
\]

The arrow denotes the finite part after regularizing and subtracting local ultraviolet terms; it does not identify the divergent sum with an ordinary convergent series. With \(D-2\) such fields this gives \(-\pi(D-2)/(24R)\).

Expanding the Nambu–Goto benchmark yields

\[
E_0(R)=\sigma R-\frac{\pi(D-2)}{24R}
-\frac{\pi^2(D-2)^2}{1152\sigma R^3}+\cdots.
\]

In \(D=4\), the first two corrections are
\(-\pi/(12R)\) and \(-\pi^2/(288\sigma R^3)\).
Boundary and higher-derivative operators must be audited before treating further terms as universal. This is a long-string expansion [M1, M2].

## Gravitational decoupling and retained string scales

Suppress numerical convention-dependent factors in the ten-dimensional relation

\[
G_{10}\propto g_s^2\alpha'^4.
\]

For the NS5 little-string limit, fixed \(\alpha'\) and \(g_s\to0\) suppress bulk gravity in string units. The nontrivial retained sector is part of the imported brane construction, not a consequence of this single equation [M3, M4].

For the NCOS convention in T08,

\[
g_s=G_o^2\delta^{-1/2},\qquad
\alpha'=\delta\alpha'_{\rm eff}
\quad\Rightarrow\quad
\frac{G_{10}}{(\alpha'_{\rm eff})^4}\propto G_o^4\delta^3.
\]

The growing bulk \(g_s\) is not itself a failure of the open-sector limit. Its finite effective coupling and the fate of closed exchange must be assessed using the complete amplitude and metric scaling [M5, M6].

For comparison, the ordinary empty-background limit \(g_s\to0\) at fixed \(\alpha'\) also sends the conventional open-string disk four-point coupling \(g_o^2\propto g_s\) to zero. It fails our retained-interaction criterion.

## Central charge and physical dimensions

For a conventional bosonic critical worldsheet, the ghost central charge is \(-26\). Four free embedding scalars contribute 4, leaving 22 to be supplied by other matter sectors.

For a conventional RNS critical worldsheet, the ghost system contributes \(-15\). Four free boson–fermion pairs contribute 6, leaving 9.

Neither balance determines the physical interpretation of the remaining sector. It might admit a geometric presentation, but consistency requires its full operator spectrum and interactions, not just its central charge.

For a curved sigma model, a conventional leading-order metric beta function is

\[
\beta^G_{\mu\nu}
=\alpha'\left(R_{\mu\nu}
+2\nabla_\mu\nabla_\nu\Phi
-\frac14H_{\mu\rho\sigma}H_\nu{}^{\rho\sigma}\right)
+O(\alpha'^2).
\]

Its vanishing is a worldsheet consistency requirement in that construction [M10]. Whether the corresponding metric fluctuations constitute physical gravity in the spacetime of interest additionally depends on the spectrum, boundary conditions, couplings and physical dictionary.
