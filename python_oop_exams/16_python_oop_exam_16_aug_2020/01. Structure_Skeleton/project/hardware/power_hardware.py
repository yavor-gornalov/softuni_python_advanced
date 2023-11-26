from math import floor

from project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    TYPE = "Power"

    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name, PowerHardware.TYPE, floor(capacity * 0.25), floor(memory * 1.75))

    @property
    def type_of_hardware(self):
        return PowerHardware.TYPE
