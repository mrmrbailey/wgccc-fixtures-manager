# imports
from reader.spond_utils import get_teams
from reader.csv_utils import get_fixture_start_datetime, get_fixture_end_datetime
from cricket_team import CricketTeam
from cricket_enums import Ground, FixtureType, Location
from reader.utils import  get_spond_path
from fixture import Fixture

from os import listdir
from csv import reader

default_start_time = '18:00'

def parse_record(record):

    matchup = record[0]
    wgc_team = CricketTeam.get_from_host(record[3])
    teams = get_teams(matchup)

    ground = Ground.get_value(record[5])
    if ground == Ground.AWAY:
        location = Location.AWAY
        oppo = teams[0]
    else:
        location = Location.HOME
        oppo = teams[1]

    fixture_type = FixtureType.LEAGUE

    match_date = record[1]
    fixture_start_datetime = get_fixture_start_datetime(match_date, default_start_time)
    fixture_end_time = get_fixture_end_datetime(fixture_start_datetime)

    return Fixture(wgc_team, oppo, location, fixture_type, fixture_start_datetime, fixture_end_time, ground)

def parse_spond_data():
    fixtures = []
    for filename in listdir(get_spond_path()):
        if filename.endswith('.csv'):
            with open(get_spond_path() + filename, 'r') as read_obj:
                csv_reader = reader(read_obj)
                for record in list(csv_reader)[1:]:
                    fixtures.append(parse_record(record))
    return fixtures
