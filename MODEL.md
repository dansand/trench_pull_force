# MODEL.md — MDOODZ elasto-plastic subduction model (R0)

Structured model description and raw-field disambiguation for this repo's analysis.
Schema: `trench-pull-model/1` (defined in the umbrella project,
`tools/MODEL_SCHEMA.md`); symbols follow `SYMBOLOGY.md` in this repo.

```yaml
schema: trench-pull-model/1

model:
  key: MD7_R0
  code: MDOODZ 7.0 (finite difference, marker-in-cell; visco-elasto-plastic)
  provenance: >
    Variant of the force-balanced subduction model S0 of Bessat et al. (2020),
    doi:10.1093/gji/ggaa092, re-run with MDOODZ 7.0 and modified outflow boundary
    conditions — a comparable but distinct realisation, not a reproduction.
    Input files: model_code_inputs/ in this repo. Companion manuscript:
    2026_version (Sandiford), preprint doi:10.22541/essoar.174413825.53806221/v1.
  cases:
    - MD7_R0 (this repo's model_output_data/MD7_R0/)
    - S0, S1 (original Bessat et al. outputs, limited set, CSV-summarised only)

domain:
  extents:
    x: "[-1600, 1600] km (analysis frame)"
    z: "[-20, 660] km — z-down analysis frame; 20 km sticky-air above z = 0,
        z = 0 at the initial rock surface"
  resolution: "uniform staggered finite-difference grid; Nx, Nz read from
    /Model/Params per file; dx, dz derived (order 1 km)"
  key_locations:
    z_c_depth: "100 km — default compensation depth for the integrations"
  time: "snapshots Output*.h5 every 100 steps; time in s at /Model/Params[0]"

native_frame:
  coordinates: "z positive UP (MDOODZ native); x as analysis frame"
  stress_sign: "engineering — tension positive, compression negative"
  stress_register: "sxxd is the DEVIATORIC normal stress; pressure separate"
  pressure: "total pressure P at cell centers (not lithostatic-subtracted)"
  layout: "staggered: P, T, sxxd at cell centers; sxz at vertices;
    topography as marker chain under /Topo"

extraction:
  - "np.flipud on every 2D field — native z-up to analysis z-down"
  - "sxz -> -1 * sxz — shear sign flip under the z-flip (diagonal components
     and pressure are invariant)"
  - "no mirror: subducting plate is already on the right"
  - "vertices_to_horizontal_faces / vertices_to_vertical_faces map the vertex
     shear onto face centers (tau_zx_hface / tau_zx_vface) for the integrals"

field_map:
  - {native: /Centers/P,      location: centers,  canonical: "-sigma_I (total pressure)",
     transform: "flipud; sigma_I = -P",                       units: Pa}
  - {native: /Centers/sxxd,   location: centers,  canonical: "tau_xx (deviatoric); tau_zz = -tau_xx (2D traceless)",
     transform: "flipud",                                     units: Pa}
  - {native: /Vertices/sxz,   location: vertices, canonical: "tau_zx",
     transform: "-1 * flipud",                                units: Pa}
  - {native: /Centers/T,      location: centers,  canonical: "T (auxiliary)",
     transform: "flipud",                                     units: K}
  - {native: /Topo/x_mark, /Topo/z_mark, location: markers, canonical: "surface; w = -topo",
     transform: "sort by x; deflection w positive downward",  units: m}
  - {native: /Model/Params,   location: global,   canonical: "n/a (time, Nx, Nz, ...)",
     transform: "Params[0] s -> Myr via 3.1436e13; Params[3], Params[4] = Nx, Nz",
     units: mixed}
```

Derived full-tensor components are reconstructed as
$\sigma_{xx} = \sigma_I + \tau_{xx}$, $\sigma_{zz} = \sigma_I + \tau_{zz}$; the
force-balance integrals then use $\sigma_{xx}-\sigma_{zz}$ (the in-plane
differential resultant's integrand), $\bar\sigma_{zz}$ ($\mathrm{GPE}^*$), and
$\tau_{zx}$ ($V$, $F_B$) per `SYMBOLOGY.md`.
