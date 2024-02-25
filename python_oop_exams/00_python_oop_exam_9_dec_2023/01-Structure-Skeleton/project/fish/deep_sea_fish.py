from project.fish.base_fish import BaseFish


class DeepSeaFish(BaseFish):
    TIME_TO_CATCH = 180
    TYPE = "DeepSeaFish"

    def __init__(self, name: str, points: float):
        super().__init__(name, points, DeepSeaFish.TIME_TO_CATCH)

    @property
    def fish_type(self):
        return DeepSeaFish.TYPE
