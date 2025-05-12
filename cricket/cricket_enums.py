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

class TeamName(Enum):
    GIRLS = 'WGCCC Girls U9'
    U9s = 'WGCCC U9'
    U10s = 'WGCCC U10B'
    U11s = 'WGCCC U11A'
    U12s = 'WGCCC U12'
    U13s = 'WGCCC U13'
    U14s = 'WGCCC U14B'
    U15s = 'WGCCC U15'
    U17s = 'WGCCC U17'
    UNKNOWN = 'Unknown'
