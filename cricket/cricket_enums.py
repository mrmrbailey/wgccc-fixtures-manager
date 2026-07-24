from enum import Enum

class SourceData(Enum):
    GOOGLE_CALENDAR = 0
    PLAY_CRICKET = 1
    SPOND = 2
    WPF_BOOKINGS = 3

class RunMode(Enum):
    PRINT_FIXTURES = 'print_fixtures'
    COMPARE = 'compare'