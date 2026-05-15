from printer.fixtures_to_print import FixturesToPrint
from printer.fixture_utils import get_this_weeks_fixtures, get_next_weeks_fixtures, get_future_fixtures, \
    get_fixtures_for_type, get_fixtures_for_ground, get_fixtures_for_home,get_fixtures_for_home_next_week, get_fixtures_for_team, \
    get_junior_fixtures, get_fixtures_for_same_day, get_fixtures_for_clash, get_fixtures_for_google_calendar_csv_import
from printer.googlecalendar_utils import print_fixtures_for_google_calendar_csv_import

def print_fixtures(list_of_fixtures, fixtures_to_print: FixturesToPrint, *args):
    fixtures_to_be_printed = []
    match fixtures_to_print:
        case FixturesToPrint.CURRENT_WEEK:
            fixtures_to_be_printed = get_this_weeks_fixtures(list_of_fixtures)
        case FixturesToPrint.NEXT_WEEK:
            fixtures_to_be_printed = get_next_weeks_fixtures(list_of_fixtures)
        case FixturesToPrint.FUTURE:
            fixtures_to_be_printed = get_future_fixtures(list_of_fixtures)
        case FixturesToPrint.FIXTURE_TYPE:
            fixtures_to_be_printed = get_fixtures_for_type(list_of_fixtures, *args)
        case FixturesToPrint.GROUND:
            fixtures_to_be_printed = get_fixtures_for_ground(list_of_fixtures, *args)
        case FixturesToPrint.HOME_NEXT_WEEK:
            fixtures_to_be_printed = get_fixtures_for_home_next_week(list_of_fixtures)
        case FixturesToPrint.HOME_BOOKINGS:
            fixtures_to_be_printed = get_fixtures_for_home(list_of_fixtures)
        case FixturesToPrint.TEAM:
            fixtures_to_be_printed = get_fixtures_for_team(list_of_fixtures, *args)
        case FixturesToPrint.JUNIOR:
            fixtures_to_be_printed = get_junior_fixtures(list_of_fixtures)
        case FixturesToPrint.SAME_DAY:
            fixtures_to_be_printed = get_fixtures_for_same_day(list_of_fixtures)
        case FixturesToPrint.CLASH:
            fixtures_to_be_printed = get_fixtures_for_clash(list_of_fixtures)
        case FixturesToPrint.GOOGLE_CALENDAR_IMPORT_CSV:
            fixtures_to_be_printed = get_fixtures_for_google_calendar_csv_import(list_of_fixtures, *args)
        case _: # FixtureListType.ALL
            fixtures_to_be_printed = list_of_fixtures

    print_fixture_header(fixtures_to_print)
    match fixtures_to_print:
        case FixturesToPrint.SAME_DAY:
            print_fixtures_on_same_day(fixtures_to_be_printed)
        case FixturesToPrint.GOOGLE_CALENDAR_IMPORT_CSV:
            print_fixtures_for_google_calendar_csv_import(fixtures_to_be_printed)
        case _:
            print_list_of_fixtures(fixtures_to_be_printed)

def print_fixture_header(fixture_list_type: FixturesToPrint):
    print('======== ' + fixture_list_type.value + ' Fixtures =========')

def print_list_of_fixtures(list_of_fixtures):
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
