---
pretty_name: Johannes V. Jensen
language:
- da
license: cc-by-sa-4.0
license_name: CC-BY-SA 4.0
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
- Books
---

# Dataset Card for Johannes V. Jensen

<!-- START-SHORT DESCRIPTION -->
The works of the Danish author and poet, [Johannes V. Jensen](https://da.wikipedia.org/wiki/Johannes_V._Jensen).
<!-- END-SHORT DESCRIPTION -->






## Dataset Description


<!-- START-DESC-STATS -->
- **Number of samples**: 42
- **Number of tokens (Llama 3)**: 3.55M
- **Average document length in tokens (min, max)**: 84.50K (15.47K, 271.79K)
<!-- END-DESC-STATS -->



## Dataset Structure
An example from the dataset looks as follows.


<!-- START-SAMPLE -->
```py
{
  "id": "jvj_Jørgine",
  "text": "JØRGINE JØRGINE KØBENHAVN HAGE & CLAUSENS FORLAG (J. FR. CLAUSEN) 1926 JOHANNES V. JENSEN COPYRIGHT [...]",
  "source": "jvj",
  "added": "2020-06-26",
  "created": "1873-01-01, 1951-01-01",
  "token_count": 29393
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
