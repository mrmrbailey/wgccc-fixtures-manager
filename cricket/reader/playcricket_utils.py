# imports
from cricket_team import CricketTeam

def add_fixture(team):
    match team:
        case CricketTeam.UNKNOWN:
            add = False
        case _:
            add = True
    return add
