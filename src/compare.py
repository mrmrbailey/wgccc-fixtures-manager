from src.fixture import InvalidFixture
from src.cricket_enums import InvalidType, SourceData, FixtureType
from src.reader.googlecalendar import parse_google_calendar_data
from src.reader.playcricket import parse_play_cricket_data

different_fixtures = []

def compare_two_fixture_lists(source_data, source_list, target_list):

    source_list.sort()
    target_list.sort()

    for fixture in source_list:
        try:
            if fixture == target_list[target_list.index(fixture)]:
                pass
        except ValueError:
            invalid_type = InvalidType.NOT_FOUND
            for target_fixture in target_list:
                if (fixture.wgc_team == target_fixture.wgc_team
                        and fixture.oppo == target_fixture.oppo
                        and fixture.location == target_fixture.location
                        and fixture.fixture_type == target_fixture.fixture_type):
                    invalid_type = InvalidType.MIS_MATCH
            invalid_fixture = InvalidFixture(fixture, invalid_type, source_data)
            different_fixtures.append(invalid_fixture)

def compare_fixtures(google_calendar_fixtures, play_cricket_fixtures):

    junior_fixtures = []
    for fixture in google_calendar_fixtures:
        if fixture.fixture_type is not FixtureType.SENIOR:
            junior_fixtures.append(fixture)

    compare_two_fixture_lists(SourceData.GOOGLE_CALENDAR, junior_fixtures, play_cricket_fixtures)
    compare_two_fixture_lists(SourceData.PLAY_CRICKET, play_cricket_fixtures, junior_fixtures)

    print_differences()

def print_differences():
    different_fixtures.sort()

    print(InvalidType.MIS_MATCH)
    for fixture in different_fixtures:
        if fixture.invalid_type == InvalidType.MIS_MATCH:
            print(fixture)

    print(InvalidType.NOT_FOUND)
    friendlies = []
    for fixture in different_fixtures:
        if fixture.invalid_type == InvalidType.NOT_FOUND:
            if fixture.fixture.fixture_type is FixtureType.FRIENDLY:
                friendlies.append(fixture)
            else:
                print(fixture)

    print(FixtureType.FRIENDLY)
    print(len(friendlies))
#    for friendly in friendlies:
#        print(friendly)

def main():
    compare_fixtures(parse_google_calendar_data(), parse_play_cricket_data())

main()
