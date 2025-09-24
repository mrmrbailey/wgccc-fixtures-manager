import pytest
from cricket_enums import FixtureType

fixture_type_get_value_test_data = [
    ('Cup', FixtureType.CUP),
    ('XXX', FixtureType.UNKNOWN)
]
@pytest.mark.parametrize('fixture_type_value,fixture_type', fixture_type_get_value_test_data)
def test_fixture_type_get_value(fixture_type_value, fixture_type):
    assert FixtureType.get_value(fixture_type_value) is fixture_type
