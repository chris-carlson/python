class Time:

    HOURS_IN_DAY = 24
    MINUTES_IN_HOUR = 60
    MERIDIEM = {'AM': 'AM', 'PM': 'PM'}

    def __init__(self, hour, minute, meridiem):
        self._hour = hour
        self._minute = minute
        self._meridiem = meridiem
        assert 0 < hour <= self.HOURS_IN_DAY / 2
        assert 0 <= minute < self.MINUTES_IN_HOUR
        assert meridiem in self.MERIDIEM

    def __eq__(self, other):
        return self._hour == other.hour and self._minute == other.minute and self._meridiem == other.meridiem

    def __str__(self):
        return self._pad_num(self._hour) + ':' + self._pad_num(self._minute) + ' ' + self._meridiem

    def __repr__(self):
        return self.__str__()

    @property
    def hour(self):
        return self._hour

    @property
    def minute(self):
        return self._minute

    @property
    def meridiem(self):
        return self._meridiem

    def add_minutes(self, minutes):
        for i in range(0, minutes):
            self.add_minute()

    def add_minute(self):
        self._minute += 1
        if self._minute > self.MINUTES_IN_HOUR:
            self._minute = 0
            self.add_hour()

    def add_hours(self, hours):
        for i in range(0, hours):
            self.add_hour()

    def add_hour(self):
        self._hour += 1
        if self._hour == self.HOURS_IN_DAY / 2:
            self._toggle_meridiem()
        if self._hour > self.HOURS_IN_DAY / 2:
            self._hour = 1

    def get_military_hour(self):
        if self._meridiem == self.MERIDIEM['PM']:
            if self._hour == self.HOURS_IN_DAY / 2:
                return self._hour
            return self._hour + int(self.HOURS_IN_DAY / 2)
        return self._hour

    def _calculate_meridiem(self):
        if self._hour < self.HOURS_IN_DAY / 2:
            return self.MERIDIEM['AM']
        return self.MERIDIEM['PM']

    def _toggle_meridiem(self):
        if self._meridiem == self.MERIDIEM['AM']:
            self._meridiem = self.MERIDIEM['PM']
        else:
            self._meridiem = self.MERIDIEM['AM']

    def _pad_num(self, num):
        if num < 10:
            return '0' + str(num)
        return str(num)
