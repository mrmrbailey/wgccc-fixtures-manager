from src.printer.fixture_list_type import FixtureListType
from src.printer.fixture_utils import get_this_weeks_fixtures, get_next_weeks_fixtures, get_future_fixtures, \
    get_fixtures_for_type, get_fixtures_for_ground, get_fixtures_for_home_next_week, get_fixtures_for_team, \
    get_junior_fixtures, get_fixtures_for_google_calendar_csv_import

def print_fixtures_for_type(list_of_fixtures, fixture_list_type: FixtureListType, *args):
    fixtures_to_be_printed = []
    match fixture_list_type:
        case FixtureListType.ALL | FixtureListType.COMPARE:
            fixtures_to_be_printed = list_of_fixtures
        case FixtureListType.CURRENT_WEEK:
            fixtures_to_be_printed = get_this_weeks_fixtures(list_of_fixtures)
        case FixtureListType.NEXT_WEEK:
            fixtures_to_be_printed = get_next_weeks_fixtures(list_of_fixtures)
        case FixtureListType.FUTURE:
            fixtures_to_be_printed = get_future_fixtures(list_of_fixtures)
        case FixtureListType.FIXTURE_TYPE:
            fixtures_to_be_printed = get_fixtures_for_type(list_of_fixtures, *args)
        case FixtureListType.GROUND:
            fixtures_to_be_printed = get_fixtures_for_ground(list_of_fixtures, *args)
        case FixtureListType.HOME_NEXT_WEEK:
            fixtures_to_be_printed = get_fixtures_for_home_next_week(list_of_fixtures)
        case FixtureListType.TEAM:
            fixtures_to_be_printed = get_fixtures_for_team(list_of_fixtures, *args)
        case FixtureListType.JUNIOR:
            fixtures_to_be_printed = get_junior_fixtures(list_of_fixtures)
        case FixtureListType.GOOGLE_CALENDAR_IMPORT_CSV:
            fixtures_to_be_printed = get_fixtures_for_google_calendar_csv_import(list_of_fixtures, *args)

    print_fixture_list_type_header(fixture_list_type)
    print_fixtures(fixtures_to_be_printed)

def print_fixture_list_type_header(fixture_list_type: FixtureListType):
    print('======== ' + fixture_list_type.value + ' Fixtures =========')

def print_fixtures(list_of_fixtures):
    list_of_fixtures.sort()
    for fixture in list_of_fixtures:
        print_fixture(fixture)

def print_fixture(fixture):
    print(fixture)
