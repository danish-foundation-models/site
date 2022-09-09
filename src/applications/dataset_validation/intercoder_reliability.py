"""Calculates summary statistics and intercoder reliability.

Requries:
    $ pip install pandas sklearn wasabi

Autogenerated a markdown at /docs/intercoder_reliability.md.
"""

from pathlib import Path

import pandas as pd
from sklearn.metrics import cohen_kappa_score
from wasabi import MarkdownRenderer

md = MarkdownRenderer()

parent_folder = Path(__file__).parent.parent.parent.parent
data_path = parent_folder / "data" / "tagging"
docs_path = parent_folder / "docs"


# taggers
taggers = {x.stem: pd.read_csv(x) for x in data_path.glob("*.csv")}

md.add(md.title(1, "Results from corpus tagging"))


md.add(
    """
Each user tagged 100 documents (unless otherwise specified). Each document were tagged
on a per "sentence" basis. A "sentence" is defined by a newline split. "sentences", longer
that 1000 characters were split into multiple sentences of 1000 characters or less.

This tagging scheme similar to 
([Kreutzer et al., 2022](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00447/109285/Quality-at-a-Glance-An-Audit-of-Web-Crawled)).

Each tag where put into one of the following categories:
    """
)
md.add("- `wrong_language`: Not Danish")
md.add("- `skipped`: Unsure of category")
md.add(
    "- `correct_language`: Danish text where at least 80\% of the text is reasonable "
    + "sentences."
)
md.add(
    "- `not_language`: Text where less than 80\% of the text is reasonable sentences."
    + " Takes priority over wrong_language."
)

md.add(
    """
Additionally, each sentence was marked as being pornographic and/or offensive.
    """
)

md.add(md.title(2, "Text proportions"))
md.add("----")


def get_proportions(taggers, md):
    # examine proportion of texts that are porn/hate/correct language:
    for tagger in taggers:
        tagger_name, _, session_n, __, n_docs, date = tagger.split("_")
        df = taggers[tagger]

        md.add(f"**{tagger_name}** (Session: {session_n})")
        md.add(
            f"- *Date: {date}*"
            + f"\n- *Sentences tagged: {len(df)}*"
            + f"\n- *Documents tagged: {n_docs}*"
        )

        n_char = sum(len(t) for t in df["text"].values)
        t = "Proportions:\n"
        for cat in sorted(df["category"].unique()):
            cat_text = df["text"][df["category"] == cat].values
            n_char_cat = sum(len(t) for t in cat_text)
            t += f"\n- {n_char_cat/n_char*100:.2f}% of characters is `{cat}`"

        cat_text = df["text"][df["is_porn"] == True].values
        n_char_cat = sum(len(t) for t in cat_text)
        t += f"\n- {n_char_cat/n_char*100:.2f}% of characters is porn"

        cat_text = df["text"][df["is_offensive"] == True].values
        n_char_cat = sum(len(t) for t in cat_text)
        t += f"\n- {n_char_cat/n_char*100:.2f}% of characters is offensive"
        md.add(t)
    return md


md = get_proportions(taggers, md)


md.add(md.title(2, "Intercoder Reliability"))
md.add("----")

# create all possible pairs
pairs = []
for i, tagger in enumerate(taggers):
    for other_tagger in list(taggers)[i + 1 :]:
        pairs.append((tagger, other_tagger))

# calculate intercoder reliability
for pair in pairs:
    tagger1, tagger2 = pair
    tagger1_name, _, session_n1, __, n_docs1, date1 = tagger1.split("_")
    tagger2_name, _, session_n2, __, n_docs2, date2 = tagger2.split("_")
    md.add(
        f"**{tagger1_name}** (Session: {session_n1}) vs **{tagger2_name}** - (Session: {session_n2})"
    )
    # merge
    df = pd.merge(taggers[pair[0]], taggers[pair[1]], on="text", suffixes=("_1", "_2"))
    kappa = cohen_kappa_score(df["category_1"], df["category_2"])
    md.add(
        f"- Cohen's Kappa (all categories): {kappa:.4f} (Overlap in sentences: {df.shape[0]})"
    )

    kappa = cohen_kappa_score(
        df["category_1"] == "correct_language", df["category_2"] == "correct_language"
    )
    md.add(
        f"- Cohen's Kappa (correct vs not): {kappa:.4f} (Overlap in sentences: {df.shape[0]})"
    )


# comparison with mc4
md.add(md.title(2, "Comparison with mC4"))
md.add("-----")

md.add(
    "*Note*: mC4 did have a high degree of repititious texts. Similarly it did when texts blocks where not language they were often something like:"
)
example = """2lineStart%22%3A%22%22%2C%22placeholder%22%3A1%2C%22extName%22%3A%22nowiki%22%7D"" class=""placeholder placeholder-ext"" contenteditable=""false"">]&#x200b;</span></a></sup>&#x200b;</span>, at en lurifaks som Jimmy page, bruger MIT navn til opfindelsen! SV<span data-rte-instance=""1524-12953202845f3523698f3f1"" data-rte-meta=""%7B%22type%22%3A%22ext%22%2C%22wikitext%22%3A%22%3Cref%3ESVIN%3C%5C%2Fref%3E%22%2C%22lineStart%22%3A%22%22%2C%22placeholder%22%3A1%2C%22extName%22%3A%22ref%22%7D"" class=""placeholder placeholder-ext"" contenteditable=""false""><sup data-rte-washtml=""1"" id=""cite_ref-2"" class=""reference"" data-rte-attribs="" """

md.add(f"```{example}```")

md.add(
    "While non-language texts in NAT was often menu bars, contact information, or navigation."
)

data_path_mc4 = data_path / "mc4"

taggers_mc4 = {x.stem: pd.read_csv(x) for x in data_path_mc4.glob("*.csv")}
md = get_proportions(taggers_mc4, md)

print(md.text)

# write to file
with open(docs_path / "intercoder_reliability.md", "w") as f:
    f.write(md.text)
