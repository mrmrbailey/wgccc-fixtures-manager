from datetime import datetime, timezone

class Fixture:
    def __init__(self, wgc_team, oppo, location, fixture_type, fixture_date, fixture_time, ground):
        self.wgc_team = wgc_team
        self.oppo = oppo
        self.location = location
        self.fixture_type = fixture_type
        self.fixture_date = fixture_date
        self.fixture_time = fixture_time
        self.ground = ground

    def __eq__(self, other):
        a = self.wgc_team == other.wgc_team
        b = self.oppo == other.oppo
        c = self.location == other.location
        d = self.fixture_date == other.fixture_date
        e = self.fixture_time == other.fixture_time
        f = self.ground == other.ground
        return (self.wgc_team == other.wgc_team
                and self.oppo == other.oppo
                and self.location == other.location
                and self.fixture_date == other.fixture_date
                and self.fixture_time == other.fixture_time
                and self.ground == other.ground)

    def __str__(self):
        return f"{self.wgc_team} and {self.oppo} {self.location} {self.fixture_date} {self.fixture_time} {self.ground} {self.fixture_type}"

    def __repr__(self):
        return f"wgc_team: {self.wgc_team}, oppo: {self.oppo}, location: {self.location}, type {self.fixture_type} date: {self.fixture_date}, time: {self.fixture_time}, ground: {self.ground}"

    def __lt__(self, other):
        return self.get_fixture_date() < other.get_fixture_date()

    def get_fixture_date(self):
        date_split_string = self.fixture_date.split("/")
        time_split_string = self.fixture_time.split(":")
        fixture_date_time = datetime(int(date_split_string[2]),
                                 int(date_split_string[1]),
                                 int(date_split_string[0]),
                                 int(time_split_string[0]),
                                 int(time_split_string[1]),
                                 tzinfo=timezone.utc)
        return fixture_date_time


class InvalidFixture:
    def __init__(self, fixture, invalid_type, source):
        self.fixture = fixture
        self.invalid_type = invalid_type
        self.source = source

    def __lt__(self, other):
        return self.fixture.get_fixture_date() < other.fixture.get_fixture_date()

    def __str__(self):
        return f"{self.fixture} {self.source}"
