from enum import Enum

class Ground(Enum):
    DP = 'Digswell Park'
    WPF = 'Welwyn Playing Fields'
    AWAY = 'Away'

class InvalidType(Enum):
    MIS_MATCH = 1
    NOT_FOUND = 2

class SourceData(Enum):
    GOOGLE_CALENDAR = 1
    PLAY_CRICKET = 2

class PlayCricketType(Enum):
    FIXTURES = 1
    RESULTS = 2