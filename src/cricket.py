import src.cricket_enums as ce
from src.cricket_team import CricketTeam as ct

from src.printer.fixtures import print_fixtures_for_type
from src.printer.fixture_list_type import FixtureListType
from src.reader.playcricket import parse_play_cricket_data
from src.reader.googlecalendar import parse_google_calendar_data

def main(source_data: ce.SourceData, fixture_list_type: FixtureListType, *args):

    list_of_fixtures = []
    match source_data:
        case ce.SourceData.PLAY_CRICKET:
            list_of_fixtures = parse_play_cricket_data()
        case ce.SourceData.GOOGLE_CALENDAR:
            list_of_fixtures = parse_google_calendar_data()

    print_fixtures_for_type(list_of_fixtures, fixture_list_type, *args)

main(ce.SourceData.PLAY_CRICKET, FixtureListType.TEAM, ct.U15s)
