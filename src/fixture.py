import pytz

from src.cricket_team import CricketTeam
from src.cricket_enums import Location, FixtureType


class Fixture:
    def __init__(self, wgc_team, oppo, location, fixture_type, fixture_start_datetime, fixture_end_datetime, ground):
        self.wgc_team = wgc_team
        self.oppo = oppo
        self.location = location
        self.fixture_type = fixture_type
        self.fixture_start_datetime = fixture_start_datetime
        self.fixture_end_datetime = fixture_end_datetime
        self.ground = ground

    def __eq__(self, other):
        return (self.wgc_team == other.wgc_team
                and self.oppo == other.oppo
                and self.location == other.location
                and self.fixture_type == other.fixture_type
                and self.fixture_start_datetime == other.fixture_start_datetime
                and self.fixture_end_datetime == other.fixture_end_datetime
                and self.ground == other.ground)

    def __str__(self):
        return f"{self.get_matchup()} {self.location} {self.get_localized_fixture_start_datetime_string()} {self.get_localized_fixture_end_time_string()} {self.ground} {self.fixture_type}"

    def __repr__(self):
        return f"wgc_team: {self.wgc_team}, oppo: {self.oppo}, location: {self.location}, type {self.fixture_type} start_datetime: {self.fixture_start_datetime}, time: {self.fixture_end_datetime}, ground: {self.ground}"

    def __lt__(self, other):
        return self.fixture_start_datetime < other.fixture_start_datetime

    def get_matchup(self):
        return self.get_matchup_string(self.wgc_team.value)

    def get_description(self):
        description =  self.get_matchup_string(self.wgc_team.team_fullname)
        description += ' on '
        description += self.fixture_start_datetime.strftime('%a %d %b %Y at %H:%M')
        description += "~"
        description += self.fixture_type.value
        if self.fixture_type.value is FixtureType.LEAGUE.value:
            description += "~"
            description += self.wgc_team.division
        return description

    def get_matchup_string(self, wgc_team):
        if self.wgc_team is CricketTeam.NotWGCCC:
            matchup = self.oppo
        elif self.location == Location.HOME:
            matchup = wgc_team + ' v ' + self.oppo
        else:
            matchup = self.oppo + ' v ' + wgc_team
        return matchup

    def get_localized_fixture_start_datetime_string(self):
        return self.fixture_start_datetime.astimezone(pytz.timezone('Europe/London')).strftime('%d/%m/%Y %H:%M')

    def get_localized_fixture_start_date_string(self):
        return self.fixture_start_datetime.astimezone(pytz.timezone('Europe/London')).strftime('%d/%m/%Y')

    def get_localized_fixture_start_time_string(self):
        return self.fixture_start_datetime.astimezone(pytz.timezone('Europe/London')).strftime('%H:%M')

    def get_localized_fixture_end_time_string(self):
        return self.fixture_end_datetime.astimezone(pytz.timezone('Europe/London')).strftime('%H:%M')

class InvalidFixture:
    def __init__(self, fixture, invalid_type, source):
        self.fixture = fixture
        self.invalid_type = invalid_type
        self.source = source

    def __lt__(self, other):
        return self.fixture.fixture_start_datetime < other.fixture.fixture_start_datetime

    def __str__(self):
        return f"{self.fixture} {self.source}"
