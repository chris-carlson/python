from pathlib import Path

from custom.file_.file_ import File

class Directory(File):

    def has_file(self, name):
        return len([file_ for file_ in self.get_files() if file_.name == name]) > 0

    def get_file(self, name):
        files = [file_ for file_ in self.get_files() if file_.name == name]
        if len(files) == 0:
            raise ValueError('Could not find file ' + name + ' in directory ' + self.path)
        return files[0]

    def get_files(self):
        return [File(child_path) for child_path in self._rep.iterdir() if not child_path.is_dir()]

    def has_directory(self, name):
        return len([directory for directory in self.get_directories() if directory.name == name]) != 0

    def get_directory(self, name):
        directories = [directory for directory in self.get_directories() if directory.name == name]
        if len(directories) == 0:
            raise ValueError('Could not find file ' + name + ' in directory ' + self.path)
        return directories[0]

    def get_directories(self):
        return [Directory(child_path) for child_path in self._rep.iterdir() if child_path.is_dir()]
