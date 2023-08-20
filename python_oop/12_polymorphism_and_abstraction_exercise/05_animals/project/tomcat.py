from abc import ABC

from project.cat import Cat


class Tomcat(Cat, ABC):
    def __init__(self, name: str, age: int):
        super().__init__(name, age, "Male")

    def sound(self):
        return "Hiss"
