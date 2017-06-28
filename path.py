from pathlib import Path as PathLibPath

class Path:

    def __init__(self, path):
        self._rep = PathLibPath(path)

    @property
    def name(self):
        return self._rep.name

    def get_directories(self):
        directories = []
        for child_path in self._rep.iterdir():
            if child_path.is_dir():
                directories.append(Path(child_path))
        return directories

    def get_files(self):
        files = []
        for child_path in self._rep.iterdir():
            if not child_path.is_dir():
                files.append(child_path.name)
        return files
