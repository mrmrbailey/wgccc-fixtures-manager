from printer.fixture_list_type import FixtureListType
from printer.fixture_utils import get_this_weeks_fixtures, get_next_weeks_fixtures, get_future_fixtures, \
    get_fixtures_for_type, get_fixtures_for_ground, get_fixtures_for_home,get_fixtures_for_home_next_week, get_fixtures_for_team, \
    get_junior_fixtures, get_fixtures_for_same_day, get_fixtures_for_clash, get_fixtures_for_google_calendar_csv_import
from printer.googlecalendar_utils import print_fixtures_for_google_calendar_csv_import

def print_fixtures_for_type(list_of_fixtures, fixture_list_type: FixtureListType, *args):
    fixtures_to_be_printed = []
    match fixture_list_type:
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
        case FixtureListType.HOME_BOOKINGS:
            fixtures_to_be_printed = get_fixtures_for_home(list_of_fixtures)
        case FixtureListType.TEAM:
            fixtures_to_be_printed = get_fixtures_for_team(list_of_fixtures, *args)
        case FixtureListType.JUNIOR:
            fixtures_to_be_printed = get_junior_fixtures(list_of_fixtures)
        case FixtureListType.SAME_DAY:
            fixtures_to_be_printed = get_fixtures_for_same_day(list_of_fixtures)
        case FixtureListType.CLASH:
            fixtures_to_be_printed = get_fixtures_for_clash(list_of_fixtures)
        case FixtureListType.GOOGLE_CALENDAR_IMPORT_CSV:
            fixtures_to_be_printed = get_fixtures_for_google_calendar_csv_import(list_of_fixtures, *args)
        case _: # FixtureListType.ALL | FixtureListType.COMPARE | FixtureListType.COMPARE_SPOND | FixtureListType.MISSING_RESULT:
            fixtures_to_be_printed = list_of_fixtures

    print_fixture_list_type_header(fixture_list_type)
    match fixture_list_type:
        case FixtureListType.SAME_DAY:
            print_fixtures_on_same_day(fixtures_to_be_printed)
        case FixtureListType.GOOGLE_CALENDAR_IMPORT_CSV:
            print_fixtures_for_google_calendar_csv_import(fixtures_to_be_printed)
        case _:
            print_fixtures(fixtures_to_be_printed)

def print_fixture_list_type_header(fixture_list_type: FixtureListType):
    print('======== ' + fixture_list_type.value + ' Fixtures =========')

def print_fixtures(list_of_fixtures):
    list_of_fixtures.sort()
    for fixture in list_of_fixtures:
        print_fixture(fixture)

def print_fixture(fixture):
    print(fixture)

def print_fixtures_on_same_day(list_of_fixtures):

    for idx in range(1, len(list_of_fixtures)):
        fixture = list_of_fixtures[idx]
        last_fixture = list_of_fixtures[idx-1]
        if idx == 1:
            print(f"{last_fixture.fixture_start_datetime.strftime('%Y-%m-%d')}")
            print(f"{last_fixture.wgc_team} {last_fixture.ground}- {last_fixture}")

        if fixture.fixture_start_datetime != last_fixture.fixture_start_datetime:
            print(f"{fixture.fixture_start_datetime.strftime('%Y-%m-%d')}")
        print(f"{fixture.wgc_team} {fixture.ground}- {fixture}")
