import unittest
from datetime import datetime, timezone

from src.fixture import Fixture
from src.cricket_enums import Location, FixtureType, Ground
from src.cricket_team import CricketTeam

def get_wgc_team():
    return CricketTeam.U17s

def get_oppo():
    return "Away Team"

def get_location():
    return Location.AWAY

def get_league_fixture_type():
    return FixtureType.LEAGUE

def get_fixture_date():
    return '25/04/2025'

def get_fixture_start_time():
    return '18:00'

def get_ground():
    return Ground.DP

def get_fixture(wgc_team, oppo, location, fixture_type, fixture_date, fixture_time, ground):
    return Fixture(wgc_team, oppo, location, fixture_type, fixture_date, fixture_time, ground)

def get_default_fixture():
    return(get_fixture(
               get_wgc_team(),
               get_oppo(),
               get_location(),
               get_league_fixture_type(),
               get_fixture_date(),
               get_fixture_start_time(),
               get_ground()
           ))

class TestFixture(unittest.TestCase):

    def test_fixture_creation(self):
        # Create a Fixture instance
        fixture = get_default_fixture()

        # Assert that the attributes are set correctly
        self.assertEqual(fixture.wgc_team, get_wgc_team())
        self.assertEqual(fixture.oppo, get_oppo())
        self.assertEqual(fixture.location, get_location())
        self.assertEqual(fixture.fixture_type, FixtureType.LEAGUE)
        self.assertEqual(fixture.fixture_date, get_fixture_date())
        self.assertEqual(fixture.fixture_time, get_fixture_start_time())
        self.assertEqual(fixture.ground, get_ground())

    def test_fixture_eq_same(self):
        fixture = get_default_fixture()
        same_fixture = get_default_fixture()

        self.assertEqual(fixture, same_fixture)

    def test_fixture_not_equal_different_wgc_teams(self):
        fixture = get_default_fixture()
        different_fixture = get_default_fixture()
        different_fixture.wgc_team = CricketTeam.U15s

        self.assertNotEqual(fixture, different_fixture)


    def test_fixture_not_equal_different_oppo(self):
        fixture = get_default_fixture()
        different_fixture = get_default_fixture()
        different_fixture.oppo = "XYZ"

        self.assertNotEqual(fixture, different_fixture)

    def test_fixture_not_equal_different_location(self):
        fixture = get_default_fixture()
        different_fixture = get_default_fixture()
        different_fixture.location = Location.HOME

        self.assertNotEqual(fixture, different_fixture)

    def test_fixture_not_equal_different_date(self):
        fixture = get_default_fixture()
        different_fixture = get_default_fixture()
        different_fixture.fixture_date = '02/04/2025'
        self.assertNotEqual(fixture, different_fixture)

    def test_fixture_not_equal_different_time(self):
        fixture = get_default_fixture()
        different_fixture = get_default_fixture()
        different_fixture.fixture_time = '17:30'
        self.assertNotEqual(fixture, different_fixture)

    def test_fixture_not_equal_different_ground(self):
        fixture = get_default_fixture()
        different_fixture = get_default_fixture()
        different_fixture.ground = Ground.AWAY
        self.assertNotEqual(fixture, different_fixture)

    def test_fixture_less_than(self):
        fixture = get_default_fixture()
        future_fixture = get_default_fixture()
        future_fixture.fixture_date = '01/06/2025'
        self.assertTrue(fixture < future_fixture)

    def test_fixture_greater_than(self):
        fixture = get_default_fixture()
        past_fixture = get_default_fixture()
        past_fixture.fixture_date = '01/04/2025'
        self.assertTrue(fixture > past_fixture)

    def test_fixture_get_fixture_date(self):
        fixture = get_default_fixture()
        expected_fixture_date = datetime(2025, 4, 25, 18, tzinfo=timezone.utc)
        self.assertEqual(fixture.get_fixture_date(), expected_fixture_date)

    def test_fixture_print(self):
        fixture = get_default_fixture()
        expected_string = 'CricketTeam.U17s and Away Team Location.AWAY 25/04/2025 18:00 Ground.DP FixtureType.LEAGUE'
        self.assertEqual(fixture.__str__(), expected_string)

    def test_fixture_print_repr(self):
        fixture = get_default_fixture()
        expected_string = 'wgc_team: CricketTeam.U17s, oppo: Away Team, location: Location.AWAY, type FixtureType.LEAGUE date: 25/04/2025, time: 18:00, ground: Ground.DP'
        self.assertEqual(fixture.__repr__(), expected_string)

if __name__ == '__main__':
    unittest.main()