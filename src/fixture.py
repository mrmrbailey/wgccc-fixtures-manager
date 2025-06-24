from datetime import datetime, timezone, date, timedelta

class Fixture:
    def __init__(self, home, away, division, fixture_date, fixture_time, ground):
        self.home = home
        self.away = away
        self.division = division
        self.fixture_date = fixture_date
        self.fixture_time = fixture_time
        self.ground = ground

    def __eq__(self, other):
        return (self.home == other.home
                and self.away == other.away
                and self.division == other.division
                and self.fixture_date == other.fixture_date
                and self.fixture_time == other.fixture_time
                and self.ground == other.ground)

    def __str__(self):
        return f"{self.home} vs {self.away} {self.fixture_date} {self.fixture_time} {self.ground}"

    def __repr__(self):
        return f"home: {self.home}, away: {self.away}, division: {self.division}, date: {self.fixture_date}, time: {self.fixture_time}, ground: {self.ground}"

    def __lt__(self, other):
        return self.get_fixture_date() < other.get_fixture_date()

    def get_fixture_date(self):
        date_split_string = self.fixture_date.split("/")
        fixture_date_time = datetime(int(date_split_string[2]),
                                 int(date_split_string[1]),
                                 int(date_split_string[0]),
                                 tzinfo=timezone.utc)
        return fixture_date_time


class InvalidFixture:
    def __init__(self, fixture, invalid_type, source):
        self.fixture = fixture
        self.invalid_type = invalid_type
        self.source = source

    def __lt__(self, other):
        return self.fixture.home < other.fixture.home

    def __str__(self):
        return f"{self.fixture} {self.source}"
