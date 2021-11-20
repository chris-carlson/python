from datetime import datetime

from cac.date import Date
from cac.date_time import DateTime
from cac.time import Time
from dateutil import tz
from dateutil.tz import tzutc


class TimeZone:

    @staticmethod
    def get_local_time(date_time: DateTime) -> DateTime:
        utc_zone: tzutc = tz.tzutc()
        local_zone: tzutc = tz.tzlocal()
        utc: datetime = datetime.strptime(str(date_time.date) + ' ' + str(date_time.time), '%Y-%m-%d %H:%M')
        utc = utc.replace(tzinfo=utc_zone)
        local: datetime = utc.astimezone(local_zone)
        return DateTime(Date(local.year, local.month, local.day), Time(local.hour, local.minute))
