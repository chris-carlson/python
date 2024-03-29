from typing import List

from cac.regex import Regex
from cac.text import Text

NUMBER_REGEX: Regex = Regex(r'\d+')

class Duration:
    DURATION_REGEX: Regex = Regex(r'(\d+:)?\d+:\d+')

    # noinspection PyArgumentEqualDefault
    @staticmethod
    def parse_duration(rep: str) -> 'Duration':
        if not Duration.DURATION_REGEX.matches(rep):
            raise ValueError('Duration must match the correct format')
        matches: List[str] = NUMBER_REGEX.find_matches(rep)
        if len(matches) == 2:
            return Duration(0, int(matches[0]), int(matches[1]))
        return Duration(int(matches[0]), int(matches[1]), int(matches[2]))

    def __init__(self, hours: int = 0, minutes: int = 0, seconds: int = 0) -> None:
        self._hours: int = hours
        self._minutes: int = minutes
        self._seconds: int = seconds

    def __eq__(self, other: 'Duration') -> bool:
        return self.hours == other.hours and self.minutes == other.minutes and self.seconds == other.seconds

    def __str__(self) -> str:
        return Text.pad_number(self.hours, 2) + ':' + Text.pad_number(self.minutes, 2) + ':' + Text.pad_number(
            self.seconds, 2)

    def __repr__(self) -> str:
        return self.__str__()

    def __lt__(self, other: 'Duration') -> bool:
        reduced_self: Duration = self.reduce()
        reduced_other: Duration = other.reduce()
        if reduced_self.hours == reduced_other.hours:
            if reduced_self.minutes == reduced_other.minutes:
                if reduced_self.seconds == reduced_other.seconds:
                    return False
                return reduced_self.seconds < reduced_other.seconds
            return reduced_self.minutes < reduced_other.minutes
        return reduced_self.hours < reduced_other.hours

    def __le__(self, other: 'Duration') -> bool:
        reduced_self: Duration = self.reduce()
        reduced_other: Duration = other.reduce()
        if reduced_self.hours == reduced_other.hours:
            if reduced_self.minutes == reduced_other.minutes:
                if reduced_self.seconds == reduced_other.seconds:
                    return False
                return reduced_self.seconds <= reduced_other.seconds
            return reduced_self.minutes <= reduced_other.minutes
        return reduced_self.hours <= reduced_other.hours

    def __gt__(self, other: 'Duration') -> bool:
        reduced_self: Duration = self.reduce()
        reduced_other: Duration = other.reduce()
        if reduced_self.hours == reduced_other.hours:
            if reduced_self.minutes == reduced_other.minutes:
                if reduced_self.seconds == reduced_other.seconds:
                    return False
                return reduced_self.seconds > reduced_other.seconds
            return reduced_self.minutes > reduced_other.minutes
        return reduced_self.hours > reduced_other.hours

    def __ge__(self, other: 'Duration') -> bool:
        reduced_self: Duration = self.reduce()
        reduced_other: Duration = other.reduce()
        if reduced_self.hours == reduced_other.hours:
            if reduced_self.minutes == reduced_other.minutes:
                if reduced_self.seconds == reduced_other.seconds:
                    return False
                return reduced_self.seconds >= reduced_other.seconds
            return reduced_self.minutes >= reduced_other.minutes
        return reduced_self.hours >= reduced_other.hours

    @property
    def hours(self) -> int:
        return self._hours

    @property
    def minutes(self) -> int:
        return self._minutes

    @property
    def seconds(self) -> int:
        return self._seconds

    def add(self, segment_duration: 'Duration') -> 'Duration':
        full_duration: Duration = self._copy()
        full_duration._hours += segment_duration.hours
        full_duration._minutes += segment_duration.minutes
        full_duration._seconds += segment_duration.seconds
        return full_duration.reduce()

    def subtract(self, segment_duration: 'Duration') -> 'Duration':
        full_duration: Duration = self._copy()
        full_duration._hours -= segment_duration.hours
        full_duration._minutes -= segment_duration.minutes
        full_duration._seconds -= segment_duration.seconds
        while full_duration._seconds < 0:
            full_duration._seconds += 60
            full_duration._minutes -= 1
        while full_duration._minutes < 0:
            full_duration._minutes += 60
            full_duration._hours -= 1
        if full_duration._hours < 0:
            raise ValueError('Hours cannot be negative')
        return full_duration.reduce()

    def divide(self, number: float) -> 'Duration':
        expanded_duration: Duration = self._expand()
        divided_seconds: int = round(expanded_duration.seconds / number)
        divided_duration: Duration = Duration(0, 0, divided_seconds)
        return divided_duration.reduce()

    def reduce(self, round_up: bool = False) -> 'Duration':
        duration: Duration = self._copy()
        while duration._seconds >= 60:
            duration._seconds -= 60
            duration._minutes += 1
        if round_up and duration._seconds > 0:
            duration._minutes += 1
        while duration._minutes >= 60:
            duration._minutes -= 60
            duration._hours += 1
        return duration

    def _expand(self) -> 'Duration':
        duration: Duration = self._copy()
        while duration._hours > 0:
            duration._minutes += 60
            duration._hours -= 1
        while duration._minutes > 0:
            duration._seconds += 60
            duration._minutes -= 1
        return duration

    def _copy(self) -> 'Duration':
        return Duration(self.hours, self.minutes, self.seconds)
