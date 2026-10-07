---
title: "PathFinder"
date: 2026-07-15
description: "Joint low-rank decompositions of linked multimodal datasets, even when some modalities are missing in some domains (e.g. species)."
icon: "fa-solid fa-route"
accent: "pink" # pink, cyan, purple, orange, red, green; also supports hex colors
status: "active" # active, paused, completed
tags: ["python", "multimodal", "matrix decomposition", "cross-species"]
---

PathFinder finds common patterns across a set of related datasets. Datasets are organised by **domain** (for example, species) and **modality** (for example, fMRI, diffusion MRI or gene expression). Each dataset is decomposed into shared low-rank components: datasets in the same domain share their row components, and datasets in the same modality share their column components. Combinations that weren't measured are simply left out.

Beyond this table setting, PathFinder supports:

- **Datasets as graphs:** any set of datasets linked through lookup tables, not just a domain-by-modality table
- **SVD-style decompositions:** shared modes with dataset-specific amplitudes
- **ICA rotations:** for more interpretable components

## Links

- Code: [github.com/akinayqz/pathfinder](https://github.com/akinayqz/pathfinder)
- Paper: [PathFinder: Joint Decompositions of Linked Multimodal Datasets](https://arxiv.org/abs/2608.14951) (arXiv preprint, 2026)
- Archive: [doi.org/10.5281/zenodo.21383855](https://doi.org/10.5281/zenodo.21383855)
