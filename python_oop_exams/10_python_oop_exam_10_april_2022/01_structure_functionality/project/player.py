class Player:
    player_names: list = []

    def __init__(self, name: str, age: int, stamina: int = 100):
        self.name = name
        self.age = age
        self.stamina = stamina

    def __lt__(self, other):
        return self.stamina < other.stamina

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        # TODO check if strip method usage needed
        if not value.strip():
            raise ValueError("Name not valid!")
        if value in self.player_names:
            raise Exception(f"Name {value} is already used!")
        self.player_names.append(value)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value: int):
        if value < 12:
            raise ValueError("The player cannot be under 12 years old!")
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value: int):
        if value < 0 or value > 100:
            raise ValueError("Stamina not valid!")
        self.__stamina = value

    @property
    def need_sustenance(self):
        return self.stamina < 100

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"


if __name__ == "__main__":
    try:
        first_player = Player('Peter', 15)
        second_player = Player('Lilly', 12, 94)
        third_player = Player('Lilly', 12, 94)
    except Exception as ex:
        print(str(ex))
    print(Player.__player_names)
