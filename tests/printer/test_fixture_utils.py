import pytest

from src.printer.fixture_utils import get_this_weeks_fixtures, get_next_weeks_fixtures, get_future_fixtures, get_fixtures_for_type, get_fixtures_for_ground, get_fixtures_for_home_next_week, get_fixtures_for_team, get_junior_fixtures, get_fixtures_for_google_calendar_csv_import
from src.fixture import Fixture
from src.cricket_enums import Location, FixtureType, Ground
from src.cricket_team import CricketTeam
from datetime import date, datetime, timezone, timedelta

today = date.today()

base_cricket_team = CricketTeam.U17s
base_oppo = 'oppo'
base_location = Location.HOME
base_fixture_type = FixtureType.LEAGUE
base_start_date_time = datetime(today.year, today.month, today.day, 18, 00, tzinfo=timezone.utc)
base_end_date_time = base_start_date_time + timedelta(hours=3)
base_ground = Ground.DP
base_fixture = Fixture(base_cricket_team, base_oppo, base_location, base_fixture_type, base_start_date_time, base_end_date_time, base_ground)
wpf_fixture = Fixture(base_cricket_team, base_oppo, base_location, base_fixture_type, base_start_date_time, base_end_date_time, Ground.WPF)
next_weeks_fixture = Fixture(base_cricket_team, base_oppo, base_location, base_fixture_type, base_start_date_time + timedelta(weeks=1), base_end_date_time, base_ground)
next_months_fixture = Fixture(base_cricket_team, base_oppo, base_location, base_fixture_type, base_start_date_time + timedelta(weeks=4), base_end_date_time, base_ground)

get_this_weeks_fixtures_test_data = [
    ([base_fixture,
    Fixture(base_cricket_team, base_oppo, base_location, base_fixture_type, base_start_date_time + timedelta(weeks=-1),
            base_end_date_time, base_ground),
    Fixture(base_cricket_team, base_oppo, base_location, base_fixture_type, base_start_date_time + timedelta(weeks=1),
            base_end_date_time, base_ground)],
    [base_fixture]),
    ([base_fixture,
      Fixture(base_cricket_team, base_oppo, base_location, base_fixture_type, base_start_date_time + timedelta(weeks=-1),
              base_end_date_time, base_ground),
      base_fixture,
      Fixture(base_cricket_team, base_oppo, base_location, base_fixture_type, base_start_date_time + timedelta(weeks=1),
              base_end_date_time, base_ground)],
     [base_fixture, base_fixture]),
    ([Fixture(base_cricket_team, base_oppo, base_location, base_fixture_type, base_start_date_time + timedelta(weeks=-1),
              base_end_date_time, base_ground)], []),
    ([],[])
]
@pytest.mark.parametrize('all_fixtures, this_weeks_fixtures', get_this_weeks_fixtures_test_data)
def test_get_this_weeks_fixtures(all_fixtures, this_weeks_fixtures):
    assert get_this_weeks_fixtures(all_fixtures) == this_weeks_fixtures

get_next_weeks_fixtures_test_data = [
    ([base_fixture, next_weeks_fixture,
    Fixture(base_cricket_team, base_oppo, base_location, base_fixture_type, base_start_date_time + timedelta(weeks=-1),
            base_end_date_time, base_ground),
    Fixture(base_cricket_team, base_oppo, base_location, base_fixture_type, base_start_date_time + timedelta(weeks=2),
            base_end_date_time, base_ground)],
    [base_fixture, next_weeks_fixture]),
    ([base_fixture, next_weeks_fixture,
      Fixture(base_cricket_team, base_oppo, base_location, base_fixture_type, base_start_date_time + timedelta(weeks=-1),
              base_end_date_time, base_ground),
      base_fixture,
      Fixture(base_cricket_team, base_oppo, base_location, base_fixture_type, base_start_date_time + timedelta(weeks=2),
              base_end_date_time, base_ground)],
     [base_fixture, base_fixture, next_weeks_fixture]),
    ([Fixture(base_cricket_team, base_oppo, base_location, base_fixture_type, base_start_date_time + timedelta(weeks=-1),
              base_end_date_time, base_ground)],[]),
    ([],[])
]
@pytest.mark.parametrize('all_fixtures, next_weeks_fixtures', get_next_weeks_fixtures_test_data)
def test_get_next_weeks_fixtures(all_fixtures, next_weeks_fixtures):
    assert get_next_weeks_fixtures(all_fixtures) == next_weeks_fixtures

