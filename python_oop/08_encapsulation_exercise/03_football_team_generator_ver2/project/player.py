class Player:
    def __init__(self, name: str, sprint: int, dribble: int, passing: int, shooting: int):
        self.__name = name
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    def __eq__(self, other):
        return self.__name == other.__name

    def __str__(self):
        return f"""Player: {self.__name}
Sprint: {self.__sprint}
Dribble: {self.__dribble}
Passing: {self.__passing}
Shooting: {self.__shooting}"""

    @property
    def name(self):
        return self.__name
