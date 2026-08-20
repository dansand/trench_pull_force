# Symbology evidence — manuscript vs code

Generated 2026-08-20 by `tools/manuscript_symbols.py`. Rerun it after any notation change.

**Method.** Symbols are extracted from *math mode only* — `$...$`, `\[...\]`,
`equation`/`align` environments — in `2026_version/main.tex` + `si.tex`, and from math
spans in notebook source cells, `.qmd`, `.typ` and `.md` across the repos. Prose and
Python identifiers are excluded, so `F_D` here means "F_D rendered as mathematics", not
"the letters F_D somewhere in a file". Scratch, archive, WIP and the backup clone are
skipped.

**Columns:** `ms` = manuscript, `tpf` = trench_pull_force, `tpfl` = trench_pull_fluidity,
`talk` = egu_2026, `postr` = egu_2026_poster.

**Reading it.** "MANUSCRIPT ONLY" is not automatically a defect — the elasto-plastic
bending symbols (`sigma_Y`, `M_p`, `kappa_y`, `varphi_c`, `t_c`, `k_f`, `mu`, `nu`)
belong to theory that the Fluidity analysis does not implement. The defects are the rows
where *the same physical quantity* is written two different ways.

---

# Manuscript symbol inventory

Symbols appearing >=3x in main.tex + si.tex math mode: 55

| symbol                 |   ms |   tpf |  tpfl |  talk | postr | note |
|------------------------|------|-------|------|-------|-------|------|
| V                      |  100 |    20 |    50 |    11 |     3 |  |
| z                      |   81 |    42 |    61 |    18 |    16 |  |
| zeta                   |   76 |     0 |     0 |     2 |     0 |  |
| x                      |   73 |    59 |   109 |    36 |    27 |  |
| sigma_zz               |   65 |    24 |    23 |    21 |     1 |  |
| g                      |   60 |     9 |    16 |    11 |    21 |  |
| h                      |   60 |     2 |     3 |     0 |    18 |  |
| rho                    |   54 |     6 |     5 |     3 |     0 |  |
| GPE                    |   48 |     0 |     0 |     0 |     0 | MANUSCRIPT ONLY |
| tau_zx,x               |   45 |     0 |     0 |     2 |     0 |  |
| N_D                    |   44 |     0 |     0 |     0 |     0 | MANUSCRIPT ONLY |
| w_T                    |   43 |     7 |     8 |     2 |     0 |  |
| sigma_xx               |   43 |    18 |     5 |    24 |     1 |  |
| w                      |   33 |     1 |    10 |     0 |     5 |  |
| tau_zx                 |   33 |     3 |     1 |     1 |     0 |  |
| z_c                    |   31 |    10 |    12 |     6 |     4 |  |
| sigma_Y                |   24 |     0 |     0 |     0 |     0 | MANUSCRIPT ONLY |
| h_m                    |   23 |     0 |     0 |     0 |     0 | MANUSCRIPT ONLY |
| rho_m                  |   18 |     8 |     6 |     0 |     0 |  |
| s                      |   18 |     2 |    31 |     2 |     4 |  |
| RHO                    |   18 |     0 |     0 |     0 |     0 | MANUSCRIPT ONLY |
| rho_w                  |   15 |     7 |     2 |     0 |     0 |  |
| M_p                    |   15 |     0 |     0 |     0 |     0 | MANUSCRIPT ONLY |
| M                      |   14 |     0 |     4 |     0 |     0 |  |
| alpha                  |   12 |     1 |     0 |     0 |     0 |  |
| P_T                    |   11 |     8 |     6 |     2 |     0 |  |
| x_I                    |    8 |     9 |    26 |     3 |     2 |  |
| F_B                    |    8 |    19 |    25 |    27 |     5 |  |
| Delta                  |    8 |    10 |     1 |     3 |     0 |  |
| Q                      |    8 |     0 |     0 |     0 |     0 | MANUSCRIPT ONLY |
| D                      |    6 |     0 |     4 |     6 |    16 |  |
| rho_c                  |    6 |     0 |     0 |     0 |     0 | MANUSCRIPT ONLY |
| beta                   |    6 |     1 |     0 |     0 |     0 |  |
| I                      |    6 |     1 |     2 |     0 |     0 |  |
| x_T                    |    5 |     6 |    52 |     4 |     1 | code-heavy |
| L_TI                   |    5 |     0 |     0 |     0 |     0 | MANUSCRIPT ONLY |
| E                      |    5 |    47 |    63 |    63 |    14 | code-heavy |
| t_c                    |    5 |     0 |     0 |     0 |     0 | MANUSCRIPT ONLY |
| varphi_c               |    5 |     0 |     0 |     0 |     0 | MANUSCRIPT ONLY |
| theta                  |    5 |     0 |    38 |     0 |     0 | code-heavy |
| L                      |    4 |     0 |     2 |     0 |     0 |  |
| xi                     |    4 |     0 |    57 |     0 |     0 | code-heavy |
| kappa                  |    4 |     0 |    13 |     0 |     0 |  |
| kappa_y                |    4 |     0 |     0 |     0 |     0 | MANUSCRIPT ONLY |
| z_0                    |    3 |     0 |     0 |     0 |     3 |  |
| sigma_m                |    3 |     0 |     0 |     0 |     0 | MANUSCRIPT ONLY |
| tau_xx                 |    3 |     9 |    23 |     5 |     0 | code-heavy |
| nu                     |    3 |     0 |     0 |     0 |     0 | MANUSCRIPT ONLY |
| k_f                    |    3 |     0 |     0 |     0 |     0 | MANUSCRIPT ONLY |
| C                      |    3 |     3 |    16 |     0 |     0 | code-heavy |
| mu                     |    3 |     0 |     0 |     0 |     0 | MANUSCRIPT ONLY |
| z_cm                   |    3 |     0 |     0 |     0 |     0 | MANUSCRIPT ONLY |
| delta                  |    3 |     0 |     0 |     0 |     0 | MANUSCRIPT ONLY |
| P                      |    3 |    50 |    65 |    60 |    14 | code-heavy |
| varphi_h/2             |    3 |     0 |     0 |     0 |     0 | MANUSCRIPT ONLY |


