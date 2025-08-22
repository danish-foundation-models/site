---
pretty_name: DSK - IDA
language:
- da
license: other
license_name: DSK-1
task_categories:
- text-generation
- fill-mask
task_ids:
- language-modeling
domains:
- News
- Other
---

# Dataset Card for DSK - IDA

<!-- START-SHORT DESCRIPTION -->
A collection of newsletters, articles and other texts produced by IDA.
<!-- END-SHORT DESCRIPTION -->

This data has been contributed by IDA through the [Dansk Sprogmodel Konsortium](https://alexandra.dk/dsk).


## Dataset Description

<!-- START-DESC-STATS -->
- **Number of samples**: 40
- **Number of tokens (Llama 3)**: 417.32K
- **Average document length in tokens (min, max)**: 10.43K (341, 72.69K)
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
This data is licensed under the data sharing agreement made between the contributor and the Dansk Sprogmodel Konsortium (DSK). 
It allows DFM to use the data for training and releasing models, but prohibits DFM from releasing any of the data, except metadata describing the data. 

### Citation Information

There is currently no citation for this dataset.
