from cricket_enums import TeamName
from os import path

def add_fixture(team):
    match team:
        case TeamName.UNKNOWN | TeamName.GIRLS | TeamName.U17s:
            add = False
        case _:
            add = True
    return add

def get_data_path():
    return path.dirname(__file__) + '/../../data/'
