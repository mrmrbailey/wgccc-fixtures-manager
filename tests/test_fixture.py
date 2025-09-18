from datetime import datetime, timezone

import pytest

from src.fixture import Fixture
from src.cricket_enums import Location, FixtureType, Ground
from src.cricket_team import CricketTeam

equalstestdata = [(Fixture(CricketTeam.U17s, 'oppo', Location.HOME, FixtureType.LEAGUE, '25/04/2025', '18:00', Ground.DP),
             Fixture(CricketTeam.U17s, 'oppo', Location.HOME, FixtureType.LEAGUE, '25/04/2025', '18:00', Ground.DP),
             True),
            (Fixture(CricketTeam.U17s, 'oppo', Location.HOME, FixtureType.LEAGUE, '25/04/2025', '18:00', Ground.DP),
             Fixture(CricketTeam.U15s, 'oppo', Location.HOME, FixtureType.LEAGUE, '25/04/2025', '18:00', Ground.DP),
             False),
            (Fixture(CricketTeam.U17s, 'oppo', Location.HOME, FixtureType.LEAGUE, '25/04/2025', '18:00', Ground.DP),
             Fixture(CricketTeam.U17s, 'xyz', Location.HOME, FixtureType.LEAGUE, '25/04/2025', '18:00', Ground.DP),
             False),
            (Fixture(CricketTeam.U17s, 'oppo', Location.HOME, FixtureType.LEAGUE, '25/04/2025', '18:00', Ground.DP),
             Fixture(CricketTeam.U17s, 'oppo', Location.HOME, FixtureType.CUP, '25/04/2025', '18:00', Ground.DP),
             False),
            (Fixture(CricketTeam.U17s, 'oppo', Location.HOME, FixtureType.LEAGUE, '25/04/2025', '18:00', Ground.DP),
             Fixture(CricketTeam.U17s, 'oppo', Location.HOME, FixtureType.LEAGUE, '26/04/2025', '18:00', Ground.DP),
             False),
            (Fixture(CricketTeam.U17s, 'oppo', Location.HOME, FixtureType.LEAGUE, '25/04/2025', '18:00', Ground.DP),
             Fixture(CricketTeam.U17s, 'oppo', Location.HOME, FixtureType.LEAGUE, '25/04/2025', '17:30', Ground.DP),
             False),
            (Fixture(CricketTeam.U17s, 'oppo', Location.HOME, FixtureType.LEAGUE, '25/04/2025', '18:00', Ground.DP),
             Fixture(CricketTeam.U17s, 'oppo', Location.HOME, FixtureType.LEAGUE, '25/04/2025', '18:00', Ground.AWAY),
             False)]

def idfn(val):
    if isinstance(val, Fixture):
        return val.__str__()

@pytest.mark.parametrize('fixture,other,expected', equalstestdata, ids=idfn)
def test_fixture_equals(fixture, other, expected):
    assert fixture.__eq__(other) is expected

sorttestdata = [(Fixture(CricketTeam.U17s, 'oppo', Location.HOME, FixtureType.LEAGUE, '25/04/2025', '18:00', Ground.DP),
             Fixture(CricketTeam.U17s, 'oppo', Location.HOME, FixtureType.LEAGUE, '25/04/2025', '18:00', Ground.DP),
             False),
            (Fixture(CricketTeam.U17s, 'oppo', Location.HOME, FixtureType.LEAGUE, '25/04/2025', '18:00', Ground.DP),
             Fixture(CricketTeam.U17s, 'oppo', Location.HOME, FixtureType.LEAGUE, '05/04/2025', '18:00', Ground.DP),
             False),
            (Fixture(CricketTeam.U17s, 'oppo', Location.HOME, FixtureType.LEAGUE, '25/04/2025', '18:00', Ground.DP),
             Fixture(CricketTeam.U17s, 'oppo', Location.HOME, FixtureType.LEAGUE, '01/05/2025', '18:00', Ground.DP),
             True),
            (Fixture(CricketTeam.U17s, 'oppo', Location.HOME, FixtureType.LEAGUE, '25/04/2025', '18:00', Ground.DP),
             Fixture(CricketTeam.U17s, 'oppo', Location.HOME, FixtureType.LEAGUE, '25/04/2025', '17:59', Ground.DP),
             False),
            (Fixture(CricketTeam.U17s, 'oppo', Location.HOME, FixtureType.LEAGUE, '25/04/2025', '18:00', Ground.DP),
             Fixture(CricketTeam.U17s, 'oppo', Location.HOME, FixtureType.LEAGUE, '25/04/2025', '18:01', Ground.DP),
             True)]

@pytest.mark.parametrize('fixture,other,expected', sorttestdata, ids=idfn)
def test_fixture_less_than(fixture, other, expected):
    assert fixture.__lt__(other) is expected

datetestdata = [(Fixture(CricketTeam.U17s, 'oppo', Location.HOME, FixtureType.LEAGUE, '25/04/2025', '18:00', Ground.DP),
                datetime(2025, 4, 25, 18, tzinfo=timezone.utc)),
                (Fixture(CricketTeam.U17s, 'oppo', Location.HOME, FixtureType.LEAGUE, '25/04/2025', '17:30', Ground.DP),
                 datetime(2025, 4, 25, 17, 30, tzinfo=timezone.utc))
                ]

@pytest.mark.parametrize('fixture,expected_date', datetestdata, ids=idfn)
def test_fixture_get_fixture_date(fixture, expected_date):
    fixture_date = fixture.get_fixture_date()
    assert fixture_date == expected_date

outputtestdata = [(Fixture(CricketTeam.U17s, 'oppo', Location.HOME, FixtureType.LEAGUE, '25/04/2025', '18:00', Ground.DP),
                   'CricketTeam.U17s and oppo Location.HOME 25/04/2025 18:00 Ground.DP FixtureType.LEAGUE',
                   'wgc_team: CricketTeam.U17s, oppo: oppo, location: Location.HOME, type FixtureType.LEAGUE date: 25/04/2025, time: 18:00, ground: Ground.DP')]

@pytest.mark.parametrize('fixture,fixture_str,fixture_repr', outputtestdata)
def test_fixture_strings(fixture, fixture_str, fixture_repr):
    assert fixture.__str__() == fixture_str
    assert fixture.__repr__() == fixture_repr
