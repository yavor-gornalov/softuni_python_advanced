from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    MAX_SPEED = 120
    TRAINING_POINTS = 2

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    @property
    def max_speed(self):
        return Appaloosa.MAX_SPEED

    @property
    def training_points(self):
        return Appaloosa.TRAINING_POINTS
