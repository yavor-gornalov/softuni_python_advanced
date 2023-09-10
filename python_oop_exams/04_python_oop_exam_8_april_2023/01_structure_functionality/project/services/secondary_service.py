from project.services.base_service import BaseService


class SecondaryService(BaseService):
    CAPACITY = 15

    def __init__(self, name: str):
        super().__init__(name, capacity=SecondaryService.CAPACITY)

    def details(self):
        robot_names = [r.name for r in self.robots]
        return f"""{self.name} Secondary Service:
Robots: {" ".join(robot_names) if robot_names else "none"}"""
