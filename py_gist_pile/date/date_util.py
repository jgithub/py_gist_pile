from datetime import datetime

def get_milliseconds_since_date(date_start: datetime) -> int:
    return int((datetime.now() - date_start).total_seconds() * 1000)
