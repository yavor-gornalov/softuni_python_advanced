from typing import List

from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    registered_users = []

    def __init__(self):
        self.movies_collection: List[Movie] = []
        self.users_collection: List[User] = []

    def register_user(self, username: str, age: int):
        if username in self.registered_users:
            raise Exception("User already exists!")
        self.registered_users.append(username)
        new_user = User(username, age)
        self.users_collection.append(new_user)
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        if username not in self.registered_users:
            raise Exception("This user does not exist!")
        if not username == movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")

        user = self._get_user_by_username(username)
        movie.uploaded = True
        user.movies_owned.append(movie)
        self.movies_collection.append(movie)
        return f"{user.username} successfully added {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        user = self._get_user_by_username(username)
        error_message = self._check_user_owns_movie(user, movie)
        if error_message:
            raise Exception(error_message)
        movie.uploaded = False
        user.movies_owned.remove(movie)
        self.movies_collection.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        user = self._get_user_by_username(username)
        error_message = self._check_user_owns_movie(user, movie)
        if error_message:
            raise Exception(error_message)
        for key, value in kwargs.items():
            movie.title = value if key == "title" else movie.title
            movie.year = value if key == "year" else movie.year
            movie.age_restriction = value if key == "age_restriction" else movie.age_restriction

        return f"{username} successfully edited {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        user = self._get_user_by_username(username)
        if movie in user.movies_owned:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")
        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")
        movie.likes += 1
        user.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user = self._get_user_by_username(username)
        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")
        user.movies_liked.remove(movie)
        movie.likes -= 1
        return f"{user.username} disliked {movie.title} movie."

    def display_movies(self):
        if not self.movies_collection:
            return "No movies found."
        collection = [m.details() for m in sorted(self.movies_collection, key=lambda x: (-x.year, x.title))]
        return '\n'.join(collection)

    def __str__(self):
        usernames = [u.username for u in self.users_collection]
        titles = [m.title for m in self.movies_collection]
        collection = [
            f"All users: {', '.join(usernames)}" if usernames else "All users: No users.",
            f"All movies: {', '.join(titles)}" if titles else "All movies: No movies."
        ]
        return "\n".join(collection)

    # helpers
    def _get_user_by_username(self, username):
        collection = [u for u in self.users_collection if u.username == username]
        return collection[0] if collection else None

    @staticmethod
    def _check_user_owns_movie(user: User, movie: Movie):
        if not movie.uploaded:
            return  f"The movie {movie.title} is not uploaded!"
        if movie not in user.movies_owned:
            return f"{user.username} is not the owner of the movie {movie.title}!"
