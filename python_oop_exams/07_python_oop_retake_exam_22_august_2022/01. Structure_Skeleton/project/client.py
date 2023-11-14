from typing import List

from project.meals.meal import Meal


class Client:
    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.shopping_cart: List[Meal] = []
        self.bill: float = 0

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value: str):
        if not all([value.startswith("0"), len(value) == 10, value.isdigit()]):
            # if not value.startswith("0") or len(value) != 10 or not value.isdigit():
            raise ValueError("Invalid phone number!")
        self.__phone_number = value


if __name__ == "__main__":
    c1 = Client("0123456789")
    # c2 = Client("012345678")
    # c3 = Client("012345678a")
