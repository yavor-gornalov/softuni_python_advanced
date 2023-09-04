from project.equipment.base_equipment import BaseEquipment


class ElbowPad(BaseEquipment):
    def __init__(self):
        super().__init__(90, 25)

    @property
    def increase_percentage(self):
        return 10
