import time


class Timer:

    def __init__(self) -> None:
        self._start: float = 0.0
        self._stop: float = 0.0

    def start(self) -> None:
        self._start = time.time()

    def stop(self) -> None:
        self._stop = time.time()

    def get_time(self) -> float:
        if self._start == 0 or self._stop == 0 or self._start > self._stop:
            raise ValueError('Timer has not been started and stopped')
        return self._stop - self._start
