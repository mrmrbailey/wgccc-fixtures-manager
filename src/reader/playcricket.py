# imports
from src.reader.playcricket_utils import get_wgc_team_from_division
from src.cricket_team import CricketTeam
from src.cricket_enums import Ground, FixtureType, Location
from src.reader.utils import add_fixture, get_data_path
from src.fixture import Fixture

from os import listdir
from csv import reader

def parse_play_cricket(list_of_fixtures):
    #iterate over the list of fixtures file
    fixtures = []
    for fixture in list_of_fixtures[1:]:

        home_team = fixture[1].replace(',', '')
        away_team = fixture[2].replace(',', '')

        match_location = fixture[6]
        match match_location:
            case Ground.DP.value:
                oppo = away_team
                location = Location.HOME
                ground = Ground.DP
            case Ground.WPF.value:
                oppo = away_team
                location = Location.HOME
                ground = Ground.WPF
            case _:
                oppo = home_team
                location = Location.AWAY
                ground = Ground.AWAY

        fixture_type = FixtureType.get_value(fixture[3])
        match fixture_type:
            case FixtureType.LEAGUE:
                division_string = fixture[4]
                wgc_team = get_wgc_team_from_division(division_string)
            case FixtureType.CUP | FixtureType.FRIENDLY:
                if ground == Ground.AWAY:
                    wgc_team_full_name = away_team
                else:
                    wgc_team_full_name = home_team
                wgc_team = CricketTeam.get_from_fullname(wgc_team_full_name)
            case _:
                wgc_team = CricketTeam.UNKNOWN

        match_date = fixture[0]
        start_time = fixture[5]

        if add_fixture(wgc_team):
            fixtures.append(Fixture(wgc_team, oppo, location, fixture_type, match_date, start_time, ground))
    return fixtures

def parse_play_cricket_data():
    for filename in listdir(get_data_path()):
        if filename.endswith('.csv'):
            with open(get_data_path() + filename, 'r') as read_obj:
                csv_reader = reader(read_obj)
                list_of_fixtures = list(csv_reader)
                return parse_play_cricket(list_of_fixtures)
    return []
