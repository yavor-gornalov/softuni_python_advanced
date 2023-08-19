from abc import ABC, abstractmethod


class Vehicle(ABC):
    ADDITIONAL_CONSUMPTION = 0
    TANK_FILLING_CAPACITY = 1

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    ADDITIONAL_CONSUMPTION = 0.9
    TANK_FILLING_CAPACITY = 1

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        needed_fuel = distance * (self.fuel_consumption + self.ADDITIONAL_CONSUMPTION)
        if needed_fuel <= self.fuel_quantity:
            self.fuel_quantity -= needed_fuel
        return self.fuel_quantity

    def refuel(self, fuel):
        refueled_quantity = fuel * self.TANK_FILLING_CAPACITY
        self.fuel_quantity += refueled_quantity
        return self.fuel_quantity


class Truck(Vehicle):
    ADDITIONAL_CONSUMPTION = 1.6
    TANK_FILLING_CAPACITY = 0.95

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        needed_fuel = distance * (self.fuel_consumption + self.ADDITIONAL_CONSUMPTION)
        if needed_fuel <= self.fuel_quantity:
            self.fuel_quantity -= needed_fuel
        return self.fuel_quantity

    def refuel(self, fuel):
        refueled_quantity = fuel * self.TANK_FILLING_CAPACITY
        self.fuel_quantity += refueled_quantity
        return self.fuel_quantity


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
