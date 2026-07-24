from enum import Enum

class CricketTeam(Enum):
    GIRLS = ('WGCCC Girls U9', 'Welwyn Garden City CC - Under 9', 'U9 Girls Group 2', 'Ian Watkins')
    U9s = ('WGCCC U9', 'Welwyn Garden City CC - Under 9','U9 Group 6', 'Bharat Ranavaya')
    U10s = ('WGCCC U10B', 'Welwyn Garden City CC - Under 10', 'U10B Group 2', 'Jack Bailey')
    U11s = ('WGCCC U11', 'Welwyn Garden City CC - Under 11', 'U11A Group 4', 'Jay Bhatt')
    U12s = ('WGCCC U12', 'Welwyn Garden City CC - Under 12', 'U12A Group 5', 'Manish Patel')
    U12As = ('WGCCC U12 A', 'Welwyn Garden City CC - Under 12 A', 'U12A - Knockout stages', 'Manish Patel A')
    U13s = ('WGCCC U13', 'Welwyn Garden City CC - Under 13', 'U13A Group 3' , 'Cheryl Worman')
    U14s = ('WGCCC U14', 'Welwyn Garden City CC - Under 14', 'U14A Group 1', 'Gareth Munday')
    U15s = ('WGCCC U15', 'Welwyn Garden City CC - Under 15', 'U15A Group 3', 'Robert Nicholls')
    U17s = ('WGCCC U17', 'Welwyn Garden City CC - Under 17', 'HJCL U17 Group 3', 'Mark Bailey')
    U11summer  = ('WGCCC U11 Summer', 'Welwyn Garden City CC - Under 11 Summer', 'U11 Summer League - North Group', 'U11 Summer Host')
    U12summer = ('WGCCC U12 Summer', 'Welwyn Garden City CC - Under 12 Summer', 'U12 Summer League - South Group', 'U12 Summer Host')
    U13summer = ('WGCCC U13 Summer', 'Welwyn Garden City CC - Under 13 Summer', 'U13 Summer League - North Group', 'U13 Summer Host')
    U14summer = ('WGCCC U14 Summer', 'Welwyn Garden City CC - Under 14 Summer', 'U14 Summer League - Central Group', 'U14 Summer Host')
    U15summer = ('WGCCC U15 Summer', 'Welwyn Garden City CC - Under 15 Summer', 'U15 Summer League - North Group', 'U15 Summer Host')
    FirstXI = ('Saturday 1st XI', 'Welwyn Garden City Cricket Club Saturday 1st XI', 'HPCL Premiership Division', 'First Team Capt')
    SecondXI = ('Saturday 2nd XI', 'Welwyn Garden City Cricket Club Saturday 2nd XI', 'HPCL Division 3 A', 'Second Team Capt')
    ThirdXI = ('Saturday 3rd XI', 'Welwyn Garden City Cricket Club Saturday 3rd XI', 'HPCL Division 6 A', 'Third Team Capt')
    FourthXI = ('Saturday 4th XI', 'Welwyn Garden City Cricket Club Saturday 4th XI', 'HPCL Division 11 East', 'Fourth Team Capt')
    FifthXI = ('Saturday 5th XI', 'Welwyn Garden City Cricket Club Saturday 5th XI', 'HPCL Division 14 East', 'Fifth Team Capt')
    SundayXI = ('Sunday XI', 'Welwyn Garden City Cricket Club Sunday XI', 'ECB Friendly', 'Sunday Team Capt')
    WGCCCJuniors = ('WGCCC Juniors', 'A WGCCC Junior Team', '','')
    CricketWeek = ('Cricket Week XI', 'Welwyn Garden City Cricket Week Team', 'Cricket Week', 'Cricket Week Host')
    CricketWeekInter = ('Beynon XI', 'Welwyn Garden City Cricket Week Team', 'Cricket Week', 'Cricket Week Host')
    WGCCC = ('WGCCC', 'A WGCCC Team', '', '')
    Hertfordshire = ('Hertfordshire', 'Hertfordshire', 'NCAA', 'Herts')
    HertsO50s = ('Hertfordshire Over-50s', 'Herts Over 50s', 'Over 50 League', 'Herts')
    HertsO60s = ('Hertfordshire Over-60s', 'Herts Over 60s', 'Over 60 League', 'Herts')
    NotWGCCC = ('Not a WGCCC Team', 'Not a WGCCC Team', '', '')
    UNKNOWN = ('Unknown','Unknown','Unknown', 'Unknown')

    def __new__(cls, team_name, team_fullname, division, host):
        obj = object.__new__(cls)
        obj._value_ = team_name
        obj.team_fullname = team_fullname
        obj.division = division
        obj.host = host
        return obj

    def __eq__(self, other):
        return self.value == other.value

    __hash__ = object.__hash__

    @classmethod
    def get_value(cls, value):
        for k, v in cls.__members__.items():
            if v.value == value:
                return v
        if value == "Totteridge Millhillians CC 1st XI":
            return CricketTeam.FirstXI
        print(f"Missing Cricket Team: {value}")
        return CricketTeam.UNKNOWN

    @classmethod
    def get_from_fullname(cls, fullname):
        for k, v in cls.__members__.items():
            if v.team_fullname == fullname:
                return v
        return CricketTeam.UNKNOWN

    @classmethod
    def get_from_division(cls, division):
        for k, v in cls.__members__.items():
            if v.division == division:
                return v
        return CricketTeam.UNKNOWN

    @classmethod
    def get_from_host(cls, host):
        for k, v in cls.__members__.items():
            if v.host == host:
                return v
        return CricketTeam.UNKNOWN

