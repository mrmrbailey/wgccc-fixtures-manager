from fixtureprinter import print_fixtures, print_this_weeks_fixtures, print_next_weeks_fixtures, print_fixtures_for_ground, print_next_weeks_home_fixtures, print_future_fixtures
from reader.playcricket import parse_play_cricket_data
from reader.googlecalendar import parse_google_calendar_data
from cricket_enums import TeamName, Ground


def main():
    list_of_play_cricket_fixtures = parse_play_cricket_data()
    list_of_google_calendar_fixtures = parse_google_calendar_data()
    print_future_fixtures(list_of_google_calendar_fixtures)

main()
