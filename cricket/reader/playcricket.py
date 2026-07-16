# imports
from reader.csv_utils import get_fixture_start_datetime, get_fixture_end_datetime
from cricket_team import CricketTeam
from fixture_enums import Location, Ground, FixtureType
from reader.playcricket_utils import is_fixture_missing_result
from reader.utils import get_play_cricket_path
from fixture import Fixture

from os import listdir
from csv import reader

def parse_record(record):

    home_team = record[1].replace(',', '')
    away_team = record[2].replace(',', '')

    match_location = record[6]
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

    fixture_type = FixtureType.get_value(record[3])
    match fixture_type:
        case FixtureType.LEAGUE:
            division_string = record[4]
            wgc_team = CricketTeam.get_from_division(division_string)
        case FixtureType.CUP | FixtureType.FRIENDLY:
            if ground == Ground.AWAY:
                wgc_team_full_name = away_team
            else:
                wgc_team_full_name = home_team
            wgc_team = CricketTeam.get_from_fullname(wgc_team_full_name)
        case _:
            wgc_team = CricketTeam.UNKNOWN

    match_date = record[0]
    start_time = record[5]
    fixture_start_datetime = get_fixture_start_datetime(match_date, start_time)
    fixture_end_time = get_fixture_end_datetime(fixture_start_datetime)
    return Fixture(wgc_team, oppo, location, fixture_type, fixture_start_datetime, fixture_end_time, ground)

def parse_play_cricket_data():
    return parse_all_play_cricket_data(False)


def parse_play_cricket_missing_results():
    return parse_all_play_cricket_data(True)


def parse_all_play_cricket_data(check_result: bool):
    fixtures = []
    for filename in listdir(get_play_cricket_path()):
        if filename.endswith('.csv'):
            with open(get_play_cricket_path() + filename, 'r') as read_obj:
                csv_reader = reader(read_obj)
                for record in list(csv_reader)[1:]:
                    fixture = parse_record(record)
                    if not check_result or is_fixture_missing_result(fixture, record[14]):
                        fixtures.append(fixture)
    return fixtures
