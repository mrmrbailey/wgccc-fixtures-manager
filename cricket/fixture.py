from datetime import datetime, timezone

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
        return f"{get_summary(self)} {self.fixture_date} {self.fixture_time} {self.ground}"

    def __lt__(self, other):
        self_date_split_string = self.fixture_date.split("/")
        self_fixture_date_time = datetime(int(self_date_split_string[2]),
                                 int(self_date_split_string[1]),
                                 int(self_date_split_string[0]),
                                 tzinfo=timezone.utc)

        other_date_split_string = other.fixture_date.split("/")
        other_fixture_date_time = datetime(int(other_date_split_string[2]),
                                            int(other_date_split_string[1]),
                                            int(other_date_split_string[0]),
                                            tzinfo=timezone.utc)

        return self_fixture_date_time < other_fixture_date_time

class InvalidFixture:
    def __init__(self, fixture, invalid_type, source):
        self.fixture = fixture
        self.invalid_type = invalid_type
        self.source = source

    def __lt__(self, other):
        return self.fixture.home < other.fixture.home

    def __str__(self):
        return f"{self.fixture} {self.source}"

def get_summary(fixture):
    summary = fixture.home + ' vs ' + fixture.away
    return summary

def print_fixtures_list(list_of_fixtures):
    list_of_fixtures.sort()
    for fixture in list_of_fixtures:
        print(fixture)
