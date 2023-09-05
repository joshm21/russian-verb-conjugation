class Verb:
    def __init__(self, accented_infinitive):
        self.accented = accented_infinitive.lower()
        self.bare = ""
        self.stem_pres = ""
        self.stem_past = ""
        self.verb_group = ""
        self.is_ending_accented = None
        self.is_reflexive = None
        self.conjugations = {"all word forms here"}
        self.categories = []
        self.parse_infinitive()

    def parse_infinitive(self):
        possible_endings = [
            # [ending, group, accented, reflexive, pres_remove, past_remove]
            # must be sorted descending by len(ending) for correct matching
            ["и'ться", "2", True, True, 6, 4],
            ["е'ться", "2", True, True, 6, 4],
            ["иться", "2", False, True, 5, 4],
            ["еться", "2", False, True, 5, 4],
            ["ться", "1", False, True, 4, 4],
            ["и'ть", "2", True, False, 4, 2],
            ["е'ть", "2", True, False, 4, 2],
            ["ить", "2", False, False, 3, 2],
            ["еть", "2", False, False, 3, 2],
            ["ть", "1", False, False, 2, 2],
        ]
        # on first match, use data from above to parse the verb
        for possibility in possible_endings:
            (ending, group, accented, reflexive, pres_remove, past_remove) = possibility
            if self.accented.endswith(ending):
                self.verb_group = group
                self.is_ending_accented = accented
                self.is_reflexive = reflexive
                self.stem_pres = self.accented[:-pres_remove]
                self.stem_past = self.accented[:-past_remove]
                return
        # if no matches, mark irregular and leave fields at default values
        self.verb_group = "irregular"

    def set_conjugation_strategy(self):
        pass

    def compare_conjugations_to_actual(self):
        pass


"""
    logging.debug(" - forming present/future and imperative conjugations")
    for ending in ENDINGS[verbGroup]:
        if isEndingAccented:
            # bug; should only work on group2 verbs
            newEnding = f"{ending[:1]}'{ending[1:]}"
            result.append(stem + newEnding)
        else:
            result.append(stem + ending)
"""
