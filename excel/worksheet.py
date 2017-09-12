from custom.excel.row import Row

class Worksheet:

    def __init__(self, worksheet):
        self._rep = worksheet
        self._rows = []
        if len(worksheet.get_cell_collection()) > 0:
            for row in worksheet:
                self._rows.append(Row(row))

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return len(self._rows)

    def __iter__(self):
        for row in self._rows:
            yield row

    def __getitem__(self, index):
        return self._rows[index]

    @property
    def title(self):
        return self._rep.title

    @title.setter
    def title(self, title):
        self._rep.title = title

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

    def write_row(self, values, row_index=None):
        if row_index == None:
            row_index = len(self._rows)
        column_index = 0
        for value in values:
            self._rep.cell(row=row_index + 1, column=column_index + 1, value=value)
            column_index += 1
        row = self._rep[str(row_index + 1)]
        self._rows.insert(row_index, Row(row))

    def clear_rows(self, start_index, end_index=None):
        if end_index == None:
            end_index = len(self._rows)
        for index in range(start_index, end_index):
            for cell in self._rows[index]:
                cell.value = None