get_future_fixtures_test_data = [
    ([base_fixture, next_weeks_fixture, next_months_fixture,
    Fixture(base_cricket_team, base_oppo, base_location, base_fixture_type, base_start_date_time + timedelta(weeks=-1),
            base_end_date_time, base_ground)],
    [base_fixture, next_weeks_fixture, next_months_fixture]),
    ([base_fixture, next_weeks_fixture, next_months_fixture,
      Fixture(base_cricket_team, base_oppo, base_location, base_fixture_type, base_start_date_time + timedelta(weeks=-1),
              base_end_date_time, base_ground),
      base_fixture],
     [base_fixture, next_weeks_fixture, next_months_fixture, base_fixture]),
    ([Fixture(base_cricket_team, base_oppo, base_location, base_fixture_type, base_start_date_time + timedelta(weeks=-1),
              base_end_date_time, base_ground)],[]),
    ([],[])
]
@pytest.mark.parametrize('all_fixtures, future_fixtures', get_future_fixtures_test_data)
def test_get_future_weeks_fixtures(all_fixtures, future_fixtures):
    assert get_future_fixtures(all_fixtures) == future_fixtures

get_fixtures_for_type_test_data = [
    ([base_fixture,
     Fixture(base_cricket_team, base_oppo, base_location, FixtureType.CUP, base_start_date_time, base_end_date_time,
             base_ground),],
     [base_fixture]),
    ([base_fixture, base_fixture,
      Fixture(base_cricket_team, base_oppo, base_location, FixtureType.SENIOR, base_start_date_time, base_end_date_time,
              base_ground),
     Fixture(base_cricket_team, base_oppo, base_location, FixtureType.FRIENDLY, base_start_date_time, base_end_date_time,
             base_ground)],
     [base_fixture, base_fixture]),
    ([Fixture(base_cricket_team, base_oppo, base_location, FixtureType.SENIOR, base_start_date_time, base_end_date_time,
              base_ground)],[]),
    ([],[])
]
@pytest.mark.parametrize('all_fixtures, fixtures_for_type', get_fixtures_for_type_test_data)
def test_get_fixtures_for_type(all_fixtures, fixtures_for_type):
    assert get_fixtures_for_type(all_fixtures, base_fixture_type) == fixtures_for_type

get_fixtures_for_ground_test_data = [
    ([base_fixture,
     Fixture(base_cricket_team, base_oppo, base_location, base_fixture_type, base_start_date_time, base_end_date_time,
             Ground.AWAY)],
     [base_fixture]),
    ([base_fixture, base_fixture,
      Fixture(base_cricket_team, base_oppo, base_location, base_fixture_type, base_start_date_time, base_end_date_time,
              Ground.WPF),
     Fixture(base_cricket_team, base_oppo, base_location, base_fixture_type, base_start_date_time, base_end_date_time,
             Ground.AWAY)],
     [base_fixture, base_fixture]),
    ([Fixture(base_cricket_team, base_oppo, base_location, base_fixture_type, base_start_date_time, base_end_date_time,
              Ground.WPF)],[]),
    ([],[])
]
@pytest.mark.parametrize('all_fixtures, fixtures_for_ground', get_fixtures_for_ground_test_data)
def test_get_fixtures_for_ground(all_fixtures, fixtures_for_ground):
    assert get_fixtures_for_ground(all_fixtures, base_ground) == fixtures_for_ground

