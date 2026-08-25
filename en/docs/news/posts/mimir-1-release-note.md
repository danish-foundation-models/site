---
draft: false
date: 2026-08-14
slug: mimir-1-release-note
authors:
  - peter
tags:
  - Model Release
---

# DFM Mimir release note

Today, Danish Foundation Models releases **Mimir v1**, a 1-billion-parameter Hierarchical Reasoning Model (HRM-Text) trained from scratch using the [HRM-Text framework](https://arxiv.org/abs/2506.20072). Mimir v1 is optimised for Danish and English tasks and is trained exclusively on permissible and openly licensed data, staying true to the DFM philosophy.

<div style="text-align: center;">
  <img src="/_static/mimir-benchmark-comparison.png" alt="Benchmark comparison of DFM Mimir against HRM-Text, Qwen 3.5 2B, and Gemma 4 E2B IT" style="width: 100%;">
</div>
<p style="text-align: center; font-size: 0.85em; color: #6b7280;">
  Comparing DFM Mimir against the original HRM-Text, Qwen 3.5 4B and Gemma 4 E2B, demonstrating strong performance across a broad set of benchmarks.
</p>

<!-- more -->

## Why Mimir?
Current large language model development relies on massive, often non-permissible datasets, creating a high barrier for researchers committed to open-source and ethically sourced data. We introduce Mimir v1, a 1-billion-parameter language model based on the Hierarchical Reasoning Model (HRM) architecture, that is trained from scratch and delivers highly competitive performance for English and sets a new state of the art for Danish using only permissible post-training data. Trained on a mixture of 161 datasets, Mimir outperforms the original HRM-Text 1B and competes with larger frontier models like Qwen 3.5 4B and Gemma 4 E2B, tested across 20 benchmarks for English, Math & Code and Danish. 

## Technical Report 
Mirmir provides strong capabilites in both the Danish and English domains. See all our results in technical report [here](https://arxiv.org/pdf/2608.13517) and access the model on the Huggingface Hub [here](https://huggingface.co/danish-foundation-models/DFM-Mimir). 


# Contributors

We list contributions according to the [Contributor Roles Taxonomy (CRediT)](https://credit.niso.org):

- **Peter Schneider-Kamp**: *Conceptualization*, *Data curation*, *Formal analysis*, *Funding acquisition*, *Investigation*, *Methodology*, *Project administration*, *Resources*, *Software*, *Supervision*, *Validation*, *Visualization*, *Writing – original draft*, *Writing – review & editing*
- **Jacob Nielsen**: *Formal analysis*, *Investigation*, *Methodology*, *Software*, *Validation*, *Visualization*, *Writing – original draft*, *Writing – review & editing*
- **Lukas Galke Poech**: *Formal analysis*, *Investigation*, *Methodology*, *Software*, *Supervision*, *Validation*, *Visualization*, *Writing – review & editing*
- **Gianluca Barmina**: *Data curation*, *Investigation*, *Writing – review & editing*
- **Kenneth Enevoldsen**: *Data curation*, *Resources*, *Writing – review & editing*

*Additional Contributors*:
- **Mogens Henrik From**: *Investigation*, *Project administration*, *Software*
- **Andrea Blasi Núñez**: *Formal analysis*, *Software*, *Visualization*
- **Annemette Brok Pirchert**: *Formal analysis*, *Software*, *Visualization*
- **Stine Lyngsø Beltoft**: *Data curation*, *Resources*
- **Torben Blach**: *Project administration*, *Funding acquisition*
- **Sofie Helene Bruun**: *Data curation*, *Resources*
- **Oliver Kinch**: *Data curation*, *Resources*
- **Rasmus Larsen**: *Data curation*, *Resources*
- **Dan Saattrup Smart**: *Data curation*, *Resources*
- **Kristoffer Laigaard Nielbo**: *Funding acquisition*

# Acknowledgements
This work originated within [OdenseNLP](https://odensenlp.github.io) and was supported by the Danish Foundation Models project — a collaboration between the University of Southern Denmark, Aarhus University, the Alexandra Institute, and the University of Copenhagen — funded by the Ministry of Science, Higher Education and Digital Affairs. We thank all members of the Danish Foundation Models project and the OdenseNLP research group for many fruitful discussions and their continued support.

