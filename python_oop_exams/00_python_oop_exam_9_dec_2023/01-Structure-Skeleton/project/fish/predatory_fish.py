from project.fish.base_fish import BaseFish


class PredatoryFish(BaseFish):
    TIME_TO_CATCH = 90
    TYPE = "PredatoryFish"

    def __init__(self, name: str, points: float):
        super().__init__(name, points, PredatoryFish.TIME_TO_CATCH)

    @property
    def fish_type(self):
        return PredatoryFish.TYPE
