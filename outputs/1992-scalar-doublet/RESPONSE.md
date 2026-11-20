# Author response for QCDS-92/1

The independent GPT-6.2 Sol referee confirmed the hand derivations of the slopes, half-residues, positive-detuning control and finite-volume factors and recommended acceptance with minor textual corrections. [Signed report](REFEREE.md)

We made all four corrections. Section 9 describes the induced source as exponentially localized. Section 11.4 calls the comparison at the same nonzero soft parameter the undetuned vortex. Section 11.3 identifies the discretization as radial and includes the centrifugal coefficients in that error. Section 8 specifies that the scalar matrix element extends through a dark eigenvalue.

We implemented the additional dilation test suggested in the report. For an eigenvector $Y$, differentiating a static scale variation gives $d_Y=\lambda_Y\langle(\rho f',a',\rho s'),Y\rangle$. Section 11.1 gives its derivation and measured convergence for both lines. Neither the spectral data nor the two primary residue formulas use this relation as input. The final PDF and the numerical rerun were checked by the author.
