# imports
from fixture import Fixture
from cricket_enums import Ground, FixtureType, Location
from reader.utils import add_fixture, get_data_path
from src.cricket_team import CricketTeam

from icalendar import Calendar
from datetime import datetime, timedelta, timezone
from os import listdir

fixtures = []

def is_valid_fixture(summary):
    if len(get_teams(summary)) == 2:
        return ' yards)' in summary
    return False

def remove_prefix(summary):
    if len(summary.split(': ')) > 1:
        return summary.split(': ')[1]
    else:
        return summary

def get_teams(summary):
    teams = remove_prefix(summary).split(' yards)')[0]
    return teams[:-4].split(' vs ')

def remove_preformatted_tag(html_snippet):
    return html_snippet.removeprefix('<br>').removeprefix('<pre>').removesuffix('</pre>')

def get_fixture_type_from_description(description):
    if description is None:
        return FixtureType.LEAGUE
    league_and_division = remove_preformatted_tag(description).split(":")
    if len(league_and_division) != 2:
        return FixtureType.LEAGUE
    else:
        return FixtureType[league_and_division[0].upper()]

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
                fixture_type = get_fixture_type_from_description(event.get("Description"))

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
