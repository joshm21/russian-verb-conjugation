import conjugate


forms = {
    "presfut": [
        "presfut_sg1",
        "presfut_sg2",
        "presfut_sg3",
        "presfut_pl1",
        "presfut_pl2",
        "presfut_pl3",
    ],
    "imp": [
        "imperative_sg",
        "imperative_pl",
    ],
    "past": ["past_m", "past_n", "past_f", "past_pl"],
    "all": [
        "presfut_sg1",
        "presfut_sg2",
        "presfut_sg3",
        "presfut_pl1",
        "presfut_pl2",
        "presfut_pl3",
        "imperative_sg",
        "imperative_pl",
        "past_m",
        "past_n",
        "past_f",
        "past_pl",
    ],
}

presfut_endings = {
    "presfut_sg1": {"conj1": "ю", "conj2": "ю"},
    "presfut_sg2": {"conj1": "ешь", "conj2": "ишь"},
    "presfut_sg3": {"conj1": "ет", "conj2": "ит"},
    "presfut_pl1": {"conj1": "ем", "conj2": "им"},
    "presfut_pl2": {"conj1": "ете", "conj2": "ите"},
    "presfut_pl3": {"conj1": "ют", "conj2": "ят"},
}

imperative_endings = {
    "imperative_sg": {
        "vowel": "й",
        "consonant1": "и",
        "consonant2": "ь",
    },
    "imperative_pl": {
        "vowel": "йте",
        "consonant1": "ите",
        "consonant2": "ьте",
    },
}

past_endings = {
    "past_m": "л",
    "past_n": "ло",
    "past_f": "ла",
    "past_pl": "ли",
}
