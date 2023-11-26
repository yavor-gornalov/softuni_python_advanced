from project.software.software import Software


class ExpressSoftware(Software):
    TYPE = "Express"

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name, ExpressSoftware.TYPE, capacity_consumption, memory_consumption * 2)

    @property
    def type_of_software(self):
        return ExpressSoftware.TYPE
