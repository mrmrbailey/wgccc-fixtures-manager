import pytest

from reader.csv_utils import get_fixture_start_datetime, get_fixture_end_datetime

from datetime import datetime, timezone

get_fixture_start_date_timetest_data = [
    ('01/04/2025', "18:00", datetime(2025, 4, 1, 17, 00, tzinfo=timezone.utc)),
]

@pytest.mark.parametrize('date_string,time_string,expected', get_fixture_start_date_timetest_data)
def test_get_fixture_start_datetime(date_string, time_string, expected):
    assert get_fixture_start_datetime(date_string, time_string) == expected

get_fixture_end_date_timetest_data = [
    (datetime(2025, 4, 1, 17, 00, tzinfo=timezone.utc),
     datetime(2025, 4, 1, 20, 00, tzinfo=timezone.utc)),
]

@pytest.mark.parametrize('start_datetime,expected', get_fixture_end_date_timetest_data)
def test_get_fixture_end_datetime(start_datetime, expected):
    assert get_fixture_end_datetime(start_datetime) == expected
