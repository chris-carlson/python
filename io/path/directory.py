from pathlib import Path


class Directory:

    def __init__(self, path):
        self._rep = Path(path)

    def __str__(self):
        return self.path

    def __repr__(self):
        return self.__str__()

    @property
    def name(self):
        return self._rep.name

    @property
    def path(self):
        return self._rep.parts[0] + '\\'.join(self._rep.parts[1:])

    def exists(self):
        return self._rep.exists()

    def contains_directory(self, directory_name):
        return directory_name in self._rep.parts

    def join(self, path):
        return Path(self.path + '\\' + path)

    def has_file(self, name):
        return len([path for path in self.get_files() if path.name == name]) > 0

    def get_file(self, name):
        paths = [path for path in self.get_files() if path.name == name]
        if len(paths) == 0:
            raise ValueError('Could not find file ' + name + ' in directory ' + self.path)
        return paths[0]

    def get_files(self):
        return [Path(child_path) for child_path in self._rep.iterdir() if not child_path.is_dir()]

    def has_directory(self, name):
        return len([directory for directory in self.get_directories() if directory.name == name]) != 0

    def get_directory(self, name):
        directories = [directory for directory in self.get_directories() if directory.name == name]
        if len(directories) == 0:
            raise ValueError('Could not find file ' + name + ' in directory ' + self.path)
        return directories[0]

    def get_directories(self):
        return [Path(child_path) for child_path in self._rep.iterdir() if child_path.is_dir()]
