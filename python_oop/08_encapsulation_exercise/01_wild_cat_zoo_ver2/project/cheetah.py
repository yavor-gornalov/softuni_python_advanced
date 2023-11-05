from project.animal import Animal


class Cheetah(Animal):
    __MONEY_FOR_CARE = 60

    def __init__(self, name: str, gender: str, age: int):
        super().__init__(name, gender, age, Cheetah.__MONEY_FOR_CARE)
