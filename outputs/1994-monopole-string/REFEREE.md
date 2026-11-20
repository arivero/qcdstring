# Independent check of the electric-string working calculation

**20 November 2026. GPT-6.2 Sol, second-line referee.** Read-only review of the two 1994 working notes, program and stored results, the preceding 1991 derivation, and the linked primary-source passages. The referee checked the equations by hand and inspected the code and printout as text. The author ran the numerical checks.

**Verdict.** Accept after targeted revisions to the microscopic scope, the light field content, and the source comparison. The unit Dirac pairing, period inversion, tension shift, vector residue and trace-doublet slope follow in the stated constant-coupling action. The scalar doublet has slopes $\pm1/2$ in photon mass units. The four broken real supercharges give localized fermion zero modes on the infinite straight string; widths into translations and the isolated two-state level splitting must retain their channel assumptions.

Two hand checks fix the leading coefficients. The Maxwell equation gives $s_1=(1-a_0)/2$, reducing the tension shift to $-w^2/4$ by a boundary integral. Dilation of the normalized vector wave converts the degenerate trace mixing element into $\nu_0$. The neutral imaginary field has the same critical radial wave as the longitudinal vector. Its direct two-phonon residue vanishes in the constant-coupling calculation. The analytic part of the matched gauge kinetic function can mix the two states. In the Pauli–Villars matching convention of Vainshtein and Yung the projected contribution has magnitude
$$
 \frac{|h|}{m_\gamma}=
 \frac{3g^2}{32\sqrt2\pi^2}\frac{m_\gamma}{|\Lambda|}J_B.
$$
Thus the leading microscopic claim concerns odd spectral weight below the first one-particle bulk threshold. Individual quantum masses, residues and line shapes need more matching.

**Response.** The vacuum note gives the signs, mass conventions and flux boundary data used in the comparisons with the two cited arXiv versions. The pole note includes the neutral imaginary block and its allowed gauge-kinetic mixing, the bulk fermion threshold, and the gapless string channels. It identifies $w=0.001$ as a hierarchical example and gives the explicit scale conversion for the larger local-QED examples. [Vacuum derivation](monopole-vacuum.md) · [Pole and mixing calculation](pseudoscalar.md)

**Numerical reproduction.** From a clean checkout of commit `99d4a3c`, Python 3.14.4, NumPy 2.3.5 and SciPy 1.16.3 reproduced all eight background rows, the three linear-response meshes, the even-channel eigenvalues and the outer-radius check byte for byte. The SHA-256 of the JSON output was `77546d2e2af2b201c54f8135fb67c601a11db8fbd30e6300586bf8f6978561f9`. The following command uses only tracked project code and the installed packages.

~~~sh
OPENBLAS_NUM_THREADS=1 python3 outputs/1994-monopole-string/code/soft_vortex.py
~~~

[Calculation](code/soft_vortex.py) · [Stored output](results/spectrum.json)
