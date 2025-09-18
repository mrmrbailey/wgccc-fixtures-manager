import pytest

from src.reader.playcricket_utils import get_wgc_team_from_division
from src.cricket_team import CricketTeam

division_test_data = [
    (CricketTeam.U11s.division, CricketTeam.U11s),
    ('XXX', CricketTeam.UNKNOWN)
]

@pytest.mark.parametrize('division,team', division_test_data)
def test_get_wgc_team_from_division(division, team):
    assert get_wgc_team_from_division(division) is team

