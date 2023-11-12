from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    SPONSOR_PRICES = {"Oracle": {1: 1_500_000, 2: 800_000},
                      "Honda": {8: 20_000, 10: 10_000}}
    RACE_COSTS = 250_000

    @property
    def expenses_per_race(self):
        return RedBullTeam.RACE_COSTS

    @property
    def sponsor_price_per_position(self):
        return RedBullTeam.SPONSOR_PRICES
