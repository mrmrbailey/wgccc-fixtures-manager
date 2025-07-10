# imports
from fixture import Fixture
from fixtureprinter import get_division
from cricket_enums import Ground, TeamName, FixtureType, Division
from reader.utils import add_fixture, get_data_path, get_wgc_team, get_wgc_team_from_summary, get_fixture_type

from icalendar import Calendar
from datetime import datetime, timedelta, timezone
from os import listdir

fixtures = []

def is_valid_fixture(summary):
    return add_fixture(get_wgc_team_from_summary(summary))

def remove_prefix(summary):
    return summary.removeprefix('POSTPONED: ').removeprefix('RAINEDOFF: ')

def get_teams(summary):
    teams = remove_prefix(summary).split(' yards)')[0]
    return teams[:-4].split(' vs ')

def remove_preformatted_tag(html_snippet):
    return html_snippet.removeprefix('<pre>').removesuffix('</pre>')

def get_division_and_type(description):
    if description is None:
        description = ''
    description.replace('<pre>','')
    return remove_preformatted_tag(description).split(':')

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
                division_and_type = get_division_and_type(event.get("Description"))
                if len(division_and_type) != 2:
                    division = get_division(get_wgc_team_from_summary(summary))
                    fixture_type = FixtureType.LEAGUE
                else:
                    fixture_type = get_fixture_type(division_and_type[0])
                    match fixture_type:
                        case FixtureType.LEAGUE:
                            division = get_division(get_wgc_team_from_summary(summary))
                        case FixtureType.CUP:
                            division = Division.CUP
                        case FixtureType.FRIENDLY:
                            division = Division.FRIENDLY
                        case _:
                            division = Division.UNKNOWN

                fixture = Fixture(teams[0],
                                  teams[1],
                                  division,
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
