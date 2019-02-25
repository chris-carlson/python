from typing import Dict

from cac.string import String

HOURS_IN_DAY: int = 24
MINUTES_IN_HOUR: int = 60
MERIDIEM: Dict[str, str] = {'AM': 'AM', 'PM': 'PM'}


class Time:

    def __init__(self, hour: int, minute: int, meridiem: str) -> None:
        assert 0 < hour <= HOURS_IN_DAY / 2
        assert 0 <= minute < MINUTES_IN_HOUR
        assert meridiem in MERIDIEM
        self._hour: int = hour
        self._minute: int = minute
        self._meridiem: str = meridiem

    def __eq__(self, other) -> bool:
        return self._hour == other.hour and self._minute == other.minute and self._meridiem == other.meridiem

    def __str__(self) -> str:
        return String.pad_number(self._hour) + ':' + String.pad_number(self._minute) + ' ' + self._meridiem

    def __repr__(self) -> str:
        return self.__str__()

    @property
    def hour(self) -> int:
        return self._hour

    @property
    def minute(self) -> int:
        return self._minute

    @property
    def meridiem(self) -> str:
        return self._meridiem

    def add_minutes(self, minutes: int) -> None:
        for i in range(0, minutes):
            self.add_minute()

    def add_minute(self) -> None:
        self._minute += 1
        if self._minute == MINUTES_IN_HOUR:
            self._minute = 0
            self.add_hour()

    def subtract_minutes(self, minutes: int) -> None:
        for i in range(0, minutes):
            self.subtract_minute()

    def subtract_minute(self) -> None:
        self._minute -= 1
        if self._minute == -1:
            self._minute = MINUTES_IN_HOUR - 1
            self.subtract_hour()

    def add_hours(self, hours: int) -> None:
        for i in range(0, hours):
            self.add_hour()

    def add_hour(self) -> None:
        self._hour += 1
        if self._hour == HOURS_IN_DAY / 2:
            self._toggle_meridiem()
        if self._hour > HOURS_IN_DAY / 2:
            self._hour = 1

    def subtract_hours(self, hours: int) -> None:
        for i in range(0, hours):
            self.subtract_hour()

    def subtract_hour(self) -> None:
        self._hour -= 1
        if self._hour == HOURS_IN_DAY / 2 - 1:
            self._toggle_meridiem()
        if self._hour == 0:
            self._hour = HOURS_IN_DAY // 2

    def get_military_hour(self) -> int:
        if self._meridiem == MERIDIEM['PM']:
            if self._hour == HOURS_IN_DAY / 2:
                return self._hour
            return self._hour + int(HOURS_IN_DAY / 2)
        return self._hour

    def _calculate_meridiem(self) -> str:
        if self._hour < HOURS_IN_DAY / 2:
            return MERIDIEM['AM']
        return MERIDIEM['PM']

    def _toggle_meridiem(self) -> None:
        if self._meridiem == MERIDIEM['AM']:
            self._meridiem = MERIDIEM['PM']
        else:
            self._meridiem = MERIDIEM['AM']
