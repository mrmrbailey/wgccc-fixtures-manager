# imports
from src.cricket_team import CricketTeam

def get_wgc_team_from_division(division):
    for team in CricketTeam:
        if team.division  == division:
            return team

    return CricketTeam.UNKNOWN

