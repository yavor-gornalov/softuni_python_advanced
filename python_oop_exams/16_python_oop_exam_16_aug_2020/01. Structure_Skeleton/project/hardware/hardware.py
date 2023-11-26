from typing import List

from project.software.software import Software


class Hardware:
    def __init__(self, name: str, hardware_type: str, capacity: int, memory: int):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components: List[Software] = []
        self.__initial_capacity = capacity
        self.__initial_memory = memory

    @property
    def initial_capacity(self):
        return self.__initial_capacity

    @property
    def initial_memory(self):
        return self.__initial_memory

    @property
    def installed_software(self):
        return ", ".join([x.name for x in self.software_components]) if self.software_components else None

    def install(self, software: Software):
        if software.capacity_consumption > self.capacity or software.memory_consumption > self.memory:
            raise Exception("Software cannot be installed")

        self.software_components.append(software)
        self.capacity -= software.capacity_consumption
        self.memory -= software.memory_consumption

    def uninstall(self, software: Software):
        if software not in self.software_components:
            return

        self.software_components.remove(software)
        self.capacity += software.capacity_consumption
        self.memory += software.memory_consumption

    def __str__(self):
        return f"""Hardware Component - {self.name}
Express Software Components: {len([x for x in self.software_components if x.software_type == "Express"])}
Light Software Components: {len([x for x in self.software_components if x.software_type == "Light"])}
Memory Usage: {sum([x.memory_consumption for x in self.software_components])} / {self.initial_memory}
Capacity Usage: {sum([x.capacity_consumption for x in self.software_components])} / {self.initial_capacity}
Type: {self.hardware_type}
Software Components: {self.installed_software}"""
