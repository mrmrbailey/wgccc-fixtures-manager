# imports
from fixture import Fixture
from icalendar import Calendar
from cricket_enums import Ground
from datetime import datetime, timedelta, timezone
import os

fixtures = []

dp_filename = 'Digswell Park - Ground Schedule_ff46e58ee40763c0cb0978a1fd1b033ba2d6724f8e886c483efbdfca84021db8@group.calendar.google.com.ics'
wpf_filename = 'Welwyn Playing Fields - Schedule_ec3965cb899d3184e14dfdfcbcccfdc541ef98cde881a0a0b68320e5af0be129@group.calendar.google.com.ics'
away_filename = 'WGCCC - Away Fixtures Schedule_92f753425e2472fcade1cebb4a647ec9eb074056dea689722914e01b58f7f5c0@group.calendar.google.com.ics'

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

    read_ical(data_path + dp_filename, Ground.DP)
    read_ical(data_path + wpf_filename, Ground.WPF)
    read_ical(data_path + away_filename, Ground.AWAY)
    return fixtures