from project.movie import Movie

from unittest import TestCase, main


class MovieTests(TestCase):
    def setUp(self) -> None:
        self.movie = Movie("The Godfather", 1972, 9.9)

    def test_constructor(self):
        self.assertEqual("The Godfather", self.movie.name)
        self.assertEqual(1972, self.movie.year)
        self.assertEqual(9.9, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_name_setter_to_raise_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.name = ""
        expected = "Name cannot be an empty string!"
        self.assertEqual(expected, str(ve.exception))

    def test_year_setter_to_raise_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.year = 1886
        expected = "Year is not valid!"
        self.assertEqual(expected, str(ve.exception))

    def test_add_actor(self):
        self.movie.add_actor("Al Pacino")
        self.assertEqual(["Al Pacino"], self.movie.actors)

    def test_add_actor_already_existing(self):
        self.movie.add_actor("Al Pacino")
        result = self.movie.add_actor("Al Pacino")
        expected = f"Al Pacino is already added in the list of actors!"
        self.assertEqual(expected, result)

    def test_gt_dunder(self):
        self.second_movie = Movie("The Godfather 2", 1976, 9.7)

        expected = '"The Godfather" is better than "The Godfather 2"'
        self.assertEqual(expected, self.movie > self.second_movie)

    def test_gt_dunder_for_movies_with_same_rating(self):
        self.second_movie = Movie("The Godfather 2", 1976, 9.9)

        expected = '"The Godfather 2" is better than "The Godfather"'
        self.assertEqual(expected, self.movie > self.second_movie)

    def test_representation_method(self):
        self.movie.add_actor("Al Pacino")
        self.movie.add_actor("Brando")
        expected = f"Name: The Godfather\n" \
                   f"Year of Release: 1972\n" \
                   f"Rating: 9.90\n" \
                   f"Cast: Al Pacino, Brando"
        self.assertEqual(expected, str(self.movie))

    if __name__ == "__main__":
        main()
