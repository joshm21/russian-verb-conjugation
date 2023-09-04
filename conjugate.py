import logging


def one(accented_infinitive):
    logging.debug(f"conjugating {accented_infinitive}...")

    ENDINGS = {
        # present/future (6) + imperative (2)
        "group1": ["ю", "ешь", "ет", "ем", "ете", "ют", "й", "йте"],
        # present/future (6) + imperative (2)
        "group2": ["у", "ишь", "ит", "им", "ите", "ут", "и", "ите"],
        "past": ["л", "ла", "ло", "ли"],  # past (4)
        # past (4) + present/future (6) + imperative (2)
        "reflexive": ["ся", "сь", "сь", "сь", "сь", "ся", "ся", "ся", "сь", "ся", "ся", "сь"]
    }
    result = []
    stem = accented_infinitive
    isReflexive = False
    isEndingAccented = False
    verbGroup = ""

    if (stem.endswith("ся")):
        stem = stem[:-2]
        isReflexive = True
        logging.debug(f" - reflexive verb; removing ся; new stem = {stem}")

    if (not stem.endswith("ть")):
        logging.debug(" - irregular infinitive; doesn't end in -ть")
        return None
    else:
        stem = stem[:-2]
        logging.debug(f" - removing ть; new stem = {stem}")

    logging.debug(" - forming past tense conjugations")
    for ending in ENDINGS["past"]:
        result.append(stem + ending)

    if (stem.endswith("'")):
        isEndingAccented = True
        stem = stem[:-1]
        logging.debug(f" - accented ending; new stem = {stem}")

    if (stem.endswith("и") or stem.endswith("е")):
        verbGroup = "group2"
        stem = stem[:-1]
        logging.debug(f" - group two verb; new stem = {stem}")
    else:
        verbGroup = "group1"
        logging.debug(" - group one verb")

    logging.debug(" - forming present/future and imperative conjugations")
    for ending in ENDINGS[verbGroup]:
        if isEndingAccented:
            newEnding = f"{ending[:1]}'{ending[1:]}"
            result.append(stem + newEnding)
        else:
            result.append(stem + ending)

    if isReflexive:
        logging.debug(" - adding reflexive endings to conjugations")
        for ndx in range(len(result)):
            result[ndx] += ENDINGS["reflexive"][ndx]

    return result


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
#    print(one("говори'ть"))
#    print(one("учи'ться"))
#    print(one("е'хать"))
    print(one("смотре'ть"))
