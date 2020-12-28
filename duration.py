class Duration:

    def __init__(self, hours: int, minutes: int, seconds: int) -> None:
        self._hours: int = hours
        self._minutes: int = minutes
        self._seconds: int = seconds

    def reduce(self, round_up: bool = False) -> 'Duration':
        while self._seconds >= 60:
            self._seconds -= 60
            self._minutes += 1
        if round_up and self._seconds > 0:
            self._minutes += 1
        while self._minutes >= 60:
            self._minutes -= 60
            self._hours += 1
