import unittest
from datetime import datetime
from src.fixture import Fixture
from src.cricket_enums import MatchType, Venue, Result, Competition

class TestFixture(unittest.TestCase):

    def test_fixture_creation(self):
        # Create a Fixture instance
        test_date = datetime(2023, 10, 27)
        fixture = Fixture(
            date=test_date,
            opposition="Test Team",
            match_type=MatchType.LEAGUE,
            venue=Venue.HOME,
            result=Result.WIN,
            competition=Competition.PREMIER,
            scorecard="test_scorecard.html"
        )

        # Assert that the attributes are set correctly
        self.assertEqual(fixture.date, test_date)
        self.assertEqual(fixture.opposition, "Test Team")
        self.assertEqual(fixture.match_type, MatchType.LEAGUE)
        self.assertEqual(fixture.venue, Venue.HOME)
        self.assertEqual(fixture.result, Result.WIN)
        self.assertEqual(fixture.competition, Competition.PREMIER)
        self.assertEqual(fixture.scorecard, "test_scorecard.html")

if __name__ == '__main__':
    unittest.main()