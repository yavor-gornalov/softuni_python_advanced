from project.car.car import Car


class Driver:
    def __init__(self, name: str):
        self.name = name
        self.car = None
        self.number_of_wins: int = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value.strip():
            raise ValueError("Name should contain at least one character!")
        self.__name = value

    def win(self):
        self.number_of_wins += 1

    def attach_car(self, new_car: Car):
        old_car = self.car
        if old_car:
            old_car.is_taken = False
        self.car = new_car
        new_car.is_taken = True
        return old_car

    def __gt__(self, other):
        return self.car.speed_limit > other.car.speed_limit
