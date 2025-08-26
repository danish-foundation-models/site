---
pretty_name: Ubuntu IRC
language:
- en
license: other
license_name: Public Domain
task_categories:
- text-generation
- fill-mask
task_ids:
- language-modeling
domains:
- Conversation
- Social Media
---

# Dataset Card for Ubuntu IRC

<!-- START-SHORT DESCRIPTION -->
Ubuntu-hosted Internet Relay Chat (IRC) is an online chat service.
<!-- END-SHORT DESCRIPTION -->

Logs of all discussions on the Ubuntu-hosted Internet Relay Chat (IRC) since 2004 have been archived and released into the Public Domain. We downloaded all chats from all channels up until March of 2025. We consider all messages for a given channel on a given day as a single document. We removed system messages as well as those from known bots.




## Dataset Description

<!-- START-DESC-STATS -->
- **Number of samples**: 216.20K
- **Number of tokens (Llama 3)**: 1.76B
- **Average document length in tokens (min, max)**: 8.14K (1, 1.37M)
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
