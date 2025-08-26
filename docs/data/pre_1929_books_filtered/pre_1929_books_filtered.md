---
pretty_name: Pre-1929 Books
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
- Books
---

# Dataset Card for Pre-1929 Books

<!-- START-SHORT DESCRIPTION -->
A set of books published in the US pre-1929.
<!-- END-SHORT DESCRIPTION -->

Books published in the US before 1929 passed into the public domain on January 1, 2024. We used the bibliographic catalog Hathifiles produced by HathiTrust to identify digitized books which were published in the US before 1929. The collection contains over 130,000 books digitized and processed by the Internet Archive on behalf of HathiTrust member libraries. The OCR plain text files were downloaded directly from the Internet Archive website.




## Dataset Description

<!-- START-DESC-STATS -->
- **Number of samples**: 124.55K
- **Number of tokens (Llama 3)**: 10.56B
- **Average document length in tokens (min, max)**: 84.82K (19, 5.78M)
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
