from cricket_enums import SourceData, RunMode
from comparator.compare_fixture_lists import get_different_fixtures, get_spond_different_fixtures

from printer.fixtures import print_fixtures
from printer.fixtures_to_print import FixturesToPrint
from reader.playcricket import parse_play_cricket_data, parse_play_cricket_missing_results
from reader.googlecalendar import parse_google_calendar_data
from reader.spond import parse_spond_data
from reader.wpf import parse_wpf_data

def cricket_str(source_data_str: int, run_mode_str: str, fixture_list_type_str: str, *args):
    cricket(SourceData(source_data_str), RunMode(run_mode_str), FixturesToPrint(fixture_list_type_str), *args)

def cricket(source_data: SourceData, run_mode: RunMode, fixtures_to_print: FixturesToPrint, *args):

    list_of_fixtures = parse_source_data(source_data)

    match run_mode:
        case RunMode.COMPARE:
            other_source = SourceData(*args)
            other_fixtures = parse_source_data(other_source)
            if is_spond(source_data, other_source):
                list_of_fixtures = get_spond_different_fixtures(list_of_fixtures, other_fixtures)
            else:
                list_of_fixtures = get_different_fixtures(list_of_fixtures, other_fixtures)

    print_fixtures(list_of_fixtures, fixtures_to_print, *args)

def parse_source_data(source_data: SourceData):
    parsed_fixtures = []
    match source_data:
        case SourceData.PLAY_CRICKET:
            parsed_fixtures = parse_play_cricket_data()
        case SourceData.GOOGLE_CALENDAR:
            parsed_fixtures = parse_google_calendar_data()
        case SourceData.SPOND:
            parsed_fixtures = parse_spond_data()
        case SourceData.WPF_BOOKINGS:
            parsed_fixtures = parse_wpf_data()
        case SourceData.MISSING_RESULTS:
            parsed_fixtures = parse_play_cricket_missing_results()
    return parsed_fixtures

def is_spond(source_data: SourceData, other_source: SourceData):
    return source_data == SourceData.SPOND or other_source == SourceData.SPOND

cricket(SourceData.PLAY_CRICKET, RunMode.COMPARE, FixturesToPrint.ALL, SourceData.GOOGLE_CALENDAR)
