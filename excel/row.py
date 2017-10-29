from custom.excel.cell import Cell

class Row:

    def __init__(self, rep=None):
        self._rep = rep
        self._cells = []
        for cell in self._rep:
            self._cells.append(Cell(cell))

    def __str__(self):
        return '[' + ', '.join(self._cells) + ']'

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return len(self._cells)

    def __iter__(self):
        for cell in self._cells:
            yield cell

    def __getitem__(self, index):
        return self._cells[index]

    def is_blank(self):
        is_blank = True
        for cell in self._cells:
            if cell.get_value() != None:
                is_blank = False
        return is_blank

    def get_values(self):
        values = []
        for cell in self._cells:
            values.append(cell.get_value())
        return values

    def set_values(self, values):
        for index in range(0, len(values)):
            self._cells[index].set_value(values[index])

    def clear_values(self):
        for cell in self._cells:
            cell.set_value(None)
