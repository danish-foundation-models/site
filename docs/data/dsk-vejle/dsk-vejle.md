---
pretty_name: DSK - Vejle Kommune
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
- Web
---

# Dataset Card for DSK - Vejle Kommune

<!-- START-SHORT DESCRIPTION -->
A collection of crawled webpages that is managed by Vejle Kommune. Contains various information, covering everything from tourists to garbage collection to historical knowledge of the area. 
<!-- END-SHORT DESCRIPTION -->

The data have been crawled from 8 different domains:
- [kyst-kyststien.dk](https://kyst-kyststien.dk) 
- [voresressourcer.dk](https://voresressourcer.dk) 
- [vejlesfolkemoede.dk](https://vejlesfolkemoede.dk)
- [vejle.dk](https://vejle.dk)
- [vejlewiki.dk](https://vejlewiki.dk)
- [vejlestadsarkiv.dk](https://vejlestadsarkiv.dk)
- [vejlebrandvaesen.dk](https://vejlebrandvaesen.dk)
- [nyrosborg.dk](https://nyrosborg.dk)

This data has been contributed by Vejle Kommune through the [Dansk Sprogmodel Konsortium](https://alexandra.dk/dsk). 


## Dataset Description

<!-- START-DESC-STATS -->
- **Number of samples**: 16.77K
- **Number of tokens (Llama 3)**: 27.99M
- **Average document length in tokens (min, max)**: 1.67K (11, 651.44K)
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
This data is licensed under the data sharing agreement made between the contributor and the Dansk Sprogmodel Konsortium (DSK). 
It allows DFM to use the data for training and releasing models, but prohibits DFM from releasing any of the data, except metadata describing the data. 

### Citation Information

There is currently no citation for this dataset.
