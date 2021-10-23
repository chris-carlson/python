import os
import shutil
from pathlib import Path
from typing import List

from cac.finder import Finder
from cac.path.file import File
from cac.regex import Regex


def get_name(path: Path) -> str:
    return path.parts[-1]


def get_path(path: Path) -> str:
    return path.parts[0] + '\\'.join(path.parts[1:])


def is_directory_valid(directory_name: str, ignored_directories: List[Regex], regex: Regex = None) -> bool:
    ignore_matches: List[Regex] = []
    if ignored_directories is not None:
        ignore_matches = [directory_regex for directory_regex in ignored_directories if
                directory_regex.matches(directory_name)]
    not_ignored: bool = ignored_directories is None or len(ignore_matches) == 0
    matches_regex: bool = regex is None or regex.matches(directory_name)
    return not_ignored and matches_regex


def is_file_valid(file_name: str, ignored_files: List[Regex], regex: Regex = None) -> bool:
    ignore_matches: List[Regex] = []
    if ignored_files is not None:
        ignore_matches = [file_regex for file_regex in ignored_files if file_regex.matches(file_name)]
    not_ignored: bool = ignored_files is None or len(ignore_matches) == 0
    matches_regex: bool = regex is None or regex.matches(file_name)
    return not_ignored and matches_regex


class Directory:

    @staticmethod
    def get_cwd() -> 'Directory':
        return Directory(os.getcwd())

    @staticmethod
    def get_environment_directory(environment_variable: str) -> 'Directory':
        return Directory(os.environ[environment_variable])

    def __init__(self, path: str) -> None:
        self._rep: Path = Path(path)

    def __eq__(self, other: 'Directory') -> bool:
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
    def path(self) -> str:
        return self._rep.parts[0] + '\\'.join(self._rep.parts[1:])

    @property
    def parent_path(self) -> str:
        return self._rep.parts[0] + '\\'.join(self._rep.parts[1: len(self._rep.parts) - 1])

    def exists(self) -> bool:
        return self._rep.exists()

    def contains_directory(self, directory_name: str) -> bool:
        return directory_name in self._rep.parts

    def join_directory(self, path: str) -> 'Directory':
        return Directory(self.path + '\\' + path)

    def join_directories(self, paths: List[str]) -> 'Directory':
        directory: Directory = Directory(self.path)
        for path in paths:
            directory = directory.join_directory(path)
        return directory

    def join_file(self, path: str, extension: str = '') -> File:
        return File(self.path + '\\' + path + extension)

    def has_file(self, name: str) -> bool:
        return len([path for path in self.get_files() if path.name == name]) > 0

    def get_file(self, name: str) -> File:
        return Finder.find_only([file_ for file_ in self.get_files() if file_.name == name])

    def get_files(self, ignore_files: List[Regex] = None, regex: Regex = None) -> List[File]:
        files: List[File] = []
        for native_path in self._rep.iterdir():
            if not native_path.is_dir():
                file_name: str = get_name(native_path)
                wrapper_path: str = get_path(native_path)
                if is_file_valid(file_name, ignore_files, regex):
                    files.append(File(wrapper_path))
        return files

    def find_file(self, name: str, ignored_directories: List[Regex] = None) -> File:
        return Finder.find_only([file_ for file_ in self.find_files(ignored_directories) if file_.name == name])

    def find_files(self, ignored_directories: List[Regex] = None, ignore_files: List[Regex] = None,
            regex: Regex = None) -> List[File]:
        files: List[File] = self.get_files(ignore_files, regex)
        for sub_directory in self.get_directories():
            if is_directory_valid(sub_directory.name, ignored_directories):
                files.extend(sub_directory.find_files(ignored_directories, ignore_files, regex))
        return files

    def has_directory(self, name) -> bool:
        return len([directory for directory in self.get_directories() if directory.name == name]) != 0

    def get_directory(self, name: str) -> 'Directory':
        return Finder.find_only([directory for directory in self.get_directories() if directory.name == name])

    def get_directories(self, ignored_directories: List[Regex] = None, regex: Regex = None) -> List['Directory']:
        directories: List[Directory] = []
        for native_path in self._rep.iterdir():
            if native_path.is_dir():
                directory_name: str = get_name(native_path)
                wrapper_path: str = get_path(native_path)
                if is_directory_valid(directory_name, ignored_directories, regex):
                    directories.append(Directory(wrapper_path))
        return directories

    def find_directory(self, name: str, ignored_directories: List[Regex] = None, regex: Regex = None) -> 'Directory':
        return Finder.find_only([directory for directory in self.find_directories(ignored_directories, regex) if
                directory.name == name])

    def find_directories(self, ignored_directories: List[Regex] = None, regex: Regex = None) -> List['Directory']:
        directories: List[Directory] = self.get_directories(ignored_directories, regex)
        for sub_directory in directories:
            if is_directory_valid(sub_directory.name, ignored_directories, regex):
                directories.extend(sub_directory.find_directories(ignored_directories, regex))
        return directories

    def rename(self, name: str) -> None:
        new_path: str = self.parent_path + '\\' + name
        os.rename(self.path, new_path)

    def delete(self) -> None:
        shutil.rmtree(self.path)

    def copy(self, path: str) -> None:
        shutil.copytree(self.path, path)
