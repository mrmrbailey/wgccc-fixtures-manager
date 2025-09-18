import src.fixtureprinter as fp
import src.cricket_enums as ce
from src.cricket_team import CricketTeam as ct
from src.reader.playcricket import parse_play_cricket_data
from src.reader.googlecalendar import parse_google_calendar_data

def main():
    list_of_play_cricket_fixtures = parse_play_cricket_data()
    list_of_google_calendar_fixtures = parse_google_calendar_data()
    fp.print_google_calendar_csv(list_of_google_calendar_fixtures, ce.Ground.DP)

main()
