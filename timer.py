import time

class Timer:

    def __init__(self) -> None:
        self._start: float = 0.0
        self._end: float = 0.0

    def start(self) -> None:
        self._start = time.time()

    def end(self) -> None:
        self._end = time.time()

    def get_time(self) -> float:
        if self._start == 0 or self._end == 0 or self._start > self._end:
            raise ValueError('Timer has not been started and stopped')
        return self._end - self._start
