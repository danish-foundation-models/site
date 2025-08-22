---
pretty_name: Python Enhancement Proposals (PEP)
language:
- en
- code
license: other
license_name: Public Domain
task_categories:
- text-generation
- fill-mask
task_ids:
- language-modeling
domains:
- Technical
---

# Dataset Card for Python Enhancement Proposals (PEP)

<!-- START-SHORT DESCRIPTION -->
This set consists of almost all PEPs created.
<!-- END-SHORT DESCRIPTION -->

Python Enhancement Proposals, or PEPs, are design documents that generally provide a technical specification and rationale for new features of the Python programming language. There have been 661 PEPs published. The majority of PEPs are published in the Public Domain, but 5 were published under the “Open Publication License” and omitted from this dataset. PEPs are long, highly-polished, and technical in nature and often include code examples paired with their prose. PEPs are authored in ReStructured Text; we used pandoc to convert them to plain text.




## Dataset Description

<!-- START-DESC-STATS -->
- **Number of samples**: 655
- **Number of tokens (Llama 3)**: 2.54M
- **Average document length in tokens (min, max)**: 3.87K (49, 19.78K)
<!-- END-DESC-STATS -->


## Dataset Structure
An entry in the dataset consists of the following fields:

- `id` (`str`): An unique identifier for each document.
- `text`(`str`): The content of the document.
- `source` (`str`): The source of the document (see [Source Data](#source-data)).
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
