from project.equipment.base_equipment import BaseEquipment


class KneePad(BaseEquipment):
    def __init__(self):
        super().__init__(120, 15)

    @property
    def increase_percentage(self):
        return 20
