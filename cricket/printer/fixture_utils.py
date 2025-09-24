from datetime import date, timedelta, datetime, timezone
from cricket_team import CricketTeam
from cricket_enums import Ground, FixtureType
from printer.googlecalendar_utils import print_fixtures_for_google_calendar_csv_import

def _get_fixtures_for_week(list_of_fixtures, week_number):
    fixtures_for_week = []
    for fixture in list_of_fixtures:
        if week_number == fixture.fixture_start_datetime.strftime("%V"):
            fixtures_for_week.append(fixture)
    return fixtures_for_week

def get_this_weeks_fixtures(list_of_fixtures):
    current_week_number = date.today().strftime("%V")
    return _get_fixtures_for_week(list_of_fixtures, current_week_number)

def get_next_weeks_fixtures(list_of_fixtures):
    next_week_number = (date.today() + timedelta(weeks=1)).strftime("%V")
    return get_this_weeks_fixtures(list_of_fixtures) + _get_fixtures_for_week(list_of_fixtures, next_week_number)

def get_future_fixtures(list_of_fixtures):
    future_fixtures = []
    current_date = datetime.now(tz=timezone.utc)
    for fixture in list_of_fixtures:
        if current_date <= fixture.fixture_start_datetime:
            future_fixtures.append(fixture)
    return future_fixtures

def get_fixtures_for_type(list_of_fixtures, *args):
    fixture_type = FixtureType(*args)
    fixtures_for_type = []
    for fixture in list_of_fixtures:
        if fixture_type == fixture.fixture_type:
            fixtures_for_type.append(fixture)
    return fixtures_for_type

def get_fixtures_for_ground(list_of_fixtures, *args):
    ground = Ground(*args)
    fixtures_for_ground = []
    for fixture in list_of_fixtures:
        if ground == fixture.ground:
            fixtures_for_ground.append(fixture)
    return fixtures_for_ground

def get_fixtures_for_home_next_week(list_of_fixtures):
    next_weeks_fixtures = get_next_weeks_fixtures(list_of_fixtures)
    return get_fixtures_for_ground(next_weeks_fixtures, Ground.DP) + get_fixtures_for_ground(next_weeks_fixtures, Ground.WPF)

def get_fixtures_for_team(list_of_fixtures, *args):
    cricket_team = CricketTeam(*args)
    fixtures_for_team = []
    for fixture in list_of_fixtures:
        if fixture.wgc_team == cricket_team:
            fixtures_for_team.append(fixture)
    return fixtures_for_team

def get_junior_fixtures(list_of_fixtures):
    junior_fixtures = []
    for fixture in list_of_fixtures:
        if fixture.fixture_type is not FixtureType.SENIOR:
            junior_fixtures.append(fixture)
    return junior_fixtures

def get_fixtures_for_google_calendar_csv_import(list_of_fixtures, *args):
    junior_fixtures = get_junior_fixtures(list_of_fixtures)
    junior_fixtures_for_ground = get_fixtures_for_ground(junior_fixtures, *args)
    print_fixtures_for_google_calendar_csv_import(junior_fixtures_for_ground)
    return junior_fixtures_for_ground