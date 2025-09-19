import pytest

from src.cricket_enums import Location, FixtureType, Ground
from src.cricket_team import CricketTeam
from src.fixture import Fixture
from src.printer.googlecalendar_utils import get_google_calendar_summary

from datetime import date, datetime, timezone, timedelta

base_oppo = 'oppo'
base_location = Location.HOME
base_fixture_type = FixtureType.LEAGUE
base_start_date_time = datetime(2025, 5, 9, 18, 00, tzinfo=timezone.utc)
base_end_date_time = base_start_date_time + timedelta(hours=3)
base_ground = Ground.DP


get_google_calendar_summary_test_data = [
    (Fixture(CricketTeam.GIRLS, base_oppo, base_location, base_fixture_type, base_start_date_time, base_end_date_time, base_ground),
     'WGCCC Girls U9 v oppo (15 yards)'),
    (Fixture(CricketTeam.GIRLS, base_oppo, Location.AWAY, base_fixture_type, base_start_date_time, base_end_date_time,
             base_ground),
     'oppo v WGCCC Girls U9 (15 yards)'),
    (Fixture(CricketTeam.U9s, base_oppo, base_location, base_fixture_type, base_start_date_time, base_end_date_time,
             base_ground),
     'WGCCC U9 v oppo (15 yards)'),
    (Fixture(CricketTeam.U10s, base_oppo, base_location, base_fixture_type, base_start_date_time, base_end_date_time,
             base_ground),
     'WGCCC U10B v oppo (17 yards)'),
    (Fixture(CricketTeam.U11s, base_oppo, base_location, base_fixture_type, base_start_date_time, base_end_date_time,
             base_ground),
     'WGCCC U11 v oppo (17 yards)'),
    (Fixture(CricketTeam.U12s, base_oppo, base_location, base_fixture_type, base_start_date_time, base_end_date_time,
             base_ground),
     'WGCCC U12 v oppo (19 yards)'),
    (Fixture(CricketTeam.U13s, base_oppo, base_location, base_fixture_type, base_start_date_time, base_end_date_time,
             base_ground),
     'WGCCC U13 v oppo (19 yards)'),
    (Fixture(CricketTeam.U14s, base_oppo, Location.HOME, base_fixture_type, base_start_date_time, base_end_date_time,
             base_ground),
     'WGCCC U14B v oppo (22 yards)'),
    (Fixture(CricketTeam.U15s, base_oppo, base_location, base_fixture_type, base_start_date_time, base_end_date_time,
             base_ground),
     'WGCCC U15 v oppo (22 yards)'),
    (Fixture(CricketTeam.U17s, base_oppo, base_location, base_fixture_type, base_start_date_time, base_end_date_time,
             base_ground),
     'WGCCC U17 v oppo (22 yards)'),
    (Fixture(CricketTeam.UNKNOWN, base_oppo, base_location, base_fixture_type, base_start_date_time, base_end_date_time,
             base_ground),
     'Unknown v oppo (? yards)'),
    (Fixture(CricketTeam.U17s, base_oppo, base_location, FixtureType.SENIOR, base_start_date_time, base_end_date_time,
             base_ground),
     'WGCCC U17 v oppo'),
]
@pytest.mark.parametrize('fixture,google_calendar_summary', get_google_calendar_summary_test_data)
def test_get_google_calendar_summary(fixture, google_calendar_summary):
    assert get_google_calendar_summary(fixture) == google_calendar_summary