from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @staticmethod
    @abstractmethod
    def animal_sound():
        pass

    def __repr__(self):
        return f"Animal: {self.__class__.__name__} - Sound: {self.animal_sound()} "


class Dog(Animal):
    @staticmethod
    def animal_sound():
        return 'woof-woof'


class Cat(Animal):
    @staticmethod
    def animal_sound():
        return 'meow'


class Tiger(Animal):
    @staticmethod
    def animal_sound():
        return 'ROAR!'


animals = [Cat("cat"), Dog("dog"), Tiger("tiger")]
for animal in animals:
    print(animal)

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
