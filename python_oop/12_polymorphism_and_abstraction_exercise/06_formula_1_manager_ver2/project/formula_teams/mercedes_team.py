from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    SPONSOR_PRICES = {"Oracle": {1: 1_000_000, 3: 500_000},
                      "Honda": {5: 100_000, 7: 50_000}}
    RACE_COSTS = 200_000

    @property
    def expenses_per_race(self):
        return MercedesTeam.RACE_COSTS

    @property
    def sponsor_price_per_position(self):
        return MercedesTeam.SPONSOR_PRICES
