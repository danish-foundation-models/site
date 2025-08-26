---
pretty_name: DBC D1G1TAL - Reviews
language:
- da
- en
- se
- nb
- nn
license: other
license_name: Written agreement (public models, private data)
task_categories:
- text-generation
- fill-mask
task_ids:
- language-modeling
domains:
- Books
- Other
---

# Dataset Card for DBC D1G1TAL - Reviews

<!-- START-SHORT DESCRIPTION -->
dbc-reviews consists of more than 214 thousand reviews of books and other materials collected and created by DBC D1G1TAL (former Dansk Bibliotekscenter).
<!-- END-SHORT DESCRIPTION -->

The dataset contains thousands of reviews in the Danish language, which are supplemented by English, Norwegian, Swedish, German, and other language reviews. Instances that comprise this dataset represent reviews of books or other materials. The dataset includes reviews created between 1991 and 2024.




## Dataset Description

<!-- START-DESC-STATS -->
- **Number of samples**: 213.93K
- **Number of tokens (Llama 3)**: 53.96M
- **Average document length in tokens (min, max)**: 252.22140730249103 (3, 1.11K)
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
Danish Foundation Models have a written agreement with DBC D1G1TAL regarding the use of the data for training and releasing models. 
Data will only be available at the entity during the project. Requests regarding access to the dataset should be directed to the data owner DBC D1G1TAL.

### Citation Information

No citation at the moment.
