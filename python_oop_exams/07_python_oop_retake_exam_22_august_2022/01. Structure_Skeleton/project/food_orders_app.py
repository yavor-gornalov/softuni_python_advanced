from typing import List
from copy import copy

from project.client import Client
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.meal import Meal
from project.meals.starter import Starter


class FoodOrdersApp:
    MEALS = {"Starter": Starter, "Main Dish": MainDish, "Dessert": Dessert}
    id = 1

    def __init__(self):
        self.menu: List[Meal] = []
        self.clients_list: List[Client] = []

    def register_client(self, client_phone_number: str):
        if self.get_client_by_phone(client_phone_number):
            raise Exception("The client has already been registered!")
        new_client = Client(client_phone_number)
        self.clients_list.append(new_client)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            # if meal.meal_type not in self.MEALS:
            if meal.__class__ not in [Starter, MainDish, Dessert]:
                continue
            self.menu.append(meal)

    def show_menu(self):
        self.check_menu_ready()
        result = []
        [result.append(x.details()) for x in self.menu]
        return "\n".join(result)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        self.check_menu_ready()

        client = self.get_client_by_phone(client_phone_number)
        if not client:
            self.register_client(client_phone_number)
            client = self.get_client_by_phone(client_phone_number)

        for meal_name, ordered_quantity in meal_names_and_quantities.items():
            meal = self.get_meal_by_name(meal_name)
            if not meal:
                raise Exception(f"{meal_name} is not on the menu!")
            if meal.quantity < ordered_quantity:
                raise Exception(f"Not enough quantity of {meal.meal_type}: {meal_name}!")

        for meal_name, ordered_quantity in meal_names_and_quantities.items():
            meal = self.get_meal_by_name(meal_name)
            meal.quantity -= ordered_quantity

            # client_meal = self.MEALS[meal.meal_type](meal.name, meal.price, ordered_quantity)
            client_meal = copy(meal)
            client_meal.quantity = ordered_quantity
            client.shopping_cart.append(client_meal)
            client.bill += client_meal.price * client_meal.quantity

        return (f"Client {client_phone_number} successfully ordered "
                f"{', '.join(n.name for n in client.shopping_cart)} for {client.bill:.2f}lv.")

    def cancel_order(self, client_phone_number: str):
        client = self.get_client_by_phone(client_phone_number)
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")
        for client_meal in client.shopping_cart:
            meal = self.get_meal_by_name(client_meal.name)
            meal.quantity += client_meal.quantity
        client.bill = 0
        client.shopping_cart.clear()
        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = self.get_client_by_phone(client_phone_number)
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")
        total_paid_money = client.bill
        client.bill = 0
        client.shopping_cart.clear()
        receipt_id = FoodOrdersApp.id
        FoodOrdersApp.id += 1
        return (f"Receipt #{receipt_id} with total amount of {total_paid_money:.2f} "
                f"was successfully paid for {client_phone_number}.")

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."

    # HELPERS:
    def check_menu_ready(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

    def get_client_by_phone(self, client_phone_number):
        return next((c for c in self.clients_list if c.phone_number == client_phone_number), None)

    def get_meal_by_name(self, meal_name):
        return next((m for m in self.menu if m.name == meal_name), None)


if __name__ == "__main__":
    class Stopper(Starter):
        ...


    food_orders_app = FoodOrdersApp()
    print(food_orders_app.register_client("0899999999"))

    french_toast = Starter("French toast", 6.50, 5)
    german_toast = Stopper("French toast", 6.50, 5)

    food_orders_app.add_meals_to_menu(french_toast)
    food_orders_app.add_meals_to_menu(german_toast)
    print(food_orders_app.menu)
