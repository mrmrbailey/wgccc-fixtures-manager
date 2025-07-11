import pytest
from datetime import datetime
from cricket.fixture import Fixture
from cricket.cricket_enums import Division, FixtureType, Ground


@pytest.fixture
def a_fixture():
    return Fixture(
        'Home Team',
        'Away Team',
        Division.U17s,
        FixtureType.FRIENDLY,
        datetime(2025,1,1,hour=18),
        datetime(2025, 1, 1, hour=18),
        Ground.DP
    )

def test_create_fixture(a_fixture):
    assert a_fixture.ground == Ground.DP

