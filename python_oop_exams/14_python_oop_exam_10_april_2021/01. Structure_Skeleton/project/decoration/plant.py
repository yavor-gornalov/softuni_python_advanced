from project.decoration.base_decoration import BaseDecoration


class Plant(BaseDecoration):
    COMFORT = 5
    PRICE = 10

    def __init__(self):
        super().__init__(comfort=Plant.COMFORT, price=Plant.PRICE)

    @property
    def decoration_type(self):
        return "Plant"
