import pytest

from src.comparator.compare_fixture_lists import get_different_fixtures
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

get_different_fixtures_test_data = [
    ([base_fixture, wpf_fixture, next_weeks_fixture, next_months_fixture],
     [base_fixture, wpf_fixture, next_weeks_fixture, next_months_fixture],
     []),
    ([],
     [base_fixture, wpf_fixture, next_weeks_fixture, next_months_fixture],
     [base_fixture, wpf_fixture, next_weeks_fixture, next_months_fixture]),
    ([base_fixture, wpf_fixture, next_weeks_fixture, next_months_fixture],
     [],
     [base_fixture, wpf_fixture, next_weeks_fixture, next_months_fixture]),
    ([base_fixture, wpf_fixture, next_weeks_fixture, next_months_fixture],
     [base_fixture, next_weeks_fixture, next_months_fixture],
     [wpf_fixture]),
    ([],[], [])
]
@pytest.mark.parametrize('source_list, target_list, differences', get_different_fixtures_test_data)
def test_get_this_weeks_fixtures(source_list, target_list, differences):
    assert get_different_fixtures(source_list, target_list) == differences
