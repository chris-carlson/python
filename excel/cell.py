class Cell:

    def __init__(self, cell):
        self._rep = cell

    def __str__(self):
        return str(self._rep.value)

    def __repr__(self):
        return self.__str__()

    def get_value(self):
        return self._rep.value

    def set_value(self, value):
        self._rep.value = value
