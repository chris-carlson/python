import os

from pathlib import Path
from typing import List

from cac.finder import Finder
from cac.ignore import Ignore
from cac.path.file import File
from cac.regex import Regex


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

    def join_directory(self, path: str, extension: str = '') -> 'Directory':
        return Directory(self.path + '\\' + path + extension)

    def join_file(self, path: str, extension: str = '') -> File:
        return File(self.path + '\\' + path + extension)

    def has_file(self, name: str) -> bool:
        return len([path for path in self.get_files() if path.name == name]) > 0

    def get_file(self, name: str) -> File:
        return Finder.find_only([file_ for file_ in self.get_files() if file_.name == name])

    def get_files(self, regex: Regex = None) -> List[File]:
        files: List[File] = []
        for native_path in self._rep.iterdir():
            if not native_path.is_dir():
                wrapper_path: str = Directory._get_path(native_path)
                if regex is None or regex.matches(wrapper_path):
                    files.append(File(wrapper_path))
        return files

    def find_file(self, name: str) -> File:
        return Finder.find_only([file_ for file_ in self.find_files() if file_.name == name])

    def find_files(self, regex: Regex = None) -> List[File]:
        files: List[File] = self.get_files(regex)
        for sub_directory in self.get_directories():
            if sub_directory.name not in Ignore.DIRECTORIES:
                files.extend(sub_directory.find_files(regex))
        return files

    def has_directory(self, name) -> bool:
        return len([directory for directory in self.get_directories() if directory.name == name]) != 0

    def get_directory(self, name: str) -> 'Directory':
        return Finder.find_only([directory for directory in self.get_directories() if directory.name == name])

    def get_directories(self, regex: Regex = None) -> List['Directory']:
        directories: List[File] = []
        for native_path in self._rep.iterdir():
            if native_path.is_dir():
                wrapper_path: str = Directory._get_path(native_path)
                if regex is None or regex.matches(wrapper_path):
                    directories.append(Directory(wrapper_path))
        return directories

    def find_directory(self, name: str) -> 'Directory':
        return Finder.find_only([directory for directory in self.find_directories() if directory.name == name])

    def find_directories(self, regex: Regex = None) -> List['Directory']:
        directories: List[File] = self.get_directories(regex)
        for sub_directory in self.get_directories():
            if sub_directory.name not in Ignore.DIRECTORIES:
                directories.extend(sub_directory.find_directories(regex))
        return directories

    def rename(self, name: str) -> None:
        new_path: str = self.parent_path + '\\' + name
        os.rename(self.path, new_path)

    def delete(self) -> None:
        os.remove(self.path)
