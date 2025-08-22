---
pretty_name: DBC D1G1TAL - Forfatterweb
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

# Dataset Card for DBC D1G1TAL - Forfatterweb

<!-- START-SHORT DESCRIPTION -->
dbc-forfatterweb consists of more than 1 thousand articles created by DBC D1G1TAL (former Dansk Bibliotekscenter).
<!-- END-SHORT DESCRIPTION -->

Forfatter web is a tool created by DBC D1G1TAL. Description from [dbcdigital.dk](https://dbcdigital.dk/abonnementer-ydelser/forfatterweb/)

> Forfatterweb is a tool for libraries and schools that provides factual knowledge about literature. With a wide array of thoroughly researched author portraits and themes, as well as introductions to literary genres and periods, Forfatterweb is your gateway to understanding books, authorships, and literary movements throughout history.
>
> Forfatterweb is a subscription service and can be used with either a Uni-Login or library login, as long as your school or library subscribes to Forfatterweb.

All articles are written in Danish language. Instances that comprise this dataset represent articles on Danish writers. 
The dataset includes articles created between 1991 and 2024.




## Dataset Description

<!-- START-DESC-STATS -->
- **Number of samples**: 1.19K
- **Number of tokens (Llama 3)**: 1.42M
- **Average document length in tokens (min, max)**: 1.20K (3, 14.44K)
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
