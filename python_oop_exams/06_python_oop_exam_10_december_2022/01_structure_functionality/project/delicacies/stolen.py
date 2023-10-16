from project.delicacies.delicacy import Delicacy


class Stolen(Delicacy):
    PORTION = 250

    def __init__(self, name: str, price: float):
        super().__init__(name, Stolen.PORTION, price)

    def _get_portion(self):
        return Stolen.PORTION
