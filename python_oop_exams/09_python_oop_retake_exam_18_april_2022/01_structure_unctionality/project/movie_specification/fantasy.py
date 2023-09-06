from project.movie_specification.movie import Movie
from project.user import User


class Fantasy(Movie):
    DEFAULT_AGE_RESTRICTION = 6

    def __init__(self, title: str, year: int, owner: User, age_restriction: int):
        super().__init__(title, year, owner, age_restriction=Fantasy.DEFAULT_AGE_RESTRICTION)
