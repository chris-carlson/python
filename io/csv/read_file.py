from custom.file_.read_file import ReadFile

class ReadFile:

    def __init__(self, file_name):
        self._file = ReadFile(file_name)
        self._rows = []

    def __str__(self):
        str_ = '['
        for rowIndex in range(0, len(self._rows)):
            row = self._rows[rowIndex]
            str_ += '['
            for columnIndex in range(0, len(row)):
                column = row[columnIndex]
                str_ += str(column)
                if columnIndex < len(row):
                    str_ += ', '
            str_ += ']'
            if rowIndex < len(self._rows):
                str_ += ', '
        str_ += ']'
        return str_

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return len(self._rows)

    def __iter__(self):
        for row in self._rows:
            yield row

    def __getitem__(self, num):
        return self._rows[num]

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

    def read_values(self):
        self._file.read_lines()
        for line in self._file.get_stripped_lines():
            line_values = []
            split_values = line.split(',')
            for split_value in split_values:
                line_values.append(split_value)
            self._rows.append(line_values)
