---
title: "LOCALISE"
date: 2024-04-24
description: "Localising deep brain stimulation targets on clinical-quality MRI, using image quality transfer from high-quality data."
icon: "fa-solid fa-crosshairs"
accent: "cyan" # pink, cyan, purple, orange, red, green; also supports hex colors
status: "active" # active, paused, completed
tags: ["python", "pytorch", "fsl", "deep brain stimulation", "image quality transfer"]
---

Deep brain stimulation (DBS) targets are hard to see on the low-quality MRI typically acquired in clinical practice. LOCALISE uses image quality transfer: models trained on high-quality data learn how connectivity features relate to target anatomy, so targets can be localised reliably on clinical-like scans.

The `localise` command covers the full pipeline:

1. Create anatomical masks in the subject's space
2. Run probabilistic tractography with FSL
3. Predict a probability map of the target (e.g. VIM) with a pre-trained model

Pre-trained models are included for common low-quality protocols, and you can train your own on subjects with high-quality labels.

## Links

- Code: [github.com/akinayqz/localise](https://github.com/akinayqz/localise)
- Documentation: [open.win.ox.ac.uk/pages/yqzheng1/python-localise](https://open.win.ox.ac.uk/pages/yqzheng1/python-localise/)
- Papers:
  - [An image quality transfer approach for localising deep brain stimulation targets](https://doi.org/10.1162/imag.a.1005) (Imaging Neuroscience, 2025)
  - [A transfer learning approach to localising a deep brain stimulation target](https://doi.org/10.1007/978-3-031-43996-4_17) (MICCAI 2023)
