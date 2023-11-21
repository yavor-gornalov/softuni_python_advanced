from unittest import TestCase, main
from project.team import Team


class TestTeam(TestCase):
    def setUp(self) -> None:
        self.team = Team("Dream")
        self.second_team = Team("Team")

    def test_constructor(self):
        self.assertEqual("Dream", self.team.name)
        self.assertEqual({}, self.team.members)

    def test_name_setter_with_non_letter_char_in_name(self):
        ve = [None] * 4
        with self.assertRaises(ValueError) as ve[0]:
            self.team.name = "Team1"
        with self.assertRaises(ValueError) as ve[1]:
            self.team.name = " Team"
        with self.assertRaises(ValueError) as ve[2]:
            self.team.name = " "
        with self.assertRaises(ValueError) as ve[3]:
            self.team.name = "123"

        expected = "Team Name can contain only letters!"
        for error in ve:
            self.assertEqual(expected, str(error.exception))

    def test_add_member_new_member(self):
        result = self.team.add_member(**{"Ronaldo": 38, "Messi": 36})
        expected = "Successfully added: Ronaldo, Messi"
        self.assertEqual(result, expected)
        self.assertEqual({"Ronaldo": 38, "Messi": 36}, self.team.members)

    def test_add_new_member_and_existing_member(self):
        self.team.add_member(**{"Ronaldo": 38, "Messi": 36})
        result = self.team.add_member(**{"Messi": 36, "Levandovski": 34})
        expected = "Successfully added: Levandovski"
        self.assertEqual(result, expected)
        self.assertEqual({"Ronaldo": 38, "Messi": 36, "Levandovski": 34}, self.team.members)

    def test_remove_unknown_member(self):
        self.team.add_member(**{"Ronaldo": 38, "Messi": 36})
        result = self.team.remove_member("Levandovski")
        expected = "Member with name Levandovski does not exist"
        self.assertEqual(expected, result)
        self.assertEqual({"Ronaldo": 38, "Messi": 36}, self.team.members)

    def test_remove_existing_member(self):
        self.team.add_member(**{"Ronaldo": 38, "Messi": 36})
        result = self.team.remove_member("Messi")
        expected = "Member Messi removed"
        self.assertEqual(expected, result)
        self.assertEqual({"Ronaldo": 38}, self.team.members)

    def test_gt_dunder(self):
        self.assertFalse(self.team.__gt__(self.second_team))
        self.team.add_member(**{"Ronaldo": 38, "Messi": 36})
        self.assertTrue(self.team > self.second_team)
        self.assertFalse(self.team < self.second_team)

    def test_len_dunder(self):
        self.assertEqual(0, self.team.__len__())
        self.assertEqual(0, self.second_team.__len__())

        self.team.add_member(**{"Ronaldo": 38, "Messi": 36})

        self.assertEqual(2, len(self.team))
        self.assertEqual(0, len(self.second_team))

    def test_add_method(self):
        self.team.add_member(Ronaldo=38)
        self.second_team.add_member(Messi=36)

        dream_team = self.team + self.second_team

        self.assertEqual("DreamTeam", dream_team.name)
        self.assertEqual(2, len(dream_team))
        self.assertEqual({"Ronaldo": 38, "Messi": 36}, dream_team.members)

    def test_str_dunder_without_members(self):
        result = str(self.team)
        expected = "Team name: Dream"
        self.assertEqual(expected, result)

    def test_str_dunder_age_sort(self):
        self.team.add_member(**{"Ronaldo": 38, "Messi": 36})
        result = str(self.team)
        expected = """Team name: Dream
Member: Ronaldo - 38-years old
Member: Messi - 36-years old"""
        self.assertEqual(expected, result)

    def test_str_dunder_name_sort(self):
        self.team.add_member(**{"Ronaldo": 38, "Messi": 38})
        result = self.team.__str__()
        expected = """Team name: Dream
Member: Messi - 38-years old
Member: Ronaldo - 38-years old"""
        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
