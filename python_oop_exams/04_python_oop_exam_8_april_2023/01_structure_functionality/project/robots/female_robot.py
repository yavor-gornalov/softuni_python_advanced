from project.robots.base_robot import BaseRobot


class FemaleRobot(BaseRobot):
    INITIAL_WEIGHT = 7
    INCREASE_WEIGHT_CONST = 1

    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, weight=FemaleRobot.INITIAL_WEIGHT)

    def eating(self):
        self.weight += FemaleRobot.INCREASE_WEIGHT_CONST
