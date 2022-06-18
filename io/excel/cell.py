class Cell:

    def __init__(self, value: object, bold: bool = False) -> None:
        self._value: object = value
        self._bold: bool = bold

    def __str__(self) -> str:
        return str(self._value)

    def __repr__(self) -> str:
        return self.__str__()

    @property
    def value(self) -> object:
        return self._value

    @property
    def bold(self) -> bool:
        return self._bold
