---
pretty_name: DBC D1G1TAL - Faktalink
language:
- da
license: other
license_name: Written agreement (public models, private data)
task_categories:
- text-generation
- fill-mask
task_ids:
- language-modeling
domains:
- Encyclopedic
---

# Dataset Card for DBC D1G1TAL - Faktalink

<!-- START-SHORT DESCRIPTION -->
dbc-faktalink consists of more than 5 hundred articles created by [DBC D1G1TAL](https://dbcdigital.dk/) (former Dansk Bibliotekscenter).
<!-- END-SHORT DESCRIPTION -->

All articles are written in Danish language. Instances that comprise this dataset represent articles on a variety of topics on aspects relevant to Danish society.
The dataset includes articles created between 1991 and 2024.

Descrition taken from [dbcdigital.dk](https://dbcdigital.dk/abonnementer-ydelser/faktalink/)

>Faktalink is a tool used by libraries and schools to provide factual knowledge on current, socially relevant, and historical topics. Through serious, trustworthy, and thoroughly researched articles, students and library users can gain a solid overview of various current and important subjects, as well as historical events.
>
>On Faktalink, you'll find articles on everything from politics and history to sports, culture, and much more. We prioritize topics that are relevant for school use and those with broader interest.
>
>There are around 500 articles and themes on Faktalink, and they are continuously updated with the latest information. Additionally, the site is regularly expanded with new, relevant articles and themes.




## Dataset Description

<!-- START-DESC-STATS -->
- **Number of samples**: 522
- **Number of tokens (Llama 3)**: 1.99M
- **Average document length in tokens (min, max)**: 3.81K (2, 18.77K)
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
Danish Foundation Models have a written agreement with DBC D1G1TAL regarding the use of the data for training and releasing models. 
Data will only be available at the entity during the project. Requests regarding access to the dataset should be directed to the data owner DBC D1G1TAL.

### Citation Information

No citation at the moment.
