---
draft: false
date: 2024-01-11
tags:
  - Modeludgivelse
---

# Udgivelse af Munin 7B Alpha — en dansk sprogmodel

Vi er glade for at kunne annoncere udgivelsen af [den første model fra Danish Foundation Models-projektet, kaldet Munin 7B Alpha](https://huggingface.co/danish-foundation-models/munin-7b-alpha). Modellen repræsenterer begyndelsen af vores forskning i danske store sprogmodeller (LLM'er) og anvender [kontinuerlig forhåndstræning](https://arxiv.org/abs/2308.04014) baseret på den allerede forhåndstrænede [Mistral-7b-v0.1](https://huggingface.co/mistralai/Mistral-7B-v0.1). Den er trænet på datasættet [Danish Gigaword](https://gigaword.dk/), som har været afgørende for træningen af en lang række danske BERT-modeller.

<!-- more -->

Modellen er trænet i én epoke over datasættet og ender med et tab på 1,27 på Danish Gigaword. Se modellens træningslog [her](https://api.wandb.ai/links/rlrs/wbqovk26).

Denne udgivelse understreger vores forpligtelse til åbenhed om vores arbejde og de udfordringer, vi møder. Vi vil tydeligt bemærke, at vi forventer, at modellen vil præstere suboptimalt i mange — om ikke de fleste — anvendelser. Vores evalueringer på de begrænsede generative danske opgaver, der er tilgængelige for os, har vist, at vores nuværende træningstilgang kan påvirke præstationen negativt på disse downstream-opgaver, selv sammenlignet med den originale Mistral-model.

| Modelnavn                                   | Samlet score    | Dansk score   | Norsk score     | Svensk score  |
|---------------------------------------------|-----------------|---------------|-----------------|---------------|
| gpt-3.5-turbo-0613                          | 58,52 ± 2,42    | 56,72 ± 2,44  | 57,31 ± 2,37    | 61,54 ± 2,46  |
| mistralai/Mistral-7B-v0.1                   | 40,30 ± 2,15    | 39,60 ± 1,94  | 35,98 ± 2,54    | 45,31 ± 1,96  |
| **danish-foundation-models/munin-7b-alpha** | 37,50 ± 2,49    | 39,56 ± 2,70  | 30,82 ± 2,69    | 42,13 ± 2,07  |
| AI-Sweden-Models/gpt-sw3-6.7b-v2           | 26,67 ± 2,30    | 23,65 ± 2,02  | 24,28 ± 2,74    | 32,08 ± 2,13  |
| mhenrichsen/danskgpt-tiny                  | 16,87 ± 3,05    | 16,66 ± 2,18  | 15,16 ± 2,64    | 18,80 ± 4,35  |

Se [det fulde ScandEval-leaderboard](https://scandeval.com) for en opdateret sammenligning. På trods af disse udfordringer håber vi, at vores åbne tilgang tilskynder fællesskabet til at samarbejde med os om at bygge den bedst mulige danske LLM. Selvom den nuværende version af modellen måske endnu ikke er et praktisk værktøj til dansk NLP, mener vi, at det er værdifuldt at dele vores resultater. Et kritisk behov er identificeret: adgang til et markant større korpus af dansk tekstdata og en juridisk ramme, der pålideligt tillader træning og udgivelse af åbne modeller, herunder til kommerciel brug.

Hos Danish Foundation Models arbejder vi aktivt på at opnå juridisk adgang til omfattende danske tekstdata og udforsker alle muligheder for at udgive modeller under den mest åbne licens muligt. Vi har allerede indgået aftaler, der giver os adgang til adskillige store danske datasæt, og vi planlægger at inkludere disse i vores træningsproces inden for den nærmeste fremtid.

Sammenfattende er Munin 7B Alpha et lille skridt fremad. Det signalerer vores forpligtelse til at fremme dansk NLP og anerkender det omfattende arbejde, der stadig ligger foran os. Ved at dele denne model ønsker vi at fremme samarbejde i fællesskabet. Modellen er nu tilgængelig til download og eksperimentering, og vi ser frem til jeres indsigter og diskussioner om, hvordan vi kan komme videre.

Udviklingen af denne model, og Danish Foundation Models-projektet generelt, støttes generøst af:

- [Danish e-infrastructure Consortium](https://www.deic.dk/)
- [Forsvarets Materieltjeneste](https://www.fmi.dk/)
- Uddannelses- og Forskningsministeriet under [resultatkontrakt om Digital Sikkerhed, Tillid og Dataetik](https://bedreinnovation.dk/)
