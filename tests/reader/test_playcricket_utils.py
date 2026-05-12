import pytest

from datetime import date, datetime, timezone, timedelta

from cricket_enums import Location, FixtureType, Ground
from fixture import Fixture
from reader.playcricket_utils import add_fixture, is_fixture_missing_result
from cricket_team import CricketTeam

base_cricket_team = CricketTeam.U17s
base_oppo = 'oppo'
base_location = Location.HOME
base_fixture_type = FixtureType.LEAGUE
base_start_date_time = datetime(date.today().year, date.today().month, date.today().day, 18, 00, tzinfo=timezone.utc)
base_end_date_time = base_start_date_time + timedelta(hours=3)
base_ground = Ground.DP

is_fixture_missing_result_test_data = [
    (Fixture(base_cricket_team, base_oppo, base_location, base_fixture_type, base_start_date_time, base_end_date_time, Ground.DP),
     "",
     False),
    (Fixture(base_cricket_team, base_oppo, base_location, base_fixture_type, base_start_date_time + timedelta(days=-4), base_end_date_time,
             Ground.DP),
     "Result",
     False),
    (Fixture(base_cricket_team, base_oppo, base_location, base_fixture_type, base_start_date_time + timedelta(days=-4),
             base_end_date_time,
             Ground.DP),
     "",
     True),
]
@pytest.mark.parametrize('fixture,result,expected', is_fixture_missing_result_test_data)
def test_is_fixture_missing_result(fixture, result, expected):
    assert is_fixture_missing_result(fixture, result) is expected

add_fixture_test_data = [
    (CricketTeam.U17s, True),
    (CricketTeam.UNKNOWN, False),
]
@pytest.mark.parametrize('cricket_team,expected', add_fixture_test_data)
def test_add_fixture(cricket_team, expected):
    assert add_fixture(cricket_team) is expected
