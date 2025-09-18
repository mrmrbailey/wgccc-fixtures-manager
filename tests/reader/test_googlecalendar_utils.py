from src.cricket_enums import FixtureType
from datetime import datetime, timezone, date

import pytest

from src.reader.googlecalendar_utils import clean_summary, get_teams, get_fixture_type_from_description, \
    clean_fixture_date, is_fixture_this_year, get_fixture_type_from_summary

summary_test_data = [
    ('Saturday 2nd XI v Hemel Hempstead Town CC 2nd XI',
     'Saturday 2nd XI v Hemel Hempstead Town CC 2nd XI'),
    ('WGCCC, U15 vs Knebworth Park CC - Under 15 (22 yards)',
     'WGCCC U15 vs Knebworth Park CC - Under 15'),
    ('WGCCC U15 vs Knebworth Park CC - Under 15 (22 yards)',
     'WGCCC U15 vs Knebworth Park CC - Under 15'),
    ('CANCELLED: Hertford v WGCCC U14B (22 yards)',
     'Hertford v WGCCC U14B')
]

@pytest.mark.parametrize('summary,expected', summary_test_data)
def test_clean_summary(summary, expected):
    assert clean_summary(summary) == expected

teams_test_data = [
    ('Saturday 2nd XI v Hemel Hempstead Town CC 2nd XI',
     ['Saturday 2nd XI','Hemel Hempstead Town CC 2nd XI']),
    ('Saturday 2nd XI vs Hemel Hempstead Town CC 2nd XI',
     ['Saturday 2nd XI','Hemel Hempstead Town CC 2nd XI']),
    ('Welwyn Beavers - Cricket intro',
     ['Not a WGCCC Team', 'Welwyn Beavers - Cricket intro']),
    ('WGCCC 1st XI v Hemel Hempstead Town CC 2nd XI',
     ['Saturday 1st XI', 'Hemel Hempstead Town CC 2nd XI']),
    ('WGCCC 2nd XI v Hemel Hempstead Town CC 2nd XI',
     ['Saturday 2nd XI', 'Hemel Hempstead Town CC 2nd XI']),
    ('WGCCC 3rd XI v Hemel Hempstead Town CC 2nd XI',
     ['Saturday 3rd XI', 'Hemel Hempstead Town CC 2nd XI']),
    ('WGCCC U11A v Hemel Hempstead Town CC 2nd XI',
     ['WGCCC U11', 'Hemel Hempstead Town CC 2nd XI']),
    ('WGCCC U11 Summer vs Cokenach CC - Under 11',
     ['Cokenach CC - Under 11', 'WGCCC U11 Summer'])
]

@pytest.mark.parametrize('summary,expected', teams_test_data)
def test_get_teams(summary, expected):
    assert get_teams(summary) == expected

description_test_data = [
    ('Welwyn Garden City Cricket Club Saturday 1st XI v Hertford CC 1st XI on Sat 12 Jul 2025 at 11:00',
     FixtureType.SENIOR.value),
    ('Welwyn Garden City CC - Under 15 Summer v Knebworth Park CC - Under 15 on Wed 20 Aug 2025 at 18:00~League~U15 Summer League - North Group',
     FixtureType.LEAGUE.value),
    ('Welwyn Garden City CC - Under 12 v Letchworth Garden City CC - Under 12 A on Wed 30 Jul 2025 at 18:00~Friendly',
     FixtureType.FRIENDLY.value),
    ('West Herts CC - U11 Green v Welwyn Garden City CC - Under 11 on Thu 10 Jul 2025 at 18:00~Cup',
     FixtureType.CUP.value),
    #Google Meet Tests
    ('-::~:~::~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~::~:~::-JOIN WITH GOOGLE MEET: HTTPS://MEET.GOOGLE.COM/PYA-DKJT-QQQLEARN MORE ABOUT MEET AT: HTTPS://SUPPORT.GOOGLE.COM/A/USERS/ANSWER/9282720PLEASE DO NOT EDIT THIS SECTION.-::~:~::~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~::~:~::-',
     FixtureType.SENIOR.value),
    #2025 tests
    ('Hertford CC - Under 9 v Welwyn Garden City CC - Under 9 on Sun 31 Aug 2025 at 18:00:League:HJCL U9 Girls Group 2',
     FixtureType.LEAGUE.value),
    ('Friendly:Friendly', FixtureType.FRIENDLY.value),
    ('Cup:Cup', FixtureType.CUP.value),
    (None, FixtureType.UNKNOWN.value),
]

@pytest.mark.parametrize('description,expected', description_test_data)
def test_get_fixture_type_from_description(description, expected):
    assert get_fixture_type_from_description(description) == expected

summary_test_data_for_fixture_type = [
    ('Saturday 2nd XI v Hemel Hempstead Town CC 2nd XI', FixtureType.SENIOR.value),
    ('WGCCC, U15 vs Knebworth Park CC - Under 15 (22 yards)', FixtureType.LEAGUE.value),
]

@pytest.mark.parametrize('summary,expected', summary_test_data_for_fixture_type)
def test_get_fixture_type_from_summary(summary, expected):
    assert get_fixture_type_from_summary(summary) == expected


date_test_data = [
    (datetime(2025, 4, 2, tzinfo=timezone.utc),
     True),
    (datetime(2025, 3, 1, tzinfo=timezone.utc),
     False),
    (date(2025, 4, 2),
     True),
    (date(2025, 3, 1),
     False)
]

@pytest.mark.parametrize('calendar_date,expected', date_test_data)
def test_is_fixture_this_year(calendar_date, expected):
    assert is_fixture_this_year(clean_fixture_date(calendar_date)) is expected