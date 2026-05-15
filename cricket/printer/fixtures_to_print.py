from enum import Enum

class FixturesToPrint(Enum):
    ALL = 'All'
    CURRENT_WEEK = 'Current Week'
    NEXT_WEEK = 'Next Week'
    FUTURE = 'Future'
    FIXTURE_TYPE = 'Fixture Type'
    GROUND ='Ground'
    HOME_NEXT_WEEK = 'Home Next Week'
    HOME_BOOKINGS = 'Home Bookings'
    TEAM = 'Team'
    JUNIOR = 'Junior'
    SAME_DAY = 'Same Day'
    CLASH = 'Clash'
    GOOGLE_CALENDAR_IMPORT_CSV = 'Google Calendar Import CSV'