---
draft: false
date: 2026-06-11
slug: munin-10-udgivelsesnote
authors:
  - rasmus
  - torben
tags:
  - Modeludgivelse
---

# Munin 1.0-udgivelsesnote

I dag udgiver Danish Foundation Models [Munin 1.0-familien af sprogmodeller](https://huggingface.co/collections/danish-foundation-models/munin-10), som er post-trænet oven på nogle af de stærkeste åbne modeller i deres klasse. Modellerne er trænet på en kombination af eksisterende åbne og nyudviklede datasæt.

<!-- more -->

## Modeller og resultater

Munin 1.0-familien er post-trænet på modeller med åbne vægte fra [Swiss AI](https://huggingface.co/swiss-ai), [Mistral](https://huggingface.co/mistralai) og [Qwen](https://huggingface.co/Qwen). Alle basismodellerne er oprindeligt udgivet under [Apache 2.0-licensen](https://www.apache.org/licenses/LICENSE-2.0), og vores modeller har samme licens.

| Udvikler | Basismodel | Munin-model | Land | Åbenhed |
| --- | --- | --- | --- | --- |
| Swiss AI | [`swiss-ai/Apertus-8B-2509`](https://huggingface.co/swiss-ai/Apertus-8B-2509) | [`munin-apertus-8b`](https://huggingface.co/danish-foundation-models/munin-apertus-8b) | Europa/Schweiz | Fuldt åben |
| Mistral | [`mistralai/Ministral-3-8B-Base-2512`](https://huggingface.co/mistralai/Ministral-3-8B-Base-2512) | [`munin-ministral3-8B`](https://huggingface.co/danish-foundation-models/munin-ministral3-8B) | Europa/Frankrig | Åbne vægte |
| Qwen 3.5 9B | [`Qwen/Qwen3.5-9B-Base`](https://huggingface.co/Qwen/Qwen3.5-9B-Base) | [`munin-qwen3.5-9B`](https://huggingface.co/danish-foundation-models/munin-qwen3.5-9B) | Kina | Åbne vægte |

Munin 1.0 er en tekstbaseret post-træningsudgivelse, så sammenligningerne nedenfor fokuserer på tekstbenchmarks. Nogle af de oprindelige instruktionsmodeller har billede-til-tekst eller andre multimodale evner, men de evner understøttes ikke af de modeller, der udgives her.

Vi evaluerer Munin-modellerne mod de instruktions-tunede modeller udgivet af de oprindelige modeludviklere. Da Munin er trænet fra de samme basismodeller, er det en direkte sammenligning af to uafhængige post-træningsindsatser: den oprindelige udviklers post-træning og vores danskfokuserede Munin-træning.

De aggregerede resultater nedenfor er uvægtede gennemsnit på tværs af evalueringer i hver opgavegruppe. Scores er procenter, og standardfejl er procentpoint. Blå markerer den bedste Original/Munin-score inden for hver modelfamilie, eller begge hvis de er lige gode inden for usikkerheden. Fed skrift markerer scores, der ikke er signifikant under den bedste score i rækken. Se de [fulde benchmarkresultater](/news/results/munin-10-full-results.html) for de enkelte evalueringer bag hvert aggregat.

<div class="md-typeset__table dfm-eval-table-wrap">
  <table class="dfm-eval-table">
    <caption>Aggregerede opgavescores</caption>
    <thead>
      <tr>
        <th scope="col" rowspan="2">Suite</th>
        <th scope="col" rowspan="2">Opgave</th>
        <th scope="col" rowspan="2">Metrik</th>
        <th scope="col" colspan="2">Apertus 8B</th>
        <th scope="col" colspan="2">Ministral 8B</th>
        <th scope="col" colspan="2">Qwen 9B</th>
      </tr>
      <tr>
        <th scope="col">Original</th>
        <th scope="col">Munin</th>
        <th scope="col">Original</th>
        <th scope="col">Munin</th>
        <th scope="col">Original</th>
        <th scope="col">Munin</th>
      </tr>
    </thead>
    <tbody>
      <tr class="dfm-suite-start dfm-suite-danish hl-apertus-original hl-ministral-original hl-ministral-munin hl-qwen-original"><td>Dansk</td><td>Common-sense Reasoning</td><td>MCC</td><td>33,1 ± 0,9</td><td>29,4 ± 1,3</td><td>52,4 ± 1,2</td><td>50,2 ± 1,3</td><td><strong>64,6 ± 0,7</strong></td><td>62,2 ± 0,9</td></tr>
      <tr class="dfm-suite-danish hl-apertus-original hl-apertus-munin hl-ministral-original hl-ministral-munin hl-qwen-original hl-qwen-munin"><td>Dansk</td><td>Grammatical Error Detection</td><td>micro-F1</td><td><strong>18,0 ± 1,3</strong></td><td><strong>17,4 ± 1,1</strong></td><td><strong>21,7 ± 2,0</strong></td><td><strong>17,7 ± 0,7</strong></td><td><strong>20,4 ± 1,2</strong></td><td><strong>20,7 ± 1,1</strong></td></tr>
      <tr class="dfm-suite-danish hl-apertus-original hl-ministral-munin hl-qwen-original"><td>Dansk</td><td>Instruction-following</td><td>Accuracy</td><td>69,0 ± 1,1</td><td>51,4 ± 1,4</td><td>66,7 ± 1,3</td><td>74,4 ± 0,9</td><td><strong>81,6 ± 0,8</strong></td><td>77,9 ± 0,9</td></tr>
      <tr class="dfm-suite-danish hl-apertus-munin hl-ministral-original hl-qwen-munin"><td>Dansk</td><td>Knowledge</td><td>MCC</td><td>58,9 ± 0,7</td><td>62,3 ± 0,7</td><td>73,6 ± 0,5</td><td>68,5 ± 0,6</td><td>76,0 ± 0,5</td><td><strong>77,6 ± 0,5</strong></td></tr>
      <tr class="dfm-suite-danish hl-apertus-original hl-apertus-munin hl-ministral-original hl-qwen-original hl-qwen-munin"><td>Dansk</td><td>Linguistic Acceptability</td><td>MCC</td><td>33,0 ± 1,2</td><td>29,3 ± 2,4</td><td>43,4 ± 1,9</td><td>18,9 ± 3,1</td><td><strong>49,2 ± 1,7</strong></td><td><strong>52,2 ± 1,3</strong></td></tr>
      <tr class="dfm-suite-danish hl-apertus-original hl-apertus-munin hl-ministral-original hl-ministral-munin hl-qwen-original hl-qwen-munin"><td>Dansk</td><td>Multiple-choice Reading Comprehension</td><td>MCC</td><td>67,1 ± 1,0</td><td>66,0 ± 2,0</td><td><strong>85,9 ± 1,4</strong></td><td><strong>84,4 ± 1,1</strong></td><td><strong>87,2 ± 1,2</strong></td><td><strong>87,3 ± 1,3</strong></td></tr>
      <tr class="dfm-suite-danish hl-apertus-original hl-apertus-munin hl-ministral-original hl-qwen-original hl-qwen-munin"><td>Dansk</td><td>Named Entity Recognition</td><td>micro-F1</td><td>49,3 ± 1,4</td><td>47,6 ± 1,3</td><td>61,1 ± 1,0</td><td>51,4 ± 1,8</td><td><strong>69,1 ± 1,2</strong></td><td><strong>69,6 ± 1,2</strong></td></tr>
      <tr class="dfm-suite-danish hl-apertus-original hl-apertus-munin hl-ministral-munin hl-qwen-munin"><td>Dansk</td><td>Natural Language Inference</td><td>MCC</td><td>48,8 ± 2,3</td><td>52,1 ± 2,6</td><td>25,8 ± 1,6</td><td>58,2 ± 2,2</td><td>53,8 ± 1,9</td><td><strong>65,6 ± 2,0</strong></td></tr>
      <tr class="dfm-suite-danish hl-apertus-original hl-apertus-munin hl-ministral-original hl-ministral-munin hl-qwen-original hl-qwen-munin"><td>Dansk</td><td>Reading Comprehension</td><td>F1</td><td><strong>70,8 ± 0,5</strong></td><td>69,4 ± 0,6</td><td>69,7 ± 0,7</td><td><strong>71,2 ± 0,8</strong></td><td><strong>70,8 ± 0,6</strong></td><td><strong>72,0 ± 0,7</strong></td></tr>
      <tr class="dfm-suite-danish hl-apertus-original hl-ministral-original hl-ministral-munin hl-qwen-original hl-qwen-munin"><td>Dansk</td><td>Sentiment Classification</td><td>MCC</td><td>57,9 ± 1,0</td><td>54,3 ± 1,1</td><td>60,4 ± 1,0</td><td>59,6 ± 1,4</td><td><strong>64,9 ± 0,9</strong></td><td><strong>64,7 ± 1,0</strong></td></tr>
      <tr class="dfm-suite-danish hl-apertus-original hl-ministral-munin hl-qwen-original hl-qwen-munin"><td>Dansk</td><td>Summarization</td><td>chrF++</td><td><strong>37,6 ± 0,2</strong></td><td>36,9 ± 0,2</td><td>35,1 ± 0,3</td><td>37,0 ± 0,2</td><td>36,5 ± 0,3</td><td><strong>36,7 ± 0,4</strong></td></tr>
      <tr class="dfm-suite-danish hl-apertus-original hl-apertus-munin hl-ministral-original hl-ministral-munin hl-qwen-original hl-qwen-munin"><td>Dansk</td><td>Word-in-Context</td><td>MCC</td><td>11,8 ± 2,2</td><td>8,7 ± 3,5</td><td>29,9 ± 1,7</td><td>23,3 ± 3,2</td><td><strong>44,6 ± 2,1</strong></td><td><strong>40,1 ± 3,5</strong></td></tr>
      <tr class="dfm-suite-start dfm-suite-english hl-apertus-original hl-ministral-original hl-qwen-original"><td>Engelsk</td><td>Common-sense Reasoning</td><td>Accuracy</td><td>58,7 ± 0,5</td><td>23,2 ± 0,4</td><td>73,1 ± 0,4</td><td>59,6 ± 0,5</td><td><strong>90,0 ± 0,3</strong></td><td>85,7 ± 0,3</td></tr>
      <tr class="dfm-suite-english hl-apertus-original hl-ministral-original hl-ministral-munin hl-qwen-original"><td>Engelsk</td><td>Instruction-following</td><td>Accuracy</td><td>73,3 ± 1,9</td><td>54,7 ± 2,0</td><td>70,4 ± 1,8</td><td>69,8 ± 1,9</td><td><strong>89,6 ± 1,5</strong></td><td>78,6 ± 1,8</td></tr>
      <tr class="dfm-suite-english hl-apertus-original hl-ministral-original hl-qwen-munin"><td>Engelsk</td><td>Knowledge</td><td>Accuracy</td><td>50,3 ± 0,5</td><td>41,9 ± 0,5</td><td><strong>81,7 ± 0,3</strong></td><td>73,0 ± 0,3</td><td>79,2 ± 0,2</td><td><strong>82,4 ± 0,2</strong></td></tr>
      <tr class="dfm-suite-english hl-apertus-original hl-apertus-munin hl-ministral-original hl-ministral-munin hl-qwen-original"><td>Engelsk</td><td>Long-context</td><td>Accuracy</td><td>34,6 ± 2,1</td><td>35,8 ± 2,1</td><td>51,4 ± 2,2</td><td>49,4 ± 2,2</td><td><strong>67,2 ± 2,1</strong></td><td>54,6 ± 2,2</td></tr>
      <tr class="dfm-suite-english hl-apertus-original hl-ministral-original hl-qwen-original"><td>Engelsk</td><td>Math</td><td>Accuracy</td><td>68,1 ± 1,3</td><td>56,7 ± 1,4</td><td>92,2 ± 0,7</td><td>82,3 ± 1,1</td><td><strong>94,8 ± 0,6</strong></td><td>92,2 ± 0,7</td></tr>
      <tr class="dfm-suite-english hl-apertus-original hl-apertus-munin hl-ministral-original hl-ministral-munin hl-qwen-original hl-qwen-munin"><td>Engelsk</td><td>Truthfulness</td><td>Accuracy</td><td>16,8 ± 1,3</td><td>15,7 ± 1,3</td><td>64,7 ± 1,7</td><td>63,3 ± 1,7</td><td><strong>78,1 ± 1,4</strong></td><td><strong>74,2 ± 1,5</strong></td></tr>
      <tr class="dfm-suite-start dfm-suite-agentic hl-apertus-original hl-ministral-original hl-qwen-original"><td>Agentisk</td><td>Code</td><td>pass@1</td><td>46,8 ± 2,5</td><td>39,2 ± 2,4</td><td>75,0 ± 2,1</td><td>49,2 ± 2,3</td><td><strong>83,0 ± 1,8</strong></td><td>77,2 ± 2,1</td></tr>
      <tr class="dfm-suite-agentic hl-apertus-original hl-ministral-original hl-qwen-original"><td>Agentisk</td><td>Tool Calling</td><td>Accuracy</td><td>52,4 ± 0,8</td><td>43,1 ± 0,8</td><td>75,0 ± 0,7</td><td>49,2 ± 0,8</td><td><strong>79,4 ± 0,6</strong></td><td>75,8 ± 0,7</td></tr>
    </tbody>
  </table>
</div>

??? info "Hvad indgår i hvert aggregat?"

    De danske opgavegrupper følger EuroEvals danske opgavetaksonomi. Links peger på artikler, hvor de findes, ellers på offentlige datasæt, upstream-repositorier eller de EuroEval-scripts, der bruges til at konstruere benchmarkdatasættet. For flere entries, der ender på `-da`, går linket til artiklen for det oprindelige benchmark, fordi den evaluerede ressource er en dansk oversat eller på anden måde lokaliseret variant. Nogle danske varianter, herunder `ifeval-da`, er tilpasninger snarere end simple direkte oversættelser.

    | Suite | Aggregeret opgave | Benchmarks |
    | --- | --- | --- |
    | Dansk | Common-sense Reasoning | [`goldenswag-da`](https://arxiv.org/abs/2504.07825), [`hellaswag-da`](https://arxiv.org/abs/1905.07830), [`winogrande-da`](https://arxiv.org/abs/1907.10641) |
    | Dansk | Grammatical Error Detection | [`gerlangmod-da`](https://github.com/noahmanu/gerlangmod) |
    | Dansk | Instruction-following | [`ifeval-da`](https://arxiv.org/abs/2311.07911) |
    | Dansk | Knowledge | [`arc-da`](https://arxiv.org/abs/1803.05457), [`dameta`](https://github.com/kuhumcst/danish-semantic-reasoning-benchmark), [`danish-citizen-tests`](https://huggingface.co/datasets/alexandrainst/danish-citizen-tests), [`danske-talemaader`](https://huggingface.co/datasets/Juunge/danske-talemaader), [`mmlu-da`](https://arxiv.org/abs/2009.03300) |
    | Dansk | Linguistic Acceptability | [`dala`](https://arxiv.org/abs/2512.04799), [`scala-da`](https://arxiv.org/abs/2304.00906) |
    | Dansk | Multiple-choice Reading Comprehension | [`belebele-da`](https://arxiv.org/abs/2308.16884) |
    | Dansk | Named Entity Recognition | [`dane`](https://arxiv.org/abs/2107.05295), [`dansk`](https://arxiv.org/abs/2402.18209) |
    | Dansk | Natural Language Inference | [`danish-entailment`](https://github.com/kuhumcst/danish-semantic-reasoning-benchmark), [`danish-lexical-inference`](https://github.com/kuhumcst/danish-semantic-reasoning-benchmark) |
    | Dansk | Reading Comprehension | [`multi-wiki-qa-da`](https://arxiv.org/abs/2509.04111), [`scandiqa-da`](https://arxiv.org/abs/2304.00906) |
    | Dansk | Sentiment Classification | [`angry-tweets`](https://huggingface.co/datasets/DDSC/angry-tweets), [`danish-sentiment-in-context`](https://github.com/kuhumcst/danish-semantic-reasoning-benchmark) |
    | Dansk | Summarization | [`nordjylland-news`](https://huggingface.co/datasets/alexandrainst/nordjylland-news-summarization) |
    | Dansk | Word-in-Context | [`danwic`](https://github.com/kuhumcst/danish-semantic-reasoning-benchmark) |
    | Engelsk | Knowledge | [`ARC-C`](https://arxiv.org/abs/1803.05457), [`ARC-E`](https://arxiv.org/abs/1803.05457), [`MMLU`](https://arxiv.org/abs/2009.03300), [`MMLU-Pro`](https://arxiv.org/abs/2406.01574) |
    | Engelsk | Other task groups | [`HellaSwag`](https://arxiv.org/abs/1905.07830), [`IFEval`](https://arxiv.org/abs/2311.07911), [`RULER 32k`](https://arxiv.org/abs/2404.06654), [`GSM8K`](https://arxiv.org/abs/2110.14168), [`TruthfulQA`](https://arxiv.org/abs/2109.07958) |
    | Agentisk | Code and Tool Calling | [`HumanEval`](https://arxiv.org/abs/2107.03374), [`MBPP p@1`](https://arxiv.org/abs/2108.07732), [`BFCL`](https://arxiv.org/abs/2407.07770) |

Hovedresultatet er, at Munin er stærkt konkurrencedygtig på de danske evalueringer, og at vores post-trænede modeller i flere opgavegrupper matcher eller forbedrer de oprindelige instruktionsmodeller. De stærkeste resultater er på dansk Knowledge, Reading Comprehension, Summarization og Natural Language Inference, hvor nogle Munin-modeller ligger foran selv med usikkerheden taget i betragtning. Dermed kan det ses at post-træningen flytter modellerne mod stærkere dansk performance, samtidig med at de bevarer en brugbar generel kapabilitetsprofil.

Resultaterne på engelsk og agentiske opgaver er mere blandede. De oprindelige instruktionsmodeller er generelt stærkere på kode, værktøjskald og flere engelske benchmarks, hvilket afspejler, at Munin 1.0 nu primært fokuserer på danske tekstkapabiliteter. De forskelle er vigtige, fordi de peger direkte på næste fase af arbejdet: at bevare de danske forbedringer, samtidig med at der investeres mere målrettet i reasoning, multilingvalitet og agentiske kapabiliteter.

Vi kørte også en fokuseret dansk turnering i kreativ skrivning på tværs af 360 bedømte kampe, vurderet af Qwen3.5-397B-A17B. Vi valgte denne dommer på grund af dens stærke dansksproglige evner.

Turneringen er ikke et bredt benchmark for modelkvalitet, men den er nyttig, fordi kreativ skrivning er en dansk opgave med højt signal: Den tester sproglig flydendehed, register, kohærens, og om modellen kan producere tekst, der føles naturlig frem for blot korrekt. [Munin Qwen 9B](https://huggingface.co/danish-foundation-models/munin-qwen3.5-9B) skiller sig tydeligt ud fra resten af feltet med en 96-9 rekord, mens [Munin Apertus 8B](https://huggingface.co/danish-foundation-models/munin-apertus-8b) placerer sig som nummer to, og [Munin Ministral 8B](https://huggingface.co/danish-foundation-models/munin-ministral3-8B) også slår sin oprindelige modpart.

<div class="md-typeset__table">
  <table class="dfm-tournament-table">
    <caption>Rangering i dansk kreativ skriveturnering; V-T er samlet vundet-tabt</caption>
    <thead>
      <tr>
        <th scope="col">Placering</th>
        <th scope="col">Model</th>
        <th scope="col">V-T</th>
      </tr>
    </thead>
    <tbody>
      <tr class="dfm-model-munin">
        <td>1</td>
        <td><strong><a href="https://huggingface.co/danish-foundation-models/munin-qwen3.5-9B">Munin Qwen 9B</a></strong></td>
        <td>96-9</td>
      </tr>
      <tr class="dfm-model-munin">
        <td>2</td>
        <td><strong><a href="https://huggingface.co/danish-foundation-models/munin-apertus-8b">Munin Apertus 8B</a></strong></td>
        <td>56-45</td>
      </tr>
      <tr>
        <td>3</td>
        <td>Original Qwen 9B</td>
        <td>43-53</td>
      </tr>
      <tr class="dfm-model-munin">
        <td>4</td>
        <td><strong><a href="https://huggingface.co/danish-foundation-models/munin-ministral3-8B">Munin Ministral 8B</a></strong></td>
        <td>43-54</td>
      </tr>
      <tr>
        <td>5</td>
        <td>Original Apertus 8B</td>
        <td>30-65</td>
      </tr>
      <tr>
        <td>6</td>
        <td>Original Ministral 8B</td>
        <td>26-68</td>
      </tr>
    </tbody>
  </table>
</div>

## Bidragydere

Rasmus Larsen ledte træningen, udførte eksperimenter, byggede syntetiske datasæt og benchmarks, og skrev udkastet til udgivelsesannonceringen.

Oliver Kinch byggede syntetiske datasæt og benchmarks.

Andreas Holm bidrog til eksperimenter.

Vladimir Salnikov og Jacob Nielsen bidrog til datasæt.

Dan Saattrup Smart udviklede benchmarks og ledte integrationen i EuroEval.

Torben Blach bidrog med projektledelse og koordinering.

## Anerkendelser

Arbejdet blev støttet af Danish Foundation Models-projektet, finansieret af den danske regering. Arbejdet blev delvist støttet af DeiC National HPC (grant agreement DeiC-SDU-N5-2025162).