# Symbols common in CODE but rare/absent in the manuscript

| F_D                    | ms=  0 | code= 237 |
| G                      | ms=  0 | code= 175 |
| t                      | ms=  0 | code= 124 |
| l                      | ms=  0 | code= 121 |
| e                      | ms=  0 | code= 116 |
| a                      | ms=  0 | code= 113 |
| d                      | ms=  0 | code= 107 |
| r                      | ms=  0 | code=  95 |
| textcolor              | ms=  0 | code=  81 |
| u                      | ms=  0 | code=  79 |
| b                      | ms=  0 | code=  75 |
| c                      | ms=  0 | code=  69 |
| i                      | ms=  0 | code=  66 |
| n                      | ms=  0 | code=  55 |
| m                      | ms=  0 | code=  53 |
| f                      | ms=  0 | code=  49 |
| k                      | ms=  0 | code=  48 |
| p                      | ms=  0 | code=  43 |
| eta                    | ms=  0 | code=  34 |
| tau_zz                 | ms=  2 | code=  32 |
| tau_xz                 | ms=  1 | code=  30 |
| F                      | ms=  1 | code=  28 |
| T                      | ms=  2 | code=  26 |
| o                      | ms=  0 | code=  25 |


# First use in the manuscript (top 30 by frequency)

**V**  (main.tex)
  ...alance:assumptions}), the weight change is set by the densities of the two fluids that bound the plate --- the seawater above ($\rho_w$) and the hydrostatic mantle beneath ($\rho_m$) --- so \begin{equation} Q(z_c) \;=\; \int_0^{z_c}\tau_{zx,x}\,dz \;=\; \frac{

**z**  (main.tex)
  ...ange in the vertically integrated vertical normal stress, $-\Delta\bar\sigma_{zz}$, between the trench and the nearest isostatic column. Graphically, the trench pull is the area between the $-\sigma_{zz}(z)$ curves of the two columns: the topography sets the a

**zeta**  (main.tex)
  ...ensity and the dipole} \label{sec:balance:szz}\label{sec:balance:dipole} The vertical normal stress follows from integrating the vertical component of equilibrium downward from the surface, \begin{equation} -\sigma_{zz}(z) \;=\; \underbrace{\int_0^{z}\!\rho\,g

**x**  (main.tex)
  ...surface, which is stress-free and contributes nothing at any slope \cite{schmalholz2014relationship}. With $\bar{(\cdot)}\equiv\int_0^{z_c}(\cdot)\,dz$ denoting the integral over a column, \begin{equation} \Delta\bar\sigma_{xx} + F_B = 0 , \qquad F_B \equiv \

**sigma_zz**  (main.tex)
  ...n: the retention of the full vertical normal stress. The trench pull force is then defined exactly as ridge push is: as the change in the vertically integrated vertical normal stress, $-\Delta\bar\sigma_{zz}$, between the trench and the nearest isostatic

**g**  (main.tex)
  ...this study): \begin{quote}\small A driving force may arise in the same way as that at ridges. Because mantle rock is replaced by water, the lithostatic pressure at all depths is reduced by $(\rho_m-\rho_w)\,g\,w_T$, where $w_T$ is the depth of the trench. How

