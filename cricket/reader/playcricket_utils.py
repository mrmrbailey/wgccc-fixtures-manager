# imports
from datetime import datetime, timezone, timedelta

from cricket_team import CricketTeam

days_to_wait_for_result = 3

def is_fixture_missing_result(fixture, result):

    result_not_entered = result == ""
    result_expected = fixture.fixture_start_datetime < datetime.now(timezone.utc).astimezone() + timedelta(days=-days_to_wait_for_result)

    return result_not_entered and result_expected


def add_fixture(team):
    match team:
        case CricketTeam.UNKNOWN:
            add = False
        case _:
            add = True
    return add
