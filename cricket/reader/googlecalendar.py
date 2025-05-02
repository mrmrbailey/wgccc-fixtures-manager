# imports
from fixture import Fixture
from icalendar import Calendar
from cricket_enums import Ground
from datetime import datetime, timedelta, timezone
import os

fixtures = []

def is_junior_fixture(summary):
    pitch_length_text = 'yards)'
    return pitch_length_text in summary

def read_ical(filename, ground):
    print(filename)

    file = open(filename, 'rb')
    cal = Calendar.from_ical(file.read())

    start_date = datetime(2025,4,1, tzinfo=timezone.utc)

    for event in cal.walk('vevent'):
        summary = str(event['SUMMARY']).replace(',','')
        if is_junior_fixture(summary):

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
