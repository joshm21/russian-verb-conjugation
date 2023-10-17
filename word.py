def last(word, n_chars):
    return word[-n_chars:]


def without_last(word, n_chars):
    return word[:-n_chars]


def insert_at(word, to_insert, n):
    return word[:n] + to_insert + word[n:]


def has_one_vowel(word):
    count = 0
    for letter in word:
        if is_vowel(letter):
            count += 1
    return count == 1


def with_stressed_vowel(word, n):
    bare = unstressed(word)
    vowel_indexes = []
    for i, letter in enumerate(bare):
        if is_vowel(letter):
            vowel_indexes.append(i)
    if len(vowel_indexes) == 0:
        # raise ValueError(f"No vowel found in {word}")
        return word
    target_index = vowel_indexes[n] + 1
    return insert_at(bare, "'", target_index).replace("е'", "ё")


def unstressed(word):
    return word.replace("'", "")


def is_reflexive(word):
    return last(word, 2) == "сь" or last(word, 2) == "ся"


def with_reflexive_ending(word):
    last_letter = last(unstressed(word), 1)
    if is_vowel(last_letter):
        return word + "сь"
    else:
        return word + "ся"


def with_consonant_mutation(inf_stem):
    mutations = {
        "п": "пл",
        "б": "бл",
        "ф": "фл",
        "в": "вл",
        "м": "мл",
        "т": "ч",
        "к": "ч",
        "д": "ж",
        "з": "ж",
        "г": "ж",
        "с": "ш",
        "х": "ш",
        "ст": "щ",
        "ск": "щ",
    }
    mutated = mutations.get(last(inf_stem, 1), False)
    if mutated:
        return without_last(inf_stem, 1) + mutated
    else:
        return inf_stem


def with_spelling_rule(word):
    result = word
    replacements = (
        ("гя", "га"),
        ("кя", "ка"),
        ("хя", "ха"),
        ("жя", "жа"),
        ("чя", "ча"),
        ("шя", "ша"),
        ("щя", "ща"),
        ("ця", "ца"),
        ("гю", "гу"),
        ("кю", "ку"),
        ("хю", "ху"),
        ("жю", "жу"),
        ("чю", "чу"),
        ("шю", "шу"),
        ("щю", "щу"),
        ("цю", "цу"),
    )
    for replacement in replacements:
        result = result.replace(replacement[0], replacement[1])
    return result


def is_vowel(letter):
    vowels = ["а", "у", "о", "ы", "э", "я", "ю", "ё", "и", "е"]
    return letter in vowels


def is_consonant(letter):
    return not is_vowel(letter)
