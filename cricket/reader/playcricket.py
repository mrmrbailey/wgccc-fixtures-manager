# imports
from reader.csv_utils import get_fixture_start_datetime, get_fixture_end_datetime
from cricket_team import CricketTeam
from fixture_enums import Location, Ground, FixtureType
from reader.utils import get_play_cricket_path
from fixture import Fixture

from os import listdir
from csv import reader

from result import Result


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

    results_headline = record[14]
    home_points = int(record[18]) if record[18] else 0
    away_points = int(record[19]) if record[19] else 0
    result = Result(results_headline, home_points, away_points)

    return Fixture(wgc_team, oppo, location, fixture_type, fixture_start_datetime, fixture_end_time, ground, result)

def parse_play_cricket_data():
    fixtures = []
    for filename in listdir(get_play_cricket_path()):
        if filename.endswith('.csv'):
            with open(get_play_cricket_path() + filename, 'r') as read_obj:
                csv_reader = reader(read_obj)
                for record in list(csv_reader)[1:]:
                    fixtures.append(parse_record(record))
    return fixtures
