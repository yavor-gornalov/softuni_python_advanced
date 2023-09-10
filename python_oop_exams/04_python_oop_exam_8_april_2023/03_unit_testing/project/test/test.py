from project.tennis_player import TennisPlayer

from unittest import TestCase, main


class TennisPlayerTests(TestCase):
    def setUp(self) -> None:
        self.player = TennisPlayer("Grisho", 32, 1000)

    def test_constructor(self):
        self.assertEqual("Grisho", self.player.name)
        self.assertEqual(32, self.player.age)
        self.assertEqual(1000, self.player.points)
        self.assertFalse(self.player.wins)

    def test_too_short_name_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.player.name = "Gr"
        expected = "Name should be more than 2 symbols!"
        self.assertEqual(expected, str(ve.exception))

    def test_age_under_limit_expect_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.player.age = 17
        expected = "Players must be at least 18 years of age!"
        self.assertEqual(expected, str(ve.exception))

    def test_adding_new_win_happy_path(self):
        self.player.add_new_win("Wimbledon")
        self.assertEqual("Wimbledon", *self.player.wins)

    def test_adding_new_win_of_existing_tournament(self):
        self.player.add_new_win("Wimbledon")
        result = self.player.add_new_win("Wimbledon")
        expected = "Wimbledon has been already added to the list of wins!"
        self.assertEqual(expected, result)

    def test_lt_dunder_other_player_is_better(self):
        self.other_player = TennisPlayer("Nadal", 36, 2000)
        result = self.player < self.other_player
        expected = "Nadal is a top seeded player and he/she is better than Grisho"
        self.assertEqual(expected, result)

    def test_lt_dunder_player_is_better_than_other(self):
        self.other_player = TennisPlayer("Nadal", 36, 750)
        result = self.player < self.other_player
        expected = "Grisho is a better player than Nadal"
        self.assertEqual(expected, result)

    def test_str_method(self):
        self.player.add_new_win("Wimbledon")
        self.player.add_new_win("Madrid")
        expected = """Tennis Player: Grisho
Age: 32
Points: 1000.0
Tournaments won: Wimbledon, Madrid"""
        self.assertEqual(expected, str(self.player))


if __name__ == "__main__":
    main()
