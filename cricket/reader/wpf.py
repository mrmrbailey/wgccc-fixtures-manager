# imports
from fixture_enums import Location, Ground, FixtureType
from reader.csv_utils import get_fixture_start_datetime, get_fixture_end_datetime
from cricket_team import CricketTeam
from reader.utils import  get_wpf_path
from fixture import Fixture
from result import Result

from os import listdir
from csv import reader

default_start_time = '18:00'

def parse_record(record):

    wgc_team = CricketTeam.get_value(record[1])
    oppo = record[2]

    location = Location.HOME
    ground = Ground.WPF
    fixture_type = FixtureType.LEAGUE

    match_date = record[0]
    fixture_start_datetime = get_fixture_start_datetime(match_date, default_start_time)
    fixture_end_time = get_fixture_end_datetime(fixture_start_datetime)

    return Fixture(wgc_team, oppo, location, fixture_type, fixture_start_datetime, fixture_end_time, ground, Result())

def parse_wpf_data():
    fixtures = []
    for filename in listdir(get_wpf_path()):
        if filename.endswith('.csv'):
            with open(get_wpf_path() + filename, 'r') as read_obj:
                csv_reader = reader(read_obj)
                for record in list(csv_reader)[1:]:
                    fixtures.append(parse_record(record))
    return fixtures
