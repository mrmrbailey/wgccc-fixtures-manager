from datetime import date, timedelta
from enum import Enum
from src.cricket_team import CricketTeam
from src.cricket_enums import Ground, Location, FixtureType

def print_fixtures(list_of_fixtures):
    list_of_fixtures.sort()
    for fixture in list_of_fixtures:
        print_fixture(fixture)

def print_fixture(fixture):
    print(fixture)

def print_title(title):
    print('======== ' + title + ' =========')

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

def get_fixtures_for_type(list_of_fixtures, fixture_type):
    type_fixtures = []
    for fixture in list_of_fixtures:
        if fixture_type == fixture.fixture_type:
            type_fixtures.append(fixture)
    return type_fixtures

def get_fixtures_for_team(list_of_fixtures, team):
    team_fixtures = []
    for fixture in list_of_fixtures:
        if fixture.wgc_team == team:
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

def print_fixtures_for_type(list_of_fixtures, fixture_type):
    print_title('Fixtures for Type')
    print_fixtures(get_fixtures_for_type(list_of_fixtures, fixture_type))

def print_next_weeks_home_fixtures(list_of_fixtures):
    print_title('Next Weeks Home Fixtures')
    next_weeks_fixtures = get_next_weeks_fixtures(list_of_fixtures)

    dp_fixtures = get_fixtures_for_ground(next_weeks_fixtures, Ground.DP)
    wpf_fixtures = get_fixtures_for_ground(next_weeks_fixtures, Ground.WPF)

    print_fixtures(dp_fixtures + wpf_fixtures)

def print_fixtures_for_team(list_of_fixtures, team):
    print_title('Fixtures for Team')
    print_fixtures(get_fixtures_for_team(list_of_fixtures, team))

def get_fixtures_for_google_calendar(list_of_fixtures, ground):
    get_fixtures_for_ground(list_of_fixtures, ground)

def print_google_calendar_csv(list_of_fixtures,ground):
    print_title('Google Calendar Import')
    print_csv_calendar(get_fixtures_for_ground(list_of_fixtures, ground))

class GoogleCalendarField(Enum):
    SUMMARY = 0
    DESCRIPTION = 1

class PitchLength(Enum):
    Y15 = ' (15 yards)'
    Y17 = ' (17 yards)'
    Y19 = ' (19 yards)'
    Y22 = ' (22 yards)'
    UNKNOWN = ' (? yards)'

def get_matchup(fixture, field):
    match field:
        case GoogleCalendarField.SUMMARY:
            wgc_team_name = fixture.wgc_team.value
        case GoogleCalendarField.DESCRIPTION:
            wgc_team_name = fixture.wgc_team.team_fullname
        case _:
            wgc_team_name = CricketTeam.WGCCC.value

    if wgc_team_name == CricketTeam.NotWGCCC.value:
        matchup = fixture.oppo
    elif fixture.location == Location.HOME:
        matchup = wgc_team_name + ' v ' + fixture.oppo
    else:
        matchup = fixture.oppo + ' v ' + wgc_team_name
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

def get_google_calendar_summary(fixture):
    matchup = get_matchup(fixture, GoogleCalendarField.SUMMARY)
    if fixture.fixture_type.value != FixtureType.SENIOR.value:
        matchup = matchup + get_pitch_length_string(fixture.wgc_team)
    return matchup

def get_description(fixture):
    description = get_matchup(fixture, GoogleCalendarField.DESCRIPTION)
    description += ' on '
    description += fixture.get_fixture_date().strftime('%a %d %b %Y at %H:%M')
    description += "~"
    description += fixture.fixture_type.value
    if fixture.fixture_type.value == FixtureType.LEAGUE.value:
        description += "~"
        description += fixture.wgc_team.division
    return description

def print_csv_calendar(list_of_fixtures):
    print('Subject, Start Date, Start Time, End Time, Location, Description')
    list_of_fixtures.sort()
    for fixture in list_of_fixtures:
        subject = get_google_calendar_summary(fixture)
        fixture_date = fixture.get_fixture_date()
        start_date = fixture_date.strftime('%d/%m/%Y')
        start_time = fixture_date.strftime('%H:%M')
        end_time = (fixture_date + timedelta(hours=3)).strftime('%H:%M')
        location = fixture.ground.value
        description = get_description(fixture)
        print(f"{subject},{start_date},{start_time},{end_time},{location},{description}")