# Tests and decisions

Priority P0 means the test constrains every proposal. P1 means it is a central construction or benchmark. P2 means it depends on an earlier success. Status describes this package, not the state of the literature.

| Test | Question and first output | Priority | Dependencies | Package status |
|---|---|---|---|---|
| [T01](ideas/T01_spin2.md) | What exactly forces a massless tensor to couple gravitationally? Derive the soft Ward identity. | P0 | None | Derivation included; full amplitude audit proposed |
| [T02](ideas/T02_open_closed.md) | Can the ordinary closed sector be removed? Factorize the annulus. | P0 | T01 | Proposed; known obstruction identified |
| [T03](ideas/T03_flux_tube.md) | What does a four-dimensional confining string predict? Compute its finite-size spectrum. | P1 | Defined gauge-theory target | Leading formulas checked |
| [T04](ideas/T04_large_N.md) | Can color ordering generate the microscopic string? Construct and test a trace basis. | P1 | SU(N) laboratory | Topological powers checked; dynamics proposed |
| [T05](ideas/T05_tensor_spectrum.md) | What is the spin-two object physically? Derive its state/operator dictionary, spectrum and couplings. | P1 | T01/T02; joint with T14 | Hard-wall toy and smooth D4 tensor benchmark solved; full residues/construction open |
| [T06](ideas/T06_hard_scattering.md) | Can the same candidate give Regge and hard fixed-angle behavior? Derive both limits. | P1 | T03 or T05 candidate | Proposed |
| [T07](ideas/T07_little_strings.md) | Can finite-tension interactions survive \(g_s\to0\)? Reproduce the NS5 limit. | P1 | Definition of retained sector | Scaling checked; interaction audit proposed |
| [T08](ideas/T08_ncos.md) | Can open strings interact after bulk closed strings decouple? Reproduce the NCOS annulus. | P1 | T02 for comparison | Scaling checked; annulus calculation proposed |
| [T09](ideas/T09_worldsheet_uv.md) | What is the ultraviolet completion of the confining worldsheet? Audit anomalies and extra modes. | P0/P2 | T03, T04 or T05 | Central-charge arithmetic checked |
| [T10](ideas/T10_internal_structure.md) | Which internal degrees of freedom encode gauge/flavor data? Build a spectrum, not a dimension count. | P1 | Candidate defined alongside T01/T02 | Proposed; promoted to first cycle |
| [T11](ideas/T11_top_yukawa.md) | Why is one up-type quark exceptionally heavy? Normalize a rank-one coupling and calculate corrections. | P1 | T10; joint with T12/T13 | Rank and one-loop RG controls executed; construction proposed |
| [T12](ideas/T12_generation_bound.md) | What bounds families, and does the bound survive removing gravity? | P1 | T10; explicit decoupling path | AF and positive-budget toy checked; geometric bound proposed |
| [T13](ideas/T13_scale_relation.md) | What relates confinement and weak symmetry breaking? Derive a ratio with thresholds and sensitivities. | P1 | T03–T06 and T10–T12 | Transmutation, QCD-breaking and threshold controls executed |
| [T14](ideas/T14_supersymmetry.md) | Why does supersymmetry appear, which charges exist, and what is its physical fate? | P1/P0 | T01/T02/T09; joint with T05 and T10–T13 | Charge distinctions and D4 breaking benchmark analyzed; full explanation open |

The central hadronic tests are T03, T05 and T06. The five explanatory targets are covered by T11–T13, T01/T05 and T14. Their construction starts immediately. T07 and T08 answer the independent existence question and provide controls for claims that gravity is inevitable. Supersymmetry breaking must be propagated through the flavor and scale calculations.

## Decision criteria

| Observation | Consequence |
|---|---|
| A standard massless spin-2 state survives with nonzero universal soft coupling | Accept that this sector is gravitational; change the model or its physical interpretation |
| Removing a state ruins a factorization channel | Reject that removal |
| Gravity vanishes only because all retained interactions vanish | Reject the claimed interacting nongravitational limit |
| The flux-tube expansion works only at large length | Record an infrared EFT; do not infer a full short-string theory |
| The tensor gap changes arbitrarily with an inserted wall | Record a boundary-dependent toy result; seek a dynamical infrared completion |
| A fixed-angle amplitude remains exponentially soft | Reject it as the intended hard hadronic amplitude, within the stated kinematics |
| A finite-tension nongravitational theory exists but has the wrong matter or spacetime | Count existence success and phenomenological failure separately |
| One controlled candidate passes the three hadronic tests | Establish a strong-sector success; also evaluate its T11–T13 predictions |
| One large Yukawa is protected but its value is arbitrary | Record a hierarchy mechanism; no numerical top-mass prediction yet |
| A family bound is finite at each compact point but unbounded in the limit | Reject a uniform nongravitational family-bound claim |
| The same construction constrains families, a top hierarchy and the scale ratio | Record the shared inputs and independent predictions; proceed to quantitative validation |
| The scale ratio is reproduced only by changing an unfixed coupling or a second scale | Record a conditional relation or fit, not a predicted proximity |
| A two-dimensional supercurrent is found but spacetime charges are not established | Record worldsheet supersymmetry only; compute the physical spectrum |
| Supersymmetry breaking invalidates a rank theorem or flux bound | Recalculate it before retaining the flavour claim |
| A smooth background gives a tensor gap and broken supersymmetry but light KK contamination | Count a mechanism benchmark; do not identify it with controlled pure QCD |

No test has been marked “passed” merely because a relevant result exists in the bibliography.
