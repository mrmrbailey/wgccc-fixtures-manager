# imports
from typing import List

from fixture import Fixture
from fixture_enums import Ground, Location, FixtureType
from reader.utils import get_google_calendar_path
from reader.googlecalendar_utils import clean_summary, get_teams, get_fixture_type_from_description, \
    get_fixture_type_from_summary, clean_fixture_date, is_fixture_this_year, is_postponed
from cricket_team import CricketTeam

from icalendar import Calendar, Component
from os import listdir

def parse_record(ground: Ground, event: Component) -> Fixture:
    summary = event['SUMMARY']
    fixture_start_date = clean_fixture_date(event.get("DTSTART").dt)
    fixture_end_date = clean_fixture_date(event.get("DTEND").dt)
    teams = get_teams(clean_summary(summary))

    fixture_type = FixtureType.POSTPONED if is_postponed(summary) else get_fixture_type_from_description(event.get("Description"))
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

    return Fixture(wgc_team,
                      oppo,
                      location,
                      fixture_type,
                      fixture_start_date,
                      fixture_end_date,
                      ground)

def parse_google_calendar_data() -> List[Fixture]:
    fixtures = []
    for filename in listdir(get_google_calendar_path()):
        if filename.endswith('.ics'):
            file = open(get_google_calendar_path() + filename, 'rb')
            cal = Calendar.from_ical(file.read())

            for event in cal.walk('vevent'):
                if is_fixture_this_year(clean_fixture_date(event.get("DTSTART").dt)):
                    fixtures.append(parse_record(get_ground(filename), event))
            file.close()
    return fixtures

def get_ground(filename:str) -> Ground:
    if filename.startswith(Ground.DP.value):
        return Ground.DP
    elif filename.startswith(Ground.WPF.value):
        return Ground.WPF
    else:
        return Ground.AWAY