import math
from abc import ABC, abstractmethod


class Computer(ABC):
    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price = 0

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value: str):
        if value.strip() == '':
            raise ValueError("Manufacturer name cannot be empty.")
        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value: str):
        if value.strip() == '':
            raise ValueError("Model name cannot be empty.")
        self.__model = value

    @property
    @abstractmethod
    def max_ram(self):
        pass

    @property
    @abstractmethod
    def processors_available(self):
        pass

    @property
    @abstractmethod
    def computer_type(self):
        pass

    @property
    def ram_available(self):
        return {2 ** n: n * 100 for n in range(1, int(math.log2(self.max_ram)) + 1)}

    def configure_computer(self, processor: str, ram: int):
        processor_price = self.processors_available.get(processor)
        if processor_price is None:
            raise ValueError(
                f"{processor} is not compatible with {self.computer_type} {self.manufacturer} {self.model}!")

        ram_price = self.ram_available.get(ram)
        if ram_price is None:
            raise ValueError(
                f"{ram}GB RAM is not compatible with {self.computer_type} {self.manufacturer} {self.model}!")

        self.processor = processor
        self.ram = ram
        self.price += processor_price + ram_price
        return f"Created {self} for {self.price}$."

    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"
