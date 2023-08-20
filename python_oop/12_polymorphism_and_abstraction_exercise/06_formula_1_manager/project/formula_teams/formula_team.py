from abc import ABC, abstractmethod


class FormulaTeam(ABC):
    def __init__(self, budget: int):
        self.budget = budget

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        if value < 1_000_000:
            raise ValueError(f"F1 is an expensive sport, find more sponsors!")
        self.__budget = value

    @property
    @abstractmethod
    def sponsors_bonuses(self) -> dict:
        """
        :return: {sponsor_name: {race_position: bonus}, ...}
        """
        pass

    @property
    @abstractmethod
    def race_expenses(self) -> int:
        """
        :return: value of expenses for current race
        """
        pass

    @staticmethod
    def get_bonus_value(race_pos, sponsors_bonuses):
        result = 0
        for sponsor_name, data in sponsors_bonuses.items():
            sponsor_bonus = 0
            for pos, current_bonus in data.items():
                if race_pos <= pos:
                    sponsor_bonus = current_bonus
                    break
            result += sponsor_bonus
        return result

    def calculate_revenue_after_race(self, race_pos: int):
        expenses = self.race_expenses
        bonus = self.get_bonus_value(race_pos, self.sponsors_bonuses)
        revenue = bonus - expenses
        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
