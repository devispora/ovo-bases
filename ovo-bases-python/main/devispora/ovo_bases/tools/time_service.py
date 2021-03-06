from datetime import datetime
from pytz import utc

one_hour_in_seconds = 3600
day_in_seconds = 86400
three_days = (day_in_seconds * 3)


def get_event_day_from_timestamp(timestamp: int) -> int:
    current_date = datetime.fromtimestamp(timestamp, tz=utc)
    result = current_date.replace(hour=0, minute=0, second=0, microsecond=0)
    return int(result.timestamp())


def grab_next_day(timestamp: int) -> int:
    next_day = timestamp + day_in_seconds
    calibrated_day = get_event_day_from_timestamp(next_day)
    return calibrated_day


def get_current_time() -> int:
    return int(datetime.now(tz=utc).timestamp())
