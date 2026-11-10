# 012. The worldsheet S-matrix is a phase
**Status:** tree level derived; the route to the square root rests on two rules assumed beyond first order; lattice test open
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

## 1984 paper
`outputs/1984-critical-dimension/` (QCDS-84/1). Test 1 done: the tree
amplitude of the area action is pure transmission with 2 delta = s/4 sigma
(`code/effective_string.py`, part D); the quartic term is the product of the
energy densities of the two directions of motion. Test 2 done at first order
and assumed beyond: free phonons on a string lengthened by the momentum of the
opposite movers give the square roots of the closed and the open string if the
zero-point motion and the standing waves obey the same rule; at first order
that is the derived shift -2 E+ E-/(sigma L). For one transverse direction
crossing and elastic unitarity make the phase odd in s, so no s^2 term exists.
Test 3 answered by a proposal instead of a loop calculation: Polyakov's
anomaly on the induced metric gives the vertex (26-d)[d_a(dX.dX)]^2/384 pi,
with amplitude (26-d) s^3/192 pi sigma^2 in the annihilation and reflection
channels; it is a total derivative for d = 3 and in d = 4 splits the closed
tube's level N = Nbar = 1 by -/+ 22 (4 pi^3/3)/(sigma^2 L^5) at first order
(about half of that at L sqrt(sigma) = 6 with dressed momenta). Test 4 (phase
shifts from lattice levels) was planned for this slot as a measurement of the
closed tube's two-phonon level and dropped when the programme turned to
theory; see the repository issues.

## References
GGRT1973, DFG2012a, DFG2012b, DGM2013, CFGT2013, CCDH2018, EliasMiro2019.
