from fixture import Fixture

from datetime import timedelta, datetime, timezone

def should_fixture_have_result(fixture: Fixture):
    days_to_wait_for_result = 3
    return fixture.fixture_start_datetime < datetime.now(timezone.utc) - timedelta(days=days_to_wait_for_result)