from pathlib import Path

from custom.file_.file_ import File

class Directory(File):
    def get_file(self, name):
        files = self.get_files()
        for file_ in files:
            if file_.name == name:
                return file_
        raise ValueError('Could not find file ' + name + ' in directory ' + self.path)

    def get_directory(self, name):
        directories = self.get_directories()
        for directory in directories:
            if directory.name == name:
                return directory
        raise ValueError('Could not find directory ' + name + ' in directory ' + self.path)

    def get_directories(self):
        directories = []
        for child_path in self._rep.iterdir():
            if child_path.is_dir():
                directories.append(Directory(child_path))
        return directories

    def get_files(self):
        files = []
        for child_path in self._rep.iterdir():
            if not child_path.is_dir():
                files.append(File(child_path))
        return files
