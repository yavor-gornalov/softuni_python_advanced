from abc import ABC, abstractmethod
from typing import List

from project.appliances.appliance import Appliance
from project.people.child import Child


class Room(ABC):
    def __init__(self, name: str, budget: float, members_count: int, *children):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children: List[Child] = list(children)
        self.expenses = 0

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = value

    def calculate_expenses(self, *args):
        total_expenses = 0
        for arg in args:
            total_expenses += arg.get_monthly_expense()
        self.expenses = total_expenses

    @property
    def appliances_expenses(self):
        appliances_expenses = 0
        for item in self.appliances:
            appliances_expenses += item.get_monthly_expense()
        return appliances_expenses

    def __str__(self):
        result = [f"{self.family_name} with {self.members_count} members. "
                  f"Budget: {self.budget:.2f}$, Expenses: {self.expenses:.2f}$"]
        if self.children:
            for i, c in enumerate(self.children, 1):
                result.append(f"--- Child {i} monthly cost: {c.get_monthly_expense():.2f}$")
        result.append(f"--- Appliances monthly cost: {self.appliances_expenses:.2f}$")
        return "\n".join(result)