get_fixtures_for_home_next_week_test_data = [
    ([base_fixture, wpf_fixture, next_weeks_fixture, next_months_fixture],
     [base_fixture, next_weeks_fixture, wpf_fixture]),
    ([base_fixture, wpf_fixture, next_weeks_fixture, base_fixture, next_months_fixture],
     [base_fixture, base_fixture, next_weeks_fixture, wpf_fixture]),
    ([next_months_fixture], []),
    ([],[])
]
@pytest.mark.parametrize('all_fixtures, fixtures_for_home_next_week', get_fixtures_for_home_next_week_test_data)
def test_get_fixtures_for_home_next_week(all_fixtures, fixtures_for_home_next_week):
    assert get_fixtures_for_home_next_week(all_fixtures) == fixtures_for_home_next_week

get_fixtures_for_team_test_data = [
    ([base_fixture,
     Fixture(CricketTeam.U11s, base_oppo, base_location, base_ground, base_start_date_time, base_end_date_time, base_ground)],
     [base_fixture]),
    ([Fixture(CricketTeam.U11s, base_oppo, base_location, base_ground, base_start_date_time, base_end_date_time, base_ground)],
     []),
    ([],[])
]
@pytest.mark.parametrize('all_fixtures, fixtures_for_team', get_fixtures_for_team_test_data)
def test_get_fixtures_for_team(all_fixtures, fixtures_for_team):
    assert get_fixtures_for_team(all_fixtures, base_cricket_team) == fixtures_for_team

get_junior_fixtures_test_data = [
    ([base_fixture,
     Fixture(base_cricket_team, base_oppo, base_location, FixtureType.SENIOR, base_start_date_time, base_end_date_time,
             base_ground)],
     [base_fixture]),
    ([base_fixture, base_fixture,
      Fixture(base_cricket_team, base_oppo, base_location, FixtureType.SENIOR, base_start_date_time, base_end_date_time,
              base_ground)],
     [base_fixture, base_fixture]),
    ([Fixture(base_cricket_team, base_oppo, base_location, FixtureType.SENIOR, base_start_date_time, base_end_date_time,
                  base_ground)],[]),
    ([],[])
]
@pytest.mark.parametrize('all_fixtures, junior_fixtures', get_junior_fixtures_test_data)
def test_get_junior_fixtures(all_fixtures, junior_fixtures):
    assert get_junior_fixtures(all_fixtures) == junior_fixtures

get_fixtures_for_google_calendar_csv_import_test_data = [
    ([base_fixture,
     Fixture(base_cricket_team, base_oppo, base_location, base_fixture_type, base_start_date_time, base_end_date_time,
             Ground.AWAY),
     Fixture(base_cricket_team, base_oppo, base_location, FixtureType.SENIOR, base_start_date_time, base_end_date_time,
             Ground.AWAY)],
     [base_fixture]),
    ([base_fixture, base_fixture,
      Fixture(base_cricket_team, base_oppo, base_location, base_fixture_type, base_start_date_time, base_end_date_time,
              Ground.AWAY),
      Fixture(base_cricket_team, base_oppo, base_location, FixtureType.SENIOR, base_start_date_time, base_end_date_time,
              Ground.AWAY)],
     [base_fixture, base_fixture]),
    ([Fixture(base_cricket_team, base_oppo, base_location, base_fixture_type, base_start_date_time, base_end_date_time,
              Ground.WPF)],[]),
    ([],[])
]
@pytest.mark.parametrize('all_fixtures, fixtures_for_google_calendar_csv_import', get_fixtures_for_google_calendar_csv_import_test_data)
def test_get_fixtures_for_google_calendar_csv_import(all_fixtures, fixtures_for_google_calendar_csv_import):
    assert get_fixtures_for_google_calendar_csv_import(all_fixtures, base_ground) == fixtures_for_google_calendar_csv_import
