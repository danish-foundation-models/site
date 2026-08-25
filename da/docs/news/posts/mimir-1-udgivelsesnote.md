---
draft: false
date: 2026-08-14
slug: mimir-1-udgivelsesnote
authors:
  - peter
tags:
  - Modeludgivelse
---

# DFM Mimir-udgivelsesnote

I dag udgiver Danish Foundation Models **Mimir v1**, en HRM-sprogmodel med 1 milliard parametre (HRM-Text), trænet fra bunden med [HRM-Text-rammeværket](https://arxiv.org/abs/2605.20613). Mimir v1 er optimeret til danske og engelske opgaver og trænet udelukkende på tilladelige data med brug af åbent licenserede data, hvor det er muligt, i tråd med DFM-filosofien.

<div style="text-align: center;">
  <img src="/_static/mimir-benchmark-comparison.png" alt="Benchmark-sammenligning af DFM Mimir med HRM-Text, Qwen 3.5 2B og Gemma 4 E2B" style="width: 100%;">
</div>
<p style="text-align: center; font-size: 0.85em; color: #6b7280;">
  Sammenligning af DFM Mimir med den oprindelige HRM-Text, Qwen 3.5 2B og Gemma 4 E2B, som viser stærk performance på tværs af et bredt sæt af benchmarks.
</p>

<!-- more -->

## Hvorfor Mimir?

Nuværende udvikling af store sprogmodeller er afhængig af massive, ofte ikke-tilladelige datasæt, hvilket skaber en høj barriere for forskere, der er forpligtede på open source og etisk datagrundlag. Vi introducerer Mimir v1, en sprogmodel med 1 milliard parametre baseret på Hierarchical Reasoning Model (HRM)-arkitekturen, som er trænet fra bunden og leverer stærkt konkurrencedygtig performance på engelsk samt sætter en ny state of the art for dansk ved udelukkende at bruge tilladelige post-træningsdata. Trænet på en blanding af 161 datasæt overgår Mimir den oprindelige HRM-Text 1B og konkurrerer med større frontier-modeller som Qwen 3.5 4B og Gemma 4 E2B, testet på tværs af 20 benchmarks for engelsk, matematik og kode samt dansk.

## Teknisk rapport

Mimir leverer stærke kapabiliteter i både det danske og det engelske domæne. Se alle resultater i den tekniske rapport [her](https://arxiv.org/pdf/2608.13517), og find modellen på Hugging Face Hub [her](https://huggingface.co/danish-foundation-models/DFM-Mimir).


# Bidragydere

Vi angiver bidrag i henhold til [Contributor Roles Taxonomy (CRediT)](https://credit.niso.org):

- **Peter Schneider-Kamp**: *Conceptualization*, *Data curation*, *Formal analysis*, *Funding acquisition*, *Investigation*, *Methodology*, *Project administration*, *Resources*, *Software*, *Supervision*, *Validation*, *Visualization*, *Writing – original draft*, *Writing – review & editing*
- **Jacob Nielsen**: *Formal analysis*, *Investigation*, *Methodology*, *Software*, *Validation*, *Visualization*, *Writing – original draft*, *Writing – review & editing*
- **Lukas Galke Poech**: *Formal analysis*, *Investigation*, *Methodology*, *Software*, *Supervision*, *Validation*, *Visualization*, *Writing – review & editing*
- **Gianluca Barmina**: *Data curation*, *Investigation*, *Writing – review & editing*
- **Kenneth Enevoldsen**: *Data curation*, *Resources*, *Writing – review & editing*

*Yderligere bidragydere*:
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

# Tak

Dette arbejde opstod i [OdenseNLP](https://odensenlp.github.io) og blev støttet af Danish Foundation Models-projektet, et samarbejde mellem Syddansk Universitet, Aarhus Universitet, Alexandra Instituttet og Københavns Universitet, finansieret af Ministeriet for Videnskab, Højere Uddannelse og Digitalisering. Vi takker alle medlemmer af Danish Foundation Models-projektet og OdenseNLP-forskningsgruppen for mange frugtbare diskussioner og deres fortsatte støtte.