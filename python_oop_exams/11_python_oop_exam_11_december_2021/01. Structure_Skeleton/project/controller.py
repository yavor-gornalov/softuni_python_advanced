from typing import List

from project.car.car import Car
from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    CAR_TYPES = {"MuscleCar": MuscleCar, "SportsCar": SportsCar}

    def __init__(self):
        self.cars: List[Car] = []
        self.drivers: List[Driver] = []
        self.races: List[Race] = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type not in self.CAR_TYPES:
            return
        if self.__find_car_by_type_and_model(car_type, model):
            raise Exception(f"Car {model} is already created!")

        new_car = self.CAR_TYPES[car_type](model, speed_limit)
        self.cars.append(new_car)
        return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        if self.__find_item_by_name(driver_name, self.drivers):
            raise Exception(f"Driver {driver_name} is already created!")

        new_driver = Driver(driver_name)
        self.drivers.append(new_driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        if self.__find_item_by_name(race_name, self.races):
            raise Exception(f"Race {race_name} is already created!")

        new_race = Race(race_name)
        self.races.append(new_race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = self.__find_item_by_name(driver_name, self.drivers)
        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")
        new_car = self.__find_last_free_car_by_type(car_type)
        if not new_car:
            raise Exception(f"Car {car_type} could not be found!")

        if driver.car is None:
            driver.car = new_car
            new_car.is_taken = True
            return f"Driver {driver_name} chose the car {new_car.model}."

        old_car = driver.car
        old_car.is_taken = False
        driver.car = new_car
        new_car.is_taken = True
        return f"Driver {driver_name} changed his car from {old_car.model} to {new_car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = self.__find_item_by_name(race_name, self.races)
        if not race:
            raise Exception(f"Race {race_name} could not be found!")

        driver = self.__find_item_by_name(driver_name, self.drivers)
        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        if driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if self.__find_item_by_name(driver.name, race.drivers):
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = self.__find_item_by_name(race_name, self.races)
        if not race:
            raise Exception(f"Race {race_name} could not be found!")

        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        result = []
        for driver in sorted(race.drivers, reverse=True)[:3]:
            result.append(f"Driver {driver.name} wins the {race_name} race with a speed of {driver.car.speed_limit}.")
            driver.win()

        return "\n".join(result)

    # HELPERS:
    def __find_car_by_type_and_model(self, car_type, model):
        return next((c for c in self.cars if c.car_type == car_type and c.model == model), None)

    def __find_last_free_car_by_type(self, car_type):
        car = None
        for current_car in self.cars:
            if current_car.car_type == car_type and not current_car.is_taken:
                car = current_car
        return car

    @staticmethod
    def __find_item_by_name(name, collection):
        return next((i for i in collection if i.name == name), None)
