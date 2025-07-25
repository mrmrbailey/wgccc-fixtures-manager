from enum import Enum

class CricketTeam(Enum):
    GIRLS = ('WGCCC Girls U9', 'Welwyn Garden City CC - Under 9', 'HJCL U9 Girls Group 2')
    U9s = ('WGCCC U9', 'Welwyn Garden City CC - Under 9','HJCL U9 Group 6')
    U10s = ('WGCCC U10B', 'Welwyn Garden City CC - Under 10 B', 'HJCL U10B Group 5')
    U11s = ('WGCCC U11A', 'Welwyn Garden City CC - Under 11', 'HJCL U11A Group 4')
    U12s = ('WGCCC U12', 'Welwyn Garden City CC - Under 12', 'HJCL U12A Group 5')
    U13s = ('WGCCC U13', 'Welwyn Garden City CC - Under 13', 'HJCL U13A Group 4')
    U14s = ('WGCCC U14B', 'Welwyn Garden City CC - Under 14 B', 'HJCL U14B Group 4')
    U15s = ('WGCCC U15', 'Welwyn Garden City CC - Under 15', 'HJCL U15A Group 3')
    U17s = ('WGCCC U17', 'Welwyn Garden City CC - Under 17', 'HJCL U17 Group 3')
    U11summer  = ('WGCCC U11 Summer', 'Welwyn Garden City CC - Under 11 Summer', 'U11 Summer League - East Group')
    U13summer = ('WGCCC U13 Summer', 'Welwyn Garden City CC - Under 13 Summer', 'U13 Summer League - North Group')
    U15summer = ('WGCCC U15 Summer', 'Welwyn Garden City CC - Under 15 Summer', 'U15 Summer League - North Group')
    UNKNOWN = ('Unknown','Unknown','Unknown')

    def __new__(cls, team_name, team_fullname, division):
        obj = object.__new__(cls)
        obj._value_ = team_name
        obj.team_fullname = team_fullname
        obj.division = division
        return obj

    def __eq__(self, other):
        return self.value == other.value

    @classmethod
    def get_value(cls, value):
        for k, v in cls.__members__.items():
            if v.value == value:
                return v
        else:
            return CricketTeam.UNKNOWN

    @classmethod
    def get_from_fullname(cls, fullname):
        for k, v in cls.__members__.items():
            if v.team_fullname == fullname:
                return v
        else:
            return CricketTeam.UNKNOWN

