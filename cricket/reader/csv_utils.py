from datetime import datetime, timezone, timedelta

def get_fixture_start_datetime(date_string, time_string):
    bst_date_time_string = date_string + ' ' + time_string
    return datetime.strptime(bst_date_time_string , "%d/%m/%Y %H:%M").astimezone(timezone.utc)

def get_fixture_end_datetime(fixture_start_datetime):
    return fixture_start_datetime + timedelta(hours=3)
