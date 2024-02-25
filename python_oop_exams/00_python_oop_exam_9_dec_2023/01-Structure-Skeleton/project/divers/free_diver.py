from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):
    TYPE = "FreeDiver"
    INITIAL_OXYGEN = 120
    REDUCE_OXYGEN_PERCENTAGE = 0.6

    def __init__(self, name: str):
        super().__init__(name, FreeDiver.INITIAL_OXYGEN)

    @property
    def reduce_oxygen_percentage(self):
        return FreeDiver.REDUCE_OXYGEN_PERCENTAGE

    @property
    def initial_oxygen(self):
        return FreeDiver.INITIAL_OXYGEN

    @property
    def diver_type(self):
        return FreeDiver.TYPE
