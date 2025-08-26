---
pretty_name: NAAT
language:
- da
license: cc0-1.0
license_name: CC-0
size_categories:
- 1-10k
task_categories:
- text-generation
- fill-mask
task_ids:
- language-modeling
source_datasets:
- danish-foundation-models/danish-gigaword
domains:
- Conversation
---

# Dataset Card for NAAT

<!-- START-SHORT DESCRIPTION -->
Danish speeches from 1930-2022.
<!-- END-SHORT DESCRIPTION -->

<!-- TODO: Check for duplicates with 'danske-taler' -->

## Dataset Description


<!-- START-DESC-STATS -->
- **Number of samples**: 129
- **Number of tokens (Llama 3)**: 286.68K
- **Average document length in tokens (min, max)**: 2.22K (228, 3.95K)
<!-- END-DESC-STATS -->



## Dataset Structure
An example from the dataset looks as follows.


<!-- START-SAMPLE -->
```py
{
  "id": "naat_1958kongfrederikix",
  "text": "Naar jeg i aften sender min nytaarshilsen til det danske folk og tænker tilbage paa det aar, der sva[...]",
  "source": "naat",
  "added": "2020-02-11",
  "created": "1930-01-01, 2022-01-01",
  "token_count": 1059
}
```

### Data Fields

An entry in the dataset consists of the following fields:

- `id` (`str`): An unique identifier for each document.
- `text`(`str`): The content of the document.
- `source` (`str`): The source of the document.
- `added` (`str`): An date for when the document was added to this collection.
- `created` (`str`): An date range for when the document was originally created.
- `token_count` (`int`): The number of tokens in the sample computed using the Llama 8B tokenizer
<!-- END-SAMPLE -->

### Dataset Statistics

<!-- START-DATASET PLOTS -->
<p align="center">
<img src="./images/dist_document_length.svg" width="600" style="margin-right: 10px;" />
</p>
<!-- END-DATASET PLOTS -->


## Additional Information


### Citation Information

This dataset was initially published as part of the [Danish gigaword](https://huggingface.co/danish-foundation-models). We recommend that you cite and reference it if you use this dataset:

> Derczynski, L., Ciosici, M. R., et al. (2021). The Danish Gigaword Corpus. In Proceedings of the 23rd Nordic Conference on Computational Linguistics (NoDaLiDa 2021).

```bash
@inproceedings{dagw,
 title = {{The Danish Gigaword Corpus}},
 author = {Leon Derczynski and Manuel R. Ciosici and Rebekah Baglini and Morten H. Christiansen and Jacob Aarup Dalsgaard and Riccardo Fusaroli and Peter Juel Henrichsen and Rasmus Hvingelby and Andreas Kirkedal and Alex Speed Kjeldsen and Claus Ladefoged and Finn Årup Nielsen and Jens Madsen and Malte Lau Petersen and Jonathan Hvithamar Rystrøm and Daniel Varab},
 year = 2021,
 booktitle = {Proceedings of the 23rd Nordic Conference on Computational Linguistics},
 publisher = {NEALT}
}
```
