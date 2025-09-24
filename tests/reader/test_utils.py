import pytest

from cricket_team import CricketTeam
from reader.utils import add_fixture

add_fixture_test_data = [
    (CricketTeam.U17s, True),
    (CricketTeam.UNKNOWN, False),
]

@pytest.mark.parametrize('cricket_team,expected', add_fixture_test_data)
def test_add_fixture(cricket_team, expected):
    assert add_fixture(cricket_team) is expected