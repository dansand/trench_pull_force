#  Analysis of the 'trench pull force' in a numerical subduction Zone Model

This repository contains data and post-processing analysis for a 2D numerical model of subduction. 

The key focus of this analysis is to examine the **vertically integrated horizontal force balance** based on a numerical subduction model, which provides approximate solutions to the stress equilibrium equations.

The model was run with the open-source code [MDOODZ7.0](https://github.com/tduretz/MDOODZ7.0), developed by Thibault Duretz and collaborators, based on the input file (or SET) called `AnneloreSubduction`. This setup was designed to replicate the "forced subduction" model from https://doi.org/10.1093/gji/ggaa092. 

This model analysis (jupyter notebook) was developed as part of the response to reviewers comments for the following manuscript: (https://doi.org/10.31223/X5TQ50). In this manuscript, a simple scaling relationship is developed for the net horizontal force due to the relative trench topography (the "trench pull force"). The scaling is based on assumptions about the depth at which the support of the non-isostatic topography occurs; this is equivalent to a statement about the depth at which vertical normal stress equilbrates, between a column of lithosphere beneath the trench, compared to an isostatic column. 

The notebook also considerers other issues raised by the reviewers, such as the assumption that we can neglect pressure gradients along an equiponential surface beneath the lithosphere.

The mathmatical background is contained with the jupyter notebook, so that I didn't have translate it to Github-compatable markdown.


## Overview of repository

- [model_output_data](./model_output_data)
  - contains the h5 outputs from the model. These have been compacted so they contain the necessary scalar data to run the analysis
- [postprocessing_notebooks](./postprocessing_notebooks)
  - contains the jupyter notbook(s) that implent the analyis
- [model_code_inputs](./model_code_inputs)
  - contains MDOOD7.0 input files to run the model
- [papers](./papers)
