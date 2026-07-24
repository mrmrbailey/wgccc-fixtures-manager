import pytest

from datetime import datetime, timezone, timedelta

from fixture import Fixture
from comparator.compare_fixture import CompareFixture
from fixture_enums import Location, FixtureType, Ground
from cricket_team import CricketTeam
from reader import csv_utils
from result import Result

base_cricket_team = CricketTeam.U17s
base_oppo = 'oppo'
base_location = Location.HOME
base_league = FixtureType.LEAGUE
base_start_date_time = datetime(2025, 4, 25, 17, 00, tzinfo=timezone.utc)
base_end_date_time = datetime(2025, 4, 25, 20, 00, tzinfo=timezone.utc)
gmt_start_time = datetime(2026, 12, 25, 17, 00, tzinfo=timezone.utc)
bst_start_time = datetime(2026, 6, 25, 17, 00, tzinfo=timezone.utc)
base_ground = Ground.DP
base_result = Result()
base_fixture = CompareFixture(Fixture(base_cricket_team, base_oppo, base_location, base_league, base_start_date_time, base_end_date_time, base_ground, base_result))

fixtures_equal_test_data = [
    (base_fixture, True),
    (CompareFixture(Fixture(CricketTeam.U15s, base_oppo, base_location, base_league, base_start_date_time, base_end_date_time, base_ground, base_result)),
     False),
    (CompareFixture(Fixture(base_cricket_team, 'xyz', base_location, base_league, base_start_date_time, base_end_date_time, base_ground, base_result)),
     True),
    (CompareFixture(Fixture(base_cricket_team, base_oppo, base_location, base_league, base_start_date_time + timedelta(days=1), base_end_date_time, base_ground, base_result)),
     False),
    (CompareFixture(Fixture(base_cricket_team, base_oppo, base_location, base_league, base_start_date_time + timedelta(hours=1), base_end_date_time, base_ground, base_result)),
     True),
    (CompareFixture(Fixture(base_cricket_team, base_oppo, base_location, base_league, base_start_date_time, base_start_date_time + timedelta(days=1), base_ground, base_result)),
     True),
    (CompareFixture(Fixture(base_cricket_team, base_oppo, base_location, base_league, base_start_date_time, base_end_date_time, Ground.AWAY, base_result)),
     False)
]

@pytest.mark.parametrize('other,expected', fixtures_equal_test_data,)
def test_fixture_equals(other, expected):
    assert base_fixture.__eq__(other) is expected

sort_fixture_date_test_data = [
    (base_fixture, False),
    (CompareFixture(Fixture(base_cricket_team, base_oppo, base_location, base_league, base_start_date_time + timedelta(days=-1), base_end_date_time, base_ground, base_result)),
     False),
    (CompareFixture(Fixture(base_cricket_team, base_oppo, base_location, base_league, base_start_date_time + timedelta(days=1), base_end_date_time, base_ground, base_result)),
     True),
    (CompareFixture(Fixture(base_cricket_team, base_oppo, base_location, base_league, base_start_date_time + timedelta(minutes=-1), base_end_date_time, base_ground, base_result)),
     False),
    (CompareFixture(Fixture(base_cricket_team, base_oppo, base_location, base_league, base_start_date_time + timedelta(minutes=1), base_end_date_time, base_ground, base_result)),
     True)
]

@pytest.mark.parametrize('other,expected', sort_fixture_date_test_data)
def test_fixture_less_than(other, expected):
    assert base_fixture.__lt__(other) is expected

test_data_for_to_string = ['WGCCC U17 oppo 25/04/2025 Digswell Park']
@pytest.mark.parametrize('fixture_str', test_data_for_to_string)
def test_fixture_to_string(fixture_str):
    assert base_fixture.__str__() == fixture_str

test_data_for_report_string = ['wgc_team: CricketTeam.U17s, start_date: 2025-04-25 17:00:00+00:00, ground: Digswell Park']
@pytest.mark.parametrize('fixture_repr', test_data_for_report_string)
def test_fixture_strings(fixture_repr):
    assert base_fixture.__repr__() == fixture_repr

test_data_for_get_localized_fixture_start_datetime = [
    (CompareFixture(Fixture(base_cricket_team, base_oppo, base_location, base_league, gmt_start_time, gmt_start_time + timedelta(hours=3), base_ground, base_result))
         , '25/12/2026'),
    (CompareFixture(Fixture(base_cricket_team, base_oppo, base_location, base_league, bst_start_time, bst_start_time + timedelta(hours=3), base_ground, base_result))
         , '25/06/2026')
]

test_data_for_get_localized_fixture_start_date = ['25/04/2025']
@pytest.mark.parametrize('date_string', test_data_for_get_localized_fixture_start_date)
def test_get_localized_fixture_start_date(date_string):
    assert base_fixture.get_localized_fixture_start_date_string() == date_string

today_start_date_time = csv_utils.get_fixture_start_datetime(datetime.now().strftime("%d/%m/%Y"), '18:00')
today_end_date_time = csv_utils.get_fixture_end_datetime(today_start_date_time)

test_data_for_is_valid = [
    (CompareFixture(Fixture(base_cricket_team, base_oppo, base_location, base_league, today_start_date_time, today_end_date_time, base_ground, base_result)),
     True),
    (CompareFixture(Fixture(base_cricket_team, base_oppo, base_location, FixtureType.SENIOR, today_start_date_time, today_end_date_time, base_ground, base_result)),
     False),
    (CompareFixture(Fixture(base_cricket_team, base_oppo, base_location, base_league, today_start_date_time + timedelta(days=1), today_end_date_time + timedelta(days=1), base_ground, base_result)),
     True),
    (CompareFixture(Fixture(base_cricket_team, base_oppo, base_location, base_league, today_start_date_time + timedelta(days=-1), today_end_date_time + timedelta(days=-1), base_ground, base_result)),
     False)
]
@pytest.mark.parametrize('fixture, expected', test_data_for_is_valid)
def test_fixture_is_valid(fixture, expected):
    assert fixture.is_valid() == expected
