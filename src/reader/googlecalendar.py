# imports
from src.fixture import Fixture
from src.cricket_enums import Ground, Location
from src.reader.utils import get_data_path
from src.reader.googlecalendar_utils import clean_summary, get_teams, get_fixture_type_from_description, get_fixture_type_from_summary, clean_fixture_date, is_fixture_this_year
from src.cricket_team import CricketTeam

from icalendar import Calendar
from os import listdir

fixtures = []

def read_ical(filename, ground):

    file = open(filename, 'rb')
    cal = Calendar.from_ical(file.read())

    for event in cal.walk('vevent'):
        summary = event['SUMMARY']
        fixture_start_date = clean_fixture_date(event.get("DTSTART").dt)

        if is_fixture_this_year(fixture_start_date):
            fixture_end_date = clean_fixture_date(event.get("DTEND").dt)
            teams = get_teams(clean_summary(summary))
            fixture_type = get_fixture_type_from_description(event.get("Description"))
            if fixture_type is None:
                fixture_type = get_fixture_type_from_summary(summary)
            if ground == Ground.AWAY:
                wgc_team = CricketTeam.get_value(teams[1])
                oppo = teams[0]
                location = Location.AWAY
            else:
                wgc_team = CricketTeam.get_value(teams[0])
                oppo = teams[1]
                location = Location.HOME

            fixture = Fixture(wgc_team,
                              oppo,
                              location,
                              fixture_type,
                              fixture_start_date,
                              fixture_end_date,
                              ground)
            fixtures.append(fixture)
    file.close()

def parse_google_calendar_data():

    for filename in listdir(get_data_path()):
        if filename.endswith('.ics'):
            if filename.startswith(Ground.DP.value):
                ground = Ground.DP
            elif filename.startswith(Ground.WPF.value):
                ground = Ground.WPF
            else:
                ground = Ground.AWAY
            read_ical(get_data_path() + filename, ground)

    return fixtures
