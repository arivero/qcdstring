# Executed checks

Environment: Python 3.12.14, SciPy 1.17.0.
All 11 consistency checks passed. No experimental data were used.

These checks validate the arithmetic and the explicitly assumed tensor toy model. They do not prove a decoupled interacting theory, solve a worldsheet, or fit QCD.

## Tensor spectrum

AdS-like hard wall, source-free UV behavior, infrared Neumann condition, z0=L=1.

| Mode | m z0 | Numerical norm | Rayleigh quotient |
|---|---:|---:|---:|
| 1 | 3.831705970 | 0.081107565 | 14.681970642 |
| 2 | 7.015586670 | 0.045034732 | 49.218456322 |
| 3 | 10.173468135 | 0.031176263 | 103.499453895 |

At m=0 the constant solution is UV-nonnormalizable. The normalizable z^4 solution fails the Neumann wall condition. Changing the wall to z psi'-4 psi=0 restores that zero mode. Thus the absence of a massless tensor depends on the physical boundary problem.

## Long-string benchmark in four dimensions

r=R sqrt(sigma); energy units sqrt(sigma). The square-root expression is a Nambu-Goto benchmark, not an asserted exact UV spectrum.

| r | Square-root energy | Through r^-3 | Difference |
|---:|---:|---:|---:|
| 2 | 1.8645109880 | 1.8648166236 | 3.056e-04 |
| 4 | 3.9340057479 | 3.9340146927 | 8.945e-06 |
| 8 | 7.9672078688 | 7.9672081440 | 2.752e-07 |
| 16 | 15.9836291631 | 15.9836291717 | 8.567e-09 |

The leading correction is -pi/(12R); the next displayed coefficient is -pi^2/(288 sigma R^3). Their scope is a long string with two massless transverse modes.

## NCOS scaling

Set alpha_eff'=1 and G_o^2=0.2. Suppress the overall normalization of G10.

| delta | alpha' | Bulk g_s | G10/(alpha_eff')^4 factor |
|---:|---:|---:|---:|
| 1e-02 | 1e-02 | 2.0 | 4.0e-08 |
| 1e-04 | 1e-04 | 20.0 | 4.0e-14 |
| 1e-06 | 1e-06 | 200.0 | 4.0e-20 |

The open scale and coupling stay finite in this bookkeeping. Metric scaling and the closed-channel amplitude still require the full NCOS analysis.

## Other checks

- Universal soft couplings satisfy momentum conservation at the chosen 2-to-2 kinematic point; a specified unequal assignment fails.
- A handle changes the vacuum color weight by N^-2 and a fixed-flavor boundary by N^-1.
- At fixed alpha', the bulk gravitational factor is proportional to g_s^2. The ordinary open disk four-point coupling also vanishes as g_s goes to zero.
- Four free embedding dimensions require additional matter central charge 22 for a conventional bosonic critical string, or 9 for a conventional RNS construction.

## Not yet calculated

The annulus comparison, little-string interaction observables, a microscopic trace Hamiltonian, a smooth confining background, tensor residues, hard scattering in the same model, and a consistent internal spectrum remain proposed work.

Full numeric output and individual checks are in results.json. Run checks.py to regenerate both output files.
