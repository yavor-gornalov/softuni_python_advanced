from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    SIZE = 3
    INCREASE_CONST = 3

    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, FreshwaterFish.SIZE, price)

    @property
    def increase_const(self):
        return FreshwaterFish.INCREASE_CONST

    @property
    def fish_type(self):
        return "FreshwaterFish"
