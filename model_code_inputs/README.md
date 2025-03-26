# The numerical model¶

## Overview

MDOODZ7.0 code is an open source geodyamics code, based on the finite-difference/marker-and-cell technique, available at https://github.com/tduretz/MDOODZ7.0/.

The version used to run this model has Git commit hash `08544b3433':

This setup was dedigned to replicate the "forced subduction" model from https://doi.org/10.1093/gji/ggaa092.

The model is based on the input file (or SET) called AnneloreSubduction, see https://github.com/tduretz/MDOODZ7.0/blob/main/SETS/AnneloreSubduction.txt


## Modification to the input files

Minor modification were made to correct errors in the input file. 


## Model output files

Numerical models of Stokes Flow, such as the one analyised in this notebook, provide solutions to the stress equilibrium equations. We therefore have direct access to stress comoponents needed to estimate terms in the vertically integrated form of the horizontal force balance, (as described in the manuscript and notebook). 

A series of h5 output files are found in the `../model_code_inputs directory` These represent (roughly) 0.5 Myr intervals, from 0 - 10 Myr.

Due to Github space limitaio, the h5 files been filtered so they contain only the datasets required for the analysis. 

The anlysis notebook shows how to convert the h5 data to a pyvista mesh, which can be viewed using the plotting capability in pyvista, or saved to a Paraview compatible format,  

## Modification to the input files

## Parameter table

| Symbol           | Description                            | Material 1: Mantle | Material 2: Lithosphere | Material 3: Weak Layer |
| ---------------- | -------------------------------------- | ------------------ | ----------------------- | ---------------------- |
| ID               | Phase identity                         | 0 (Mantle)         | 1 (Lithosphere)         | 2 (Weak Layer)         |
| $\rho$           | Density (kg/m³)                        | 3250.00            | 3250.00                 | 3250.00                |
| $G$              | Shear modulus (Pa)                     | 3e10               | 3e10                    | 3e10                   |
| $C_v$            | Heat capacity (J/kg·K)                 | 1050               | 1050                    | 1050                   |
| $k$              | Thermal conductivity (W/m·K)           | 3.0                | 3.0                     | 3.0                    |
| $Q_r$            | Radiogenic heat production (W/m³)      | 1e-10              | 1e-10                   | 1e-10                  |
| $C$              | Cohesion (Pa)                          | 1e6                | 1e7                     | 1e6                    |
| $\phi$           | Friction angle (°)                     | 5                  | 30                      | 0                      |
| $S_\mathrm{lim}$ | Stress cutoff (Pa)                     | 500e9              | 500e9                   | 500e9                  |
| $\alpha$         | Coefficient of thermal expansion (1/K) | 8e-6               | 8e-6                    | 8e-6                   |
| $\beta$          | Coefficient of compressibility (1/Pa)  | 1e-11              | 1e-11                   | 1e-11                  |
| $d\rho$          | Density variation (kg/m³)              | 0                  | 0                       | 0                      |
| cstv             | Constant viscosity switch              | 0                  | 0                       | 0                      |
| pwlv             | Dislocation creep parameter            | 40                 | 40                      | 40                     |
| linv             | Diffusion creep parameter              | 40                 | 40                      | 40                     |
| gbsv             | Grain boundary sliding parameter       | 0                  | 0                       | 0                      |
| expv             | Peierls creep parameter                | 40                 | 40                      | 40                     |
| gsel             | Grain size evolution switch            | 0                  | 0                       | 0                      |
| $\eta_0$         | Constant viscosity (Pa·s)              | 1e22               | 1e22                    | 1e22                   |
| gs_ref           | Reference grain size (m)               | 5e-3               | 5e-3                    | 5e-3                   |
