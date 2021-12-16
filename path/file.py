import os
import shutil
from pathlib import Path

import time
from cac.date import Date


class File:

    def __init__(self, path: str) -> None:
        self._rep: Path = Path(path)

    def __eq__(self, other: 'File') -> bool:
        return self.path == other.path

    def __hash__(self) -> int:
        return hash(self.path)

    def __str__(self) -> str:
        return self.path

    def __repr__(self) -> str:
        return self.__str__()

    @property
    def name(self) -> str:
        return self._rep.name

    @property
    def stem(self) -> str:
        return self._rep.stem

    @property
    def suffix(self) -> str:
        return self._rep.suffix

    @property
    def path(self) -> str:
        return self._rep.parts[0] + '\\'.join(self._rep.parts[1:])

    @property
    def directory_path(self) -> str:
        return self._rep.parts[0] + '\\'.join(self._rep.parts[1: len(self._rep.parts) - 1])

    def exists(self) -> bool:
        return self._rep.exists()

    def has_parent_directory(self, name: str) -> bool:
        return name in self._rep.parts[1:]

    def modified_date(self) -> Date:
        epoch_seconds: float = os.path.getmtime(self.path)
        modified_time: str = time.ctime(epoch_seconds)
        return Date.parse_time(modified_time)

    def rename(self, path: str) -> None:
        os.rename(self.path, path)

    def delete(self) -> None:
        os.remove(self.path)

    def copy(self, path: str) -> None:
        shutil.copyfile(self.path, path)
