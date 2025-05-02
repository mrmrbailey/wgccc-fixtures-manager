from reader.googlecalendar import parse_google_calendar_data
from reader.playcricket import parse_play_cricket_data
from compare import compare_fixtures
from cricket_enums import PlayCricketType

def main(play_cricket_type):
    compare_fixtures(parse_google_calendar_data(), parse_play_cricket_data(play_cricket_type))

main(PlayCricketType.RESULTS)