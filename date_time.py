from cac.date import Date
from cac.time import Time

class DateTime:

    def __init__(self, date: Date, time: Time) -> None:
        self._date: Date = date
        self._time: Time = time

    def __eq__(self, other: 'DateTime') -> bool:
        return self.date == other.date and self.time == other.time

    def __str__(self) -> str:
        return str(self.date) + ' ' + str(self.time)

    def __repr__(self) -> str:
        return self.__str__()

    def __lt__(self, other: 'DateTime') -> bool:
        if self.date == other.date:
            if self.time == other.time:
                return False
            return self.time < other.time
        return self.date < other.date

    def __le__(self, other: 'DateTime') -> bool:
        if self.date == other.date:
            if self.time == other.time:
                return False
            return self.time <= other.time
        return self.date <= other.date

    def __gt__(self, other: 'DateTime') -> bool:
        if self.date == other.date:
            if self.time == other.time:
                return False
            return self.time > other.time
        return self.date > other.date

    def __ge__(self, other: 'DateTime') -> bool:
        if self.date == other.date:
            if self.time == other.time:
                return False
            return self.time >= other.time
        return self.date >= other.date

    @property
    def date(self) -> Date:
        return self._date

    @property
    def time(self) -> Time:
        return self._time
