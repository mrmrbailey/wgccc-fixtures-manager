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

class FixtureType(Enum):
    LEAGUE = 'League'
    FRIENDLY = 'Friendly'
    CUP = 'Cup'
    UNKNOWN = 'Unknown'

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
    U11summer  = 'WGCCC U11 Summer'
    U13summer = 'WGCCC U13 Summer'
    U15summer = 'WGCCC U15 Summer'
    UNKNOWN = 'Unknown'

class FullTeamName(Enum):
    GIRLS = 'Welwyn Garden City CC - Under 9'
    U9s = 'Welwyn Garden City CC - Under 9'
    U10s = 'Welwyn Garden City CC - Under 10 B'
    U11s = 'Welwyn Garden City CC - Under 11'
    U12s = 'Welwyn Garden City CC - Under 12'
    U13s = 'Welwyn Garden City CC - Under 13'
    U14s = 'Welwyn Garden City CC - Under 14 B'
    U15s = 'Welwyn Garden City CC - Under 15'
    U17s = 'Welwyn Garden City CC - Under 17'
    U11summer  = 'Welwyn Garden City CC - Under 11 Summer'
    U13summer = 'Welwyn Garden City CC - Under 13 Summer'
    U15summer = 'Welwyn Garden City CC - Under 15 Summer'
    UNKNOWN = 'Unknown'


class Division(Enum):
    GIRLS = 'HJCL U9 Girls Group 2'
    U9s = 'HJCL U9 Group 6'
    U10s = 'HJCL U10B Group 5'
    U11s = 'HJCL U11A Group 4'
    U12s = 'HJCL U12A Group 5'
    U13s = 'HJCL U13A Group 4'
    U14s = 'HJCL U14B Group 4'
    U15s = 'HJCL U15A Group 3'
    U17s = 'HJCL U17 Group 3'
    U11summer = 'U11 Summer League - East Group'
    U13summer = 'U13 Summer League - North Group'
    U15summer = 'U15 Summer League - North Group'
    CUP = 'Cup'
    FRIENDLY = 'Friendly'
    UNKNOWN = 'UNKNOWN'
