from cricket_enums import TeamName

def add_fixture(team):
    match team:
        case TeamName.UNKNOWN | TeamName.GIRLS | TeamName.U17s:
            add = False
        case _:
            add = True
    return add
