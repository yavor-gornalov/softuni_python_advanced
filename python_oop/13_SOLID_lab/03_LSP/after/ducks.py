from abc import abstractmethod, ABC


class BaseFlyingObject:
    FLY_LIMIT = 50

    def __init__(self):
        self.__height = 0

    def fly(self):
        self.height += 1

    def land(self):
        self.height = 0

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if value < self.FLY_LIMIT:
            self.__height = value
        else:
            self.land()


class BaseWalkingObject(ABC):
    @abstractmethod
    def walk(self):
        pass


class Duck(ABC):
    def __init__(self, name: str):
        self.name = name

    @staticmethod
    @abstractmethod
    def quack():
        pass


class RubberDuck(Duck):
    @staticmethod
    def quack():
        return "Squeek"


class RobotDuck(Duck, BaseWalkingObject, BaseFlyingObject):
    def __init__(self, name):
        Duck.__init__(self, name)
        BaseFlyingObject.__init__(self)

    @staticmethod
    def quack():
        return 'Robotic quacking'

    def walk(self):
        return 'Robotic walking'


rubber_duck = RubberDuck("My Rubber Duck")
robot_duck = RobotDuck("My Robot Duck")

print(rubber_duck.quack())
print(robot_duck.quack())

print(robot_duck.walk())
robot_duck.height = 49
print(robot_duck.height)
robot_duck.fly()
print(robot_duck.height)
