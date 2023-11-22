from unittest import TestCase, main
from project.team import Team


class TestTeam(TestCase):
    def setUp(self) -> None:
        self.team = Team("Dream")
        self.team.members = {"Peter": 21, "George": 23}

        self.team2 = Team("Team")
        self.team2.members = {"John": 22, "Tom": 23}

        self.new_team = self.team + self.team2

    def test_constructor(self):
        new_team = Team("NewTeam")
        self.assertEqual("NewTeam", new_team.name)
        self.assertEqual({}, new_team.members)

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

    def test_add_member_already_added(self):
        result = self.team.add_member(**{"George": 22, "Peter": 23})
        expected = "Successfully added: "
        self.assertEqual(result, expected)
        self.assertEqual({"Peter": 21, "George": 23}, self.team.members)

    def test_add_new_members(self):
        result = self.team.add_member(**{"Peter": 23, "John": 22, "Tom": 23})
        expected = "Successfully added: John, Tom"
        self.assertEqual(result, expected)
        self.assertEqual({"Peter": 21, "George": 23, "John": 22, "Tom": 23}, self.team.members)

    def test_remove_unknown_member(self):
        result = self.team.remove_member("Tom")
        expected = "Member with name Tom does not exist"
        self.assertEqual(expected, result)

    def test_remove_existing_member(self):
        result = self.team2.remove_member("Tom")
        expected = "Member Tom removed"
        self.assertEqual(expected, result)

    def test_gt_dunder_with_equal_team_members_count(self):
        self.team2.remove_member("Tom")
        self.assertEqual(True, self.team > self.team2)
        self.assertEqual(False, self.team < self.team2)

    def test_len_dunder(self):
        self.assertEqual(2, len(self.team2))
        self.team2.remove_member("Tom")
        self.assertEqual(1, len(self.team2))
        self.team2.remove_member("John")
        self.assertEqual(0, len(self.team2))

    def test_add_method(self):
        self.new_team = self.team + self.team2
        self.assertEqual("DreamTeam", self.new_team.name)
        self.assertEqual(4, len(self.new_team))
        self.assertTrue(self.new_team > self.team)
        self.assertEqual({"Peter": 21, "George": 23, "John": 22, "Tom": 23}, self.new_team.members)

    def test_add_method_with_same_members(self):
        self.team3 = Team("TeamCopy")
        self.team3.add_member(**{"Peter": 21, "George": 23})
        self.new_team = self.team + self.team3
        self.assertEqual("DreamTeamCopy", self.new_team.name)
        self.assertEqual(2, len(self.new_team))
        self.assertEqual({"Peter": 21, "George": 23}, self.new_team.members)

    def test_str_dunder(self):
        result = str(self.new_team)
        expected = """Team name: DreamTeam
Member: George - 23-years old
Member: Tom - 23-years old
Member: John - 22-years old
Member: Peter - 21-years old"""
        self.assertEqual(expected, result)

        self.new_team.add_member(**{"Adam": 23, "Evans": 21})
        resul2 = str(self.new_team)
        expected2 = """Team name: DreamTeam
Member: Adam - 23-years old
Member: George - 23-years old
Member: Tom - 23-years old
Member: John - 22-years old
Member: Evans - 21-years old
Member: Peter - 21-years old"""
        self.assertEqual(expected2, resul2)

    def test_str_dunder_without_members(self):
        result = str(Team("Empty"))
        expected = "Team name: Empty"
        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
