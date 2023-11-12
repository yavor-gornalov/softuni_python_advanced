from abc import ABC, abstractmethod


class FormulaTeam(ABC):
    BUDGET_LOW_LIMIT = 1_000_000

    def __init__(self, budget: int):
        self.budget = budget

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        if value < FormulaTeam.BUDGET_LOW_LIMIT:
            raise ValueError("F1 is an expensive sport, find more sponsors!")
        self.__budget = value

    @property
    @abstractmethod
    def expenses_per_race(self) -> int:
        pass

    @property
    @abstractmethod
    def sponsor_price_per_position(self) -> dict:
        pass

    def calculate_revenue_after_race(self, race_pos: int):
        revenue = -self.expenses_per_race
        for sponsor, prices in self.sponsor_price_per_position.items():
            for pos, price in prices.items():
                if race_pos <= pos:
                    revenue += price
                    break
        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
