from fixture import InvalidFixture
from cricket_enums import InvalidType, SourceData
from reader.googlecalendar import parse_google_calendar_data
from reader.playcricket import parse_play_cricket_data

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
                if fixture.home == target_fixture.home and fixture.away == target_fixture.away:
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
        if fixture.invalid_type == InvalidType.MIS_MATCH:
            print(fixture)

    print(InvalidType.NOT_FOUND)
    for fixture in different_fixtures:
        if fixture.invalid_type == InvalidType.NOT_FOUND:
            print(fixture)

def main():
    compare_fixtures(parse_google_calendar_data(), parse_play_cricket_data())

main()
