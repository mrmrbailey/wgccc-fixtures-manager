import pytest

from src.reader.playcricket_utils import get_wgc_team_from_division, get_fixture_start_datetime
from src.cricket_team import CricketTeam

from datetime import datetime, timezone

division_test_data = [
    (CricketTeam.U11s.division, CricketTeam.U11s),
    ('XXX', CricketTeam.UNKNOWN)
]

@pytest.mark.parametrize('division,team', division_test_data)
def test_get_wgc_team_from_division(division, team):
    assert get_wgc_team_from_division(division) is team

get_fixture_start_date_timetest_data = [
    ('01/04/2025', "18:00", datetime(2025, 4, 1, 17, 00, tzinfo=timezone.utc)),
]

@pytest.mark.parametrize('date_string,time_string,expected', get_fixture_start_date_timetest_data)
def test_get_fixture_start_datetime(date_string, time_string, expected):
    assert get_fixture_start_datetime(date_string, time_string) == expected