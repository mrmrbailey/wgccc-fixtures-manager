from datetime import datetime, timezone, timedelta

import pytest

from src.fixture import Fixture
from src.cricket_enums import Location, FixtureType, Ground
from src.cricket_team import CricketTeam

base_cricket_team = CricketTeam.U17s
base_oppo = 'oppo'
base_location = Location.HOME
base_league = FixtureType.LEAGUE
base_start_date_time = datetime(2025, 4, 25, 17, 00, tzinfo=timezone.utc)
base_end_date_time = datetime(2025, 4, 25, 20, 00, tzinfo=timezone.utc)
base_ground = Ground.DP

base_fixture = Fixture(base_cricket_team, base_oppo, base_location, base_league, base_start_date_time, base_end_date_time, base_ground)

fixtures_equal_test_data = [
    (base_fixture, True),
    (Fixture(CricketTeam.U15s, base_oppo, base_location, base_league, base_start_date_time, base_end_date_time, base_ground),
     False),
    (Fixture(base_cricket_team, 'xyz', base_location, base_league, base_start_date_time, base_end_date_time, base_ground),
     False),
    (Fixture(base_cricket_team, base_oppo, base_location, FixtureType.CUP, base_start_date_time, base_end_date_time, base_ground),
     False),
    (Fixture(base_cricket_team, base_oppo, base_location, base_league, base_start_date_time + timedelta(days=1), base_end_date_time, base_ground),
     False),
    (Fixture(base_cricket_team, base_oppo, base_location, base_league, base_start_date_time, base_start_date_time + timedelta(days=1), base_ground),
     False),
    (Fixture(base_cricket_team, base_oppo, base_location, base_league, base_start_date_time, base_end_date_time, Ground.AWAY),
     False)
]

@pytest.mark.parametrize('other,expected', fixtures_equal_test_data,)
def test_fixture_equals(other, expected):
    assert base_fixture.__eq__(other) is expected

sort_fixture_date_test_data = [
    (base_fixture, False),
    (Fixture(base_cricket_team, base_oppo, base_location, base_league, base_start_date_time + timedelta(days=-1), base_end_date_time, base_ground),
     False),
    (Fixture(base_cricket_team, base_oppo, base_location, base_league, base_start_date_time + timedelta(days=1), base_end_date_time, base_ground),
     True),
    (Fixture(base_cricket_team, base_oppo, base_location, base_league, base_start_date_time + timedelta(minutes=-1), base_end_date_time, base_ground),
     False),
    (Fixture(base_cricket_team, base_oppo, base_location, base_league, base_start_date_time + timedelta(minutes=1), base_end_date_time, base_ground),
     True)
]

@pytest.mark.parametrize('other,expected', sort_fixture_date_test_data)
def test_fixture_less_than(other, expected):
    assert base_fixture.__lt__(other) is expected

test_data_for_to_string = ['WGCCC U17 v oppo Location.HOME 25/04/2025 18:00 21:00 Ground.DP FixtureType.LEAGUE']
@pytest.mark.parametrize('fixture_str', test_data_for_to_string)
def test_fixture_to_string(fixture_str):
    assert base_fixture.__str__() == fixture_str

test_data_for_report_string = ['wgc_team: CricketTeam.U17s, oppo: oppo, location: Location.HOME, type FixtureType.LEAGUE start_datetime: 2025-04-25 17:00:00+00:00, time: 2025-04-25 20:00:00+00:00, ground: Ground.DP']
@pytest.mark.parametrize('fixture_repr', test_data_for_report_string)
def test_fixture_strings(fixture_repr):
    assert base_fixture.__repr__() == fixture_repr

test_data_for_get_localized_fixture_start_datetime = ['25/04/2025 18:00']
@pytest.mark.parametrize('date_time_string', test_data_for_get_localized_fixture_start_datetime)
def test_get_localized_fixture_start_datetime(date_time_string):
    assert base_fixture.get_localized_fixture_start_datetime_string() == date_time_string

test_data_for_get_localized_fixture_start_date = ['25/04/2025']
@pytest.mark.parametrize('date_string', test_data_for_get_localized_fixture_start_date)
def test_get_localized_fixture_start_date(date_string):
    assert base_fixture.get_localized_fixture_start_date_string() == date_string

test_data_for_get_localized_fixture_start_time = ['18:00']
@pytest.mark.parametrize('time_string', test_data_for_get_localized_fixture_start_time)
def test_get_localized_fixture_start_time(time_string):
    assert base_fixture.get_localized_fixture_start_time_string() == time_string

match_up_test_data = [
    (base_fixture,'WGCCC U17 v oppo'),
    (Fixture(base_cricket_team, base_oppo, Ground.AWAY, base_league, base_start_date_time, base_end_date_time, base_ground),
     'oppo v WGCCC U17'),
    (Fixture(CricketTeam.NotWGCCC, base_oppo, base_location, base_league, base_start_date_time, base_end_date_time, base_ground),
     'oppo')
]
@pytest.mark.parametrize('fixture,expected', match_up_test_data)
def test_fixture_match_up(fixture, expected):
    assert fixture.get_matchup() == expected

description_test_data = [
    (base_fixture,
     'Welwyn Garden City CC - Under 17 v oppo on Fri 25 Apr 2025 at 17:00~League~HJCL U17 Group 3'),
    (Fixture(base_cricket_team, base_oppo, Ground.AWAY, base_league, base_start_date_time, base_end_date_time, base_ground),
     'oppo v Welwyn Garden City CC - Under 17 on Fri 25 Apr 2025 at 17:00~League~HJCL U17 Group 3'),
    (Fixture(base_cricket_team, base_oppo, base_location, FixtureType.CUP, base_start_date_time, base_end_date_time, base_ground),
     'Welwyn Garden City CC - Under 17 v oppo on Fri 25 Apr 2025 at 17:00~Cup'),
    (Fixture(CricketTeam.NotWGCCC, base_oppo, base_location, FixtureType.SENIOR, base_start_date_time, base_end_date_time, base_ground),
     'oppo on Fri 25 Apr 2025 at 17:00~Senior')
]
@pytest.mark.parametrize('fixture,expected', description_test_data)
def test_description_match_up(fixture, expected):
    assert fixture.get_description() == expected