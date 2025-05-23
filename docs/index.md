# Empowering the Danish Language in the Digital Age

Welcome to the Danish Foundation Models (DFM) project, a pioneering initiative in the field of machine learning and natural language processing (NLP) dedicated to the Danish language. Our mission is to develop, maintain, and provide open access to high-quality foundation models tailored for Danish, promoting innovation and inclusivity in language technologies.

!!! abstract "Read the paper"

    You can read more about the argument for Danish Language models in our [publication](https://arxiv.org/abs/2311.07264).

## Why Danish Foundation Models?

### Bridging the Digital Language Divide

- **Global Gap**: The rise of large language models has transformed research and technology, but smaller languages like Danish risk falling behind both in development, evaluation and application.
- **Local Focus**: We combat this by focusing on the Danish language, ensuring that it is well-represented in the digital landscape.
- **Broad Collaboration**: Our project unites public and private institutions, ensuring high data quality and practical applicability of our models.

## Our Objectives

1. To develop and maintain **state-of-the-art language models for Danish** for applications within both text and speech.
2. To extensively **validate** foundation models for Danish in a representative set of tasks.
3. To maintain a high standard of **documentation** of models such as model cards \[[Mitchell et al., 2019](https://arxiv.org/abs/1810.03993)\] and datasheets \[[Gebru et al., 2021](https://cacm.acm.org/magazines/2021/12/256932-datasheets-for-datasets/abstract)\].
4. To **open-source** not only the models but also all components required for reproducibility such as pre-processing, training, and validation code.



## Open-source

###  Open-source Development with Privacy-Focused Data Handling

In our commitment to advancing open-source development, we strongly emphasise the ethical handling of data, particularly when it involves personally sensitive information or material under copyright. This ensures that we share as much as possible while protecting privacy.

To achieve this, our project is structured to differentiate between data that can be shared openly and that which cannot. 
This demarcation is documented through detailed datasheets and training logs, thereby ensuring transparency in our processes.

Additionally, we prioritise the security of the data during its processing and training phases. All data is stored on UCloud, a platform that upholds the recognised highest standards in information security management. This commitment to data security is exemplified by UCloud's adherence to ISO27001, a globally recognised standard, ensuring that our data handling practices meet rigorous international criteria. For more information on our security measures, please visit UCloud's security [documentation](https://docs.cloud.sdu.dk/intro/security.html).

![](_static/structure.png)

### Contributions

Besides our [models](https://www.foundationmodels.dk/models/) DFM has led to a series of positive open-source contributions, the following table include some of these contributions:


| Project                                                                                                                                                                                                                                                                            | Contribution                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Packages**                                                                                                                                                                                                                                                                       |                                                                                                     |
| [NLPDedup](https://github.com/saattrupdan/NLPDedup)                                                                                                                                                                                                                                | A deduplication library derived from DFM's deduplication code                                       |
| **Code contributions**                                                                                                                                                                                                                                                             |                                                                                                     |
| [TextDescriptives](https://hlasse.github.io/TextDescriptives/)                                                                                                                                                                                                                     | Added heuristic quality measure for texts                                                           |
| [dolma](https://github.com/allenai/dolma)                                                                                                                                                                                                                                          | Bugfixes and addition of taggers for filtering                                                      |
| **Benchmarks**                                                                                                                                                                                                                                                                     |                                                                                                     |
| [ScandEval](https://scandeval.com)                                                                                                                                                                                                                                                 | Co-contributors have significant contributions to developing NLU and NLG benchmarks for Scandinavian and Germanic languages |
| [Scandinavian Embedding Benchmark](https://kennethenevoldsen.github.io/scandinavian-embedding-benchmark/)                                                                                                                                                                          | The benchmark for evaluating Scandinavian embedding has been created as a part of DFM               |
| **Datasets**                                                                                                                                                                                                                                                                       |                                                                                                     |
| [m_arc](https://huggingface.co/datasets/alexandrainst/m_arc), [m_mmlu](https://huggingface.co/datasets/alexandrainst/m_mmlu), [m_hellaswag](https://huggingface.co/datasets/alexandrainst/m_hellaswag), [m_truthfulqa](https://huggingface.co/datasets/alexandrainst/m_truthfulqa) | Translated versions of English datasets intended for model evaluation for these domains             |


<!-- 
temp. removed (see DDSC slack channel: NLP)

| [dagw_reddit_filtered_v1.0.0](https://huggingface.co/datasets/DDSC/dagw_reddit_filtered_v1.0.0)                        | A filtered version of the Danish Gigaword, including reddit   | 
| **Lexical Resources**                                                                                                  |                                                               |
| [Detailed Word Frequencies](https://huggingface.co/collections/chcaa/danish-word-frequencies-65ba3f61875c73327d1691b2) | Detailed word frequencies across domain and pos-tags          |

-->

## Improving the Danish Language Technology Landscape

The Danish Foundations models is a collaboration across Danish universities and research organizations. The project engages with data science communities and initiatives ([Danish Data Science Community](https://danskdatascience.dk/)), to promote the development of Danish language tools. We continually gather information about how to improve the Danish language technologies and how to best support the community. If you want to highlight missing pieces in Danish NLP we invite you to open a thread on the [forum](https://github.com/centre-for-humanities-computing/danish-foundation-models/discussions/categories/missing-pieces-for-danish-nlp) stating the problems and potential solutions.

## Contributors

## The Core Team
Those with data access, who contribute to the project, including data management, model development, project management, and more.

From [the Center for Humanities Computing at Aarhus University](https://chc.au.dk/):

  - Kenneth Enevoldsen ([kenneth.enevoldsen@cas.au.dk](mailto:kenneth.enevoldsen@cas.au.dk))
 - Marton Kardos ([martonkardos@cas.au.dk](mailto:martonkardos@cas.au.dk))
  - Jan Kostkan ([jan.kostkan@cas.au.dk](mailto:jan.kostkan@cas.au.dk))
  - Peter Vahlstrup ([imvpbv@cc.au.dk](mailto:imvpbv@cc.au.dk))
  - Per Møldrup-Dalum ([per@cas.au.dk](mailto:per@cas.au.dk))
  - Kristoffer Laigaard Nielbo ([kln@cas.au.dk](mailto:kln@cas.au.dk))

From [the Alexandra Institute](https://alexandra.dk/):

  - Rasmus Larsen ([rasmus.larsen@alexandra.dk](mailto:rasmus.larsen@alexandra.dk))
  - Dan Saattrup Nielsen ([dan.nielsen@alexandra.dk](mailto:dan.nielsen@alexandra.dk))
  - Andreas Nugaard Holm ([andreas.holm@alexandra.dk](mailto:andreas.holm@alexandra.dk))
  - Kristian Nørgaaard Jensen ([kristian.n.jensen@alexandra.dk](mailto:kristian.n.jensen@alexandra.dk))
  - Torben Blach ([torben.blach@alexandra.dk](mailto:torben.blach@alexandra.dk))
  - Jens Kaas Benner ([jens.benner@alexandra.dk](mailto:jens.benner@alexandra.dk))

From [the Center for Machine Learning at the University of Southern Denmark](https://www.sdu.dk/en/forskning/machine-learning):

  - Peter Schneider-Kamp ([petersk@imada.sdu.dk](mailto:petersk@imada.sdu.dk))
  - Lukas Galke ([galke@imada.sdu.dk](mailto:galke@imada.sdu.dk))
  - Andrea Blasi Núñez ([abln@mmmi.sdu.dk](mailto:abln@mmmi.sdu.dk))
  - Gianluca Barmina ([gbarmina@imada.sdu.dk](mailto:gbarmina@imada.sdu.dk))
  - Jacob Nielsen ([jacn@imada.sdu.dk](mailto:jacn@imada.sdu.dk))
  - Mogens Henrik From ([from@imada.sdu.dk](mailto:from@imada.sdu.dk))
  - Stine Lyngsø Beltoft ([stinelb@imada.sdu.dk](mailto:stinelb@imada.sdu.dk))

From [the Department of Computer Science at the University of Copenhagen](https://di.ku.dk/):

  - Desmond Elliott ([de@di.ku.dk](mailto:de@di.ku.dk))

From [Center for Sprogteknologi at the University of Copenhagen](https://cst.ku.dk):

  - Bolette Sandford Pedersen ([bspedersen@hum.ku.dk]((mailto:bspedersen@hum.ku.dk))
  - Ali Basirat ([alib@hum.ku.dk](mailto:alib@hum.ku.dk))

<details>
<summary>Project Alumnis</summary>
<br>

Lasse Hansen, Martin Bernstorff, Tao Tang

</details>


### Core Contributors
Those without data access, but who have contributed substantially to the project including code contributions, model development, and experiment planning.

From [Alvenir](https://www.alvenir.ai/):

  - Martin Carsten Nielsen ([martin@alvenir.ai](martin@alvenir.ai))
  - Søren Vejlgaard Holm ([swh@alvenir.ai](swh@alvenir.ai))

## Join Us

We invite collaboration and contributions from industry professionals, researchers, and the open-source community. Together, we can advance the field of Danish NLP and create a more inclusive digital future. You can reach out to us using the following channels:


|                                                                                                                                                                         |                                                                                                                            |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| :octicons-people-24: - [**DDSC Slack**](https://join.slack.com/t/danskdatascie-o8m9638/shared_invite/zt-1jh2dwmj4-D_mjywfXERvVP75n9O0ykg)                               | Join the discussion in the "danish-foundation-models-text"-channel                                                         |
| :octicons-comment-discussion-24: -  [**GitHub Discussion**](https://github.com/centre-for-humanities-computing/danish-foundation-models/discussions)                    | Ask questions or start a discussion                                                                                        |
| :octicons-issue-tracks-24: - [**GitHub Issues**](https://github.com/centre-for-humanities-computing/danish-foundation-models/issues)                                    | Noticed a bug in the code? Please create an issue                                                                          |
| :octicons-feed-rocket-16: - [**Using the model?**](https://github.com/centre-for-humanities-computing/danish-foundation-models/discussions/categories/using-our-models) | If you use the model, let us know it makes it easier for us to apply for funding and justify the devopment of the project. |

[Contact us :fontawesome-solid-paper-plane:](mailto:kenneth.enevoldsen@cas.au.dk){ .md-button }
