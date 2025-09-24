from cricket_team import CricketTeam
from os import path

def add_fixture(team):
    match team:
        case CricketTeam.UNKNOWN:
            add = False
        case _:
            add = True
    return add

def get_data_path():
    return path.dirname(__file__) + '/../../data/'
