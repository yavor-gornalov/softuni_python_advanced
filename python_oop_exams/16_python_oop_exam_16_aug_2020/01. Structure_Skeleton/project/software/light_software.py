from math import floor

from project.software.software import Software


class LightSoftware(Software):
    TYPE = "Light"

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name, LightSoftware.TYPE, floor(capacity_consumption * 1.5), floor(memory_consumption * 0.5))

    @property
    def type_of_software(self):
        return LightSoftware.TYPE
