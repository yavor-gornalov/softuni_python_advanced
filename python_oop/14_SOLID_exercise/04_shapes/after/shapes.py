from abc import ABC, abstractmethod
from typing import List


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def calculate_area(self):
        return self.side_a * self.side_b


class Triangle(Shape):
    def __init__(self, side, height):
        self.side = side
        self.height = height

    def calculate_area(self):
        return (self.side * self.height) / 2


class AreaCalculator:
    def __init__(self, shapes: List[Shape]):
        self.shapes = shapes

    @property
    def shapes(self):
        return self.__shapes

    @shapes.setter
    def shapes(self, value):
        for shape in value:
            if not isinstance(shape, Shape):
                raise AssertionError(f"`shapes` should be of type `{Shape.__name__}`.")
        self.__shapes = value

    @property
    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.calculate_area()
        return total


shapes = [Rectangle(1, 6), Triangle(2, 3)]
calculator = AreaCalculator(shapes)
print("The total area is: ", calculator.total_area)
