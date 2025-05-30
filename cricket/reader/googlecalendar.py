# imports
from fixture import Fixture
from fixtureprinter import get_division
from cricket_enums import Ground, TeamName
from reader.utils import add_fixture, get_data_path, get_wgc_team, get_wgc_team_from_summary

from icalendar import Calendar
from datetime import datetime, timedelta, timezone
from os import listdir

fixtures = []

def is_valid_fixture(summary):
    return add_fixture(get_wgc_team_from_summary(summary))

def get_teams(summary):
    teams = summary.removeprefix('POSTPONED: ').split(' yards)')[0]
    return teams[:-4].split(' vs ')

def read_ical(filename, ground):

    file = open(filename, 'rb')
    cal = Calendar.from_ical(file.read())

    start_date = datetime(2025,4,1, tzinfo=timezone.utc)

    for event in cal.walk('vevent'):
        summary = str(event['SUMMARY']).replace(',','')
        if is_valid_fixture(summary):
            fixture_date = event.get("DTSTART").dt
            if fixture_date > start_date:
                teams = get_teams(summary)
                division = get_division(get_wgc_team_from_summary(summary))
                fixture = Fixture(teams[0],
                                  teams[1],
                                  division,
                                  fixture_date.strftime('%d/%m/%Y'),
                                  (fixture_date + timedelta(hours=1)).strftime('%H:%M'),
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
