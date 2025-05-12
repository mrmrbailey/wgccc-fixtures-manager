# imports
from enum import Enum
import csv
from cricket_enums import Ground, TeamName
from reader.utils import add_fixture, get_data_path
from fixture import Fixture
from os import listdir

class DivisionDetails(Enum):
    GIRLS = 'HJCL U9 Girls Group 2'
    U9s = 'HJCL U9 Group 6'
    U10s = 'HJCL U10B Group 5'
    U11s = 'HJCL U11A Group 4'
    U12s = 'HJCL U12A Group 5'
    U13s = 'HJCL U13A Group 4'
    U14s = 'HJCL U14B Group 4'
    U15s = 'HJCL U15A Group 3'
    U17s = 'HJCL U17 Group 3'

class PitchLength(Enum):
    Y15 = '(15 yards)'
    Y17 = '(17 yards)'
    Y19 = '(19 yards)'
    Y22 = '(22 yards)'

def parse_play_cricket(list_of_fixtures):
    #iterate over the list of fixtures file
    fixtures = []
    for fixture in list_of_fixtures[1:]:
        division = fixture[4]
        match division:
            case DivisionDetails.GIRLS.value:
                wgc_team = TeamName.GIRLS
                pitch_length = PitchLength.Y15
            case DivisionDetails.U9s.value:
                wgc_team = TeamName.U9s
                pitch_length = PitchLength.Y15
            case DivisionDetails.U10s.value:
                wgc_team = TeamName.U10s
                pitch_length = PitchLength.Y17
            case DivisionDetails.U11s.value:
                wgc_team = TeamName.U11s
                pitch_length = PitchLength.Y17
            case DivisionDetails.U12s.value:
                wgc_team = TeamName.U12s
                pitch_length = PitchLength.Y19
            case DivisionDetails.U13s.value:
                wgc_team = TeamName.U13s
                pitch_length = PitchLength.Y19
            case DivisionDetails.U14s.value:
                wgc_team = TeamName.U14s
                pitch_length = PitchLength.Y22
            case DivisionDetails.U15s.value:
                wgc_team = TeamName.U15s
                pitch_length = PitchLength.Y22
            case DivisionDetails.U17s.value:
                wgc_team = TeamName.U17s
                pitch_length = PitchLength.Y22
            case _:
                wgc_team = TeamName.UNKNOWN
                pitch_length = PitchLength.Y22

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

        fixture_summary =  home_team + ' vs ' + away_team + ' ' + pitch_length.value

        match_date = fixture[0]
        start_time = fixture[5]

        if add_fixture(wgc_team):
            fixture = Fixture(fixture_summary, match_date, start_time, ground)
            fixtures.append(fixture)
    return fixtures

def parse_play_cricket_data():

    for filename in listdir(get_data_path()):
        if filename.endswith('.csv'):
            with open(get_data_path() + filename, 'r') as read_obj:
                csv_reader = csv.reader(read_obj)
                list_of_fixtures = list(csv_reader)
                return parse_play_cricket(list_of_fixtures)

    return []
