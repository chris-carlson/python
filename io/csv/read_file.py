from custom.io.text.read_file import ReadFile as TextReadFile


class ReadFile:

    def __init__(self, file_name):
        self._file = TextReadFile(file_name)
        self._rows = []

    @property
    def rows(self):
        return self._rows

    def read_data(self):
        self._file.read_lines()
        self._rows = [[value for value in line.split('\"') if len(value) > 0 and value != ','] for line in
                      self._file.get_stripped_lines()]

    def get_row(self, num):
        if num >= len(self._rows):
            raise ValueError('The file does not have ' + str(num) + ' rows')
        return self._rows[num]

    def get_column(self, num):
        column = []
        for row in self._rows:
            if num >= len(row):
                raise ValueError('A row in the file does not have ' + str(num) + ' columns')
            column.append(row[num])
        return column

    def close(self):
        self._file.close()
