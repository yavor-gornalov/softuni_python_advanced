from project.animal import Animal


class Lion(Animal):
    __MONEY_FOR_CARE = 50

    def __init__(self, name: str, gender: str, age: int):
        super().__init__(name, gender, age, Lion.__MONEY_FOR_CARE)
