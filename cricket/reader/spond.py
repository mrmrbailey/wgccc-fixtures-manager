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
welwyn_home_string = 'Welwyn Garden City CC (H)'
welwyn_away_string = 'Welwyn Garden City CC (A)'

def parse_spond(list_of_fixtures):
    #iterate over the list of fixtures file
    fixtures = []
    for fixture in list_of_fixtures[1:]:

        matchup = fixture[0]
        wgc_team = CricketTeam.get_from_host(fixture[3])
        teams = get_teams(matchup)
        if welwyn_home_string in matchup:
            oppo = teams[1]
        else:
            oppo = teams[0]

        ground = Ground.get_value(fixture[5])
        location = Location.AWAY if ground == Ground.AWAY else Location.HOME
        fixture_type = FixtureType.LEAGUE

        match_date = fixture[1]
        fixture_start_datetime = get_fixture_start_datetime(match_date, default_start_time)
        fixture_end_time = get_fixture_end_datetime(fixture_start_datetime)

        fixtures.append(Fixture(wgc_team, oppo, location, fixture_type, fixture_start_datetime, fixture_end_time, ground))
    return fixtures

def parse_spond_data():
    for filename in listdir(get_spond_path()):
        if filename.endswith('.csv'):
            with open(get_spond_path() + filename, 'r') as read_obj:
                csv_reader = reader(read_obj)
                list_of_fixtures = list(csv_reader)
                return parse_spond(list_of_fixtures)
    return []
