from zoneinfo import ZoneInfo

from cricket_team import CricketTeam
from cricket_enums import Location, FixtureType

class CompareFixture:
    def __init__(self, fixture):
        self.wgc_team = fixture.wgc_team
        self.oppo = fixture.oppo
        self.fixture_start_date = fixture.fixture_start_datetime
        self.fixture_type = fixture.fixture_type
        self.ground = fixture.ground

    def __eq__(self, other):
        return (self.wgc_team == other.wgc_team
                and self.get_localized_fixture_start_date_string() == other.get_localized_fixture_start_date_string()
                and self.ground == other.ground)

    def __str__(self):
        return f"{self.wgc_team.value} {self.oppo} {self.get_localized_fixture_start_date_string()} {self.ground}"

    def __repr__(self):
        return f"wgc_team: {self.wgc_team}, start_date: {self.fixture_start_date}, ground: {self.ground}"

    def __lt__(self, other):
        return self.fixture_start_date < other.fixture_start_date

    def get_localized_fixture_start_date_string(self):
        return self.fixture_start_date.astimezone(ZoneInfo('Europe/London')).strftime('%d/%m/%Y')
