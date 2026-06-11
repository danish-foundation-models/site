---
draft: false
date: 2026-06-11
slug: munin-10-release-note
tags:
  - Model Release
---

# Munin 1.0 release note

<p class="dfm-post-byline"><strong>Authors:</strong> Rasmus Larsen, Torben Blach – Alexandra Instituttet A/S</p>

Today, Danish Foundation Models releases the [Munin 1.0 family of language models](https://huggingface.co/collections/danish-foundation-models/munin-10), post-trained on top of several best-in-class open models. These models are trained using a combination of existing open and newly developed datasets.

<!-- more -->

## Models and results

The Munin 1.0 family of models are post-trained on open-weights models from [Swiss AI](https://huggingface.co/swiss-ai), [Mistral](https://huggingface.co/mistralai), and [Qwen](https://huggingface.co/Qwen). All models were originally released under the [Apache 2.0 license](https://www.apache.org/licenses/LICENSE-2.0), and our models have the same license.

| Developer | Base model | Munin model | Country | Openness |
| --- | --- | --- | --- | --- |
| Swiss AI | [`swiss-ai/Apertus-8B-2509`](https://huggingface.co/swiss-ai/Apertus-8B-2509) | [`munin-apertus-8b`](https://huggingface.co/danish-foundation-models/munin-apertus-8b) | Europe/Switzerland | Fully open |
| Mistral | [`mistralai/Ministral-3-8B-Base-2512`](https://huggingface.co/mistralai/Ministral-3-8B-Base-2512) | [`munin-ministral3-8B`](https://huggingface.co/danish-foundation-models/munin-ministral3-8B) | Europe/France | Open weights |
| Qwen 3.5 9B | [`Qwen/Qwen3.5-9B-Base`](https://huggingface.co/Qwen/Qwen3.5-9B-Base) | [`munin-qwen3.5-9B`](https://huggingface.co/danish-foundation-models/munin-qwen3.5-9B) | China | Open weights |

Munin 1.0 is a text-only post-training release, so the comparisons below focus on text benchmarks. Some upstream instruct models advertise image-to-text or other multimodal capabilities, but those capabilities are not supported by the models released here.

We evaluated the Munin models against the instruction-tuned models released by the original model developers. Since Munin is trained from the same base models, this is an apples-to-apples comparison of two independent post-training efforts: the original developer's post-training and our Danish-focused Munin training.

The aggregate scores below are unweighted means across evaluations in each task group. Scores are percentages, and standard errors are percentage points. Blue marks the better Original/Munin score within each model family, or both if they are tied within uncertainty. Bold scores are not substantially below the row-best score. See the [full benchmark results](../results/munin-10-full-results.md) for the individual evaluations behind each aggregate.

<div class="md-typeset__table dfm-eval-table-wrap">
  <table class="dfm-eval-table">
    <caption>Task aggregate scores</caption>
    <thead>
      <tr>
        <th scope="col" rowspan="2">Suite</th>
        <th scope="col" rowspan="2">Task</th>
        <th scope="col" rowspan="2">Metric</th>
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
      <tr class="dfm-suite-start dfm-suite-danish hl-apertus-original hl-ministral-original hl-ministral-munin hl-qwen-original"><td>Danish</td><td>Common-sense Reasoning</td><td>MCC</td><td>33.1 ± 0.9</td><td>29.4 ± 1.3</td><td>52.4 ± 1.2</td><td>50.2 ± 1.3</td><td><strong>64.6 ± 0.7</strong></td><td>62.2 ± 0.9</td></tr>
      <tr class="dfm-suite-danish hl-apertus-original hl-apertus-munin hl-ministral-original hl-ministral-munin hl-qwen-original hl-qwen-munin"><td>Danish</td><td>Grammatical Error Detection</td><td>micro-F1</td><td><strong>18.0 ± 1.3</strong></td><td><strong>17.4 ± 1.1</strong></td><td><strong>21.7 ± 2.0</strong></td><td><strong>17.7 ± 0.7</strong></td><td><strong>20.4 ± 1.2</strong></td><td><strong>20.7 ± 1.1</strong></td></tr>
      <tr class="dfm-suite-danish hl-apertus-original hl-ministral-munin hl-qwen-original"><td>Danish</td><td>Instruction-following</td><td>Accuracy</td><td>69.0 ± 1.1</td><td>51.4 ± 1.4</td><td>66.7 ± 1.3</td><td>74.4 ± 0.9</td><td><strong>81.6 ± 0.8</strong></td><td>77.9 ± 0.9</td></tr>
      <tr class="dfm-suite-danish hl-apertus-munin hl-ministral-original hl-qwen-munin"><td>Danish</td><td>Knowledge</td><td>MCC</td><td>58.9 ± 0.7</td><td>62.3 ± 0.7</td><td>73.6 ± 0.5</td><td>68.5 ± 0.6</td><td>76.0 ± 0.5</td><td><strong>77.6 ± 0.5</strong></td></tr>
      <tr class="dfm-suite-danish hl-apertus-original hl-apertus-munin hl-ministral-original hl-qwen-original hl-qwen-munin"><td>Danish</td><td>Linguistic Acceptability</td><td>MCC</td><td>33.0 ± 1.2</td><td>29.3 ± 2.4</td><td>43.4 ± 1.9</td><td>18.9 ± 3.1</td><td><strong>49.2 ± 1.7</strong></td><td><strong>52.2 ± 1.3</strong></td></tr>
      <tr class="dfm-suite-danish hl-apertus-original hl-apertus-munin hl-ministral-original hl-ministral-munin hl-qwen-original hl-qwen-munin"><td>Danish</td><td>Multiple-choice Reading Comprehension</td><td>MCC</td><td>67.1 ± 1.0</td><td>66.0 ± 2.0</td><td><strong>85.9 ± 1.4</strong></td><td><strong>84.4 ± 1.1</strong></td><td><strong>87.2 ± 1.2</strong></td><td><strong>87.3 ± 1.3</strong></td></tr>
      <tr class="dfm-suite-danish hl-apertus-original hl-apertus-munin hl-ministral-original hl-qwen-original hl-qwen-munin"><td>Danish</td><td>Named Entity Recognition</td><td>micro-F1</td><td>49.3 ± 1.4</td><td>47.6 ± 1.3</td><td>61.1 ± 1.0</td><td>51.4 ± 1.8</td><td><strong>69.1 ± 1.2</strong></td><td><strong>69.6 ± 1.2</strong></td></tr>
      <tr class="dfm-suite-danish hl-apertus-original hl-apertus-munin hl-ministral-munin hl-qwen-munin"><td>Danish</td><td>Natural Language Inference</td><td>MCC</td><td>48.8 ± 2.3</td><td>52.1 ± 2.6</td><td>25.8 ± 1.6</td><td>58.2 ± 2.2</td><td>53.8 ± 1.9</td><td><strong>65.6 ± 2.0</strong></td></tr>
      <tr class="dfm-suite-danish hl-apertus-original hl-apertus-munin hl-ministral-original hl-ministral-munin hl-qwen-original hl-qwen-munin"><td>Danish</td><td>Reading Comprehension</td><td>F1</td><td><strong>70.8 ± 0.5</strong></td><td>69.4 ± 0.6</td><td>69.7 ± 0.7</td><td><strong>71.2 ± 0.8</strong></td><td><strong>70.8 ± 0.6</strong></td><td><strong>72.0 ± 0.7</strong></td></tr>
      <tr class="dfm-suite-danish hl-apertus-original hl-ministral-original hl-ministral-munin hl-qwen-original hl-qwen-munin"><td>Danish</td><td>Sentiment Classification</td><td>MCC</td><td>57.9 ± 1.0</td><td>54.3 ± 1.1</td><td>60.4 ± 1.0</td><td>59.6 ± 1.4</td><td><strong>64.9 ± 0.9</strong></td><td><strong>64.7 ± 1.0</strong></td></tr>
      <tr class="dfm-suite-danish hl-apertus-original hl-ministral-munin hl-qwen-original hl-qwen-munin"><td>Danish</td><td>Summarization</td><td>chrF++</td><td><strong>37.6 ± 0.2</strong></td><td>36.9 ± 0.2</td><td>35.1 ± 0.3</td><td>37.0 ± 0.2</td><td>36.5 ± 0.3</td><td><strong>36.7 ± 0.4</strong></td></tr>
      <tr class="dfm-suite-danish hl-apertus-original hl-apertus-munin hl-ministral-original hl-ministral-munin hl-qwen-original hl-qwen-munin"><td>Danish</td><td>Word-in-Context</td><td>MCC</td><td>11.8 ± 2.2</td><td>8.7 ± 3.5</td><td>29.9 ± 1.7</td><td>23.3 ± 3.2</td><td><strong>44.6 ± 2.1</strong></td><td><strong>40.1 ± 3.5</strong></td></tr>
      <tr class="dfm-suite-start dfm-suite-english hl-apertus-original hl-ministral-original hl-qwen-original"><td>English</td><td>Common-sense Reasoning</td><td>Accuracy</td><td>58.7 ± 0.5</td><td>23.2 ± 0.4</td><td>73.1 ± 0.4</td><td>59.6 ± 0.5</td><td><strong>90.0 ± 0.3</strong></td><td>85.7 ± 0.3</td></tr>
      <tr class="dfm-suite-english hl-apertus-original hl-ministral-original hl-ministral-munin hl-qwen-original"><td>English</td><td>Instruction-following</td><td>Accuracy</td><td>73.3 ± 1.9</td><td>54.7 ± 2.0</td><td>70.4 ± 1.8</td><td>69.8 ± 1.9</td><td><strong>89.6 ± 1.5</strong></td><td>78.6 ± 1.8</td></tr>
      <tr class="dfm-suite-english hl-apertus-original hl-ministral-original hl-qwen-munin"><td>English</td><td>Knowledge</td><td>Accuracy</td><td>50.3 ± 0.5</td><td>41.9 ± 0.5</td><td><strong>81.7 ± 0.3</strong></td><td>73.0 ± 0.3</td><td>79.2 ± 0.2</td><td><strong>82.4 ± 0.2</strong></td></tr>
      <tr class="dfm-suite-english hl-apertus-original hl-apertus-munin hl-ministral-original hl-ministral-munin hl-qwen-original"><td>English</td><td>Long-context</td><td>Accuracy</td><td>34.6 ± 2.1</td><td>35.8 ± 2.1</td><td>51.4 ± 2.2</td><td>49.4 ± 2.2</td><td><strong>67.2 ± 2.1</strong></td><td>54.6 ± 2.2</td></tr>
      <tr class="dfm-suite-english hl-apertus-original hl-ministral-original hl-qwen-original"><td>English</td><td>Math</td><td>Accuracy</td><td>68.1 ± 1.3</td><td>56.7 ± 1.4</td><td>92.2 ± 0.7</td><td>82.3 ± 1.1</td><td><strong>94.8 ± 0.6</strong></td><td>92.2 ± 0.7</td></tr>
      <tr class="dfm-suite-english hl-apertus-original hl-apertus-munin hl-ministral-original hl-ministral-munin hl-qwen-original hl-qwen-munin"><td>English</td><td>Truthfulness</td><td>Accuracy</td><td>16.8 ± 1.3</td><td>15.7 ± 1.3</td><td>64.7 ± 1.7</td><td>63.3 ± 1.7</td><td><strong>78.1 ± 1.4</strong></td><td><strong>74.2 ± 1.5</strong></td></tr>
      <tr class="dfm-suite-start dfm-suite-agentic hl-apertus-original hl-ministral-original hl-qwen-original"><td>Agentic</td><td>Code</td><td>pass@1</td><td>46.8 ± 2.5</td><td>39.2 ± 2.4</td><td>75.0 ± 2.1</td><td>49.2 ± 2.3</td><td><strong>83.0 ± 1.8</strong></td><td>77.2 ± 2.1</td></tr>
      <tr class="dfm-suite-agentic hl-apertus-original hl-ministral-original hl-qwen-original"><td>Agentic</td><td>Tool Calling</td><td>Accuracy</td><td>52.4 ± 0.8</td><td>43.1 ± 0.8</td><td>75.0 ± 0.7</td><td>49.2 ± 0.8</td><td><strong>79.4 ± 0.6</strong></td><td>75.8 ± 0.7</td></tr>
    </tbody>
  </table>
</div>

??? info "What is included in each aggregate?"

    Danish task groupings follow the EuroEval Danish task taxonomy. Links point to papers where available, otherwise to public datasets, upstream repositories, or the EuroEval dataset construction scripts used for the benchmark. For several entries ending in `-da`, the link is to the original benchmark paper because the evaluated resource is a Danish translated or otherwise localized variant. Some Danish variants, including `ifeval-da`, are adaptations rather than simple direct translations.

    | Suite | Aggregate task | Benchmarks |
    | --- | --- | --- |
    | Danish | Common-sense Reasoning | [`goldenswag-da`](https://arxiv.org/abs/2504.07825), [`hellaswag-da`](https://arxiv.org/abs/1905.07830), [`winogrande-da`](https://arxiv.org/abs/1907.10641) |
    | Danish | Grammatical Error Detection | [`gerlangmod-da`](https://github.com/noahmanu/gerlangmod) |
    | Danish | Instruction-following | [`ifeval-da`](https://arxiv.org/abs/2311.07911) |
    | Danish | Knowledge | [`arc-da`](https://arxiv.org/abs/1803.05457), [`dameta`](https://github.com/kuhumcst/danish-semantic-reasoning-benchmark), [`danish-citizen-tests`](https://huggingface.co/datasets/alexandrainst/danish-citizen-tests), [`danske-talemaader`](https://huggingface.co/datasets/Juunge/danske-talemaader), [`mmlu-da`](https://arxiv.org/abs/2009.03300) |
    | Danish | Linguistic Acceptability | [`dala`](https://arxiv.org/abs/2512.04799), [`scala-da`](https://arxiv.org/abs/2304.00906) |
    | Danish | Multiple-choice Reading Comprehension | [`belebele-da`](https://arxiv.org/abs/2308.16884) |
    | Danish | Named Entity Recognition | [`dane`](https://arxiv.org/abs/2107.05295), [`dansk`](https://arxiv.org/abs/2402.18209) |
    | Danish | Natural Language Inference | [`danish-entailment`](https://github.com/kuhumcst/danish-semantic-reasoning-benchmark), [`danish-lexical-inference`](https://github.com/kuhumcst/danish-semantic-reasoning-benchmark) |
    | Danish | Reading Comprehension | [`multi-wiki-qa-da`](https://arxiv.org/abs/2509.04111), [`scandiqa-da`](https://arxiv.org/abs/2304.00906) |
    | Danish | Sentiment Classification | [`angry-tweets`](https://huggingface.co/datasets/DDSC/angry-tweets), [`danish-sentiment-in-context`](https://github.com/kuhumcst/danish-semantic-reasoning-benchmark) |
    | Danish | Summarization | [`nordjylland-news`](https://huggingface.co/datasets/alexandrainst/nordjylland-news-summarization) |
    | Danish | Word-in-Context | [`danwic`](https://github.com/kuhumcst/danish-semantic-reasoning-benchmark) |
    | English | Knowledge | [`ARC-C`](https://arxiv.org/abs/1803.05457), [`ARC-E`](https://arxiv.org/abs/1803.05457), [`MMLU`](https://arxiv.org/abs/2009.03300), [`MMLU-Pro`](https://arxiv.org/abs/2406.01574) |
    | English | Other task groups | [`HellaSwag`](https://arxiv.org/abs/1905.07830), [`IFEval`](https://arxiv.org/abs/2311.07911), [`RULER 32k`](https://arxiv.org/abs/2404.06654), [`GSM8K`](https://arxiv.org/abs/2110.14168), [`TruthfulQA`](https://arxiv.org/abs/2109.07958) |
    | Agentic | Code and Tool Calling | [`HumanEval`](https://arxiv.org/abs/2107.03374), [`MBPP p@1`](https://arxiv.org/abs/2108.07732), [`BFCL`](https://arxiv.org/abs/2407.07770) |

The main result is that Munin is highly competitive on the Danish evaluations, and in several task groups, our post-trained models match or improve on the original instruct models. The strongest results are on Danish knowledge, reading comprehension, summarization, and natural language inference, where some Munin models are ahead within uncertainty. This is the behavior we wanted to see: post-training moves the models toward stronger Danish performance while retaining a useful general capability profile.

The English and agentic task results are more mixed. The original instruct models are generally stronger on code, tool calling, and several English benchmarks, which reflects that Munin 1.0 is now primarily focused on Danish text capabilities. These gaps are important, because they point directly to the next stage of work: keeping the Danish gains while investing more deliberately in reasoning, multilingual retention, and agentic capabilities.

We also ran a focused Danish creative writing tournament across 360 rated matches, judged by Qwen3.5-397B-A17B. We chose this judge due to its strong Danish language capabilities.

This tournament is not a broad benchmark of model quality, but it is useful because creative writing is a high-signal Danish task: it tests fluency, register, coherence, and whether the model can produce text that feels natural rather than merely correct. [Munin Qwen 9B](https://huggingface.co/danish-foundation-models/munin-qwen3.5-9B) separates clearly from the rest of the field with a 96-9 record, while [Munin Apertus 8B](https://huggingface.co/danish-foundation-models/munin-apertus-8b) places second and [Munin Ministral 8B](https://huggingface.co/danish-foundation-models/munin-ministral3-8B) also beats its original counterpart.

<div class="md-typeset__table">
  <table class="dfm-tournament-table">
    <caption>Danish creative writing tournament ranking; W-L is aggregate win-loss</caption>
    <thead>
      <tr>
        <th scope="col">Rank</th>
        <th scope="col">Model</th>
        <th scope="col">W-L</th>
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

## Contributors

Rasmus Larsen led training, performed experiments, built synthetic datasets and benchmarks, and drafted the release announcement.

Oliver Kinch built synthetic datasets and benchmarks.

Vladimir Salnikov and Jacob Nielsen contributed to datasets.

Dan Saattrup Smart developed benchmarks and led the integration into EuroEval.

Torben Blach contributed with project management and coordination.

## Acknowledgements

The work was supported by the Danish Foundation Models project, funded by the Danish government. This work was partially supported by DeiC National HPC (grant agreement DeiC-SDU-N5-2025162).
