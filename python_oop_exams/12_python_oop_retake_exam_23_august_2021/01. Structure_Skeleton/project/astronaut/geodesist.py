from project.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):
    def __init__(self, name: str):
        super().__init__(name, 50)

    @property
    def units_per_breathe(self):
        return self.UNITS_PER_BREATHE
