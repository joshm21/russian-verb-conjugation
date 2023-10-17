import pandas as pd

words = pd.read_csv("russian3 - words.csv")[["id", "accented", "rank", "type"]]
forms = pd.read_csv("russian3 - words_forms.csv")[
    ["word_id", "form_type", "position", "form"]
]

verbs = words[words["type"] == "verb"]

merged = pd.merge(
    left=verbs, right=forms, how="left", left_on="id", right_on="word_id"
).drop(columns=["type", "word_id"])

merged["form"] = merged["form"].astype("str")
combine_forms = (
    merged.sort_values("position")
    .groupby(["id", "accented", "rank", "form_type"], sort=False, as_index=False)[
        "form"
    ]
    .agg("|".join)
)

pivot_form_type = combine_forms.pivot(
    index=["id", "accented", "rank"], columns="form_type", values="form"
).reset_index()

print(pivot_form_type.info())
print(pivot_form_type.head(50))
pivot_form_type.to_csv("verb_table.csv")
