

This section gives an overview of the models available through the DFM project. The
models are available through the [Huggingface model
hub](https://huggingface.co/danish-foundation-models). To avoid duplicating information
surrounding the models and the information regarding the models are available at the
models model sheet.


!!! tip "Model recommendations"

    Danish foundation models maintains a list of [state-of-the-art recommendations](https://huggingface.co/collections/danish-foundation-models/state-of-the-art-danish-models)
    This list is updated approximately once per year to reflect the best available models for various tasks in Danish language and speech processing.

## Text Models

| Model                                                                                               | Model type | Size (parameters) |
| --------------------------------------------------------------------------------------------------- | ---------- | ----------------- |
| [munin-7b-alpha](https://huggingface.co/danish-foundation-models/munin-7b-alpha)                    | Decoder    | 7.24B             |
| [dfm-sentence-encoder-large](https://huggingface.co/KennethEnevoldsen/dfm-sentence-encoder-large)   | Encoder    | large (355M)      |
| [dfm-sentence-encoder-medium](https://huggingface.co/KennethEnevoldsen/dfm-sentence-encoder-medium) | Encoder    | medium (110M)     |


??? note "Previously released models"

    Previously the DFM project released the following text models, however these models were taken down due to copyright concerns.
    Preventative measures have been taken to ensure that future models do not have the same issues.

    | Model                                                                                  | Model type | Size (parameters) |
    | -------------------------------------------------------------------------------------- | ---------- | ----------------- |
    | [encoder-large-v1](https://huggingface.co/danish-foundation-models/encoder-large-v1)   | Encoder    | large (355M)      |
    | [encoder-medium-v1](https://huggingface.co/danish-foundation-models/encoder-medium-v1) | Encoder    | medium (110M)     |
    | [encoder-small-v1](https://huggingface.co/danish-foundation-models/encoder-small-v1)   | Encoder    | small (22M)       |

    Similarly the DFM project previously released the following speech models which were also taken down due to copyright concerns.

    | Model                                                                               | Model type                   |
    | ----------------------------------------------------------------------------------- | ---------------------------- |
    | [xls-r-300m-danish](https://huggingface.co/chcaa/xls-r-300m-danish)                 | Pretrained wav2vec2.0 model  |
    | [xls-r-300m-danish-nst-cv9](https://huggingface.co/chcaa/xls-r-300m-danish-nst-cv9) | Automatic speech recognition |
    | [chcaa/xls-r-300m-nst-cv9-da](https://huggingface.co/chcaa/xls-r-300m-nst-cv9-da)   | Automatic speech recognition |

    We refer to our [state-of-the-art model recommendations](https://huggingface.co/collections/danish-foundation-models/state-of-the-art-danish-models)
    for an best alternatives to these models.
