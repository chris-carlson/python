from datetime import date
from enum import IntEnum
from typing import List

from cac.math import Math
from cac.regex import Regex
from cac.string import String

DATE_REGEX: Regex = Regex('\\d{4}\\D\\d{2}\\D\\d{2}')
NUMBER_REGEX: Regex = Regex('\\d+')
NUM_MONTHS: int = 12
DAYS_IN_MONTHS: List[int] = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
DAYS_IN_WEEK: int = 7
LEAP_MONTH: int = 2
LEAP_YEAR_FREQUENCY: int = 4


class Date:

    @staticmethod
    def parse_date(date_str: str) -> 'Date':
        if not DATE_REGEX.matches(date_str):
            raise ValueError('Date must match the format ####-##-##')
        matches: List[str] = NUMBER_REGEX.find_matches(date_str)
        return Date(int(matches[0]), int(matches[1]), int(matches[2]))

    @staticmethod
    def today() -> 'Date':
        today: date = date.today()
        return Date(today.year, today.month, today.day)

    def __init__(self, year: int, month: int, day_of_month: int) -> None:
        self._year: int = year
        self._month: int = month
        self._day_of_month: int = day_of_month
        self._day_of_week: IntEnum = self._get_day_of_week()
        assert len(str(year)) == 4
        assert 1 <= month <= NUM_MONTHS
        assert self._day_is_valid()

    def __eq__(self, other) -> bool:
        return self._year == other.year and self._month == other.month and self._day_of_month == other.day_of_month

    def __str__(self) -> str:
        return self._day_of_week.name.capitalize() + ' ' + str(self._year) + '/' + String.pad_number(
            self._month) + '/' + String.pad_number(self._day_of_month)

    def __repr__(self) -> str:
        return self.__str__()

    def __lt__(self, other) -> bool:
        if self.year == other.year:
            if self.month == other.month:
                if self.day_of_month == other.day_of_month:
                    return False
                return self.day_of_month < other.day_of_month
            return self.month < other.month
        return self.year < other.year

    def __le__(self, other) -> bool:
        if self.year == other.year:
            if self.month == other.month:
                if self.day_of_month == other.day_of_month:
                    return True
                return self.day_of_month <= other.day_of_month
            return self.month <= other.month
        return self.year <= other.year

    def __gt__(self, other) -> bool:
        if self.year == other.year:
            if self.month == other.month:
                if self.day_of_month == other.day_of_month:
                    return False
                return self.day_of_month > other.day_of_month
            return self.month > other.month
        return self.year > other.year

    def __ge__(self, other) -> bool:
        if self.year == other.year:
            if self.month == other.month:
                if self.day_of_month == other.day_of_month:
                    return True
                return self.day_of_month >= other.day_of_month
            return self.month >= other.month
        return self.year >= other.year

    @property
    def year(self) -> int:
        return self._year

    @property
    def month(self) -> int:
        return self._month

    @property
    def day_of_month(self) -> int:
        return self._day_of_month

    @property
    def day_of_week(self) -> IntEnum:
        return self._day_of_week

    def add_day(self) -> 'Date':
        cloned_date: Date = self.clone()
        cloned_date._day_of_month += 1
        if cloned_date._day_of_month > cloned_date._get_days_in_current_month():
            cloned_date._month += 1
            if cloned_date._month > NUM_MONTHS:
                cloned_date._month = 1
                cloned_date._year += 1
            cloned_date._day_of_month = 1
        cloned_date._day_of_week = DayOfWeek((cloned_date._day_of_week.value + 1) % DAYS_IN_WEEK)
        return cloned_date

    def add_days(self, days: int) -> 'Date':
        cloned_date: Date = self.clone()
        for i in range(0, days):
            cloned_date = cloned_date.add_day()
        return cloned_date

    def subtract_day(self) -> 'Date':
        cloned_date: Date = self.clone()
        cloned_date._day_of_month -= 1
        if cloned_date._day_of_month < 1:
            cloned_date._month -= 1
            if cloned_date._month < 1:
                cloned_date._month = NUM_MONTHS
                cloned_date._year -= 1
            cloned_date._day_of_month = cloned_date._get_days_in_current_month()
        cloned_date._day_of_week = DayOfWeek((cloned_date._day_of_week.value - 1) % DAYS_IN_WEEK)
        return cloned_date

    def subtract_days(self, days: int) -> 'Date':
        cloned_date: Date = self.clone()
        for i in range(0, days):
            cloned_date = cloned_date.subtract_day()
        return cloned_date

    def get_days_to(self, target_date) -> int:
        cloned_date: Date = target_date.clone()
        num_days: int = 0
        while self < cloned_date:
            cloned_date = cloned_date.subtract_day()
            num_days += 1
        while self > cloned_date:
            cloned_date = cloned_date.add_day()
            num_days -= 1
        return num_days

    def clone(self) -> 'Date':
        return Date(self._year, self._month, self._day_of_month)

    def _get_day_of_week(self) -> IntEnum:
        new_month: int = Math.one_based_mod(self._month, -2, 12)
        first_two_digits_of_year: int = int(str(self._year)[:2])
        last_two_digits_of_year: int = int(str(self._year)[2:])
        if new_month > 10:
            last_two_digits_of_year -= 1
        return DayOfWeek((self._day_of_month + int((13 * new_month - 1) / 5) + last_two_digits_of_year + int(
            last_two_digits_of_year / 4) + int(first_two_digits_of_year / 4) - 2 * first_two_digits_of_year) % 7)

    def _get_days_in_current_month(self) -> int:
        if self._month == LEAP_MONTH and self._is_leap_year():
            return DAYS_IN_MONTHS[LEAP_MONTH - 1] + 1
        return DAYS_IN_MONTHS[self._month - 1]

    def _is_leap_year(self) -> bool:
        return self._year % LEAP_YEAR_FREQUENCY == 0 and (
                self._year % (LEAP_YEAR_FREQUENCY * 25) != 0 or self._year % (LEAP_YEAR_FREQUENCY * 100) == 0)

    def _day_is_valid(self) -> bool:
        return 1 <= self._day_of_month <= self._get_days_in_current_month()


class DayOfWeek(IntEnum):
    SUNDAY: int = 0
    MONDAY: int = 1
    TUESDAY: int = 2
    WEDNESDAY: int = 3
    THURSDAY: int = 4
    FRIDAY: int = 5
    SATURDAY: int = 6
