import unittest
from verb import Verb


class TestVerb(unittest.TestCase):
    def test_parse_irregular(self):
        irregular = Verb("идти'")
        self.assertEqual(irregular.verb_group, "irregular")

    def test_parse_group_1_nonreflexive(self):
        group_1_nonreflexive = Verb("чита'ть")
        self.assertEqual(group_1_nonreflexive.verb_group, "1")
        self.assertEqual(group_1_nonreflexive.is_ending_accented, False)
        self.assertEqual(group_1_nonreflexive.is_reflexive, False)
        self.assertEqual(group_1_nonreflexive.stem_pres, "чита'")
        self.assertEqual(group_1_nonreflexive.stem_past, "чита'")

    def test_parse_group_2_unaccented_nonreflexive(self):
        group_2_unaccented_nonreflexive = Verb("ви'деть")
        self.assertEqual(group_2_unaccented_nonreflexive.verb_group, "2")
        self.assertEqual(group_2_unaccented_nonreflexive.is_ending_accented, False)
        self.assertEqual(group_2_unaccented_nonreflexive.is_reflexive, False)
        self.assertEqual(group_2_unaccented_nonreflexive.stem_pres, "ви'д")
        self.assertEqual(group_2_unaccented_nonreflexive.stem_past, "ви'де")

    def test_parse_group_2_accented_nonreflexive(self):
        group_2_accented_nonreflexive = Verb("говори'ть")
        self.assertEqual(group_2_accented_nonreflexive.verb_group, "2")
        self.assertEqual(group_2_accented_nonreflexive.is_ending_accented, True)
        self.assertEqual(group_2_accented_nonreflexive.is_reflexive, False)
        self.assertEqual(group_2_accented_nonreflexive.stem_pres, "говор")
        self.assertEqual(group_2_accented_nonreflexive.stem_past, "говори'")

    def test_parse_group_1_reflexive(self):
        group_1_reflexive = Verb("начина'ться")
        self.assertEqual(group_1_reflexive.verb_group, "1")
        self.assertEqual(group_1_reflexive.is_ending_accented, False)
        self.assertEqual(group_1_reflexive.is_reflexive, True)
        self.assertEqual(group_1_reflexive.stem_pres, "начина'")
        self.assertEqual(group_1_reflexive.stem_past, "начина'")

    def test_parse_group_2_unaccented_reflexive(self):
        group_2_unaccented_reflexive = Verb("уда'риться")
        self.assertEqual(group_2_unaccented_reflexive.verb_group, "2")
        self.assertEqual(group_2_unaccented_reflexive.is_ending_accented, False)
        self.assertEqual(group_2_unaccented_reflexive.is_reflexive, True)
        self.assertEqual(group_2_unaccented_reflexive.stem_pres, "уда'р")
        self.assertEqual(group_2_unaccented_reflexive.stem_past, "уда'ри")

    def test_group_2_accented_reflexive(self):
        group_2_accented_reflexive = Verb("учи'ться")
        self.assertEqual(group_2_accented_reflexive.verb_group, "2")
        self.assertEqual(group_2_accented_reflexive.is_ending_accented, True)
        self.assertEqual(group_2_accented_reflexive.is_reflexive, True)
        self.assertEqual(group_2_accented_reflexive.stem_pres, "уч")
        self.assertEqual(group_2_accented_reflexive.stem_past, "учи'")


if __name__ == "__main__":
    unittest.main()
