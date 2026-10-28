---
draft: false
date: 2026-10-27
slug: mimir-geometry-of-ignorance
authors:
  - kenneth
tags:
  - Behind the Scenes
---

# Hvad falder Mimir tilbage på, når den ikke ved det?

Hvad forudsiger en sprogmodel, når konteksten kun giver den få ledetråde? En ny artikel,
[The Geometry of Ignorance (Liu et al., 2026)](https://arxiv.org/abs/2609.02959), argumenterer for, at den falder
tilbage på, hvor almindeligt hvert ord er. Dette udgangspunkt, modellens *prior*, er gemt langs én enkelt retning i
modellens outputlag: *uvidenhedens retning*. Hvor meget en forudsigelse peger langs den retning (kaldet λ),
fortæller, hvor meget modellen læner sig op ad sin prior. Vi har testet idéen på
[DFM Mimir](https://huggingface.co/danish-foundation-models/DFM-Mimir), mens den løste matematiske tekstopgaver fra
[multilingual GSM-symbolic](https://github.com/centre-for-humanities-computing/multilingual-gsm-symbolic) på otte sprog.

<div style="text-align: center;">
  <a class="md-button md-button--primary" href="https://github.com/KennethEnevoldsen/mimirs-geometry-of-ignorance">Kode, data og alle resultater →</a>
</div>

<!-- more -->

## Én prior pr. sprog

Den oprindelige artikel undersøgte engelskdominerede modeller, hvor én retning er nok til at fange prioren. Mimir
er tosproget, og det viser sig, at den gemmer **to** priors: én retning genskaber engelske ordfrekvenser
(R² = 0,73) og en anden de danske (R² = 0,81). De to retninger står vinkelret på hinanden (cosinus −0,02). En
tilfældigt initialiseret model giver R² = 0,05, så strukturen kommer fra træningen.

![Mimirs outputlag gemmer den engelske og den danske unigram-prior langs to ortogonale retninger](../images/mimir-ignorance-prior-fit.png){ style="display: block; margin: 0 auto;" }

## Retningen gør en forskel

Hvis vi skubber Mimirs interne tilstand langs uvidenhedens retning ved et ord, hvor modellen er usikker, bevæger
forudsigelsen sig mod den rene ordfrekvensfordeling. Skubber vi lige så langt i en tilfældig retning, sker det
ikke. Det stemmer med det kausale resultat i den oprindelige artikel.

![Styring langs prior-retningen trækker forudsigelsen mod unigram-prioren; en tilfældig retning gør ikke](../images/mimir-ignorance-steering.png){ style="display: block; margin: 0 auto;" }

## Mimir bruger næsten ikke prioren, når den regner

Når Mimir løser opgaver, bruger den næsten ingen prior (|λ| ≤ 0,12, mod omkring 0,4 for Llama‑3.2‑3B på
Wikipedia-tekst). Den smule, den bruger, passer til svarets sprog: danske, norske og svenske svar læner sig op ad
den danske prior, og engelske svar op ad den engelske. Mimir er en *Hierarchical Reasoning Model*, der kører de
samme blokke igennem flere gange. Den sprogspecifikke prior dukker først op i allersidste gennemløb; alle de
tidligere gennemløb skubber *væk* fra prioren.

![Prior-vægten gennem Mimirs rekurrens](../images/mimir-ignorance-recurrence.png){ style="display: block; margin: 0 auto;" }

## Hvad vi ikke fandt, og hvad vi fandt i stedet

Artiklen foreslår, at λ kan bruges som advarselslampe for hallucinationer. På matematikopgaver virker det ikke: λ
skelner ikke rigtige fra forkerte svar bedre end tilfældigt (AUROC 0,52), mens modellens almindelige usikkerhed
(entropi) gør det langt bedre (0,73).

Til gengæld afslørede eksperimentet noget, vi kan bruge. **På dansk, norsk og islandsk springer Mimir af og til
ræsonnementet over og skriver svaret med det samme** (i 32 %, 52 % og 35 % af opgaverne). De svar er for det meste
forkerte. Når Mimir regner opgaven igennem, løser den 89 % af de danske og 93 % af de norske, tæt på de 92 % på
engelsk, hvor den aldrig springer ræsonnementet over. Det fortæller os, hvad vi skal rette i næste version af Mimir.

Al kode, alle genereringer og figurer ligger på [GitHub](https://github.com/KennethEnevoldsen/mimirs-geometry-of-ignorance),
og det hele kan genskabes med ét script.
