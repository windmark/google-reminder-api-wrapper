import datetime
import dateutil.parser


def create_date_object(date):
    if not isinstance(date, datetime.datetime):
        date = dateutil.parser.parse(date)

    date_object = {
        "year": date.year,
        "month": date.month,
        "day": date.day,
        "time": {
            "hour": date.hour,
            "minute": date.minute,
            "second": date.second
        }
    }
    return date_object
