import pandas as pd

def main():
    verbs = pd.read_csv("russian3 - verbs.csv",
                        usecols=["word_id"])
    words = pd.read_csv("russian3 - words.csv",
                        usecols=["id", "bare", "accented"])
    forms = pd.read_csv("russian3 - words_forms.csv",
                        usecols=["word_id", "form_type", "position", "form"])

    forms = forms.loc[forms["form_type"].str.startswith("ru_verb")]
    forms["form"] = forms["form"].astype("string")
    forms = forms.fillna("").pivot_table(index="word_id",
                                         columns="form_type",
                                         values="form",
                                         aggfunc=lambda x: "; ".join(x)).reset_index()

    result = pd.merge(verbs, words, how="left",
                      left_on="word_id", right_on="id").drop('id', axis=1)
    result = pd.merge(result, forms, how="left")

    result.to_csv("actual_conjugations.csv")


if __name__ == "__main__":
    main()
