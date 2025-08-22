---
pretty_name: Hestenettet (Danish debate forum)
language:
- da
license: cc0-1.0
license_name: CC-0
size_categories:
- 10k-100k
task_categories:
- text-generation
- fill-mask
task_ids:
- language-modeling
source_datasets:
- danish-foundation-models/danish-gigaword
domains:
- Social Media
---

# Dataset Card for Hestenettet

<!-- START-SHORT DESCRIPTION -->
Samples from the Danish debate forum www.heste-nettet.dk.
<!-- END-SHORT DESCRIPTION -->


The forum have been in use since 1997 and it is used as a debate forum covering a wide range of everyday topics. 

Its inclusion as training data for large language models have multiple times reached [national news](https://www.dr.dk/nyheder/viden/teknologi/heste-nettet-kan-blive-grundlag-kunstig-intelligens-paa-dansk).

## Dataset Description


<!-- START-DESC-STATS -->
- **Number of samples**: 14.34K
- **Number of tokens (Llama 3)**: 389.32M
- **Average document length in tokens (min, max)**: 27.15K (3, 9.81M)
<!-- END-DESC-STATS -->



## Dataset Structure
An example from the dataset looks as follows.


<!-- START-SAMPLE -->
```py
{
  "id": "hest_forum112802271280227_0",
  "text": "Er den ikke kær? \nJeg kan ikke forstå at der altid er nogle der åbenbart ser alle indlæg her på HN ,[...]",
  "source": "hest",
  "added": "2020-10-05",
  "created": "2000-01-01, 2022-01-01",
  "token_count": 311
}
```

### Data Fields

An entry in the dataset consists of the following fields:

- `id` (`str`): An unique identifier for each document.
- `text`(`str`): The content of the document.
- `source` (`str`): The source of the document (see [Source Data](#source-data)).
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