**h**  (main.tex)
  ...force balance in itself. It can be evaluated between any two columns of lithosphere, independent of any proposed mechanism, and what defines the trench pull force is the choice of columns: \begin{align} \text{trench pull force} &\equiv -\Delta\bar\sigma_{zz}

**rho**  (main.tex)
  ...ensity and the dipole} \label{sec:balance:szz}\label{sec:balance:dipole} The vertical normal stress follows from integrating the vertical component of equilibrium downward from the surface, \begin{equation} -\sigma_{zz}(z) \;=\; \underbrace{\int_0^{z}\!\rho\,g

**GPE**  (main.tex)
  ...cite{lister1975gravitational,dahlen1981isostasy}; this paper concerns the non-isostatic domain, where the basal term is negligible over the short horizontal scale and the balance reduces to $\Delta N_D\approx\Delta\GPE$ (Eqs.~\ref{eq:FD} and~\ref{eq:identity})

**tau_zx,x**  (main.tex)
  ...the two columns: the topography sets the amplitude, and the equilibration with depth sets the area. The equilibration is due to the depth distribution of the vertical shear-stress gradient, $\tau_{zx,x}$ --- exactly the information that thin-plate flexure theo

**N_D**  (main.tex)
  ...basal shear and by a change in the in-plane stress resultant; the basal term is second order over the short flexural window, so the balance falls almost entirely on the in-plane resultant: $\Delta N_D\approx-\Delta\bar\sigma_{zz}$. For standard assumptions ab

**w_T**  (main.tex)
  ...this study): \begin{quote}\small A driving force may arise in the same way as that at ridges. Because mantle rock is replaced by water, the lithostatic pressure at all depths is reduced by $(\rho_m-\rho_w)\,g\,w_T$, where $w_T$ is the depth of the trench. How

**sigma_xx**  (main.tex)
  ...st isostatic column ($w=0$). For each domain, between the equipotentials $z_0$ and $z_c$, static equilibrium reduces to a sum of boundary terms (Eq.~\ref{eq:balance}): the column resultants $\bar\sigma_{xx}$ (arrows; signs enter through the outward normals), t

**w**  (main.tex)
  ...e thermal boundary layer); vertically exaggerated, not to scale. The boundary layer is split into two rectangular domains sharing the internal boundary at $x_I$, the first isostatic column ($w=0$). For each domain, between the equipotentials $z_0$ and $z_c$, s

**tau_zx**  (main.tex)
  ...sum of boundary terms (Eq.~\ref{eq:balance}): the column resultants $\bar\sigma_{xx}$ (arrows; signs enter through the outward normals), the basal shear $F_B$, and a traction-free surface ($\tau_{zx}=0$). Because the two balances share the column at $x_I$, tr

**z_c**  (main.tex)
  ...e. The boundary layer is split into two rectangular domains sharing the internal boundary at $x_I$, the first isostatic column ($w=0$). For each domain, between the equipotentials $z_0$ and $z_c$, static equilibrium reduces to a sum of boundary terms (Eq.~\ref

**sigma_Y**  (main.tex)
  ...undation stiffness & $k_f=\Delta\rho\,g$ & $2.26\times10^{4}$ & \si{\pascal\per\meter} \\ trench shear resultant (reference) & $V$ & 4 & \si{\tera\newton\per\meter} \\ Tresca yield stress & $\sigma_Y$ & 150 & \si{\mega\pascal} \\ plastic moment & $M_p=\sigma_Y

**h_m**  (main.tex)
  ...on_compare.pdf} \caption{Ridge push and trench pull as topographic pressure anomalies for old oceanic lithosphere, relative to the same isostatic reference column ($\sim$100-Myr columns; $h_m\approx60$~\si{\kilo\meter}, $L\approx100$~\si{\kilo\meter}). (b)~

**rho_m**  (main.tex)
  ...this study): \begin{quote}\small A driving force may arise in the same way as that at ridges. Because mantle rock is replaced by water, the lithostatic pressure at all depths is reduced by $(\rho_m-\rho_w)\,g\,w_T$, where $w_T$ is the depth of the trench. How

