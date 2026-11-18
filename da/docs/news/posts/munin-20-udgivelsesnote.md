---
draft: false
date: 2026-11-18
slug: munin-20-udgivelsesnote
authors:
  - rasmus
  - torben
tags:
  - Modeludgivelse
---

# Munin 2.0-udgivelsesnote

I dag udgiver vi Munin 2.0, den mest kapable fuldt åbne sprogmodel, der nogensinde er lavet i Danmark. Det er en 120B-model (12B aktive) til dansk og engelsk, bygget til agentisk softwareudvikling, og dens vægte er frie at bruge, også kommercielt. Vi har post-trænet den fra NVIDIAs fortrænede [Nemotron 3 Super Base](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-Base-BF16) på under fem dages endelig træning: 2,5 dages supervised fine-tuning (SFT) på 128 GPU'er på LUMI og 2 dages reinforcement learning (RL) på 128 GPU'er på Gefion, under 0,1 % af den compute, der gik til basismodellen.

<!-- more -->

Munin 2.0 er vores første model trænet med RL. Munin 1.0 brugte kun SFT. I RL lærer modellen ved at forsøge sig med tusindvis af virkelige opgaver, hver i sit eget isolerede computermiljø. At køre disse miljøer i stor skala er en stor del af arbejdet, og vi har bygget vores egen infrastruktur til det. Ved selv at gøre det bliver knowhowen i Danmark for en teknologi, der hurtigt er ved at blive kritisk infrastruktur. Vi udgiver resuméer af træningsdata og den fulde RL-opsætning.

RL løftede SWE-bench Verified fra 58 % til 66 % og Terminal-Bench Lite fra 48 % til 64 %, på niveau med de 66,4 % på SWE-bench Verified, som NVIDIA rapporterer for den lige så store Qwen3.5-122B-A10B. RL indeholdt ingen dansk og kun lidt matematik, men dansk, matematik og naturvidenskab blev alligevel bedre, til niveauet for NVIDIAs egen post-trænede Nemotron 3 Super, på benchmarks uden overlap med vores træningsdata. Uden nogen dedikeret sikkerhedstræning er Munin 2.0 nummer tre af 16 modeller til at undgå skadelige handlinger som agent, kun overgået af to lukkede frontier-modeller. Vi har også kørt en blind sammenligning af dansk kreativ skrivning på tværs af 13 modeller. Munin 2.0 blev nummer tre, og kun en model, der er mere end tre gange så stor, var tydeligt bedre.

Herfra kan vi skalere på flere måder: mere compute, flere og bredere RL-miljøer og bedre basismodeller. Større europæiske indsatser fokuserer på fortræning; post-træning skalerer lettere, og fordi vores opskrift er modeluafhængig, kan vi anvende den på de basismodeller, de indsatser frembringer.

## Modeller

| Model | Hvad det er |
| --- | --- |
| [Munin 2.0](TODO-link) | SFT + RL, BF16-vægte. |
| [Munin 2.0 NVFP4](TODO-link) | Anbefalet på Blackwell-GPU'er, som kører FP4 nativt. |
| [Munin 2.0 SFT](TODO-link) | SFT-checkpointet, Munin 2.0 er trænet fra. Til forskning og videre fine-tuning. |

Alle tre udgives under [NVIDIA Nemotron Open Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-nemotron-open-model-license/), som tillader kommerciel brug. Se modelkortene på Hugging Face for mere information.

NVFP4-versionen bruger samme blandede præcisionslayout som NVIDIAs egen NVFP4-udgivelse af Nemotron 3 Super. Den fylder 80 GB i stedet for 247 GB og kan køre på et enkelt 96 GB RTX PRO 6000 Blackwell.

## Resultater

![Benchmarkresultater for Munin 2.0](../images/munin-20-results.png)

RL var rettet mod softwareudvikling og terminalopgaver, og det er dér, forbedringerne er. Sammenlignet med SFT-checkpointet får Munin 2.0 8 point mere på SWE-bench Verified og 13–16 point mere på Terminal-Bench. Den er tydeligt foran NVIDIAs [Nemotron 3 Super](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16) på SWE-bench Verified og Terminal-Bench Lite og på niveau på Terminal-Bench 2.0 og 2.1.

Dansk, GPQA og AIME var ikke mål for RL, men alle tre blev bedre end SFT-checkpointet, til nogenlunde Nemotron 3 Supers niveau. To benchmarks er ikke med i figuren. På AIME 2025 er scorerne 79,2 for Munin 2.0, 74,2 for SFT-checkpointet og 76,7 for Nemotron 3 Super, og på Humanity's Last Exam 10,6, 9,2 og 11,3.

