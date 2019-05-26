import os

from pathlib import Path
from typing import List

from cac.path.file import File


class Directory:

    @staticmethod
    def get_cwd() -> 'Directory':
        return Directory(os.getcwd())

    @staticmethod
    def _get_path(path: Path) -> str:
        return path.parts[0] + '\\'.join(path.parts[1:])

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
    def path(self) -> str:
        return self._rep.parts[0] + '\\'.join(self._rep.parts[1:])

    @property
    def parent_path(self) -> str:
        return self._rep.parts[0] + '\\'.join(self._rep.parts[1 : len(self._rep.parts) - 1])

    def exists(self) -> bool:
        return self._rep.exists()

    def contains_directory(self, directory_name: str) -> bool:
        return directory_name in self._rep.parts

    def join_directory(self, path: str) -> 'Directory':
        return Directory(self.path + '\\' + path)

    def join_file(self, path: str) -> File:
        return File(self.path + '\\' + path)

    def has_file(self, name: str) -> bool:
        return len([path for path in self.get_files() if path.name == name]) > 0

    def get_file(self, name: str) -> File:
        paths: List[File] = [path for path in self.get_files() if path.name == name]
        if len(paths) == 0:
            raise ValueError('Could not find file ' + name + ' in directory ' + self.path)
        return paths[0]

    def get_files(self) -> List[File]:
        return [File(self._get_path(child_path)) for child_path in self._rep.iterdir() if not child_path.is_dir()]

    def has_directory(self, name) -> bool:
        return len([directory for directory in self.get_directories() if directory.name == name]) != 0

    def get_directory(self, name: str) -> 'Directory':
        directories: List[Directory] = [directory for directory in self.get_directories() if directory.name == name]
        if len(directories) == 0:
            raise ValueError('Could not find file ' + name + ' in directory ' + self.path)
        return directories[0]

    def get_directories(self) -> List['Directory']:
        return [Directory(self._get_path(child_path)) for child_path in self._rep.iterdir() if child_path.is_dir()]

    def rename(self, name: str) -> None:
        new_path: str = self.parent_path + '\\' + name
        os.rename(self.path, new_path)

    def delete(self) -> None:
        os.remove(self.path)
