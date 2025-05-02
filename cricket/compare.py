from fixture import InvalidFixture
from cricket_enums import InvalidType, SourceData

different_fixtures = []

def compare_two_fixture_lists(source_data, source_list, target_list):

    for fixture in source_list:
        try:
            if fixture == target_list[target_list.index(fixture)]:
                pass
        except ValueError:
            invalid_type = InvalidType.NOT_FOUND
            for target_fixture in target_list:
                if fixture.summary == target_fixture.summary:
                    invalid_type = InvalidType.MIS_MATCH
            invalid_fixture = InvalidFixture(fixture, invalid_type, source_data)
            different_fixtures.append(invalid_fixture)

def compare_fixtures(google_calendar_fixtures, play_cricket_fixtures):

    compare_two_fixture_lists(SourceData.GOOGLE_CALENDAR, google_calendar_fixtures, play_cricket_fixtures)
    compare_two_fixture_lists(SourceData.PLAY_CRICKET, play_cricket_fixtures, google_calendar_fixtures)

    print_differences()

def print_differences():
    different_fixtures.sort()

    print(InvalidType.MIS_MATCH)
    for fixture in different_fixtures:
        if fixture.type == InvalidType.MIS_MATCH:
            print(fixture)

    print(InvalidType.NOT_FOUND)
    for fixture in different_fixtures:
        if fixture.type == InvalidType.NOT_FOUND:
            print(fixture)