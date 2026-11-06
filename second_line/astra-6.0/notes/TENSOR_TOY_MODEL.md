# A tensor field without a four-dimensional massless graviton

This is an explicitly assumed spectral problem. It is useful because it separates a higher-dimensional tensor equation from the spectrum seen in the four-dimensional coordinates. It is not a derived string vacuum.

Take

\[
ds^2=\frac{L^2}{z^2}(\eta_{\mu\nu}dx^\mu dx^\nu+dz^2),
\qquad 0<z\le z_0.
\]

The ultraviolet boundary is at \(z=0\). The wall at \(z=z_0\) is an imposed infrared boundary. In a transverse-traceless tensor sector with the usual decoupled equation, write the dimensionless metric perturbation as
\(h_{\mu\nu}(x,z)=\epsilon_{\mu\nu}\psi(z)e^{ip\cdot x}\), with \(p^2=-m^2\).

Its radial equation and inner product are

\[
\psi''-\frac3z\psi'+m^2\psi=0,\qquad
\langle\psi,\psi\rangle=L^3\int_0^{z_0}z^{-3}|\psi|^2\,dz.
\]

The overall positive factor \(L^3\) does not affect normalizability.

## The zero-mode test

At \(m=0\), solve directly:

\[
\psi(z)=a+bz^4.
\]

The constant solution has norm diverging as \(a^2/(2\epsilon^2)\) when the ultraviolet cutoff \(\epsilon\to0\). Under the standard fixed-source boundary interpretation it is excluded from the normalizable particle spectrum. A prescribed boundary metric is a source, not a state being integrated over.

The \(bz^4\) solution is normalizable at the ultraviolet boundary. Impose the infrared Neumann condition \(\psi'(z_0)=0\). It gives \(4bz_0^3=0\), hence \(b=0\). There is no nonzero normalizable massless tensor satisfying both conditions.

This conclusion uses the specified ultraviolet quantization and infrared boundary. Adding boundary gravitational dynamics or changing these conditions can change the result.

## The massive modes

For \(m>0\),

\[
\psi(z)=z^2[A J_2(mz)+B Y_2(mz)].
\]

The \(Y_2\) contribution tends to a nonnormalizable constant near \(z=0\), so set \(B=0\). The identity

\[
\frac{d}{dz}[z^2J_2(mz)]=mz^2J_1(mz)
\]

reduces the infrared condition to \(J_1(mz_0)=0\). With \(j_{1,n}\) denoting the positive zeros of \(J_1\),

\[
m_n=\frac{j_{1,n}}{z_0},\qquad
m_nz_0\simeq3.831706,\ 7.015587,\ 10.173468,\ldots .
\]

The normalized shape can be obtained from

\[
\int_0^{z_0} dz\,z\,J_2(m_nz)^2
=\frac{z_0^2}{2}J_2(j_{1,n})^2.
\]

The script independently evaluates the integral and compares it with this expression.

Writing the equation as

\[
-\frac{d}{dz}\left(z^{-3}\psi'\right)
=m^2 z^{-3}\psi
\]

gives, after the boundary terms vanish,

\[
m^2=
\frac{\int_0^{z_0}z^{-3}|\psi'|^2\,dz}
{\int_0^{z_0}z^{-3}|\psi|^2\,dz}\ge0.
\]

Since the zero solution was excluded, the nontrivial eigenvalues are positive. The numerical Rayleigh quotients provide a second check of the computed masses.

## A control that changes the answer

Replace Neumann by the Robin condition

\[
z_0\psi'(z_0)-4\psi(z_0)=0.
\]

Now \(\psi=z^4\) satisfies both boundaries and is a normalizable zero mode. The same differential equation can therefore give a different massless spectrum after a boundary change.

This is not permission to choose a boundary merely to obtain the preferred answer. It identifies what a microscopic construction must determine.

## What the example establishes

A bulk tensor need not produce a massless particle in the four-dimensional normalizable spectrum. Its role can be a tower of massive tensor states. This makes a gauge-theory interpretation compatible with gravitational variables in a dual description.

The example does not remove bulk gravity, establish a consistent string background, calculate the physical residues, or derive a flux-tube tension. It also does not prove that these states are QCD glueballs. Calling \(z_0\) a confinement scale would still require the Wilson-loop and microscopic checks.

The next substantive calculation is to derive the infrared end dynamically and evaluate the tensor spectrum and string tension in that same solution. See T05.
