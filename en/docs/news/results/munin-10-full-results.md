---
hide:
  - navigation
---

# Munin 1.0 Full Evaluation Results

Scores are percentages. Standard errors are percentage points. Deltas are `Munin - Original`; Danish deltas were computed from the reported scores with propagated standard errors.

Task groupings use the EuroEval Danish task taxonomy for Danish datasets. Aggregate rows are unweighted means across evals in the task; aggregate standard error is `sqrt(sum(SE_i^2)) / n`, assuming independent evaluation estimates.

| Suite | Task | Metric | Benchmark | Apertus Original ± SE | Apertus Munin ± SE | Apertus Δ ± SE | Ministral Original ± SE | Ministral Munin ± SE | Ministral Δ ± SE | Qwen Original ± SE | Qwen Munin ± SE | Qwen Δ ± SE |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Danish | Common-sense Reasoning | MCC | Average (3 evals) | 33.11 ± 0.86 | 29.40 ± 1.28 | -3.71 ± 1.54 | 52.37 ± 1.19 | 50.21 ± 1.29 | -2.16 ± 1.76 | 64.64 ± 0.72 | 62.22 ± 0.88 | -2.42 ± 1.14 |
| Danish | Common-sense Reasoning | MCC | goldenswag-da | 47.66 ± 1.23 | 38.65 ± 2.50 | -9.01 ± 2.79 | 68.89 ± 1.49 | 64.52 ± 1.51 | -4.37 ± 2.12 | 85.94 ± 0.79 | 78.94 ± 1.19 | -7.00 ± 1.43 |
| Danish | Common-sense Reasoning | MCC | hellaswag-da | 39.19 ± 1.01 | 36.89 ± 1.88 | -2.30 ± 2.13 | 55.79 ± 2.04 | 51.80 ± 2.79 | -3.99 ± 3.46 | 73.28 ± 0.99 | 67.50 ± 1.35 | -5.78 ± 1.67 |
| Danish | Common-sense Reasoning | MCC | winogrande-da | 12.48 ± 2.02 | 12.65 ± 2.25 | +0.17 ± 3.02 | 32.43 ± 2.54 | 34.32 ± 2.21 | +1.89 ± 3.37 | 34.71 ± 1.75 | 40.22 ± 1.93 | +5.51 ± 2.61 |
| Danish | Grammatical Error Detection | micro-F1 | Average (1 eval) | 18.00 ± 1.31 | 17.35 ± 1.06 | -0.65 ± 1.69 | 21.72 ± 2.04 | 17.66 ± 0.74 | -4.06 ± 2.17 | 20.37 ± 1.25 | 20.74 ± 1.14 | +0.37 ± 1.69 |
| Danish | Grammatical Error Detection | micro-F1 | gerlangmod-da | 18.00 ± 1.31 | 17.35 ± 1.06 | -0.65 ± 1.69 | 21.72 ± 2.04 | 17.66 ± 0.74 | -4.06 ± 2.17 | 20.37 ± 1.25 | 20.74 ± 1.14 | +0.37 ± 1.69 |
| Danish | Instruction-following | Accuracy | Average (1 eval) | 69.00 ± 1.06 | 51.43 ± 1.38 | -17.57 ± 1.74 | 66.67 ± 1.31 | 74.38 ± 0.94 | +7.71 ± 1.61 | 81.56 ± 0.85 | 77.88 ± 0.89 | -3.68 ± 1.23 |
| Danish | Instruction-following | Accuracy | ifeval-da | 69.00 ± 1.06 | 51.43 ± 1.38 | -17.57 ± 1.74 | 66.67 ± 1.31 | 74.38 ± 0.94 | +7.71 ± 1.61 | 81.56 ± 0.85 | 77.88 ± 0.89 | -3.68 ± 1.23 |
| Danish | Knowledge | MCC | Average (5 evals) | 58.89 ± 0.73 | 62.29 ± 0.72 | +3.41 ± 1.03 | 73.58 ± 0.52 | 68.48 ± 0.58 | -5.09 ± 0.78 | 75.98 ± 0.52 | 77.64 ± 0.50 | +1.67 ± 0.72 |
| Danish | Knowledge | MCC | arc-da | 63.02 ± 1.58 | 65.87 ± 1.43 | +2.85 ± 2.13 | 84.17 ± 0.80 | 81.86 ± 0.77 | -2.31 ± 1.11 | 88.30 ± 0.80 | 88.82 ± 0.72 | +0.52 ± 1.08 |
| Danish | Knowledge | MCC | dameta | 62.52 ± 1.58 | 67.63 ± 1.66 | +5.11 ± 2.29 | 74.93 ± 1.21 | 66.52 ± 1.48 | -8.41 ± 1.91 | 76.70 ± 0.68 | 78.14 ± 1.01 | +1.44 ± 1.22 |
| Danish | Knowledge | MCC | danish-citizen-tests | 72.31 ± 2.18 | 73.25 ± 2.06 | +0.94 ± 3.00 | 78.01 ± 0.94 | 71.59 ± 1.71 | -6.42 ± 1.95 | 76.92 ± 1.67 | 82.16 ± 1.53 | +5.24 ± 2.26 |
| Danish | Knowledge | MCC | danske-talemaader | 55.11 ± 1.80 | 62.44 ± 1.68 | +7.33 ± 2.46 | 73.14 ± 1.56 | 68.47 ± 1.40 | -4.67 ± 2.10 | 75.67 ± 1.43 | 76.72 ± 0.92 | +1.05 ± 1.70 |
| Danish | Knowledge | MCC | mmlu-da | 41.47 ± 0.58 | 42.27 ± 1.11 | +0.80 ± 1.25 | 57.63 ± 1.11 | 53.97 ± 0.94 | -3.66 ± 1.45 | 62.30 ± 0.90 | 62.38 ± 1.20 | +0.08 ± 1.50 |
| Danish | Linguistic Acceptability | MCC | Average (2 evals) | 32.95 ± 1.19 | 29.34 ± 2.38 | -3.62 ± 2.66 | 43.37 ± 1.85 | 18.89 ± 3.06 | -24.48 ± 3.57 | 49.25 ± 1.68 | 52.19 ± 1.30 | +2.95 ± 2.12 |
| Danish | Linguistic Acceptability | MCC | dala | 29.38 ± 1.82 | 25.56 ± 3.12 | -3.82 ± 3.61 | 39.49 ± 2.66 | 16.99 ± 4.12 | -22.50 ± 4.90 | 45.65 ± 2.09 | 49.07 ± 1.55 | +3.42 ± 2.60 |
| Danish | Linguistic Acceptability | MCC | scala-da | 36.53 ± 1.53 | 33.11 ± 3.60 | -3.42 ± 3.91 | 47.25 ± 2.58 | 20.79 ± 4.52 | -26.46 ± 5.20 | 52.84 ± 2.62 | 55.31 ± 2.08 | +2.47 ± 3.35 |
| Danish | Multiple-choice Reading Comprehension | MCC | Average (1 eval) | 67.09 ± 1.02 | 65.99 ± 2.04 | -1.10 ± 2.28 | 85.94 ± 1.39 | 84.42 ± 1.12 | -1.52 ± 1.79 | 87.19 ± 1.17 | 87.35 ± 1.27 | +0.16 ± 1.73 |
| Danish | Multiple-choice Reading Comprehension | MCC | belebele-da | 67.09 ± 1.02 | 65.99 ± 2.04 | -1.10 ± 2.28 | 85.94 ± 1.39 | 84.42 ± 1.12 | -1.52 ± 1.79 | 87.19 ± 1.17 | 87.35 ± 1.27 | +0.16 ± 1.73 |
| Danish | Named Entity Recognition | micro-F1 | Average (2 evals) | 49.33 ± 1.40 | 47.60 ± 1.33 | -1.72 ± 1.93 | 61.13 ± 1.01 | 51.41 ± 1.76 | -9.72 ± 2.03 | 69.12 ± 1.16 | 69.63 ± 1.23 | +0.51 ± 1.69 |
| Danish | Named Entity Recognition | micro-F1 | dane | 51.69 ± 1.30 | 48.66 ± 1.53 | -3.03 ± 2.01 | 66.16 ± 1.42 | 53.80 ± 1.51 | -12.36 ± 2.07 | 74.51 ± 0.75 | 76.33 ± 0.85 | +1.82 ± 1.13 |
| Danish | Named Entity Recognition | micro-F1 | dansk | 46.97 ± 2.48 | 46.55 ± 2.18 | -0.42 ± 3.30 | 56.11 ± 1.44 | 49.02 ± 3.19 | -7.09 ± 3.50 | 63.74 ± 2.20 | 62.94 ± 2.31 | -0.80 ± 3.19 |
| Danish | Natural Language Inference | MCC | Average (2 evals) | 48.80 ± 2.34 | 52.09 ± 2.62 | +3.29 ± 3.51 | 25.75 ± 1.58 | 58.18 ± 2.22 | +32.42 ± 2.73 | 53.80 ± 1.93 | 65.63 ± 2.01 | +11.83 ± 2.79 |
| Danish | Natural Language Inference | MCC | danish-entailment | 57.24 ± 3.67 | 64.03 ± 4.45 | +6.79 ± 5.77 | 51.51 ± 3.17 | 55.54 ± 3.61 | +4.03 ± 4.80 | 62.10 ± 2.55 | 67.72 ± 1.46 | +5.62 ± 2.94 |
| Danish | Natural Language Inference | MCC | danish-lexical-inference | 40.37 ± 2.90 | 40.15 ± 2.76 | -0.22 ± 4.00 | 0.00 ± 0.00 | 60.82 ± 2.59 | +60.82 ± 2.59 | 45.51 ± 2.91 | 63.55 ± 3.75 | +18.04 ± 4.75 |
| Danish | Reading Comprehension | F1 | Average (2 evals) | 70.75 ± 0.51 | 69.41 ± 0.56 | -1.35 ± 0.76 | 69.71 ± 0.72 | 71.23 ± 0.81 | +1.52 ± 1.08 | 70.84 ± 0.55 | 71.96 ± 0.68 | +1.12 ± 0.88 |
| Danish | Reading Comprehension | F1 | multi-wiki-qa-da | 77.94 ± 0.97 | 74.11 ± 1.10 | -3.83 ± 1.47 | 75.77 ± 1.34 | 79.52 ± 1.43 | +3.75 ± 1.96 | 79.28 ± 0.78 | 79.51 ± 1.20 | +0.23 ± 1.43 |
| Danish | Reading Comprehension | F1 | scandiqa-da | 63.57 ± 0.34 | 64.70 ± 0.25 | +1.13 ± 0.42 | 63.65 ± 0.52 | 62.95 ± 0.76 | -0.70 ± 0.92 | 62.39 ± 0.78 | 64.40 ± 0.66 | +2.01 ± 1.02 |
| Danish | Sentiment Classification | MCC | Average (2 evals) | 57.89 ± 0.97 | 54.30 ± 1.10 | -3.59 ± 1.46 | 60.37 ± 0.97 | 59.56 ± 1.41 | -0.81 ± 1.71 | 64.89 ± 0.93 | 64.69 ± 1.00 | -0.20 ± 1.36 |
| Danish | Sentiment Classification | MCC | angry-tweets | 52.17 ± 0.96 | 48.76 ± 0.94 | -3.41 ± 1.34 | 52.91 ± 0.72 | 52.71 ± 1.32 | -0.20 ± 1.50 | 55.73 ± 1.16 | 56.26 ± 1.07 | +0.53 ± 1.58 |
| Danish | Sentiment Classification | MCC | danish-sentiment-in-context | 63.61 ± 1.68 | 59.84 ± 1.99 | -3.77 ± 2.60 | 67.83 ± 1.81 | 66.40 ± 2.49 | -1.43 ± 3.08 | 74.05 ± 1.45 | 73.11 ± 1.68 | -0.94 ± 2.22 |
| Danish | Summarization | chrF++ | Average (1 eval) | 37.56 ± 0.20 | 36.88 ± 0.20 | -0.68 ± 0.28 | 35.09 ± 0.35 | 36.97 ± 0.21 | +1.88 ± 0.41 | 36.51 ± 0.28 | 36.66 ± 0.44 | +0.15 ± 0.52 |
| Danish | Summarization | chrF++ | nordjylland-news | 37.56 ± 0.20 | 36.88 ± 0.20 | -0.68 ± 0.28 | 35.09 ± 0.35 | 36.97 ± 0.21 | +1.88 ± 0.41 | 36.51 ± 0.28 | 36.66 ± 0.44 | +0.15 ± 0.52 |
| Danish | Word-in-Context | MCC | Average (1 eval) | 11.83 ± 2.20 | 8.71 ± 3.46 | -3.12 ± 4.10 | 29.87 ± 1.70 | 23.27 ± 3.18 | -6.60 ± 3.61 | 44.60 ± 2.06 | 40.11 ± 3.46 | -4.49 ± 4.03 |
| Danish | Word-in-Context | MCC | danwic | 11.83 ± 2.20 | 8.71 ± 3.46 | -3.12 ± 4.10 | 29.87 ± 1.70 | 23.27 ± 3.18 | -6.60 ± 3.61 | 44.60 ± 2.06 | 40.11 ± 3.46 | -4.49 ± 4.03 |
| English | Common-sense Reasoning | Accuracy | Average (1 eval) | 58.70 ± 0.50 | 23.20 ± 0.40 | -35.50 ± 0.60 | 73.10 ± 0.40 | 59.60 ± 0.50 | -13.50 ± 0.70 | 90.00 ± 0.30 | 85.70 ± 0.30 | -4.30 ± 0.50 |
| English | Common-sense Reasoning | Accuracy | HellaSwag | 58.7 ± 0.5 | 23.2 ± 0.4 | -35.5 ± 0.6 | 73.1 ± 0.4 | 59.6 ± 0.5 | -13.5 ± 0.7 | 90.0 ± 0.3 | 85.7 ± 0.3 | -4.3 ± 0.5 |
| English | Instruction-following | Accuracy | Average (1 eval) | 73.30 ± 1.90 | 54.70 ± 2.00 | -18.50 ± 2.70 | 70.40 ± 1.80 | 69.80 ± 1.90 | -0.60 ± 2.70 | 89.60 ± 1.50 | 78.60 ± 1.80 | -11.00 ± 2.30 |
| English | Instruction-following | Accuracy | IFEval | 73.3 ± 1.9 | 54.7 ± 2.0 | -18.5 ± 2.7 | 70.4 ± 1.8 | 69.8 ± 1.9 | -0.6 ± 2.7 | 89.6 ± 1.5 | 78.6 ± 1.8 | -11.0 ± 2.3 |
| English | Knowledge | Accuracy | Average (4 evals) | 50.27 ± 0.46 | 41.92 ± 0.45 | -8.35 ± 0.65 | 81.72 ± 0.26 | 72.97 ± 0.29 | -8.75 ± 0.42 | 79.15 ± 0.22 | 82.40 ± 0.24 | +3.23 ± 0.33 |
| English | Knowledge | Accuracy | ARC-C | 55.5 ± 1.5 | 55.0 ± 1.5 | -0.5 ± 2.1 | 90.8 ± 0.8 | 88.5 ± 0.9 | -2.3 ± 1.3 | 96.1 ± 0.6 | 93.8 ± 0.7 | -2.3 ± 0.9 |
| English | Knowledge | Accuracy | ARC-E | 72.9 ± 0.9 | 74.2 ± 0.9 | +1.3 ± 1.3 | 96.3 ± 0.4 | 94.6 ± 0.5 | -1.7 ± 0.6 | 98.5 ± 0.3 | 98.3 ± 0.3 | -0.2 ± 0.4 |
| English | Knowledge | Accuracy | MMLU | 39.8 ± 0.4 | 31.7 ± 0.4 | -8.1 ± 0.6 | 71.3 ± 0.4 | 67.8 ± 0.4 | -3.6 ± 0.6 | 41.4 ± 0.4 | 76.6 ± 0.4 | +35.2 ± 0.6 |
| English | Knowledge | Accuracy | MMLU-Pro | 32.9 ± 0.4 | 6.8 ± 0.2 | -26.1 ± 0.5 | 68.5 ± 0.4 | 41.0 ± 0.4 | -27.4 ± 0.6 | 80.6 ± 0.4 | 60.9 ± 0.4 | -19.8 ± 0.6 |
| English | Long-context | Accuracy | Average (1 eval) | 34.60 ± 2.10 | 35.80 ± 2.10 | +1.20 ± 3.00 | 51.40 ± 2.20 | 49.40 ± 2.20 | -2.00 ± 3.20 | 67.20 ± 2.10 | 54.60 ± 2.20 | -12.60 ± 3.10 |
| English | Long-context | Accuracy | RULER 32k | 34.6 ± 2.1 | 35.8 ± 2.1 | +1.2 ± 3.0 | 51.4 ± 2.2 | 49.4 ± 2.2 | -2.0 ± 3.2 | 67.2 ± 2.1 | 54.6 ± 2.2 | -12.6 ± 3.1 |
| English | Math | Accuracy | Average (1 eval) | 68.10 ± 1.30 | 56.70 ± 1.40 | -11.40 ± 1.90 | 92.20 ± 0.70 | 82.30 ± 1.10 | -9.90 ± 1.30 | 94.80 ± 0.60 | 92.20 ± 0.70 | -2.60 ± 1.00 |
| English | Math | Accuracy | GSM8K | 68.1 ± 1.3 | 56.7 ± 1.4 | -11.4 ± 1.9 | 92.2 ± 0.7 | 82.3 ± 1.1 | -9.9 ± 1.3 | 94.8 ± 0.6 | 92.2 ± 0.7 | -2.6 ± 1.0 |
| English | Truthfulness | Accuracy | Average (1 eval) | 16.80 ± 1.30 | 15.70 ± 1.30 | -1.10 ± 1.80 | 64.70 ± 1.70 | 63.30 ± 1.70 | -1.50 ± 2.40 | 78.10 ± 1.40 | 74.20 ± 1.50 | -3.90 ± 2.10 |
| English | Truthfulness | Accuracy | TruthfulQA | 16.8 ± 1.3 | 15.7 ± 1.3 | -1.1 ± 1.8 | 64.7 ± 1.7 | 63.3 ± 1.7 | -1.5 ± 2.4 | 78.1 ± 1.4 | 74.2 ± 1.5 | -3.9 ± 2.1 |
| Agentic | Code | pass@1 | Average (2 evals) | 46.75 ± 2.49 | 39.20 ± 2.38 | -7.55 ± 3.44 | 75.05 ± 2.13 | 49.20 ± 2.31 | -25.85 ± 3.13 | 82.95 ± 1.84 | 77.20 ± 2.06 | -5.75 ± 2.72 |
| Agentic | Code | pass@1 | HumanEval | 42.1 ± 3.9 | 29.9 ± 3.6 | -12.2 ± 5.3 | 76.2 ± 3.3 | 29.3 ± 3.6 | -47.0 ± 4.9 | 87.8 ± 2.6 | 80.5 ± 3.1 | -7.3 ± 4.0 |
| Agentic | Code | pass@1 | MBPP p@1 | 51.4 ± 3.1 | 48.5 ± 3.1 | -2.9 ± 4.4 | 73.9 ± 2.7 | 69.1 ± 2.9 | -4.7 ± 3.9 | 78.1 ± 2.6 | 73.9 ± 2.7 | -4.2 ± 3.7 |
| Agentic | Tool Calling | Accuracy | Average (1 eval) | 52.40 ± 0.80 | 43.10 ± 0.80 | -9.30 ± 1.10 | 75.00 ± 0.70 | 49.20 ± 0.80 | -25.80 ± 1.00 | 79.40 ± 0.60 | 75.80 ± 0.70 | -3.60 ± 0.90 |
| Agentic | Tool Calling | Accuracy | BFCL | 52.4 ± 0.8 | 43.1 ± 0.8 | -9.3 ± 1.1 | 75.0 ± 0.7 | 49.2 ± 0.8 | -25.8 ± 1.0 | 79.4 ± 0.6 | 75.8 ± 0.7 | -3.6 ± 0.9 |
