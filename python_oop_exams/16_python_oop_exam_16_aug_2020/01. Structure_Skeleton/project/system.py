from typing import List

from project.hardware.hardware import Hardware
from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware
from project.software.software import Software


class System:
    _hardware: List[Hardware] = []
    _software: List[Software] = []
    __total_capacity = 0
    __total_memory = 0

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(hardware)
        System.__total_capacity += hardware.capacity
        System.__total_memory += hardware.memory

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(hardware)
        System.__total_capacity += hardware.capacity
        System.__total_memory += hardware.memory

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = System.__get_item_by_attr(System._hardware, name=hardware_name)
        if not hardware:
            return "Hardware does not exist"
        software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(software)
        System._software.append(software)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = System.__get_item_by_attr(System._hardware, name=hardware_name)
        if not hardware:
            return "Hardware does not exist"
        software = LightSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(software)
        System._software.append(software)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hardware = System.__get_item_by_attr(System._hardware, name=hardware_name)
        software = System.__get_item_by_attr(System._software, name=software_name)
        if hardware is None or software is None:
            return "Some of the components do not exist"
        hardware.uninstall(software)
        System._software.remove(software)

    @staticmethod
    def total_capacity():
        return System.__total_capacity

    @staticmethod
    def total_memory():
        return System.__total_memory

    @staticmethod
    def total_memory_consumption():
        return sum([x.memory_consumption for x in System._software])

    @staticmethod
    def total_capacity_consumption():
        return sum([x.capacity_consumption for x in System._software])

    @staticmethod
    def analyze():
        return f"""System Analysis
Hardware Components: {len(System._hardware)}
Software Components: {len(System._software)}
Total Operational Memory: {System.total_memory_consumption()} / {System.total_memory()}
Total Capacity Taken: {System.total_capacity_consumption()} / {System.total_capacity()}"""

    @staticmethod
    def system_split():
        return "\n".join([str(x) for x in System._hardware])

    # HELPERS:
    @staticmethod
    def __get_item_by_attr(collection, **kwargs):
        for attr, value in kwargs.items():
            return next((x for x in collection if getattr(x, attr, None) == value), None)
