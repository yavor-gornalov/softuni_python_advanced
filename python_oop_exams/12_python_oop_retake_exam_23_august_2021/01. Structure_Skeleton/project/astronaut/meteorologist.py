from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    UNITS_PER_BREATHE = 15

    def __init__(self, name: str):
        super().__init__(name, 90)

    @property
    def units_per_breathe(self):
        return self.UNITS_PER_BREATHE
