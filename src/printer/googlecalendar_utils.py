from enum import Enum
from src.cricket_team import CricketTeam
from src.cricket_enums import FixtureType

class PitchLength(Enum):
    Y15 = ' (15 yards)'
    Y17 = ' (17 yards)'
    Y19 = ' (19 yards)'
    Y22 = ' (22 yards)'
    UNKNOWN = ' (? yards)'

def print_fixtures_for_google_calendar_csv_import(list_of_fixtures):
    print('Subject, Start Date, Start Time, End Time, Location, Description')
    list_of_fixtures.sort()
    for fixture in list_of_fixtures:
        subject = get_google_calendar_summary(fixture)
        start_date = fixture.get_localized_fixture_start_date_string()
        start_time = fixture.get_localized_fixture_start_time_string()
        end_time = fixture.get_localized_fixture_end_time_string()
        location = fixture.ground.value
        description = fixture.get_description()
        print(f"{subject},{start_date},{start_time},{end_time},{location},{description}")

def get_google_calendar_summary(fixture):
    matchup = fixture.get_matchup_for_calendar()
    if fixture.fixture_type.value is not FixtureType.SENIOR.value:
        matchup = matchup + get_pitch_length_string(fixture.wgc_team)
    return matchup

def get_pitch_length_string(cricket_team):
    match cricket_team:
        case CricketTeam.GIRLS | CricketTeam.U9s:
            return PitchLength.Y15.value
        case CricketTeam.U10s | CricketTeam.U11s | CricketTeam.U11summer:
            return PitchLength.Y17.value
        case CricketTeam.U12s | CricketTeam.U13s | CricketTeam.U13summer:
            return PitchLength.Y19.value
        case CricketTeam.U14s | CricketTeam.U15s | CricketTeam.U17s | CricketTeam.U15summer:
            return PitchLength.Y22.value
        case _:
            return PitchLength.UNKNOWN.value
