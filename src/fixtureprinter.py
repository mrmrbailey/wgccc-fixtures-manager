from datetime import datetime, timezone, date, timedelta
from enum import Enum
from cricket_enums import Division, TeamName, Ground

class PitchLength(Enum):
    Y15 = ' (15 yards)'
    Y17 = ' (17 yards)'
    Y19 = ' (19 yards)'
    Y22 = ' (22 yards)'
    UNKNOWN = ' (? yards)'

def print_fixtures(list_of_fixtures):
    list_of_fixtures.sort()
    for fixture in list_of_fixtures:
        print_fixture(fixture)

def print_fixture(fixture):
    print(fixture)

def print_title(title):
    print('======== ' + title + ' =========')

def get_summary(fixture):
    summary = fixture.home + ' vs ' + fixture.away
    return summary

def get_pitch_length(division):
    match division:
        case Division.GIRLS | Division.U9s:
            return PitchLength.Y15
        case Division.U10s | Division.U11s | Division.U11summer:
            return PitchLength.Y17
        case Division.U12s | Division.U13s | Division.U13summer:
            return PitchLength.Y19
        case Division.U14s | Division.U15s | Division.U17s | Division.U15summer:
            return PitchLength.Y22
        case _:
            return PitchLength.UNKNOWN

def get_division(team):
    match team:
        case TeamName.GIRLS:
            return Division.GIRLS
        case TeamName.U9s:
            return Division.U9s
        case TeamName.U10s:
            return Division.U10s
        case TeamName.U11s:
            return Division.U11s
        case TeamName.U12s:
            return Division.U12s
        case TeamName.U13s:
            return Division.U13s
        case TeamName.U14s:
            return Division.U14s
        case TeamName.U15s:
            return Division.U15s
        case TeamName.U17s:
            return Division.U17s
        case TeamName.U11summer:
            return Division.U11summer
        case TeamName.U13summer:
            return Division.U13summer
        case TeamName.U15summer:
            return Division.U15summer
        case _:
            return Division.UNKNOWN

def get_google_calendar_summary(fixture):
    return get_summary(fixture) + get_pitch_length(fixture.division).value

def get_current_week():
    return date.today().strftime("%V")

def get_this_weeks_fixtures(list_of_fixtures):
    this_weeks_fixtures = []
    current_week = get_current_week()
    for fixture in list_of_fixtures:
        if current_week == fixture.get_fixture_date().strftime("%V"):
            this_weeks_fixtures.append(fixture)
    return this_weeks_fixtures

def get_next_weeks_fixtures(list_of_fixtures):
    next_weeks_fixtures = get_this_weeks_fixtures(list_of_fixtures)
    next_week = (date.today()+timedelta(weeks=1)).strftime("%V")
    for fixture in list_of_fixtures:
        if next_week == fixture.get_fixture_date().strftime("%V"):
            next_weeks_fixtures.append(fixture)
    return next_weeks_fixtures

def get_future_fixtures(list_of_fixtures):
    future_fixtures = []
    current_week = get_current_week()
    for fixture in list_of_fixtures:
        if current_week <= fixture.get_fixture_date().strftime("%V"):
            future_fixtures.append(fixture)
    return future_fixtures

def get_fixtures_for_ground(list_of_fixtures, ground):
    ground_fixtures = []
    for fixture in list_of_fixtures:
        if ground == fixture.ground:
            ground_fixtures.append(fixture)
    return ground_fixtures

def get_fixtures_for_team(list_of_fixtures, team):
    division = get_division(team)
    team_fixtures = []
    for fixture in list_of_fixtures:
        if fixture.division == division:
            team_fixtures.append(fixture)
    return team_fixtures

def print_this_weeks_fixtures(list_of_fixtures):
    print_title('This Weeks Fixtures')
    print_fixtures(get_this_weeks_fixtures(list_of_fixtures))

def print_next_weeks_fixtures(list_of_fixtures):
    print_title('Next Weeks Fixtures')
    print_fixtures(get_next_weeks_fixtures(list_of_fixtures))

def print_future_fixtures(list_of_fixtures):
    print_title('Future Fixtures')
    print_fixtures(get_future_fixtures(list_of_fixtures))

def print_fixtures_for_ground(list_of_fixtures, ground):
    print_title('Fixtures for Ground')
    print_fixtures(get_fixtures_for_ground(list_of_fixtures, ground))

def print_next_weeks_home_fixtures(list_of_fixtures):
    print_title('Next Weeks Home Fixtures')
    next_weeks_fixtures = get_next_weeks_fixtures(list_of_fixtures)

    dp_fixtures = get_fixtures_for_ground(next_weeks_fixtures, Ground.DP)
    wpf_fixtures = get_fixtures_for_ground(next_weeks_fixtures, Ground.WPF)

    print_fixtures(dp_fixtures + wpf_fixtures)

def print_fixtures_for_team(list_of_fixtures, team):
    print_title('Fixtures for Team')
    print_fixtures(get_fixtures_for_team(list_of_fixtures, team))
