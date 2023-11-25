from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):
    SIZE = 5
    INCREASE_CONST = 2

    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, SaltwaterFish.SIZE, price)

    @property
    def increase_const(self):
        return SaltwaterFish.INCREASE_CONST

    @property
    def fish_type(self):
        return "SaltwaterFish"
