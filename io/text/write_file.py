class WriteFile():

    def __init__(self, file_name):
        self._file = open(file_name, 'w')

    def write(self, str_):
        self._file.write(str(str_))

    def write_line(self, str_=''):
        self._file.write(str(str_) + '\n')

    def close(self):
        self._file.close()
