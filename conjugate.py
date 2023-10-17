import data
import word


def deduce_stem(inf, form):
    if word.last(inf, 2) != "ть":
        return None  # can't guess stem

    is_form_past = form in data.forms["past"]
    if is_form_past:
        return word.without_last(inf, 2)
    else:
        if word.last(inf, 3) == "ить":
            return word.without_last(inf, 3)
        elif word.last(inf, 4) == "и'ть":
            return word.without_last(inf, 4)
        else:
            return word.without_last(inf, 2)


def deduce_ending(inf, form, stem):
    is_form_past = form in data.forms["past"]
    if is_form_past:
        return data.past_endings[form]

    is_form_presfut = form in data.forms["presfut"]
    if is_form_presfut:
        if word.last(word.unstressed(inf), 3) == "ить":
            return data.presfut_endings[form]["conj2"]
        else:
            return data.presfut_endings[form]["conj1"]

    is_form_imp = form in data.forms["imp"]
    if is_form_imp:
        # https://therussianblog.wordpress.com/2018/10/03/commands-the-imperative-mood/
        is_stem_stressed = "'" in stem
        bare = word.unstressed(stem)
        is_last_letter_consonant = word.is_consonant(word.last(bare, 1))
        is_2nd_last_letter_consonant = word.is_consonant(bare[-2:-1])

        if is_last_letter_consonant:
            if is_2nd_last_letter_consonant or not is_stem_stressed:
                return data.imperative_endings[form]["consonant1"]
            else:
                return data.imperative_endings[form]["consonant2"]
        else:
            return data.imperative_endings[form]["vowel"]

    raise IndexError(f"Invalid conjugation form: {form}")


def conjugate_all_forms(infinitive, dict_of_kwargs={}):
    result = {}
    for form in data.forms["all"]:
        result[form] = conjugate_form(infinitive, form, **dict_of_kwargs.get(form, {}))
    return result


def conjugate_form(
    infinitive,
    form,
    stem_func=deduce_stem,
    ending_func=deduce_ending,
    consonant_mutation=True,
    stress_shift=False,
    spelling_rule=True,
    # ova verbs
):
    # normalize infinitive
    inf = infinitive
    if word.has_one_vowel(infinitive):
        inf = word.with_stressed_vowel(inf, 0)
    if word.is_reflexive(infinitive):
        inf = word.without_last(inf, 2)

    # get stem
    stem = stem_func(inf, form)
    if stem == None:
        return "can't deduce stem"
    if consonant_mutation:
        stem = word.with_consonant_mutation(stem)
    is_stem_stressed = "'" in stem
    stem_should_be_stressed = stress_shift and not is_stem_stressed
    if stem_should_be_stressed:
        stem = word.with_stressed_vowel(stem, -1)

    # get ending
    ending = ending_func(inf, form, stem)
    ending_should_be_stressed = (stress_shift and is_stem_stressed) or (
        not stress_shift and not is_stem_stressed
    )
    if ending_should_be_stressed:
        ending = word.with_stressed_vowel(ending, 0)
    if word.is_reflexive(infinitive):
        ending = word.with_reflexive_ending(ending)

    # conjugate
    conjugation = stem + ending
    if spelling_rule:
        conjugation = word.with_spelling_rule(conjugation)
    return conjugation


if __name__ == "__main__":
    print(conjugate_all_forms("по'мнить"))
    # make sure to include stress mark
