# imports
from cricket_enums import Ground, TeamName, Division
from reader.utils import add_fixture, get_data_path, get_wgc_team
from fixture import Fixture
from fixtureprinter import get_division

from os import listdir
from csv import reader

def parse_play_cricket(list_of_fixtures):
    #iterate over the list of fixtures file
    fixtures = []
    for fixture in list_of_fixtures[1:]:

        division_string = fixture[4]
        wgc_team = get_wgc_team(division_string)
        division = get_division(wgc_team)

        home_team = fixture[1].replace(',', '')
        away_team = fixture[2].replace(',', '')

        match_location = fixture[6]
        match match_location:
            case Ground.DP.value:
                home_team = wgc_team.value
                ground = Ground.DP
            case Ground.WPF.value:
                home_team = wgc_team.value
                ground = Ground.WPF
            case _:
                away_team = wgc_team.value
                ground = Ground.AWAY

        match_date = fixture[0]
        start_time = fixture[5]

        if add_fixture(wgc_team):
            fixture = Fixture(home_team, away_team, division, match_date, start_time, ground)
            fixtures.append(fixture)

    return fixtures

def parse_play_cricket_data():
    for filename in listdir(get_data_path()):
        if filename.endswith('.csv'):
            with open(get_data_path() + filename, 'r') as read_obj:
                csv_reader = reader(read_obj)
                list_of_fixtures = list(csv_reader)
                return parse_play_cricket(list_of_fixtures)
    return []
