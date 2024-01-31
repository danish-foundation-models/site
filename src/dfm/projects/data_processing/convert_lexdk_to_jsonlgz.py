import datetime
import gzip
import io
import json
import tarfile
from pathlib import Path
from typing import Union


def main():
    input_path = Path("/work/raw_datasets/lexdk-raw.tar.gz")
    output_path = Path("/work/pre-training/lexdk/documents/lexdk_articles.jsonl.gz")

    with tarfile.open(input_path, "r:gz") as inputfile, gzip.open(
        output_path,
        "wt",
    ) as outputfile:
        extracted = inputfile.extractfile("lexdk_data/articles.jsonl")
        assert extracted is not None
        count = 0
        for idx, line in enumerate(io.TextIOWrapper(extracted, encoding="UTF-8")):
            obj = json.loads(line)

            metadata = {
                "url": obj["url"],
                "title": obj["title"],
                "authors": obj["authors"],
                "clarification": obj["clarification"],
            }
            new_obj: dict[str, Union[dict[str, str], str]] = {
                "id": str(idx),
                "text": obj["text"],
                "source": "lexdk",
                "added": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.000Z"),
                "created": obj["date"],
                "metadata": metadata,
            }
            json.dump(new_obj, outputfile)
            count += 1
        print("Wrote %d documents to %s" % (count, output_path))


if __name__ == "__main__":
    main()
