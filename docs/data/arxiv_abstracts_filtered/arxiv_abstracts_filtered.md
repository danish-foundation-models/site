---
pretty_name: ArXiv Abstracts
language:
- en
license: cc0-1.0
license_name: CC-0
task_categories:
- text-generation
- fill-mask
task_ids:
- language-modeling
domains:
- Scientific
---

# Dataset Card for ArXiv Abstracts

<!-- START-SHORT DESCRIPTION -->
A set of public domain arxiv paper abstracts.
<!-- END-SHORT DESCRIPTION -->

Each paper uploaded to ArXiv includes structured metadata fields, including an abstract summarizing the paper’s findings and contributions. According to ArXiv’s licensing policy, the metadata for any paper submitted to ArXiv is distributed under the CC0 license, regardless of the license of the paper itself. Thus, this dataset contains the abstract for every paper submitted to ArXiv through late 2024. We source the abstracts from ArXiv’s API via the Open Archives Initiative Protocol for Metadata Harvesting endpoint and reproduce them as-is. Code for collecting, processing, and preparing this dataset is available in the common-pile GitHub repo.




## Dataset Description

<!-- START-DESC-STATS -->
- **Number of samples**: 2.50M
- **Number of tokens (Llama 3)**: 524.45M
- **Average document length in tokens (min, max)**: 209.42911292167878 (4, 1.31K)
<!-- END-DESC-STATS -->


## Dataset Structure
An entry in the dataset consists of the following fields:

- `id` (`str`): An unique identifier for each document.
- `text`(`str`): The content of the document.
- `source` (`str`): The source of the document.
- `added` (`str`): An date for when the document was added to this collection.
- `created` (`str`): An date range for when the document was originally created.
- `token_count` (`int`): The number of tokens in the sample computed using the Llama 8B tokenizer


### Additional Processing


### Dataset Statistics

<!-- START-DATASET PLOTS -->
<p align="center">
<img src="./images/dist_document_length.svg" width="600" style="margin-right: 10px;" />
</p>
<!-- END-DATASET PLOTS -->


# Additional Information

## License Information
While we aim to produce datasets with completely accurate licensing information, license laundering and inaccurate metadata can cause us to erroneously assign the incorrect license to some documents (for further discussion of this limitation, please see our paper). If you believe you have found an instance of incorrect licensing in this dataset, please start a discussion on this repository.

### Citation Information

If you use this dataset, please cite:
```bibtex
@article{kandpal2025common,
  title={{The Common Pile v0.1: An 8TB Dataset of Public Domain and Openly Licensed Text}},
  author={Nikhil Kandpal and Brian Lester and Colin Raffel and Sebastian Majstorovic and Stella Biderman and Baber Abbasi and Luca Soldaini and Enrico Shippole and A. Feder Cooper and Aviya Skowron and Shayne Longpre and Lintang Sutawika and Alon Albalak and Zhenlin Xu and Guilherme Penedo and Loubna Ben  and Elie Bakouch and John David  and Honglu Fan and Dashiell Stander and Guangyu Song and Aaron Gokaslan and John Kirchenbauer and Tom Goldstein and Brian R and Bhavya Kailkhura and Tyler Murray},
  journal={arXiv preprint},
  year={2025}
}
```
