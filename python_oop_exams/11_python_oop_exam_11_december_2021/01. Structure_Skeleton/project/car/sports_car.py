from project.car.car import Car


class SportsCar(Car):
    MIN_SPEED_LIMIT = 400
    MAX_SPEED_LIMIT = 600

    def __init__(self, model: str, speed_limit: int):
        super().__init__(model, speed_limit)

    @property
    def min_speed_limit(self):
        return SportsCar.MIN_SPEED_LIMIT

    @property
    def max_speed_limit(self):
        return SportsCar.MAX_SPEED_LIMIT
