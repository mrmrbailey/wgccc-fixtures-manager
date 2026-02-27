import cricket_enums as ce
from comparator.compare_fixture_lists import get_different_fixtures

from printer.fixtures import print_fixtures_for_type
from printer.fixture_list_type import FixtureListType
from reader.playcricket import parse_play_cricket_data
from reader.googlecalendar import parse_google_calendar_data

from cricket_team import CricketTeam

import sys

def main(source_data_str, fixture_list_type_str, *args):

    for p in sys.path:
        print(p)


    source_data = ce.SourceData(source_data_str)
    fixture_list_type = FixtureListType(fixture_list_type_str)

    list_of_fixtures = []
    match source_data:
        case ce.SourceData.PLAY_CRICKET:
            list_of_fixtures = parse_play_cricket_data()
        case ce.SourceData.GOOGLE_CALENDAR:
            list_of_fixtures = parse_google_calendar_data()

    if fixture_list_type == FixtureListType.COMPARE:
        other_fixtures = parse_play_cricket_data() if source_data == ce.SourceData.GOOGLE_CALENDAR else parse_google_calendar_data()
        list_of_fixtures = get_different_fixtures(list_of_fixtures, other_fixtures)

    print_fixtures_for_type(list_of_fixtures, fixture_list_type, *args)

main(ce.SourceData.PLAY_CRICKET, FixtureListType.TEAM, CricketTeam.U9s)

