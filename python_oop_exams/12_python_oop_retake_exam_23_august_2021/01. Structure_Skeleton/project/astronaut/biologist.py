from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    UNITS_PER_BREATHE = 5

    def __init__(self, name: str):
        super().__init__(name, 70)

    @property
    def units_per_breathe(self):
        return self.UNITS_PER_BREATHE
