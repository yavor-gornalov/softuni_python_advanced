from math import floor

from project.hardware.hardware import Hardware


class HeavyHardware(Hardware):
    TYPE = "Heavy"

    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name, HeavyHardware.TYPE, capacity * 2, floor(memory * 0.75))

    @property
    def type_of_hardware(self):
        return HeavyHardware.TYPE
4