from abc import ABC


class Animal(ABC):
    def __init__(self, name: str, gender: str, age: int, money_for_care: int):
        self.name = name
        self.gender = gender
        self.age = age
        self.money_for_care = money_for_care

    def get_animal_type(self):
        return self.__class__.__name__

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"
