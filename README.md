#  Analysis of the 'trench pull force' in a numerical subduction Zone Model

This repostory contains data and post-processing analysis for a 2D numerical model of subduction. $x=1$

The key focus of this anaysis is to examine the **vertically integrated horizontal force balance** based on a numerical subduction model, which provides approximate solutions to the stress equilbrium equations.

The model run with the open-source code [MDOODZ7.0](https://github.com/tduretz/MDOODZ7.0), developed by Thibault Duretz and collaborators, based on the input file (or SET) called `AnneloreSubduction`. This setup was designed to replicate the "forced subduction" model from https://doi.org/10.1093/gji/ggaa092. 

This model analysis (jupyter notebook) was developed as part of the reponse to reviewers comments for the following manuscript: (https://doi.org/10.31223/X5TQ50). In this manuscript, a simple scaling relationship is developed for the net horizontal force due to the relative trench topography (the "trench pull force"). The relationship is:  

```
(\Delta \rho ) g w_T ( \frac{z'_m}{2}) \approx (\Delta \rho ) g w_T z'_{np}
```

where $w_T$ is the relative depth of the trench, and $z'_m$ is the mechanical thickness of the lithosphere, which is generally signficantly less than the thermal thickness, with the depth of the $z'_{np}$ being approximately half $z'_m$. 

This scaling is based on assumptions about the depth at which the support of the non-isostatic topography occurs; this is equilivalent to a statement about the depth at which verrtical normal stress equilbrates, between a column of lithipshere beneath the trench, compared to an isostatic column. 

The notebook also considerers other issues raised by the reviewers, such as the assumption that we can neglect pressure gradients along an equiponential surface beneath the lithosphere.

## Overview of repository


