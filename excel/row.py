from custom.excel.cell import Cell

class Row:

    def __init__(self, row):
        self._rep = row
        self._cells = []
        for cell in row:
            self._cells.append(Cell(cell))

    def __str__(self):
        str_ = '['
        for i in range(0, len(self._cells)):
            cell = self._cells[i]
            str_ += str(cell.value)
            if i < len(self._cells) - 1:
                str_ += ', '
        str_ += ']'
        return str_

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return len(self._cells)

    def __iter__(self):
        for cell in self._cells:
            yield cell

    def __getitem__(self, index):
        return self._cells[index]

    def set_values(self, *values):
        for value_index in range(0, len(values)):
            value = values[value_index]
            cell = self._cells[value_index]
            cell.set_value(value)

    def set_font(self, font):
        for cell in self._cells:
            cell.font = font
