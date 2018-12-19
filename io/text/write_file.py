class WriteFile:

    def __init__(self, file_name, append=False):
        mode = 'a' if append else 'w'
        self._file = open(file_name, mode=mode, encoding='utf-8', newline='\n')

    def write(self, str_):
        self._file.write(str(str_))

    def write_line(self, str_=''):
        self._file.write(str(str_) + '\n')

    def write_iterable(self, iterable):
        for item in iterable:
            self._file.write(str(item) + '\n')

    def close(self):
        self._file.close()
