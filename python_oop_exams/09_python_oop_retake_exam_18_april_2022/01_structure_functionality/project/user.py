class User:
    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
        self.movies_liked = []
        self.movies_owned = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value: str):
        if not value:
            raise ValueError("Invalid username!")
        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value: int):
        if value < 6:
            raise ValueError("Users under the age of 6 are not allowed!")
        self.__age = value

    def __str__(self):
        result = [f"Username: {self.username}, Age: {self.age}", "Liked movies:"]
        if not self.movies_liked:
            result.append("No movies liked.")
        else:
            liked_movies_collection = [m.details() for m in self.movies_liked]
            [result.append(m) for m in liked_movies_collection]
        result.append("Owned movies:")
        if not self.movies_owned:
            result.append("No movies owned.")
        else:
            owned_movies_collection = [m.details() for m in self.movies_owned]
            [result.append(m) for m in owned_movies_collection]
        return "\n".join(result)
