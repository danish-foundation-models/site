---
pretty_name: Creative Commons Youtube
language:
- en
license: cc-by-sa-4.0
license_name: CC-BY-SA 4.0
task_categories:
- text-generation
- fill-mask
task_ids:
- language-modeling
domains:
- Speeches
- Spoken
---

# Dataset Card for Creative Commons Youtube

<!-- START-SHORT DESCRIPTION -->
YouTube is a large-scale video-sharing platform where users have the option of uploading content under a CC BY license.
<!-- END-SHORT DESCRIPTION -->

To collect high-quality speech-based textual content and combat the rampant license laundering on YouTube, we manually curated a set of over 2,000 YouTube channels that consistently release original openly licensed content containing speech. The resulting collection spans a wide range of genres, including lectures, tutorials, reviews, video essays, speeches, and vlogs. From these channels, we retrieved over 1.1 million openly licensed videos comprising more than 470,000 hours of content. Finally, each video was transcribed to text using the Whisper speech recognition model. Code for collecting, processing, and preparing this dataset is available here.




## Dataset Description

<!-- START-DESC-STATS -->
- **Number of samples**: 988.25K
- **Number of tokens (Llama 3)**: 4.07B
- **Average document length in tokens (min, max)**: 4.12K (1, 193.44K)
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
