from datetime import date
from enum import IntEnum
from typing import Dict, List

from cac.consumer import Consumer
from cac.math import Math
from cac.regex import Regex
from cac.string import String

DATE_REGEX_1: Regex = Regex('\d{4}\D\d{2}\D\d{2}')
DATE_REGEX_2: Regex = Regex('\d{2}\D\d{2}\D\d{4}')
NUMBER_REGEX: Regex = Regex('\d+')
NUM_MONTHS: int = 12
DAYS_IN_MONTHS: List[int] = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
DAYS_IN_WEEK: int = 7
LEAP_MONTH: int = 2
LEAP_YEAR_FREQUENCY: int = 4

MONTHS: Dict[str, int] = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9,
        'Oct': 10, 'Nov': 11, 'Dec': 12}


class Date:

    @staticmethod
    def parse_date(date_str: str) -> 'Date':
        if not DATE_REGEX_1.matches(date_str) and not DATE_REGEX_2.matches(date_str):
            raise ValueError('Date must match the format ####-##-## or ##-##-####')
        if DATE_REGEX_1.matches(date_str):
            matches: List[str] = NUMBER_REGEX.find_matches(date_str)
            return Date(int(matches[0]), int(matches[1]), int(matches[2]))
        elif DATE_REGEX_2.matches(date_str):
            matches: List[str] = NUMBER_REGEX.find_matches(date_str)
            return Date(int(matches[2]), int(matches[0]), int(matches[1]))

    @staticmethod
    def today() -> 'Date':
        today: date = date.today()
        return Date(today.year, today.month, today.day)

    @staticmethod
    def parse_time(time_rep: str) -> 'Date':
        consumer: Consumer = Consumer(time_rep)
        consumer.consume_through(' ')
        month: int = MONTHS[consumer.consume_to(' ')]
        consumer.consume_char(' ')
        day_of_month: int = int(consumer.consume_to(' '))
        consumer.consume_char(' ')
        consumer.consume_through(' ')
        year: int = int(consumer.consume_to_end())
        return Date(year, month, day_of_month)

    def __init__(self, year: int, month: int, day_of_month: int) -> None:
        self._year: int = year
        self._month: int = month
        self._day_of_month: int = day_of_month
        self._day_of_week: IntEnum = self._get_day_of_week()
        assert len(str(year)) == 4
        assert 1 <= month <= NUM_MONTHS
        assert self._day_is_valid()

    def __eq__(self, other: 'Date') -> bool:
        return self.year == other.year and self.month == other.month and self.day_of_month == other.day_of_month

    def __str__(self) -> str:
        return str(self.year) + '-' + String.pad_number(self.month, 2) + '-' + String.pad_number(self.day_of_month, 2)

    def __repr__(self) -> str:
        return self.__str__()

    def __lt__(self, other: 'Date') -> bool:
        if self.year == other.year:
            if self.month == other.month:
                if self.day_of_month == other.day_of_month:
                    return False
                return self.day_of_month < other.day_of_month
            return self.month < other.month
        return self.year < other.year

    def __le__(self, other: 'Date') -> bool:
        if self.year == other.year:
            if self.month == other.month:
                if self.day_of_month == other.day_of_month:
                    return True
                return self.day_of_month <= other.day_of_month
            return self.month <= other.month
        return self.year <= other.year

    def __gt__(self, other: 'Date') -> bool:
        if self.year == other.year:
            if self.month == other.month:
                if self.day_of_month == other.day_of_month:
                    return False
                return self.day_of_month > other.day_of_month
            return self.month > other.month
        return self.year > other.year

    def __ge__(self, other: 'Date') -> bool:
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

    def format(self, order: 'DateFormat', separator: str) -> str:
        if order == DateFormat.YMD:
            return str(self.year) + separator + String.pad_number(self.month, 2) + separator + String.pad_number(
                    self.day_of_month, 2)
        elif order == DateFormat.MDY:
            return String.pad_number(self.month, 2) + separator + String.pad_number(self.day_of_month,
                    2) + separator + str(self.year)

    def add_days(self, days: int) -> 'Date':
        cloned_date: Date = self.clone()
        for i in range(0, days):
            cloned_date = cloned_date.add_day()
        return cloned_date

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

    def subtract_days(self, days: int) -> 'Date':
        cloned_date: Date = self.clone()
        for i in range(0, days):
            cloned_date = cloned_date.subtract_day()
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


class DateFormat(IntEnum):
    YMD: int = 0
    MDY: int = 1
