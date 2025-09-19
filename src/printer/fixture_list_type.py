from enum import Enum

class FixtureListType(Enum):
    CURRENT_WEEK = 'Current Week'
    NEXT_WEEK = 'Next Week'
    FUTURE = 'Future'
    FIXTURE_TYPE = 'Fixture Type'
    GROUND ='Ground'
    HOME_NEXT_WEEK = 'Home Next Week'
    TEAM = 'Team'
    JUNIOR = 'Junior'
    GOOGLE_CALENDAR_IMPORT_CSV = 'Google Calendar Import CSV'
