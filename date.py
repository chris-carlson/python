from custom.regex import Regex

DATE_REGEX = Regex('\d{4}-\d{2}-\d{2}')

class Date:

    NUM_MONTHS = 12
    DAYS_IN_MONTHS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    LEAP_MONTH = 2
    LEAP_YEAR_FREQUENCY = 4

    @staticmethod
    def parse_date(date_str):
        if not DATE_REGEX.matches(date_str):
            raise ValueError('Date must match the format ####-##-##')
        first_dash = date_str.find('-')
        second_dash = date_str.find('-', first_dash + 1)
        year = int(date_str[:first_dash])
        month = int(date_str[first_dash + 1 : second_dash])
        day = int(date_str[second_dash + 1:])
        return Date(year, month, day)

    def __init__(self, year, month, day):
        self._year = year
        self._month = month
        self._day = day
        assert len(str(year)) == 4
        assert 1 <= month <= self.NUM_MONTHS
        assert self._day_is_valid()

    def __eq__(self, other):
        return self._year == other.year and self._month == other.month and self._day == other.day

    def __str__(self):
        return str(self._year) + '-' + self._pad_num(self._month) + '-' + self._pad_num(self._day)

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
    def day(self):
        return self._day

    def clone(self):
        return Date(self.year, self.month, self.day)

    def add_day(self):
        self._day += 1
        if self._day > self._get_days_in_current_month():
            self._month += 1
            if self._month > self.NUM_MONTHS:
                self._month = 1
                self._year += 1
            self._day = 1

    def add_days(self, days):
        for i in range(0, days):
            self.add_day()

    def subtract_day(self):
        self._day -= 1
        if self._day < 1:
            self._month -= 1
            if self._month < 1:
                self._month = self.NUM_MONTHS
                self._year -= 1
            self._day = self._get_days_in_current_month()

    def subtract_days(self, days):
        for i in range(0, days):
            self.subtract_day()

    def get_days_to(self, date):
        copied_date = date.clone()
        num_days = 0
        while self < copied_date:
            copied_date.subtract_day()
            num_days += 1
        while self > copied_date:
            copied_date.add_day()
            num_days -= 1
        return num_days

    def _get_days_in_current_month(self):
        if self._month == self.LEAP_MONTH and self._is_leap_year():
            return self.DAYS_IN_MONTHS[self.LEAP_MONTH - 1] + 1
        return self.DAYS_IN_MONTHS[self._month - 1]

    def _is_leap_year(self):
        return self._year % self.LEAP_YEAR_FREQUENCY == 0 and (self._year % (self.LEAP_YEAR_FREQUENCY * 25) != 0 or self._year % (self.LEAP_YEAR_FREQUENCY * 100) == 0)

    def _day_is_valid(self):
        return 1 <= self._day <= self._get_days_in_current_month()

    def _pad_num(self, num):
        if num < 10:
            return '0' + str(num)
        return str(num)
