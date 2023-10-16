from typing import List

from project.booths.booth import Booth
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.delicacy import Delicacy
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    DELICACY_TYPES = {'Gingerbread': Gingerbread, 'Stolen': Stolen}
    BOOTH_TYPES = {'Open Booth': OpenBooth, 'Private Booth': PrivateBooth}

    def __init__(self):
        self.booths: List[Booth] = []
        self.delicacies: List[Delicacy] = []
        self.income: float = 0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        if type_delicacy not in self.DELICACY_TYPES:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")
        if [x for x in self.delicacies if x.name == name]:
            raise Exception(f"{name} already exists!")
        new_delicacy = self.DELICACY_TYPES[type_delicacy](name, price)
        self.delicacies.append(new_delicacy)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        if type_booth not in self.BOOTH_TYPES:
            raise Exception(f"{type_booth} is not a valid booth!")
        if [x for x in self.booths if x.booth_number == booth_number]:
            raise Exception(f"Booth number {booth_number} already exists!")
        new_booth = self.BOOTH_TYPES[type_booth](booth_number, capacity)
        self.booths.append(new_booth)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        collection = [x for x in self.booths if not x.is_reserved and x.capacity >= number_of_people]
        if not collection:
            raise Exception(f"No available booth for {number_of_people} people!")
        booth = collection[0]
        booth.reserve(number_of_people)
        return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        booth = self._get_booth_by_number(booth_number)
        delicacy = self._get_delicacy_by_name(delicacy_name)
        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth.booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = self._get_booth_by_number(booth_number)
        bill = sum([x.price for x in booth.delicacy_orders]) + booth.price_for_reservation
        self.income += bill
        booth.delicacy_orders.clear()
        booth.price_for_reservation = 0
        booth.is_reserved = False
        return f"Booth {booth.booth_number}:\nBill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."

    # HELPERS:
    def _get_booth_by_number(self, booth_number):
        collection = [x for x in self.booths if x.booth_number == booth_number]
        if not collection:
            raise Exception(f"Could not find booth {booth_number}!")
        return collection[0]

    def _get_delicacy_by_name(self, delicacy_name):
        collection = [x for x in self.delicacies if x.name == delicacy_name]
        if not collection:
            raise Exception(f"No {delicacy_name} in the pastry shop!")
        return collection[0]
