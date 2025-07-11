import unittest
from datetime import datetime
from src.fixture import Fixture
from src.cricket_enums import Division, Ground

class TestFixture(unittest.TestCase):

    @staticmethod
    def get_home_team():
        return "Home Team"

    @staticmethod
    def get_away_team():
        return "Away Team"

    @staticmethod
    def get_fixture_date():
        return datetime(2023, 10, 27,hour=18)

    @staticmethod
    def get_divsion():
        return Division.U17s

    @staticmethod
    def get_ground():
        return Ground.DP

    def get_fixture(self):
        return Fixture(
            home = self.get_home_team(),
            away = self.get_away_team(),
            division = self.get_divsion(),
            fixture_date = self.get_fixture_date(),
            fixture_time = self.get_fixture_date(),
            ground = self.get_ground()
        )

    def test_fixture_creation(self):
        # Create a Fixture instance
        fixture = self.get_fixture()

        # Assert that the attributes are set correctly
        self.assertEqual(fixture.home, self.get_home_team())
        self.assertEqual(fixture.away, self.get_away_team())
        self.assertEqual(fixture.division, self.get_divsion())
        self.assertEqual(fixture.fixture_date, self.get_fixture_date())
        self.assertEqual(fixture.fixture_time, self.get_fixture_date())
        self.assertEqual(fixture.ground, self.get_ground())

    def test_fixture_eq_same(self):
        fixture = self.get_fixture()
        same_fixture = self.get_fixture()

        self.assertEqual(fixture, same_fixture)

if __name__ == '__main__':
    unittest.main()