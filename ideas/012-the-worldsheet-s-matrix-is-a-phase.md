# 012. The worldsheet S-matrix is a phase
**Status:** open
**Depends on:** 001
**Predictions:** P03

## Claim
The transverse oscillations of a long string are massless particles on
the two-dimensional worldsheet. Their two-body scattering, computed
from the Nambu-Goto action, is a pure phase,

    S(s) = exp( i s / (4 sigma) ),     s = worldsheet Mandelstam invariant,

with no particle production, to all orders, in d = 26 and d = 3. Putting
this S-matrix on a circle of length R through the thermodynamic Bethe
ansatz reproduces the square-root spectrum of 001 exactly. In d = 4 the
first correction appears at one loop, is proportional to (26 - d), and
breaks the pure-phase form in the channel where the two transverse
polarisations annihilate. This is what the critical dimension means for
a hadronic string: it is the coefficient of the first inelastic term on
the worldsheet, and the term is small.

## Known in 1974
* GGRT: the transverse modes and their free spectrum.
* Nothing on scattering of the modes among themselves.

## What the memory says
* Dubovsky-Flauger-Gorbenko 2012: the phase above; its origin as the
  gravitational dressing of free bosons; the (26-d) one-loop term from
  the Polchinski-Strominger action.
* Dubovsky-Gorbenko-Mirbabayi 2013, Caselle et al 2013: the same phase is
  the TTbar deformation of the free theory, and the TBA gives Arvis.
* Chen, Conkey, Dubovsky, Hernandez-Chifflet 2018: the phase shift can be
  read off lattice spectra directly, and in d = 4 the residual after
  removing it is the resonance of 013.
* Elias Miro et al 2019: bootstrap bounds on the worldsheet S-matrix
  consistent with the lattice.

## Test
1. `[pencil]` Expand Nambu-Goto to quartic order in the transverse
   fields in static gauge; compute the tree-level 2 to 2 amplitude;
   check the phase shift 2 delta = s/(4 sigma).
2. `[pencil]` Solve the TBA for one species with this phase and recover
   the square root. Then for (d-2) species.
3. `[pencil]` One loop: identify the (26-d) term.
4. `[lattice, later]` Extract phase shifts from excited flux-tube levels.

## Expected outcome, and what would refute it
The square root recovered; a (26-d) one-loop term that is a few percent
effect at R sqrt(sigma) ~ 2. Refuted if the tree-level amplitude is not
a phase, or if lattice phase shifts at low energy deviate from the
linear law.

## References
GGRT1973, DFG2012a, DFG2012b, DGM2013, CFGT2013, CCDH2018, EliasMiro2019.