To forbehold. Det udgivne checkpoint er delvist valgt på baggrund af disse benchmarks, så dets scorer på dem er noget optimistiske. Og Nemotron 3 Super laver få værktøjskald i vores harnesses, så den scorer lavere her end i NVIDIAs egen evaluering, som bruger andre harnesses ([Nemotron 3 Super-modelkort](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16)):

|  | SWE-bench Verified | Terminal-Bench 2.0 |
| --- | ---: | ---: |
| Munin 2.0 (vores harnesses) | 66,2 | 35,8 |
| Qwen3.5-122B-A10B (NVIDIA) | 66,4 | 37,5 |
| Nemotron 3 Super (NVIDIA) | 60,5 | 31,0 |
| gpt-oss-120b (NVIDIA) | 41,9 | 18,7 |

De 95 % bootstrap-intervaller på Munin 2.0's agentiske scorer er ±7 til 9 point. Forbedringen i forhold til SFT-checkpointet er mere sikker end det, fordi begge kørte de samme opgaver. Sammenlignet opgave for opgave i bash-harnesset, på tværs af SWE-bench Verified, Terminal-Bench 2.0 og Terminal-Bench Lite, er Munin 2.0 11 point foran (p < 0,001).

Vores SWE-bench Verified-score er på de første 128 af de 500 opgaver, som alle modeller kørte i alle tre harnesses. På hele sættet i bash-harnesset løser Munin 2.0 65,7 % og Nemotron 3 Super 46,6 %.

Instruktionsfølgning, kontaminering, dansk kreativ skrivning og sammenligningen med DFM Mimir v1.5 behandles under Flere evalueringer.

## Sådan trænede vi den

Munin 2.0 blev trænet i to trin fra Nemotron 3 Super Base, med uændret arkitektur, tokenizer og chatskabelon. Resuméer af træningsdata for begge trin følger EU's AI-forordnings skabelon: [SFT](TODO-link), [RL](TODO-link).

### Supervised fine-tuning

SFT-trinnet var ét gennemløb af 6,8 millioner samtaler, 11 milliarder tokens, i sekvenser på op til 128k tokens. Blandingen dækker chat, ræsonnement med udregnede løsninger, kode, funktionskald og agenttrajektorier med værktøjskald, hvoraf nogle vi selv har genereret. Omkring 8 % af de trænede tokens er på dansk, og yderligere 9 % blander dansk og engelsk. En basismodel fortsætter blot tekst; dette trin lærer den at chatte, ræsonnere og kalde værktøjer. Resultatet er Munin 2.0 SFT.

### Reinforcement learning

I RL-trinnet fungerer modellen som en agent. Den får en opgave, f.eks. en fejlrapport og et repository, og løser den ved at køre kommandoer og redigere filer. Når den stopper, kontrollerer et program resultatet. For en kodeopgave betyder det at køre tests, som agenten aldrig har set. Modellen forsøger hver opgave otte gange, og GRPO forstærker de forsøg, der scorer over gruppens gennemsnit. Alle belønninger kommer fra programmer: der er ingen menneskelig feedback og ingen dommermodel.

Ved det udgivne checkpoint havde modellen gennemarbejdet omkring 119.000 episoder og produceret eller læst 5,6 milliarder tokens. Omkring halvdelen af episoderne er softwareudvikling (Scale-SWE, SWE-smith, OpenSWE) og en fjerdedel er terminalopgaver (Terminal-Lego, TMax). Resten er værktøjsbrug, text-to-SQL, instruktionsfølgning og matematik. Kode- og terminalopgaverne kører i tre agent-harnesses: opencode, pi og et almindeligt bash-værktøj. Ingen af opgaverne er på dansk.

En episode kan løbe op til 300 ture og 300.000 tokens. Modellens kontekst er 128k tokens, så ved lange opgaver komprimerer harnesset samtalen til et resumé, og agenten fortsætter.