**s**  (main.tex)
  ...ensity and the dipole} \label{sec:balance:szz}\label{sec:balance:dipole} The vertical normal stress follows from integrating the vertical component of equilibrium downward from the surface, \begin{equation} -\sigma_{zz}(z) \;=\; \underbrace{\int_0^{z}\!\rho\,g

**RHO**  (main.tex)
  ...as the units of $\rho g$ --- a specific weight. Dividing it by $g$ gives a quantity with the units of a density, and Eq.~\eqref{eq:szz} can then be written as a single lithostatic integral, \begin{equation} -\sigma_{zz}(z)\;=\;g\!\int_0^{z}\!\Big(\rho+\frac{\t

**rho_w**  (main.tex)
  ...this study): \begin{quote}\small A driving force may arise in the same way as that at ridges. Because mantle rock is replaced by water, the lithostatic pressure at all depths is reduced by $(\rho_m-\rho_w)\,g\,w_T$, where $w_T$ is the depth of the trench. How

**M_p**  (main.tex)
  ...{4}$ & \si{\pascal\per\meter} \\ trench shear resultant (reference) & $V$ & 4 & \si{\tera\newton\per\meter} \\ Tresca yield stress & $\sigma_Y$ & 150 & \si{\mega\pascal} \\ plastic moment & $M_p=\sigma_Y h^{2}/4$ & $1.35\times10^{17}$ & \si{\newton} \\ element

**M**  (main.tex)
  ...zeta / \int \hat\rho\,d\zeta$, which stays near mid-plate. Its denominator, $g^{-1}\,dV/dx$, vanishes at the isostatic columns, and the line is not drawn there. (e)~The resultants $V$ (with $dM/dx$ overlain), $M$, and $\Delta\GPE(x)$ with $\Delta N_D(x)$ overl

**alpha**  (main.tex)
  ...ef{tab:params}). Each is a plate of uniform thickness $h$ and length $L$, resting on a buoyant foundation, loaded at its trench edge, and clamped at the far edge. The domain is long enough ($L\approx13\alpha$, with $\alpha$ the flexural parameter) that the cla

**P_T**  (main.tex)
  ...ertical force applied to the trailing plate, coupled to a horizontal force through a pressure deficit. We adopt the name `trench pull force', following \citeA{bird1998testing}, and refer to $(\rho_m-\rho_w)\,g\,w_T\equiv\Delta P_T$ as the trench pressure defic

**x_I**  (main.tex)
  ...lized subducting plate (a convective thermal boundary layer); vertically exaggerated, not to scale. The boundary layer is split into two rectangular domains sharing the internal boundary at $x_I$, the first isostatic column ($w=0$). For each domain, between th

**F_B**  (main.tex)
  ..._c$, static equilibrium reduces to a sum of boundary terms (Eq.~\ref{eq:balance}): the column resultants $\bar\sigma_{xx}$ (arrows; signs enter through the outward normals), the basal shear $F_B$, and a traction-free surface ($\tau_{zx}=0$). Because the two ba

**Delta**  (main.tex)
  ...ery column. Stress carries the usual continuum sign convention, positive in tension and negative in compression, so $-\sigma_{zz}$ is positive beneath the surface. The difference operator $\Delta(\cdot)\equiv(\cdot)(x_I)-(\cdot)(x_T)$ compares the isostatic

**Q**  (main.tex)
  ...ensity and the dipole} \label{sec:balance:szz}\label{sec:balance:dipole} The vertical normal stress follows from integrating the vertical component of equilibrium downward from the surface, \begin{equation} -\sigma_{zz}(z) \;=\; \underbrace{\int_0^{z}\!\rho\,g

