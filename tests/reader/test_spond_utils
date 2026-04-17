import pytest

from reader.spond_utils import get_teams
from cricket_team import CricketTeam

teams_test_data = [
    ('Welwyn Garden City CC (H) - Bishop\'s Stortford CC (A)',
     ['Welwyn Garden City CC','Bishop\'s Stortford CC']),
    ('Old Albanian CC (H) - Welwyn Garden City CC (A)',
     ['Old Albanian CC','Welwyn Garden City CC']),
    ('Welwyn Beavers - Cricket intro',
     ['Not a WGCCC Team', 'Welwyn Beavers - Cricket intro']),
]

@pytest.mark.parametrize('summary,expected', teams_test_data)
def test_get_teams(summary, expected):
    assert get_teams(summary) == expected
