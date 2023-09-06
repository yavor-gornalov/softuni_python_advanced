from project.movie_specification.movie import Movie
from project.user import User


class Thriller(Movie):
    DEFAULT_AGE_RESTRICTION = 16

    def __init__(self, title: str, year: int, owner: User, age_restriction: int):
        super().__init__(title, year, owner, age_restriction=Thriller.DEFAULT_AGE_RESTRICTION)
