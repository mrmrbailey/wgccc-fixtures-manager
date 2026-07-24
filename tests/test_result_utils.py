import pytest
from datetime import datetime, timezone, timedelta

from fixture import Fixture
from fixture_enums import Location, FixtureType, Ground
from cricket_team import CricketTeam
from result import Result
from result_utils import should_fixture_have_result

now = datetime.now(timezone.utc)

def make_fixture(start_datetime):
    return Fixture(CricketTeam.U17s, 'oppo', Location.HOME, FixtureType.LEAGUE,
                   start_datetime, start_datetime + timedelta(hours=3), Ground.DP, Result())

should_fixture_have_result_test_data = [
    (make_fixture(now - timedelta(days=4)), True),
    (make_fixture(now - timedelta(days=2)), False),
    (make_fixture(now + timedelta(days=1)), False),
]

@pytest.mark.parametrize('fixture, expected', should_fixture_have_result_test_data)
def test_should_fixture_have_result(fixture, expected):
    assert should_fixture_have_result(fixture) == expected
