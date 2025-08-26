---
pretty_name: European Parliament
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
- Spoken
---

# Dataset Card for European Parliament

<!-- START-SHORT DESCRIPTION -->
The Danish subsection of [Europarl](https://aclanthology.org/2005.mtsummit-papers.11/).
<!-- END-SHORT DESCRIPTION -->


The europarl is a corpus of parallel text in 11 languages from the proceedings of the European Parliament, which are published on the web. This corpus has found widespread use in the NLP community. It was initially intended as training data for statistical machine translation.


## Dataset Description


<!-- START-DESC-STATS -->
- **Number of samples**: 3.93K
- **Number of tokens (Llama 3)**: 100.84M
- **Average document length in tokens (min, max)**: 25.66K (8, 222.73K)
<!-- END-DESC-STATS -->



## Dataset Structure
An example from the dataset looks as follows.


<!-- START-SAMPLE -->
```py
{
  "id": "ep_07-02-01-008",
  "text": "TALER 6703: Jeg har stemt for henstillingen om godkendelse af opdelingsanordninger til beskyttelse a[...]",
  "source": "ep",
  "added": "2019-11-20",
  "created": "2004-01-01, 2009-01-01",
  "token_count": 16237
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