Træningsframeworket er Prime Intellects open source-projekt [prime-rl](https://github.com/PrimeIntellect-ai/prime-rl), og den fulde opsætning findes på munin-2.0-grenene i vores [fork](https://github.com/danish-foundation-models/prime-rl/tree/munin-2.0/gefion-rl).

### Sandkasser og infrastruktur

Hver kode- og terminalepisode har brug for sin egen computer at arbejde på. Uden en måde at levere tusindvis af dem findes der ingen RL på agentopgaver. En sandkasse er en frisk container startet fra opgavens image, med repositoryet og dets afhængigheder installeret. Agent-harnesset kører indeni, så al kode, agenten udfører, bliver dér, og når episoden er bedømt, kasseres containeren. Omkring tusind episoder kørte samtidig. Det var sandkasse-tjenesten, ikke GPU'erne, der begrænsede, hvor hurtigt træningen kunne gå.

Vi byggede [sandkasse-tjenesten](https://github.com/rlrs/ucloud-sandboxes) til dette projekt. Den starter og fjerner containere på to mulige backends, [UCloud](https://cloud.sdu.dk) på Syddansk Universitet og Hetzner, bygger opgave-images og kobles til prime-rl. Til denne model kørte sandkasserne på Hetzner. Harnesset i hver sandkasse når modellen via et relay, og for de fleste opgaver er relayet den eneste adresse, en sandkasse kan nå, så agenten har ingen internetadgang.

### Belønninger

En agent, der trænes på testresultater, tager enhver genvej, testene tillader, så hver opgave er sat op til at lukke de oplagte. Git-historik fjernes fra repositories, så agenten ikke kan slå rettelsen op, og hver opgave valideres: referencerettelsen består, og et urørt repository fejler. Før bedømmelsen sættes de originale tests tilbage, hvis agenten har ændret dem. Episoder, der løber tør for budget, får nul i belønning, og ture, der ender i en gentagelsesløkke, udelades fra opdateringen.

Bedømmelsen var stadig støjfyldt. En audit efter det udgivne checkpoint viste, at for SWE-smiths Rust-, C++- og Java-opgaver var 18–42 % af nøjagtige referencerettelser blevet bedømt som fejl, mest fordi testene kørte i den samme sandkasse, som agenten havde bygget i. SWE-smith bruges kun i træning, så det gjorde belønningen mere støjfyldt, men påvirker ikke benchmarkresultaterne. Rettelserne er med i den udgivne opsætning.

### Compute

| Trin | Hardware | Compute |
| --- | --- | --- |
| SFT | 16 LUMI-noder (AMD MI250X), 57,5 timer | ≈ 8,7×10²⁰ FLOP; 1.870 kWh |
| Syntetiske data til SFT | n/a | ≈ 3–4×10¹⁹ FLOP |
| RL (til det udgivne checkpoint) | 16 Gefion-noder (NVIDIA DGX H100), 788 node-timer | ≈ 6×10²⁰ FLOP; ~5–8 MWh (estimeret) |

RL-node-timerne inkluderer mislykkede forsøg.

Samlet brugte DFM omkring 1,5×10²¹ FLOP på Munin 2.0. Mimir v1.5, som DFM trænede fra bunden på 8× B200, tog omkring 1,7×10²², cirka elleve gange så meget. Begge tal medregner kun DFMs egen compute: ikke NVIDIAs fortræning af vores basismodel (anslået 1,8×10²⁴ FLOP), lærermodeller eller de syntetiske datasæt, der deles internt i DFM.

## Flere evalueringer

### Instruktionsfølgning

IFBench er der, hvor Munin 2.0 ligger længst bagud: 49,7 mod 74,0 for Nemotron 3 Super. Hver prompt er en almindelig forespørgsel med en eller to usædvanlige, mekanisk kontrollerede begrænsninger. Forskellen findes allerede i SFT-checkpointet. Instruktionsfølgningsprompts udgjorde omkring 6 % af vores RL-opgaver, mens NVIDIA trænede Nemotron 3 Super med dedikeret RL i instruktionsfølgning.

Munin 2.0 ignorerer sjældent en begrænsning: dens ræsonnement planlægger for den i 160 af dens 163 fejl. Den forsøger og rammer lidt ved siden af. Bedt om f.eks. at lade hver sætning være præcis fem ord længere end den forrige skrev den sætninger på 5, 10, 13, 20 og 25 ord.

### Kontaminering og danske benchmarks

Alle vores træningsdata blev scannet, element for element, mod alle benchmarks, der rapporteres her. De engelske og agentiske benchmarks er rene, bortset fra ét genbrugt AIME 2026-problem og nogle IFBench-baseprompts fra offentlige chatdata (uden deres begrænsninger).

SFT-dataene indeholder træningssplittene fra 24 danske EuroEval-opgaver. De indeholder også testelementer fra 10 af de 27 datasæt, vi kører, fordi nogle af EuroEvals trænings- og testsplit overlapper, og flere opgaver deler kilder. Den danske score, vi rapporterer, er gennemsnittet over de 17 rene datasæt. Med alle 27 ville både vores score og vores forspring til Nemotron 3 Super være højere.

Scanningen dækker kun det, vi tilføjede i SFT og RL. NVIDIAs fortræning af basismodellen, som Munin 2.0 arver, og dens post-træning af Nemotron 3 Super er ikke scannet, så "ren" betyder her ren for vores egne træningsdata.

Københavns Universitets [Danish Semantic Reasoning Benchmark](https://github.com/kuhumcst/danish-semantic-reasoning-benchmark) (beta) tester ordbetydning og inferens. Som reference kørte vi Gemma 4 31B, som er meget brugt som en af de bedste modeller til dansk, i samme harness. På de elementer, der er rene for vores træningsdata, scorer Munin 2.0 80,1 og Gemma 4 31B 80,5.

### Dansk kreativ skrivning

Den danske skrivekonkurrence bruger 24 prompts fra [dfm-evals](https://github.com/danish-foundation-models/dfm-evals), tre svar pr. prompt, med ræsonnement slået fra (gpt-oss-120b og Embla 1 kan ikke slå det fra, så kun deres endelige svar blev bedømt). Der var to dommere: Gemma 4 31B, som sammenlignede svar parvis, og Claude Sonnet 5.5, som rangordnede alle tretten svar til hver prompt. Ingen af dem vidste, hvilken model der havde skrevet hvad. De to dommere er enige om 86 % af parrene. Tabellen viser andelen af modstandere, hver model slog.

| Model | Claude Sonnet 5.5 | Gemma 4 31B |
| --- | ---: | ---: |
| Qwen3.5-397B-A17B | 0,84 | 0,86 |
| Nemotron 3 Super | 0,77 | 0,81 |
| **Munin 2.0** | 0,75 | 0,75 |
| Gemma 4 31B | 0,73 | 0,68 |
| Gemma 4 26B-A4B | 0,72 | 0,70 |
| Munin 2.0 SFT | 0,71 | 0,74 |
| Gemma 3 27B | 0,55 | 0,50 |
| Munin 1.0 Qwen 9B | 0,43 | 0,42 |
| gpt-oss-120b | 0,36 | 0,41 |
| Munin 1.0 Ministral 8B | 0,19 | 0,26 |
| Munin 1.0 Apertus 8B | 0,17 | 0,16 |
| DFM Mimir v1.5 | 0,15 | 0,17 |
| Embla 1 | 0,11 | 0,05 |

Qwen3.5-397B-A17B er nummer ét hos begge dommere og slår Munin 2.0 i omkring to ud af tre direkte dueller. Dens danske er godt, men den smutter en gang imellem: i ét svar skrev den, at en bus "ikke减速erede", hvor det kinesiske ord for "sænke farten" får en dansk verbalendelse.

Nemotron 3 Super, Munin 2.0, de to Gemma 4-modeller og Munin 2.0 SFT ligger tæt sammen. I direkte dueller sætter Sonnet Munin 2.0 på niveau med Nemotron 3 Super; Gemma sætter Nemotron 3 Super foran. Gemma 4 31B favoriserer ikke sig selv: den rangerer sine egne svar som nummer seks. RL ændrede næsten ikke på, hvordan Munin 2.0 skriver.

Munin 2.0 slår hver Munin 1.0-model i omkring ni ud af ti direkte dueller eller flere. I bunden er 8B Munin 1.0-modellerne, Mimir v1.5 og [Embla 1](https://huggingface.co/sevren-ai/Embla1-bf16). Syv af Mimirs 72 svar ender i en gentagelsesløkke, og Embla 1 besvarer otte af de danske prompts på engelsk og én på norsk.

### Sammenligning med DFM Mimir v1.5

![Munin 2.0 sammenlignet med DFM Mimir v1.5](../images/munin-20-mimir-comparison.png)

[DFM Mimir v1.5](https://huggingface.co/danish-foundation-models/DFM-Mimir-v1.5) er vores anden nylige model, og de to har forskellige formål. Mimir er en 1,8B-model, der genbruger sine lag flere gange pr. token, trænet fra bunden på DFMs egne datablandinger og udgivet under Apache 2.0. Munin 2.0 er en 120B-model bygget på en fortrænet basis. Mimir køres uden ræsonnement og bruger omkring en tredjedel af Munin 2.0's compute pr. token.

Sammenligningen dækker de 11 danske opgaver, begge modeller rapporterer. Mimirs scorer er dens publicerede (EuroEvals valideringssplit, plus Mimirs evalueringsharness til DaLA og WMT24++). Den samme kontamineringsscanning blev kørt over begge modellers træningsdata.

Mimir fører på tre opgaver, og dens træningsdata indeholder de fleste af testelementerne for alle tre: 95 % af MultiWikiQA-da-spørgsmålene med svar og næsten hver eneste grammatiske DaLA- og ScaLA-sætning. DaLA- og ScaLA-sætningerne kommer fra DFMs eget danske Dynaword-korpus, som inkluderer det treebank, disse benchmarks er bygget på. Munin 2.0 har et mindre overlap på DaLA og ScaLA (21 %), så begge opgaver er udeladt af Munin 2.0's danske score.

Munin 2.0 fører på to opgaver mere, hvor kun én model har set testelementer. På DANSK NER fører den, selvom Mimirs træningsdata indeholder 28 % af testsætningerne. På statsborgerskabstestene tæller dens føring ikke, fordi Munin 2.0's træningssplit gentager 76 % af testen.

På de seks opgaver, ingen af modellerne har set, fører Munin 2.0 på tre og er på niveau på tre, med et gennemsnit på 64,0 mod Mimirs 59,0. Disse seks opgaver måler dog ikke dansk færdighed rent. Nogle ligger tæt på loftet, og begge modeller trænede på relaterede data: Munin 2.0 på træningssplittene fra idiom-, HellaSwag-da-, sentiment- og resumeopgaverne, og Mimir på langt flere resumédata, store mængder instruktionsfølgnings-, oversættelses- og engelske sentimentdata og nogle af de engelske HellaSwag-elementer. Så EuroEval kan ikke afgøre denne sammenligning.

## Sikkerhed

Munin 2.0 havde ingen dedikeret sikkerhedstræning. Efter RL foretager den sjældnere skadelige handlinger som agent, men handler oftere imod sin operatør, når den bliver truet.

I SABERs 716 agentopgaver i levende shell-arbejdsområder foretager Munin 2.0 sjældnere skadelige handlinger end SFT-checkpointet og Nemotron 3 Super og er nummer tre af de 16 modeller, hvis resultater SABERs forfattere har publiceret, efter Claude Opus 4.6 og GPT-5.4. Forbedringen holder på tværs af scenarier, inklusive ondsindede instruktioner plantet i filer eller værktøjsoutput.

![SABER-resultater for agentsikkerhed](../images/munin-20-safety-saber.png)

Forværringen er i Agentic Misalignment, hvor modellen får at vide, at den vil blive erstattet, eller at dens mål vil blive tilsidesat. Her afpresser Munin 2.0 og lækker fortrolige data oftere end SFT-checkpointet. Nemotron 3 Super lækker endnu oftere.

![Resultater for Agentic Misalignment](../images/munin-20-safety-agentic-misalignment.png)

Munin 2.0's viden om cybersikkerhed steg også under RL, inklusive farlig viden (WMDP-cyber). Hvis du bruger Munin 2.0 som autonom agent, bør du tilføje dine egne sikkerhedsforanstaltninger.

## Hvad er det næste

Dette var vores første RL-kørsel i denne skala, og pipelinen kan stadig optimeres markant. Vi tilføjer flere softwareudviklings- og terminalopgaver, miljøer langt uden for software og danske opgaver med verificerbare belønninger. På SFT-siden har modellen brug for dedikerede instruktionsfølgningsdata, længere agenttrajektorier og mere dansk. Sideløbende vil vi bygge danske evalueringer, der holdes ude af træningen.

Vi hører gerne feedback på modellen, evalueringerne og på, hvor vi bør tage det videre.

## Bidragydere

Vi angiver bidrag efter [Contributor Roles Taxonomy (CRediT)](https://credit.niso.org).

**Rasmus Larsen**: Konceptualisering, metodologi, software, undersøgelse, formel analyse, validering, datakuratering, visualisering, skrivning – oprindeligt udkast

**Yderligere bidragydere**

Oliver Kinch: Software, datakuratering

Torben Blach: Projektadministration, skrivning – gennemgang og redigering

Gianluca Barmina: Ressourcer

Kenneth Enevoldsen: Ressourcer

Vladimir Salnikov: Ressourcer

Peter Schneider-Kamp: Ressourcer

Dan Saattrup Smart: Ressourcer

## Anerkendelser

Arbejdet blev støttet af Danish Foundation Models-projektet, finansieret af den danske regering. Den superviserede finjustering kørte på LUMI under DeiC-bevillingen DeiC-SDU-N5-2026185.
