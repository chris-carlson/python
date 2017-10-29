from pathlib import Path

class File:

    def __init__(self, path):
        self._rep = Path(path)

    def __str__(self):
        return self.path

    def __repr__(self):
        return self.__str__()

    @property
    def path(self):
        return self._rep.parts[0] + '\\'.join(self._rep.parts[1:])

    @property
    def name(self):
        return self._rep.name

    @property
    def stem(self):
        return self._rep.stem

    @property
    def suffix(self):
        return self._rep.suffix

    def join(self, path):
        self._rep.joinpath(path)

    def get_renamed_name(self, old_str, new_str):
        return self._rep.parts[0] + '\\'.join(self._rep.parts[1:len(self._rep.parts) - 1]) + '\\' + self._rep.name.replace(old_str, new_str)
