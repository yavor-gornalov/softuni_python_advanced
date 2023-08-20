from project.formula_teams.mercedes_team import MercedesTeam
from project.formula_teams.red_bull_team import RedBullTeam


class F1SeasonApp:
    TEAM_NAMES = ["Red Bull", "Mercedes"]

    def __init__(self):
        self.red_bull_team: RedBullTeam = None
        self.mercedes_team: MercedesTeam = None

    def register_team_for_season(self, team_name: str, budget: int) -> str:
        if team_name == self.TEAM_NAMES[0]:
            self.red_bull_team = RedBullTeam(budget)
        elif team_name == self.TEAM_NAMES[1]:
            self.mercedes_team = MercedesTeam(budget)
        else:
            raise ValueError("Invalid team name!")

        return f"{team_name} has joined the new F1 season."

    def get_team_ahead(self, red_bull_pos: int, mercedes_pos: int):
        return self.TEAM_NAMES[0] if red_bull_pos < mercedes_pos else self.TEAM_NAMES[1]

    def new_race_results(self, race_name: str, red_bull_pos: int, mercedes_pos: int):
        if self.red_bull_team is None or self.mercedes_team is None:
            raise Exception("Not all teams have registered for the season.")

        return (f"Red Bull: {self.red_bull_team.calculate_revenue_after_race(red_bull_pos)}. "
                f"Mercedes: {self.mercedes_team.calculate_revenue_after_race(mercedes_pos)}. "
                f"{self.get_team_ahead(red_bull_pos, mercedes_pos)} is ahead at the {race_name} race.")
