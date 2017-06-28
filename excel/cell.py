class Cell:

    def __init__(self, cell):
        self._rep = cell

    def __str__(self):
        return self._rep.value

    def __repr__(self):
        return self.__str__()

    @property
    def value(self):
        return self._rep.value

    @value.setter
    def value(self, value):
        self._rep.value = value

    @property
    def font(self):
        return self._rep.font

    @font.setter
    def font(self, font):
        self._rep.font = font
