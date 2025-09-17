from enum import Enum

class Location(Enum):
    HOME = 'home'
    AWAY = 'away'

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

class FixtureType(Enum):
    LEAGUE = 'League'
    FRIENDLY = 'Friendly'
    CUP = 'Cup'
    SENIOR = 'Senior'
    UNKNOWN = 'Unknown'

    @classmethod
    def get_value(cls, value):
        for k, v in cls.__members__.items():
            if v.value == value:
                return v
        else:
            return FixtureType.UNKNOWN
