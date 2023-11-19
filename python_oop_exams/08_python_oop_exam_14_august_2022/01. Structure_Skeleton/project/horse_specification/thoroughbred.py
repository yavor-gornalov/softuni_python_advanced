from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    MAX_SPEED = 140
    TRAINING_POINTS = 3

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    @property
    def max_speed(self):
        return Thoroughbred.MAX_SPEED

    @property
    def training_points(self):
        return Thoroughbred.TRAINING_POINTS
