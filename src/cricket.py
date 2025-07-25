import fixtureprinter as fp
import cricket_enums as ce
from cricket_team import CricketTeam as ct
from reader.playcricket import parse_play_cricket_data
from reader.googlecalendar import parse_google_calendar_data

def main():
    list_of_play_cricket_fixtures = parse_play_cricket_data()
    list_of_google_calendar_fixtures = parse_google_calendar_data()
    fp.print_fixtures_for_ground(list_of_google_calendar_fixtures, ce.Ground.DP)

main()
