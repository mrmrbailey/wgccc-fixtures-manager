# imports
from fixture import Fixture
from icalendar import Calendar
from cricket_enums import Ground, TeamName
from reader.utils import add_fixture
from datetime import datetime, timedelta, timezone
import os

fixtures = []

def is_valid_fixture(summary):
    return add_fixture(get_team(summary))

def get_team(summary):
    if TeamName.GIRLS.value in summary:
        return TeamName.GIRLS
    elif TeamName.U9s.value in summary:
        return TeamName.U9s
    elif TeamName.U10s.value in summary:
        return TeamName.U10s
    elif TeamName.U11s.value in summary:
        return TeamName.U11s
    elif TeamName.U12s.value in summary:
        return TeamName.U12s
    elif TeamName.U13s.value in summary:
        return TeamName.U13s
    elif TeamName.U14s.value in summary:
        return TeamName.U14s
    elif TeamName.U15s.value in summary:
        return TeamName.U15s
    elif TeamName.U17s.value in summary:
        return TeamName.U17s
    else:
        return TeamName.UNKNOWN

def read_ical(filename, ground):

    file = open(filename, 'rb')
    cal = Calendar.from_ical(file.read())

    start_date = datetime(2025,4,1, tzinfo=timezone.utc)

    for event in cal.walk('vevent'):
        summary = str(event['SUMMARY']).replace(',','')
        if is_valid_fixture(summary):
            fixture_date = event.get("DTSTART").dt
            if fixture_date > start_date:
                fixture = Fixture(summary,
                                      fixture_date.strftime('%d/%m/%Y'),
                                      (fixture_date + timedelta(hours=1)).strftime('%H:%M'),
                                      ground)
                fixtures.append(fixture)
    file.close()

def parse_google_calendar_data():

    data_path = os.path.dirname(__file__) + '/../../data/'
    for filename in os.listdir(data_path):
        if filename.endswith('.ics'):
            if filename.startswith(Ground.DP.value):
                ground = Ground.DP
            elif filename.startswith(Ground.WPF.value):
                ground = Ground.WPF
            else:
                ground = Ground.AWAY
            read_ical(data_path + filename, ground)

    return fixtures
