class Cell:

    def __init__(self, cell):
        self._rep = cell

    def get_value(self):
        return self._rep.value

    def set_value(self, value):
        self._rep.value = value
