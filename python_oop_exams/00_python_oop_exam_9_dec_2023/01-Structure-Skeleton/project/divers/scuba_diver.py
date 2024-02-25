from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):
    TYPE = "ScubaDiver"
    INITIAL_OXYGEN = 540
    REDUCE_OXYGEN_PERCENTAGE = 0.3

    def __init__(self, name: str):
        super().__init__(name, ScubaDiver.INITIAL_OXYGEN)

    @property
    def reduce_oxygen_percentage(self):
        return ScubaDiver.REDUCE_OXYGEN_PERCENTAGE

    @property
    def initial_oxygen(self):
        return ScubaDiver.INITIAL_OXYGEN

    @property
    def diver_type(self):
        return ScubaDiver.TYPE
