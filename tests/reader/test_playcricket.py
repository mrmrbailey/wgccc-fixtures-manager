import pytest

from datetime import datetime, timezone, timedelta

from reader.playcricket import parse_record
from fixture import Fixture
from cricket_enums import Location, FixtureType, Ground
from cricket_team import CricketTeam

base_start_date_time = datetime(2026, 7, 2, 17, 00, tzinfo=timezone.utc)
base_end_date_time = datetime(2026, 7, 2, 20, 00, tzinfo=timezone.utc)

parse_record_test_data = [
    (['2/07/2026', 'Welwyn Garden City CC - Under 10 B', 'Hitchin CC - Under 10 B', 'League', 'U10B Group 2', '18:00', 'Digswell Park', '', '', '', '', '', '', '7509046', '', '0', '0', '0', '0', '0', '0', '0', '0', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
     Fixture(CricketTeam.U10s, 'Hitchin CC - Under 10 B', Location.HOME, FixtureType.LEAGUE, base_start_date_time, base_end_date_time, Ground.DP)),
    (['02/07/2026', 'Welwyn Garden City CC - Under 13 A', 'Old Albanian CC - U13A 2', 'League', 'U13A Group 3', '18:00', 'Welwyn Playing Fields', '', '', '', '', '', '', '7466518', '', '0', '0', '0', '0', '0', '0', '0', '0', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
     Fixture(CricketTeam.U13s, 'Old Albanian CC - U13A 2', Location.HOME, FixtureType.LEAGUE, base_start_date_time, base_end_date_time, Ground.WPF)),
    (['02/07/2026', 'Harpenden CC - Under 14', 'Welwyn Garden City CC - Under 14 A', 'League', 'U14A Group 1', '18:00', '', '', '', '', '', '', '', '7466719', '', '0', '0', '0', '0', '0', '0', '0', '0', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
     Fixture(CricketTeam.U14s, 'Harpenden CC - Under 14', Location.AWAY, FixtureType.LEAGUE, base_start_date_time, base_end_date_time, Ground.AWAY)),
    (['2/07/2026', 'Welwyn Garden City CC - Under 11', 'Hitchin CC - Under 11', 'Cup', 'U10B Group 2', '18:00', 'Digswell Park', '', '', '', '', '', '', '7509046', '', '0', '0', '0', '0', '0', '0', '0', '0', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
     Fixture(CricketTeam.U11s, 'Hitchin CC - Under 11', Location.HOME, FixtureType.CUP, base_start_date_time, base_end_date_time, Ground.DP)),
    (['2/07/2026', 'Welwyn Garden City CC - Under 11', 'Hitchin CC - Under 11', 'Friendly', 'U10B Group 2', '18:00', 'Digswell Park', '', '', '', '', '', '', '7509046', '', '0', '0', '0', '0', '0', '0', '0', '0', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
     Fixture(CricketTeam.U11s, 'Hitchin CC - Under 11', Location.HOME, FixtureType.FRIENDLY, base_start_date_time, base_end_date_time, Ground.DP)),
    (['02/07/2026', 'Harpenden CC - Under 14', 'Welwyn Garden City CC - Under 11', 'Friendly', 'U14A Group 1', '18:00', '', '', '', '', '', '', '', '7466719', '', '0', '0', '0', '0', '0', '0', '0', '0', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
     Fixture(CricketTeam.U11s, 'Harpenden CC - Under 14', Location.AWAY, FixtureType.FRIENDLY, base_start_date_time, base_end_date_time, Ground.AWAY)),
    (['02/07/2026', 'Harpenden CC - Under 14', 'UNKNOWN', 'Friendly', 'U14A Group 1', '18:00', '', '', '', '', '', '', '', '7466719', '', '0', '0', '0', '0', '0', '0', '0', '0', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
     Fixture(CricketTeam.UNKNOWN, 'Harpenden CC - Under 14', Location.AWAY, FixtureType.FRIENDLY, base_start_date_time, base_end_date_time, Ground.AWAY)),
]
@pytest.mark.parametrize('record,expected_fixture', parse_record_test_data)
def test_parse_record(record, expected_fixture):
    assert parse_record(record) == expected_fixture
