from custom.date.day_of_week import DayOfWeek
from custom.math import Math
from custom.regex import Regex

DATE_REGEX = Regex('\d{4}\D\d{2}\D\d{2}')
NUMBER_REGEX = Regex('\d+')
NUM_MONTHS = 12
DAYS_IN_MONTHS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
DAYS_IN_WEEK = 7
LEAP_MONTH = 2
LEAP_YEAR_FREQUENCY = 4

class Date:

    @staticmethod
    def parse_date(date_str):
        if not DATE_REGEX.matches(date_str):
            raise ValueError('Date must match the format ####-##-##')
        matches = NUMBER_REGEX.find_matches(date_str)
        return Date(int(matches[0]), int(matches[1]), int(matches[2]))

    def __init__(self, year, month, day_of_month):
        self._year = year
        self._month = month
        self._day_of_month = day_of_month
        self._day_of_week = self._get_day_of_week()
        assert len(str(year)) == 4
        assert 1 <= month <= NUM_MONTHS
        assert self._day_is_valid()

    def __eq__(self, other):
        return self._year == other.year and self._month == other.month and self._day_of_month == other.day

    def __str__(self):
        return self._day_of_week.name.capitalize() + ' ' + str(self._year) + '/' + self._pad_num(self._month) + '/' + self._pad_num(self._day_of_month)

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        if self.year == other.year:
            if self.month == other.month:
                if self.day == other.day:
                    return False
                return self.day < other.day
            return self.month < other.month
        return self.year < other.year

    def __le__(self, other):
        if self.year == other.year:
            if self.month == other.month:
                if self.day == other.day:
                    return True
                return self.day <= other.day
            return self.month <= other.month
        return self.year <= other.year

    def __gt__(self, other):
        if self.year == other.year:
            if self.month == other.month:
                if self.day == other.day:
                    return False
                return self.day > other.day
            return self.month > other.month
        return self.year > other.year

    def __ge__(self, other):
        if self.year == other.year:
            if self.month == other.month:
                if self.day == other.day:
                    return True
                return self.day >= other.day
            return self.month >= other.month
        return self.year >= other.year

    @property
    def year(self):
        return self._year

    @property
    def month(self):
        return self._month

    @property
    def day_of_month(self):
        return self._day_of_month

    @property
    def day_of_week(self):
        return self._day_of_week

    def add_day(self):
        date = self._clone()
        date._day_of_month += 1
        if date._day_of_month > date._get_days_in_current_month():
            date._month += 1
            if date._month > NUM_MONTHS:
                date._month = 1
                date._year += 1
            date._day_of_month = 1
        date._day_of_week = DayOfWeek((date._day_of_week.value + 1) % DAYS_IN_WEEK)
        return date

    def add_days(self, days):
        date = self._clone()
        for i in range(0, days):
            date = date.add_day()
        return date

    def subtract_day(self):
        date = self._clone()
        date._day_of_month -= 1
        if date._day_of_month < 1:
            date._month -= 1
            if date._month < 1:
                date._month = NUM_MONTHS
                date._year -= 1
            date._day_of_month = date._get_days_in_current_month()
        date._day_of_week = DayOfWeek((date._day_of_week.value - 1) % DAYS_IN_WEEK)
        return date

    def subtract_days(self, days):
        date = self._clone()
        for i in range(0, days):
            date = date.subtract_day()
        return date

    def get_days_to(self, date):
        copied_date = date.clone()
        num_days = 0
        while self < copied_date:
            copied_date = copied_date.subtract_day()
            num_days += 1
        while self > copied_date:
            copied_date = copied_date.add_day()
            num_days -= 1
        return num_days

    def _clone(self):
        return Date(self._year, self._month, self._day_of_month)

    def _get_day_of_week(self):
        new_month = Math.one_based_mod(self._month, -2, 12)
        first_two_digits_of_year = int(str(self._year)[:2])
        last_two_digits_of_year = int(str(self._year)[2:])
        if new_month > 10:
            last_two_digits_of_year -= 1
        return DayOfWeek((self._day_of_month + int((13 * new_month - 1) / 5) + last_two_digits_of_year + int(last_two_digits_of_year / 4) + int(first_two_digits_of_year / 4) - 2 * first_two_digits_of_year) % 7)

    def _get_days_in_current_month(self):
        if self._month == LEAP_MONTH and self._is_leap_year():
            return DAYS_IN_MONTHS[LEAP_MONTH - 1] + 1
        return DAYS_IN_MONTHS[self._month - 1]

    def _is_leap_year(self):
        return self._year % LEAP_YEAR_FREQUENCY == 0 and (self._year % (LEAP_YEAR_FREQUENCY * 25) != 0 or self._year % (LEAP_YEAR_FREQUENCY * 100) == 0)

    def _day_is_valid(self):
        return 1 <= self._day_of_month <= self._get_days_in_current_month()

    def _pad_num(self, num):
        return '0' + str(num) if num < 10 else str(num)
