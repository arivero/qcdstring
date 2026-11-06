# Tensor and supersymmetry benchmark

The first tensor root is stable under three endpoint cutoffs; the independent Rayleigh quotient agrees; the sampled mode is nodeless.

| Endpoint cutoff | Radial eigenvalue | m_tensor / M_KK |
|---:|---:|---:|
| 1e-04 | 5.5241599998 | 1.5669021099 |
| 1e-05 | 5.5241599998 | 1.5669021099 |
| 1e-06 | 5.5241599998 | 1.5669021099 |

Rayleigh eigenvalue: 5.5241599997.
In the Brower–Mathur–Tan convention the squared eigenvalue is 4 times ours: 22.096640, agreeing with their rounded 22.097.

Regularity at the smooth tip and UV normalizability eliminate the zero mode analytically. No hard wall or fitted tensor mass is used.

The fermion spin structure on the contractible spatial circle is antiperiodic. Circle frequencies are (n+1/2) M_KK; bosonic frequencies are n M_KK. These are not a calculation of strongly interacting superpartner pole masses.

The same metric gives sigma = [2 lambda4/(27 pi)] M_KK^2. The tensor and unwanted KK scales have no parametric separation in the classical-gravity regime.

## Free worldsheet discriminator

Open interval of length R; two massless transverse scalars. Extra Majoranas, if present, are physical modes. Sector ground energies before projections:

| Content | Coefficient of pi/R |
|---|---:|
| two transverse bosons | -1/12 |
| two bosons + two NS Majoranas | -1/8 |
| two bosons + two R Majoranas | 0 |

Boundary conditions, projections and masses change this answer. These are analytic free-field controls, not claims about the physical QCD flux-tube spectrum.

Derivations: notes/SPIN2_AND_SUPERSYMMETRY.md. Run spin_susy_checks.py to reproduce the numerical calculation.
