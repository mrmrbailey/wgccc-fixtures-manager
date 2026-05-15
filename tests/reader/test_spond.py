import pytest

from datetime import datetime, timezone, timedelta

from reader.spond import parse_record
from fixture import Fixture
from fixture_enums import Location, FixtureType, Ground
from cricket_team import CricketTeam

base_start_date_time = datetime(2026, 5, 13, 17, 00, tzinfo=timezone.utc)
base_end_date_time = datetime(2026, 5, 13, 20, 00, tzinfo=timezone.utc)

parse_record_test_data = [
    (['Potters Bar CC (H) - Welwyn Garden City CC (A)', '13/05/2026', 'WGCCC Juniors', 'Cheryl Worman', '12', ''],
     Fixture(CricketTeam.U13s, 'Potters Bar CC', Location.AWAY, FixtureType.LEAGUE, base_start_date_time, base_end_date_time, Ground.AWAY)),
    (['Welwyn Garden City CC (H) - Wheathampstead CC (A)', '13/05/2026', 'WGCCC Juniors', 'Bharat Ranavaya', '12', 'Digswell Park'],
     Fixture(CricketTeam.U9s, 'Wheathampstead CC', Location.HOME, FixtureType.LEAGUE, base_start_date_time, base_end_date_time, Ground.DP)),
]
@pytest.mark.parametrize('record,expected_fixture', parse_record_test_data)
def test_parse_record(record, expected_fixture):
    assert parse_record(record) == expected_fixture
