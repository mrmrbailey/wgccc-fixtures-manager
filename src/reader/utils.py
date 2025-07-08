from cricket_enums import TeamName, Division, FixtureType, FullTeamName
from os import path

def add_fixture(team):
    match team:
        case TeamName.UNKNOWN:
            add = False
        case _:
            add = True
    return add

def get_data_path():
    return path.dirname(__file__) + '/../../data/'

def get_fixture_type(fixture_type):
    match fixture_type:
        case FixtureType.LEAGUE.value:
            return FixtureType.LEAGUE
        case FixtureType.CUP.value:
            return FixtureType.CUP
        case FixtureType.FRIENDLY.value:
            return FixtureType.FRIENDLY
        case _:
            return FixtureType.UNKNOWN

def get_wgc_team(division):
    match division:
        case Division.GIRLS.value:
            return TeamName.GIRLS
        case Division.U9s.value:
            return TeamName.U9s
        case Division.U10s.value:
            return TeamName.U10s
        case Division.U11s.value:
            return TeamName.U11s
        case Division.U12s.value:
            return TeamName.U12s
        case Division.U13s.value:
            return TeamName.U13s
        case Division.U14s.value:
            return TeamName.U14s
        case Division.U15s.value:
            return TeamName.U15s
        case Division.U17s.value:
            return TeamName.U17s
        case Division.U11summer.value:
            return TeamName.U11summer
        case Division.U13summer.value:
            return TeamName.U13summer
        case Division.U15summer.value:
            return TeamName.U15summer
        case _:
            return TeamName.UNKNOWN

def get_wgc_team_from_summary(summary):
    if TeamName.GIRLS.value in summary:
        return TeamName.GIRLS
    elif TeamName.U11summer.value in summary:
        return TeamName.U11summer
    elif TeamName.U13summer.value in summary:
        return TeamName.U13summer
    elif TeamName.U15summer.value in summary:
        return TeamName.U15summer
    elif TeamName.U9s.value in summary:
        return TeamName.U9s
    elif TeamName.U10s.value in summary:
        return TeamName.U10s
    elif TeamName.U11s.value in summary:
        return TeamName.U11s
    elif TeamName.U12s.value in summary:
        return TeamName.U12s
    elif TeamName.U13s.value in summary:
        return TeamName.U13s
    elif TeamName.U14s.value in summary:
        return TeamName.U14s
    elif TeamName.U15s.value in summary:
        return TeamName.U15s
    elif TeamName.U17s.value in summary:
        return TeamName.U17s
    elif TeamName.U11summer.value in summary:
        return TeamName.U11ssummer
    elif TeamName.U13summer.value in summary:
        return TeamName.U13summer
    elif TeamName.U15summer.value in summary:
        return TeamName.U15summer
    else:
        return TeamName.UNKNOWN

def get_team_name_from_full_name(full_team_name):
    if FullTeamName.GIRLS.value in full_team_name:
        return TeamName.GIRLS
    elif FullTeamName.U11summer.value in full_team_name:
        return TeamName.U11summer
    elif FullTeamName.U13summer.value in full_team_name:
        return TeamName.U13summer
    elif FullTeamName.U15summer.value in full_team_name:
        return TeamName.U15summer
    elif FullTeamName.U9s.value in full_team_name:
        return TeamName.U9s
    elif FullTeamName.U10s.value in full_team_name:
        return TeamName.U10s
    elif FullTeamName.U11s.value in full_team_name:
        return TeamName.U11s
    elif FullTeamName.U12s.value in full_team_name:
        return TeamName.U12s
    elif FullTeamName.U13s.value in full_team_name:
        return TeamName.U13s
    elif FullTeamName.U14s.value in full_team_name:
        return TeamName.U14s
    elif FullTeamName.U15s.value in full_team_name:
        return TeamName.U15s
    elif FullTeamName.U17s.value in full_team_name:
        return TeamName.U17s
    elif FullTeamName.U11ssummer.value in full_team_name:
        return TeamName.U11ssummer
    elif FullTeamName.U13summer.value in full_team_name:
        return TeamName.U13summer
    elif FullTeamName.U15summer.value in full_team_name:
        return TeamName.U15summer
    else:
        return TeamName.UNKNOWN
