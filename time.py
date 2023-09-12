from cac.text import Text

HOURS_IN_DAY: int = 24
MINUTES_IN_HOUR: int = 60

class Time:

    def __init__(self, hour: int, minute: int) -> None:
        assert 0 <= hour < HOURS_IN_DAY
        assert 0 <= minute < MINUTES_IN_HOUR
        self._hour: int = hour
        self._minute: int = minute

    def __eq__(self, other) -> bool:
        return self._hour == other.hour and self._minute == other.minute

    def __str__(self) -> str:
        return Text.pad_number(self._hour, 2) + ':' + Text.pad_number(self._minute, 2)

    def __repr__(self) -> str:
        return self.__str__()

    def __lt__(self, other: 'Time') -> bool:
        if self.hour == other.hour:
            if self.minute == other.minute:
                return False
            return self.minute < other.minute
        return self.hour < other.hour

    def __le__(self, other: 'Time') -> bool:
        if self.hour == other.hour:
            if self.minute == other.minute:
                return False
            return self.minute <= other.minute
        return self.hour <= other.hour

    def __gt__(self, other: 'Time') -> bool:
        if self.hour == other.hour:
            if self.minute == other.minute:
                return False
            return self.minute > other.minute
        return self.hour > other.hour

    def __ge__(self, other: 'Time') -> bool:
        if self.hour == other.hour:
            if self.minute == other.minute:
                return False
            return self.minute >= other.minute
        return self.hour >= other.hour

    @property
    def hour(self) -> int:
        return self._hour

    @property
    def minute(self) -> int:
        return self._minute

    def add_minutes(self, minutes: int) -> 'Time':
        cloned_time: Time = self.clone()
        for i in range(0, minutes):
            cloned_time = cloned_time.add_minute()
        return cloned_time

    def add_minute(self) -> 'Time':
        cloned_time: Time = self.clone()
        cloned_time._minute += 1
        if cloned_time._minute == MINUTES_IN_HOUR:
            cloned_time._minute = 0
            cloned_time = cloned_time.add_hour()
        return cloned_time

    def subtract_minutes(self, minutes: int) -> 'Time':
        cloned_time: Time = self.clone()
        for i in range(0, minutes):
            cloned_time = cloned_time.subtract_minute()
        return cloned_time

    def subtract_minute(self) -> 'Time':
        cloned_time: Time = self.clone()
        cloned_time._minute -= 1
        if cloned_time._minute == -1:
            cloned_time._minute = MINUTES_IN_HOUR - 1
            cloned_time = cloned_time.subtract_hour()
        return cloned_time

    def add_hours(self, hours: int) -> 'Time':
        cloned_time: Time = self.clone()
        for i in range(0, hours):
            cloned_time = cloned_time.add_hour()
        return cloned_time

    def add_hour(self) -> 'Time':
        cloned_time: Time = self.clone()
        cloned_time._hour += 1
        if cloned_time._hour == HOURS_IN_DAY:
            cloned_time._hour = 0
        return cloned_time

    def subtract_hours(self, hours: int) -> 'Time':
        cloned_time: Time = self.clone()
        for i in range(0, hours):
            cloned_time = cloned_time.subtract_hour()
        return cloned_time

    def subtract_hour(self) -> 'Time':
        cloned_time: Time = self.clone()
        cloned_time._hour -= 1
        if cloned_time._hour == -1:
            cloned_time._hour = HOURS_IN_DAY - 1
        return cloned_time

    def clone(self) -> 'Time':
        return Time(self._hour, self._minute)

    def get_meridiem_string(self) -> str:
        meridiem: str = 'AM' if self._hour < HOURS_IN_DAY / 2 else 'PM'
        hour: int = self._hour
        if self._hour == 0:
            hour = HOURS_IN_DAY // 2
        if self._hour > HOURS_IN_DAY / 2:
            hour = self._hour - HOURS_IN_DAY // 2
        return Text.pad_number(hour, 2) + ':' + Text.pad_number(self._minute, 2) + ' ' + meridiem
