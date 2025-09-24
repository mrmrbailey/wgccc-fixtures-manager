import pytest
from cricket_team import CricketTeam

cricket_team_get_value_test_data = [
    ('WGCCC U9', CricketTeam.U9s),
    ('XXX', CricketTeam.UNKNOWN)
]
@pytest.mark.parametrize('cricket_team_value,cricket_team', cricket_team_get_value_test_data)
def test_get_cricket_team_get_value(cricket_team_value, cricket_team):
    assert CricketTeam.get_value(cricket_team_value) == cricket_team


cricket_team_get_from_fullname_test_data = [
    ('Welwyn Garden City Cricket Club Saturday 1st XI', CricketTeam.FirstXI),
    ('XXX', CricketTeam.UNKNOWN)
]
@pytest.mark.parametrize('cricket_team_fullname,cricket_team', cricket_team_get_from_fullname_test_data)
def test_cricket_team_get_from_fullname(cricket_team_fullname, cricket_team):
    assert CricketTeam.get_from_fullname(cricket_team_fullname) == cricket_team