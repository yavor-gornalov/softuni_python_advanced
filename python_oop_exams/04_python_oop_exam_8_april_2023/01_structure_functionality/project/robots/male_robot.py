from project.robots.base_robot import BaseRobot


class MaleRobot(BaseRobot):
    INITIAL_WEIGHT = 9
    INCREASE_WEIGHT_CONST = 3

    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, weight=MaleRobot.INITIAL_WEIGHT)

    def eating(self):
        self.weight += MaleRobot.INCREASE_WEIGHT_CONST
