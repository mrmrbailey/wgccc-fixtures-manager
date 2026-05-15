import pytest
from fixture_enums import FixtureType, Ground

ground_test_data = [
    ('Digswell Park', Ground.DP),
    ('XXX', Ground.AWAY)
]
@pytest.mark.parametrize('ground_value, ground', ground_test_data)
def test_ground(ground_value, ground):
    assert Ground.get_value(ground_value) == ground

fixture_type_get_value_test_data = [
    ('Cup', FixtureType.CUP),
    ('XXX', FixtureType.UNKNOWN)
]
@pytest.mark.parametrize('fixture_type_value,fixture_type', fixture_type_get_value_test_data)
def test_fixture_type_get_value(fixture_type_value, fixture_type):
    assert FixtureType.get_value(fixture_type_value) is fixture_type