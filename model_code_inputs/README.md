# The numerical model¶


The MDOODZ7.0, code is based on the finite-difference/marker-and-cell technique. The version compile to run this model was as the commit hash `08544b3433':

Numerical model of Stokes Flow, such as the one analyised in this notebook, provide approximate solutions to the stress equilibrium equations. They therefore provide all of the stress terms we need to analyse the verticaly integrated form of the horizontal force balance, which is descibed in the notebook. 

This setup was dedigned to replicate the "forced subduction" model from https://doi.org/10.1093/gji/ggaa092.

The model is based on the input file (or SET) called AnneloreSubduction

## Modification to the input files


## Modification output files

A series of h5 output files are found in the `../model_code_inputs directory` These represent (roughly) 0.5 Myr intervals, from 0 - 10 Myr.


## Modification to the input files

Parameter table
