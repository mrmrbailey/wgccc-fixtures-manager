import cricket_enums as ce
from comparator.compare_fixture_lists import get_different_fixtures, get_spond_different_fixtures
from cricket_team import CricketTeam

from printer.fixtures import print_fixtures_for_type
from printer.fixture_list_type import FixtureListType
from reader.playcricket import parse_play_cricket_data, get_results_missing_in_play_cricket
from reader.googlecalendar import parse_google_calendar_data
from reader.spond import parse_spond_data

def cricket_str(source_data_str: int, fixture_list_type_str: str, *args):
    cricket(ce.SourceData(source_data_str), FixtureListType(fixture_list_type_str), *args)

def cricket(source_data: ce.SourceData, fixture_list_type: FixtureListType, *args):
    list_of_fixtures = []
    match source_data:
        case ce.SourceData.PLAY_CRICKET:
            list_of_fixtures = parse_play_cricket_data()
        case ce.SourceData.GOOGLE_CALENDAR:
            list_of_fixtures = parse_google_calendar_data()

    match fixture_list_type:
        case FixtureListType.COMPARE:
            other_fixtures = parse_play_cricket_data() if source_data == ce.SourceData.GOOGLE_CALENDAR else parse_google_calendar_data()
            list_of_fixtures = get_different_fixtures(list_of_fixtures, other_fixtures)
        case FixtureListType.COMPARE_SPOND:
            spond_fixtures = parse_spond_data()
            list_of_fixtures = get_spond_different_fixtures(list_of_fixtures, spond_fixtures)
        case FixtureListType.MISSING_RESULT:
            list_of_fixtures = get_results_missing_in_play_cricket()

    print_fixtures_for_type(list_of_fixtures, fixture_list_type, *args)

cricket(ce.SourceData.GOOGLE_CALENDAR, FixtureListType.ALL)
