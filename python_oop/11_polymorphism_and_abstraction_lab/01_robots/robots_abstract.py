from abc import ABC, abstractmethod


class Robot(ABC):
    @staticmethod
    @abstractmethod
    def sensors_amount():
        raise NotImplementedError("Unknown nuber of sensors!")


class BasicRobot:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def sensors_amount():
        return 1


class MedicalRobot(Robot):
    def __init__(self, name):
        self.name = name

    @staticmethod
    def sensors_amount():
        return 6


class ChefRobot(Robot):
    def __init__(self, name):
        self.name = name

    @staticmethod
    def sensors_amount():
        return 4


class WarRobot(Robot):
    def __init__(self, name):
        self.name = name

    @staticmethod
    def sensors_amount():
        return 12


basic_robot = BasicRobot('Robo')
da_vinci = MedicalRobot('Da Vinci')
moley = ChefRobot('Moley')
griffin = WarRobot('Griffin')

robots = []
robots.extend([basic_robot, da_vinci, moley, griffin])

for robot in robots:
    print(robot.sensors_amount())
