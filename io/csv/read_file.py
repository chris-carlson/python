from custom.io.text.read_file import ReadFile as TextReadFile

class ReadFile:

    def __init__(self, file_name):
        self._file = TextReadFile(file_name)
        self._rows = []

    def __len__(self):
        return len(self._rows)

    def __iter__(self):
        for row in self._rows:
            yield row

    def __getitem__(self, index):
        if not type(index) == int:
            raise TypeError('Index \'' + index + '\' must be of integer type')
        if index < 0:
            raise IndexError('Index \'' + index + '\' must be positive')
        if index >= len(self._rows):
            raise IndexError('Index \'' + index + '\' must be less than the number of rows')
        return self._rows[num]

    def read_data(self):
        self._file.read_lines()
        self._rows = [[value for value in line.split('\"') if len(value) > 0 and value != ','] for line in self._file.get_stripped_lines()]

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
