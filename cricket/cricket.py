from reader.googlecalendar import parse_google_calendar_data
from reader.playcricket import parse_play_cricket_data
from compare import compare_fixtures

def main():
    compare_fixtures(parse_google_calendar_data(), parse_play_cricket_data())

main()
