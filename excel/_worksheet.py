from custom.excel._row import Row

class Worksheet:

    def __init__(self, rep):
        self._rep = rep
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
        return self._rows[index]

    def load_data(self):
        for row in self._rep.rows:
            row = Row(row)
            row.load_data()
            self._rows.append(row)

    def get_title(self):
        return self._rep.title

    def set_title(self, title):
        self._rep.title = title

    def num_columns(self):
        length = -1
        for row in self._rows:
            if len(row) > length:
                length = len(row)
        return length

    def get_column_by_header(self, header):
        column_index = self.get_column_index(header)
        if column_index == -1:
            return []
        else:
            return self.get_column_by_index(column_index)[1:]

    def get_column_by_index(self, index):
        column = []
        for row in self._rows:
            column.append(row[index])
        return column

    def get_column_index(self, header):
        if len(self._rows) == 0:
            return -1
        for column_index in range(0, len(self._rows[0])):
            if self._rows[0][column_index].value == header:
                return column_index
        return -1

    def add_row(self, values):
        row = self._create_row()
        row.set_values(values)

    def insert_row(self, insert_index, values):
        self._create_row()
        for index in range(len(self._rows) - 2, insert_index - 1, -1):
            self._shift_row(index, 1)
        row = self._rows[insert_index]
        row.set_values(values)

    def replace_row(self, index, values):
        self._rows[index].set_values(values)

    def delete_row(self, delete_index):
        for index in range(delete_index + 1, len(self._rows)):
            self._shift_row(index, -1)
        self._rows.pop()

    def delete_rows(self, start_index, end_index=None):
        if end_index == None:
            end_index = len(self._rows)
        for index in range(start_index, end_index):
            self.delete_row(start_index)

    def clear_row(self, index):
        self._rows[index].clear_values()

    def clear_rows(self, start_index, end_index=None):
        if end_index == None:
            end_index = len(self._rows)
        for index in range(start_index, end_index):
            self.clear_row(index)

    def _create_row(self):
        cells = []
        for column_index in range(0, self.num_columns()):
            cells.append(self._rep.cell(row=len(self._rows) + 1, column=column_index + 1))
        row = Row(cells)
        self._rows.append(row)
        return row

    def _shift_row(self, index, offset):
        self._rows[index + offset].set_values(self._rows[index].get_values())
        self._rows[index].clear_values()
