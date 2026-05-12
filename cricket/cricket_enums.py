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

class SourceData(Enum):
    GOOGLE_CALENDAR = 0
    PLAY_CRICKET = 1

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

class Notes(StrEnum):
    ASTRO = 'Astro'
    ASTRO_MAYBE = 'Astro?'
    CANCELLED = 'Cancelled'
    POSTPONED = 'Postponed'
    UNKNOWN = 'Unknown'

    @classmethod
    def get_value(cls, value):
        for k, v in cls.__members__.items():
            if v.value == value:
                return v
        else:
            return Notes.UNKNOWN