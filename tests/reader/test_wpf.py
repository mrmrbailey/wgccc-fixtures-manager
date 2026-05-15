import pytest

from datetime import datetime, timezone, timedelta

from reader.wpf import parse_record
from fixture import Fixture
from cricket_enums import Location, FixtureType, Ground
from cricket_team import CricketTeam

base_start_date_time = datetime(2026, 5, 19, 17, 00, tzinfo=timezone.utc)
base_end_date_time = datetime(2026, 5, 19, 20, 00, tzinfo=timezone.utc)

parse_record_test_data = [
    (['19/05/2026', 'WGCCC U10B', 'Letchworth Garden City CC - Under 10 B', 'Astro'],
     Fixture(CricketTeam.U10s, 'Letchworth Garden City CC - Under 10 B', Location.HOME, FixtureType.LEAGUE, base_start_date_time, base_end_date_time, Ground.WPF)),
]
@pytest.mark.parametrize('record,expected_fixture', parse_record_test_data)
def test_parse_record(record, expected_fixture):
    assert parse_record(record) == expected_fixture
