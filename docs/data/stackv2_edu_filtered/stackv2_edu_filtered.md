---
pretty_name: Stack V2 Edu
language:
- en
- code
license: other
license_name: Various - MIT, BSD-3-Clause, Apache-2.0, etc.
task_categories:
- text-generation
- fill-mask
task_ids:
- language-modeling
domains:
- Other
---

# Dataset Card for Stack V2 Edu

<!-- START-SHORT DESCRIPTION -->
Stack V2 Edu is a dataset containing files in various programming and markup languages from openly licensed projects.
<!-- END-SHORT DESCRIPTION -->

We filter the Stack V2 to only include code from openly licensed repositories, based on the license detection performed by the creators of Stack V2. When multiple licenses are detected in a single repository, we ensure that all of the licenses are on the Blue Oak Council certified license list. Per-document license information is available in the license entry of the metadata field of each example. Code for collecting, processing, and preparing this dataset is available in the common-pile GitHub repo.




## Dataset Description

<!-- START-DESC-STATS -->
- **Number of samples**: 67.79M
- **Number of tokens (Llama 3)**: 62.39B
- **Average document length in tokens (min, max)**: 920.2978463866087 (1, 6.70M)
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
