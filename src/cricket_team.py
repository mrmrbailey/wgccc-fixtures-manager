from enum import Enum

class CricketTeam(Enum):
    GIRLS = ('WGCCC Girls U9', 'Welwyn Garden City CC - Under 9', 'HJCL U9 Girls Group 2')
    U9s = ('WGCCC U9', 'Welwyn Garden City CC - Under 9','HJCL U9 Group 6')
    U10s = ('WGCCC U10B', 'Welwyn Garden City CC - Under 10 B', 'HJCL U10B Group 5')
    U11s = ('WGCCC U11', 'Welwyn Garden City CC - Under 11', 'HJCL U11A Group 4')
    U12s = ('WGCCC U12', 'Welwyn Garden City CC - Under 12', 'HJCL U12A Group 5')
    U13s = ('WGCCC U13', 'Welwyn Garden City CC - Under 13', 'HJCL U13A Group 4')
    U14s = ('WGCCC U14B', 'Welwyn Garden City CC - Under 14 B', 'HJCL U14B Group 4')
    U15s = ('WGCCC U15', 'Welwyn Garden City CC - Under 15', 'HJCL U15A Group 3')
    U17s = ('WGCCC U17', 'Welwyn Garden City CC - Under 17', 'HJCL U17 Group 3')
    U11summer  = ('WGCCC U11 Summer', 'Welwyn Garden City CC - Under 11 Summer', 'U11 Summer League - East Group')
    U13summer = ('WGCCC U13 Summer', 'Welwyn Garden City CC - Under 13 Summer', 'U13 Summer League - North Group')
    U15summer = ('WGCCC U15 Summer', 'Welwyn Garden City CC - Under 15 Summer', 'U15 Summer League - North Group')
    FirstXI = ('Saturday 1st XI', 'Welwyn Garden City Cricket Club Saturday 1st XI', 'HPCL Premiership Division')
    SecondXI = ('Saturday 2nd XI', 'Welwyn Garden City Cricket Club Saturday 2nd XI', 'HPCL Division 3 A')
    ThirdXI = ('Saturday 3rd XI', 'Welwyn Garden City Cricket Club Saturday 3rd XI', 'HPCL Division 6 A')
    FourthXI = ('Saturday 4th XI', 'Welwyn Garden City Cricket Club Saturday 4th XI', 'HPCL Division 11 East')
    FifthXI = ('Saturday 5th XI', 'Welwyn Garden City Cricket Club Saturday 5th XI', 'HPCL Division 14 East')
    SundayXI = ('WGCCC Sunday XI', 'Welwyn Garden City Cricket Club Sunday XI', 'ECB Friendly')
    WGCCCJuniors = ('WGCCC Juniors', 'A WGCCC Junior Team', '')
    WGCCC = ('WGCCC', 'A WGCCC Team', '')
    HertsO50s = ('Herts O50s', 'Herts Over 50s', 'Over 50 League')
    HertsO60s = ('Herts Over 60s', 'Herts Over 60s', 'Over 60 League')
    NotWGCCC = ('Not a WGCCC Team', 'Not a WGCCC Team', '')
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
            print(f"Missing Cricket Team: {value}")
            return CricketTeam.UNKNOWN

    @classmethod
    def get_from_fullname(cls, fullname):
        for k, v in cls.__members__.items():
            if v.team_fullname == fullname:
                return v
        else:
            return CricketTeam.UNKNOWN

