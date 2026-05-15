from enum import Enum, StrEnum

class Location(StrEnum):
    HOME = 'Home'
    AWAY = 'Away'

class Ground(StrEnum):
    DP = 'Digswell Park'
    WPF = 'Welwyn Playing Fields'
    AWAY = 'Away'

    @classmethod
    def get_value(cls, value):
        for k, v in cls.__members__.items():
            if v.value == value:
                return v
        else:
            return Ground.AWAY

class FixtureType(StrEnum):
    LEAGUE = 'League'
    FRIENDLY = 'Friendly'
    CUP = 'Cup'
    SENIOR = 'Senior'
    UNKNOWN = 'Unknown'
    POSTPONED = 'Postponed'

    @classmethod
    def get_value(cls, value):
        for k, v in cls.__members__.items():
            if v.value == value:
                return v
        else:
            return FixtureType.UNKNOWN
