from typing import List

from project.baked_food.baked_food import BakedFood
from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.drink import Drink
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable
from project.table.table import Table


class Bakery:
    FOOD_TYPES = {"Bread": Bread, "Cake": Cake}
    DRINK_TYPES = {"Tea": Tea, "Water": Water}
    TABLE_TYPES = {"InsideTable": InsideTable, "OutsideTable": OutsideTable}

    def __init__(self, name: str):
        self.name = name
        self.food_menu: List[BakedFood] = []
        self.drinks_menu: List[Drink] = []
        self.tables_repository: List[Table] = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value.strip():
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type: str, food_name: str, price: float):
        if food_type not in self.FOOD_TYPES:
            return
        if self.__get_item_by_attr(self.food_menu, name=food_name):
            raise Exception(f"{food_type} {food_name} is already in the menu!")

        new_food = self.FOOD_TYPES[food_type](food_name, price)
        self.food_menu.append(new_food)
        return f"Added {food_name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, drink_name: str, portion: float, brand: str):
        if drink_type not in self.DRINK_TYPES:
            return
        if self.__get_item_by_attr(self.drinks_menu, name=drink_name):
            raise Exception(f"{drink_type} {drink_name} is already in the menu!")

        new_drink = self.DRINK_TYPES[drink_type](drink_name, portion, brand)
        self.drinks_menu.append(new_drink)
        return f"Added {drink_name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if table_type not in self.TABLE_TYPES:
            return
        if self.__get_item_by_attr(self.tables_repository, table_number=table_number):
            raise Exception(f"Table {table_number} is already in the bakery!")

        new_table = self.TABLE_TYPES[table_type](table_number, capacity)
        self.tables_repository.append(new_table)
        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        table = self.__find_free_table(number_of_people)
        if not table:
            return f"No available table for {number_of_people} people"

        table.reserve(number_of_people)
        return f"Table {table.table_number} has been reserved for {number_of_people} people"

    def order_food(self, table_number: int, *args):
        table = self.__get_item_by_attr(self.tables_repository, table_number=table_number)
        if not table:
            return f"Could not find table {table_number}"

        ordered_food = [f"Table {table_number} ordered:"]
        not_existing_food = [f"{self.name} does not have in the menu:"]
        for food_name in args:
            food = self.__get_item_by_attr(self.food_menu, name=food_name)
            if not food:
                not_existing_food.append(food_name)
            else:
                table.order_food(food)
                ordered_food.append(str(food))

        return "\n".join(ordered_food + not_existing_food)

    def order_drink(self, table_number: int, *args):
        table = self.__get_item_by_attr(self.tables_repository, table_number=table_number)
        if not table:
            return f"Could not find table {table_number}"

        ordered_drink = [f"Table {table_number} ordered:"]
        not_existing_drink = [f"{self.name} does not have in the menu:"]
        for drink_name in args:
            drink = self.__get_item_by_attr(self.drinks_menu, name=drink_name)
            if not drink:
                not_existing_drink.append(drink_name)
            else:
                table.order_drink(drink)
                ordered_drink.append(str(drink))

        return "\n".join(ordered_drink + not_existing_drink)

    def leave_table(self, table_number: int):
        table = self.__get_item_by_attr(self.tables_repository, table_number=table_number)
        if not table:
            return

        table_bill = table.get_bill()
        self.total_income += table_bill
        table.clear()

        return f"Table: {table_number}\nBill: {table_bill:.2f}"

    def get_free_tables_info(self):
        info = [t.free_table_info() for t in self.tables_repository if t.free_table_info() is not None]
        return "\n".join(info)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"

    # HELPERS:
    @staticmethod
    def __get_item_by_attr(collection, **kwargs):
        for attr, value in kwargs.items():
            return next((x for x in collection if getattr(x, attr, None) == value), None)

    def __find_free_table(self, number_of_people):
        return next((t for t in self.tables_repository if not t.is_reserved and t.capacity >= number_of_people), None)
