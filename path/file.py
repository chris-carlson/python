import os
import shutil

from pathlib import Path


class File:

    def __init__(self, path: str) -> None:
        self._rep: Path = Path(path)

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

    def rename(self, name: str) -> None:
        new_path: str = self.directory_path + '\\' + name
        os.rename(self.path, new_path)

    def delete(self) -> None:
        os.remove(self.path)

    def copy(self, path: str) -> None:
        shutil.copyfile(self.path, path)
