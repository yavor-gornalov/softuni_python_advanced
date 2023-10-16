from project.delicacies.delicacy import Delicacy


class Gingerbread(Delicacy):
    PORTION = 200

    def __init__(self, name: str, price: float):
        super().__init__(name, Gingerbread.PORTION, price)

    def _get_portion(self):
        return Gingerbread.PORTION
